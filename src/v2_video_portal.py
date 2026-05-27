import yaml
import os
import re

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
                "technology": entry.get("technology", "Cloud Native"),
                "summary": entry.get("ai_summary", entry.get("description", "")),
                "video_order": entry.get("video_order", 999),
                "year": entry.get("year", "N/A")
            })

    if not featured_videos:
        print("No featured videos found in inventory.")
        return

    # Logical category order following the O'Reilly learning flow
    CATEGORY_ORDER = [
        "Fundamentals and Documentaries",
        "Architecture and Cloud Strategy",
        "Infrastructure as Code",
        "Developer Productivity",
        "Observability and Monitoring",
        "Security and Compliance",
        "AI and Future Operations"
    ]

    def category_key(cat):
        try:
            return CATEGORY_ORDER.index(cat)
        except ValueError:
            return len(CATEGORY_ORDER)

    featured_videos.sort(key=lambda x: (category_key(x["category"]), x.get("video_order", 999)))

    def clean_header(text):
        # MANDATE 30: No ampersands, no special characters
        # Also remove the numeric prefix for the final display
        t = re.sub(r'^\d+\.\s*', '', text)
        t = t.replace("&", "and")
        t = t.replace("(", "").replace(")", "")
        return t

    def get_slug(text):
        # Slug should include the numeric prefix to be unique and match TOC
        t = text.replace("&", "and").replace("(", "").replace(")", "")
        return t.lower().strip().replace(" ", "-").replace("/", "-").replace(".", "")

    content = [
        "# 🎥 Nubenetes Elite Video Hub",
        "",
        "Welcome to the **Agentic Video Hub**. This section presents a logical, architectural journey through the Cloud Native landscape, from foundational documentaries to advanced AI operations.",
        "",
        "## Table of Contents",
        ""
    ]

    categories = sorted(list(set(v["category"] for v in featured_videos)), key=category_key)
    for idx, cat in enumerate(categories, 1):
        clean_cat = clean_header(cat)
        slug = get_slug(cat)
        content.append(f"{idx}. [{clean_cat}](#{slug})")

    content.append("")

    for cat in categories:
        clean_cat = clean_header(cat)
        slug = get_slug(cat)
        # Use standard headers (MkDocs generates anchors automatically)
        content.append(f"## {clean_cat}")
        cat_videos = [v for v in featured_videos if v["category"] == cat]
        
        # Sort by video_order within category
        cat_videos.sort(key=lambda x: x.get("video_order", 999))

        for v in cat_videos:
            tech = v.get("technology", "Cloud Native")
            # Ensure summary is correctly indented for multiline blocks
            summary = v.get("summary", "").strip()
            indented_summary = summary.replace("\n", "\n        ")
            
            # Collapsible block per video for better flow
            content.append(f"??? note \"🎬 {v['title']} | `{tech}`\"")
            content.append(f"    !!! info \"Architectural Summary\"")
            content.append(f"        {indented_summary}")
            content.append("")
            content.append('    <center markdown="1">')
            content.append('')
            content.append(f'    <iframe width="720" height="405" src="{v["url"]}" title="{v["title"]}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy" style="border: 1px solid var(--md-typeset-table-color); border-radius: 8px;"></iframe>')
            content.append('')
            content.append('    </center>')
            content.append("")

    with open(V2_VIDEOS_PATH, "w") as f:
        f.write("\n".join(content))

    print(f"✅ Generated {V2_VIDEOS_PATH} with {len(featured_videos)} videos.")

if __name__ == "__main__":
    generate_v2_videos()
