import yaml
import os
import re
import asyncio
import httpx
from src.logger import log_event
from src.gemini_utils import call_gemini_with_retry

INVENTORY_PATH = "data/inventory.yaml"

async def fetch_youtube_metadata(url: str):
    """Fetches basic metadata from YouTube page without API key."""
    try:
        async with httpx.AsyncClient(follow_redirects=True, timeout=10.0) as client:
            # Convert embed to watch URL if needed for better meta tags
            watch_url = url.replace("/embed/", "/watch?v=").split("?")[0]
            resp = await client.get(watch_url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"})
            if resp.status_code != 200:
                return None
            
            html = resp.text
            title_match = re.search(r'<title>(.*?)</title>', html)
            desc_match = re.search(r'name="description" content="(.*?)"', html)
            
            title = title_match.group(1).replace(" - YouTube", "") if title_match else "YouTube Video"
            description = desc_match.group(1) if desc_match else ""
            
            return {"raw_title": title, "raw_description": description}
    except Exception as e:
        log_event(f"Error fetching YT metadata for {url}: {e}")
        return None

async def enrich_video_entry(url: str, entry: dict):
    log_event(f"[*] Enriching video: {url}")
    meta = await fetch_youtube_metadata(url)
    if not meta:
        return entry

    prompt = f"""
    You are a Senior Cloud Architect. Analyze the following YouTube video metadata:
    Title: {meta['raw_title']}
    Description: {meta['raw_description']}

    Tasks:
    1. Generate a high-density architectural summary (2-3 sentences) focused on its value for a 2026 DevOps/Cloud context.
    2. Identify the primary technology (e.g., Kubernetes, Istio, Terraform).
    3. Select the best category from: [Fundamentals and Documentaries, Architecture and Cloud Strategy, Networking and Service Mesh, Infrastructure as Code, Observability and Monitoring, AI and Future Operations, Security and Compliance].

    Return ONLY a JSON object:
    {{
      "summary": "...",
      "technology": "...",
      "category": "..."
    }}
    """
    
    try:
        data = await call_gemini_with_retry(prompt, prefer_flash=True)
        
        entry["title"] = meta['raw_title']
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

    with open(INVENTORY_PATH, "r") as f:
        inventory = yaml.safe_load(f)

    video_urls = [u for u, e in inventory.items() if e.get("is_featured_video")]
    
    tasks = []
    for url in video_urls:
        tasks.append(enrich_video_entry(url, inventory[url]))

    # Process in small batches to respect rate limits
    batch_size = 5
    for i in range(0, len(tasks), batch_size):
        batch = tasks[i:i+batch_size]
        await asyncio.gather(*batch)
        await asyncio.sleep(2) # Safety delay

    with open(INVENTORY_PATH, "w") as f:
        yaml.dump(inventory, f, sort_keys=False, allow_unicode=True)
    
    log_event("✅ Video Hub Enrichment Complete.")

if __name__ == "__main__":
    asyncio.run(main())
