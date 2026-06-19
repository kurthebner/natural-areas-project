#!/usr/bin/env python3
"""
wod_mishe_monoto_disposition_v1.py
Move OH-WOD-SI-073 (Mishe Monoto Preserve) from sites to held_entities.

Reason: entity was committed to Wood County but Appalachia Ohio Alliance
operates in southeast Ohio (Athens/Hocking/Pickaway area) — not Wood County.
Cannot confirm this is a Wood County entity. Hold as unconfirmed_baseline_seed
pending Pickaway County or other relevant county discovery run.

No related rows exist in site_parent, access_point_parents, or trail_parents.
"""

import sqlite3
import pathlib
from datetime import datetime, timezone

DB_PATH = pathlib.Path(__file__).parent.parent / "NASqlite" / "natural_areas_v5.db"
SITE_ID = "OH-WOD-SI-073"
NOW     = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

HOLD_DETAIL = (
    "Baseline seed entry placed in Wood County run but governance entity "
    "(Appalachia Ohio Alliance) operates in southeast Ohio (Athens/Hocking/"
    "Pickaway area), not Wood County. Cannot confirm this is a Wood County "
    "entity. Hold pending Pickaway County or other relevant county discovery "
    "run. If confirmed outside Ohio or non-public, remove entirely."
)

RUN_ID = "wod_mishe_monoto_disposition_2026_05_24"


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

    already = conn.execute(
        "SELECT held_id FROM held_entities WHERE record_id=?", (SITE_ID,)
    ).fetchone()
    if already:
        print(f"WARNING: {SITE_ID} already in held_entities (held_id={already['held_id']}). Aborting.")
        conn.close()
        return

    try:
        conn.execute("BEGIN")

        # Insert into held_entities
        conn.execute("""
            INSERT INTO held_entities
                (record_id, entity_type, name, county, hold_reason, hold_detail, run_id, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            SITE_ID,
            "Site",
            row["name"],
            "Wood",
            "unconfirmed_baseline_seed",
            HOLD_DETAIL,
            RUN_ID,
            NOW,
        ))
        print(f"  Inserted into held_entities.")

        # Delete from sites
        conn.execute("DELETE FROM sites WHERE site_id=?", (SITE_ID,))
        print(f"  Deleted from sites.")

        conn.commit()
        print()
        print("Committed.")

    except Exception as e:
        conn.rollback()
        print(f"ERROR — rolled back: {e}")
        conn.close()
        return

    # Verify
    in_sites = conn.execute(
        "SELECT count(*) FROM sites WHERE site_id=?", (SITE_ID,)
    ).fetchone()[0]
    in_held  = conn.execute(
        "SELECT record_id, hold_reason, hold_detail FROM held_entities WHERE record_id=?", (SITE_ID,)
    ).fetchone()

    print(f"sites rows remaining:    {in_sites}  (expect 0)")
    print(f"held_entities record_id: {in_held['record_id']}")
    print(f"hold_reason:             {in_held['hold_reason']}")
    print(f"hold_detail:             {in_held['hold_detail'][:80]}...")
    conn.close()


if __name__ == "__main__":
    run()
