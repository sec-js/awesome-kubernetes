from __future__ import annotations

import asyncio
import re
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple

import httpx

from src.config import GH_TOKEN, MADRID_TZ
from src.logger import log_event

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
CNCF_LANDSCAPE_URL = "https://landscape.cncf.io/api/items"  # Legacy, now SPA — fallback to GitHub topic search
GITHUB_API_BASE = "https://api.github.com"
GITHUB_RATE_DELAY = 0.75  # seconds between GitHub API calls to stay under 5000/hr
MAX_REPOS_DEFAULT = 500
ACTIVITY_STALENESS_DAYS = 30

# Community health thresholds
HEALTH_ACTIVE = 50
HEALTH_HEALTHY = 10

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _github_headers() -> Dict[str, str]:
    """Build GitHub API request headers with optional auth."""
    headers = {"Accept": "application/vnd.github.v3+json"}
    if GH_TOKEN:
        headers["Authorization"] = f"token {GH_TOKEN}"
    return headers


def _parse_github_repo(url: str) -> Optional[str]:
    """Extract 'owner/repo' from a GitHub URL. Returns None if not a GitHub URL."""
    match = re.search(r"github\.com/([^/]+/[^/]+)", url)
    if not match:
        return None
    repo = match.group(1).split("#")[0].split("?")[0].rstrip("/")
    # Strip trailing .git if present
    if repo.endswith(".git"):
        repo = repo[:-4]
    return repo


def _normalize_repo_url(url: str) -> str:
    """Normalize a GitHub repo URL for comparison (lowercase, no trailing slash)."""
    url = url.lower().rstrip("/")
    if url.endswith(".git"):
        url = url[:-4]
    # Strip protocol
    url = re.sub(r"^https?://", "", url)
    return url


def _is_activity_stale(entry: Dict) -> bool:
    """Check whether an entry's activity data is older than ACTIVITY_STALENESS_DAYS."""
    checked = entry.get("gh_activity_checked")
    if not checked:
        return True
    try:
        checked_dt = datetime.fromisoformat(checked)
        return datetime.now(MADRID_TZ) - checked_dt > timedelta(days=ACTIVITY_STALENESS_DAYS)
    except (ValueError, TypeError):
        return True


# ---------------------------------------------------------------------------
# Module 1: CNCF Landscape Status
# ---------------------------------------------------------------------------

async def fetch_cncf_landscape() -> Dict[str, str]:
    """Fetch CNCF project graduation status via GitHub topic search.

    The legacy landscape.cncf.io/api/items endpoint is now a SPA and no
    longer returns JSON.  Instead, we search GitHub for repos with CNCF
    maturity topics (cncf-sandbox, cncf-incubating, cncf-graduated).

    Returns dict mapping repo_url (normalized) -> maturity.
    """
    result: Dict[str, str] = {}
    headers = _github_headers()
    maturity_queries = {
        "graduated": "topic:cncf-graduated",
        "incubating": "topic:cncf-incubating",
        "sandbox": "topic:cncf-sandbox",
    }

    async with httpx.AsyncClient(timeout=30.0) as client:
        for maturity, query in maturity_queries.items():
            try:
                url = f"{GITHUB_API_BASE}/search/repositories?q={query}&per_page=100"
                resp = await client.get(url, headers=headers)
                resp.raise_for_status()
                data = resp.json()
                for repo in data.get("items", []):
                    repo_url = repo.get("html_url", "")
                    if repo_url:
                        result[_normalize_repo_url(repo_url)] = maturity
                log_event(f"  [CNCF] {maturity}: {len(data.get('items', []))} repos found")
            except Exception as e:
                log_event(f"[WARN] CNCF {maturity} search failed: {str(e)[:100]}")
            await asyncio.sleep(GITHUB_RATE_DELAY)

    log_event(f"[CNCF] Fetched {len(result)} projects from CNCF landscape")
    return result


