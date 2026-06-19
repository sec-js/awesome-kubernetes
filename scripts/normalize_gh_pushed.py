"""One-off migration: normalize `gh_pushed` to None.

The enrichment writers historically stored the string "N/A" in the date
field `gh_pushed` when GitHub data was unavailable. That literal reached
`datetime.fromisoformat()` in the safety audit and curator, producing
"Invalid isoformat string: 'N/A'" warnings (and, combined with other null
fields, an aborted audit). The writers now emit None; this script cleans
the existing inventory so the stored data matches.

Usage:
    python3 -m scripts.normalize_gh_pushed --dry-run   # report only
    python3 -m scripts.normalize_gh_pushed             # apply + save (YAML+SQL)

NOTE: save_inventory() round-trips through in-memory SQLite, and SQLite's
iterdump renders REAL columns (e.g. epoch timestamps) with version-specific
float precision. Running this on a machine whose SQLite differs from the one
that generated the committed inventory.sql will rewrite ~all rows with no
semantic change. Run it in CI (same SQLite as the pipeline) so the committed
diff stays limited to the actual gh_pushed values.
"""
import sys

from src.inventory_manager import load_inventory, save_inventory
from src.logger import log_event

BAD_VALUES = {"N/A", "NONE", ""}


def main(dry_run: bool):
    inv = load_inventory()
    changed = 0
    for url, meta in inv.items():
        if not isinstance(meta, dict):
            continue
        pushed = meta.get("gh_pushed")
        if isinstance(pushed, str) and pushed.strip().upper() in BAD_VALUES:
            changed += 1
            if not dry_run:
                meta["gh_pushed"] = None

    log_event(f"[Migration] gh_pushed normalize: {changed} entries with non-date value")
    if dry_run:
        log_event("[Migration] dry-run — no files written")
        return
    if changed:
        save_inventory(inv)
        log_event(f"[Migration] saved inventory (YAML+SQL); normalized {changed} entries")
    else:
        log_event("[Migration] nothing to change")


if __name__ == "__main__":
    main(dry_run="--dry-run" in sys.argv)
