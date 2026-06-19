#!/usr/bin/env python3
"""
na_pipeline_core.py — Natural Areas Project Pipeline Core Module
v1.1  |  2026-05-09

Shared pipeline logic for all county pipeline scripts.
Covers Stages 3–6: GPS Acquisition → TSV Output → Vocabulary Validation Gate
                   → Integrity Check → Database Upsert.

Stages 1 (Resolution) and 2 (Normalization) remain county-specific — the
normalized entity lists (SITES, TRAILS, etc.) are defined in the county
script and passed into PipelineRunner.

USAGE IN A COUNTY SCRIPT:
    import sys, os
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'utilities'))
    from na_pipeline_core import PipelineRunner, ALLOWED_FEATURES  # etc.

    SITES = [ { ... }, ... ]      # normalized entity dicts
    TRAILS = [ { ... }, ... ]
    ACCESS_POINTS = [ { ... }, ... ]
    TRAIL_SEGMENTS = []
    TRAIL_NETWORKS = []
    SITE_NETWORKS  = []

    GPS_QUERIES  = { "XXX-S-001": "123 Main St, Town, Ohio", ... }
    FALLBACK_GPS = { "XXX-S-001": (41.123, -83.456), ... }

    runner = PipelineRunner(
        run_id        = "county_oh_2026_xx_xx",
        county        = "County Name",
        state         = "Ohio",
        run_date      = "2026-xx-xx",
        records_input = 20,
        output_dir    = SCRIPT_DIR,
        db_path       = DEFAULT_DB,
        county_bbox   = (lat_min, lat_max, lon_min, lon_max),
    )
    runner.run(SITES, TRAILS, ACCESS_POINTS,
               TRAIL_SEGMENTS, TRAIL_NETWORKS, SITE_NETWORKS,
               GPS_QUERIES, FALLBACK_GPS, dry_run=False)

VOCABULARY SOURCES (read before normalization in every county):
    vocabularies/na_site_vocabulary_v5.5.md
    vocabularies/na_trail_vocabulary_v5.1.md
    vocabularies/na_access_point_vocabulary_v5.2.md
"""

import csv
import os
import sqlite3
import sys
import time
from datetime import datetime, timezone
from typing import Dict, List, Optional, Tuple

# IMP-128: Windows console UTF-8 fix — prevents UnicodeEncodeError on → and em dashes
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# ── Optional dependencies ────────────────────────────────────────────────────
try:
    from na_plus_code import encode_plus_code
except ImportError:
    encode_plus_code = None
    print("WARNING [na_pipeline_core]: na_plus_code not found. Plus codes will be blank.")

try:
    from na_township_lookup import OhioTownshipLookup
    _LOOKUP = OhioTownshipLookup()
    _LOOKUP_AVAILABLE = True
except Exception as e:
    _LOOKUP = None
    _LOOKUP_AVAILABLE = False
    print(f"WARNING [na_pipeline_core]: OhioTownshipLookup unavailable ({e}).")

try:
    import requests as _requests
    _REQUESTS_OK = True
except ImportError:
    _requests = None
    _REQUESTS_OK = False
    print("WARNING [na_pipeline_core]: 'requests' not available. Nominatim GPS disabled.")

# ── Nominatim config ─────────────────────────────────────────────────────────
NOMINATIM_URL     = "https://nominatim.openstreetmap.org/search"
NOMINATIM_DELAY   = 1.1   # seconds between requests (Nominatim policy)
NOMINATIM_HEADERS = {
    "User-Agent": "NaturalAreasProject/5.x (research use; admin contact available)",
    "Accept-Language": "en",
}

# ── US bounding box (plausibility check for all geocoded results) ─────────────
US_LAT_MIN, US_LAT_MAX = 24.0, 50.0
US_LON_MIN, US_LON_MAX = -130.0, -65.0


# ════════════════════════════════════════════════════════════════════════════
#  VOCABULARY CONSTANTS  — imported from na_vocab_constants (single source)
# ════════════════════════════════════════════════════════════════════════════
from na_vocab_constants import (
    ALLOWED_CATEGORIES,
    ALLOWED_SUBTYPES,
    ALLOWED_DESIGNATIONS,
    ALLOWED_SITE_STATUSES,
    ALLOWED_FEATURES,
    ALLOWED_TRAIL_USE_TYPES,
    ALLOWED_TRAIL_SURFACES,
    ALLOWED_TRAIL_ORIGINS,
    ALLOWED_TRAIL_STATUSES,
    ALLOWED_TRAIL_DIFFICULTIES,
    ALLOWED_AP_TYPES,
    ALLOWED_AP_STATUSES,
)

