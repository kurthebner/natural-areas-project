#!/usr/bin/env python3
"""
na_generate_config.py — Natural Areas Project
Scaffold a county pipeline JSON config from a raw discovery YAML file (IMP-090).

PROBLEM: Claude currently builds the per-county pipeline config JSON by hand
during Stage 2, transcribing ~500 lines per county from raw YAML records.
This is slow, error-prone, and mechanically repetitive.

SOLUTION: This script reads the raw discovery YAML, extracts the county header
(county, state, run_id, prefix), assigns sequential entity IDs from the prefix,
lifts name_raw → name in each skeleton record, and writes a blank-normalized
JSON config for Claude to fill in during Stage 2 normalization.

USAGE:
    cd "Natural Areas Project v5"
    python utilities/na_generate_config.py \\
        --yaml "County_Spreadsheets/Van Wert/van_wert_oh_raw_discovery.yaml" \\
        --out  "County_Spreadsheets/Van Wert/van_wert_oh_pipeline_config.json"

    # Dry-run (print to stdout, don't write):
    python utilities/na_generate_config.py \\
        --yaml "County_Spreadsheets/Van Wert/van_wert_oh_raw_discovery.yaml" \\
        --dry-run

OUTPUT:
    A JSON file conforming to na_pipeline_config_template.json schema v1.
    - All normalized fields are blank / null (for Claude to fill in Stage 2).
    - name is pre-populated from name_raw.
    - Entity IDs are assigned: PREFIX-S-001, PREFIX-T-001, PREFIX-AP-001, etc.
    - gps_queries and fallback_gps keys are pre-populated per entity_id with
      empty strings / null so Claude can fill in Nominatim queries.

HEADER DETECTION:
    The script looks for a YAML record with entity_type == "county_header" or
    a record that has fields: county, state, prefix.  If no header record is
    found, county/state/prefix must be supplied via --county, --state, --prefix
    command-line flags.

ENTITY TYPE DETECTION:
    entity_type values recognised (case-insensitive):
        site, trail, trail_segment, trail_network, site_network, access_point
    Records with unrecognised entity_type are logged to stderr and skipped.
"""

import argparse
import json
import sys
from pathlib import Path

# IMP-128: Windows console UTF-8 fix — prevents UnicodeEncodeError on → and em dashes
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

try:
    import yaml
except ImportError:
    sys.exit("ERROR: PyYAML is required. Install with: pip install pyyaml --break-system-packages")

# ---------------------------------------------------------------------------
# Entity type → (list_key, id_prefix, id_field)
# ---------------------------------------------------------------------------
_ENTITY_META = {
    'site':           ('sites',          'S',  'site_id'),
    'trail':          ('trails',         'T',  'trail_id'),
    'trail_segment':  ('trail_segments', 'TS', 'trail_segment_id'),
    'trail_network':  ('trail_networks', 'TN', 'trail_network_id'),
    'site_network':   ('site_networks',  'SN', 'site_network_id'),
    'access_point':   ('access_points',  'AP', 'access_point_id'),
}

# Aliases: discovery YAMLs sometimes use spaces or alternate spellings
_ENTITY_TYPE_ALIASES = {
    'access point':  'access_point',
    'trail segment': 'trail_segment',
    'trail network': 'trail_network',
    'site network':  'site_network',
}

# ---------------------------------------------------------------------------
# Blank skeleton builders — all normalized fields null/"" for Claude to fill
# ---------------------------------------------------------------------------

def _site_skeleton(entity_id: str, county: str, name: str) -> dict:
    return {
        "site_id":          entity_id,
        "name":             name,
        "category":         "",
        "subtype":          "",
        "designation":      "",
        "status":           "Active",
        "ownership":        "",
        "governance":       "",
        "partner_agencies": "",
        "coordination":     "",
        "description":      "",
        "location":         "",
        "acres":            None,
        "counties":         county,
        "township":         "",
        "municipality":     "",
        "address":          "",
        "gps_lat":          None,
        "gps_lon":          None,
        "gps_confidence":   "NONE",
        "features_raw":     "",
        "features":         "",
        "access":           "Public",
        "hours":            "",
        "url_primary":      "",
        "url_secondary":    "",
        "parent_site_id":   "",
        "child_site_ids":   "",
        "trail_ids":        "",
        "identity_notes":   "",
        "notes":            "",
        "status_flag":      "",
        "hold_detail":      "",
        "temp_id":          "",
    }


