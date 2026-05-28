import re
import yaml
import os

# Map category IDs to outline border colors (V2 only)
COLOR_MAP = {
    "ai_advanced_tech": "#8b5cf6",                  # Purple
    "cloud_providers": "#3b82f6",                   # Blue
    "cloud_native_kubernetes": "#10b981",           # Emerald Green
    "devops_cicd_iac": "#f59e0b",                   # Amber Orange
    "observability_databases_storage": "#ec4899",   # Pink
    "dev_testing_collab": "#14b8a6",                # Teal
    "learning_influencers_communities": "#64748b"   # Slate Gray
}

ORIGINAL_V1_ORDER = [
    {'title': 'docker videos', 'url': 'https://www.youtube.com/c/DockerIo'},
    {'title': 'cncf videos', 'url': 'https://www.youtube.com/c/cloudnativefdn'},
    {'title': 'kubernetes logo', 'url': 'https://www.youtube.com/kubernetescommunity'},
    {'title': 'redhat videos', 'url': 'https://www.youtube.com/c/redhat'},
    {'title': 'openshift videos', 'url': 'https://www.youtube.com/c/OpenShift'},
    {'title': 'rancher logo', 'url': 'https://www.youtube.com/c/Rancher'},
    {'title': 'cloudbees videos', 'url': 'https://www.youtube.com/c/CloudBeesTV'},
    {'title': 'jenkins videos', 'url': 'https://www.youtube.com/c/jenkinscicd'},
    {'title': 'jenkins-x videos', 'url': 'https://www.youtube.com/channel/UCN2kblPjXKMcjjVYmwvquvg'},
    {'title': 'spinnaker videos', 'url': 'https://www.youtube.com/channel/UCcxQbw8kT1-FRhFhO2QCetg'},
    {'title': 'vmware tanzu logo', 'url': 'https://www.youtube.com/c/VMwareTanzu'},
    {'title': 'ibm cloud videos', 'url': 'https://www.youtube.com/c/IBMTechnology'},
    {'title': 'aws videos', 'url': 'https://www.youtube.com/c/amazonwebservices'},
    {'title': 'gcp videos', 'url': 'https://www.youtube.com/user/googlecloudplatform'},
    {'title': 'azure videos', 'url': 'https://www.youtube.com/c/MicrosoftAzure'},
    {'title': 'oraclecloud videos', 'url': 'https://www.youtube.com/c/OracleCloudInfrastructure'},
    {'title': 'digitalocean videos', 'url': 'https://www.youtube.com/c/Digitalocean'},
    {'title': 'cloudflare', 'url': 'https://www.youtube.com/cloudflare'},
    {'title': 'scaleway cloud', 'url': 'https://www.youtube.com/c/Scaleway-Cloud'},
    {'title': 'openstack', 'url': 'https://www.youtube.com/c/OpenStackFoundation'},
    {'title': 'harhicorp videos', 'url': 'https://www.youtube.com/c/HashiCorp'},
    {'title': 'pulumi videos', 'url': 'https://www.youtube.com/c/PulumiTV'},
    {'title': 'dzone videos', 'url': 'https://www.youtube.com/c/dzone'},
    {'title': 'prometheus videos', 'url': 'https://www.youtube.com/c/PrometheusIo'},
    {'title': 'grafana videos', 'url': 'https://www.youtube.com/c/Grafana'},
    {'title': 'istio videos', 'url': 'https://www.youtube.com/c/Istio'},
    {'title': 'elastic videos', 'url': 'https://www.youtube.com/c/Elastic'},
    {'title': 'dynatrace videos', 'url': 'https://www.youtube.com/c/dynatrace'},
    {'title': 'appdynamics videos', 'url': 'https://www.youtube.com/c/appdynamics'},
    {'title': 'newrelic videos', 'url': 'https://www.youtube.com/c/NewRelicInc'},
    {'title': 'tigera calico', 'url': 'https://www.youtube.com/channel/UC8uN3yhpeBeerGNwDiQbcgw'},
    {'title': 'weavecloud', 'url': 'https://www.youtube.com/c/WeaveWorksInc'},
    {'title': 'lambdatest', 'url': 'https://www.youtube.com/c/LambdaTest'},
    {'title': 'atlassian videos', 'url': 'https://www.youtube.com/c/Atlassian'},
    {'title': 'vscode videos', 'url': 'https://www.youtube.com/c/Code'},
    {'title': 'github videos', 'url': 'https://www.youtube.com/c/GitHub'},
    {'title': 'gitlab video', 'url': 'https://www.youtube.com/c/Gitlab'},
    {'title': 'gitkraken', 'url': 'https://www.youtube.com/c/Gitkraken'},
    {'title': 'rocketchat videos', 'url': 'https://www.youtube.com/c/RocketChatApp'},
    {'title': 'slack videos', 'url': 'https://www.youtube.com/c/Slackhq'},
    {'title': 'mattermost videos', 'url': 'https://www.youtube.com/c/MattermostHQ'},
    {'title': 'microsoft365', 'url': 'https://www.youtube.com/c/microsoft365'},
    {'title': 'openproject', 'url': 'https://www.youtube.com/c/OpenProjectCommunity'},
    {'title': 'tetrate', 'url': 'https://www.youtube.com/c/Tetrate'},
    {'title': 'rh devel', 'url': 'https://www.youtube.com/c/RedHatDevelopers'},
    {'title': 'spring logo', 'url': 'https://www.youtube.com/user/SpringSourceDev'},
    {'title': 'quarkus logo', 'url': 'https://www.youtube.com/c/Quarkusio'},
    {'title': 'lightbend videos', 'url': 'https://www.youtube.com/c/Lightbend-TV'},
    {'title': 'postman videos', 'url': 'https://www.youtube.com/c/postman'},
    {'title': 'swagger videos', 'url': 'https://www.youtube.com/c/Smartbear'},
    {'title': 'jfrog', 'url': 'https://www.youtube.com/c/JFrogInc'},
    {'title': 'sonatype', 'url': 'https://www.youtube.com/c/Sonatypeinc'},
    {'title': 'sonarsource sonarqube', 'url': 'https://www.youtube.com/channel/UCS5-gTYteN9rnFd98YxYtrA'},
    {'title': 'chrome developers videos', 'url': 'https://www.youtube.com/c/GoogleChromeDevelopers'},
    {'title': 'mozilla developer', 'url': 'https://www.youtube.com/c/MozillaDeveloper'},
    {'title': 'crunchydata', 'url': 'https://www.youtube.com/c/CrunchyDataPostgres'},
    {'title': 'liquibase video', 'url': 'https://www.youtube.com/channel/UC5qMsRjObu685rTBq0PJX8w'},
    {'title': 'cockroachdb', 'url': 'https://www.youtube.com/c/cockroachdb'},
    {'title': 'mongodb', 'url': 'https://www.youtube.com/c/MongoDBofficial'},
    {'title': 'redis', 'url': 'https://www.youtube.com/c/Redisinc'},
    {'title': 'confluent video', 'url': 'https://www.youtube.com/c/Confluent'},
    {'title': 'kubemq video', 'url': 'https://www.youtube.com/channel/UCud7fErZAyMC6lHT_cWZNfA'},
    {'title': 'openebs', 'url': 'https://www.youtube.com/channel/UC3ywadaAUQ1FI4YsHZ8wa0g'},
    {'title': 'storageos', 'url': 'https://www.youtube.com/channel/UCm63IQg81KP9vXRWSHQpu1w'},
    {'title': 'robin', 'url': 'https://www.youtube.com/channel/UCt7N400Z8gB_3yKq1qrjP2w'},
    {'title': 'portworx', 'url': 'https://www.youtube.com/c/Portworx'},
    {'title': 'cloud academy', 'url': 'https://www.youtube.com/c/Cloudacademy'},
    {'title': 'acloudguru', 'url': 'https://www.youtube.com/c/AcloudGuru'},
    {'title': 'devops_tv', 'url': 'https://www.youtube.com/c/Devopsdotcom'},
    {'title': 'xebialabs', 'url': 'https://www.youtube.com/c/XebiaLabs'},
    {'title': 'devops library', 'url': 'https://www.youtube.com/c/Devopslibrary'},
    {'title': 'codecademy', 'url': 'https://www.youtube.com/c/codecademy'},
    {'title': 'coursera', 'url': 'https://www.youtube.com/user/coursera'},
    {'title': 'academind', 'url': 'https://www.youtube.com/c/Academind'},
    {'title': 'guru99', 'url': 'https://www.youtube.com/c/guru99comm'},
    {'title': 'intellipaat', 'url': 'https://www.youtube.com/c/Intellipaat'},
    {'title': 'cloud quick POCs', 'url': 'https://www.youtube.com/channel/UCv9MUffHWyo2GgLIDLVu0KQ'},
    {'title': 'thetips4you', 'url': 'https://www.youtube.com/c/Thetips4you'},
    {'title': 'cloud learnhub', 'url': 'https://www.youtube.com/channel/UC57acx8sCmE7uFHfVMvIlNg'},
    {'title': 'John Savill', 'url': 'https://www.youtube.com/c/NTFAQGuy'},
    {'title': 'microservice factory', 'url': 'https://www.youtube.com/channel/UCorFV-WGnajyfNu4zPI0AAA'},
    {'title': 'kubedb appscode', 'url': 'https://www.youtube.com/c/AppsCodeInc'},
    {'title': 'devops toolkit', 'url': 'https://www.youtube.com/c/DevOpsToolkit'},
    {'title': 'ansible pilot', 'url': 'https://www.youtube.com/c/AnsiblePilot'},
    {'title': 'codelytv', 'url': 'https://www.youtube.com/CodelyTV'},
    {'title': 'pelado nerd', 'url': 'https://www.youtube.com/c/PeladoNerd'},
    {'title': 'hola mundo', 'url': 'https://www.youtube.com/c/HolaMundoDev'},
    {'title': 'javier garzas', 'url': 'https://www.youtube.com/c/JavierGarz%C3%A1s'},
    {'title': 'london IAC', 'url': 'https://www.youtube.com/c/LondonIAC'},
    {'title': 'techworld nana', 'url': 'https://www.youtube.com/c/TechWorldwithNana'},
    {'title': 'honeypot', 'url': 'https://www.youtube.com/c/Honeypotio'},
    {'title': 'Ali Spittel', 'url': 'https://www.youtube.com/c/AliSpittelDev'},
    {'title': 'thomas maurer', 'url': 'https://www.youtube.com/c/ThomasMaurerCloud'},
    {'title': 'freecodecamp', 'url': 'https://www.youtube.com/c/Freecodecamp'},
    {'title': 'thenewstack', 'url': 'https://www.youtube.com/c/TheNewStack'},
    {'title': 'argocd project', 'url': 'https://www.youtube.com/channel/UCOvYmppcbOPm1viN6ust3lA'},
    {'title': 'fluxcd', 'url': 'https://www.youtube.com/channel/UCoZxt-YMhGHb20ZkvcCc5KA'},
    {'title': 'container days', 'url': 'https://www.youtube.com/c/ContainerDays'},
    {'title': 'the cloud girl', 'url': 'https://www.youtube.com/c/priyankavergadia'},
    {'title': 'ContinuousDeliveryFoundation', 'url': 'https://www.youtube.com/c/ContinuousDeliveryFoundation'},
    {'title': 'tina huang', 'url': 'https://www.youtube.com/c/TinaHuang1'},
    {'title': 'azure devops', 'url': 'https://www.youtube.com/c/AzureDevOps'},
    {'title': 'azure cloud native', 'url': 'https://www.youtube.com/channel/UC2Pk9GcHhlVV0R9CQIU6gLw'},
    {'title': 'alibaba cloud', 'url': 'https://www.youtube.com/c/AlibabaCloud'},
    {'title': 'linode cloud', 'url': 'https://www.youtube.com/c/linode'},
    {'title': 'gaia-x', 'url': 'https://www.youtube.com/channel/UCB5WMc2FfrxKzfd7XIODoMw'},
    {'title': 'gps', 'url': 'https://www.youtube.com/c/MadeByGPS'},
    {'title': 'keptn', 'url': 'https://www.youtube.com/c/keptn'},
    {'title': 'anais urlichs', 'url': 'https://www.youtube.com/c/AnaisUrlichs'},
    {'title': 'the digital life', 'url': 'https://www.youtube.com/c/TheDigitalLifeTech'},
    {'title': 'Azure Terraformer', 'url': 'https://www.youtube.com/@azure-terraformer'},
    {'title': 'Ned in the Cloud', 'url': 'https://www.youtube.com/@NedintheCloud'},
    {'title': 'netbox', 'url': 'https://www.youtube.com/@NetBoxLabs'},
    {'title': 'Tech with Helen', 'url': 'https://www.youtube.com/@techwithhelen'},
    {'title': 'bytebytego', 'url': 'https://www.youtube.com/@ByteByteGo'},
    {'title': 'dotcsv', 'url': 'https://www.youtube.com/@DotCSV'},
    {'title': 'midulive', 'url': 'https://www.youtube.com/@midulive'},
    {'title': 'returngis', 'url': 'https://www.youtube.com/@returngis'},
    {'title': 'kubefm', 'url': 'https://www.youtube.com/@kubefm'},
    {'title': 'Olena Kutsenko', 'url': 'https://www.youtube.com/@OlenaKutsenko'},
    {'title': 'mouredev', 'url': 'https://www.youtube.com/@mouredev'},
    {'title': 'CloudNativeMadrid', 'url': 'https://www.youtube.com/@CloudNativeMadrid'},
    {'title': 'kyndryl', 'url': 'https://www.youtube.com/@kyndryl'},
    {'title': 'itopstalk', 'url': 'https://www.youtube.com/@ITOpsTalk'},
    {'title': 'gcp videos', 'url': 'https://www.youtube.com/@googlecloudtech'},
    {'title': 'Google Gemini', 'url': 'https://www.youtube.com/@GoogleGemini'},
    {'title': 'Google DeepMind', 'url': 'https://www.youtube.com/@googledeepmind'},
    {'title': 'Anthropic', 'url': 'https://www.youtube.com/@anthropic-ai'},
    {'title': 'Microsoft Copilot', 'url': 'https://www.youtube.com/@Microsoft.Copilot'},
    {'title': 'OpenAI', 'url': 'https://www.youtube.com/OpenAI'},
    {'title': 'Meta AI', 'url': 'https://www.youtube.com/@aiatmeta'},
    {'title': 'Microsoft Reactor', 'url': 'https://www.youtube.com/@MicrosoftReactor'},
    {'title': 'Playwright', 'url': 'https://www.youtube.com/@Playwrightdev'},
]

