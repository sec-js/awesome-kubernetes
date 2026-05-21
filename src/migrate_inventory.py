import os
from src.inventory_manager import load_inventory, save_inventory

def main():
    print("Loading monolithic inventory.yaml...")
    inv = load_inventory()
    print(f"Loaded {len(inv)} items.")
    
    print("Saving to sharded directory...")
    save_inventory(inv)
    print("Saved successfully.")
    
    if os.path.exists("data/inventory.yaml"):
        os.remove("data/inventory.yaml")
        print("Deleted old data/inventory.yaml.")

if __name__ == "__main__":
    main()
