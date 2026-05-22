import yaml
import os
import re
import asyncio
import httpx
from src.logger import log_event
from src.gemini_utils import call_gemini_with_retry, fetch_youtube_metadata

INVENTORY_PATH = "data/inventory.yaml"

async def enrich_video_entry(url: str, entry: dict):
    log_event(f"[*] Enriching video: {url}")
    meta = await fetch_youtube_metadata(url)
    
    # Strategy A: Use metadata from direct fetch
    # Strategy B: Fallback to AI Grounding if fetch was blocked or generic
    use_grounding = False
    is_generic = False
    if meta:
        title = meta.get('raw_title', '').lower()
        if title in ['youtube', 'before you continue', 'n/a', '']:
            is_generic = True

    if not meta or is_generic:
        log_event(f"    [!] Missing or generic metadata for {url}. Forcing AI Grounding (Pro Model)...")
        use_grounding = True
        context = f"YouTube URL: {url}\nNote: The local scraper was blocked and returned generic platform metadata. YOU MUST SEARCH FOR THE REAL TITLE."
    else:
        context = f"Local Context (from YouTube extraction):\nTitle: {meta['raw_title']}\nDescription: {meta['raw_description']}"

    prompt = f"""
    You are a Senior Cloud Architect. Your goal is to provide a high-fidelity summary of a technical YouTube video.
    
    INPUT CONTEXT:
    {context}

    CRITICAL INSTRUCTIONS:
    1. If the 'Local Context' above is missing, generic, or mentions 'YouTube' without a specific title, you MUST use your internal GOOGLE SEARCH GROUNDING to find the actual title and technical description of this video URL: {url}.
    2. Identify the ACTUAL technical content based on the verified video metadata.
    3. Generate a high-density architectural summary (2-3 sentences) explaining its specific value for a 2026 Cloud Native context.
    4. DO NOT describe generic YouTube platform infrastructure unless the video is specifically about it.
    5. Select the primary technology (e.g., Kubernetes, Vitess, Istio) and a category from: [Fundamentals and Documentaries, Architecture and Cloud Strategy, Networking and Service Mesh, Infrastructure as Code, Observability and Monitoring, AI and Future Operations, Security and Compliance].

    Return ONLY a JSON object:
    {{
      "title": "Actual Verified Title",
      "summary": "Specific and faithful architectural summary...",
      "technology": "...",
      "category": "..."
    }}
    """
    
    try:
        # Use grounding only if direct fetch failed
        data = await call_gemini_with_retry(prompt, prefer_flash=True, use_grounding=use_grounding)
        
        entry["title"] = data.get("title", meta['raw_title'] if meta else "YouTube Video")
        entry["ai_summary"] = data["summary"]
        entry["technology"] = data["technology"]
        entry["category"] = data["category"]
        entry["is_enriched"] = True
        log_event(f"    [OK] {url} enriched successfully.")
    except Exception as e:
        log_event(f"    [ERROR] Failed to parse AI response for {url}: {e}")
    
    return entry

async def main():
    if not os.path.exists(INVENTORY_PATH):
        return

    force_enrich = os.getenv("FORCE_ENRICH", "false").lower() == "true"

    with open(INVENTORY_PATH, "r") as f:
        inventory = yaml.safe_load(f)

    video_urls = [u for u, e in inventory.items() if e.get("is_featured_video")]
    
    tasks = []
    skipped = 0
    for url in video_urls:
        if inventory[url].get("is_enriched") and not force_enrich:
            skipped += 1
            continue
        tasks.append(enrich_video_entry(url, inventory[url]))

    if skipped > 0:
        log_event(f"[*] Skipped {skipped} already enriched videos. Use FORCE_ENRICH=true to re-process.")

    if not tasks:
        log_event("[*] No videos need enrichment.")
        return

    # Process in small batches to respect rate limits
    batch_size = 5
    for i in range(0, len(tasks), batch_size):
        batch = tasks[i:i+batch_size]
        await asyncio.gather(*batch)
        
        # Incremental Persistence: Save after each batch
        with open(INVENTORY_PATH, "w") as f:
            yaml.dump(inventory, f, sort_keys=False, allow_unicode=True)
        log_event(f"    [💾] Saved progress: {min(i + batch_size, len(tasks))}/{len(tasks)} videos.")
        
        if i + batch_size < len(tasks):
            await asyncio.sleep(2) # Safety delay
    
    log_event("✅ Video Hub Enrichment Complete.")

if __name__ == "__main__":
    asyncio.run(main())
