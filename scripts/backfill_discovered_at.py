"""
Backfill script: adds discovered_at to inventory entries that lack it.
Priority: gh_pushed > last_checked > year > default "2024-01-01T00:00:00"
Run once: python -m scripts.backfill_discovered_at
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from datetime import datetime
from src.inventory_manager import load_inventory, save_inventory
from src.config import MADRID_TZ


def backfill():
    inv = load_inventory()
    updated = 0
    total = 0

    for url, entry in inv.items():
        if not isinstance(entry, dict):
            continue
        total += 1
        if entry.get("discovered_at"):
            continue

        discovered = None

        gh_pushed = entry.get("gh_pushed")
        if gh_pushed and isinstance(gh_pushed, str) and len(gh_pushed) >= 10:
            discovered = gh_pushed

        if not discovered:
            last_checked = entry.get("last_checked")
            if isinstance(last_checked, (int, float)) and last_checked > 0:
                try:
                    discovered = datetime.fromtimestamp(last_checked, tz=MADRID_TZ).isoformat()
                except (OSError, ValueError):
                    pass

        if not discovered:
            year = entry.get("year", "")
            if isinstance(year, str) and year.isdigit() and len(year) == 4:
                discovered = f"{year}-06-01T00:00:00+02:00"
            elif isinstance(year, int):
                discovered = f"{year}-06-01T00:00:00+02:00"

        if not discovered:
            discovered = "2024-01-01T00:00:00+02:00"

        entry["discovered_at"] = discovered
        updated += 1

    print(f"Backfill complete: {updated}/{total} entries updated with discovered_at")
    save_inventory(inv)


if __name__ == "__main__":
    backfill()
