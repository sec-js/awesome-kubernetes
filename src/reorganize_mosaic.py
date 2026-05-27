import re
import yaml
import os

# Map category IDs to outline border colors
COLOR_MAP = {
    "ai_advanced_tech": "#8b5cf6",                  # Purple
    "cloud_providers": "#3b82f6",                   # Blue
    "cloud_native_kubernetes": "#10b981",           # Emerald Green
    "devops_cicd_iac": "#f59e0b",                   # Amber Orange
    "observability_databases_storage": "#ec4899",   # Pink
    "dev_testing_collab": "#14b8a6",                # Teal
    "learning_influencers_communities": "#64748b"   # Slate Gray
}

def build_mosaic_markdown(yaml_path):
    with open(yaml_path, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)

    lines = []
    lines.append('<center markdown="1">')
    lines.append('')  # Mandatory blank line after center tag

    for cat in data['categories']:
        color = COLOR_MAP.get(cat['id'], '#64748b')
        
        # Open category block container
        # Note: markdown="1" is required inside the HTML tag to process markdown links correctly
        lines.append(f'<div markdown="1" style="border: 1px solid {color}; border-radius: 8px; padding: 10px; margin: 8px 0; background: rgba(255, 255, 255, 0.01);" title="{cat["name"]}">')
        lines.append('') # Mandatory blank line after block tag
        
        # Channel links
        chan_links = []
        for chan in cat['channels']:
            chan_links.append(f"[![{chan['title']}]({chan['image']}){{: style=\"width:48px; height:48px; object-fit:contain; margin:6px;\" .channel-logo}}]({chan['url']})")
        
        lines.append(" ".join(chan_links))
        lines.append('')
        
        # Close container
        lines.append('</div>')
        lines.append('')
        
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
    yaml_path = os.path.join(repo_root, 'data', 'youtube_channels_mosaic.yaml')
    v1_path = os.path.join(repo_root, 'docs', 'index.md')
    v2_path = os.path.join(repo_root, 'v2-docs', 'index.md')

    new_mosaic = build_mosaic_markdown(yaml_path)
    
    update_file(v1_path, new_mosaic)
    update_file(v2_path, new_mosaic)

if __name__ == '__main__':
    main()
