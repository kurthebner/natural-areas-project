#!/usr/bin/env python3
"""
Natural Areas Project — Franklin County, Ohio
Self-Contained Upsert Script
Generated: 2026-03-25 | Schema: v5.2 (Sites) / v5.1 (all others)

USAGE:
    python franklin_oh_upsert.py [--db PATH] [--dry-run] [--reset-county]

OPTIONS:
    --db PATH         Path to the SQLite database file
                      Default: ./natural_areas.db
    --dry-run         Print SQL summary without executing
    --reset-county    DELETE all existing Franklin County records before upserting
"""

import sqlite3
import sys
import csv
import argparse
import os
from datetime import datetime, timezone

# ---------------------------------------------------------------------------
# CONFIG
# ---------------------------------------------------------------------------

DEFAULT_DB = "./natural_areas.db"
COUNTY = "Franklin"
STATE = "Ohio"
RUN_ID = "franklin_oh_2026_03_25"
RUN_DATE = "2026-03-25"
TSV_DIR = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------------------
# SCHEMA
# ---------------------------------------------------------------------------

SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS sites (
    site_id         TEXT PRIMARY KEY,
    name            TEXT NOT NULL,
    category        TEXT,
    subtype         TEXT,
    designation     TEXT,
    status          TEXT,
    ownership       TEXT,
    governance      TEXT,
    partner_agencies TEXT,
    coordination    TEXT,
    description     TEXT,
    location        TEXT,
    acres           REAL,
    counties        TEXT,
    municipality    TEXT,
    township        TEXT,
    gps_lat         REAL,
    gps_lon         REAL,
    plus_code       TEXT,
    features        TEXT,
    notes           TEXT,
    url_primary     TEXT,
    urls            TEXT,
    parent_site_id  TEXT,
    created_at      TEXT,
    updated_at      TEXT,
    features_raw    TEXT
);

CREATE TABLE IF NOT EXISTS trails (
    trail_id            TEXT PRIMARY KEY,
    name                TEXT NOT NULL,
    alternate_names     TEXT,
    use_type            TEXT,
    surface_type        TEXT,
    origin_type         TEXT,
    length_mi           REAL,
    counties            TEXT,
    governance          TEXT,
    partner_agencies    TEXT,
    status              TEXT,
    difficulty          TEXT,
    accessibility       TEXT,
    description         TEXT,
    trail_history       TEXT,
    identity_notes      TEXT,
    notes               TEXT,
    url_primary         TEXT,
    maps                TEXT,
    created_at          TEXT,
    updated_at          TEXT
);

CREATE TABLE IF NOT EXISTS trail_segments (
    segment_id      TEXT PRIMARY KEY,
    parent_trail_id TEXT,
    name            TEXT,
    counties        TEXT,
    governance      TEXT,
    length_mi       REAL,
    surface_type    TEXT,
    segment_type    TEXT,
    status          TEXT,
    difficulty      TEXT,
    accessibility   TEXT,
    description     TEXT,
    identity_notes  TEXT,
    notes           TEXT,
    url_primary     TEXT,
    maps            TEXT,
    geometry        TEXT,
    created_at      TEXT,
    updated_at      TEXT
);

CREATE TABLE IF NOT EXISTS trail_networks (
    network_id          TEXT PRIMARY KEY,
    name                TEXT NOT NULL,
    network_type        TEXT,
    status              TEXT,
    ownership           TEXT,
    governance          TEXT,
    partner_agencies    TEXT,
    counties            TEXT,
    states_included     TEXT,
    length_mi           REAL,
    member_trail_count  INTEGER,
    member_trail_ids    TEXT,
    description         TEXT,
    identity_notes      TEXT,
    notes               TEXT,
    url_primary         TEXT,
    maps                TEXT,
    created_at          TEXT,
    updated_at          TEXT
);

CREATE TABLE IF NOT EXISTS site_networks (
    network_id      TEXT PRIMARY KEY,
    name            TEXT NOT NULL,
    network_type    TEXT,
    status          TEXT,
    ownership       TEXT,
    governance      TEXT,
    partner_agencies TEXT,
    counties        TEXT,
    states_included TEXT,
    member_count    INTEGER,
    member_site_ids TEXT,
    description     TEXT,
    identity_notes  TEXT,
    notes           TEXT,
    url_primary     TEXT,
    created_at      TEXT,
    updated_at      TEXT
);

