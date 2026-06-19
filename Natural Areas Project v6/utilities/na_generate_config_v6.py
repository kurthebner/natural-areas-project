#!/usr/bin/env python3
"""
na_generate_config_v6.py — Natural Areas Project Config Generator (v6)
v2.0  |  2026-05-31

v6 changes from v1.0:
  - Four entity types: site, trailthing, site_network, access_point
  - trail / trail_segment / trail_network entity types removed
  - Trailthing entity type alias handles: trailthing, trail, trail_segment,
    trail_network (graceful migration — v5 discovery YAMLs still seed correctly)
  - Trailthing skeleton includes: source_term, source_hierarchy_context,
    parent_id, site_parent_id, parent_site_network_id
  - Site skeleton includes new v6 fields: habitat_type, access_notes,
    last_verified_date, field_verified
  - Access Point skeleton: parent_trailthings_raw, last_verified_date,
    field_verified; county → counties
  - Entity ID code: TT for new Trailthing entities (T/TS/TN for migrated records)
  - Config key: trailthings (replaces trails / trail_segments / trail_networks)

USAGE:
    cd "Natural Areas Project v6"

    python utilities/na_generate_config_v6.py \\
        --yaml "County_Spreadsheets/Franklin/franklin_oh_raw_discovery.yaml" \\
        --out  "County_Spreadsheets/Franklin/franklin_oh_pipeline_config.json"

    python utilities/na_generate_config_v6.py \\
        --yaml "County_Spreadsheets/Franklin/franklin_oh_raw_discovery.yaml" \\
        --dry-run

OUTPUT:
    A JSON file conforming to the v6 pipeline config schema.
    - All normalized fields are blank/null for Claude to fill in during normalization.
    - name is pre-populated from name_raw.
    - Entity IDs assigned: OH-PREFIX-S-001, OH-PREFIX-TT-001, OH-PREFIX-AP-001.
    - gps_queries and fallback_gps keys pre-populated per entity_id.
"""

import argparse
import json
import sys
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

try:
    import yaml
except ImportError:
    sys.exit("ERROR: PyYAML is required. Install with: pip install pyyaml")

# ---------------------------------------------------------------------------
# Entity type metadata: (config_list_key, id_code, id_field)
# ---------------------------------------------------------------------------
_ENTITY_META = {
    'site':         ('sites',         'S',  'site_id'),
    'trailthing':   ('trailthings',   'TT', 'trailthing_id'),
    'site_network': ('site_networks', 'SN', 'network_id'),
    'access_point': ('access_points', 'AP', 'access_point_id'),
}

# Aliases: handle v5 entity_type values and space variants gracefully
_ENTITY_TYPE_ALIASES = {
    # Space variants
    'access point':    'access_point',
    'site network':    'site_network',
    # v5 → v6 migration: all trail types seed as Trailthing
    'trail':           'trailthing',
    'trail_segment':   'trailthing',
    'trail_network':   'trailthing',
    'trail segment':   'trailthing',
    'trail network':   'trailthing',
}


# ---------------------------------------------------------------------------
# Skeleton builders
# ---------------------------------------------------------------------------

def _site_skeleton(entity_id: str, county: str, name: str) -> dict:
    return {
        "site_id":             entity_id,
        "name":                name,
        "category":            "",
        "subtype":             "",
        "designation":         "",
        "status":              "Active",
        "ownership":           "",
        "governance":          "",
        "partner_agencies":    "",
        "coordination":        "",
        "description":         "",
        "habitat_type":        "",
        "features_raw":        "",
        "features":            "",
        "access_notes":        "",
        "location":            "",
        "acres":               None,
        "counties":            county,
        "township":            "",
        "municipality":        "",
        "gps_lat":             None,
        "gps_lon":             None,
        "gps_confidence":      "NONE",
        "plus_code":           "",
        "notes":               "",
        "url_primary":         "",
        "urls":                "",
        "last_verified_date":  "",
        "field_verified":      False,
        "parent_site_id":      "",
        "identity_notes":      "",
        "status_flag":         "",
        "hold_detail":         "",
    }


