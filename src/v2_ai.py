import asyncio
from src.v2_optimizer import V2VisionEngine
from src.logger import log_event
from src.gemini_utils import normalize_url

async def run_ai_curation():
    engine = V2VisionEngine(render_only=False)
    log_event("STARTING V2 SPECIALIZED AI CURATOR", section_break=True)
    
    all_v1_links, _, _ = await engine._gather_all_v1_content()
    log_event(f"[*] Discovery: Found {len(all_v1_links)} resources for AI analysis.")
    
    # Filter for online links to save tokens
    online_links = [l for l in all_v1_links if engine.inventory.get(normalize_url(l["url"]), {}).get("status") == "online"]
    log_event(f"[*] Analysis: Processing {len(online_links)} online resources.")
    
    # Run the evaluation phase (Analyst + Auditor)
    # This method already handles incremental persistence and batching
    await engine._evaluate_and_score_resources(online_links)
    
    engine._save_inventory()
    log_event("V2 AI CURATOR COMPLETED SUCCESSFULLY.")

if __name__ == "__main__":
    asyncio.run(run_ai_curation())