# TSV column definitions (one list per entity type)
SITE_TSV_COLUMNS = [
    "name", "category", "subtype", "designation", "status",
    "ownership", "governance", "partner_agencies", "coordination",
    "description", "location", "acres", "counties", "municipality", "township",
    "gps_lat", "gps_lon", "plus_code", "features", "notes",
    "url_primary", "urls", "parent_site_id", "created_at", "updated_at",
]
TRAIL_TSV_COLUMNS = [
    "name", "alternate_names", "use_type", "surface_type", "origin_type",
    "length_mi", "counties", "governance", "partner_agencies",
    "status", "difficulty", "accessibility",
    "description", "trail_history", "identity_notes", "notes",
    "url_primary", "maps", "created_at", "updated_at",
]
TRAIL_SEGMENT_TSV_COLUMNS = [
    "name", "counties", "governance", "length_mi", "surface_type",
    "segment_type", "status", "difficulty", "accessibility",
    "description", "identity_notes", "notes", "url_primary", "maps",
    "geometry", "created_at", "updated_at",
]
TRAIL_NETWORK_TSV_COLUMNS = [
    "name", "network_type", "status", "ownership", "governance",
    "partner_agencies", "counties", "states_included", "length_mi",
    "member_trail_count", "member_trail_ids",
    "description", "identity_notes", "notes", "url_primary", "maps",
    "created_at", "updated_at",
]
SITE_NETWORK_TSV_COLUMNS = [
    "name", "network_type", "status", "ownership", "governance",
    "partner_agencies", "counties", "states_included",
    "member_count", "member_site_ids",
    "description", "identity_notes", "notes", "url_primary",
    "created_at", "updated_at",
]
AP_TSV_COLUMNS = [
    "name", "ap_type", "status",
    "parent_entity_type", "parent_entity_id",
    "county", "township", "municipality", "address",
    "gps_lat", "gps_lon", "plus_code", "features",
    "identity_notes", "notes", "url_primary",
    "created_at", "updated_at",
]


# ════════════════════════════════════════════════════════════════════════════
#  GPS ACQUISITION  (Stage 3)
# ════════════════════════════════════════════════════════════════════════════

