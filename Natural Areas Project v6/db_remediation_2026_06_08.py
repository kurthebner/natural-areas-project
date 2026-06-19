#!/usr/bin/env python3
"""
Natural Areas DB — ID Integrity Remediation Script
Generated: 2026-06-08

Fixes all 12 issues identified in db_id_audit_2026_06_08.md, in order:

  Phase 1: MC-T collision — rebase 16 old 3-digit MC-T records to 0200+
  Phase 2: MC-TR → MC-T (type code fix, 6 records)
  Phase 3: MC-SI → MC-S (type code fix, 3 records)
  Phase 4: OTT-AP-006 moved from sites table to access_points table
  Phase 5: Single-county wrong type codes → correct type + 4-digit
             WOD-SI → WOD-S, FUL-SI → FUL-S,
             WIL/WOD/FUL -TR → -T,
             PUT-A → PUT-AP
  Phase 6: SEED- IDs in held_entities → proper OH-HAR-S-0xxx IDs
           OH-WOD-SEED-xxx → OH-WOD-S-0xxx
  Phase 7: All remaining 3-digit single-county IDs → 4-digit

USAGE:
    python db_remediation_2026_06_08.py [--db PATH] [--dry-run]

OPTIONS:
    --db PATH    Path to the SQLite database (default: NASqlite/natural_areas_v6.db
                 relative to the script's directory)
    --dry-run    Print all SQL without executing; roll back at the end
"""

import sqlite3
import sys
import argparse
import os
from datetime import datetime, timezone

# ---------------------------------------------------------------------------
# CONFIG
# ---------------------------------------------------------------------------

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_DB = os.path.join(SCRIPT_DIR, "NASqlite", "natural_areas_v6.db")

# ---------------------------------------------------------------------------
# RENAME ENGINE
# ---------------------------------------------------------------------------
# For each entity type, define which tables and columns hold that ID.
# Format: list of (table, column) pairs to UPDATE when that entity type's ID changes.

ENTITY_FK_MAP = {
    # entity_type_key: (primary_table, pk_col, [(fk_table, fk_col), ...])
    "site": (
        "sites", "site_id",
        [
            ("site_parent",          "site_id"),
            ("site_parent",          "parent_site_id"),
            ("site_network_members", "site_id"),
            ("trail_parents",        "parent_site_id"),
            ("access_point_parents", "parent_entity_id"),  # only where parent_entity_type='Site'
            ("discovery_provenance", "entity_id"),
            ("resolution_provenance","entity_id"),
            ("normalization_provenance","entity_id"),
            ("held_entities",        "record_id"),
            ("entity_conflicts",     "entity_id"),
            ("entity_uncertainty",   "entity_id"),
            ("entity_geometry",      "entity_id"),
            ("manual_review_queue",  "record_id"),
        ],
    ),
    "trail": (
        "trails", "trail_id",
        [
            ("trail_parents",        "trail_id"),
            ("trail_to_segment",     "trail_id"),
            ("trail_network_members","trail_id"),
            ("access_point_parents", "parent_entity_id"),  # where parent_entity_type='Trail'
            ("discovery_provenance", "entity_id"),
            ("resolution_provenance","entity_id"),
            ("normalization_provenance","entity_id"),
            ("held_entities",        "record_id"),
            ("entity_conflicts",     "entity_id"),
            ("entity_uncertainty",   "entity_id"),
            ("entity_geometry",      "entity_id"),
            ("manual_review_queue",  "record_id"),
        ],
    ),
    "trail_segment": (
        "trail_segments", "segment_id",
        [
            ("trail_to_segment",     "segment_id"),
            ("discovery_provenance", "entity_id"),
            ("resolution_provenance","entity_id"),
            ("normalization_provenance","entity_id"),
            ("held_entities",        "record_id"),
            ("entity_conflicts",     "entity_id"),
            ("entity_geometry",      "entity_id"),
        ],
    ),
    "trail_network": (
        "trail_networks", "network_id",
        [
            ("trail_network_members","network_id"),
            ("discovery_provenance", "entity_id"),
            ("resolution_provenance","entity_id"),
            ("normalization_provenance","entity_id"),
            ("held_entities",        "record_id"),
            ("entity_conflicts",     "entity_id"),
            ("entity_geometry",      "entity_id"),
        ],
    ),
    "site_network": (
        "site_networks", "network_id",
        [
            ("site_network_members", "network_id"),
            ("discovery_provenance", "entity_id"),
            ("resolution_provenance","entity_id"),
            ("normalization_provenance","entity_id"),
            ("held_entities",        "record_id"),
            ("entity_conflicts",     "entity_id"),
            ("entity_geometry",      "entity_id"),
        ],
    ),
    "trailthing": (
        "trailthings", "trailthing_id",
        [
            ("trailthing_hierarchy", "parent_id"),
            ("trailthing_hierarchy", "child_id"),
            ("access_point_parents","parent_entity_id"),  # where parent_entity_type='Trailthing'
            ("discovery_provenance", "entity_id"),
            ("resolution_provenance","entity_id"),
            ("normalization_provenance","entity_id"),
            ("held_entities",        "record_id"),
            ("entity_conflicts",     "entity_id"),
            ("entity_geometry",      "entity_id"),
        ],
    ),
    "access_point": (
        "access_points", "access_point_id",
        [
            ("access_point_parents", "access_point_id"),
            ("discovery_provenance", "entity_id"),
            ("resolution_provenance","entity_id"),
            ("normalization_provenance","entity_id"),
            ("held_entities",        "record_id"),
            ("entity_conflicts",     "entity_id"),
            ("entity_geometry",      "entity_id"),
            ("manual_review_queue",  "record_id"),
        ],
    ),
    # held-only entities (no primary entity table)
    "held_only": (
        None, None,
        [
            ("held_entities",        "record_id"),
            ("manual_review_queue",  "record_id"),
        ],
    ),
}