def normalize_url(url):
    url = url.lower().strip()
    if url.endswith('/'):
        url = url[:-1]
    return url

def build_v2_mosaic_markdown(yaml_path):
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

def build_v1_mosaic_markdown(yaml_path):
    with open(yaml_path, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)

    # Index current channels by URL and Title
    current_by_url = {}
    current_by_title = {}
    for cat in data['categories']:
        for chan in cat['channels']:
            norm_url = normalize_url(chan['url'])
            current_by_url[norm_url] = chan
            current_by_title[chan['title'].lower()] = chan

    # Reconstruct the list preserving the original V1 order
    ordered_channels = []
    seen_urls = set()

    for old_item in ORIGINAL_V1_ORDER:
        old_title = old_item['title']
        old_url = old_item['url']
        norm_url = normalize_url(old_url)
        
        chan_info = None
        if norm_url in current_by_url:
            chan_info = current_by_url[norm_url]
        elif old_title.lower() in current_by_title:
            chan_info = current_by_title[old_title.lower()]
            
        if chan_info:
            ordered_channels.append(chan_info)
            seen_urls.add(normalize_url(chan_info['url']))
        else:
            # Fallback if some channel in history is not in YAML but we want to preserve it
            pass

    # Append any new channels not present in the original V1 sequence
    for cat in data['categories']:
        for chan in cat['channels']:
            norm_url = normalize_url(chan['url'])
            if norm_url not in seen_urls:
                ordered_channels.append(chan)
                seen_urls.add(norm_url)

    # Now format into rows of 11 channels each
    lines = []
    lines.append('<center markdown="1">')
    lines.append('') # Mandatory blank line after center tag

    row_size = 11
    formatted_channels = []
    for chan in ordered_channels:
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
    yaml_path = os.path.join(repo_root, 'data', 'youtube_channels_mosaic.yaml')
    v1_path = os.path.join(repo_root, 'docs', 'index.md')
    v2_path = os.path.join(repo_root, 'v2-docs', 'index.md')

    new_v1_mosaic = build_v1_mosaic_markdown(yaml_path)
    new_v2_mosaic = build_v2_mosaic_markdown(yaml_path)
    
    update_file(v1_path, new_v1_mosaic)
    update_file(v2_path, new_v2_mosaic)

if __name__ == '__main__':
    main()
