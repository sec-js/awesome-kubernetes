import yaml
import os

INVENTORY_PATH = "data/inventory.yaml"
V2_VIDEOS_PATH = "v2-docs/videos.md"

def generate_v2_videos():
    if not os.path.exists(INVENTORY_PATH):
        return

    with open(INVENTORY_PATH, "r") as f:
        inventory = yaml.safe_load(f)

    featured_videos = []
    for url, entry in inventory.items():
        if entry.get("is_featured_video"):
            featured_videos.append({
                "url": url,
                "title": entry.get("title", "YouTube Video"),
                "category": entry.get("category", "General"),
                "summary": entry.get("ai_summary", entry.get("description", "")),
                "year": entry.get("year", "N/A")
            })

    if not featured_videos:
        print("No featured videos found in inventory.")
        return

    # Sort by Category and then Title
    featured_videos.sort(key=lambda x: (x["category"], x["title"]))

    def clean_header(text):
        # MANDATE 30: No ampersands, no special characters
        t = text.replace("&", "and")
        t = t.replace("(", "").replace(")", "")
        return t

    def get_slug(text):
        t = clean_header(text)
        return t.lower().strip().replace(" ", "-").replace("/", "-")

    content = [
        "# 🎥 Nubenetes Elite Video Hub",
        "",
        "Welcome to the **Agentic Video Hub**. Here we curate the most impactful technical clips, tutorials, and architectural deep-dives for the 2026 Cloud Native landscape.",
        "",
        "## Table of Contents",
        ""
    ]

    categories = sorted(list(set(v["category"] for v in featured_videos)))
    for idx, cat in enumerate(categories, 1):
        clean_cat = clean_header(cat)
        slug = get_slug(cat)
        content.append(f"{idx}. [{clean_cat}](#{slug})")

    content.append("")

    for cat in categories:
        clean_cat = clean_header(cat)
        content.append(f"## {clean_cat}")
        cat_videos = [v for v in featured_videos if v["category"] == cat]
        
        for v in cat_videos:
            content.append(f"### {v['title']}")
            content.append(f"!!! info \"Architectural Summary\"")
            content.append(f"    {v['summary']}")
            content.append("")
            # Optimized iframe with lazy loading
            content.append('<center markdown="1">')
            content.append(f'    <iframe width="560" height="315" src="{v["url"]}" title="{v["title"]}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy"></iframe>')
            content.append('</center>')
            content.append("")

    with open(V2_VIDEOS_PATH, "w") as f:
        f.write("\n".join(content))

    print(f"✅ Generated {V2_VIDEOS_PATH} with {len(featured_videos)} videos.")

if __name__ == "__main__":
    generate_v2_videos()
