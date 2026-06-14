import os
import re
import json
import asyncio
import yaml
import httpx
from datetime import datetime
from typing import List, Dict, Set, Any, Tuple
from src.config import GEMINI_API_KEYS, GH_TOKEN, TARGET_REPO, MADRID_TZ, INVENTORY_PATH
from src.gemini_utils import call_gemini_with_retry, normalize_url, clean_toc_text, get_github_activity, fetch_youtube_metadata
from src.logger import log_event

def nuclear_strip(text: str) -> str:
    """Mandate 30: MD039 - Removes all leading/trailing whitespace including hidden unicode characters."""
    if not text: return ""
    # Purge all known whitespace characters (standard, non-breaking, thin, etc.)
    text = re.sub(r'^[\s\u00a0\u200b\u1680\u180e\u2000-\u200a\u2028\u2029\u202f\u205f\u3000]+', '', text)
    text = re.sub(r'[\s\u00a0\u200b\u1680\u180e\u2000-\u200a\u2028\u2029\u202f\u205f\u3000]+$', '', text)
    return text.replace("==", "")

V1_DIR = "docs"
V2_DIR = "v2-docs"

class V2VisionEngine:
    def __init__(self, render_only: bool = False):
        self.render_only = render_only
        # Load Config & Policy
        self.special_assets_rules = self._load_special_assets()
        self.link_rules = self._load_link_rules()
        self.max_depth = self.link_rules.get("hierarchy_rules", {}).get("max_depth", 10)
        
        # 100% Comprehensive 2026 Taxonomy
        self.dimensions = {
            "AI": ["ai", "ai-agents-mcp", "chatgpt", "mlops"],
            "Architectural Foundations": ["introduction", "faq", "kubernetes", "linux", "git", "cloud-arch-diagrams", "matrix-table", "other-awesome-lists", "about"],
            "Platform & Site Reliability": ["sre", "devops", "developerportals", "scaffolding", "finops", "chaos-engineering", "performance-testing-with-jenkins-and-jmeter", "project-management-methodology", "project-management-tools", "qa", "test-automation-frameworks", "testops"],
            "Hardened Infrastructure": ["iac", "terraform", "pulumi", "crossplane", "ansible", "securityascode", "kubernetes-security", "aws-security", "oauth", "devsecops", "kustomize", "liquibase", "chef"],
            "Cloud Providers (Hyperscalers)": ["aws", "azure", "GoogleCloudPlatform", "ibm_cloud", "oraclecloud", "digitalocean", "cloudflare", "scaleway", "managed-kubernetes-in-public-cloud", "public-cloud-solutions", "private-cloud-solutions", "edge-computing", "aws-architecture", "aws-security", "aws-networking", "aws-databases", "aws-storage", "aws-monitoring", "aws-iac", "aws-tools-scripts", "aws-messaging", "aws-data", "aws-devops", "aws-serverless", "aws-containers", "aws-backup", "aws-training", "aws-newfeatures", "aws-miscellaneous", "aws-pricing", "aws-spain"],
            "Networking & Service Mesh": ["networking", "kubernetes-networking", "servicemesh", "istio", "caching", "web-servers", "cloudflare"],
            "The Container Stack": ["docker", "container-managers", "serverless", "kubernetes-autoscaling", "kubernetes-operators-controllers", "kubernetes-storage", "kubernetes-monitoring", "kubernetes-troubleshooting", "kubernetes-backup-migrations", "kubernetes-on-premise", "kubernetes-bigdata", "kubernetes-client-libraries", "kubernetes-releases", "kubernetes-based-devel", "kubernetes-alternatives", "kubectl-commands", "rancher", "openshift", "ocp3", "ocp4", "noops"],
            "Data & Advanced Analytics": ["databases", "nosql", "newsql", "message-queue", "crunchydata", "yaml", "bigdata"],
            "Engineering Pipeline": ["cicd", "gitops", "argo", "flux", "tekton", "jenkins", "jenkins-alternatives", "openshift-pipelines", "sonarqube", "registries", "keptn", "stackstorm", "cicd-kubernetes-plugins"],
            "Developer Ecosystem": ["visual-studio", "javascript", "golang", "python", "java_frameworks", "java_app_servers", "java-and-java-performance-optimization", "dotnet", "angular", "react", "web3", "api", "swagger-code-generator-for-rest-apis", "postman", "lowcode-nocode", "devel-sites", "dom", "linux-dev-env", "ChromeDevTools", "xamarin", "jvm-parameters-matrix-table", "maven-gradle", "embedded-servlet-containers"],
            "Career & Industry": ["recruitment", "hr", "finops", "freelancing", "remote-tech-jobs", "workfromhome", "interview-questions", "elearning", "digital-money", "appointment-scheduling", "newsfeeds"]
        }
        
        self.library_criteria = (
            "You are a Senior Technical Architect in 2026. Your mission is to organize a high-density technical reference portal "
            "structured like a professional technical book (O'Reilly style).\n"
            "PHASE 1: TECHNICAL PRESERVATION & CURATION\n"
            "- KEEP >90% of technical resources (except for 'introduction.md' where only high-impact links are kept).\n"
            "PHASE 2: SOPHISTICATED HIERARCHICAL CLASSIFICATION\n"
            "- Identify TECHNICAL_HIERARCHY: A list of strings (max 10) representing Area > Topic > Subtopics.\n"
            "- For 'introduction.md', identify links related to MICROSERVICES for extraction.\n"
            "PHASE 3: KNOWLEDGE ASSIMILATION FLOW\n"
            "- Order hierarchy to facilitate a structured learning journey.\n"
            "PHASE 4: HIGH-DENSITY TECHNICAL SUMMARIES (Double-Evidence Synthesis)\n"
            "- Generate professional, neutral, and advanced technical summaries. Style: O'Reilly technical.\n"
            "- PROTOCOL: Contrast 'Curator Insight' (from source) with 'Live Grounding' (from search).\n"
            "- If discrepancies are found (e.g. project is archived but source says it's new), PRIORITIZE live engineering truth.\n"
            "- Summaries MUST be high-density: Include architectural value, key features, and technical significance.\n"
            "- Format: Use paragraphs and bullet points for complex tools. Aim for 2-5 sentences of depth.\n"
            "PHASE 5: ADVANCED MATURITY TAGGING\n"
            "- Assign 1 to 3 tags from: [DE FACTO STANDARD], [ENTERPRISE-STABLE], [EMERGING], [GUIDE], [CASE STUDY], [COMMUNITY-TOOL], [LEGACY].\n"
        )
        self.inventory = self._load_inventory()
        self.maturity_audit = []

    def _load_special_assets(self) -> Dict:
        path = "data/special_assets.yaml"
        if os.path.exists(path):
            try: return yaml.safe_load(open(path, "r")) or {}
            except: return {}
        return {}

    def _load_link_rules(self) -> Dict:
        path = "data/link_rules.yaml"
        if os.path.exists(path):
            try: return yaml.safe_load(open(path, "r")) or {}
            except: return {}
        return {}

    def _load_inventory(self) -> Dict:
        from src.inventory_manager import load_inventory
        return load_inventory()

    def _save_inventory(self):
        from src.inventory_manager import save_inventory
        save_inventory(self.inventory)

    async def analyze_and_cluster(self):
        log_event("STARTING V2 HIGH-DENSITY O'REILLY LIBRARY GENERATION", section_break=True)
        
        # Mandate 30: MD039 - Global Data Sanitization (Purge all whitespace/hidden chars from titles)
        for url in list(self.inventory.keys()):
            if isinstance(self.inventory[url], dict) and "title" in self.inventory[url]:
                # Purge all known whitespace characters (standard, non-breaking, thin, etc.)
                t = self.inventory[url]["title"]
                t = re.sub(r'^[\s\u00a0\u200b\u1680\u180e\u2000-\u200a\u2028\u2029\u202f\u205f\u3000]+', '', t)
                t = re.sub(r'[\s\u00a0\u200b\u1680\u180e\u2000-\u200a\u2028\u2029\u202f\u205f\u3000]+$', '', t)
                self.inventory[url]["title"] = t
        
        # 0. Mandate Sync
        try:
            from src.mandate_ingestor import MandateIngestor
            MandateIngestor().save_system_instructions()
        except: pass

        all_v1_links, mosaic_html, videos_html = await self._gather_all_v1_content()
        
        log_event(f"[*] Discovery: Found {len(all_v1_links)} resources to process.")

        log_event("[*] Phase 1: Health Check...")
        if self.render_only:
            # Mandate 19/22: In render-only mode (Fast-Track), we are conservative to avoid pruning valid sections.
            # We keep links that are explicitly 'online', 'review_required' OR have no status yet.
            health_inventory = []
            for l in all_v1_links:
                entry = self.inventory.get(normalize_url(l["url"]), {})
                status = entry.get("status", "online") # Assume online if unknown for rendering
                if status in ["online", "review_required"]:
                    health_inventory.append(l)
        else:
            health_inventory = await self._verify_link_health(all_v1_links)
        
        log_event("[*] Phase 2: Evaluation & Deep Indexing (Semantic Dedup)...")
        library_inventory = await self._evaluate_and_score_resources(health_inventory)

        log_event("[*] Phase 3: Recursive Hierarchy Construction...")
        v2_data = await self._rebuild_structure(library_inventory)
        
        log_event("[*] Phase 4: Generating Premium Portal Hubs...")
        os.makedirs(V2_DIR, exist_ok=True)
        
        # --- SURGICAL GARBAGE COLLECTION ---
        # Track every file we generate
        generated_files = {"index.md", "audit-log.md", "videos.md"}
        for f_name in v2_data.keys():
            generated_files.add(f_name)


        await self._write_premium_files(v2_data, mosaic_html, videos_html)
        await self._sync_enterprise_navigation(v2_data)
        
        # Delete only orphaned files
        log_event("[*] Phase 5: Pruning Orphaned V2 Assets...")
        for f in os.listdir(V2_DIR):
            if f.endswith(".md") and f not in generated_files:
                log_event(f"  [DEL] Pruning obsolete V2 page: {f}")
                os.remove(os.path.join(V2_DIR, f))

        self._save_inventory()
        
        # --- FINAL SAFETY AUDIT ---
        try:
            from src.safety_guard import SafetyGuard
            guard = SafetyGuard()
            report = guard.generate_audit_report()
            with open("v2_safety_report.md", "w") as f: f.write(report)
        except Exception as e:
            log_event(f"  [!] V2 Safety Audit Error: {e}")
        
        log_event("V2 ELITE PORTAL GENERATED SUCCESSFULLY.")

    async def _gather_all_v1_content(self):
        all_links, mosaic_html, videos_html = [], "", ""
        if os.path.exists("docs/index.md"):
            with open("docs/index.md", "r") as f:
                idx_content = f.read()
                videos_match = re.search(r'\?\?\? note "Top Videos & Clips.*?\n\s+(<center.*?</center>)', idx_content, re.DOTALL)
                if videos_match:
                    videos_html = videos_match.group(1)
        
        # Dynamically generate V2 categorized mosaic from youtube_channels_mosaic.yaml
        try:
            from src.reorganize_mosaic import build_v2_mosaic_markdown
            v2_mosaic_full = build_v2_mosaic_markdown("data/youtube_channels_mosaic.yaml")
            mosaic_html = v2_mosaic_full.replace('<center markdown="1">', '').replace('</center>', '').strip()
        except Exception as e:
            log_event(f"  [!] Error generating V2 mosaic dynamically: {e}")
            mosaic_html = ""

        for root, _, files in os.walk(V1_DIR):
            for file in files:
                if not file.endswith(".md") or file == "index.md": continue
                path = os.path.join(root, file)
                with open(path, "r") as f: content = f.read()
                matches = re.finditer(r'^\s*-\s*\[([^\]]+)\]\(([^\)]+)\)(.*?(?:\n\s{2,}.*)*)', content, re.MULTILINE)
                for m in matches:
                    title, url, full_desc = m.groups()
                    if not url.startswith(("http", "mailto", "#")):
                        url = f"https://nubenetes.com/{url.replace('.md', '/')}"
                    # Mandate 30: MD039 - Strip all whitespace (including non-breaking space) from link text
                    all_links.append({"title": nuclear_strip(title), "url": url.strip(), "description": full_desc.strip(), "original_file": file})
        return all_links, mosaic_html, videos_html

    async def _verify_link_health(self, links: List[Dict]):
        force_full = os.getenv("FORCE_FULL_CHECK", "false").lower() == "true"
        fast_online = []
        needs_check = []
        
        for l in links:
            nu = normalize_url(l["url"])
            entry = self.inventory.get(nu, {})
            # Mandate 32: skip links under review
            if entry.get("status") == "review_required": continue
            
            if not force_full and entry.get("status") == "online":
                fast_online.append(l)
            else:
                needs_check.append(l)
                
        if not needs_check: return fast_online

        log_event(f"    [>] Fast-Track Health: {len(fast_online)} | Network-Check: {len(needs_check)}")
        
        online_links = list(fast_online)
        total_needs = len(needs_check)
        async with httpx.AsyncClient(timeout=15.0, follow_redirects=True, verify=False) as client:
            # Mandate 16/22: Resilient asynchronous health checks with increased concurrency
            CHUNK_SIZE = 100 
            for i in range(0, total_needs, CHUNK_SIZE):
                batch = needs_check[i:i+CHUNK_SIZE]
                tasks = [self._check_single_link_resilient(client, l) for l in batch]
                results = await asyncio.gather(*tasks)
                online_links.extend([r for r in results if r is not None])
                if i % 100 == 0:
                    log_event(f"    [>] Progress: [{i}/{total_needs}] links validated over network...")
                await asyncio.sleep(0.05) # Minimal delay
        return online_links

    async def _check_single_link_resilient(self, client, link: Dict):
        url = link["url"]
        norm_url = normalize_url(url)
        entry = self.inventory.get(norm_url, {})
        
        # Mandate 31: Skip links under review for V2 Elite
        if entry.get("status") == "review_required":
            log_event(f"  [-] SKIPPING V2: {url} is under Review.")
            return None
            
        if entry.get("status") == "online" and os.getenv("FORCE_FULL_CHECK", "false").lower() != "true": return link
        try:
            resp = await client.get(url, timeout=10.0)
            if resp.status_code < 400:
                final_url = str(resp.url)
                from src.gemini_utils import sanitize_trailing_slashes
                final_url = sanitize_trailing_slashes(final_url)
                
                # Update URL if it was redirected/normalized
                if final_url != url:
                    link["url"] = final_url
                
                self.inventory.setdefault(normalize_url(final_url), {})["status"] = "online"
                # Mandate 22: Update last_checked for the inventory entry
                self.inventory[normalize_url(final_url)]["last_checked"] = datetime.now().timestamp()
                return link
        except: pass
        return None

    async def _evaluate_and_score_resources(self, links: List[Dict]):
        to_evaluate = []
        project_registry = {} 
        force_eval = os.getenv("FORCE_EVAL", "false").lower() == "true"
        force_full_check = os.getenv("FORCE_FULL_CHECK", "false").lower() == "true"
        # Bypassing GitHub UI limitation: If force_eval or force_full_check is ON, we must enrich metadata
        enrich_metadata = os.getenv("ENRICH_METADATA", "false").lower() == "true" or force_eval or force_full_check
        special_files = [sa["file"] for sa in self.special_assets_rules.get("special_assets", [])]
        
        # Mandate 47: Zero-Redundancy & Smart Grounding
        from src.mandate_ingestor import get_system_mandates
        dynamic_mandates = get_system_mandates()

        # Mandate 15: Proactive Enrichment for V2 (GitHub metadata is critical for tags)
        # Optimized: Parallel fetching with Semaphore to avoid sequential bottleneck
        processed_gh_metadata = set()
        gh_fetch_count = 0
        gh_tasks = []
        gh_sem = asyncio.Semaphore(30) # Increased for final sprint strategy

        async def _fetch_gh_with_sem(url: str):
            async with gh_sem:
                return url, await get_github_activity(url)

        for l in links:
            norm_url = normalize_url(l["url"])
            if "github.com" not in norm_url or self.render_only: continue

            cached = self.inventory.get(norm_url, {})
            # Mandate 43: Always ensure GH metadata for GitHub links in V2 to power [DE FACTO STANDARD] logic
            if (enrich_metadata or not cached.get("gh_stars")) and norm_url not in processed_gh_metadata:
                processed_gh_metadata.add(norm_url)
                gh_tasks.append(_fetch_gh_with_sem(norm_url))

        if gh_tasks:
            log_event(f"  [METADATA] V2 Pulse: Batch fetching {len(gh_tasks)} GitHub profiles in parallel...", section_break=True)
            gh_results = await asyncio.gather(*gh_tasks)
            for norm_url, gh_data in gh_results:
                if gh_data:
                    if norm_url not in self.inventory: self.inventory[norm_url] = {}
                    self.inventory[norm_url].update(gh_data)
                    gh_fetch_count += 1

            # Periodic Save: Save once after the massive batch
            from src.inventory_manager import save_inventory
            save_inventory(self.inventory)
            log_event(f"    [💾] Inventory Persisted: {gh_fetch_count} metadata entries updated.")

        for l in links:
            item = l.copy()
            norm_url = normalize_url(l["url"])
            orig_file = l.get("original_file", "unknown.md")
            is_special = orig_file in special_files
            item["is_special"] = is_special
            project_id = norm_url
            if "github.com" in norm_url:
                match = re.search(r'github\.com/([^/]+/[^/]+)', norm_url)
                if match: project_id = match.group(1).lower()

            # Reuse enriched metadata from inventory
            if "github.com" in norm_url:
                item.update(self.inventory.get(norm_url, {}))

            if not force_eval and norm_url in self.inventory:
                cached = self.inventory[norm_url]
                item.update(cached)
                if is_special: item["is_special"] = True
                # Mandate 30: Hierarchy and AI Summaries are mandatory for ELITE AI curation.
                # Optimized Skip Logic: Only skip if we already have BOTH hierarchy and a summary.
                if (cached.get("hierarchy") and cached.get("ai_summary")) or self.render_only:
                    if project_id not in project_registry or item.get("stars", 0) > project_registry[project_id].get("stars", 0):
                        if project_id in project_registry and project_registry[project_id].get("is_special"): item["is_special"] = True
                        project_registry[project_id] = item
                    continue
            to_evaluate.append(item)

        if to_evaluate and not self.render_only:
            # Mandate 47: Zero-Redundancy & Smart Grounding
            # Fast-Track (Metadata/Desc present) vs Grounded-Track (Needs deep search)
            fast_track = []
            grounded_track = []
            
            for l in to_evaluate:
                nu = normalize_url(l["url"])
                is_github = "github.com" in nu
                
                # Fast-Track Eligibility:
                # 1. Has AI summary (previous run)
                # 2. Is GitHub and has stars (metadata present)
                # 3. Has decent manual description (> 40 chars)
                # 4. Is already in inventory (we have title/category context)
                has_ai_summary = l.get("ai_summary") is not None and len(l.get("ai_summary")) > 50
                has_stars = l.get("gh_stars") is not None
                has_desc = len(l.get("description", "")) > 40
                is_known = nu in self.inventory

                if has_ai_summary or has_stars or has_desc or is_known:
                    fast_track.append(l)
                else:
                    # Grounded-Track is ONLY for "Unknown" resources with zero context
                    grounded_track.append(l)

            log_event(f"[*] Agent Phase 1: Analyst Evaluation ({len(to_evaluate)} resources)...")
            log_event(f"    [>] Fast-Track: {len(fast_track)} | Grounded-Track: {len(grounded_track)}")

            analyst_results = []

            # 1.1 Fast-Track: Large Batches, NO GROUNDING (Fast)
            # Optimized: Parallel batch processing to leverage high-tier API quotas
            BATCH_SIZE_FAST = 50 
            total_fast = len(fast_track)
            fast_tasks = []

            async def _process_fast_batch(batch_links, batch_idx, total_b):
                log_event(f"    [>] Fast-Track: Queuing Batch {batch_idx}/{total_b}...")
                prompt = (
                    f"You are the Nubenetes Technical Analyst (2026).\n"
                    f"{dynamic_mandates}\n"
                    f"{self.library_criteria}\n"
                    "PHASE 5: TECHNICAL SYNTHESIS (FAST-TRACK)\n"
                    "- Use provided metadata, AI summaries, and descriptions to classify maturity.\n"
                    "Respond ONLY JSON: {{\"results\": [{{ \"idx\": int, \"year\": \"YYYY\", \"stars\": 0-5, \"hierarchy\": [\"Area\", \"Topic\", ...], \"tags\": [\"...\"], \"summary\": \"Synthesis...\", \"language\": \"...\", \"type\": \"...\", \"complexity\": \"...\", \"is_microservice\": bool }}, ...]}}\n\n"
                    "LINKS:\n" + "\n".join([f"{idx}. {l['title']} ({l['url']}) | Stars: {l.get('gh_stars', l.get('stars'))} | Existing Summary: {l.get('ai_summary', l.get('description'))}" for idx, l in enumerate(batch_links)])
                )
                try:
                    data = await call_gemini_with_retry(prompt, prefer_flash=True, use_grounding=False, role="Analyst-Fast")
                    batch_results = []
                    for res in data.get("results", []):
                        idx = int(res["idx"])
                        if idx < len(batch_links):
                            item = batch_links[idx].copy()
                            eval_data = {
                                "year": str(res.get("year", "N/A")), "stars": min(max(int(res.get("stars", 0)), 0), 5),
                                "ai_summary": res.get("summary", item.get("ai_summary", "")),
                                "language": res.get("language", "English"),
                                "resource_type": res.get("type", "Reference"), "complexity": res.get("complexity", "Intermediate"),
                                "hierarchy": res.get("hierarchy", ["General"]), "tags": res.get("tags", []),
                                "is_microservice": bool(res.get("is_microservice", False)),
                                "status": "online", "is_special": item.get("is_special", False)
                            }
                            item.update(eval_data)
                            batch_results.append(item)
                            
                            # Incremental Persistence
                            norm_url = normalize_url(item["url"])
                            self.inventory[norm_url] = {k:v for k,v in item.items() if k not in ["url", "title", "original_file", "is_special", "aliases"]}
                            self.inventory[norm_url]["title"] = item["title"]
                    return batch_results
                except Exception as e:
                    log_event(f"    [!] Error in Fast-Batch {batch_idx}: {e}")
                    return batch_links # Fallback to original links (standard layer)

            total_batches_fast = (total_fast + BATCH_SIZE_FAST - 1) // BATCH_SIZE_FAST
            for i in range(0, total_fast, BATCH_SIZE_FAST):
                batch = fast_track[i:i+BATCH_SIZE_FAST]
                batch_num = (i // BATCH_SIZE_FAST) + 1
                fast_tasks.append(_process_fast_batch(batch, batch_num, total_batches_fast))

            if fast_tasks:
                log_event(f"[*] Agent Phase 1.1: Dispatching {len(fast_tasks)} parallel batches...")
                
                # Use as_completed to persist results incrementally during parallel execution
                processed_count = 0
                for task in asyncio.as_completed(fast_tasks):
                    r_list = await task
                    analyst_results.extend(r_list)
                    processed_count += 1
                    
                    # Mandate 22: Save every 10 batches to disk to avoid data loss during 6h timeouts
                    if processed_count % 10 == 0:
                        log_event(f"    [💾] Periodic Save: Persisting inventory after {processed_count} batches...")
                        from src.inventory_manager import save_inventory
                        save_inventory(self.inventory)

                # Final Save
                from src.inventory_manager import save_inventory
                save_inventory(self.inventory)
                log_event(f"    [💾] Inventory Persisted after {len(analyst_results)} AI evaluations.")

                await asyncio.sleep(2.0) # Safety delay to respect TPM limits

            # 1.2 Grounded-Track: Small Batches, WITH GROUNDING (Slower but precise)
            BATCH_SIZE_GROUNDED = 15 # Increased from 5
            total_grounded = len(grounded_track)
            for i in range(0, total_grounded, BATCH_SIZE_GROUNDED):
                batch = grounded_track[i:i+BATCH_SIZE_GROUNDED]
                batch_num = (i // BATCH_SIZE_GROUNDED) + 1
                total_batches = (total_grounded + BATCH_SIZE_GROUNDED - 1) // BATCH_SIZE_GROUNDED
                log_event(f"    [🌟] Grounded-Track: Processing Batch {batch_num}/{total_batches} (Grounding active)...")

                # MANDATE 25: Pre-enrich YouTube links with real metadata
                enriched_batch = []
                for item in batch:
                    url = item["url"]
                    if "youtube.com" in url or "youtu.be" in url:
                        log_event(f"      [YT] Pre-fetching metadata for: {url}")
                        meta = await fetch_youtube_metadata(url)
                        if meta:
                            item["description"] = f"TITLE: {meta['raw_title']}\nDESCRIPTION: {meta['raw_description']}"
                    enriched_batch.append(item)

                prompt = (
                    f"You are the Nubenetes Technical Analyst (2026).\n"
                    f"{dynamic_mandates}\n"
                    f"{self.library_criteria}\n"
                    "PHASE 5: DOUBLE-EVIDENCE SYNTHESIS & RICH SUMMARY (GROUNDED)\n"
                    "- Cross-reference provided title/desc with search grounding.\n"
                    "Respond ONLY JSON: {{\"results\": [{{ \"idx\": int, \"year\": \"YYYY\", \"stars\": 0-5, \"hierarchy\": [\"Area\", \"Topic\", ...], \"tags\": [\"...\"], \"summary\": \"Synthesis...\", \"language\": \"...\", \"type\": \"...\", \"complexity\": \"...\", \"is_microservice\": bool }}, ...]}}\n\n"
                    "LINKS:\n" + "\n".join([f"{idx}. {l['title']} ({l['url']}) | Input Context: {l.get('description', 'N/A')}" for idx, l in enumerate(enriched_batch)])
                )
                try:
                    data = await call_gemini_with_retry(prompt, prefer_flash=True, use_grounding=True, role="Analyst-Grounded")
                    for res in data.get("results", []):
                        idx = int(res["idx"])
                        if idx < len(batch):
                            item = batch[idx].copy()
                            eval_data = {
                                "year": str(res.get("year", "N/A")), "stars": min(max(int(res.get("stars", 0)), 0), 5),
                                "ai_summary": res.get("summary", ""), "language": res.get("language", "English"),
                                "resource_type": res.get("type", "Reference"), "complexity": res.get("complexity", "Intermediate"),
                                "hierarchy": res.get("hierarchy", ["General"]), "tags": res.get("tags", []),
                                "is_microservice": bool(res.get("is_microservice", False)),
                                "status": "online", "is_special": item.get("is_special", False)
                            }
                            item.update(eval_data)
                            analyst_results.append(item)
                except Exception:
                    for l in batch: analyst_results.append(l)
                await asyncio.sleep(4.0) # Higher delay for Grounding tasks            # --- AGENT PHASE 2: SELECTIVE AUDIT (MCP-Grounded) ---
            # Identify candidates for high-trust verification
            audit_candidates = [l for l in analyst_results if "[DE FACTO STANDARD]" in l.get("tags", []) or "[ENTERPRISE-STABLE]" in l.get("tags", [])]
            
            if audit_candidates:
                log_event(f"[*] Agent Phase 2: Auditor Verification ({len(audit_candidates)} high-impact candidates)...")
                # AUDIT BATCH: Very small for max grounding precision
                for i in range(0, len(audit_candidates), 5):
                    batch = audit_candidates[i:i+5]
                    audit_prompt = (
                        f"You are the Nubenetes Auditor (2026).\n"
                        f"{dynamic_mandates}\n"
                        "MISSION: Perform 'Double-Evidence' verification using your GOOGLE_SEARCH tool.\n"
                        "PROTOCOL:\n"
                        "1. SEARCH: Look for community reputation (Reddit, HN) and repo status (GitHub).\n"
                        "2. CONTRAST: Compare findings with the proposed Analyst summary.\n"
                        "3. REFINE: Correct any 'vaporware' or 'hype' claims. Ensure technical accuracy.\n"
                        "CRITERIA:\n"
                        "- [DE FACTO STANDARD]: Industry baseline, used by everyone.\n"
                        "- [ENTERPRISE-STABLE]: Proven, high-trust, supported.\n"
                        "Respond ONLY JSON: {{\"audits\": [{{ \"idx\": int, \"verified_tags\": [\"...\"], \"refined_summary\": \"Synthesized and verified technical summary...\", \"reputation_summary\": \"...\", \"reputation_penalty\": bool }}, ...]}}\n\n"
                        "RESOURCES TO AUDIT:\n" + "\n".join([f"{idx}. {l['title']} ({l['url']}) - Proposed: {l.get('tags')}" for idx, l in enumerate(batch)])
                    )
                    try:
                        # AUDIT USES PRO MODEL (High Reasoning) + GROUNDING (Live Data)
                        audit_data = await call_gemini_with_retry(audit_prompt, prefer_flash=False, use_grounding=True, role="Auditor")
                        for aud in audit_data.get("audits", []):
                            idx = int(aud["idx"])
                            if idx < len(batch):
                                # Update tags, summary and add reputation metadata (Mandate 32/33)
                                batch[idx]["tags"] = aud.get("verified_tags", batch[idx]["tags"])
                                if aud.get("refined_summary"): batch[idx]["ai_summary"] = aud["refined_summary"]
                                batch[idx]["reputation_summary"] = aud.get("reputation_summary", "")
                                if aud.get("reputation_penalty"):
                                    batch[idx]["stars"] = max(batch[idx].get("stars", 1) - 1, 1)
                                    if "[DE FACTO STANDARD]" in batch[idx]["tags"]: batch[idx]["tags"].remove("[DE FACTO STANDARD]")
                    except: pass
                    await asyncio.sleep(0.5)

            # Finalize Registry
            for item in analyst_results:
                norm_url = normalize_url(item["url"])
                p_id = norm_url
                if "github.com" in norm_url:
                    m = re.search(r'github\.com/([^/]+/[^/]+)', norm_url)
                    if m: p_id = m.group(1).lower()
                
                # Persist to inventory
                self.inventory[norm_url] = {k:v for k,v in item.items() if k not in ["url", "title", "original_file", "is_special", "aliases"]}
                self.inventory[norm_url]["title"] = item["title"]
                if "addition_method" not in self.inventory[norm_url]:
                    self.inventory[norm_url]["addition_method"] = "manual"
                
                if p_id not in project_registry or item.get("stars", 0) > project_registry[p_id].get("stars", 0):
                    if p_id in project_registry and project_registry[p_id].get("is_special"): item["is_special"] = True
                    project_registry[p_id] = item

        return list(project_registry.values())

    def _calculate_tags(self, item: Dict) -> List[str]:
        """
        Mandate 40: Multi-Dimensional Tagging (1:N).
        Merges AI-assigned tags with rule-based maturity signals to ensure high-fidelity classification.
        Utilizes MCP-style grounding data (GitHub stars, resource types) to override generic defaults.
        """
        # 0. Collect all possible tag sources
        ai_tags = item.get("tags", [])
        if isinstance(ai_tags, str): ai_tags = [ai_tags] # Resiliency
        
        valid_set = {"[DE FACTO STANDARD]", "[ENTERPRISE-STABLE]", "[EMERGING]", "[GUIDE]", "[CASE STUDY]", "[COMMUNITY-TOOL]", "[LEGACY]"}
        
        # Start with filtered AI tags
        tags = set([t for t in ai_tags if t in valid_set])
        
        # 1. GitHub Objective Reality (Mandate 43)
        raw_gh = item.get("gh_stars", 0)
        gh_stars = int(raw_gh) if str(raw_gh).isdigit() else 0
        curator_stars = int(item.get("stars", 0))

        if gh_stars > 15000 or curator_stars >= 5: 
            tags.add("[DE FACTO STANDARD]")
            if "[COMMUNITY-TOOL]" in tags: tags.remove("[COMMUNITY-TOOL]")
        elif gh_stars > 3000 or curator_stars >= 4: 
            tags.add("[ENTERPRISE-STABLE]")
            if "[COMMUNITY-TOOL]" in tags: tags.remove("[COMMUNITY-TOOL]")
        
        # 2. Type Mapping (AI based labels)
        res_type = item.get("resource_type", "Reference").lower()
        if any(x in res_type for x in ["guide", "tutorial", "hands-on", "learning", "course"]): 
            tags.add("[GUIDE]")
        if any(x in res_type for x in ["case study", "report", "whitepaper", "success story", "usage"]): 
            tags.add("[CASE STUDY]")
        
        # 3. Emerging / Legacy logic
        ai_summary = item.get("ai_summary", "").lower()
        complexity = item.get("complexity", "Intermediate")
        if complexity == "Cutting Edge" or "emerging" in ai_summary or "experimental" in ai_summary or "alpha" in ai_summary:
            tags.add("[EMERGING]")
        if "legacy" in ai_summary or "deprecated" in ai_summary or "archived" in ai_summary or "v1-only" in ai_summary:
            tags.add("[LEGACY]")

        # 4. Fallback: Only use [COMMUNITY-TOOL] if no other maturity tag is present
        maturity_tags = {"[DE FACTO STANDARD]", "[ENTERPRISE-STABLE]", "[EMERGING]", "[LEGACY]"}
        if not (tags & maturity_tags):
            tags.add("[COMMUNITY-TOOL]")
        
        # Clean up: If we have high maturity, remove community-tool
        if (tags & {"[DE FACTO STANDARD]", "[ENTERPRISE-STABLE]"}) and "[COMMUNITY-TOOL]" in tags:
            tags.remove("[COMMUNITY-TOOL]")

        return sorted(list(tags))

    async def _rebuild_structure(self, library_inventory: List[Dict]):
        special_rules = {sa["file"]: sa for sa in self.special_assets_rules.get("special_assets", [])}
        v2_structure = {} 
        
        file_to_dim = {f + ".md": dim for dim, files in self.dimensions.items() for f in files}

        for item in library_inventory:
            # Calculate multi-tags
            item["tags"] = self._calculate_tags(item)
            
            # Mandate: Persist tags back to inventory for reporting & caching
            norm_url = normalize_url(item["url"])
            
            # Mandate 19: Use v1_locations to preserve file context and prevent page deletions
            v1_locations = item.get("v1_locations", [])
            if not v1_locations:
                # Fallback to original_file if v1_locations is missing
                v1_locations = [f"docs/{item.get('original_file', 'unknown.md')}"]
            
            for loc in v1_locations:
                orig_file = os.path.basename(loc)
                if not orig_file.endswith(".md") or orig_file == "index.md": continue
                
                if norm_url in self.inventory:
                    self.inventory[norm_url]["tags"] = item["tags"]
                    # Track V2 locations for reporting (Mandate 22)
                    v2_locs = self.inventory[norm_url].get("v2_locations", [])
                    if orig_file not in v2_locs:
                        v2_locs.append(orig_file)
                        self.inventory[norm_url]["v2_locations"] = v2_locs
                
                dim = file_to_dim.get(orig_file, "Architectural Foundations")
                
                # Mandate 29: Special Assets must include 100% of ALIVE links, bypassing impact filters.
                is_special = item.get("is_special", False) or orig_file in special_rules
                if not is_special and orig_file == "introduction.md" and item.get("stars", 0) < 3 and not item.get("is_microservice"):
                    continue
                
                if orig_file not in v2_structure:
                    short_title = orig_file.replace(".md", "").replace("-", " ").title()
                    # Custom mapping for known acronyms (Mandate 32)
                    acronyms = {
                        "Ai": "AI", "Mcp": "MCP", "Iac": "IaC", "Aws": "AWS", "Gcp": "GCP", 
                        "Api": "API", "Sre": "SRE", "Cicd": "CI/CD", "Ocp3": "OCP 3", 
                        "Ocp4": "OCP 4", "Jvm": "JVM", "Sql": "SQL", "Nosql": "NoSQL",
                        "Chatgpt": "ChatGPT", "Mlops": "MLOps", "Devops": "DevOps",
                        "Hr": "HR", "Qa": "QA"
                    }
                    for k, v in acronyms.items():
                        short_title = short_title.replace(k, v)
                    
                    long_title = short_title
                    v1_path = os.path.join("docs", orig_file)
                    if os.path.exists(v1_path):
                        with open(v1_path, "r", encoding="utf-8") as f:
                            for line in f:
                                if line.startswith("# "):
                                    long_title = line.strip().replace("# ", "").strip()
                                    break

                    v2_structure[orig_file] = {
                        "dim": dim,
                        "title": short_title,
                        "long_title": long_title,
                        "content": {"__links__": []}
                    }
                
                # Populate Maturity Audit for GitOps Reporting (Deduplicated)
                audit_entry = {
                    "url": item["url"],
                    "tag": ", ".join(item["tags"]),
                    "stars": item.get("stars", 0),
                    "dimension": dim,
                    "v2_locations": True 
                }
                if audit_entry not in self.maturity_audit:
                    self.maturity_audit.append(audit_entry)
                
                hierarchy = item.get("hierarchy", [])
                # Skip redundant top-level labels
                if hierarchy and (hierarchy[0] == dim or hierarchy[0] == v2_structure[orig_file]["title"]): hierarchy = hierarchy[1:]
                
                current = v2_structure[orig_file]["content"]
                for h_name in hierarchy[:self.max_depth]:
                    if h_name not in current: current[h_name] = {"__links__": []}
                    current = current[h_name]
                current["__links__"].append(item)

        def sort_rec(node):
            if "__links__" in node: node["__links__"].sort(key=lambda x: (-x.get("stars", 1), -(int(x["year"]) if str(x.get("year", "")).isdigit() else 0)))
            for k, v in node.items():
                if k != "__links__" and isinstance(v, dict): sort_rec(v)
                
        for f_name in v2_structure:
            sort_rec(v2_structure[f_name]["content"])
            
        return v2_structure

    async def _generate_comparison_table(self, links: List[Dict]) -> str:
        standard_tools = [l for l in links if l.get("stars", 0) >= 3]
        if len(standard_tools) < 5: return ""
        table = "\n??? abstract \"Architect's Technical Comparison Table\"\n"
        table += "    | Solution | Maturity | Primary Focus | Language | Stars |\n"
        table += "    | :--- | :--- | :--- | :--- | :--- |\n"
        for l in standard_tools[:10]:
            stars = "🌟" * l.get("stars", 0)
            focus = l.get("topic", l.get("hierarchy", ["General"])[-1])
            # Mandate 30: MD039 - Strip all whitespace (including non-breaking space) from link text
            clean_title = nuclear_strip(l['title'])
            table += f"    | [{clean_title}]({l['url'].strip()}) | {l.get('tag','').replace('[','').replace(']','')} | {focus} | {l.get('language','English')} | {stars} |\n"
        return table + "\n"

    async def _render_single_link(self, l: Dict, is_intro: bool) -> str:
        md = ""
        is_gold = is_intro and l.get("stars", 0) >= 4
        title = nuclear_strip(l['title']) 
        if is_gold:
            img = f"    ![Preview]({l.get('social_preview_url')})\n" if l.get('social_preview_url') else ""
            md += f"??? note \"{title}\"\n{img}    **[Access Resource]({l['url'].strip()})** {'🌟'*l.get('stars',4)} | Level: {l.get('complexity', 'Beginner')}\n    \n    {l.get('ai_summary', l.get('description', ''))}\n\n"
        else:
            year = l.get('year', 'N/A')
            year_prefix = f"**({year})** " if year != 'N/A' else ""
            gh_info = f" <span class='md-tag md-tag--info'>⭐ {l.get('gh_stars',0)}</span>" if l.get('gh_stars') else ""
            
            icon = " 🎥" if l.get("is_video") else ""
            lang = l.get("language", "English")
            lang_tag = f" <span class='md-tag md-tag--warning'>[{lang.upper()} CONTENT]</span>" if lang.lower() != "english" else ""
            comp = l.get("complexity", "Intermediate")
            level_tag = f" <span class='md-tag md-tag--critical'>[{comp.upper()} LEVEL]</span>" if comp.lower() in ["architect", "advanced"] else ""
            res_type = l.get("resource_type", "Reference")
            type_tag = f" <span class='md-tag md-tag--primary'>[{res_type.upper()}]</span>" if res_type.lower() in ["case study", "guide", "documentation"] else ""
            rich = "".join([f" <small>by **{l['author']}**</small>" if l.get("author") else "", f" <span class='md-tag md-tag--info'>⏱️ {l['duration']}</span>" if l.get("duration") else "", f" <span class='md-tag md-tag--info'>📖 {l['reading_time']}</span>" if l.get("reading_time") else ""])
            tag_html = ""
            for tag in l.get("tags", ["[COMMUNITY-TOOL]"]):
                color = "success" if "STANDARD" in tag else "warning" if "EMERGING" in tag else "secondary" if "CASE STUDY" in tag or "GUIDE" in tag else "info"
                tag_html += f" <span class='md-tag md-tag--{color}'>{tag}</span>"
            
            # Apply Visual Highlighting based on stars
            raw_stars = l.get('stars', 0)
            link_content = title
            if raw_stars >= 5:
                link_content = f"=={link_content}=="
            elif raw_stars >= 4:
                link_content = f"**{link_content}**"
            
            md += f"  - {year_prefix}[{link_content}]({l['url'].strip()}){icon}{gh_info}{lang_tag}{level_tag}{type_tag}{rich} {'🌟'*raw_stars}{tag_html}"

            # Layer 2: High-Density Technical Summary (Always Visible Inline)
            summary = l.get('ai_summary', l.get('description', ''))
            if summary:
                # Use a separator and append summary directly to the same line
                md += f" — {summary.strip()}\n"
            else:
                md += "\n"
        return md


    async def _write_premium_files(self, data: Dict[str, Dict], mosaic_html: str, videos_html: str):
        # 1. Update Index with Pulse
        trending_pool = sorted([dict(meta, url=url) for url, meta in self.inventory.items() if isinstance(meta, dict) and meta.get("stars", 0) >= 4], key=lambda x: (str(x.get("year", "0000")) if str(x.get("year", "")).isdigit() else "0000", -x.get("stars", 0)), reverse=True)
        pulse_md = "## The Agentic Pulse\n" + "\n".join([f"- **({l.get('year', 'N/A')})** [**=={nuclear_strip(l['title'])}==**]({l['url'].strip()}) {'🌟'*l.get('stars',3)}" for l in trending_pool[:5]])
        
        # Calculate coverage for the index
        total_v1 = len(self.inventory)
        v2_links_all = [dict(meta, url=url) for url, meta in self.inventory.items() if isinstance(meta, dict) and meta.get("v2_locations")]
        total_v2 = len(v2_links_all)
        v2_efficiency = round((total_v2 / total_v1) * 100, 2) if total_v1 > 0 else 0
        enriched = len([l for l in v2_links_all if l.get('hierarchy') or l.get('ai_summary')])
        coverage_pct = round((enriched / total_v2) * 100, 2) if total_v2 > 0 else 0
        
        # GitHub Metadata Coverage for index
        gh_links = [l for l in v2_links_all if "github.com" in str(l.get('url', ''))]
        total_gh = len(gh_links)
        gh_meta = len([l for l in gh_links if l.get('gh_stars') is not None])
        gh_coverage = round((gh_meta / total_gh) * 100, 2) if total_gh > 0 else 0

        coverage_info = (
            "\n??? info \"Knowledge Architecture and AI Coverage Status\"\n"
            "    The Nubenetes Elite Portal operates on a dual-layer knowledge architecture:\n"
            "    1. **Elite Layer (AI-Enriched)**: Resources individually analyzed by our Agentic AI with high-density summaries and hierarchical indexing.\n"
            "    2. **Standard Layer (Mapped)**: Resources identified as candidates for Elite status but pending deep AI analysis.\n\n"
            "    **Current Inventory Coverage:**\n"
            f"    - **V1 Base Inventory**: {total_v1} total resources analyzed.\n"
            f"    - **V2 Elite Selection**: {total_v2} candidates identified ({v2_efficiency}% density ratio).\n"
            f"    - **AI Enrichment Coverage**: {enriched} / {total_v2} ({coverage_pct}%)\n"
            f"    - **GitHub Metadata Coverage**: {gh_meta} / {total_gh} ({gh_coverage}%) - *Critical for Maturity Tagging*\n"
            "    - **Status**: The system is incrementally processing pending resources to complete the knowledge graph.\n"
        )

        index_md = (
            "# Nubenetes Elite Portal (V2) | Awesome Kubernetes & Cloud [![Awesome](https://cdn.jsdelivr.net/gh/sindresorhus/awesome@d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)\n\n"
            "<center markdown=\"1\">\n"
            "<div class=\"hero-showcase-wrapper\">\n"
            "  <a href=\"https://www.cncf.io/certification/software-conformance\" class=\"hero-showcase-link\">\n"
            "    <img src=\"images/container_with_cars_v2.png\" alt=\"container_with_cars\" class=\"hero-showcase-image\" />\n"
            "    <div class=\"hero-showcase-footer\">\n"
            "      <span class=\"hero-showcase-badge\">CNCF Conformance</span>\n"
            "      <span class=\"hero-showcase-caption\">Standardized conformance guarantees seamless workload portability across the Cloud Native landscape.</span>\n"
            "    </div>\n"
            "  </a>\n"
            "</div>\n"
            "</center>\n\n"
            "<div class=\"quote-card-container\">\n"
            "  <a href=\"https://en.wikipedia.org/wiki/Horatio_Nelson_Jackson\" class=\"quote-card-link\">\n"
            "    <div class=\"quote-card\">\n"
            "      <div class=\"quote-card-text\">\"I do not believe you can do today's job with yesterday's methods and be in business tomorrow\"</div>\n"
            "      <div class=\"quote-card-author\">Horatio Nelson Jackson</div>\n"
            "    </div>\n"
            "  </a>\n"
            "</div>\n\n"
            "<div style=\"display: flex; justify-content: center; gap: 24px; margin: 16px 0; flex-wrap: wrap;\">\n"
            "  <a href=\"./kubernetes/\" style=\"text-decoration: none; color: inherit; display: block;\">\n"
            "    <div class=\"hero-badge-card hero-badge-card--cyan\">\n"
            "      <img src=\"/v2/images/kubernetes_logo.png\" alt=\"Kubernetes\"/>\n"
            "      <div class=\"hero-badge-title\">Ecosystem Core</div>\n"
            "      <div class=\"hero-badge-subtitle\">Explore Kubernetes</div>\n"
            "    </div>\n"
            "  </a>\n"
            "  <a href=\"./ai-agents-mcp/\" style=\"text-decoration: none; color: inherit; display: block;\">\n"
            "    <div class=\"hero-badge-card hero-badge-card--purple\">\n"
            "      <img src=\"/v2/images/ai_agents_logo.png\" alt=\"AI & MCP Agents\"/>\n"
            "      <div class=\"hero-badge-title\">AI & MCP Agents</div>\n"
            "      <div class=\"hero-badge-subtitle\">Agentic Ecosystem</div>\n"
            "    </div>\n"
            "  </a>\n"
            "  <a href=\"./videos/\" style=\"text-decoration: none; color: inherit; display: block;\">\n"
            "    <div class=\"hero-badge-card hero-badge-card--pink\">\n"
            "      <img src=\"/v2/images/video_hub_logo.png\" alt=\"Agentic Video Hub\"/>\n"
            "      <div class=\"hero-badge-title\">Agentic Video Hub</div>\n"
            "      <div class=\"hero-badge-subtitle\">Architect Video Library</div>\n"
            "    </div>\n"
            "  </a>\n"
            "  <a href=\"./introduction/\" style=\"text-decoration: none; color: inherit; display: block;\">\n"
            "    <div class=\"hero-badge-card hero-badge-card--teal\">\n"
            "      <img src=\"/v2/images/hero-car.png\" alt=\"Nubenetes Car\"/>\n"
            "      <div class=\"hero-badge-title\">Get Started</div>\n"
            "      <div class=\"hero-badge-subtitle\">Introduction Guide</div>\n"
            "    </div>\n"
            "  </a>\n"
            "</div>\n\n"
            "!!! abstract \"The High-Density Vision\"\n"
            "    The V2 Edition is a curated, high-density version of the Nubenetes archive. Using **Agentic AI Orchestration**, "
            "the system selects only the most relevant, stable, and impactful resources for the modern Cloud Native ecosystem (2026 and beyond).\n\n"
            f"{coverage_info}\n\n"
            f"<center markdown=\"1\">\n{mosaic_html}\n</center>\n\n"
            f"{pulse_md}\n\n"
            "## Strategic Dimensions\n"
            "- **[🎥 Agentic Video Hub (Architectural Summary)](./videos/index.md)**\n\n"
        )
        
        # Group by dimension for index
        dim_groups = {}
        for f_name, info in data.items():
            dim_groups.setdefault(info["dim"], []).append(f_name)
            
        # Mandate: Use the order defined in self.dimensions for architectural flow
        for dim in self.dimensions.keys():
            if dim in dim_groups:
                index_md += f"### {dim}\n"
                for f in sorted(dim_groups[dim]):
                    index_md += f"- **[{data[f]['title']}](./{f})**\n"
        
        index_md += (
            "\n---\n\n"
            "## The Maturity Taxonomy\n\n"
            "To ensure industrial-grade precision, every resource in V2 is classified using our proprietary 5-tier maturity system:\n\n"
            "| Tag | Description | Engineering Context |\n"
            "| :--- | :--- | :--- |\n"
            "| **`[DE FACTO STANDARD]`** | The industry baseline. | Tools like Kubernetes, Terraform, or Prometheus that define the current architecture. |\n"
            "| **`[ENTERPRISE-STABLE]`** | Battle-tested and reliable. | Proven solutions with strong community and commercial support. |\n"
            "| **`[EMERGING]`** | The cutting edge. | High-potential tools and patterns (e.g., AI Agents, MCP) shaping the future. |\n"
            "| **`[GUIDE]`** | Strategic knowledge. | High-quality tutorials, architectural deep-dives, and decision matrices. |\n"
            "| **`[LEGACY]`** | Historical context. | Established tools that are being replaced or are primarily for maintaining older stacks. |\n\n"
            "## Technical Impact (Relevance Score)\n\n"
            "The stars accompanying each resource represent its **Technical Impact** and **Architectural Relevance** for a 2026 Senior Architect:\n\n"
            "| Impact | Level | Meaning | Visual Code |\n"
            "| :---: | :--- | :--- | :--- |\n"
            "| 🌟🌟🌟🌟🌟 | **Platinum Standard** | Critical industry foundation. Essential knowledge for any Cloud Native architecture. | `==[Highlighted Link]==` |\n"
            "| 🌟🌟🌟🌟 | **Gold Standard** | Highly recommended. Proven value and significant community/enterprise momentum. | `**[Bold Link]**` |\n"
            "| 🌟🌟🌟 | **Silver Standard** | Solid technical reference. Useful for specific use cases or established patterns. | Standard Link |\n"
            "| 🌟🌟 | **Bronze Standard** | Interesting alternative or niche tool. Good to have in the toolkit for specific scenarios. | Standard Link |\n"
            "| 🌟 | **Reference Only** | Basic documentation or historical reference without major current impact. | Standard Link |\n"
        )
        
        with open(os.path.join(V2_DIR, "index.md"), "w") as f: f.write(index_md)

        async def render_node(node, depth, base_slug, used_headers, is_intro=False):
            md = ""
            # Mandate: Process links at this level FIRST if they have NO further hierarchy
            # This handles links that are candidates but haven't been deeply classified yet (orphans)
            if "__links__" in node and depth == -1:
                orphan_links = node["__links__"]
                if orphan_links:
                    md += "## Standard Reference\n\n"
                    for l in orphan_links:
                        md += await self._render_single_link(l, is_intro)
                    md += "\n"

            for name, subnode in sorted(node.items()):
                if name == "__links__": continue
                clean_name = clean_toc_text(name)
                
                # Mandate 30: MD024 - Deduplicate headings to prevent Linter errors
                h_name = clean_name
                counter = 1
                while h_name in used_headers:
                    h_name = f"{clean_name} ({counter})"
                    counter += 1
                used_headers.add(h_name)
                
                slug = f"{base_slug}-{h_name.lower().replace(' ', '-')}"
                # MD025: Ensure only one H1. Main title is H1, so internal headers start at H2 (depth + 3)
                header_level = min(6, depth + 3) 
                md += f"{'#' * header_level} {h_name}\n\n"
                
                if depth == 1 and "__links__" in subnode: 
                    md += await self._generate_comparison_table(subnode["__links__"])
                
                md += await render_node(subnode, depth + 1, slug, used_headers, is_intro)
            
            if "__links__" in node and depth >= 0:
                for l in node["__links__"]:
                    md += await self._render_single_link(l, is_intro)
            return md

        for f_name, info in data.items():
            used_headers = {info['long_title']} # Mandate 30: MD024 - Pre-populate with H1 to avoid duplicates
            md = f"# {info['long_title']}\n\n!!! info \"Architectural Context\"\n    Detailed reference for {info['long_title']} in the context of {info['dim']}.\n\n"
            
            if f_name == "introduction.md":
                md += "## Vision 2026\n\n!!! quote \"The Evolution of Autonomy\"\n    From manual curation to agentic intelligence.\n\n### Ecosystem Map\n\n\n```mermaid\ngraph TD\n    A[Foundations] --> B[AI & Intelligence]\n    A --> C[Hardened Infra]\n    B --> D[Agentic Curation]\n    C --> E[Enterprise Stability]\n    D --> F[Nubenetes Portal]\n    E --> F\n```\n\n\n"

            
            md += await render_node(info["content"], -1, f_name.replace(".md", ""), used_headers, is_intro=(f_name=="introduction.md"))
            
            # Add Semantic "See Also" ONLY ONCE at the end of the page
            related = [f"[{data[f]['title']}](./{f})" for f in data if f != f_name and data[f]["dim"] == info["dim"]]
            if related:
                md += f"\n---\n💡 **Explore Related:** {' | '.join(related[:3])}\n\n"
            
            # Smart Write: Only update disk if content changed
            target_path = os.path.join(V2_DIR, f_name)
            existing_content = ""
            if os.path.exists(target_path):
                with open(target_path, "r") as f: existing_content = f.read()
            
            if md != existing_content:
                with open(target_path, "w") as f: f.write(md)

    async def _sync_enterprise_navigation(self, data: Dict[str, Dict]):
        try:
            with open("v2-mkdocs.yml", "r") as f: content = f.read()
            nav = [
                "nav:", 
                "  - \"🔙 Back to V1 (Exhaustive)\": https://nubenetes.com/v1/", 
                "  - \"The 2026 Vision\": index.md",
                "  - \"Agentic Video Hub\":",
                "      - videos/index.md",
                "      - \"AI Agents and MCP\": videos/ai-agents.md",
                "      - \"DevOps, IaC, and SRE\": videos/devops-iac.md",
                "      - \"Cloud Native Core\": videos/cloud-native.md",
                "      - \"Fundamentals\": videos/fundamentals.md"
            ]
            
            # Group files by dimension
            dim_groups = {}
            for f_name, info in data.items():
                dim_groups.setdefault(info["dim"], []).append(f_name)

            for dim in self.dimensions.keys():
                if dim in dim_groups:
                    dim_nav = [f"  - \"{dim}\":"]
                    for f in sorted(dim_groups[dim]):
                        dim_nav.append(f"    - \"{data[f]['title']}\": {f}")
                    nav.extend(dim_nav)                    
            updated = re.sub(r'nav:.*', "\n".join(nav), content, flags=re.DOTALL)
            with open("v2-mkdocs.yml", "w") as f: f.write(updated)
        except: pass

import argparse
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--render-only", action="store_true")
    args = parser.parse_args()

    engine = V2VisionEngine(render_only=args.render_only)
    asyncio.run(engine.analyze_and_cluster())
    
    # --- PLATINUM GITOPS REPORTING (Multi-Comment) ---
    from src.gitops_manager import RepositoryController
    from src.config import TARGET_REPO
    
    # 1. High-Density Metrics Calculation
    total_v1_links = len(engine.inventory)
    v2_links_all = [dict(meta, url=url) for url, meta in engine.inventory.items() if isinstance(meta, dict) and meta.get("v2_locations")]
    total_v2_links = len(v2_links_all)
    
    # Coverage Metrics (Mandate: Transparency in Knowledge Discovery)
    enriched_v2 = [l for l in v2_links_all if l.get('hierarchy') or l.get('ai_summary')]
    total_enriched = len(enriched_v2)
    coverage_pct = round((total_enriched / total_v2_links) * 100, 2) if total_v2_links > 0 else 0
    
    # GitHub Metadata Coverage
    gh_links = [l for l in v2_links_all if "github.com" in str(l.get('url', ''))]
    total_gh = len(gh_links)
    gh_with_metadata = len([l for l in gh_links if l.get('gh_stars') is not None])
    gh_coverage_pct = round((gh_with_metadata / total_gh) * 100, 2) if total_gh > 0 else 0
    
    # Delta & Efficiency
    density_ratio = round((total_v2_links / total_v1_links) * 100, 2) if total_v1_links > 0 else 0
    reduction_delta = total_v1_links - total_v2_links
    
    # Maturity Distribution
    maturity_counts = {}
    for l in v2_links_all:
        tags = l.get('tags', ['[COMMUNITY-TOOL]'])
        for tag in tags:
            maturity_counts[tag] = maturity_counts.get(tag, 0) + 1

    # 2. Document Architecture Audit
    v2_files = sorted([f for f in os.listdir(V2_DIR) if f.endswith(".md")])
    file_list_md = "| # | Document Name | Description |\n| :--- | :--- | :--- |\n"
    for i, f in enumerate(v2_files, 1):
        # Quick extract title from file
        title = "Elite Category"
        try:
            with open(os.path.join(V2_DIR, f), "r") as doc:
                line = doc.readline()
                if line.startswith("# "): title = line.replace("# ", "").strip()
        except: pass
        file_list_md += f"| {i} | `{f}` | {title} |\n"

    # 3. Decision Matrix (Maturity Audit)
    matrix_rows = []
    header_table = "| # | Status | Maturity | Stars | Dimension | Resource |\n| :--- | :--- | :--- | :---: | :--- | :--- |\n"
    for idx, entry in enumerate(engine.maturity_audit, 1):
        status = "💎 ELITE" if entry.get('v2_locations') else "📦 ARCHIVE"
        row = f"| {idx} | {status} | {entry.get('tag', 'N/A')} | {'🌟'*entry.get('stars',0)} | {entry.get('dimension', 'N/A')} | {entry.get('url', 'N/A')} |\n"
        matrix_rows.append(row)

    # 4. Generate PR Body (Main Report)
    with open("pr_description.md", "w") as f:
        f.write(f"## 🏆 V2 Elite: Agentic Optimization Sync (2026)\n\n")
        f.write(f"The V2 Portal has been synchronized with the latest V1 changes. This update enforces the **Minimum Viable Quality (MVQ)** and O'Reilly-style architectural standards.\n\n")
        
        f.write(f"### 📊 High-Density Efficiency\n")
        f.write(f"| Metric | V1 Archive | V2 Elite | Delta / Efficiency |\n")
        f.write(f"| :--- | :---: | :---: | :---: |\n")
        f.write(f"| **Total Resources** | {total_v1_links} | {total_v2_links} | -{reduction_delta} ({density_ratio}% Density) |\n")
        f.write(f"| **AI Enrichment** | N/A | {total_enriched} / {total_v2_links} | {coverage_pct}% Coverage |\n")
        f.write(f"| **GitHub Metadata** | N/A | {gh_with_metadata} / {total_gh} | {gh_coverage_pct}% Coverage |\n")
        f.write(f"| **Maturity Tagging** | Manual | AI-Vetted | 100% Coverage |\n")
        f.write(f"| **Hierarchical Depth** | Flat | Recursive | Max Depth: {engine.max_depth} |\n\n")

        f.write("### 🏗️ Evidence of Elite Status\n")
        f.write("<details><summary>📊 Clic para ver Gráfico de Distribución</summary>\n\n")
        f.write("```mermaid\npie title V2 Maturity Distribution\n")
        for tag, count in maturity_counts.items():
            tag_name = tag.replace('[','').replace(']','')
            f.write(f"    \"{tag_name}\" : {count}\n")
        f.write("```\n\n</details>\n\n")
        
        from src.gemini_utils import SESSION_TRACKER
        f.write(SESSION_TRACKER.get_intelligence_report())
        f.write("\n\n---\n**Detailed Architectural Audit and Decision Matrix follow in comments.**\n")

    # 5. Save Supplementary Reports for Workflow/GitOps
    with open("v2_file_audit.md", "w") as f:
        f.write("### 📜 V2 Document Architecture\n")
        f.write(f"Exhaustive list of {len(v2_files)} generated elite documents.\n\n")
        f.write(file_list_md)

    with open("v2_decision_matrix.md", "w") as f:
        f.write("### 📋 Elite Decision Matrix\n")
        f.write("Detailed logs of maturity promotions and elite selections.\n\n")
        f.write(header_table)
        for row in matrix_rows: f.write(row)