async def enrich_cncf_status(inventory: Dict) -> int:
    """Update inventory entries with cncf_status field.

    If an entry maps to a CNCF-graduated project and lacks the
    ``[DE FACTO STANDARD]`` tag, the tag is appended.

    Returns count of entries updated.
    """
    landscape = await fetch_cncf_landscape()
    if not landscape:
        return 0

    updated = 0
    for url, entry in inventory.items():
        if url.startswith("INTRO:"):
            continue
        normalized = _normalize_repo_url(url)
        maturity = landscape.get(normalized)
        if not maturity:
            continue

        old_status = entry.get("cncf_status")
        entry["cncf_status"] = maturity
        if old_status != maturity:
            updated += 1

        # Auto-tag graduated projects
        if maturity == "graduated":
            tags = entry.get("tags")
            if isinstance(tags, list) and "[DE FACTO STANDARD]" not in tags:
                tags.append("[DE FACTO STANDARD]")
                entry["tags"] = tags

    log_event(f"[CNCF] Enriched {updated} inventory entries with CNCF status")
    return updated


# ---------------------------------------------------------------------------
# Module 2: Social Signal Enrichment (GitHub Activity)
# ---------------------------------------------------------------------------

async def _fetch_repo_activity(
    client: httpx.AsyncClient,
    owner_repo: str,
) -> Tuple[int, int]:
    """Fetch open issue count and recent open PR count for a single repo.

    Returns (open_issues_count, open_prs_count).
    """
    headers = _github_headers()
    open_issues = 0
    open_prs = 0

    # Fetch repo-level stats (open_issues_count includes PRs on GitHub)
    try:
        resp = await client.get(
            f"{GITHUB_API_BASE}/repos/{owner_repo}",
            headers=headers,
            timeout=15.0,
        )
        if resp.status_code == 200:
            data = resp.json()
            open_issues = data.get("open_issues_count", 0)
    except Exception as e:
        log_event(f"[WARN] GitHub repo fetch failed for {owner_repo}: {str(e)[:120]}")

    await asyncio.sleep(GITHUB_RATE_DELAY)

    # Fetch open PRs (page 1 only — we use total_count from search or headers)
    try:
        resp = await client.get(
            f"{GITHUB_API_BASE}/repos/{owner_repo}/pulls",
            headers=headers,
            params={"state": "open", "sort": "created", "per_page": 1},
            timeout=15.0,
        )
        if resp.status_code == 200:
            # The total count of open PRs is not directly in the body for the
            # list endpoint, but we can parse the Link header for the last page.
            # As a simpler approach, the body is a list; if it has items the repo
            # has open PRs. We use the repo-level open_issues_count as the
            # combined metric (GitHub counts PRs as issues).
            pr_data = resp.json()
            if isinstance(pr_data, list) and len(pr_data) > 0:
                # Parse Link header for total pages
                link_header = resp.headers.get("Link", "")
                last_match = re.search(r'page=(\d+)>;\s*rel="last"', link_header)
                open_prs = int(last_match.group(1)) if last_match else len(pr_data)
    except Exception as e:
        log_event(f"[WARN] GitHub PRs fetch failed for {owner_repo}: {str(e)[:120]}")

    await asyncio.sleep(GITHUB_RATE_DELAY)

    return open_issues, open_prs


def _classify_health(total_activity: int) -> str:
    """Classify community health based on combined issue + PR activity."""
    if total_activity > HEALTH_ACTIVE:
        return "active"
    if total_activity >= HEALTH_HEALTHY:
        return "healthy"
    if total_activity > 0:
        return "low"
    return "dormant"


async def enrich_github_activity(inventory: Dict, max_repos: int = MAX_REPOS_DEFAULT) -> int:
    """Fetch recent issue/PR velocity for GitHub repos in the inventory.

    Adds fields:
    - ``gh_open_issues_30d``
    - ``gh_open_prs_30d``
    - ``gh_community_health`` ("active" | "healthy" | "low" | "dormant")
    - ``gh_activity_checked`` (ISO timestamp)

    Skips entries whose ``gh_activity_checked`` is less than 30 days old.
    Processes at most *max_repos* repos per run.

    Returns count of entries enriched.
    """
    candidates: List[Tuple[str, str]] = []  # (url, owner/repo)

    for url, entry in inventory.items():
        if url.startswith("INTRO:"):
            continue
        repo = _parse_github_repo(url)
        if not repo:
            continue
        if not _is_activity_stale(entry):
            continue
        candidates.append((url, repo))
        if len(candidates) >= max_repos:
            break

    if not candidates:
        log_event("[Activity] No GitHub repos require activity enrichment")
        return 0

    log_event(f"[Activity] Enriching {len(candidates)} GitHub repos (max {max_repos})")

    enriched = 0
    async with httpx.AsyncClient() as client:
        for url, owner_repo in candidates:
            try:
                open_issues, open_prs = await _fetch_repo_activity(client, owner_repo)
                total = open_issues + open_prs
                health = _classify_health(total)

                entry = inventory[url]
                entry["gh_open_issues_30d"] = open_issues
                entry["gh_open_prs_30d"] = open_prs
                entry["gh_community_health"] = health
                entry["gh_activity_checked"] = datetime.now(MADRID_TZ).isoformat()
                enriched += 1
            except Exception as e:
                log_event(f"[WARN] Activity enrichment failed for {owner_repo}: {str(e)[:150]}")

    log_event(f"[Activity] Enriched {enriched}/{len(candidates)} repos with community health data")
    return enriched