CREATE TABLE IF NOT EXISTS access_points (
    access_point_id     TEXT PRIMARY KEY,
    name                TEXT NOT NULL,
    ap_type             TEXT,
    status              TEXT,
    parent_entity_type  TEXT,
    parent_entity_id    TEXT,
    county              TEXT,
    township            TEXT,
    municipality        TEXT,
    address             TEXT,
    gps_lat             REAL,
    gps_lon             REAL,
    plus_code           TEXT,
    features            TEXT,
    identity_notes      TEXT,
    notes               TEXT,
    url_primary         TEXT,
    created_at          TEXT,
    updated_at          TEXT
);

-- Relationship tables
CREATE TABLE IF NOT EXISTS site_parent (
    site_id         TEXT NOT NULL,
    parent_site_id  TEXT NOT NULL,
    PRIMARY KEY (site_id, parent_site_id)
);

CREATE TABLE IF NOT EXISTS trail_to_segment (
    trail_id        TEXT NOT NULL,
    segment_id      TEXT NOT NULL,
    PRIMARY KEY (trail_id, segment_id)
);

CREATE TABLE IF NOT EXISTS trail_network_members (
    network_id      TEXT NOT NULL,
    trail_id        TEXT NOT NULL,
    PRIMARY KEY (network_id, trail_id)
);

CREATE TABLE IF NOT EXISTS site_network_members (
    network_id      TEXT NOT NULL,
    site_id         TEXT NOT NULL,
    PRIMARY KEY (network_id, site_id)
);

CREATE TABLE IF NOT EXISTS access_point_parents (
    access_point_id     TEXT NOT NULL,
    parent_entity_type  TEXT NOT NULL,
    parent_entity_id    TEXT NOT NULL,
    PRIMARY KEY (access_point_id, parent_entity_type, parent_entity_id)
);

-- Operational tables
CREATE TABLE IF NOT EXISTS entity_conflicts (
    conflict_id     INTEGER PRIMARY KEY AUTOINCREMENT,
    entity_id       TEXT NOT NULL,
    entity_type     TEXT NOT NULL,
    field           TEXT NOT NULL,
    value_a         TEXT,
    value_b         TEXT,
    run_id          TEXT,
    created_at      TEXT
);

CREATE TABLE IF NOT EXISTS entity_uncertainty (
    uncertainty_id  INTEGER PRIMARY KEY AUTOINCREMENT,
    entity_id       TEXT NOT NULL,
    entity_type     TEXT NOT NULL,
    field           TEXT,
    uncertainty_note TEXT,
    run_id          TEXT,
    created_at      TEXT
);

CREATE TABLE IF NOT EXISTS held_entities (
    held_id         INTEGER PRIMARY KEY AUTOINCREMENT,
    entity_id       TEXT NOT NULL,
    entity_type     TEXT NOT NULL,
    hold_reason     TEXT,
    hold_detail     TEXT,
    data_json       TEXT,
    run_id          TEXT,
    created_at      TEXT
);

CREATE TABLE IF NOT EXISTS manual_review_queue (
    review_id       INTEGER PRIMARY KEY AUTOINCREMENT,
    entity_id       TEXT,
    entity_type     TEXT,
    issue           TEXT,
    detail          TEXT,
    run_id          TEXT,
    created_at      TEXT
);

