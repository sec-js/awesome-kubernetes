import yaml
import os
import re

INVENTORY_PATH = "data/inventory.yaml"
VIDEOS_DIR = "v2-docs/videos"

def get_target_file(category, technology):
    cat_lower = category.lower()
    tech_lower = technology.lower()
    
    if "agent" in tech_lower or "mcp" in tech_lower or "ai and future operations" in cat_lower:
        return "ai-agents.md", "AI Agents and MCP"
    elif "infrastructure as code" in cat_lower or "security" in cat_lower or "observability" in cat_lower or "monitoring" in cat_lower or "devops" in tech_lower or "iac" in tech_lower or "sre" in tech_lower:
        return "devops-iac.md", "DevOps, IaC, and SRE"
    elif "fundamentals" in cat_lower:
        return "fundamentals.md", "Fundamentals"
    else:
        return "cloud-native.md", "Cloud Native Core"

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

    # Delete old videos.md if it exists
    old_videos_file = "v2-docs/videos.md"
    if os.path.exists(old_videos_file):
        os.remove(old_videos_file)
        print(f"Removed legacy {old_videos_file}")

    os.makedirs(VIDEOS_DIR, exist_ok=True)

    # Helper functions
    def clean_header(text):
        t = re.sub(r'^\d+\.\s*', '', text)
        t = t.replace("&", "and")
        t = re.sub(r'[^a-zA-Z0-9\s-]', ' ', t)
        t = re.sub(r'\s+', ' ', t)
        return t.strip()

    def get_slug(text):
        t = clean_header(text).lower()
        t = re.sub(r'[^a-z0-9\s-]', '', t)
        t = re.sub(r'[\s-]+', '-', t)
        return t.strip('-')

    def is_spanish(title, summary):
        if "[SPANISH CONTENT]" in summary or "[SPANISH CONTENT]" in title:
            return True
        if title.strip().startswith("¿"):
            return True
        return False

    # Group videos by target file
    themed_videos = {}
    for v in featured_videos:
        filename, title = get_target_file(v["category"], v["technology"])
        if filename not in themed_videos:
            themed_videos[filename] = {"title": title, "videos": []}
        themed_videos[filename]["videos"].append(v)

    # Generate each themed MD file
    for filename, theme_info in themed_videos.items():
        theme_title = theme_info["title"]
        videos = theme_info["videos"]
        videos.sort(key=lambda x: x.get("video_order", 999))

        content = [
            f"# 🎥 {theme_title}",
            "",
            f"Welcome to the **{theme_title}** section of the V2 Video Hub. Explore curated high-density videos with architectural summaries.",
            "",
            "## Table of Contents",
            ""
        ]

        # Group by Technology for TOC
        techs = []
        for v in videos:
            tech = v.get("technology", "Cloud Native")
            if tech not in techs:
                techs.append(tech)

        for idx, tech in enumerate(techs, 1):
            clean_tech = clean_header(tech)
            slug = get_slug(tech)
            content.append(f"{idx}. [{clean_tech}](#{slug})")

        content.append("")

        # Render Grouped Videos
        grouped_by_tech = {}
        for v in videos:
            tech = v.get("technology", "Cloud Native")
            if tech not in grouped_by_tech:
                grouped_by_tech[tech] = []
            grouped_by_tech[tech].append(v)

        for tech in techs:
            clean_tech = clean_header(tech)
            content.append(f"## {clean_tech}")
            content.append("")

            for v in grouped_by_tech[tech]:
                summary = v.get("summary", "").strip()
                indented_summary = summary.replace("\n", "\n        ")
                is_sp = is_spanish(v['title'], summary)
                lang_suffix = " [SPANISH CONTENT]" if is_sp else ""

                content.append(f"??? note \"🎬 {v['title']}{lang_suffix}\"")
                content.append(f"    !!! info \"Architectural Summary\"")
                content.append(f"        {indented_summary}")
                content.append("")
                content.append('    <center markdown="1">')
                content.append('')
                content.append(f'    <iframe width="720" height="405" src="{v["url"]}" title="{v["title"]}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy" style="border: 1px solid var(--md-typeset-table-color); border-radius: 8px;"></iframe>')
                content.append('')
                content.append('    </center>')
                content.append("")

        filepath = os.path.join(VIDEOS_DIR, filename)
        with open(filepath, "w") as f:
            f.write("\n".join(content))
        print(f"Generated {filepath} with {len(videos)} videos.")

    # Generate Overview page
    overview_content = [
        "# 🎥 Agentic Video Hub",
        "",
        "Welcome to the **Nubenetes Elite Video Hub**. Discover highly-curated architectural video resources organized into logical learning paths:",
        "",
        "### Learning Dimensions",
        "- 🤖 [**AI Agents and MCP**](./ai-agents.md) — Dive into agentic architectures, tool integration, and Model Context Protocol setups.",
        "- 🛠️ [**DevOps, IaC, and SRE**](./devops-iac.md) — Platform engineering, infrastructure automation with Terraform, SRE, and compliance workflows utilizing AI assistants.",
        "- ☁️ [**Cloud Native Core**](./cloud-native.md) — Architectural strategies, Kubernetes operations, networking, and MLOps platforms.",
        "- 🏁 [**Fundamentals**](./fundamentals.md) — Documentaries, foundational cloud native concepts, and core Strategy tutorials.",
        ""
    ]
    with open(os.path.join(VIDEOS_DIR, "index.md"), "w") as f:
        f.write("\n".join(overview_content))
    print(f"Generated {VIDEOS_DIR}/index.md")

    # Update MkDocs Nav
    update_mkdocs_nav()

def update_mkdocs_nav():
    mkdocs_path = "v2-mkdocs.yml"
    if not os.path.exists(mkdocs_path):
        return
    with open(mkdocs_path, "r") as f:
        content = f.read()

    # Match exact entry and replace with nested list
    old_entry = '- "Agentic Video Hub": videos.md'
    new_entry = """- "Agentic Video Hub":
      - "Overview": videos/index.md
      - "AI Agents and MCP": videos/ai-agents.md
      - "DevOps, IaC, and SRE": videos/devops-iac.md
      - "Cloud Native Core": videos/cloud-native.md
      - "Fundamentals": videos/fundamentals.md"""

    if old_entry in content:
        content = content.replace(old_entry, new_entry)
        with open(mkdocs_path, "w") as f:
            f.write(content)
        print("Updated v2-mkdocs.yml navigation.")
    else:
        print("v2-mkdocs.yml navigation is already updated or entry not found.")

if __name__ == "__main__":
    generate_v2_videos()
