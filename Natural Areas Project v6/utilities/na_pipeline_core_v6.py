#!/usr/bin/env python3
"""
na_pipeline_core_v6.py — Natural Areas Project Pipeline Core Module (v6)
v2.0  |  2026-05-31

v6 changes from v1.1 (na_pipeline_core.py):
  - Four entity types: Site, Trailthing, Site Network, Access Point
  - Trail/Trail Segment/Trail Network entity handling removed
  - trailthings table added; legacy trail tables untouched in DB
  - trailthing_hierarchy relationship table added
  - Single GPS acquisition pass (no separate propagate_gps_to_trails)
  - Trailthings are multi-location — no GPS, Plus Code, township, municipality
  - New Site fields: habitat_type, access_notes, last_verified_date, field_verified
  - New AP fields: last_verified_date, field_verified
  - parent_site_network_id replaces external_parent_id/external_parent_type
  - Stage labels updated to match Processing Orchestration Module v6.0

Shared pipeline logic for all v6 county pipeline scripts.
Covers Stages 3–8: GPS Acquisition → TSV Output → Vocabulary Validation Gate
                   → Integrity Check → Human Review Gate → Database Upsert.

Stages 1–2 (Resolution, Normalization) remain county-specific — the
normalized entity lists are defined in the county config and passed into
PipelineRunner.

VOCABULARY SOURCES (read before normalization in every county):
    vocabularies/na_site_vocabulary_v6.0.md
    vocabularies/na_trailthing_vocabulary_v6.0.md
    vocabularies/na_site_network_vocabulary_v6.0.md
    vocabularies/na_access_point_vocabulary_v6.0.md
"""

import csv
import os
import sqlite3
import sys
import time
from datetime import datetime, timezone
from typing import Dict, List, Optional, Tuple

# IMP-128: Windows console UTF-8 fix
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
V6_ROOT    = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))

# Utilities are now in the v6 utilities folder
sys.path.insert(0, SCRIPT_DIR)

# ── Optional dependencies ────────────────────────────────────────────────────
try:
    from na_plus_code import encode_plus_code
except ImportError:
    encode_plus_code = None
    print("WARNING [na_pipeline_core_v6]: na_plus_code not found. Plus codes will be blank.")

try:
    from na_township_lookup import OhioTownshipLookup
    _LOOKUP = OhioTownshipLookup()
    _LOOKUP_AVAILABLE = True
except Exception as e:
    _LOOKUP = None
    _LOOKUP_AVAILABLE = False
    print(f"WARNING [na_pipeline_core_v6]: OhioTownshipLookup unavailable ({e}).")

try:
    import requests as _requests
    _REQUESTS_OK = True
except ImportError:
    _requests = None
    _REQUESTS_OK = False
    print("WARNING [na_pipeline_core_v6]: 'requests' not available. Nominatim GPS disabled.")

# ── Nominatim config ─────────────────────────────────────────────────────────
NOMINATIM_URL     = "https://nominatim.openstreetmap.org/search"
NOMINATIM_DELAY   = 1.1
NOMINATIM_HEADERS = {
    "User-Agent": "NaturalAreasProject/6.x (research use; admin contact available)",
    "Accept-Language": "en",
}
US_LAT_MIN, US_LAT_MAX = 24.0, 50.0
US_LON_MIN, US_LON_MAX = -130.0, -65.0

# ── Vocabulary constants ─────────────────────────────────────────────────────
try:
    from na_vocab_constants_v6 import (
        ALLOWED_CATEGORIES,
        ALLOWED_SUBTYPES,
        ALLOWED_DESIGNATIONS,
        ALLOWED_SITE_STATUSES,
        ALLOWED_FEATURES,
        ALLOWED_TRAILTHING_USE_TYPES,
        ALLOWED_TRAILTHING_SURFACES,
        ALLOWED_TRAILTHING_ORIGINS,
        ALLOWED_TRAILTHING_STATUSES,
        ALLOWED_TRAILTHING_DIFFICULTIES,
        ALLOWED_SN_NETWORK_TYPES,
        ALLOWED_SN_ORG_TYPES,
        ALLOWED_SN_STATUSES,
        ALLOWED_AP_TYPES,
        ALLOWED_AP_STATUSES,
    )
except ImportError:
    print("WARNING [na_pipeline_core_v6]: na_vocab_constants_v6 not found. "
          "Vocabulary validation will be skipped.")
    ALLOWED_CATEGORIES = ALLOWED_SUBTYPES = ALLOWED_DESIGNATIONS = frozenset()
    ALLOWED_SITE_STATUSES = ALLOWED_FEATURES = frozenset()
    ALLOWED_TRAILTHING_USE_TYPES = ALLOWED_TRAILTHING_SURFACES = frozenset()
    ALLOWED_TRAILTHING_ORIGINS = ALLOWED_TRAILTHING_STATUSES = frozenset()
    ALLOWED_TRAILTHING_DIFFICULTIES = frozenset()
    ALLOWED_SN_NETWORK_TYPES = ALLOWED_SN_ORG_TYPES = ALLOWED_SN_STATUSES = frozenset()
    ALLOWED_AP_TYPES = ALLOWED_AP_STATUSES = frozenset()