def nominatim_geocode(query: str) -> Tuple[Optional[float], Optional[float]]:
    """Query Nominatim; return (lat, lon) rounded to 6dp, or (None, None)."""
    if not _REQUESTS_OK:
        return None, None
    params = {"q": query, "format": "json", "limit": 1, "countrycodes": "us"}
    try:
        resp = _requests.get(NOMINATIM_URL, params=params,
                             headers=NOMINATIM_HEADERS, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        if data:
            lat = round(float(data[0]["lat"]), 6)
            lon = round(float(data[0]["lon"]), 6)
            if US_LAT_MIN <= lat <= US_LAT_MAX and US_LON_MIN <= lon <= US_LON_MAX:
                return lat, lon
    except Exception as e:
        print(f"  Nominatim error for '{query}': {e}")
    return None, None


def acquire_gps(entities: List[dict], id_field: str,
                queries: Dict[str, str],
                fallbacks: Dict[str, Tuple[float, float]],
                fallback_conf: Dict[str, str] = None) -> None:
    """
    Attempt GPS acquisition for each entity missing coordinates.
    Modifies entities in-place, setting gps_lat, gps_lon, gps_confidence.

    fallback_conf: optional dict mapping entity_id → confidence string for
                   that specific fallback (default "LOW"; use "MED" for
                   street-level geocodes pre-computed outside Nominatim).
    """
    if fallback_conf is None:
        fallback_conf = {}

    for ent in entities:
        eid = ent[id_field]
        if ent.get("gps_lat") is not None:
            continue

        query = queries.get(eid)
        if not query:
            # IMP-082: apply fallback directly when no Nominatim query is present
            if eid in fallbacks:
                lat, lon = fallbacks[eid]
                conf = fallback_conf.get(eid, "LOW") if fallback_conf else "LOW"
                print(f"  GPS [{eid}]: direct fallback (no query) {lat}, {lon} ({conf})")
                ent["gps_lat"] = round(lat, 6)
                ent["gps_lon"] = round(lon, 6)
                ent["gps_confidence"] = conf
            continue

        print(f"  GPS [{eid}]: querying '{query}'")
        lat, lon = nominatim_geocode(query)
        time.sleep(NOMINATIM_DELAY)

        if lat is not None:
            print(f"  GPS [{eid}]: acquired {lat}, {lon}")
            ent["gps_lat"] = lat
            ent["gps_lon"] = lon
            if ent.get("gps_confidence") in (None, "NONE", ""):
                ent["gps_confidence"] = "HIGH"
        elif eid in fallbacks:
            lat, lon = fallbacks[eid]
            conf = fallback_conf.get(eid, "LOW")
            print(f"  GPS [{eid}]: Nominatim null → fallback {lat}, {lon} ({conf})")
            ent["gps_lat"] = lat
            ent["gps_lon"] = lon
            ent["gps_confidence"] = conf
        else:
            print(f"  GPS [{eid}]: not acquired")


def propagate_gps_to_children(sites: List[dict]) -> None:
    """Copy parent GPS to child sites that still lack coordinates (LOW confidence)."""
    id_map = {s["site_id"]: s for s in sites}
    for s in sites:
        if s.get("gps_lat") is None and s.get("parent_site_id"):
            parent = id_map.get(s["parent_site_id"])
            if parent and parent.get("gps_lat") is not None:
                s["gps_lat"] = parent["gps_lat"]
                s["gps_lon"] = parent["gps_lon"]
                s["gps_confidence"] = "LOW"
                print(f"  GPS [{s['site_id']}]: propagated from parent {s['parent_site_id']} (LOW)")


def propagate_gps_to_trails(trails: List[dict], sites: List[dict]) -> None:
    """Copy parent site GPS to trails that lack coordinates (LOW confidence)."""
    id_map = {s["site_id"]: s for s in sites}
    for t in trails:
        if t.get("gps_lat") is None and t.get("parent_site_id"):
            parent = id_map.get(t["parent_site_id"])
            if parent and parent.get("gps_lat") is not None:
                t["gps_lat"] = parent["gps_lat"]
                t["gps_lon"] = parent["gps_lon"]
                t["gps_confidence"] = "LOW"
                print(f"  GPS [{t['trail_id']}]: propagated from parent site (LOW)")


def propagate_gps_to_aps(aps: List[dict], sites: List[dict]) -> None:
    """Copy parent site GPS to access points that lack coordinates (LOW confidence)."""
    id_map = {s["site_id"]: s for s in sites}
    for ap in aps:
        if ap.get("gps_lat") is None and ap.get("parent_entity_id"):
            parent = id_map.get(ap["parent_entity_id"])
            if parent and parent.get("gps_lat") is not None:
                ap["gps_lat"] = parent["gps_lat"]
                ap["gps_lon"] = parent["gps_lon"]
                ap["gps_confidence"] = "LOW"
                print(f"  GPS [{ap['access_point_id']}]: propagated from parent site (LOW)")


def add_plus_codes(entities: List[dict]) -> None:
    """Compute Plus Code for each entity with GPS. Modifies in-place."""
    if encode_plus_code is None:
        return
    for ent in entities:
        lat = ent.get("gps_lat")
        lon = ent.get("gps_lon")
        ent["plus_code"] = encode_plus_code(lat, lon) if (lat is not None and lon is not None) else ""


def add_gis_lookup(entities: List[dict]) -> None:
    """Derive township and municipality from GPS via OhioTownshipLookup. Modifies in-place."""
    if not _LOOKUP_AVAILABLE:
        return
    for ent in entities:
        lat = ent.get("gps_lat")
        lon = ent.get("gps_lon")
        if lat is None or lon is None:
            continue
        try:
            if not ent.get("township"):
                twp = _LOOKUP.get_township(lat, lon)
                if twp:
                    ent["township"] = twp
            if not ent.get("municipality"):
                muni = _LOOKUP.get_municipality(lat, lon)
                if muni:
                    ent["municipality"] = muni
        except Exception:
            pass


# ════════════════════════════════════════════════════════════════════════════
#  VOCABULARY VALIDATION GATE  (Stage 4.5)
# ════════════════════════════════════════════════════════════════════════════

def validate_sites(sites: List[dict]) -> List[str]:
    errors = []
    for s in sites:
        sid = s.get("site_id", "?")
        cat = s.get("category", "")
        sub = s.get("subtype", "")
        des = s.get("designation", "")
        sta = s.get("status", "")
        feats = s.get("features", "")

        if cat not in ALLOWED_CATEGORIES:
            errors.append(f"{sid}: invalid category '{cat}'")
        if sub:
            allowed = ALLOWED_SUBTYPES.get(cat, frozenset())
            if sub not in allowed:
                errors.append(f"{sid}: invalid subtype '{sub}' for category '{cat}'")
        if des:
            for term in des.split(";"):
                term = term.strip()
                if term and term not in ALLOWED_DESIGNATIONS:
                    errors.append(f"{sid}: invalid designation token '{term}'")
        if sta and sta not in ALLOWED_SITE_STATUSES:
            errors.append(f"{sid}: invalid status '{sta}'")
        if feats:
            for term in feats.split(";"):
                term = term.strip()
                if term and term not in ALLOWED_FEATURES:
                    errors.append(f"{sid}: invalid features term '{term}'")
    return errors


def validate_trails(trails: List[dict]) -> List[str]:
    errors = []
    checks = [
        ("use_type",    ALLOWED_TRAIL_USE_TYPES),
        ("surface_type", ALLOWED_TRAIL_SURFACES),
        ("origin_type", ALLOWED_TRAIL_ORIGINS),
        ("status",      ALLOWED_TRAIL_STATUSES),
        ("difficulty",  ALLOWED_TRAIL_DIFFICULTIES),
    ]
    for t in trails:
        tid = t.get("trail_id", "?")
        for field, allowed in checks:
            val = t.get(field, "")
            if val and val not in allowed:
                errors.append(f"{tid}: invalid {field} '{val}'")
    return errors


def validate_access_points(aps: List[dict]) -> List[str]:
    errors = []
    for ap in aps:
        aid = ap.get("access_point_id", "?")
        if ap.get("ap_type", "") not in ALLOWED_AP_TYPES:
            errors.append(f"{aid}: invalid ap_type '{ap.get('ap_type', '')}'")
        if ap.get("status", "") not in ALLOWED_AP_STATUSES:
            errors.append(f"{aid}: invalid status '{ap.get('status', '')}'")
    return errors


def run_vocab_gate(sites, trails, aps) -> None:
    """Stage 4.5 — halt on any vocabulary violation."""
    errors = validate_sites(sites) + validate_trails(trails) + validate_access_points(aps)
    if errors:
        print("FATAL: Vocabulary validation FAILED — halting pipeline.")
        for err in errors:
            print(f"  ERROR: {err}")
        sys.exit(1)
    print("  All vocabulary checks PASSED.")


# ════════════════════════════════════════════════════════════════════════════
#  TSV OUTPUT  (Stage 4)
# ════════════════════════════════════════════════════════════════════════════

def _write_tsv(path: str, columns: List[str], rows: List[dict], now: str) -> None:
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=columns, delimiter="\t",
                                extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            row.setdefault("created_at", now)
            row.setdefault("updated_at", now)
            out = {k: ("" if v is None else v) for k, v in row.items()}
            writer.writerow(out)
    print(f"  Wrote {len(rows)} rows -> {os.path.basename(path)}")


def write_all_tsvs(output_dir: str, prefix: str, now: str,
                   sites, trails, trail_segments,
                   trail_networks, site_networks, access_points) -> None:
    """Write six TSV files to output_dir. Files with zero entities get header only."""
    _write_tsv(os.path.join(output_dir, f"{prefix}_sites.tsv"),
               SITE_TSV_COLUMNS, sites, now)
    _write_tsv(os.path.join(output_dir, f"{prefix}_trails.tsv"),
               TRAIL_TSV_COLUMNS, trails, now)
    _write_tsv(os.path.join(output_dir, f"{prefix}_trail_segments.tsv"),
               TRAIL_SEGMENT_TSV_COLUMNS, trail_segments, now)
    _write_tsv(os.path.join(output_dir, f"{prefix}_trail_networks.tsv"),
               TRAIL_NETWORK_TSV_COLUMNS, trail_networks, now)
    _write_tsv(os.path.join(output_dir, f"{prefix}_site_networks.tsv"),
               SITE_NETWORK_TSV_COLUMNS, site_networks, now)
    _write_tsv(os.path.join(output_dir, f"{prefix}_access_points.tsv"),
               AP_TSV_COLUMNS, access_points, now)


# ════════════════════════════════════════════════════════════════════════════
#  INTEGRITY CHECK  (Stage 5)
# ════════════════════════════════════════════════════════════════════════════

def integrity_check(sites, trails, access_points) -> List[str]:
    warnings = []
    known_site_ids = {s["site_id"] for s in sites}

    # Missing GPS — suppress for gps_unresolvable entities (IMP-122)
    no_gps = [s["site_id"] for s in sites
              if s.get("gps_lat") is None and not s.get("gps_unresolvable")]
    if no_gps:
        warnings.append(f"Sites missing GPS ({len(no_gps)}): {', '.join(no_gps)}")

    # Parent references
    for s in sites:
        psid = s.get("parent_site_id", "")
        if psid and psid not in known_site_ids:
            warnings.append(f"{s['site_id']}: parent_site_id '{psid}' not in this run")
    for t in trails:
        psid = t.get("parent_site_id", "")
        if psid and psid not in known_site_ids:
            warnings.append(f"{t['trail_id']}: parent_site_id '{psid}' not in this run")
    for ap in access_points:
        peid = ap.get("parent_entity_id", "")
        if peid and peid not in known_site_ids:
            warnings.append(f"{ap['access_point_id']}: parent_entity_id '{peid}' not in run")

    # Duplicate IDs
    for id_list, label in [
        ([s["site_id"] for s in sites], "site"),
        ([t["trail_id"] for t in trails], "trail"),
        ([ap["access_point_id"] for ap in access_points], "ap"),
    ]:
        seen, dups = set(), set()
        for eid in id_list:
            (dups if eid in seen else seen).add(eid)
        if dups:
            warnings.append(f"Duplicate {label} IDs: {dups}")

    return warnings


# ════════════════════════════════════════════════════════════════════════════
#  DATABASE UPSERT  (Stage 6)
# ════════════════════════════════════════════════════════════════════════════

def _nullify_empty_numerics(row: dict, fields=("acres", "gps_lat", "gps_lon", "length_mi")) -> dict:
    for f in fields:
        if row.get(f) == "" or row.get(f) == "None":
            row[f] = None
    return row


def upsert_sites(cur, sites: List[dict], now: str, dry_run: bool) -> None:
    sql = """
    INSERT INTO sites (
        site_id, name, category, subtype, designation, status,
        ownership, governance, partner_agencies, coordination,
        description, location, acres, counties, municipality, township,
        gps_lat, gps_lon, plus_code, features, features_raw, notes,
        url_primary, urls, parent_site_id, created_at, updated_at
    ) VALUES (
        :site_id, :name, :category, :subtype, :designation, :status,
        :ownership, :governance, :partner_agencies, :coordination,
        :description, :location, :acres, :counties, :municipality, :township,
        :gps_lat, :gps_lon, :plus_code, :features, :features_raw, :notes,
        :url_primary, :urls, :parent_site_id, :created_at, :updated_at
    )
    ON CONFLICT(site_id) DO UPDATE SET
        name=excluded.name, category=excluded.category, subtype=excluded.subtype,
        designation=excluded.designation, status=excluded.status,
        ownership=excluded.ownership, governance=excluded.governance,
        partner_agencies=excluded.partner_agencies,
        coordination=excluded.coordination,
        description=excluded.description, location=excluded.location,
        acres=excluded.acres, counties=excluded.counties,
        municipality=excluded.municipality, township=excluded.township,
        gps_lat=excluded.gps_lat, gps_lon=excluded.gps_lon,
        plus_code=excluded.plus_code, features=excluded.features,
        features_raw=excluded.features_raw, notes=excluded.notes,
        url_primary=excluded.url_primary, urls=excluded.urls,
        parent_site_id=excluded.parent_site_id, updated_at=excluded.updated_at
    """
    for s in sites:
        row = {**s}
        row.setdefault("created_at", now); row.setdefault("updated_at", now)
        row.setdefault("township", ""); row.setdefault("plus_code", "")
        row.setdefault("features_raw", ""); row.setdefault("urls", "")
        row.setdefault("coordination", ""); row.setdefault("partner_agencies", "")
        row.setdefault("parent_site_id", "")
        _nullify_empty_numerics(row)
        if dry_run:
            print(f"  [DRY-RUN] UPSERT site {row['site_id']} — {row['name']}")
        else:
            cur.execute(sql, row)


def upsert_site_parents(cur, sites: List[dict], dry_run: bool) -> None:
    sql = "INSERT OR IGNORE INTO site_parent (site_id, parent_site_id) VALUES (?, ?)"
    for s in sites:
        if s.get("parent_site_id"):
            if dry_run:
                print(f"  [DRY-RUN] site_parent {s['site_id']} → {s['parent_site_id']}")
            else:
                cur.execute(sql, (s["site_id"], s["parent_site_id"]))


def upsert_trails(cur, trails: List[dict], now: str, dry_run: bool) -> None:
    sql = """
    INSERT INTO trails (
        trail_id, name, alternate_names, use_type, surface_type, origin_type,
        length_mi, counties, governance, partner_agencies,
        status, difficulty, accessibility,
        description, trail_history, identity_notes, notes,
        url_primary, maps, created_at, updated_at
    ) VALUES (
        :trail_id, :name, :alternate_names, :use_type, :surface_type, :origin_type,
        :length_mi, :counties, :governance, :partner_agencies,
        :status, :difficulty, :accessibility,
        :description, :trail_history, :identity_notes, :notes,
        :url_primary, :maps, :created_at, :updated_at
    )
    ON CONFLICT(trail_id) DO UPDATE SET
        name=excluded.name, alternate_names=excluded.alternate_names,
        use_type=excluded.use_type, surface_type=excluded.surface_type,
        origin_type=excluded.origin_type, length_mi=excluded.length_mi,
        counties=excluded.counties, governance=excluded.governance,
        partner_agencies=excluded.partner_agencies,
        status=excluded.status, difficulty=excluded.difficulty,
        accessibility=excluded.accessibility,
        description=excluded.description, trail_history=excluded.trail_history,
        identity_notes=excluded.identity_notes, notes=excluded.notes,
        url_primary=excluded.url_primary, maps=excluded.maps,
        updated_at=excluded.updated_at
    """
    for t in trails:
        row = {**t}
        row.setdefault("created_at", now); row.setdefault("updated_at", now)
        row.setdefault("alternate_names", ""); row.setdefault("origin_type", "")
        row.setdefault("partner_agencies", ""); row.setdefault("accessibility", "")
        row.setdefault("trail_history", ""); row.setdefault("identity_notes", "")
        row.setdefault("maps", "")
        _nullify_empty_numerics(row)
        if dry_run:
            print(f"  [DRY-RUN] UPSERT trail {row['trail_id']} — {row['name']}")
        else:
            cur.execute(sql, row)


def upsert_trail_parents(cur, trails: List[dict], dry_run: bool) -> None:
    sql = "INSERT OR IGNORE INTO trail_parents (trail_id, parent_site_id) VALUES (?, ?)"
    for t in trails:
        if t.get("parent_site_id"):
            if dry_run:
                print(f"  [DRY-RUN] trail_parent {t['trail_id']} → {t['parent_site_id']}")
            else:
                cur.execute(sql, (t["trail_id"], t["parent_site_id"]))


def upsert_access_points(cur, aps: List[dict], now: str, dry_run: bool) -> None:
    sql = """
    INSERT INTO access_points (
        access_point_id, name, ap_type, status,
        parent_entity_type, parent_entity_id,
        county, township, municipality, address,
        gps_lat, gps_lon, plus_code, features,
        identity_notes, notes, url_primary,
        created_at, updated_at
    ) VALUES (
        :access_point_id, :name, :ap_type, :status,
        :parent_entity_type, :parent_entity_id,
        :county, :township, :municipality, :address,
        :gps_lat, :gps_lon, :plus_code, :features,
        :identity_notes, :notes, :url_primary,
        :created_at, :updated_at
    )
    ON CONFLICT(access_point_id) DO UPDATE SET
        name=excluded.name, ap_type=excluded.ap_type, status=excluded.status,
        parent_entity_type=excluded.parent_entity_type,
        parent_entity_id=excluded.parent_entity_id,
        county=excluded.county, township=excluded.township,
        municipality=excluded.municipality, address=excluded.address,
        gps_lat=excluded.gps_lat, gps_lon=excluded.gps_lon,
        plus_code=excluded.plus_code, features=excluded.features,
        identity_notes=excluded.identity_notes, notes=excluded.notes,
        url_primary=excluded.url_primary, updated_at=excluded.updated_at
    """
    for ap in aps:
        row = {**ap}
        row.setdefault("created_at", now); row.setdefault("updated_at", now)
        row.setdefault("township", ""); row.setdefault("plus_code", "")
        row.setdefault("identity_notes", ""); row.setdefault("url_primary", "")
        row.setdefault("address", ""); row.setdefault("municipality", "")
        row.setdefault("county", "")
        _nullify_empty_numerics(row)
        if dry_run:
            print(f"  [DRY-RUN] UPSERT AP {row['access_point_id']} — {row['name']}")
        else:
            cur.execute(sql, row)


def upsert_run_metadata(cur, run_id: str, county: str, state: str,
                        run_date: str, records_input: int,
                        normalized: int, held: int, notes: str,
                        now: str, dry_run: bool) -> None:
    sql = """
    INSERT INTO run_metadata
        (run_id, county, state, run_date, records_input, normalized, held, notes, created_at)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ON CONFLICT(run_id) DO UPDATE SET
        normalized=excluded.normalized, held=excluded.held, notes=excluded.notes
    """
    if dry_run:
        print(f"  [DRY-RUN] run_metadata {run_id} — normalized={normalized} held={held}")
    else:
        cur.execute(sql, (run_id, county, state, run_date,
                          records_input, normalized, held, notes, now))


# ════════════════════════════════════════════════════════════════════════════
#  HELD-ENTITY HELPERS AND UPSERTS  (IMP-118 / IMP-119)
# ════════════════════════════════════════════════════════════════════════════

def _is_held(rec: dict) -> bool:
    """Return True if an entity record is held and should be excluded from pipeline output."""
    sf = rec.get("status_flag") or ""
    if sf.startswith("HELD"):
        return True
    notes = rec.get("notes") or ""
    return ("HELD" in notes and
            ("cross_county_held" in notes or "gps_missing" in notes or "parent_held" in notes))


def _get_hold_reason(rec: dict):
    """Return (hold_reason, hold_detail) for a held entity, using canonical IMP-113 values."""
    hd    = rec.get("hold_detail") or ""
    notes = rec.get("notes") or ""
    if "cross_county_held" in hd or "cross_county_held" in notes:
        detail = hd if hd else notes.strip().split("\n")[0]
        return "cross_county_held", detail[:250]
    if "parent_held" in hd:
        return "parent_held", hd[:250]
    if "gps_missing" in hd or "gps_missing" in notes:
        return "gps_missing", "gps_missing"
    return "unknown", (hd or notes[:100])


def upsert_held_entities(cur, held_sites: List[dict], held_trails: List[dict],
                         held_aps: List[dict], county: str,
                         run_id: str, now: str, dry_run: bool) -> None:
    sql = """
    INSERT OR IGNORE INTO held_entities
        (record_id, entity_type, name, county, hold_reason, hold_detail, run_id, created_at)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """
    rows = (
        [(s["site_id"],            "Site",         s.get("name", ""), s) for s in held_sites]  +
        [(t["trail_id"],           "Trail",        t.get("name", ""), t) for t in held_trails] +
        [(ap["access_point_id"],   "Access Point", ap.get("name", ""), ap) for ap in held_aps]
    )
    ct = 0
    for record_id, entity_type, name, rec in rows:
        reason, detail = _get_hold_reason(rec)
        if dry_run:
            print(f"  [DRY-RUN] held_entities {record_id} ({entity_type}) reason={reason}")
        else:
            cur.execute(sql, (record_id, entity_type, name, county,
                              reason, detail, run_id, now))
        ct += 1
    if ct:
        print(f"  held_entities: {ct} rows")


def upsert_access_point_parents(cur, aps: List[dict], dry_run: bool) -> None:
    sql = """
    INSERT OR IGNORE INTO access_point_parents
        (access_point_id, parent_entity_type, parent_entity_id)
    VALUES (?, ?, ?)
    """
    ct = 0
    for ap in aps:
        ptype = ap.get("parent_entity_type", "")
        pid   = ap.get("parent_entity_id",   "")
        if ptype and pid:
            if dry_run:
                print(f"  [DRY-RUN] access_point_parents {ap['access_point_id']} -> {ptype} {pid}")
            else:
                cur.execute(sql, (ap["access_point_id"], ptype, pid))
            ct += 1
    if ct:
        print(f"  access_point_parents: {ct} rows")


# ════════════════════════════════════════════════════════════════════════════
#  PIPELINE RUNNER
# ════════════════════════════════════════════════════════════════════════════

class ReviewRequired(Exception):
    """
    Raised by Stage 5.5 when confirm_review=False and dry_run=False.
    The pipeline has written TSV files and completed integrity checks but
    has NOT touched the database. Re-run with --confirm-review once the
    TSV output has been manually verified.
    """


class PipelineRunner:
    """
    Orchestrates Stages 3–6 for a single county pipeline run.

    Parameters
    ----------
    run_id        : str   e.g. "van_wert_oh_2026_04_14"
    county        : str   e.g. "Van Wert"
    state         : str   e.g. "Ohio"
    run_date      : str   ISO date e.g. "2026-04-19"
    records_input : int   total raw records in discovery YAML
    output_dir    : str   directory for TSV files
    db_path       : str   path to natural_areas_v5.db
    tsv_prefix    : str   filename prefix for TSVs (default: snake_case county_state)
    county_bbox   : tuple (lat_min, lat_max, lon_min, lon_max) — for logging only
    """

    def __init__(self, run_id: str, county: str, state: str,
                 run_date: str, records_input: int,
                 output_dir: str, db_path: str,
                 tsv_prefix: str = None,
                 county_bbox: tuple = None):
        self.run_id        = run_id
        self.county        = county
        self.state         = state
        self.run_date      = run_date
        self.records_input = records_input
        self.output_dir    = output_dir
        self.db_path       = db_path
        self.tsv_prefix    = tsv_prefix or run_id.replace("-", "_")
        self.county_bbox   = county_bbox
        self.now           = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    def run(self,
            sites, trails, access_points,
            trail_segments=None, trail_networks=None, site_networks=None,
            gps_queries: Dict[str, str] = None,
            fallback_gps: Dict[str, Tuple[float, float]] = None,
            fallback_conf: Dict[str, str] = None,
            run_notes: str = "",
            dry_run: bool = False,
            confirm_review: bool = False) -> None:

        trail_segments  = trail_segments  or []
        trail_networks  = trail_networks  or []
        site_networks   = site_networks   or []
        gps_queries     = gps_queries     or {}
        fallback_gps    = fallback_gps    or {}
        fallback_conf   = fallback_conf   or {}

        # ── Filter held entities before pipeline stages (IMP-118) ─────────
        held_sites  = [s  for s  in sites          if _is_held(s)]
        held_trails = [t  for t  in trails          if _is_held(t)]
        held_aps    = [ap for ap in access_points   if _is_held(ap)]
        sites          = [s  for s  in sites          if not _is_held(s)]
        trails         = [t  for t  in trails          if not _is_held(t)]
        access_points  = [ap for ap in access_points   if not _is_held(ap)]
        trail_segments = [ts for ts in trail_segments  if not _is_held(ts)]
        trail_networks = [tn for tn in trail_networks  if not _is_held(tn)]
        site_networks  = [sn for sn in site_networks   if not _is_held(sn)]
        total_held = len(held_sites) + len(held_trails) + len(held_aps)

        print("=" * 60)
        print(f"NAP Pipeline  |  {self.county} County, {self.state}  |  {self.run_id}")
        print(f"DB: {self.db_path}")
        print(f"Dry run: {dry_run}")
        if total_held:
            print(f"Held (excluded from pipeline): {total_held} "
                  f"({len(held_sites)} sites, {len(held_trails)} trails, {len(held_aps)} APs)")
        print("=" * 60)

        # Default timestamps and required fields on every entity
        self._stamp_entities(sites, trails, access_points,
                             trail_segments, trail_networks, site_networks)

        # ── Stage 3: GPS Acquisition ─────────────────────────────────────
        print(f"\n[Stage 3] GPS Acquisition")
        if _REQUESTS_OK:
            acquire_gps(sites, "site_id", gps_queries, fallback_gps, fallback_conf)
        propagate_gps_to_children(sites)
        propagate_gps_to_trails(trails, sites)
        propagate_gps_to_aps(access_points, sites)
        add_plus_codes(sites); add_plus_codes(trails); add_plus_codes(access_points)
        add_gis_lookup(sites)
        gps_count = sum(1 for s in sites if s.get("gps_lat") is not None)
        print(f"  GPS acquired: {gps_count}/{len(sites)} sites")

        # ── Stage 4.5: Vocabulary Validation Gate ────────────────────────
        print(f"\n[Stage 4.5] Vocabulary Validation Gate")
        run_vocab_gate(sites, trails, access_points)

        # ── Stage 4: TSV Output ──────────────────────────────────────────
        print(f"\n[Stage 4] TSV Output")
        write_all_tsvs(self.output_dir, self.tsv_prefix, self.now,
                       sites, trails, trail_segments,
                       trail_networks, site_networks, access_points)

        # ── Stage 5: Integrity Check ─────────────────────────────────────
        print(f"\n[Stage 5] Integrity Check")
        warnings = integrity_check(sites, trails, access_points)
        if warnings:
            for w in warnings:
                print(f"  WARNING: {w}")
        else:
            print("  No integrity issues found.")

        # ── Stage 5.5: Human Review Gate ─────────────────────────────────
        print(f"\n[Stage 5.5] Human Review Gate")
        if dry_run:
            print("  Dry run — review gate bypassed.")
        elif confirm_review:
            print("  Review confirmed (--confirm-review). Proceeding to upsert.")
        else:
            tsv_dir = self.output_dir
            print("  ┌─────────────────────────────────────────────────────────┐")
            print("  │  PIPELINE HALTED — REVIEW REQUIRED BEFORE UPSERT       │")
            print("  └─────────────────────────────────────────────────────────┘")
            print(f"  TSV files written to: {tsv_dir}")
            print(f"  Entity counts: {len(sites)} Sites, {len(trails)} Trails, "
                  f"{len(trail_segments)} Segments, {len(trail_networks)} Trail Networks, "
                  f"{len(site_networks)} Site Networks, {len(access_points)} APs")
            print()
            print("  Review checklist:")
            print("    1. Entity counts look reasonable for this county")
            print("    2. Category/subtype assignments are substantively correct")
            print("    3. GPS coordinates spot-check — do they land in the right county?")
            print("    4. Held entities (if any) are expected")
            print()
            print("  To proceed: re-run with --confirm-review")
            print("  Example:")
            print(f"    python utilities/na_run_county.py --county-dir <dir> --confirm-review")
            raise ReviewRequired(
                f"Stage 5.5: Human review required before upsert. "
                f"Re-run with --confirm-review after verifying TSV output in {tsv_dir}"
            )

        # ── Stage 6: Database Upsert ─────────────────────────────────────
        print(f"\n[Stage 6] Database Upsert")
        normalized = len(sites) + len(trails) + len(access_points) + \
                     len(trail_segments) + len(trail_networks) + len(site_networks)
        if not run_notes:
            run_notes = (f"{self.county} County {self.state} pipeline complete. "
                         f"{len(sites)} Sites, {len(trails)} Trails, "
                         f"{len(access_points)} APs, "
                         f"{len(trail_segments)} Trail Segments, "
                         f"{len(trail_networks)} Trail Networks, "
                         f"{len(site_networks)} Site Networks.")

        conn = sqlite3.connect(self.db_path)
        try:
            cur = conn.cursor()
            upsert_sites(cur, sites, self.now, dry_run)
            upsert_site_parents(cur, sites, dry_run)
            upsert_trails(cur, trails, self.now, dry_run)
            upsert_trail_parents(cur, trails, dry_run)
            upsert_access_points(cur, access_points, self.now, dry_run)
            upsert_access_point_parents(cur, access_points, dry_run)          # IMP-119
            upsert_held_entities(cur, held_sites, held_trails, held_aps,      # IMP-119
                                 self.county, self.run_id, self.now, dry_run)
            upsert_run_metadata(cur, self.run_id, self.county, self.state,
                                self.run_date, self.records_input,
                                normalized, total_held, run_notes, self.now, dry_run)  # IMP-120
            if not dry_run:
                conn.commit()
                print(f"  Committed {len(sites)} sites, {len(trails)} trails, "
                      f"{len(access_points)} APs to {os.path.basename(self.db_path)}")
        except Exception as e:
            conn.rollback()
            print(f"  ERROR during upsert: {e}", file=sys.stderr)
            raise
        finally:
            conn.close()

        # ── Summary ──────────────────────────────────────────────────────
        print("\n" + "=" * 60)
        print("PIPELINE COMPLETE")
        print(f"  Sites:          {len(sites)}")
        print(f"  Trails:         {len(trails)}")
        print(f"  Trail Segments: {len(trail_segments)}")
        print(f"  Trail Networks: {len(trail_networks)}")
        print(f"  Site Networks:  {len(site_networks)}")
        print(f"  Access Points:  {len(access_points)}")
        missing_gps = [s["site_id"] for s in sites if s.get("gps_lat") is None]
        if missing_gps:
            print(f"  Sites still missing GPS: {', '.join(missing_gps)}")
        print("=" * 60)

    # ── Helpers ───────────────────────────────────────────────────────────

    def _stamp_entities(self, *entity_lists):
        now = self.now
        for lst in entity_lists:
            for e in lst:
                e.setdefault("created_at", now)
                e["updated_at"] = now