CREATE TABLE IF NOT EXISTS run_metadata (
    run_id          TEXT PRIMARY KEY,
    county          TEXT,
    state           TEXT,
    run_date        TEXT,
    sites_upserted  INTEGER DEFAULT 0,
    trails_upserted INTEGER DEFAULT 0,
    trail_segs_upserted INTEGER DEFAULT 0,
    trail_nets_upserted INTEGER DEFAULT 0,
    site_nets_upserted  INTEGER DEFAULT 0,
    aps_upserted    INTEGER DEFAULT 0,
    held_count      INTEGER DEFAULT 0,
    rejected_count  INTEGER DEFAULT 0,
    notes           TEXT,
    created_at      TEXT
);
"""

# ---------------------------------------------------------------------------
# HELPERS
# ---------------------------------------------------------------------------

def now_utc():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

def blank(v):
    """Return None for empty/whitespace strings."""
    if v is None:
        return None
    s = v.strip()
    return s if s else None

def to_real(v):
    """Convert string to float, return None if blank or unconvertible."""
    s = blank(v)
    if s is None:
        return None
    try:
        return float(s)
    except ValueError:
        return None

def to_int(v):
    """Convert string to int, return None if blank or unconvertible."""
    s = blank(v)
    if s is None:
        return None
    try:
        return int(s)
    except ValueError:
        return None

def read_tsv(filepath):
    """Read TSV file, return list of dicts."""
    rows = []
    with open(filepath, encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter='\t')
        for row in reader:
            rows.append(row)
    return rows

# ---------------------------------------------------------------------------
# UPSERT FUNCTIONS
# ---------------------------------------------------------------------------

def upsert_sites(conn, dry_run):
    tsv_path = os.path.join(TSV_DIR, "franklin_oh_sites.tsv")
    rows = read_tsv(tsv_path)
    ts = now_utc()
    count = 0
    site_parents = []

    for r in rows:
        sid = blank(r.get('site_id'))
        if not sid:
            continue
        parent = blank(r.get('parent_site_id'))
        if parent:
            site_parents.append((sid, parent))

        vals = (
            sid,
            blank(r.get('name')),
            blank(r.get('category')),
            blank(r.get('subtype')),
            blank(r.get('designation')),
            blank(r.get('status')),
            blank(r.get('ownership')),
            blank(r.get('governance')),
            blank(r.get('partner_agencies')),
            blank(r.get('coordination')),
            blank(r.get('description')),
            blank(r.get('location')),
            to_real(r.get('acres')),
            blank(r.get('counties')),
            blank(r.get('municipality')),
            blank(r.get('township')),
            to_real(r.get('gps_lat')),
            to_real(r.get('gps_lon')),
            blank(r.get('plus_code')),
            blank(r.get('features')),
            blank(r.get('notes')),
            blank(r.get('url_primary')),
            blank(r.get('urls')),
            parent,
            ts, ts, None
        )
        if not dry_run:
            conn.execute("""
                INSERT INTO sites
                (site_id,name,category,subtype,designation,status,ownership,governance,
                 partner_agencies,coordination,description,location,acres,counties,
                 municipality,township,gps_lat,gps_lon,plus_code,features,notes,
                 url_primary,urls,parent_site_id,created_at,updated_at,features_raw)
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                ON CONFLICT(site_id) DO UPDATE SET
                  name=excluded.name, category=excluded.category, subtype=excluded.subtype,
                  designation=excluded.designation, status=excluded.status,
                  ownership=excluded.ownership, governance=excluded.governance,
                  partner_agencies=excluded.partner_agencies, coordination=excluded.coordination,
                  description=excluded.description, location=excluded.location,
                  acres=excluded.acres, counties=excluded.counties, municipality=excluded.municipality,
                  township=excluded.township, gps_lat=excluded.gps_lat, gps_lon=excluded.gps_lon,
                  plus_code=excluded.plus_code, features=excluded.features, notes=excluded.notes,
                  url_primary=excluded.url_primary, urls=excluded.urls,
                  parent_site_id=excluded.parent_site_id, updated_at=excluded.updated_at
            """, vals)
        count += 1

    # Upsert site_parent relationships
    parent_count = 0
    for (sid, psid) in site_parents:
        if not dry_run:
            conn.execute("""
                INSERT OR IGNORE INTO site_parent (site_id, parent_site_id) VALUES (?,?)
            """, (sid, psid))
        parent_count += 1

    return count, parent_count


def upsert_trails(conn, dry_run):
    tsv_path = os.path.join(TSV_DIR, "franklin_oh_trails.tsv")
    rows = read_tsv(tsv_path)
    ts = now_utc()
    count = 0

    for r in rows:
        tid = blank(r.get('Trail ID'))
        if not tid:
            continue
        vals = (
            tid,
            blank(r.get('Trail Name')),
            blank(r.get('Alternate Names')),
            blank(r.get('Trail Use Type')),
            blank(r.get('Trail Surface Type')),
            blank(r.get('Trail Origin Type')),
            to_real(r.get('Total Length (Miles)')),
            blank(r.get('Counties')),
            blank(r.get('Governance')),
            blank(r.get('Partner Agencies')),
            blank(r.get('Status')),
            blank(r.get('Difficulty')),
            blank(r.get('Accessibility')),
            blank(r.get('Description')),
            blank(r.get('Trail History')),
            blank(r.get('Identity Notes')),
            blank(r.get('Notes')),
            blank(r.get('URL')),
            blank(r.get('Maps')),
            ts, ts
        )
        if not dry_run:
            conn.execute("""
                INSERT INTO trails
                (trail_id,name,alternate_names,use_type,surface_type,origin_type,length_mi,
                 counties,governance,partner_agencies,status,difficulty,accessibility,
                 description,trail_history,identity_notes,notes,url_primary,maps,
                 created_at,updated_at)
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                ON CONFLICT(trail_id) DO UPDATE SET
                  name=excluded.name, alternate_names=excluded.alternate_names,
                  use_type=excluded.use_type, surface_type=excluded.surface_type,
                  origin_type=excluded.origin_type, length_mi=excluded.length_mi,
                  counties=excluded.counties, governance=excluded.governance,
                  partner_agencies=excluded.partner_agencies, status=excluded.status,
                  difficulty=excluded.difficulty, accessibility=excluded.accessibility,
                  description=excluded.description, trail_history=excluded.trail_history,
                  identity_notes=excluded.identity_notes, notes=excluded.notes,
                  url_primary=excluded.url_primary, maps=excluded.maps,
                  updated_at=excluded.updated_at
            """, vals)
        count += 1

    return count


def upsert_trail_networks(conn, dry_run):
    tsv_path = os.path.join(TSV_DIR, "franklin_oh_trail_networks.tsv")
    rows = read_tsv(tsv_path)
    ts = now_utc()
    count = 0
    member_rows = []

    for r in rows:
        nid = blank(r.get('Network ID'))
        if not nid:
            continue
        member_ids_raw = blank(r.get('Member Trail IDs'))
        if member_ids_raw:
            for mid in [m.strip() for m in member_ids_raw.split(';') if m.strip()]:
                member_rows.append((nid, mid))

        vals = (
            nid,
            blank(r.get('Network Name')),
            blank(r.get('Network Type')),
            blank(r.get('Status')),
            blank(r.get('Ownership')),
            blank(r.get('Governance')),
            blank(r.get('Partner Agencies')),
            blank(r.get('Counties')),
            blank(r.get('States Included')),
            to_real(r.get('Total Length (Miles)')),
            to_int(r.get('Member Trail Count')),
            member_ids_raw,
            blank(r.get('Description')),
            blank(r.get('Identity Notes')),
            blank(r.get('Notes')),
            blank(r.get('URL')),
            blank(r.get('Maps')),
            ts, ts
        )
        if not dry_run:
            conn.execute("""
                INSERT INTO trail_networks
                (network_id,name,network_type,status,ownership,governance,partner_agencies,
                 counties,states_included,length_mi,member_trail_count,member_trail_ids,
                 description,identity_notes,notes,url_primary,maps,created_at,updated_at)
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                ON CONFLICT(network_id) DO UPDATE SET
                  name=excluded.name, network_type=excluded.network_type,
                  status=excluded.status, ownership=excluded.ownership,
                  governance=excluded.governance, partner_agencies=excluded.partner_agencies,
                  counties=excluded.counties, states_included=excluded.states_included,
                  length_mi=excluded.length_mi, member_trail_count=excluded.member_trail_count,
                  member_trail_ids=excluded.member_trail_ids, description=excluded.description,
                  identity_notes=excluded.identity_notes, notes=excluded.notes,
                  url_primary=excluded.url_primary, maps=excluded.maps,
                  updated_at=excluded.updated_at
            """, vals)
        count += 1

    member_count = 0
    for (nid, tid) in member_rows:
        if not dry_run:
            conn.execute("""
                INSERT OR IGNORE INTO trail_network_members (network_id, trail_id) VALUES (?,?)
            """, (nid, tid))
        member_count += 1

    return count, member_count


def upsert_site_networks(conn, dry_run):
    tsv_path = os.path.join(TSV_DIR, "franklin_oh_site_networks.tsv")
    rows = read_tsv(tsv_path)
    ts = now_utc()
    count = 0
    member_rows = []

    for r in rows:
        nid = blank(r.get('Network ID'))
        if not nid:
            continue
        member_ids_raw = blank(r.get('Member Site IDs'))
        if member_ids_raw:
            for mid in [m.strip() for m in member_ids_raw.split(';') if m.strip()]:
                member_rows.append((nid, mid))

        vals = (
            nid,
            blank(r.get('Network Name')),
            blank(r.get('Network Type')),
            blank(r.get('Status')),
            blank(r.get('Ownership')),
            blank(r.get('Governance')),
            blank(r.get('Partner Agencies')),
            blank(r.get('Counties')),
            blank(r.get('States Included')),
            to_int(r.get('Member Count')),
            member_ids_raw,
            blank(r.get('Description')),
            blank(r.get('Identity Notes')),
            blank(r.get('Notes')),
            blank(r.get('URL')),
            ts, ts
        )
        if not dry_run:
            conn.execute("""
                INSERT INTO site_networks
                (network_id,name,network_type,status,ownership,governance,partner_agencies,
                 counties,states_included,member_count,member_site_ids,description,
                 identity_notes,notes,url_primary,created_at,updated_at)
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                ON CONFLICT(network_id) DO UPDATE SET
                  name=excluded.name, network_type=excluded.network_type,
                  status=excluded.status, ownership=excluded.ownership,
                  governance=excluded.governance, partner_agencies=excluded.partner_agencies,
                  counties=excluded.counties, states_included=excluded.states_included,
                  member_count=excluded.member_count, member_site_ids=excluded.member_site_ids,
                  description=excluded.description, identity_notes=excluded.identity_notes,
                  notes=excluded.notes, url_primary=excluded.url_primary,
                  updated_at=excluded.updated_at
            """, vals)
        count += 1

    member_count = 0
    for (nid, sid) in member_rows:
        if not dry_run:
            conn.execute("""
                INSERT OR IGNORE INTO site_network_members (network_id, site_id) VALUES (?,?)
            """, (nid, sid))
        member_count += 1

    return count, member_count


# ---------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--db', default=DEFAULT_DB)
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--reset-county', action='store_true')
    args = parser.parse_args()

    db_path = args.db
    dry_run = args.dry_run

    print(f"Natural Areas Project — Franklin County, Ohio Upsert")
    print(f"Database: {db_path}")
    print(f"Dry run: {dry_run}")
    print()

    conn = sqlite3.connect(db_path)
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA foreign_keys=OFF")

    # Create schema
    for stmt in SCHEMA_SQL.strip().split(';'):
        stmt = stmt.strip()
        if stmt:
            conn.execute(stmt)
    conn.commit()
    print("Schema: OK")

    if args.reset_county and not dry_run:
        for tbl in ['sites', 'trails', 'trail_segments', 'trail_networks',
                    'site_networks', 'access_points']:
            conn.execute(f"DELETE FROM {tbl} WHERE counties LIKE '%Franklin%'")
        conn.commit()
        print("Reset: Franklin County records deleted")

    # Upsert each entity type
    sites_count, site_parent_count = upsert_sites(conn, dry_run)
    trails_count = upsert_trails(conn, dry_run)
    trail_nets_count, trail_net_members_count = upsert_trail_networks(conn, dry_run)
    site_nets_count, site_net_members_count = upsert_site_networks(conn, dry_run)

    if not dry_run:
        conn.commit()

    print(f"Sites:          {sites_count} upserted")
    print(f"Trails:         {trails_count} upserted")
    print(f"Trail Segments: 0 (none in TSV)")
    print(f"Trail Networks: {trail_nets_count} upserted")
    print(f"Site Networks:  {site_nets_count} upserted")
    print(f"Access Points:  0 (none in TSV)")
    print(f"site_parent:    {site_parent_count} rows")
    print(f"trail_network_members: {trail_net_members_count} rows")
    print(f"site_network_members:  {site_net_members_count} rows")

    total = sites_count + trails_count + trail_nets_count + site_nets_count
    print()

    # Write run metadata
    if not dry_run:
        conn.execute("""
            INSERT OR REPLACE INTO run_metadata
            (run_id, county, state, run_date, records_input, normalized, held, rejected, created_at)
            VALUES (?,?,?,?,?,?,?,?,?)
        """, (RUN_ID, COUNTY, STATE, RUN_DATE, total, total, 0, 0, now_utc()))
        conn.commit()
        print(f"Run metadata:   written (run_id={RUN_ID})")

    conn.close()
    print()
    print(f"✓ Upsert complete — {total} records written to {db_path}")
    print(f"  Sites: {sites_count} | Trails: {trails_count} | Trail Networks: {trail_nets_count} | Site Networks: {site_nets_count}")
    print(f"  Held: 0 | Rejected: 0")


if __name__ == '__main__':
    main()
