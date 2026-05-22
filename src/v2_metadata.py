import os
import asyncio
from src.v2_optimizer import V2VisionEngine
from src.logger import log_event
from src.gemini_utils import normalize_url, get_github_activity

async def run_metadata_enrichment():
    engine = V2VisionEngine(render_only=False)
    log_event("STARTING V2 SPECIALIZED METADATA ENGINE", section_break=True)
    
    all_v1_links, _, _ = await engine._gather_all_v1_content()
    log_event(f"[*] Discovery: Found {len(all_v1_links)} resources for metadata enrichment.")
    
    # Mandate 15 & 43: Proactive Enrichment for V2
    processed_gh_metadata = set()
    gh_fetch_count = 0
    force_full = os.getenv("ENRICH_METADATA", "false").lower() == "true"

    for l in all_v1_links:
        norm_url = normalize_url(l["url"])
        if "github.com" not in norm_url: continue
        
        cached = engine.inventory.get(norm_url, {})
        # Enrich if missing or if forced
        if (force_full or not cached.get("gh_stars")) and norm_url not in processed_gh_metadata:
            log_event(f"  [METADATA] Fetching GH Activity for {norm_url}")
            processed_gh_metadata.add(norm_url)
            gh_data = await get_github_activity(norm_url)
            if gh_data:
                if norm_url not in engine.inventory: engine.inventory[norm_url] = {}
                engine.inventory[norm_url].update(gh_data)
                
            gh_fetch_count += 1
            if gh_fetch_count % 100 == 0:
                engine._save_inventory()
                log_event(f"    [💾] Periodic Save: {gh_fetch_count} fetches...")

    engine._save_inventory()
    log_event(f"V2 METADATA ENGINE COMPLETED. Processed {gh_fetch_count} repos.")

if __name__ == "__main__":
    asyncio.run(run_metadata_enrichment())
