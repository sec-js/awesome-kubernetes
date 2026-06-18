import os
import yaml
from typing import Dict

INVENTORY_PATH = "data/inventory.yaml"

def load_inventory(shard_file: str = None) -> Dict:
    """
    Loads the entire inventory from a single YAML file.
    Legacy/Fast-Track standard restored: Zero-sharding complexity.
    """
    if os.path.exists(INVENTORY_PATH):
        try:
            with open(INVENTORY_PATH, "r") as file:
                return yaml.safe_load(file) or {}
        except: pass
    return {}

def save_inventory(inv: Dict, shard_file: str = None):
    """
    Saves the entire inventory to a single YAML file.
    """
    os.makedirs(os.path.dirname(INVENTORY_PATH), exist_ok=True)
    with open(INVENTORY_PATH, "w") as file:
        yaml.dump(inv, file, sort_keys=False, allow_unicode=True)

def get_shard_name(url: str) -> str:
    # Kept for backward compatibility but unused in single-file mode
    return "inventory.yaml"

def update_inventory_entry(inventory: Dict, norm_url: str, new_data: Dict):
    """
    Updates an inventory entry by merging new_data with existing data,
    preserving metadata keys like 'youtube_mosaic' if they are not in new_data.
    """
    if norm_url not in inventory:
        inventory[norm_url] = {}
    
    existing = inventory[norm_url]
    if isinstance(existing, dict):
        merged = existing.copy()
        merged.update(new_data)
        inventory[norm_url] = merged
    else:
        inventory[norm_url] = new_data