def _trail_skeleton(entity_id: str, county: str, name: str) -> dict:
    return {
        "trail_id":         entity_id,
        "name":             name,
        "use_type":         "",
        "surface":          "",
        "difficulty":       "",
        "origin":           "",
        "status":           "Active",
        "length_mi":        None,
        "ownership":        "",
        "governance":       "",
        "counties":         county,
        "township":         "",
        "municipality":     "",
        "parent_site_id":   "",
        "network_ids":      "",
        "segment_ids":      "",
        "gps_lat":          None,
        "gps_lon":          None,
        "gps_confidence":   "NONE",
        "description":      "",
        "url_primary":      "",
        "identity_notes":   "",
        "notes":            "",
        "status_flag":      "",
        "hold_detail":      "",
        "temp_id":          "",
    }


def _trail_segment_skeleton(entity_id: str, county: str, name: str) -> dict:
    return {
        "trail_segment_id": entity_id,
        "name":             name,
        "parent_trail_id":  "",
        "surface":          "",
        "difficulty":       "",
        "length_mi":        None,
        "counties":         county,
        "township":         "",
        "municipality":     "",
        "gps_lat":          None,
        "gps_lon":          None,
        "gps_confidence":   "NONE",
        "description":      "",
        "identity_notes":   "",
        "notes":            "",
        "temp_id":          "",
    }


def _trail_network_skeleton(entity_id: str, county: str, name: str) -> dict:
    return {
        "trail_network_id":   entity_id,
        "name":               name,
        "network_type":       "",
        "status":             "Active",
        "governance":         "",
        "counties":           county,
        "member_trail_ids":   "",
        "description":        "",
        "url_primary":        "",
        "identity_notes":     "",
        "notes":              "",
        "temp_id":            "",
    }


def _site_network_skeleton(entity_id: str, county: str, name: str) -> dict:
    return {
        "site_network_id":  entity_id,
        "name":             name,
        "network_type":     "",
        "status":           "Active",
        "governance":       "",
        "counties":         county,
        "member_site_ids":  "",
        "description":      "",
        "url_primary":      "",
        "identity_notes":   "",
        "notes":            "",
        "temp_id":          "",
    }


def _access_point_skeleton(entity_id: str, county: str, name: str) -> dict:
    return {
        "access_point_id":    entity_id,
        "name":               name,
        "ap_type":            "",
        "status":             "Active",
        "parent_entity_type": "Site",
        "parent_entity_id":   "",
        "county":             county,
        "township":           "",
        "municipality":       "",
        "address":            "",
        "gps_lat":            None,
        "gps_lon":            None,
        "gps_confidence":     "NONE",
        "features":           "",
        "identity_notes":     "",
        "notes":              "",
        "url_primary":        "",
        "temp_id":            "",
    }


_SKELETON_BUILDERS = {
    'site':          _site_skeleton,
    'trail':         _trail_skeleton,
    'trail_segment': _trail_segment_skeleton,
    'trail_network': _trail_network_skeleton,
    'site_network':  _site_network_skeleton,
    'access_point':  _access_point_skeleton,
}

# ---------------------------------------------------------------------------
# YAML loading helpers
# ---------------------------------------------------------------------------