# ── TSV column definitions ───────────────────────────────────────────────────
# Canonical column order per v6 TSV Output Specifications.
# Entity IDs: site_id and access_point_id are DB-only (excluded from TSV).
# trailthing_id is included in Trailthing TSV at position 31.

SITE_TSV_COLUMNS = [
    "name", "category", "subtype", "designation", "status",
    "ownership", "governance", "partner_agencies", "coordination",
    "description", "habitat_type", "features", "access_notes",
    "location", "acres", "counties", "municipality", "township",
    "gps_lat", "gps_lon", "plus_code",
    "notes", "url_primary", "urls",
    "last_verified_date", "field_verified",
    "parent_site_id", "parent_site_name",
    "created_at", "updated_at",
]  # 30 fields, 29 tab delimiters

TRAILTHING_TSV_COLUMNS = [
    "name", "alternate_names", "source_term", "source_hierarchy_context",
    "parent_id", "parent_name",
    "site_parent_id", "site_parent_name",
    "parent_site_network_id", "parent_site_network_name",
    "use_type", "surface_type", "origin_type", "org_type",
    "status", "difficulty", "accessibility",
    "ownership", "governance", "partner_agencies", "coordination",
    "counties", "states_included", "total_length",
    "description", "trail_history", "identity_notes", "notes",
    "url", "maps",
    "trailthing_id",
]  # 31 fields, 30 tab delimiters

SITE_NETWORK_TSV_COLUMNS = [
    "name", "network_type", "org_type", "status",
    "ownership", "governance", "partner_agencies", "coordination",
    "counties", "states_included",
    "member_count", "member_site_ids", "member_site_names",
    "description", "identity_notes", "notes", "url",
    "network_id",
]  # 18 fields, 17 tab delimiters

AP_TSV_COLUMNS = [
    "name", "ap_type", "status",
    "parent_entity_type", "parent_entity_id", "parent_entity_name",
    "counties", "township", "municipality", "location",
    "gps_lat", "gps_lon", "plus_code", "features",
    "identity_notes", "notes", "url_primary",
    "last_verified_date", "field_verified",
    "created_at", "updated_at",
]  # 20 fields (note: access_point_id is DB-only, not in TSV)


# ════════════════════════════════════════════════════════════════════════════
#  GPS ACQUISITION  (Stages 4a / 4b)
# ════════════════════════════════════════════════════════════════════════════

def nominatim_geocode(query: str) -> Tuple[Optional[float], Optional[float]]:
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
    """Stage 4b — GPS acquisition for Sites and APs. Modifies entities in-place."""
    if fallback_conf is None:
        fallback_conf = {}
    for ent in entities:
        eid = ent[id_field]
        if ent.get("gps_lat") is not None:
            continue
        query = queries.get(eid)
        if not query:
            if eid in fallbacks:
                lat, lon = fallbacks[eid]
                conf = fallback_conf.get(eid, "LOW")
                print(f"  GPS [{eid}]: direct fallback {lat}, {lon} ({conf})")
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
    """Copy parent GPS to child sites lacking coordinates (LOW confidence)."""
    id_map = {s["site_id"]: s for s in sites}
    for s in sites:
        if s.get("gps_lat") is None and s.get("parent_site_id"):
            parent = id_map.get(s["parent_site_id"])
            if parent and parent.get("gps_lat") is not None:
                s["gps_lat"] = parent["gps_lat"]
                s["gps_lon"] = parent["gps_lon"]
                s["gps_confidence"] = "LOW"
                print(f"  GPS [{s['site_id']}]: propagated from parent (LOW)")


def propagate_gps_to_aps(aps: List[dict], sites: List[dict]) -> None:
    """Copy parent site GPS to APs lacking coordinates (LOW confidence)."""
    id_map = {s["site_id"]: s for s in sites}
    for ap in aps:
        if ap.get("gps_lat") is None and ap.get("parent_entity_id"):
            parent = id_map.get(ap["parent_entity_id"])
            if parent and parent.get("gps_lat") is not None:
                ap["gps_lat"] = parent["gps_lat"]
                ap["gps_lon"] = parent["gps_lon"]
                ap["gps_confidence"] = "LOW"
                print(f"  GPS [{ap['access_point_id']}]: propagated from parent (LOW)")


def add_plus_codes(entities: List[dict]) -> None:
    """Compute Plus Code for entities with GPS. Modifies in-place."""
    if encode_plus_code is None:
        return
    for ent in entities:
        lat = ent.get("gps_lat")
        lon = ent.get("gps_lon")
        ent["plus_code"] = (encode_plus_code(lat, lon)
                            if (lat is not None and lon is not None) else "")


