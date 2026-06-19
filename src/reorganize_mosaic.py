import yaml
import os
from src.inventory_manager import load_inventory

# Map category IDs to their friendly names and outline border colors (V2 only)
CATEGORIES = {
    "ai_advanced_tech": {"name": "AI & Advanced Tech", "color": "#8b5cf6"},
    "cloud_providers": {"name": "Cloud Providers & Core Infrastructure", "color": "#3b82f6"},
    "cloud_native_kubernetes": {"name": "Cloud Native Platforms & Kubernetes", "color": "#10b981"},
    "devops_cicd_iac": {"name": "DevOps, CI/CD, IaC & GitOps", "color": "#f59e0b"},
    "observability_databases_storage": {"name": "Observability, Databases & Cloud Storage", "color": "#ec4899"},
    "dev_testing_collab": {"name": "Development, Testing & Collaboration", "color": "#14b8a6"},
    "learning_influencers_communities": {"name": "Tech E-Learning, Influencers & Communities", "color": "#64748b"}
}

def load_inventory_channels():
    inventory = load_inventory()
        
    channels = []
    for url, entry in inventory.items():
        if not isinstance(entry, dict):
            continue
        metadata = entry.get('youtube_mosaic')
        # Every inventory entry carries a 'youtube_mosaic' column that the SQL
        # round-trip materializes as an empty dict {}, so a bare key-presence
        # check matches the entire inventory and explodes the mosaic to ~18k
        # logos. Only treat an entry as a mosaic channel when it actually has
        # mosaic metadata with a logo image.
        if not isinstance(metadata, dict) or not metadata.get('image'):
            continue
        channels.append({
            'title': entry.get('title', 'Unknown Channel'),
            'url': url,
            'image': metadata.get('image', ''),
            'category': metadata.get('category', 'learning_influencers_communities'),
            'order_v1': metadata.get('order_v1', 9999),
            'order_v2': metadata.get('order_v2', 9999)
        })
    return channels

def build_v2_mosaic_markdown_from_channels(channels):
    # Group channels by category
    grouped = {cat_id: [] for cat_id in CATEGORIES.keys()}
    for chan in channels:
        cat_id = chan['category']
        if cat_id in grouped:
            grouped[cat_id].append(chan)
        else:
            grouped.setdefault('learning_influencers_communities', []).append(chan)
            
    lines = []
    lines.append('<center markdown="1">')
    lines.append('')  # Mandatory blank line after center tag

    for cat_id, cat_info in CATEGORIES.items():
        cat_chans = grouped[cat_id]
        if not cat_chans:
            continue
        # Sort within category by order_v2
        cat_chans.sort(key=lambda x: x['order_v2'])
        
        # Open category block container
        lines.append(f'<div markdown="1" style="border: 1px solid {cat_info["color"]}; border-radius: 8px; padding: 10px; margin: 8px 0; background: rgba(255, 255, 255, 0.01);" title="{cat_info["name"]}">')
        lines.append('') # Mandatory blank line after block tag
        
        # Channel links
        chan_links = []
        for chan in cat_chans:
            chan_links.append(f"[![{chan['title']}]({chan['image']}){{: style=\"width:48px; height:48px; object-fit:contain; margin:6px;\" .channel-logo}}]({chan['url']})")
        
        lines.append(" ".join(chan_links))
        lines.append('')
        
        # Close container
        lines.append('</div>')
        lines.append('')
        
    lines.append('</center>')
    return "\n".join(lines)

def build_v2_mosaic_markdown(yaml_path=None):
    # Backward compatible wrapper used by v2_optimizer.py
    channels = load_inventory_channels()
    return build_v2_mosaic_markdown_from_channels(channels)

def build_v1_mosaic_markdown_from_channels(channels):
    # Sort channels by order_v1
    sorted_chans = sorted(channels, key=lambda x: x['order_v1'])
    
    # Now format into rows of 11 channels each
    lines = []
    lines.append('<center markdown="1">')
    lines.append('') # Mandatory blank line after center tag

    row_size = 11
    formatted_channels = []
    for chan in sorted_chans:
        formatted_channels.append(f"[![{chan['title']}]({chan['image']}){{: style=\"width:7%\"}}]({chan['url']})")

    for i in range(0, len(formatted_channels), row_size):
        row = formatted_channels[i:i+row_size]
        line_str = " ".join(row)
        if i + row_size < len(formatted_channels):
            line_str += "<br/>"
        lines.append(line_str)

    lines.append('') # Mandatory blank line before closing center tag
    lines.append('</center>')
    return "\n".join(lines)

def update_file(file_path, new_mosaic):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the specific <center markdown="1"> block containing "docker videos" or "docker_logo.jpg"
    start_tag = '<center markdown="1">'
    end_tag = '</center>'
    
    idx = 0
    found = False
    while True:
        start_pos = content.find(start_tag, idx)
        if start_pos == -1:
            break
        end_pos = content.find(end_tag, start_pos)
        if end_pos == -1:
            break
        
        block = content[start_pos : end_pos + len(end_tag)]
        if 'docker videos' in block or 'docker_logo.jpg' in block:
            content = content[:start_pos] + new_mosaic + content[end_pos + len(end_tag):]
            found = True
            break
        idx = start_pos + len(start_tag)
        
    if not found:
        raise ValueError(f"Could not locate the YouTube channels mosaic block in {file_path}")
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Successfully updated {file_path}")

def main():
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    v1_path = os.path.join(repo_root, 'docs', 'index.md')
    v2_path = os.path.join(repo_root, 'v2-docs', 'index.md')

    channels = load_inventory_channels()
    new_v1_mosaic = build_v1_mosaic_markdown_from_channels(channels)
    new_v2_mosaic = build_v2_mosaic_markdown_from_channels(channels)
    
    update_file(v1_path, new_v1_mosaic)
    update_file(v2_path, new_v2_mosaic)

if __name__ == '__main__':
    main()