def _load_records(yaml_path: Path) -> list[dict]:
    """
    Load all entity records from a raw discovery YAML, applying the IMP-089 pre-processor.

    Handles two structural formats:
      1. Multi-document YAML (one entity per document, separated by ---):
            ---
            entity_type: site
            name_raw: Elm Park
            ...

      2. Single-document YAML with a top-level 'records:' list (current standard):
            records:
              - entity_type: site
                name_raw: Elm Park
            tier_5_entity_type_results:
              ...

    In format 2, only the 'records:' list is returned; any tier_N_entity_type_results
    keys are skipped (they contain null-evidence blocks, not entity records).
    """
    # Import the pre-processor if available alongside this script
    try:
        from utilities.na_yaml_preprocess import preprocess_yaml_text
    except ImportError:
        try:
            sys.path.insert(0, str(yaml_path.parent.parent / 'utilities'))
            from na_yaml_preprocess import preprocess_yaml_text
        except ImportError:
            preprocess_yaml_text = lambda t: t   # noqa: E731 — fall back to raw parse

    raw_text   = yaml_path.read_text(encoding='utf-8')
    clean_text = preprocess_yaml_text(raw_text)
    docs       = [d for d in yaml.safe_load_all(clean_text) if d is not None]

    if not docs:
        return []

    # Format 2: single doc with 'records:' key
    if len(docs) == 1 and isinstance(docs[0], dict) and 'records' in docs[0]:
        raw_records = docs[0]['records']
        return [r for r in (raw_records or []) if isinstance(r, dict)]

    # Format 1: each doc is an entity record
    return [d for d in docs if isinstance(d, dict)]


def _extract_header(records: list[dict], args: argparse.Namespace) -> dict:
    """
    Extract county header from records or command-line args.

    Header record has entity_type == 'county_header' OR contains 'county' + 'prefix'.
    Falls back to --county / --state / --prefix flags if no header record is found.
    """
    header = {}
    for rec in records:
        et = str(rec.get('entity_type', '')).lower()
        if et == 'county_header' or ('county' in rec and 'prefix' in rec):
            header = rec
            break

    county  = getattr(args, 'county',  None) or header.get('county',  '')
    state   = getattr(args, 'state',   None) or header.get('state',   'Ohio')
    prefix  = getattr(args, 'prefix',  None) or header.get('prefix',  '')
    run_id  = getattr(args, 'run_id',  None) or header.get('run_id',  '')
    run_date = header.get('run_date', '')
    bbox    = header.get('bbox', [0.0, 0.0, 0.0, 0.0])

    if not county:
        sys.exit("ERROR: county not found in YAML and --county not supplied.")
    if not prefix:
        sys.exit("ERROR: prefix not found in YAML and --prefix not supplied.")
    if not run_id:
        # Derive from county + state
        run_id = f"{county.lower().replace(' ', '_')}_{state.lower().replace(' ', '_')}_YYYY_MM_DD"

    return {
        'county':   county,
        'state':    state,
        'prefix':   prefix.upper(),
        'run_id':   run_id,
        'run_date': run_date,
        'bbox':     bbox,
    }


# ---------------------------------------------------------------------------
# Main scaffold logic
# ---------------------------------------------------------------------------