def add_gis_lookup(entities: List[dict]) -> None:
    """Derive township and municipality from GPS. Modifies in-place."""
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
#  VOCABULARY VALIDATION GATE  (Stage 6.5)
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
                    errors.append(f"{sid}: invalid designation '{term}'")
        if sta and sta not in ALLOWED_SITE_STATUSES:
            errors.append(f"{sid}: invalid status '{sta}'")
        if feats:
            for term in feats.split(";"):
                term = term.strip()
                if term and term not in ALLOWED_FEATURES:
                    errors.append(f"{sid}: invalid features term '{term}'")
    return errors


def validate_trailthings(trailthings: List[dict]) -> List[str]:
    errors = []
    checks = [
        ("use_type",    ALLOWED_TRAILTHING_USE_TYPES),
        ("surface_type", ALLOWED_TRAILTHING_SURFACES),
        ("origin_type", ALLOWED_TRAILTHING_ORIGINS),
        ("status",      ALLOWED_TRAILTHING_STATUSES),
        ("difficulty",  ALLOWED_TRAILTHING_DIFFICULTIES),
    ]
    for tt in trailthings:
        tid = tt.get("trailthing_id", "?")
        if not tt.get("source_term"):
            print(f"  WARN: {tid}: source_term is blank — check discovery record")
        for field, allowed in checks:
            val = tt.get(field, "")
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


def run_vocab_gate(sites, trailthings, aps) -> None:
    """Stage 6.5 — halt on any vocabulary violation."""
    errors = (validate_sites(sites) +
              validate_trailthings(trailthings) +
              validate_access_points(aps))
    if errors:
        print("FATAL: Vocabulary validation FAILED — halting pipeline.")
        for err in errors:
            print(f"  ERROR: {err}")
        sys.exit(1)
    print("  All vocabulary checks PASSED.")


# ════════════════════════════════════════════════════════════════════════════
#  TSV OUTPUT  (Stage 6)
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
    print(f"  Wrote {len(rows)} rows → {os.path.basename(path)}")


def write_all_tsvs(output_dir: str, prefix: str, now: str,
                   sites, trailthings, site_networks, access_points) -> None:
    """Write four TSV files to output_dir. Files with zero entities get header only."""
    _write_tsv(os.path.join(output_dir, f"{prefix}_sites.tsv"),
               SITE_TSV_COLUMNS, sites, now)
    _write_tsv(os.path.join(output_dir, f"{prefix}_trailthings.tsv"),
               TRAILTHING_TSV_COLUMNS, trailthings, now)
    _write_tsv(os.path.join(output_dir, f"{prefix}_site_networks.tsv"),
               SITE_NETWORK_TSV_COLUMNS, site_networks, now)
    _write_tsv(os.path.join(output_dir, f"{prefix}_access_points.tsv"),
               AP_TSV_COLUMNS, access_points, now)


# ════════════════════════════════════════════════════════════════════════════
#  INTEGRITY CHECK  (Stage 7)
# ════════════════════════════════════════════════════════════════════════════

def integrity_check(sites, trailthings, access_points) -> List[str]:
    warnings = []
    known_site_ids = {s["site_id"] for s in sites}
    known_tt_ids   = {tt["trailthing_id"] for tt in trailthings}

    # GPS missing (Sites and APs only — Trailthings not gated)
    no_gps = [s["site_id"] for s in sites
              if s.get("gps_lat") is None and not s.get("gps_unresolvable")]
    if no_gps:
        warnings.append(f"Sites missing GPS ({len(no_gps)}): {', '.join(no_gps)}")

    # Parent references — Sites
    for s in sites:
        psid = s.get("parent_site_id", "")
        if psid and psid not in known_site_ids:
            warnings.append(f"{s['site_id']}: parent_site_id '{psid}' not in this run")

    # Parent references — Trailthings
    for tt in trailthings:
        pid = tt.get("parent_id", "")
        if pid and pid not in known_tt_ids:
            warnings.append(f"{tt['trailthing_id']}: parent_id '{pid}' not in this run")

    # Parent references — APs
    for ap in access_points:
        peid = ap.get("parent_entity_id", "")
        if peid and peid not in known_site_ids and peid not in known_tt_ids:
            warnings.append(f"{ap['access_point_id']}: parent_entity_id '{peid}' not in run")

    # Cross-entity name pairings (ID present but name blank)
    for s in sites:
        sid = s["site_id"]
        if s.get("parent_site_id") and not s.get("parent_site_name"):
            warnings.append(f"{sid}: parent_site_id populated but parent_site_name blank")
    for tt in trailthings:
        tid = tt["trailthing_id"]
        if tt.get("parent_id") and not tt.get("parent_name"):
            warnings.append(f"{tid}: parent_id populated but parent_name blank")
        if tt.get("site_parent_id") and not tt.get("site_parent_name"):
            warnings.append(f"{tid}: site_parent_id populated but site_parent_name blank")
        if tt.get("parent_site_network_id") and not tt.get("parent_site_network_name"):
            warnings.append(f"{tid}: parent_site_network_id populated but name blank")
    for ap in access_points:
        aid = ap["access_point_id"]
        if ap.get("parent_entity_id") and not ap.get("parent_entity_name"):
            warnings.append(f"{aid}: parent_entity_id populated but parent_entity_name blank")

    # Duplicate IDs
    for id_list, label in [
        ([s["site_id"] for s in sites], "site"),
        ([tt["trailthing_id"] for tt in trailthings], "trailthing"),
        ([ap["access_point_id"] for ap in access_points], "ap"),
    ]:
        seen, dups = set(), set()
        for eid in id_list:
            (dups if eid in seen else seen).add(eid)
        if dups:
            warnings.append(f"Duplicate {label} IDs: {dups}")

    return warnings