def rename_entity(cur, entity_type_key, old_id, new_id, dry_run=False):
    """Rename a single entity ID across its primary table and all FK tables."""
    primary_table, pk_col, fk_refs = ENTITY_FK_MAP[entity_type_key]

    statements = []

    # Primary table UPDATE
    if primary_table:
        statements.append(
            (f"UPDATE {primary_table} SET {pk_col}=? WHERE {pk_col}=?", (new_id, old_id))
        )

    # FK table UPDATEs
    for fk_table, fk_col in fk_refs:
        statements.append(
            (f"UPDATE {fk_table} SET {fk_col}=? WHERE {fk_col}=?", (new_id, old_id))
        )

    for sql, params in statements:
        if dry_run:
            print(f"  SQL: {sql}  PARAMS: {params}")
        else:
            cur.execute(sql, params)


def rename_batch(cur, entity_type_key, mapping, label, dry_run=False):
    """Apply a batch of old→new renames. mapping is list of (old_id, new_id)."""
    print(f"\n--- {label} ({len(mapping)} renames) ---")
    for old_id, new_id in mapping:
        print(f"  {old_id}  →  {new_id}")
        rename_entity(cur, entity_type_key, old_id, new_id, dry_run)


# ---------------------------------------------------------------------------
# PHASE DEFINITIONS
# ---------------------------------------------------------------------------

def build_phase1_mc_t_collision(cur):
    """Rebase 16 old 3-digit MC-T records to OH-MC-T-0200+."""
    cur.execute(
        "SELECT trail_id FROM trails WHERE trail_id GLOB 'OH-MC-T-[0-9][0-9][0-9]' ORDER BY trail_id"
    )
    old_ids = [r[0] for r in cur.fetchall()]
    mapping = []
    for i, old_id in enumerate(old_ids):
        new_id = f"OH-MC-T-{200 + i:04d}"
        mapping.append((old_id, new_id))
    return mapping


