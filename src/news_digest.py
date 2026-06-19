from __future__ import annotations

import os
import json
import asyncio
from datetime import datetime, timedelta
from typing import Dict, List, Any

from src.inventory_manager import load_inventory
from src.gemini_utils import call_gemini_with_retry
from src.config import MADRID_TZ
from src.logger import log_event

DIGEST_OUTPUT_PATH = "data/news_digest.json"


class NewsDigestEngine:
    """Generates a curated news digest by filtering inventory entries by
    recency and using Gemini AI to rank the most relevant ones per category.

    Three time windows (3 / 6 / 12 months) are produced in a single run.
    Each window contains up to 10 AI-ranked items per digest category.
    """

    # ------------------------------------------------------------------ #
    # 26 Digest Categories – mapped from V2 category slugs               #
    # ------------------------------------------------------------------ #
    DIGEST_CATEGORIES: Dict[str, List[str]] = {
        # --- TECH CORE (9) ---
        "Kubernetes & Orchestration": [
            "kubernetes", "kubernetes-tools", "kubernetes-tutorials",
            "kubectl-commands", "kubernetes-releases", "kubernetes-autoscaling",
            "kubernetes-operators-controllers", "kubernetes-based-devel",
            "kubernetes-alternatives", "kubernetes-client-libraries",
            "kubernetes-bigdata", "managed-kubernetes-in-public-cloud", "helm",
        ],
        "Containers & Runtime": [
            "docker", "container-managers", "serverless", "noops", "registries",
        ],
        "Networking & Service Mesh": [
            "networking", "kubernetes-networking", "servicemesh", "istio",
            "caching", "web-servers", "cloudflare",
        ],
        "Architecture & Microservices": [
            "introduction", "faq", "cloud-arch-diagrams", "matrix-table",
            "other-awesome-lists", "about",
        ],
        "Data, Messaging & Storage": [
            "databases", "nosql", "newsql", "message-queue", "crunchydata",
            "yaml", "kubernetes-storage", "kubernetes-backup-migrations",
        ],
        "AI & Agents": [
            "ai", "ai-agents-mcp", "chatgpt",
        ],
        "MLOps & Data Science": [
            "mlops",
        ],
        "Python, Java & Developer Ecosystem": [
            "python", "golang", "java_frameworks", "java_app_servers",
            "java-and-java-performance-optimization", "javascript", "dotnet",
            "angular", "react", "web3", "api",
            "swagger-code-generator-for-rest-apis", "postman",
            "lowcode-nocode", "devel-sites", "dom", "linux-dev-env",
            "ChromeDevTools", "xamarin", "jvm-parameters-matrix-table",
            "maven-gradle", "embedded-servlet-containers", "visual-studio",
        ],
        "Linux & System Foundations": [
            "linux", "git",
        ],
        # --- PLATFORM & OPS (8) ---
        "Security & Compliance": [
            "securityascode", "kubernetes-security", "aws-security", "oauth",
            "devsecops",
        ],
        "Infrastructure as Code": [
            "iac", "terraform", "pulumi", "crossplane", "ansible",
            "kustomize", "chef", "liquibase",
        ],
        "CI/CD & GitOps": [
            "cicd", "gitops", "argo", "flux", "tekton", "jenkins",
            "jenkins-alternatives", "sonarqube", "cicd-kubernetes-plugins",
            "openshift-pipelines", "stackstorm", "keptn",
        ],
        "Observability, SRE & Testing": [
            "sre", "monitoring", "prometheus", "grafana",
            "kubernetes-monitoring", "chaos-engineering", "qa",
            "test-automation-frameworks", "testops",
            "performance-testing-with-jenkins-and-jmeter",
            "kubernetes-troubleshooting",
        ],
        "DevOps & Culture": [
            "devops", "devops-tools", "project-management-methodology",
            "project-management-tools",
        ],
        "Platform Engineering & DevEx": [
            "developerportals", "scaffolding", "mkdocs",
        ],
        "FinOps & Cloud Cost": [
            "finops", "aws-pricing",
        ],
        "Certification & Training": [
            "elearning", "interview-questions", "aws-training", "cheatsheets",
            "demos",
        ],
        # --- CLOUD & ENTERPRISE (5) ---
        "AWS": [
            "aws", "aws-architecture", "aws-security", "aws-networking",
            "aws-databases", "aws-storage", "aws-monitoring", "aws-iac",
            "aws-tools-scripts", "aws-messaging", "aws-data", "aws-devops",
            "aws-serverless", "aws-containers", "aws-backup",
            "aws-newfeatures", "aws-miscellaneous", "aws-spain",
        ],
        "Azure": [
            "azure",
        ],
        "GCP, OCI & Others": [
            "GoogleCloudPlatform", "ibm_cloud", "oraclecloud",
            "digitalocean", "scaleway", "edge-computing",
            "public-cloud-solutions",
        ],
        "OpenShift / Red Hat": [
            "openshift", "ocp3", "ocp4", "openshift-pipelines", "rancher",
        ],
        "Virtualization & Private Cloud": [
            "kubernetes-on-premise", "kubernetes-alternatives",
            "private-cloud-solutions",
        ],
        # --- INDUSTRY / GEO (4) – resolved via geo_region, not slugs ---
        "Americas": [],
        "Europe": [],
        "España": [],
        "Asia-Pacific": [],
    }

    GEO_CATEGORIES: Dict[str, str] = {
        "Americas": "americas",
        "Europe": "europe",
        "España": "spain",
        "Asia-Pacific": "asia_pacific",
    }

    PERIODS: Dict[str, int] = {
        "3_months": 90,
        "6_months": 180,
        "12_months": 365,
    }

    ITEMS_PER_PERIOD: Dict[str, int] = {
        "3_months": 10,
        "6_months": 15,
        "12_months": 20,
    }

    # ------------------------------------------------------------------ #

    def __init__(self) -> None:
        self.inventory: Dict[str, Any] = load_inventory()

        # Reverse map: v2_category_slug -> digest_category_name
        self.category_map: Dict[str, str] = {}
        for digest_cat, slugs in self.DIGEST_CATEGORIES.items():
            for slug in slugs:
                self.category_map[slug] = digest_cat

    # ------------------------------------------------------------------ #
    # Classification helpers                                              #
    # ------------------------------------------------------------------ #

    def _get_entry_category(self, entry: dict) -> str | None:
        """Determine which digest category an entry belongs to.

        Checks ``v2_locations`` paths first (more specific), then falls
        back to the ``category`` field.
        """
        for loc in entry.get("v2_locations", []):
            slug = loc.replace(".md", "")
            if slug in self.category_map:
                return self.category_map[slug]
        cat = entry.get("category", "")
        if cat in self.category_map:
            return self.category_map[cat]
        return None

    def _get_entry_geo(self, entry: dict) -> str | None:
        """Return the geo digest category if ``geo_region`` matches."""
        region = entry.get("geo_region", "")
        for geo_name, geo_val in self.GEO_CATEGORIES.items():
            if region == geo_val:
                return geo_name
        return None

    @staticmethod
    def _is_within_period(entry: dict, cutoff_iso: str) -> bool:
        """Check if entry falls within the time period using discovered_at,
        with year field as fallback for backfilled entries."""
        discovered = entry.get("discovered_at", "")
        if discovered:
            try:
                if discovered >= cutoff_iso:
                    return True
            except Exception:
                pass
        year = entry.get("year", "")
        if year and isinstance(year, str) and year.isdigit():
            cutoff_year = cutoff_iso[:4] if len(cutoff_iso) >= 4 else "2020"
            return year >= cutoff_year
        return False

    # ------------------------------------------------------------------ #
    # Prompt builder                                                      #
    # ------------------------------------------------------------------ #

    @staticmethod
    def _build_ranking_prompt(
        category: str, entries: List[dict], period: str
    ) -> str:
        """Assemble the Gemini prompt that asks for a ranked TOP-10."""
        period_label = period.replace("_", " ")
        lines: List[str] = []
        for i, e in enumerate(entries[:50]):
            summary_fragment = (e.get("ai_summary", "") or "")[:200]
            lines.append(
                f'{i}. "{e.get("title", "Unknown")}" '
                f'({e.get("url", "")}) | '
                f'Stars: {e.get("stars", 0)} | '
                f'Year: {e.get("year", "N/A")} | '
                f'Summary: {summary_fragment}'
            )
        entries_text = "\n".join(lines)

        return (
            "You are a Senior Technical Curator for a Cloud Native "
            "knowledge portal.\n"
            f'Given these resources discovered in the last {period_label} '
            f'for "{category}", select the TOP 10 most relevant.\n\n'
            "SCORING CRITERIA:\n"
            "- Industry Impact (30%): Does this change how teams "
            "build/operate?\n"
            "- Technical Novelty (25%): New capability, paradigm shift, "
            "major release?\n"
            "- Enterprise Adoption (20%): GA releases, production-ready?\n"
            "- Community Signal (15%): CNCF graduations, major blog posts?\n"
            "- Nubenetes Relevance (10%): Directly related to cloud native?\n\n"
            'Respond ONLY JSON: {"items": [{"idx": int, '
            '"impact": "critical|high|medium", '
            '"why": "1 sentence explaining why this matters"}]}\n\n'
            f"RESOURCES:\n{entries_text}"
        )

    # ------------------------------------------------------------------ #
    # Star-based fallback (used when Gemini is unavailable / < 3 entries) #
    # ------------------------------------------------------------------ #

    @staticmethod
    def _fallback_items(
        entries: List[dict], cat_name: str, limit: int = 10
    ) -> List[dict]:
        """Return up to *limit* items using a deterministic star-based
        ranking (no AI call required)."""
        return [
            {
                "url": e["url"],
                "title": e.get("title", "Unknown"),
                "date": e.get("discovered_at", "")[:10],
                "stars": e.get("stars") or 0,
                "impact": "high" if (e.get("stars") or 0) >= 4 else "medium",
                "why": (e.get("ai_summary", "") or "")[:200],
                "category": cat_name,
            }
            for e in entries[:limit]
        ]

    # ------------------------------------------------------------------ #
    # Core generation loop                                                #
    # ------------------------------------------------------------------ #

    async def generate_digest(self) -> dict:
        """Generate the full digest for all categories and time periods.

        Returns a nested dict::

            {
                "3_months": { "Kubernetes & Orchestration": [...], ... },
                "6_months": { ... },
                "12_months": { ... }
            }
        """
        digest: Dict[str, Dict[str, List[dict]]] = {}

        for period_name, days in self.PERIODS.items():
            cutoff = (
                datetime.now(MADRID_TZ) - timedelta(days=days)
            ).isoformat()
            digest[period_name] = {}

            # Bucket entries into their digest categories
            category_pools: Dict[str, List[dict]] = {}
            for url, entry in self.inventory.items():
                if not isinstance(entry, dict):
                    continue
                if not self._is_within_period(entry, cutoff):
                    continue

                # Tech / topic category
                cat = self._get_entry_category(entry)
                if cat:
                    category_pools.setdefault(cat, []).append(
                        dict(entry, url=url)
                    )

                # Geo category (entry may belong to both)
                geo = self._get_entry_geo(entry)
                if geo:
                    category_pools.setdefault(geo, []).append(
                        dict(entry, url=url)
                    )

            # Rank each category pool
            for cat_name, entries in category_pools.items():
                entries.sort(
                    key=lambda x: (
                        x.get("stars", 0),
                        x.get("discovered_at", ""),
                    ),
                    reverse=True,
                )

                max_items = self.ITEMS_PER_PERIOD.get(period_name, 10)

                if len(entries) < 3:
                    digest[period_name][cat_name] = self._fallback_items(
                        entries, cat_name, limit=max_items
                    )
                    continue

                try:
                    prompt = self._build_ranking_prompt(
                        cat_name, entries, period_name
                    )
                    result = await call_gemini_with_retry(
                        prompt,
                        prefer_flash=True,
                        role="Digest-Analyst",
                    )

                    ranked: List[dict] = []
                    for item in result.get("items", []):
                        idx = int(item.get("idx", -1))
                        if 0 <= idx < len(entries):
                            e = entries[idx]
                            ranked.append(
                                {
                                    "url": e["url"],
                                    "title": e.get("title", "Unknown"),
                                    "date": e.get("discovered_at", "")[:10],
                                    "stars": e.get("stars", 0),
                                    "impact": item.get("impact", "medium"),
                                    "why": item.get("why", ""),
                                    "category": cat_name,
                                }
                            )

                    digest[period_name][cat_name] = ranked[:max_items]
                    log_event(
                        f"  [Digest] {period_name}/{cat_name}: "
                        f"{len(ranked)} items ranked"
                    )

                except Exception as exc:
                    log_event(
                        f"  [Digest WARN] {period_name}/{cat_name}: "
                        f"Gemini failed ({str(exc)[:80]}), "
                        "using star-based fallback"
                    )
                    digest[period_name][cat_name] = self._fallback_items(
                        entries, cat_name, limit=max_items
                    )

                # Respect Gemini rate limits
                await asyncio.sleep(1.0)

        return digest

    # ------------------------------------------------------------------ #
    # Persistence                                                         #
    # ------------------------------------------------------------------ #

    @staticmethod
    def save_digest(digest: dict) -> None:
        """Serialise *digest* to ``data/news_digest.json``."""
        os.makedirs(os.path.dirname(DIGEST_OUTPUT_PATH), exist_ok=True)
        with open(DIGEST_OUTPUT_PATH, "w", encoding="utf-8") as fh:
            json.dump(digest, fh, indent=2, ensure_ascii=False)
        log_event(f"[Digest] Saved to {DIGEST_OUTPUT_PATH}")


# ====================================================================== #
# CLI / CI entry point                                                    #
# ====================================================================== #


async def run_news_digest() -> None:
    """Entry point for the CI pipeline."""
    log_event("STARTING NEWS DIGEST GENERATION", section_break=True)
    engine = NewsDigestEngine()
    digest = await engine.generate_digest()
    engine.save_digest(digest)

    total_items = sum(
        len(items) for period in digest.values() for items in period.values()
    )
    log_event(
        f"NEWS DIGEST COMPLETE: {total_items} total items across all periods"
    )


if __name__ == "__main__":
    asyncio.run(run_news_digest())
