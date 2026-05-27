import re
import yaml
import os

def build_mosaic_markdown(yaml_path):
    with open(yaml_path, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)

    lines = []
    lines.append('<center markdown="1">')
    lines.append('')  # Mandatory blank line after center tag

    first = True
    for cat in data['categories']:
        if not first:
            lines.append('<br/>')
            lines.append('')
        first = False
        
        # Category header
        lines.append(f"**{cat['name']}**")
        
        # Channel links
        chan_links = []
        for chan in cat['channels']:
            chan_links.append(f"[![{chan['title']}]({chan['image']}){{: style=\"width:7%\"}}]({chan['url']})")
        
        lines.append(" ".join(chan_links))
        lines.append('')
        
    lines.append('</center>')
    return "\n".join(lines)

def update_file(file_path, new_mosaic):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the specific <center markdown="1"> block containing "docker videos"
    # We find where '<center markdown="1">' is, and make sure it has 'docker videos' before the next '</center>'
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
            # This is the target block
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