def build_phase2_mc_tr(cur):
    """Rename MC-TR → MC-T starting at OH-MC-T-0216."""
    cur.execute(
        "SELECT trail_id FROM trails WHERE trail_id LIKE 'OH-MC-TR-%' ORDER BY trail_id"
    )
    old_ids = [r[0] for r in cur.fetchall()]
    mapping = []
    for i, old_id in enumerate(old_ids):
        new_id = f"OH-MC-T-{216 + i:04d}"
        mapping.append((old_id, new_id))
    return mapping


def build_phase3_mc_si(cur):
    """Rename MC-SI → MC-S, continuing after current max MC-S (0029 → 0030+)."""
    cur.execute(
        "SELECT site_id FROM sites WHERE site_id LIKE 'OH-MC-SI-%' ORDER BY site_id"
    )
    old_ids = [r[0] for r in cur.fetchall()]
    # Current max 4-digit MC-S
    cur.execute(
        "SELECT MAX(CAST(SUBSTR(site_id,-4) AS INT)) FROM sites WHERE site_id GLOB 'OH-MC-S-[0-9][0-9][0-9][0-9]'"
    )
    max_seq = cur.fetchone()[0] or 0
    mapping = []
    for i, old_id in enumerate(old_ids):
        new_id = f"OH-MC-S-{max_seq + 1 + i:04d}"
        mapping.append((old_id, new_id))
    return mapping


def phase4_ott_ap_wrong_table(cur, dry_run=False):
    """Move OH-OTT-AP-006 from sites table into access_points."""
    print("\n--- Phase 4: OTT-AP-006 wrong table ---")

    # Fetch the record from sites
    cur.execute("SELECT * FROM sites WHERE site_id='OH-OTT-AP-006'")
    row = cur.fetchone()
    if not row:
        print("  OH-OTT-AP-006 not found in sites — skipping")
        return

    cur.execute("PRAGMA table_info(sites)")
    site_cols = {r[1]: row[i] for i, r in enumerate(cur.fetchall())}

    # Check access_points schema
    cur.execute("PRAGMA table_info(access_points)")
    ap_cols = [r[1] for r in cur.fetchall()]

    # Map site fields → access_point fields
    # This entity is a boat launch (township access point to a water body)
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    ap_record = {
        "access_point_id":   "OH-OTT-AP-006",
        "name":              site_cols.get("name"),
        "ap_type":           "Boat Launch",
        "status":            site_cols.get("status"),
        "parent_entity_type": None,
        "parent_entity_id":  None,
        "county":            "Ottawa",
        "township":          site_cols.get("township"),
        "municipality":      site_cols.get("municipality"),
        "address":           site_cols.get("location"),
        "gps_lat":           site_cols.get("gps_lat"),
        "gps_lon":           site_cols.get("gps_lon"),
        "plus_code":         site_cols.get("plus_code"),
        "features":          site_cols.get("features"),
        "identity_notes":    site_cols.get("identity_notes"),
        "notes":             site_cols.get("notes"),
        "url_primary":       site_cols.get("url_primary"),
        "created_at":        site_cols.get("created_at", now),
        "updated_at":        now,
        "last_verified_date": site_cols.get("last_verified_date", ""),
        "field_verified":    site_cols.get("field_verified", 0),
        "counties":          site_cols.get("counties", "Ottawa"),
        "description":       site_cols.get("description", ""),
        "location":          site_cols.get("location", ""),
        "urls":              site_cols.get("urls", ""),
    }

    # Build INSERT using only columns that exist in access_points
    insert_cols = [c for c in ap_cols if c in ap_record]
    vals = [ap_record[c] for c in insert_cols]
    placeholders = ",".join(["?"] * len(insert_cols))
    insert_sql = f"INSERT INTO access_points ({','.join(insert_cols)}) VALUES ({placeholders})"
    delete_sql = "DELETE FROM sites WHERE site_id='OH-OTT-AP-006'"

    # Also update discovery_provenance to fix entity_id reference
    prov_update_sql = "UPDATE discovery_provenance SET entity_type='Access Point' WHERE entity_id='OH-OTT-AP-006' AND entity_type='Site'"

    if dry_run:
        print(f"  INSERT: {insert_sql}")
        print(f"  DELETE: {delete_sql}")
        print(f"  PROV:   {prov_update_sql}")
    else:
        cur.execute(insert_sql, vals)
        cur.execute(delete_sql)
        cur.execute(prov_update_sql)
        print(f"  Moved OH-OTT-AP-006 (West Harbor Boat Launch) → access_points")


