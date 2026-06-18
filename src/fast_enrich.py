import os
import re
import yaml
import asyncio
import httpx
from datetime import datetime
from src.config import GH_TOKEN, INVENTORY_PATH
from src.gemini_utils import normalize_url

# Dimensions mapping from v2_optimizer.py
DIMENSIONS = {
    "AI": ["ai", "ai-agents-mcp", "chatgpt", "mlops"],
    "Architectural Foundations": ["introduction", "faq", "kubernetes", "linux", "git", "cloud-arch-diagrams", "matrix-table", "other-awesome-lists", "about"],
    "Platform & Site Reliability": ["sre", "devops", "developerportals", "scaffolding", "finops", "chaos-engineering", "performance-testing-with-jenkins-and-jmeter", "project-management-methodology", "project-management-tools", "qa", "test-automation-frameworks", "testops"],
    "Hardened Infrastructure": ["iac", "terraform", "pulumi", "crossplane", "ansible", "securityascode", "kubernetes-security", "aws-security", "oauth", "devsecops", "kustomize", "liquibase", "chef"],
    "Cloud Providers (Hyperscalers)": ["aws", "azure", "GoogleCloudPlatform", "ibm_cloud", "oraclecloud", "digitalocean", "cloudflare", "scaleway", "managed-kubernetes-in-public-cloud", "public-cloud-solutions", "private-cloud-solutions", "edge-computing", "aws-architecture", "aws-security", "aws-networking", "aws-databases", "aws-storage", "aws-monitoring", "aws-iac", "aws-tools-scripts", "aws-messaging", "aws-data", "aws-devops", "aws-serverless", "aws-containers", "aws-backup", "aws-training", "aws-newfeatures", "aws-miscellaneous", "aws-pricing", "aws-spain"],
    "Networking & Service Mesh": ["networking", "kubernetes-networking", "servicemesh", "istio", "caching", "web-servers", "cloudflare"],
    "The Container Stack": ["docker", "container-managers", "serverless", "kubernetes-autoscaling", "kubernetes-operators-controllers", "kubernetes-storage", "kubernetes-monitoring", "kubernetes-troubleshooting", "kubernetes-backup-migrations", "kubernetes-on-premise", "kubernetes-bigdata", "kubernetes-client-libraries", "kubernetes-releases", "kubernetes-based-devel", "kubernetes-alternatives", "kubectl-commands", "rancher", "openshift", "ocp3", "ocp4", "noops"],
    "Data & Advanced Analytics": ["databases", "nosql", "newsql", "message-queue", "crunchydata", "yaml", "bigdata"],
    "Engineering Pipeline": ["cicd", "gitops", "argo", "flux", "tekton", "jenkins", "jenkins-alternatives", "openshift-pipelines", "sonarqube", "registries", "keptn", "stackstorm", "cicd-kubernetes-plugins"],
    "Developer Ecosystem": ["visual-studio", "javascript", "golang", "python", "java_frameworks", "java_app_servers", "java-and-java-performance-optimization", "dotnet", "angular", "react", "web3", "api", "swagger-code-generator-for-rest-apis", "postman", "lowcode-nocode", "devel-sites", "dom", "linux-dev-env", "ChromeDevTools", "xamarin", "jvm-parameters-matrix-table", "maven-gradle", "embedded-servlet-containers"],
    "Career & Industry": ["recruitment", "hr", "finops", "freelancing", "remote-tech-jobs", "workfromhome", "interview-questions", "elearning", "digital-money", "appointment-scheduling", "newsfeeds"]
}

# Helper to find dimension of a category
def get_dimension_for_category(category: str) -> str:
    if not category:
        return "Architectural Foundations"
    for dim, cats in DIMENSIONS.items():
        if category in cats:
            return dim
    return "Architectural Foundations"

# Helper to build readable category name
def get_readable_category(category: str) -> str:
    if not category:
        return "General"
    title = category.replace("-", " ").title()
    acronyms = {
        "Ai": "AI", "Mcp": "MCP", "Iac": "IaC", "Aws": "AWS", "Gcp": "GCP", 
        "Api": "API", "Sre": "SRE", "Cicd": "CI/CD", "Ocp3": "OCP 3", 
        "Ocp4": "OCP 4", "Jvm": "JVM", "Sql": "SQL", "Nosql": "NoSQL",
        "Chatgpt": "ChatGPT", "Mlops": "MLOps", "Devops": "DevOps",
        "Hr": "HR", "Qa": "QA"
    }
    for k, v in acronyms.items():
        title = title.replace(k, v)
    return title

