import os
import yaml
import hashlib
from typing import Dict

INVENTORY_DIR = "data/inventory"
TOTAL_SHARDS = 64

def get_shard_name(url: str) -> str:
    if not url: return f"shard_00.yaml"
    hash_val = int(hashlib.md5(url.encode('utf-8')).hexdigest(), 16)
    return f"shard_{hash_val % TOTAL_SHARDS:02d}.yaml"

def load_inventory(shard_file: str = None) -> Dict:
    """
    Loads the entire inventory. 
    Mandate 47 Optimization: Always loads the legacy data/inventory.yaml first as a global base
    to ensure Fast-Track context is available even in sharded runs.
    """
    inv = {}
    
    # 1. Load Legacy Global Base (Crucial for context)
    if os.path.exists("data/inventory.yaml"):
        try:
            with open("data/inventory.yaml", "r") as file:
                inv = yaml.safe_load(file) or {}
        except: pass

    # 2. Overwrite with Sharded data if exists
    if shard_file:
        path = os.path.join(INVENTORY_DIR, shard_file)
        if os.path.exists(path):
            try:
                with open(path, 'r') as file:
                    shard_data = yaml.safe_load(file) or {}
                    inv.update(shard_data)
            except: pass
        return inv

    # 3. Load all shards into base
    if os.path.exists(INVENTORY_DIR):
        for f in os.listdir(INVENTORY_DIR):
            if f.endswith('.yaml'):
                try:
                    with open(os.path.join(INVENTORY_DIR, f), 'r') as file:
                        shard_data = yaml.safe_load(file) or {}
                        inv.update(shard_data)
                except: pass
                
    return inv

def save_inventory(inv: Dict, shard_file: str = None):
    """
    Saves the entire inventory split by hash, or saves a specific shard file directly.
    """
    os.makedirs(INVENTORY_DIR, exist_ok=True)
    
    shards = {}
    for url, data in inv.items():
        shard = get_shard_name(url)
        shards.setdefault(shard, {})[url] = data
        
    if shard_file:
        # Save only the specified shard
        if shard_file in shards:
            with open(os.path.join(INVENTORY_DIR, shard_file), "w") as file:
                yaml.dump(shards[shard_file], file, sort_keys=False, allow_unicode=True)
        return

    # Save all shards
    for shard, s_data in shards.items():
        with open(os.path.join(INVENTORY_DIR, shard), "w") as file:
            yaml.dump(s_data, file, sort_keys=False, allow_unicode=True)