def build_phase5_wrong_type_codes(cur):
    """
    Fix single-county wrong type codes. Each group gets the correct type code
    and 4-digit zero-padded sequence, preserving the original sequence number.
    """
    mapping_sites = []
    mapping_trails = []
    mapping_aps = []

    # WOD-SI → WOD-S-0xxx (preserve seq number)
    cur.execute("SELECT site_id FROM sites WHERE site_id GLOB 'OH-WOD-SI-[0-9][0-9][0-9]' ORDER BY site_id")
    for (old_id,) in cur.fetchall():
        seq = int(old_id.split("-")[-1])
        mapping_sites.append((old_id, f"OH-WOD-S-{seq:04d}"))

    # FUL-SI → FUL-S-0xxx
    cur.execute("SELECT site_id FROM sites WHERE site_id GLOB 'OH-FUL-SI-[0-9][0-9][0-9]' ORDER BY site_id")
    for (old_id,) in cur.fetchall():
        seq = int(old_id.split("-")[-1])
        mapping_sites.append((old_id, f"OH-FUL-S-{seq:04d}"))

    # WIL-TR → WIL-T-0xxx
    cur.execute("SELECT trail_id FROM trails WHERE trail_id GLOB 'OH-WIL-TR-[0-9][0-9][0-9]' ORDER BY trail_id")
    for (old_id,) in cur.fetchall():
        seq = int(old_id.split("-")[-1])
        mapping_trails.append((old_id, f"OH-WIL-T-{seq:04d}"))

    # WOD-TR → WOD-T-0xxx
    cur.execute("SELECT trail_id FROM trails WHERE trail_id GLOB 'OH-WOD-TR-[0-9][0-9][0-9]' ORDER BY trail_id")
    for (old_id,) in cur.fetchall():
        seq = int(old_id.split("-")[-1])
        mapping_trails.append((old_id, f"OH-WOD-T-{seq:04d}"))

    # FUL-TR → FUL-T-0xxx
    cur.execute("SELECT trail_id FROM trails WHERE trail_id GLOB 'OH-FUL-TR-[0-9][0-9][0-9]' ORDER BY trail_id")
    for (old_id,) in cur.fetchall():
        seq = int(old_id.split("-")[-1])
        mapping_trails.append((old_id, f"OH-FUL-T-{seq:04d}"))

    # PUT-A → PUT-AP-0xxx
    cur.execute("SELECT access_point_id FROM access_points WHERE access_point_id GLOB 'OH-PUT-A-[0-9][0-9][0-9]' ORDER BY access_point_id")
    for (old_id,) in cur.fetchall():
        seq = int(old_id.split("-")[-1])
        mapping_aps.append((old_id, f"OH-PUT-AP-{seq:04d}"))

    return mapping_sites, mapping_trails, mapping_aps