def _trailthing_skeleton(entity_id: str, county: str, name: str) -> dict:
    return {
        "trailthing_id":              entity_id,
        "name":                       name,
        "alternate_names":            "",
        "source_term":                "",
        "source_hierarchy_context":   "",
        "parent_id":                  "",
        "site_parent_id":             "",
        "parent_site_network_id":     "",
        "use_type":                   "",
        "surface_type":               "",
        "origin_type":                "",
        "org_type":                   "",
        "status":                     "",
        "difficulty":                 "",
        "accessibility":              "",
        "ownership":                  "",
        "governance":                 "",
        "partner_agencies":           "",
        "coordination":               "",
        "counties":                   county,
        "states_included":            "",
        "total_length":               None,
        "description":                "",
        "trail_history":              "",
        "identity_notes":             "",
        "notes":                      "",
        "url":                        "",
        "maps":                       "",
        "status_flag":                "",
        "hold_detail":                "",
    }


def _site_network_skeleton(entity_id: str, county: str, name: str) -> dict:
    return {
        "network_id":       entity_id,
        "name":             name,
        "network_type":     "",
        "org_type":         "",
        "status":           "Active",
        "ownership":        "",
        "governance":       "",
        "partner_agencies": "",
        "coordination":     "",
        "counties":         county,
        "states_included":  "",
        "member_count":     None,
        "member_site_ids":  "",
        "description":      "",
        "identity_notes":   "",
        "notes":            "",
        "url":              "",
        "status_flag":      "",
        "hold_detail":      "",
    }


def _access_point_skeleton(entity_id: str, county: str, name: str) -> dict:
    return {
        "access_point_id":    entity_id,
        "name":               name,
        "ap_type":            "",
        "status":             "Active",
        "parent_entity_type": "Site",
        "parent_entity_id":   "",
        "counties":           county,
        "township":           "",
        "municipality":       "",
        "location":           "",
        "gps_lat":            None,
        "gps_lon":            None,
        "gps_confidence":     "NONE",
        "plus_code":          "",
        "features":           "",
        "identity_notes":     "",
        "notes":              "",
        "url_primary":        "",
        "last_verified_date": "",
        "field_verified":     False,
        "status_flag":        "",
        "hold_detail":        "",
    }


_SKELETON_BUILDERS = {
    'site':         _site_skeleton,
    'trailthing':   _trailthing_skeleton,
    'site_network': _site_network_skeleton,
    'access_point': _access_point_skeleton,
}


# ---------------------------------------------------------------------------
# YAML loading helpers
# ---------------------------------------------------------------------------

def _load_records(yaml_path: Path) -> list:
    try:
        script_dir = Path(__file__).parent
        sys.path.insert(0, str(script_dir.resolve()))
        from na_yaml_preprocess import preprocess_yaml_text
    except ImportError:
        preprocess_yaml_text = lambda t: t  # noqa: E731

    raw_text   = yaml_path.read_text(encoding='utf-8')
    clean_text = preprocess_yaml_text(raw_text)
    docs       = [d for d in yaml.safe_load_all(clean_text) if d is not None]

    if not docs:
        return []

    if len(docs) == 1 and isinstance(docs[0], dict) and 'records' in docs[0]:
        raw_records = docs[0]['records']
        return [r for r in (raw_records or []) if isinstance(r, dict)]

    return [d for d in docs if isinstance(d, dict)]