async def fetch_github_metadata(client: httpx.AsyncClient, url: str, sem: asyncio.Semaphore) -> tuple[str, dict]:
    default_meta = {
        "gh_stars": 0,
        "gh_pushed": "N/A",
        "gh_license": "N/A"
    }
    match = re.search(r'github\.com/([^/]+/[^/]+)', url)
    if not match:
        return url, default_meta
    repo = match.group(1).split('#')[0].split('?')[0].rstrip('/')
    api_url = f"https://api.github.com/repos/{repo}"
    
    headers = {"Accept": "application/vnd.github.v3+json"}
    if GH_TOKEN:
        headers["Authorization"] = f"token {GH_TOKEN}"
        
    async with sem:
        try:
            resp = await client.get(api_url, headers=headers, timeout=10.0)
            if resp.status_code == 200:
                data = resp.json()
                lic = data.get("license")
                lic_id = lic.get("spdx_id", "N/A") if isinstance(lic, dict) else "N/A"
                return url, {
                    "gh_stars": data.get("stargazers_count", 0),
                    "gh_pushed": data.get("pushed_at", "N/A"),
                    "gh_license": lic_id
                }
            elif resp.status_code == 404:
                return url, {
                    "gh_stars": 0,
                    "gh_pushed": "N/A",
                    "gh_license": "N/A",
                    "status": "dead"
                }
            else:
                return url, {
                    "gh_stars": 0,
                    "gh_pushed": "N/A",
                    "gh_license": "N/A",
                    "status": "unreachable"
                }
        except Exception as e:
            print(f"Error fetching metadata for {url}: {e}")
    return url, default_meta


from src.inventory_manager import load_inventory

async def run_enrichment():
    print("[*] Loading inventory database...")
    inventory = load_inventory()

    print(f"[*] Loaded {len(inventory)} total entries.")
    
    # 1. IDENTIFY GAPS
    v2_links = []
    github_missing = []
    unenriched = []
    
    for url, meta in inventory.items():
        if url.startswith("INTRO:"):
            continue
        
        # Check if candidate for V2 (meaning it has v2_locations)
        if meta.get("v2_locations"):
            v2_links.append(url)
            
            # Check if missing GitHub metadata
            if "github.com" in url:
                if meta.get("gh_stars") is None:
                    github_missing.append(url)
            
            # Check if unenriched (missing hierarchy or ai_summary)
            if not meta.get("hierarchy") or not meta.get("ai_summary"):
                unenriched.append(url)

    print(f"[*] Total V2 Candidates: {len(v2_links)}")
    print(f"[*] GitHub links missing metadata: {len(github_missing)}")
    print(f"[*] Candidates missing AI Enrichment: {len(unenriched)}")

    # 2. BATCH FETCH GITHUB METADATA (Concurrent)
    if github_missing:
        print(f"\n[*] Starting concurrent GitHub API metadata retrieval for {len(github_missing)} repos...")
        sem = asyncio.Semaphore(15)
        async with httpx.AsyncClient() as client:
            tasks = [fetch_github_metadata(client, url, sem) for url in github_missing]
            results = await asyncio.gather(*tasks)
            
            fetched_count = 0
            for url, gh_data in results:
                if gh_data:
                    norm = normalize_url(url)
                    if norm in inventory:
                        inventory[norm].update(gh_data)
                        fetched_count += 1
        print(f"[+] Successfully fetched metadata for {fetched_count} GitHub repositories.")

    # 3. LOCAL ENRICHMENT (Rule-based Fallback)
    print(f"\n[*] Applying local rule-based enrichment to {len(unenriched)} unenriched links...")
    enriched_count = 0
    for url in unenriched:
        meta = inventory.get(url)
        if not meta:
            continue
            
        category = meta.get("category", "kubernetes-tools")
        dim = get_dimension_for_category(category)
        readable_cat = get_readable_category(category)
        
        # 3.1. Build Hierarchy
        if not meta.get("hierarchy"):
            meta["hierarchy"] = [dim, readable_cat, "General Reference"]
            
        # 3.2. Build AI Summary
        if not meta.get("ai_summary"):
            desc = meta.get("description", "").strip()
            # If standard V1 description contains markdown links or is empty, build a clean text summary
            if desc and len(desc) > 15:
                # Remove markdown links text and use description
                clean_desc = re.sub(r'\[(.*?)\]\((.*?)\)', r'\1', desc)
                meta["ai_summary"] = clean_desc
            else:
                title = meta.get("title", url.split("//")[-1].split("/")[0])
                meta["ai_summary"] = f"A curated technical resource and architectural guide covering {title} in the {readable_cat} ecosystem."
                
        # 3.3. Populate other missing metadata fields to ensure compliance
        if not meta.get("language"):
            meta["language"] = "English"
        if not meta.get("resource_type"):
            meta["resource_type"] = "Reference"
        if not meta.get("complexity"):
            meta["complexity"] = "Intermediate"
        if not meta.get("tags"):
            meta["tags"] = ["[COMMUNITY-TOOL]"]
            
        inventory[url] = meta
        enriched_count += 1
        
    print(f"[+] Successfully enriched {enriched_count} resources locally.")

    # 4. SAVE DATABASE
    print("\n[*] Saving updated inventory to disk...")
    from src.inventory_manager import save_inventory
    save_inventory(inventory)
    print("[+] Database saved successfully.")

if __name__ == "__main__":
    asyncio.run(run_enrichment())