def build_phase6_seed_ids(cur):
    """
    Assign proper OH-HAR-S-0xxx IDs to SEED- held_entities records.
    Assign OH-WOD-S-0xxx IDs to OH-WOD-SEED-xxx records.
    These are held_only (no primary entity table row).
    """
    mapping_har = []
    mapping_wod = []

    # SEED- records (Hardin)
    cur.execute(
        "SELECT record_id FROM held_entities WHERE record_id NOT LIKE 'OH-%' ORDER BY record_id"
    )
    seed_ids = [r[0] for r in cur.fetchall()]

    # Current max HAR-S 3-digit (will be 4-digit after phase 7 — but phase 6 runs before 7,
    # so we base off 3-digit max and assign 4-digit directly)
    cur.execute(
        "SELECT MAX(CAST(SUBSTR(site_id,-3) AS INT)) FROM sites WHERE site_id GLOB 'OH-HAR-S-[0-9][0-9][0-9]'"
    )
    max_har = cur.fetchone()[0] or 0
    # Also check held entities for existing HAR-S assignments
    cur.execute(
        "SELECT MAX(CAST(SUBSTR(record_id,-3) AS INT)) FROM held_entities WHERE record_id GLOB 'OH-HAR-S-[0-9][0-9][0-9]'"
    )
    max_har_held = cur.fetchone()[0] or 0
    max_har = max(max_har, max_har_held)

    for i, old_id in enumerate(seed_ids):
        new_id = f"OH-HAR-S-{max_har + 1 + i:04d}"
        mapping_har.append((old_id, new_id))

    # WOD-SEED records
    cur.execute(
        "SELECT record_id FROM held_entities WHERE record_id LIKE 'OH-WOD-SEED-%' ORDER BY record_id"
    )
    wod_seed_ids = [r[0] for r in cur.fetchall()]

    # Phase 5 has already renamed WOD-SI → WOD-S by the time this runs,
    # so query WOD-S (not WOD-SI) in both sites and held_entities.
    cur.execute(
        "SELECT MAX(CAST(SUBSTR(site_id,-4) AS INT)) FROM sites WHERE site_id GLOB 'OH-WOD-S-[0-9][0-9][0-9][0-9]'"
    )
    max_wod_sites = cur.fetchone()[0] or 0
    cur.execute(
        "SELECT MAX(CAST(SUBSTR(record_id,-4) AS INT)) FROM held_entities WHERE record_id GLOB 'OH-WOD-S-[0-9][0-9][0-9][0-9]'"
    )
    max_wod_s_held = cur.fetchone()[0] or 0
    start_wod = max(max_wod_sites, max_wod_s_held)

    for i, old_id in enumerate(wod_seed_ids):
        new_id = f"OH-WOD-S-{start_wod + 1 + i:04d}"
        mapping_wod.append((old_id, new_id))

    return mapping_har, mapping_wod


def build_phase7_three_to_four_digit(cur):
    """
    Convert all remaining 3-digit single-county IDs to 4-digit.
    Excludes MC entities (already handled or already 4-digit).
    Excludes records already fixed in phases 1-6.
    """
    table_configs = [
        ("sites",         "site_id",         "S"),
        ("trails",        "trail_id",         "T"),
        ("trail_segments","segment_id",       "TS"),
        ("trail_networks","network_id",       "TN"),
        ("site_networks", "network_id",       "SN"),
        ("access_points", "access_point_id",  "AP"),
        ("trailthings",   "trailthing_id",    "TT"),
    ]
    entity_type_keys = {
        "sites":          "site",
        "trails":         "trail",
        "trail_segments": "trail_segment",
        "trail_networks": "trail_network",
        "site_networks":  "site_network",
        "access_points":  "access_point",
        "trailthings":    "trailthing",
    }

    batches = {}  # entity_type_key → [(old, new), ...]
    for table, pk, typ in table_configs:
        etk = entity_type_keys[table]
        # Only non-MC 3-digit records with correct type code
        cur.execute(
            f"SELECT {pk} FROM {table} "
            f"WHERE {pk} GLOB 'OH-???-{typ}-[0-9][0-9][0-9]' "
            f"AND {pk} NOT GLOB 'OH-MC-*' "
            f"ORDER BY {pk}"
        )
        rows = [r[0] for r in cur.fetchall()]
        if not rows:
            continue
        mapping = []
        for old_id in rows:
            seq = int(old_id.split("-")[-1])
            parts = old_id.rsplit("-", 1)
            new_id = f"{parts[0]}-{seq:04d}"
            mapping.append((old_id, new_id))
        batches[etk] = batches.get(etk, []) + mapping

    # Also held_entities with 3-digit proper IDs (e.g. OH-HAR-S-002 → OH-HAR-S-0002)
    # These were not covered by phases 1-6
    cur.execute(
        "SELECT record_id FROM held_entities "
        "WHERE record_id GLOB 'OH-???-*-[0-9][0-9][0-9]' "
        "AND record_id NOT GLOB 'OH-MC-*' "
        "ORDER BY record_id"
    )
    held_3digit = [r[0] for r in cur.fetchall()]
    if held_3digit:
        # These are held_only (no primary table row, just held_entities)
        mapping = []
        for old_id in held_3digit:
            seq = int(old_id.split("-")[-1])
            parts = old_id.rsplit("-", 1)
            new_id = f"{parts[0]}-{seq:04d}"
            mapping.append((old_id, new_id))
        batches["held_only"] = batches.get("held_only", []) + mapping

    return batches