def _extract_header(records: list, args: argparse.Namespace) -> dict:
    header = {}
    for rec in records:
        et = str(rec.get('entity_type', '')).lower()
        if et == 'county_header' or ('county' in rec and 'prefix' in rec):
            header = rec
            break

    county   = getattr(args, 'county',  None) or header.get('county',  '')
    state    = getattr(args, 'state',   None) or header.get('state',   'Ohio')
    prefix   = getattr(args, 'prefix',  None) or header.get('prefix',  '')
    run_id   = getattr(args, 'run_id',  None) or header.get('run_id',  '')
    run_date = header.get('run_date', '')
    bbox     = header.get('bbox', [0.0, 0.0, 0.0, 0.0])

    if not county:
        sys.exit("ERROR: county not found in YAML and --county not supplied.")
    if not prefix:
        sys.exit("ERROR: prefix not found in YAML and --prefix not supplied.")
    if not run_id:
        run_id = (f"{county.lower().replace(' ', '_')}_"
                  f"{state.lower().replace(' ', '_')}_YYYY_MM_DD")

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
    records = _load_records(yaml_path)
    hdr     = _extract_header(records, args)

    county = hdr['county']
    prefix = hdr['prefix']

    counters: dict = {k: 0 for k in _ENTITY_META}
    entity_lists: dict = {meta[0]: [] for meta in _ENTITY_META.values()}
    gps_queries:  dict = {}
    fallback_gps: dict = {}

    skipped = 0
    migrated_trail_types = 0

    for rec in records:
        et = str(rec.get('entity_type', '')).lower().strip()
        original_et = et

        # Apply aliases (including v5 → v6 trail migration)
        et = _ENTITY_TYPE_ALIASES.get(et, et)

        if et in ('county_header', '') or et not in _ENTITY_META:
            if et not in ('county_header', ''):
                print(f"  WARNING: skipping record with unrecognised entity_type={original_et!r}",
                      file=sys.stderr)
                skipped += 1
            continue

        # Track v5 trail type migrations for summary
        if original_et in ('trail', 'trail_segment', 'trail_network',
                            'trail segment', 'trail network'):
            migrated_trail_types += 1

        list_key, id_code, _id_field = _ENTITY_META[et]
        counters[et] += 1
        entity_id = f"OH-{prefix}-{id_code}-{counters[et]:03d}"

        name = str(rec.get('name_raw') or rec.get('name') or '').strip()
        skeleton = _SKELETON_BUILDERS[et](entity_id, county, name)

        # Carry over useful raw fields to the skeleton
        carry_fields = {
            'site':         ('features_raw', 'governance_raw', 'url_primary', 'acres_raw'),
            'trailthing':   ('governance_raw', 'url_primary', 'source_term_raw'),
            'site_network': ('governance_raw', 'url_primary'),
            'access_point': ('governance_raw', 'url_primary'),
        }
        for raw_field in carry_fields.get(et, ()):
            if raw_field in rec:
                # Map to the target skeleton field
                target = raw_field.replace('_raw', '') if raw_field.endswith('_raw') else raw_field
                if target in skeleton:
                    skeleton[target] = str(rec[raw_field])

        # source_term special case for Trailthings seeded from v5 trail records
        if et == 'trailthing' and not skeleton.get('source_term'):
            raw_et = original_et.replace('_', ' ')
            if raw_et in ('trail', 'trail segment', 'trail network'):
                skeleton['source_term'] = raw_et

        entity_lists[list_key].append(skeleton)
        gps_queries[entity_id]  = ""
        fallback_gps[entity_id] = None

    config = {
        "_schema":       "na_pipeline_config_v2",
        "_generated_by": "na_generate_config_v6.py",
        "_note": (
            "v6 config. Four entity types: sites, trailthings, site_networks, access_points. "
            "All normalized fields are blank — fill in during normalization. "
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

    for et_key in ('site', 'trailthing', 'site_network', 'access_point'):
        list_key = _ENTITY_META[et_key][0]
        config[list_key] = entity_lists[list_key]

    print(f"Scaffolded {hdr['county']} ({hdr['prefix']}) — {config['records_input']} entities:")
    for et_key, (list_key, id_code, _) in _ENTITY_META.items():
        n = len(entity_lists[list_key])
        if n:
            print(f"  {n:3d} {list_key}")
    if migrated_trail_types:
        print(f"  ({migrated_trail_types} v5 trail-type records migrated to Trailthings)")
    if skipped:
        print(f"  {skipped} records skipped (unrecognised entity_type)")

    return config


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Scaffold a v6 county pipeline JSON config from raw discovery YAML."
    )
    parser.add_argument('--yaml', required=True,
                        help="Path to raw discovery YAML file")
    parser.add_argument('--out',
                        help="Output JSON path (default: same dir as YAML)")
    parser.add_argument('--dry-run', action='store_true',
                        help="Print JSON to stdout without writing a file")
    parser.add_argument('--county',  help="County name (override)")
    parser.add_argument('--state',   default='Ohio', help="State (default: Ohio)")
    parser.add_argument('--prefix',  help="Entity ID prefix, e.g. FR (override)")
    parser.add_argument('--run-id',  help="Run ID (override)")
    args = parser.parse_args()

    yaml_path = Path(args.yaml)
    if not yaml_path.exists():
        sys.exit(f"ERROR: YAML file not found: {yaml_path}")

    config = generate_config(yaml_path, args)

    if args.dry_run:
        print(json.dumps(config, indent=2, ensure_ascii=False))
        return

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