# ════════════════════════════════════════════════════════════════════════════
#  DATABASE UPSERT  (Stage 8)
# ════════════════════════════════════════════════════════════════════════════

def _nullify_empty_numerics(row: dict,
                            fields=("acres", "gps_lat", "gps_lon",
                                    "total_length", "member_count")) -> dict:
    for f in fields:
        if row.get(f) == "" or row.get(f) == "None":
            row[f] = None
    return row


def upsert_sites(cur, sites: List[dict], now: str, dry_run: bool) -> None:
    sql = """
    INSERT INTO sites (
        site_id, name, category, subtype, designation, status,
        ownership, governance, partner_agencies, coordination,
        description, habitat_type, features, features_raw, access_notes,
        location, acres, counties, municipality, township,
        gps_lat, gps_lon, plus_code,
        notes, url_primary, urls,
        last_verified_date, field_verified,
        parent_site_id, created_at, updated_at
    ) VALUES (
        :site_id, :name, :category, :subtype, :designation, :status,
        :ownership, :governance, :partner_agencies, :coordination,
        :description, :habitat_type, :features, :features_raw, :access_notes,
        :location, :acres, :counties, :municipality, :township,
        :gps_lat, :gps_lon, :plus_code,
        :notes, :url_primary, :urls,
        :last_verified_date, :field_verified,
        :parent_site_id, :created_at, :updated_at
    )
    ON CONFLICT(site_id) DO UPDATE SET
        name=excluded.name, category=excluded.category, subtype=excluded.subtype,
        designation=excluded.designation, status=excluded.status,
        ownership=excluded.ownership, governance=excluded.governance,
        partner_agencies=excluded.partner_agencies,
        coordination=excluded.coordination,
        description=excluded.description, habitat_type=excluded.habitat_type,
        features=excluded.features, features_raw=excluded.features_raw,
        access_notes=excluded.access_notes,
        location=excluded.location, acres=excluded.acres,
        counties=excluded.counties, municipality=excluded.municipality,
        township=excluded.township,
        gps_lat=excluded.gps_lat, gps_lon=excluded.gps_lon,
        plus_code=excluded.plus_code,
        notes=excluded.notes, url_primary=excluded.url_primary, urls=excluded.urls,
        last_verified_date=excluded.last_verified_date,
        field_verified=excluded.field_verified,
        parent_site_id=excluded.parent_site_id, updated_at=excluded.updated_at
    """
    for s in sites:
        row = {**s}
        row.setdefault("created_at", now)
        row.setdefault("updated_at", now)
        row.setdefault("township", "")
        row.setdefault("plus_code", "")
        row.setdefault("features_raw", "")
        row.setdefault("urls", "")
        row.setdefault("coordination", "")
        row.setdefault("partner_agencies", "")
        row.setdefault("parent_site_id", "")
        row.setdefault("habitat_type", "")
        row.setdefault("access_notes", "")
        row.setdefault("last_verified_date", "")
        row.setdefault("field_verified", False)
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