def generate_config(yaml_path: Path, args: argparse.Namespace) -> dict:
    """Read raw YAML and return a pipeline config dict."""
    records = _load_records(yaml_path)
    hdr     = _extract_header(records, args)

    county = hdr['county']
    prefix = hdr['prefix']

    # Counters per entity type
    counters: dict[str, int] = {k: 0 for k in _ENTITY_META}

    # Accumulated entity lists and GPS dicts
    entity_lists: dict[str, list] = {meta[0]: [] for meta in _ENTITY_META.values()}
    gps_queries:  dict[str, str]  = {}
    fallback_gps: dict[str, list] = {}

    skipped = 0
    for rec in records:
        et = str(rec.get('entity_type', '')).lower().strip()
        et = _ENTITY_TYPE_ALIASES.get(et, et)   # normalise space-variants

        # Skip header records and unrecognised types
        if et in ('county_header', '') or et not in _ENTITY_META:
            if et not in ('county_header', ''):
                print(f"  WARNING: skipping record with unrecognised entity_type={et!r}",
                      file=sys.stderr)
                skipped += 1
            continue

        list_key, id_code, _id_field = _ENTITY_META[et]
        counters[et] += 1
        entity_id = f"{prefix}-{id_code}-{counters[et]:03d}"

        # Lift name_raw → name
        name = str(rec.get('name_raw') or rec.get('name') or '').strip()

        # Build skeleton
        skeleton = _SKELETON_BUILDERS[et](entity_id, county, name)

        # Carry over any raw fields that are safe/informative for the skeleton
        for raw_field in ('features_raw', 'governance_raw', 'url_primary',
                          'address_raw', 'acres_raw', 'notes_raw'):
            if raw_field in rec and raw_field in skeleton:
                skeleton[raw_field] = str(rec[raw_field])

        entity_lists[list_key].append(skeleton)

        # Pre-populate GPS query slots (Claude fills in the actual query)
        gps_queries[entity_id]  = ""
        fallback_gps[entity_id] = None

    # Build final config
    config = {
        "_schema":       "na_pipeline_config_v1",
        "_generated_by": "na_generate_config.py",
        "_note": (
            "All normalized fields are blank — fill in during Stage 2 normalization. "
            "name is pre-populated from name_raw. "
            "gps_queries: fill in Nominatim query string per entity_id. "
            "fallback_gps: fill in [lat, lon] for entities with known coordinates."
        ),
        "county":        hdr['county'],
        "state":         hdr['state'],
        "run_id":        hdr['run_id'],
        "run_date":      hdr['run_date'],
        "prefix":        hdr['prefix'],
        "records_input": sum(counters.values()),
        "bbox":          hdr['bbox'],
        "run_notes":     "",
        "gps_queries":   gps_queries,
        "fallback_gps":  {k: v for k, v in fallback_gps.items() if v is not None},
        "fallback_conf": {},
    }

    # Append entity lists in canonical order
    for et_key in ('site', 'trail', 'trail_segment', 'trail_network',
                   'site_network', 'access_point'):
        list_key = _ENTITY_META[et_key][0]
        config[list_key] = entity_lists[list_key]

    # Summary
    print(f"Scaffolded {hdr['county']} ({hdr['prefix']}) — {config['records_input']} entities:")
    for et_key, (list_key, id_code, _) in _ENTITY_META.items():
        n = len(entity_lists[list_key])
        if n:
            print(f"  {n:3d} {list_key}")
    if skipped:
        print(f"  {skipped} records skipped (unrecognised entity_type)")

    return config


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Scaffold a county pipeline JSON config from raw discovery YAML (IMP-090)."
    )
    parser.add_argument('--yaml', required=True,
                        help="Path to raw discovery YAML file")
    parser.add_argument('--out',
                        help="Output JSON path (default: same dir as YAML, "
                             "{county}_{state}_pipeline_config.json)")
    parser.add_argument('--dry-run', action='store_true',
                        help="Print JSON to stdout without writing a file")
    # Override flags (used when YAML has no county_header record)
    parser.add_argument('--county',  help="County name (override)")
    parser.add_argument('--state',   default='Ohio', help="State (default: Ohio)")
    parser.add_argument('--prefix',  help="Entity ID prefix, e.g. VNW (override)")
    parser.add_argument('--run-id',  help="Run ID (override)")
    args = parser.parse_args()

    yaml_path = Path(args.yaml)
    if not yaml_path.exists():
        sys.exit(f"ERROR: YAML file not found: {yaml_path}")

    config = generate_config(yaml_path, args)

    if args.dry_run:
        print(json.dumps(config, indent=2, ensure_ascii=False))
        return

    # Determine output path
    if args.out:
        out_path = Path(args.out)
    else:
        county_slug = config['county'].lower().replace(' ', '_')
        state_slug  = config['state'].lower().replace(' ', '_')
        out_path    = yaml_path.parent / f"{county_slug}_{state_slug}_pipeline_config.json"

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(
        json.dumps(config, indent=2, ensure_ascii=False),
        encoding='utf-8'
    )
    print(f"Config written: {out_path}")


if __name__ == '__main__':
    main()
