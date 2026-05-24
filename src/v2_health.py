import asyncio
from src.v2_optimizer import V2VisionEngine
from src.logger import log_event

async def run_health_check():
    engine = V2VisionEngine(render_only=False)
    log_event("STARTING V2 SPECIALIZED HEALTH MONITOR", section_break=True)
    
    all_v1_links, _, _ = await engine._gather_all_v1_content()
    log_event(f"[*] Discovery: Found {len(all_v1_links)} resources to validate.")
    
    # We only run the health check phase
    await engine._verify_link_health(all_v1_links)
    
    engine._save_inventory()
    log_event("V2 HEALTH MONITOR COMPLETED SUCCESSFULLY.")

if __name__ == "__main__":
    asyncio.run(run_health_check())
