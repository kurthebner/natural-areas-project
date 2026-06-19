#!/usr/bin/env python3
"""
wod_dry_creek_delete_v1.py
Delete OH-WOD-SI-013 (Dry Creek Wildlife Area) from sites.

Reason: Confirmed hallucination. Evidence:
  1. US-24 does not pass through Wood County — the location description
     ("Near US-24 and Township Road 6C, Wood County, OH") is geographically
     impossible.
  2. "Dry Creek Wildlife Area" returns zero matches in ODNR Division of Wildlife
     GIS statewide (gis.ohiodnr.gov, Name_Label LIKE '%DRY CREEK%').
  3. Not present in ODNR Ohio Conservation Lands layer.
  4. Not found on eBird.
  5. "Township Road 6C" cannot be located in Wood County via any mapping source.
  6. Entity was a baseline seed with notes already flagging unconfirmed location.

No related rows exist in site_parent, access_point_parents, or trail_parents.
"""

import sqlite3
import pathlib

DB_PATH = pathlib.Path(__file__).parent.parent / "NASqlite" / "natural_areas_v5.db"
SITE_ID = "OH-WOD-SI-013"


def run():
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row

    # Pre-flight
    row = conn.execute(
        "SELECT site_id, name, category FROM sites WHERE site_id=?", (SITE_ID,)
    ).fetchone()
    if not row:
        print(f"ERROR: {SITE_ID} not found in sites table.")
        conn.close()
        return

    print(f"Found in sites: {row['site_id']} — {row['name']} ({row['category']})")

    # Check for related rows
    checks = [
        ("site_parent",           "site_id"),
        ("site_parent",           "parent_site_id"),
        ("access_point_parents",  "parent_entity_id"),
        ("trail_parents",         "parent_site_id"),
    ]
    for table, col in checks:
        count = conn.execute(
            f"SELECT count(*) FROM {table} WHERE {col}=?", (SITE_ID,)
        ).fetchone()[0]
        if count:
            print(f"WARNING: {count} row(s) in {table}.{col} — review before deleting.")

    try:
        conn.execute("BEGIN")
        conn.execute("DELETE FROM sites WHERE site_id=?", (SITE_ID,))
        conn.commit()
        print(f"  Deleted from sites.")
    except Exception as e:
        conn.rollback()
        print(f"ERROR — rolled back: {e}")
        conn.close()
        return

    # Verify
    remaining = conn.execute(
        "SELECT count(*) FROM sites WHERE site_id=?", (SITE_ID,)
    ).fetchone()[0]
    print(f"sites rows remaining: {remaining}  (expect 0)")
    conn.close()


if __name__ == "__main__":
    run()