# ---------------------------------------------------------------------------
# Module 3: License Change Detection
# ---------------------------------------------------------------------------

async def _fetch_current_license(
    client: httpx.AsyncClient,
    owner_repo: str,
) -> Optional[str]:
    """Fetch the current SPDX license identifier for a GitHub repo."""
    headers = _github_headers()
    try:
        resp = await client.get(
            f"{GITHUB_API_BASE}/repos/{owner_repo}",
            headers=headers,
            timeout=15.0,
        )
        if resp.status_code == 200:
            data = resp.json()
            lic = data.get("license")
            if isinstance(lic, dict):
                return lic.get("spdx_id", "N/A")
            return "N/A"
        elif resp.status_code == 404:
            return None  # repo not found / deleted
    except Exception as e:
        log_event(f"[WARN] License fetch failed for {owner_repo}: {str(e)[:120]}")
    return None


async def detect_license_changes(inventory: Dict) -> List[Dict]:
    """Compare current gh_license with stored license, flag changes.

    For each GitHub repo in inventory that has ``gh_license``:
    - Fetches the current license from the GitHub API.
    - Compares with the stored ``gh_license``.
    - If different, updates the entry: sets ``gh_license`` to the new value
      and stores the old value in ``gh_license_previous``.

    Returns list of ``{url, old_license, new_license, title}`` dicts.
    """
    candidates: List[Tuple[str, str, Dict]] = []  # (url, owner/repo, entry)

    for url, entry in inventory.items():
        if url.startswith("INTRO:"):
            continue
        if not entry.get("gh_license") or entry["gh_license"] == "N/A":
            continue
        repo = _parse_github_repo(url)
        if not repo:
            continue
        candidates.append((url, repo, entry))

    if not candidates:
        log_event("[License] No repos with stored licenses to check")
        return []

    log_event(f"[License] Checking {len(candidates)} repos for license changes")

    changes: List[Dict] = []
    async with httpx.AsyncClient() as client:
        for url, owner_repo, entry in candidates:
            try:
                current = await _fetch_current_license(client, owner_repo)
                if current is None:
                    # Repo not found or API error — skip
                    continue

                stored = entry.get("gh_license", "N/A")
                if current != stored:
                    change_record = {
                        "url": url,
                        "old_license": stored,
                        "new_license": current,
                        "title": entry.get("title", url),
                    }
                    changes.append(change_record)
                    entry["gh_license_previous"] = stored
                    entry["gh_license"] = current
                    log_event(
                        f"[License] Change detected: {owner_repo} "
                        f"{stored} -> {current}"
                    )
            except Exception as e:
                log_event(f"[WARN] License check failed for {owner_repo}: {str(e)[:150]}")

            await asyncio.sleep(GITHUB_RATE_DELAY)

    log_event(f"[License] Detected {len(changes)} license change(s)")
    return changes


# ---------------------------------------------------------------------------
# Full Enrichment Pipeline
# ---------------------------------------------------------------------------

async def run_enrichment():
    """Full enrichment pipeline: CNCF + GitHub activity + license detection."""
    from src.inventory_manager import load_inventory, save_inventory

    log_event("ENRICHMENT PIPELINE STARTING", section_break=True)
    inventory = load_inventory()
    log_event(f"[*] Loaded {len(inventory)} inventory entries")

    cncf_count = await enrich_cncf_status(inventory)
    activity_count = await enrich_github_activity(inventory)
    license_changes = await detect_license_changes(inventory)

    save_inventory(inventory)
    log_event(
        f"Enrichment complete: {cncf_count} CNCF, "
        f"{activity_count} activity, "
        f"{len(license_changes)} license changes",
        section_break=True,
    )

    return license_changes


if __name__ == "__main__":
    asyncio.run(run_enrichment())
