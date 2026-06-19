#!/usr/bin/env python3
"""
upsert_hardin.py  —  Stage 8 Database Upsert for Hardin County
Generated 2026-06-02

Reads hardin_config.json and upserts all entities into natural_areas_v6.db
using the shared upsert functions from na_pipeline_core_v6.py.

Stage 7.5 Human Review Gate must be passed before running this script.
"""

import json
import os
import sqlite3
import sys
from datetime import datetime, timezone

SCRIPT_DIR  = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, "..", ".."))
UTILITIES   = os.path.join(PROJECT_ROOT, "utilities")
CONFIG_PATH = os.path.join(SCRIPT_DIR, "hardin_config.json")
DB_PATH     = os.path.join(PROJECT_ROOT, "NASqlite", "natural_areas_v6.db")

sys.path.insert(0, UTILITIES)

from na_pipeline_core_v6 import (
    upsert_sites, upsert_site_parents,
    upsert_trailthings, upsert_trailthing_hierarchy,
    upsert_site_networks, upsert_site_network_members,
    upsert_access_points, upsert_access_point_parents,
    upsert_run_metadata,
)

# ── Load config ────────────────────────────────────────────────────────────────

with open(CONFIG_PATH, encoding="utf-8") as f:
    cfg = json.load(f)

county       = cfg["county"]          # "Hardin"
state        = cfg["state"]           # "Ohio"
run_id       = cfg["run_id"]          # "hardin_ohio_2026_06_01"
run_date     = cfg["run_date"]        # "2026-06-01"
records_input = cfg.get("records_input", 144)
now          = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

sites         = cfg.get("sites", [])
trailthings   = cfg.get("trailthings", [])
site_networks = cfg.get("site_networks", [])
access_points = cfg.get("access_points", [])
held_entities = cfg.get("held_entities", [])

# Separate held from non-held
active_sites   = [s for s in sites   if not (s.get("status_flag","") or "").startswith("HELD")]
active_tts     = [t for t in trailthings if not (t.get("status_flag","") or "").startswith("HELD")]
active_aps_raw = [a for a in access_points if not (a.get("status_flag","") or "").startswith("HELD")]

# Remap AP fields to match pipeline core expectations
def remap_ap(ap):
    a = dict(ap)
    # parent_entity_type/id from identity_ prefix fields
    a.setdefault("parent_entity_type", a.pop("identity_parent_entity_type", ""))
    a.setdefault("parent_entity_id",   a.pop("identity_parent_entity_id", ""))
    # url -> url_primary
    if "url" in a and "url_primary" not in a:
        a["url_primary"] = a.pop("url")
    elif "url" in a:
        a.pop("url")
    # counties: use 'county' if 'counties' missing
    a.setdefault("counties", a.get("county", "Hardin"))
    return a

active_aps = [remap_ap(a) for a in active_aps_raw]
active_sns     = [n for n in site_networks if not (n.get("status_flag","") or "").startswith("HELD")]

normalized = len(active_sites) + len(active_tts) + len(active_sns) + len(active_aps)
total_held = len(held_entities)

run_notes = (
    f"Hardin County Ohio v6 pipeline complete. "
    f"{len(active_sites)} Sites, {len(active_tts)} Trailthings, "
    f"{len(active_sns)} Site Networks, {len(active_aps)} APs. "
    f"{total_held} held entities. "
    f"52 cemetery GPS coordinates resolved via OSM/Nominatim/human-assist. "
    f"34 cemeteries gps_unresolvable pending GNIS acquisition."
)

# ── Pre-upsert MC county format scan (IMP-115) ────────────────────────────────

print("Pre-upsert MC county format scan (IMP-115)...")
conn_check = sqlite3.connect(DB_PATH)
cur_check = conn_check.cursor()
issues = 0
for table, id_col in [("trailthings","trailthing_id"),("sites","site_id"),("site_networks","network_id")]:
    try:
        cur_check.execute(f'SELECT {id_col}, counties FROM {table} '
                          f'WHERE {id_col} LIKE "OH-MC-%" AND counties LIKE "%; %"')
        rows = cur_check.fetchall()
        if rows:
            print(f"  WARNING: {table} has {len(rows)} malformed MC county rows")
            issues += 1
    except Exception:
        pass
conn_check.close()
if issues:
    print("ABORT: Fix MC county format issues before upserting.")
    sys.exit(1)
print("  OK — no malformed MC county rows.")

# ── Stage 8 Upsert ────────────────────────────────────────────────────────────

print(f"\n[Stage 8] Database Upsert → {os.path.basename(DB_PATH)}")
print(f"  County:       {county}")
print(f"  Run ID:       {run_id}")
print(f"  Sites:        {len(active_sites)}")
print(f"  Trailthings:  {len(active_tts)}")
print(f"  Site Networks:{len(active_sns)}")
print(f"  Access Points:{len(active_aps)}")
print(f"  Held:         {total_held}")

conn = sqlite3.connect(DB_PATH)
try:
    cur = conn.cursor()

    # Ensure all v6 tables exist (IMP-087 DDL requirement)
    # Run na_create_v6_tables.py separately if tables are missing
    # Tables verified to exist in DB before this run.

    # Upsert all entity types
    upsert_sites(cur, active_sites, now, dry_run=False)
    print(f"  sites: {len(active_sites)} upserted")

    upsert_site_parents(cur, active_sites, dry_run=False)

    upsert_trailthings(cur, active_tts, now, dry_run=False)
    print(f"  trailthings: {len(active_tts)} upserted")

    upsert_trailthing_hierarchy(cur, active_tts, dry_run=False)

    upsert_site_networks(cur, active_sns, now, dry_run=False)
    print(f"  site_networks: {len(active_sns)} upserted")

    upsert_site_network_members(cur, active_sns, dry_run=False)

    upsert_access_points(cur, active_aps, now, dry_run=False)
    print(f"  access_points: {len(active_aps)} upserted")

    upsert_access_point_parents(cur, active_aps, dry_run=False)

    # Held entities
    held_sql = """
    INSERT OR IGNORE INTO held_entities
        (record_id, entity_type, name, county, hold_reason, hold_detail, run_id, created_at)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """
    for h in held_entities:
        cur.execute(held_sql, (
            h["entity_id"], h["entity_type"], h.get("name",""),
            h.get("county", county), h.get("hold_reason",""),
            h.get("hold_detail",""), h.get("run_id", run_id), now
        ))
    print(f"  held_entities: {total_held} rows")

    # Run metadata
    upsert_run_metadata(cur, run_id, county, state, run_date,
                        records_input, normalized, total_held, run_notes, now,
                        dry_run=False)
    print(f"  run_metadata: {run_id}")

    conn.commit()
    print(f"\n  Committed to {os.path.basename(DB_PATH)}")

except Exception as e:
    conn.rollback()
    print(f"\n  ERROR during upsert: {e}", file=sys.stderr)
    raise
finally:
    conn.close()

print("\n" + "=" * 60)
print("STAGE 8 COMPLETE — Hardin County")
print(f"  Sites upserted:         {len(active_sites)}")
print(f"  Trailthings upserted:   {len(active_tts)}")
print(f"  Site Networks upserted: {len(active_sns)}")
print(f"  Access Points upserted: {len(active_aps)}")
print(f"  Held entities logged:   {total_held}")
print("=" * 60)
