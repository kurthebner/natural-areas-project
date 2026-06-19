#!/usr/bin/env python3
"""
na_create_v6_tables.py — Natural Areas Project v6 Table Creation Script
v1.0  |  2026-05-31

Creates all v6 tables in natural_areas_v5.db that do not yet exist.
Safe to run multiple times — uses CREATE TABLE IF NOT EXISTS throughout.
Does not modify or drop any existing v5 tables.

USAGE:
    python utilities/na_create_v6_tables.py
    python utilities/na_create_v6_tables.py --db path/to/natural_areas_v5.db
    python utilities/na_create_v6_tables.py --dry-run  (print DDL only)
"""

import argparse
import os
import sqlite3
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
V6_ROOT    = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
DEFAULT_DB = os.path.join(V6_ROOT, "NASqlite", "natural_areas_v6.db")

# ── DDL statements ────────────────────────────────────────────────────────────

DDL_STATEMENTS = [

    # ── Primary entity tables (v6 new) ────────────────────────────────────────

    """CREATE TABLE IF NOT EXISTS trailthings (
        trailthing_id             TEXT PRIMARY KEY,
        name                      TEXT NOT NULL,
        alternate_names           TEXT DEFAULT '',
        source_term               TEXT DEFAULT '',
        source_hierarchy_context  TEXT DEFAULT '',
        parent_id                 TEXT DEFAULT '',
        site_parent_id            TEXT DEFAULT '',
        parent_site_network_id    TEXT DEFAULT '',
        use_type                  TEXT DEFAULT '',
        surface_type              TEXT DEFAULT '',
        origin_type               TEXT DEFAULT '',
        org_type                  TEXT DEFAULT '',
        status                    TEXT DEFAULT '',
        difficulty                TEXT DEFAULT '',
        accessibility             TEXT DEFAULT '',
        ownership                 TEXT DEFAULT '',
        governance                TEXT DEFAULT '',
        partner_agencies          TEXT DEFAULT '',
        coordination              TEXT DEFAULT '',
        counties                  TEXT DEFAULT '',
        states_included           TEXT DEFAULT '',
        total_length              REAL,
        description               TEXT DEFAULT '',
        trail_history             TEXT DEFAULT '',
        identity_notes            TEXT DEFAULT '',
        notes                     TEXT DEFAULT '',
        url                       TEXT DEFAULT '',
        maps                      TEXT DEFAULT '',
        created_at                TEXT NOT NULL,
        updated_at                TEXT NOT NULL,
        FOREIGN KEY (parent_id)              REFERENCES trailthings(trailthing_id),
        FOREIGN KEY (site_parent_id)         REFERENCES sites(site_id),
        FOREIGN KEY (parent_site_network_id) REFERENCES site_networks(network_id)
    )""",

    # Add new v6 columns to sites table if they don't exist
    # (sites table already exists from v5; ALTER TABLE adds missing columns safely)
    "ALTER TABLE sites ADD COLUMN habitat_type       TEXT DEFAULT ''",
    "ALTER TABLE sites ADD COLUMN access_notes        TEXT DEFAULT ''",
    "ALTER TABLE sites ADD COLUMN last_verified_date  TEXT DEFAULT ''",
    "ALTER TABLE sites ADD COLUMN field_verified      INTEGER DEFAULT 0",
    "ALTER TABLE sites ADD COLUMN ebird_hotspot_id    TEXT DEFAULT ''",

    # Add new v6 columns to access_points table if they don't exist
    "ALTER TABLE access_points ADD COLUMN last_verified_date  TEXT DEFAULT ''",
    "ALTER TABLE access_points ADD COLUMN field_verified      INTEGER DEFAULT 0",

    # ── Relationship tables (v6 new) ───────────────────────────────────────────

    """CREATE TABLE IF NOT EXISTS trailthing_hierarchy (
        parent_id  TEXT NOT NULL,
        child_id   TEXT NOT NULL,
        PRIMARY KEY (parent_id, child_id),
        FOREIGN KEY (parent_id) REFERENCES trailthings(trailthing_id),
        FOREIGN KEY (child_id)  REFERENCES trailthings(trailthing_id)
    )""",

    # ── Operational tables (ensure all exist) ──────────────────────────────────

    """CREATE TABLE IF NOT EXISTS held_entities (
        record_id    TEXT NOT NULL,
        entity_type  TEXT NOT NULL,
        name         TEXT DEFAULT '',
        hold_reason  TEXT NOT NULL,
        hold_detail  TEXT DEFAULT '',
        county       TEXT NOT NULL,
        run_id       TEXT,
        created_at   TEXT NOT NULL,
        PRIMARY KEY (record_id, county)
    )""",

    """CREATE TABLE IF NOT EXISTS manual_review_queue (
        review_id          INTEGER PRIMARY KEY AUTOINCREMENT,
        entity_type        TEXT NOT NULL,
        collision_type     TEXT NOT NULL,
        entity_record_a    TEXT,
        entity_record_b    TEXT,
        field_diff         TEXT,
        run_id             TEXT,
        queued_at          TEXT NOT NULL,
        resolution_status  TEXT DEFAULT 'pending',
        resolved_by        TEXT DEFAULT '',
        resolved_at        TEXT DEFAULT '',
        resolution_notes   TEXT DEFAULT ''
    )""",

    """CREATE TABLE IF NOT EXISTS entity_conflicts (
        conflict_id        INTEGER PRIMARY KEY AUTOINCREMENT,
        entity_id          TEXT NOT NULL,
        entity_type        TEXT NOT NULL,
        field_name         TEXT NOT NULL,
        value_a            TEXT,
        value_b            TEXT,
        resolution_status  TEXT DEFAULT 'pending',
        resolution_notes   TEXT DEFAULT '',
        run_id             TEXT,
        created_at         TEXT NOT NULL
    )""",

    """CREATE TABLE IF NOT EXISTS entity_uncertainty (
        uncertainty_id  INTEGER PRIMARY KEY AUTOINCREMENT,
        entity_id       TEXT NOT NULL,
        entity_type     TEXT NOT NULL,
        field_name      TEXT NOT NULL,
        uncertainty     TEXT NOT NULL,
        run_id          TEXT,
        created_at      TEXT NOT NULL
    )""",

    """CREATE TABLE IF NOT EXISTS entity_geometry (
        geometry_id   INTEGER PRIMARY KEY AUTOINCREMENT,
        entity_id     TEXT NOT NULL,
        entity_type   TEXT NOT NULL,
        geometry_type TEXT NOT NULL,
        geometry_wkt  TEXT,
        source        TEXT DEFAULT '',
        created_at    TEXT NOT NULL,
        updated_at    TEXT NOT NULL
    )""",

    # ── Provenance tables (ensure all exist) ───────────────────────────────────

    """CREATE TABLE IF NOT EXISTS run_metadata (
        run_id         TEXT PRIMARY KEY,
        county         TEXT NOT NULL,
        state          TEXT NOT NULL,
        run_date       TEXT NOT NULL,
        records_input  INTEGER DEFAULT 0,
        normalized     INTEGER DEFAULT 0,
        held           INTEGER DEFAULT 0,
        notes          TEXT DEFAULT '',
        created_at     TEXT NOT NULL
    )""",

    """CREATE TABLE IF NOT EXISTS discovery_provenance (
        prov_id         INTEGER PRIMARY KEY AUTOINCREMENT,
        entity_id       TEXT NOT NULL,
        entity_type     TEXT NOT NULL,
        county          TEXT NOT NULL,
        source_url      TEXT DEFAULT '',
        discovery_tier  INTEGER,
        extraction_method TEXT DEFAULT '',
        run_id          TEXT,
        created_at      TEXT NOT NULL
    )""",

    """CREATE TABLE IF NOT EXISTS resolution_provenance (
        prov_id          INTEGER PRIMARY KEY AUTOINCREMENT,
        entity_id        TEXT NOT NULL,
        entity_type      TEXT NOT NULL,
        county           TEXT NOT NULL,
        resolution_run   TEXT DEFAULT '',
        notes            TEXT DEFAULT '',
        run_id           TEXT,
        created_at       TEXT NOT NULL
    )""",

    """CREATE TABLE IF NOT EXISTS normalization_provenance (
        prov_id         INTEGER PRIMARY KEY AUTOINCREMENT,
        entity_id       TEXT NOT NULL,
        entity_type     TEXT NOT NULL,
        county          TEXT NOT NULL,
        field_name      TEXT NOT NULL,
        raw_value       TEXT DEFAULT '',
        normalized_value TEXT DEFAULT '',
        decision        TEXT DEFAULT '',
        run_id          TEXT,
        created_at      TEXT NOT NULL
    )""",

    # ── Indexes for common queries ─────────────────────────────────────────────

    "CREATE INDEX IF NOT EXISTS idx_trailthings_counties ON trailthings(counties)",
    "CREATE INDEX IF NOT EXISTS idx_trailthings_parent_id ON trailthings(parent_id)",
    "CREATE INDEX IF NOT EXISTS idx_trailthings_site_parent ON trailthings(site_parent_id)",
    "CREATE INDEX IF NOT EXISTS idx_held_entities_county ON held_entities(county)",
    "CREATE INDEX IF NOT EXISTS idx_held_entities_reason ON held_entities(hold_reason)",
]


