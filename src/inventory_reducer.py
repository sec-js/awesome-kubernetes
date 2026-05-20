import os
import json
import yaml
import re
from datetime import datetime
from src.config import GH_TOKEN, TARGET_REPO
from src.gitops_manager import RepositoryController
from src.inventory_manager import load_inventory, save_inventory
from src.gemini_utils import normalize_url

def main():
    git_controller = RepositoryController(GH_TOKEN, TARGET_REPO)
    inventory = load_inventory()
    dead_links = {}
    full_report_metrics = []
    
    # Read all shard JSON artifacts (supports both sharded and single-file result)
    for f in os.listdir("."):
        if f.startswith("shard_result") and f.endswith(".json"):
            try:
                data = json.load(open(f, "r"))
                inventory.update(data.get("inventory_updates", {}))
                dead_links.update(data.get("dead_links", {}))
                full_report_metrics.extend(data.get("full_report_metrics", []))
            except Exception as e:
                print(f"Failed to load {f}: {e}")

    # Apply markdown file updates
    file_updates = {}
    link_registry = {} # Rebuild a minimal link registry for fallback paths
    for root, _, files in os.walk("docs"):
        for f in files:
            if f.endswith(".md"):
                path = os.path.join(root, f)
                content = open(path, "r").read()
                matches = re.finditer(r'\[.*?\]\((https?://.*?)\)', content)
                for m in matches:
                    url = m.group(1)
                    nu = normalize_url(url)
                    link_registry.setdefault(nu, []).append({"file": path})

    for url, (fallback, reason) in dead_links.items():
        nu = normalize_url(url)
        paths = inventory.get(nu, {}).get("v1_locations", [])
        if not paths: paths = [occ["file"] for occ in link_registry.get(nu, [])]
        
        for path in set(paths):
            if not os.path.exists(path): continue
            if path not in file_updates: file_updates[path] = open(path, "r").readlines()
            for i, line in enumerate(file_updates[path]):
                if url in line:
                    if fallback and fallback.startswith("CANONICAL:"):
                        fallback_url = fallback.replace("CANONICAL:", "")
                        line_updated = line.replace(f"({url})", f"({fallback_url})")
                        if line_updated == line:
                            line_updated = re.sub(rf'({re.escape(url)})(?=[)\s]|$)', fallback_url, line)
                        line_updated = line_updated.replace(f"{fallback_url}/", fallback_url)
                        file_updates[path][i] = line_updated
                    else: 
                        file_updates[path][i] = None 

    final_payload = {p: "".join([l for l in lines if l is not None]) for p, lines in file_updates.items()}
    final_payload["data/inventory.yaml"] = None
    
    # Save the updated inventory to disk
    save_inventory(inventory)
    
    # Add main inventory to payload (Fast-Track Single-File)
    if os.path.exists("data/inventory.yaml"):
        final_payload["data/inventory.yaml"] = open("data/inventory.yaml", "r").read()

    metrics = {"full_report": full_report_metrics, "end_date": datetime.now().isoformat()}
    
    if final_payload: 
        from src.safety_guard import SafetyGuard
        report = SafetyGuard().generate_audit_report()
        git_controller.apply_multi_file_changes(final_payload, metrics, safety_report=report)

if __name__ == "__main__":
    main()