def upsert_trailthings(cur, trailthings: List[dict], now: str, dry_run: bool) -> None:
    sql = """
    INSERT INTO trailthings (
        trailthing_id, name, alternate_names,
        source_term, source_hierarchy_context,
        parent_id, site_parent_id, parent_site_network_id,
        use_type, surface_type, origin_type, org_type,
        status, difficulty, accessibility,
        ownership, governance, partner_agencies, coordination,
        counties, states_included, total_length,
        description, trail_history, identity_notes, notes,
        url, maps, created_at, updated_at
    ) VALUES (
        :trailthing_id, :name, :alternate_names,
        :source_term, :source_hierarchy_context,
        :parent_id, :site_parent_id, :parent_site_network_id,
        :use_type, :surface_type, :origin_type, :org_type,
        :status, :difficulty, :accessibility,
        :ownership, :governance, :partner_agencies, :coordination,
        :counties, :states_included, :total_length,
        :description, :trail_history, :identity_notes, :notes,
        :url, :maps, :created_at, :updated_at
    )
    ON CONFLICT(trailthing_id) DO UPDATE SET
        name=excluded.name, alternate_names=excluded.alternate_names,
        source_term=excluded.source_term,
        source_hierarchy_context=excluded.source_hierarchy_context,
        parent_id=excluded.parent_id, site_parent_id=excluded.site_parent_id,
        parent_site_network_id=excluded.parent_site_network_id,
        use_type=excluded.use_type, surface_type=excluded.surface_type,
        origin_type=excluded.origin_type, org_type=excluded.org_type,
        status=excluded.status, difficulty=excluded.difficulty,
        accessibility=excluded.accessibility,
        ownership=excluded.ownership, governance=excluded.governance,
        partner_agencies=excluded.partner_agencies,
        coordination=excluded.coordination,
        counties=excluded.counties, states_included=excluded.states_included,
        total_length=excluded.total_length,
        description=excluded.description, trail_history=excluded.trail_history,
        identity_notes=excluded.identity_notes, notes=excluded.notes,
        url=excluded.url, maps=excluded.maps, updated_at=excluded.updated_at
    """
    for tt in trailthings:
        row = {**tt}
        row.setdefault("created_at", now)
        row.setdefault("updated_at", now)
        row.setdefault("alternate_names", "")
        row.setdefault("source_term", "")
        row.setdefault("source_hierarchy_context", "")
        row.setdefault("parent_id", "")
        row.setdefault("site_parent_id", "")
        row.setdefault("parent_site_network_id", "")
        row.setdefault("org_type", "")
        row.setdefault("origin_type", "")
        row.setdefault("partner_agencies", "")
        row.setdefault("coordination", "")
        row.setdefault("states_included", "")
        row.setdefault("trail_history", "")
        row.setdefault("identity_notes", "")
        row.setdefault("maps", "")
        row.setdefault("accessibility", "")
        _nullify_empty_numerics(row)
        if dry_run:
            print(f"  [DRY-RUN] UPSERT trailthing {row['trailthing_id']} — {row['name']}")
        else:
            cur.execute(sql, row)


def upsert_trailthing_hierarchy(cur, trailthings: List[dict], dry_run: bool) -> None:
    sql = """
    INSERT OR IGNORE INTO trailthing_hierarchy (parent_id, child_id) VALUES (?, ?)
    """
    ct = 0
    for tt in trailthings:
        if tt.get("parent_id"):
            if dry_run:
                print(f"  [DRY-RUN] trailthing_hierarchy {tt['parent_id']} → {tt['trailthing_id']}")
            else:
                cur.execute(sql, (tt["parent_id"], tt["trailthing_id"]))
            ct += 1
    if ct:
        print(f"  trailthing_hierarchy: {ct} rows")


def upsert_site_networks(cur, site_networks: List[dict], now: str, dry_run: bool) -> None:
    sql = """
    INSERT INTO site_networks (
        network_id, name, network_type, org_type, status,
        ownership, governance, partner_agencies, coordination,
        counties, states_included, member_count, member_site_ids,
        description, identity_notes, notes, url,
        created_at, updated_at
    ) VALUES (
        :network_id, :name, :network_type, :org_type, :status,
        :ownership, :governance, :partner_agencies, :coordination,
        :counties, :states_included, :member_count, :member_site_ids,
        :description, :identity_notes, :notes, :url,
        :created_at, :updated_at
    )
    ON CONFLICT(network_id) DO UPDATE SET
        name=excluded.name, network_type=excluded.network_type,
        org_type=excluded.org_type, status=excluded.status,
        ownership=excluded.ownership, governance=excluded.governance,
        partner_agencies=excluded.partner_agencies,
        coordination=excluded.coordination,
        counties=excluded.counties, states_included=excluded.states_included,
        member_count=excluded.member_count, member_site_ids=excluded.member_site_ids,
        description=excluded.description, identity_notes=excluded.identity_notes,
        notes=excluded.notes, url=excluded.url, updated_at=excluded.updated_at
    """
    for sn in site_networks:
        row = {**sn}
        row.setdefault("created_at", now)
        row.setdefault("updated_at", now)
        row.setdefault("org_type", "")
        row.setdefault("ownership", "")
        row.setdefault("partner_agencies", "")
        row.setdefault("coordination", "")
        row.setdefault("states_included", "")
        row.setdefault("member_site_ids", "")
        row.setdefault("identity_notes", "")
        _nullify_empty_numerics(row)
        if dry_run:
            print(f"  [DRY-RUN] UPSERT site_network {row['network_id']} — {row['name']}")
        else:
            cur.execute(sql, row)


