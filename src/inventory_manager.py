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