# ---------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Natural Areas DB ID remediation")
    parser.add_argument("--db", default=DEFAULT_DB, help="Path to SQLite database")
    parser.add_argument("--dry-run", action="store_true", help="Print SQL without executing")
    args = parser.parse_args()

    print(f"Database: {args.db}")
    print(f"Dry run:  {args.dry_run}")
    print()

    conn = sqlite3.connect(args.db)
    conn.execute("PRAGMA foreign_keys = OFF")  # We manage FKs manually
    cur = conn.cursor()

    try:
        if not args.dry_run:
            conn.execute("BEGIN")

        # ---- Phase 1: MC-T collision ----
        p1 = build_phase1_mc_t_collision(cur)
        rename_batch(cur, "trail", p1, "Phase 1: MC-T 3-digit → 4-digit (0200+)", args.dry_run)

        # ---- Phase 2: MC-TR → MC-T ----
        p2 = build_phase2_mc_tr(cur)
        rename_batch(cur, "trail", p2, "Phase 2: MC-TR → MC-T (0216+)", args.dry_run)

        # ---- Phase 3: MC-SI → MC-S ----
        p3 = build_phase3_mc_si(cur)
        rename_batch(cur, "site", p3, "Phase 3: MC-SI → MC-S (0030+)", args.dry_run)

        # ---- Phase 4: OTT-AP-006 wrong table ----
        phase4_ott_ap_wrong_table(cur, args.dry_run)

        # ---- Phase 5: Single-county wrong type codes ----
        p5_sites, p5_trails, p5_aps = build_phase5_wrong_type_codes(cur)
        if p5_sites:
            rename_batch(cur, "site",  p5_sites,  "Phase 5a: WOD-SI/FUL-SI → WOD-S/FUL-S (4-digit)", args.dry_run)
        if p5_trails:
            rename_batch(cur, "trail", p5_trails, "Phase 5b: WIL/WOD/FUL -TR → -T (4-digit)", args.dry_run)
        if p5_aps:
            rename_batch(cur, "access_point", p5_aps, "Phase 5c: PUT-A → PUT-AP (4-digit)", args.dry_run)

        # ---- Phase 6: SEED- IDs ----
        p6_har, p6_wod = build_phase6_seed_ids(cur)
        if p6_har:
            rename_batch(cur, "held_only", p6_har, "Phase 6a: SEED- → OH-HAR-S-0xxx", args.dry_run)
        if p6_wod:
            rename_batch(cur, "held_only", p6_wod, "Phase 6b: WOD-SEED → OH-WOD-S-0xxx", args.dry_run)

        # ---- Phase 7: All remaining 3-digit → 4-digit ----
        p7_batches = build_phase7_three_to_four_digit(cur)
        for etk, mapping in sorted(p7_batches.items()):
            rename_batch(cur, etk, mapping, f"Phase 7: {etk} 3-digit → 4-digit", args.dry_run)

        # ---- Verification counts ----
        print("\n--- Post-remediation verification ---")
        checks = [
            ("3-digit MC-T remaining",
             "SELECT COUNT(*) FROM trails WHERE trail_id GLOB 'OH-MC-T-[0-9][0-9][0-9]'"),
            ("MC-TR remaining",
             "SELECT COUNT(*) FROM trails WHERE trail_id LIKE 'OH-MC-TR-%'"),
            ("MC-SI remaining",
             "SELECT COUNT(*) FROM sites WHERE site_id LIKE 'OH-MC-SI-%'"),
            ("OTT-AP-006 in sites",
             "SELECT COUNT(*) FROM sites WHERE site_id='OH-OTT-AP-006'"),
            ("OTT-AP-006 in access_points",
             "SELECT COUNT(*) FROM access_points WHERE access_point_id='OH-OTT-AP-006'"),
            ("WOD-SI remaining",
             "SELECT COUNT(*) FROM sites WHERE site_id LIKE 'OH-WOD-SI-%'"),
            ("FUL-SI remaining",
             "SELECT COUNT(*) FROM sites WHERE site_id LIKE 'OH-FUL-SI-%'"),
            ("PUT-A remaining",
             "SELECT COUNT(*) FROM access_points WHERE access_point_id LIKE 'OH-PUT-A-%'"),
            ("SEED- in held_entities",
             "SELECT COUNT(*) FROM held_entities WHERE record_id NOT LIKE 'OH-%'"),
            ("WOD-SEED in held_entities",
             "SELECT COUNT(*) FROM held_entities WHERE record_id LIKE 'OH-WOD-SEED-%'"),
            ("Any 3-digit single-county sites",
             "SELECT COUNT(*) FROM sites WHERE site_id GLOB 'OH-???-S-[0-9][0-9][0-9]' AND site_id NOT GLOB 'OH-MC-*'"),
            ("Any 3-digit single-county trails",
             "SELECT COUNT(*) FROM trails WHERE trail_id GLOB 'OH-???-T-[0-9][0-9][0-9]' AND trail_id NOT GLOB 'OH-MC-*'"),
            ("Any 3-digit single-county APs",
             "SELECT COUNT(*) FROM access_points WHERE access_point_id GLOB 'OH-???-AP-[0-9][0-9][0-9]' AND access_point_id NOT GLOB 'OH-MC-*'"),
            ("Total sites",    "SELECT COUNT(*) FROM sites"),
            ("Total trails",   "SELECT COUNT(*) FROM trails"),
            ("Total APs",      "SELECT COUNT(*) FROM access_points"),
            ("Total held",     "SELECT COUNT(*) FROM held_entities"),
        ]
        all_pass = True
        for label, sql in checks:
            cur.execute(sql)
            val = cur.fetchone()[0]
            # Expected 0 for all "remaining" checks, non-zero for counts
            is_remaining = "remaining" in label.lower() or "3-digit" in label.lower() or "seed" in label.lower()
            status = ""
            if is_remaining and "OTT-AP-006 in access_points" not in label:
                if label == "OTT-AP-006 in access_points":
                    status = "✓" if val == 1 else "✗ EXPECTED 1"
                    if val != 1:
                        all_pass = False
                elif val == 0:
                    status = "✓"
                else:
                    status = f"✗ EXPECTED 0 (got {val})"
                    all_pass = False
            elif label == "OTT-AP-006 in access_points":
                status = "✓" if val == 1 else "✗ EXPECTED 1"
                if val != 1:
                    all_pass = False
            print(f"  {label}: {val}  {status}")

        if all_pass:
            print("\n✓ All checks passed.")
        else:
            print("\n✗ Some checks failed — review above.")

        if args.dry_run:
            conn.rollback()
            print("\nDry run — rolled back.")
        else:
            conn.commit()
            print("\nCommitted.")

    except Exception as e:
        conn.rollback()
        print(f"\nERROR: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
    finally:
        conn.close()


if __name__ == "__main__":
    main()