def upsert_site_network_members(cur, site_networks: List[dict], dry_run: bool) -> None:
    sql = """
    INSERT OR IGNORE INTO site_network_members (network_id, site_id) VALUES (?, ?)
    """
    ct = 0
    for sn in site_networks:
        member_ids = sn.get("member_site_ids", "")
        if not member_ids:
            continue
        for site_id in str(member_ids).split(";"):
            site_id = site_id.strip()
            if site_id:
                if dry_run:
                    print(f"  [DRY-RUN] site_network_members {sn['network_id']} → {site_id}")
                else:
                    cur.execute(sql, (sn["network_id"], site_id))
                ct += 1
    if ct:
        print(f"  site_network_members: {ct} rows")


def upsert_access_points(cur, aps: List[dict], now: str, dry_run: bool) -> None:
    sql = """
    INSERT INTO access_points (
        access_point_id, name, ap_type, status,
        parent_entity_type, parent_entity_id,
        counties, township, municipality, location,
        gps_lat, gps_lon, plus_code, features,
        identity_notes, notes, url_primary,
        last_verified_date, field_verified,
        created_at, updated_at
    ) VALUES (
        :access_point_id, :name, :ap_type, :status,
        :parent_entity_type, :parent_entity_id,
        :counties, :township, :municipality, :location,
        :gps_lat, :gps_lon, :plus_code, :features,
        :identity_notes, :notes, :url_primary,
        :last_verified_date, :field_verified,
        :created_at, :updated_at
    )
    ON CONFLICT(access_point_id) DO UPDATE SET
        name=excluded.name, ap_type=excluded.ap_type, status=excluded.status,
        parent_entity_type=excluded.parent_entity_type,
        parent_entity_id=excluded.parent_entity_id,
        counties=excluded.counties, township=excluded.township,
        municipality=excluded.municipality, location=excluded.location,
        gps_lat=excluded.gps_lat, gps_lon=excluded.gps_lon,
        plus_code=excluded.plus_code, features=excluded.features,
        identity_notes=excluded.identity_notes, notes=excluded.notes,
        url_primary=excluded.url_primary,
        last_verified_date=excluded.last_verified_date,
        field_verified=excluded.field_verified,
        updated_at=excluded.updated_at
    """
    for ap in aps:
        row = {**ap}
        row.setdefault("created_at", now)
        row.setdefault("updated_at", now)
        row.setdefault("township", "")
        row.setdefault("plus_code", "")
        row.setdefault("identity_notes", "")
        row.setdefault("url_primary", "")
        row.setdefault("location", "")
        row.setdefault("municipality", "")
        row.setdefault("counties", "")
        row.setdefault("last_verified_date", "")
        row.setdefault("field_verified", False)
        _nullify_empty_numerics(row)
        if dry_run:
            print(f"  [DRY-RUN] UPSERT AP {row['access_point_id']} — {row['name']}")
        else:
            cur.execute(sql, row)


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
                print(f"  [DRY-RUN] access_point_parents {ap['access_point_id']} → {ptype} {pid}")
            else:
                cur.execute(sql, (ap["access_point_id"], ptype, pid))
            ct += 1
    if ct:
        print(f"  access_point_parents: {ct} rows")