def run_ddl(db_path: str, dry_run: bool) -> None:
    if dry_run:
        print(f"DRY RUN — DDL that would be executed against: {db_path}\n")
        for stmt in DDL_STATEMENTS:
            print(stmt.strip())
            print()
        return

    if not os.path.exists(db_path):
        print(f"WARNING: DB not found at {db_path} — will be created.", file=sys.stderr)

    conn = sqlite3.connect(db_path)
    conn.execute("PRAGMA foreign_keys = ON")
    success = 0
    skipped = 0
    errors  = []

    for stmt in DDL_STATEMENTS:
        label = stmt.strip().split('\n')[0][:80]
        try:
            conn.execute(stmt)
            conn.commit()
            print(f"  OK: {label}")
            success += 1
        except sqlite3.OperationalError as e:
            msg = str(e)
            # ALTER TABLE "duplicate column" is expected on re-runs — treat as skip
            if "duplicate column" in msg.lower():
                print(f"  SKIP (column exists): {label}")
                skipped += 1
            else:
                print(f"  ERROR: {label}\n    {msg}", file=sys.stderr)
                errors.append((label, msg))

    conn.close()

    print(f"\nSummary: {success} executed, {skipped} skipped, {len(errors)} errors")
    if errors:
        print("\nErrors requiring attention:")
        for label, msg in errors:
            print(f"  {label}: {msg}")
        sys.exit(1)
    else:
        print(f"v6 tables created successfully in: {db_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Create v6 tables in natural_areas_v5.db"
    )
    parser.add_argument("--db",      default=DEFAULT_DB,
                        help=f"Database path (default: {DEFAULT_DB})")
    parser.add_argument("--dry-run", action="store_true",
                        help="Print DDL without executing")
    args = parser.parse_args()

    run_ddl(os.path.abspath(args.db), args.dry_run)


if __name__ == "__main__":
    main()
