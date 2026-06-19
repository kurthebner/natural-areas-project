#!/usr/bin/env python3
"""
han_wpa_duplicates_delete_v1.py
Delete 6 garbled WPA duplicate records from sites (Hancock County).

Root cause: The ODNR GIS LANDS_NAME field concatenates the internal WPA
designation code with "Wildlife Area", producing names like
"Wildlife Production Area 9 Wildlife Area". The pipeline ingested both
LANDS_NAME and Name_Label per polygon and created two records per parcel.

The Name_Label records (S-003 through S-008, "Hancock County Wildlife Area X")
are correct and are retained. The LANDS_NAME artifacts (S-009, S-011–S-015)
are duplicates sharing identical GPS, governance, and acreage.

No related rows exist in site_parent, access_point_parents, or trail_parents
for any of the records being deleted.

Pairs (kept → deleted):
  OH-HAN-S-003  Hancock County Wildlife Area 1  →  OH-HAN-S-009
  OH-HAN-S-004  Hancock County Wildlife Area 3  →  OH-HAN-S-011
  OH-HAN-S-005  Hancock County Wildlife Area 4  →  OH-HAN-S-012
  OH-HAN-S-006  Hancock County Wildlife Area 5  →  OH-HAN-S-013
  OH-HAN-S-007  Hancock County Wildlife Area 6  →  OH-HAN-S-014
  OH-HAN-S-008  Hancock County Wildlife Area 7  →  OH-HAN-S-015
"""

import sqlite3
import pathlib

DB_PATH = pathlib.Path(__file__).parent.parent / "NASqlite" / "natural_areas_v5.db"

DELETE_IDS = [
    "OH-HAN-S-009",   # dup of OH-HAN-S-003
    "OH-HAN-S-011",   # dup of OH-HAN-S-004
    "OH-HAN-S-012",   # dup of OH-HAN-S-005
    "OH-HAN-S-013",   # dup of OH-HAN-S-006
    "OH-HAN-S-014",   # dup of OH-HAN-S-007
    "OH-HAN-S-015",   # dup of OH-HAN-S-008
]


def run():
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row

    # Pre-flight: confirm each target exists and check for related rows
    abort = False
    for sid in DELETE_IDS:
        row = conn.execute(
            "SELECT site_id, name FROM sites WHERE site_id=?", (sid,)
        ).fetchone()
        if not row:
            print(f"WARN: {sid} not found in sites — already deleted?")
            continue
        print(f"  Found: {row['site_id']} — {row['name']}")

        for tbl, col in [("site_parent",          "site_id"),
                         ("site_parent",          "parent_site_id"),
                         ("access_point_parents", "parent_entity_id"),
                         ("trail_parents",        "parent_site_id")]:
            n = conn.execute(
                f"SELECT count(*) FROM {tbl} WHERE {col}=?", (sid,)
            ).fetchone()[0]
            if n:
                print(f"  ERROR: {sid} has {n} row(s) in {tbl}.{col} — aborting.")
                abort = True

    if abort:
        print("Aborting — resolve related rows first.")
        conn.close()
        return

    print()
    try:
        conn.execute("BEGIN")
        placeholders = ",".join("?" * len(DELETE_IDS))
        conn.execute(
            f"DELETE FROM sites WHERE site_id IN ({placeholders})", DELETE_IDS
        )
        conn.commit()
        print(f"Committed: deleted {len(DELETE_IDS)} rows.")
    except Exception as e:
        conn.rollback()
        print(f"ERROR — rolled back: {e}")
        conn.close()
        return

    # Verify
    remaining = conn.execute(
        f"SELECT count(*) FROM sites WHERE site_id IN ({placeholders})", DELETE_IDS
    ).fetchone()[0]
    print(f"Remaining rows for deleted IDs: {remaining}  (expect 0)")

    kept = conn.execute(
        "SELECT site_id, name, gps_lat FROM sites WHERE site_id IN "
        "('OH-HAN-S-003','OH-HAN-S-004','OH-HAN-S-005','OH-HAN-S-006','OH-HAN-S-007','OH-HAN-S-008')"
    ).fetchall()
    print(f"\nRetained records ({len(kept)}):")
    for r in kept:
        print(f"  {r[0]}  {r[1]}  lat={r[2]}")

    conn.close()


if __name__ == "__main__":
    run()