def upsert_held_entities(cur,
                         held_sites, held_trailthings, held_aps,
                         county: str, run_id: str, now: str, dry_run: bool) -> None:
    sql = """
    INSERT OR IGNORE INTO held_entities
        (record_id, entity_type, name, county, hold_reason, hold_detail, run_id, created_at)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """
    rows = (
        [(s["site_id"],           "Site",        s.get("name", ""), s) for s in held_sites] +
        [(tt["trailthing_id"],    "Trailthing",  tt.get("name", ""), tt) for tt in held_trailthings] +
        [(ap["access_point_id"], "Access Point", ap.get("name", ""), ap) for ap in held_aps]
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


def upsert_run_metadata(cur, run_id: str, county: str, state: str,
                        run_date: str, records_input: int,
                        normalized: int, held: int, notes: str,
                        now: str, dry_run: bool) -> None:
    # IMP-101: use exact column names; state must be full name
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


# ── Held entity helpers ──────────────────────────────────────────────────────

def _is_held(rec: dict) -> bool:
    sf = rec.get("status_flag") or ""
    if sf.startswith("HELD"):
        return True
    notes = rec.get("notes") or ""
    return ("HELD" in notes and
            any(r in notes for r in (
                "cross_county_held", "gps_missing", "parent_held",
                "cross_county_candidate", "unconfirmed_baseline_seed")))


def _get_hold_reason(rec: dict):
    hd    = rec.get("hold_detail") or ""
    notes = rec.get("notes") or ""
    for reason in ("cross_county_held", "cross_county_candidate",
                   "parent_held", "gps_missing",
                   "unconfirmed_baseline_seed", "identity_uncertain",
                   "unresolved_parent", "unresolved_member_ids"):
        if reason in hd or reason in notes:
            detail = hd if hd else notes.strip().split("\n")[0]
            return reason, detail[:250]
    return "unknown", (hd or notes[:100])


# ════════════════════════════════════════════════════════════════════════════
#  PIPELINE RUNNER
# ════════════════════════════════════════════════════════════════════════════

class ReviewRequired(Exception):
    """
    Raised by Stage 7.5 when confirm_review=False and dry_run=False.
    TSV files have been written and integrity checks completed but the DB
    has NOT been touched. Re-run with --confirm-review after manual review.
    """


class PipelineRunner:
    """
    Orchestrates Stages 4–8 for a single v6 county pipeline run.

    Parameters
    ----------
    run_id        : str   e.g. "franklin_oh_2026_05_31"
    county        : str   e.g. "Franklin"
    state         : str   e.g. "Ohio"
    run_date      : str   ISO date
    records_input : int   total raw records in discovery YAML
    output_dir    : str   directory for TSV files
    db_path       : str   path to natural_areas_v6.db
    tsv_prefix    : str   filename prefix for TSVs
    county_bbox   : tuple (lat_min, lat_max, lon_min, lon_max)
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
            sites, trailthings, site_networks=None, access_points=None,
            gps_queries: Dict[str, str] = None,
            fallback_gps: Dict[str, Tuple[float, float]] = None,
            fallback_conf: Dict[str, str] = None,
            run_notes: str = "",
            dry_run: bool = False,
            confirm_review: bool = False) -> None:

        site_networks  = site_networks  or []
        access_points  = access_points  or []
        gps_queries    = gps_queries    or {}
        fallback_gps   = fallback_gps   or {}
        fallback_conf  = fallback_conf  or {}

        # ── Filter held entities ──────────────────────────────────────────
        held_sites       = [s  for s  in sites         if _is_held(s)]
        held_trailthings = [tt for tt in trailthings   if _is_held(tt)]
        held_aps         = [ap for ap in access_points if _is_held(ap)]
        sites            = [s  for s  in sites         if not _is_held(s)]
        trailthings      = [tt for tt in trailthings   if not _is_held(tt)]
        site_networks    = [sn for sn in site_networks if not _is_held(sn)]
        access_points    = [ap for ap in access_points if not _is_held(ap)]
        total_held = len(held_sites) + len(held_trailthings) + len(held_aps)

        print("=" * 60)
        print(f"NAP v6 Pipeline  |  {self.county} County, {self.state}  |  {self.run_id}")
        print(f"DB: {self.db_path}")
        print(f"Dry run: {dry_run}")
        if total_held:
            print(f"Held (excluded): {total_held} "
                  f"({len(held_sites)} sites, {len(held_trailthings)} trailthings, "
                  f"{len(held_aps)} APs)")
        print("=" * 60)

        self._stamp_entities(sites, trailthings, site_networks, access_points)

        # ── Stage 4a: GPS Fill-Forward ────────────────────────────────────
        print(f"\n[Stage 4a] GPS Fill-Forward")
        print("  (Fill-forward from prior DB runs handled in normalization stage)")

        # ── Stage 4b: GPS Acquisition ─────────────────────────────────────
        print(f"\n[Stage 4b] GPS Acquisition")
        # Sites: GPS required
        if _REQUESTS_OK:
            acquire_gps(sites, "site_id", gps_queries, fallback_gps, fallback_conf)
        propagate_gps_to_children(sites)
        add_plus_codes(sites)
        add_gis_lookup(sites)
        # APs: GPS required
        if _REQUESTS_OK:
            acquire_gps(access_points, "access_point_id", gps_queries,
                        fallback_gps, fallback_conf)
        propagate_gps_to_aps(access_points, sites)
        add_plus_codes(access_points)
        add_gis_lookup(access_points)
        # Trailthings: no GPS (multi-location entities)
        gps_sites = sum(1 for s in sites if s.get("gps_lat") is not None)
        gps_aps   = sum(1 for ap in access_points if ap.get("gps_lat") is not None)
        print(f"  GPS acquired: {gps_sites}/{len(sites)} sites, "
              f"{gps_aps}/{len(access_points)} APs")

        # ── Stage 4c: GPS Gate ────────────────────────────────────────────
        print(f"\n[Stage 4c] GPS Gate")
        gps_held_sites = [s for s in sites
                          if s.get("gps_lat") is None and not s.get("gps_unresolvable")]
        gps_held_aps   = [ap for ap in access_points
                          if ap.get("gps_lat") is None and not ap.get("gps_unresolvable")]
        for s in gps_held_sites:
            s["hold_reason"] = "gps_missing"
            held_sites.append(s)
            print(f"  HELD (gps_missing): {s['site_id']} — {s.get('name', '')}")
        for ap in gps_held_aps:
            ap["hold_reason"] = "gps_missing"
            held_aps.append(ap)
            print(f"  HELD (gps_missing): {ap['access_point_id']} — {ap.get('name', '')}")
        sites         = [s  for s  in sites         if s.get("gps_lat") is not None or s.get("gps_unresolvable")]
        access_points = [ap for ap in access_points if ap.get("gps_lat") is not None or ap.get("gps_unresolvable")]
        total_held = len(held_sites) + len(held_trailthings) + len(held_aps)
        if gps_held_sites or gps_held_aps:
            print(f"  GPS Gate held: {len(gps_held_sites)} sites, {len(gps_held_aps)} APs")
        else:
            print("  GPS Gate: all entities pass.")

        # ── Stage 6.5: Vocabulary Validation Gate ────────────────────────
        print(f"\n[Stage 6.5] Vocabulary Validation Gate")
        run_vocab_gate(sites, trailthings, access_points)

        # ── Stage 6: TSV Output ───────────────────────────────────────────
        print(f"\n[Stage 6] TSV Output")
        write_all_tsvs(self.output_dir, self.tsv_prefix, self.now,
                       sites, trailthings, site_networks, access_points)

        # ── Stage 7: Integrity Check ──────────────────────────────────────
        print(f"\n[Stage 7] Integrity Check")
        warnings = integrity_check(sites, trailthings, access_points)
        if warnings:
            for w in warnings:
                print(f"  WARNING: {w}")
        else:
            print("  No integrity issues found.")

        # ── Stage 7.5: Human Review Gate ─────────────────────────────────
        print(f"\n[Stage 7.5] Human Review Gate")
        if dry_run:
            print("  Dry run — review gate bypassed.")
        elif confirm_review:
            print("  Review confirmed (--confirm-review). Proceeding to upsert.")
        else:
            print("  ┌─────────────────────────────────────────────────────────┐")
            print("  │  PIPELINE HALTED — REVIEW REQUIRED BEFORE UPSERT       │")
            print("  └─────────────────────────────────────────────────────────┘")
            print(f"  TSV files written to: {self.output_dir}")
            print(f"  Entity counts: {len(sites)} Sites, {len(trailthings)} Trailthings, "
                  f"{len(site_networks)} Site Networks, {len(access_points)} APs")
            print(f"  Held: {total_held} total")
            print()
            print("  Review checklist:")
            print("    1. Entity counts look reasonable for this county")
            print("    2. Category/subtype assignments are substantively correct")
            print("    3. GPS coordinates spot-check — do they land in the right county?")
            print("    4. Held entities are expected — no surprises")
            print("    5. Vocabulary expansion candidates reviewed")
            print()
            print("  To proceed: re-run with --confirm-review")
            raise ReviewRequired(
                f"Stage 7.5: Human review required. "
                f"Re-run with --confirm-review after verifying TSV output."
            )

        # ── Stage 8: Database Upsert ──────────────────────────────────────
        print(f"\n[Stage 8] Database Upsert")
        normalized = (len(sites) + len(trailthings) +
                      len(site_networks) + len(access_points))
        if not run_notes:
            run_notes = (f"{self.county} County {self.state} v6 pipeline complete. "
                         f"{len(sites)} Sites, {len(trailthings)} Trailthings, "
                         f"{len(site_networks)} Site Networks, {len(access_points)} APs.")

        conn = sqlite3.connect(self.db_path)
        try:
            cur = conn.cursor()
            upsert_sites(cur, sites, self.now, dry_run)
            upsert_site_parents(cur, sites, dry_run)
            upsert_trailthings(cur, trailthings, self.now, dry_run)
            upsert_trailthing_hierarchy(cur, trailthings, dry_run)
            upsert_site_networks(cur, site_networks, self.now, dry_run)
            upsert_site_network_members(cur, site_networks, dry_run)
            upsert_access_points(cur, access_points, self.now, dry_run)
            upsert_access_point_parents(cur, access_points, dry_run)
            upsert_held_entities(cur, held_sites, held_trailthings, held_aps,
                                 self.county, self.run_id, self.now, dry_run)
            upsert_run_metadata(cur, self.run_id, self.county, self.state,
                                self.run_date, self.records_input,
                                normalized, total_held, run_notes, self.now, dry_run)
            if not dry_run:
                conn.commit()
                print(f"  Committed to {os.path.basename(self.db_path)}")
        except Exception as e:
            conn.rollback()
            print(f"  ERROR during upsert: {e}", file=sys.stderr)
            raise
        finally:
            conn.close()

        # ── Summary ───────────────────────────────────────────────────────
        print("\n" + "=" * 60)
        print("PIPELINE COMPLETE")
        print(f"  Sites:          {len(sites)}")
        print(f"  Trailthings:    {len(trailthings)}")
        print(f"  Site Networks:  {len(site_networks)}")
        print(f"  Access Points:  {len(access_points)}")
        print(f"  Held:           {total_held}")
        missing_gps = [s["site_id"] for s in sites if s.get("gps_lat") is None
                       and not s.get("gps_unresolvable")]
        if missing_gps:
            print(f"  Sites still missing GPS: {', '.join(missing_gps)}")
        print("=" * 60)

    def _stamp_entities(self, *entity_lists):
        now = self.now
        for lst in entity_lists:
            for e in lst:
                e.setdefault("created_at", now)
                e["updated_at"] = now
