"""
Stage 3 — Resolution Engine Pass 1 (Sandusky County)
Applies Phases 0-5 of Resolution Engine v5.5 to the pipeline config.

Resolution decisions:
  Phase 0 — MC bootstrap: NCIT = KNOWN_MC:OH-MC-T-0110 (pre-assigned)
  Phase 1 — Grouping: (entity_type, county_primary)
  Phase 2/3/4 — Identity matching: no merges (all single-record clusters)
  Phase 5 — Parent resolution + cross-county handling
"""

import json, yaml, pathlib

YAML_PATH = pathlib.Path('County_Spreadsheets/Sandusky/sandusky_ohio_raw_discovery.yaml')
CFG_PATH  = pathlib.Path('County_Spreadsheets/Sandusky/sandusky_config.json')
THIS_COUNTY = 'Sandusky'

raw_data = yaml.safe_load(YAML_PATH.read_text(encoding='utf-8'))
cfg      = json.loads(CFG_PATH.read_text(encoding='utf-8'))
records  = raw_data.get('records', [])

# ── helper ──────────────────────────────────────────────────────────────────

def sorted_counties(counties_raw):
    """Return alphabetically sorted, semicolon-delimited county string."""
    return ';'.join(sorted(set(counties_raw)))

def record_for_id(entity_id):
    """Return the raw YAML record that maps to this config entity_id."""
    return _id_to_record.get(entity_id)

# Build entity_id → raw record index by matching order
# na_generate_config assigns IDs sequentially by type, in YAML record order.
s_idx = t_idx = ts_idx = tn_idx = sn_idx = ap_idx = 0
_id_to_record = {}
for rec in records:
    etype = rec['entity_type']
    prefix = 'SAN'
    if etype == 'Site':
        s_idx += 1
        eid = f'{prefix}-S-{s_idx:03d}'
    elif etype == 'Trail':
        t_idx += 1
        eid = f'{prefix}-T-{t_idx:03d}'
    elif etype == 'Trail Segment':
        ts_idx += 1
        eid = f'{prefix}-TS-{ts_idx:03d}'
    elif etype == 'Trail Network':
        tn_idx += 1
        eid = f'{prefix}-TN-{tn_idx:03d}'
    elif etype == 'Site Network':
        sn_idx += 1
        eid = f'{prefix}-SN-{sn_idx:03d}'
    elif etype == 'Access Point':
        ap_idx += 1
        eid = f'{prefix}-AP-{ap_idx:03d}'
    else:
        continue
    _id_to_record[eid] = rec

# ── MC entity mapping (Phase 0) ──────────────────────────────────────────────
# NCIT is KNOWN_MC:OH-MC-T-0110 (pre-assigned from bootstrap check)
MC_TRAIL_MAP = {
    'SAN-T-001': 'OH-MC-T-0110',  # North Coast Inland Trail
}

# ── Manual review queue entities ────────────────────────────────────────────
MANUAL_REVIEW = {
    'SAN-S-104': 'GOVERNANCE_UNCERTAIN: River Cliff Golf Course — adjacent to SCPD Don W. Miller Park (1329 Tiffin St); if SCPD-owned reclassify T3. GIS parcel lookup required.',
    'SAN-S-108': 'T4_MISS: County Home Cemetery — county government burial ground staged at T8; verify Sandusky County ownership vs historical association.',
    'SAN-S-109': 'GOVERNANCE_UNKNOWN: Old Fremont Cemetery — governance not confirmed; may be T6 city-managed or historical association.',
    'SAN-S-110': 'T6_MISS_POSSIBLE: Green Springs Cemetery — likely Village of Green Springs-managed; GIS_VERIFY_COUNTY (straddles Sandusky/Seneca).',
    'SAN-S-062': 'ENTITY_UNCONFIRMED: Green Creek Township Cemetery — existence unconfirmed; contact Green Creek Township (3106 Limerick Rd, Clyde OH) to verify.',
}

# ── Apply resolution to sites ────────────────────────────────────────────────
held_sites = []
held_aps   = []

for site in cfg['sites']:
    eid = site['site_id']
    rec = record_for_id(eid)
    if rec is None:
        continue

    # Fix counties field (always alphabetical semicolon-delimited)
    site['counties'] = sorted_counties(rec.get('counties_raw', [THIS_COUNTY]))

    # Phase 0 / cross-county resolution
    cp = rec.get('county_primary', THIS_COUNTY)
    counties_raw = rec.get('counties_raw', [THIS_COUNTY])

    if cp != THIS_COUNTY:
        # Scenario A: partner county not yet run — hold this entity
        site['status_flag'] = 'HELD'
        site['hold_detail']  = (
            f'cross_county_held: county_primary={cp}; '
            f'Scenario A — {cp} County pipeline not yet run. '
            f'Entity will be primary in {cp} County pipeline.'
        )
        held_sites.append(eid)

    elif len(counties_raw) > 1:
        # Sandusky primary but multiple counties — flag as CROSS_COUNTY_CANDIDATE
        other = [c for c in sorted(counties_raw) if c != THIS_COUNTY]
        note = f'CROSS_COUNTY_CANDIDATE: also in {", ".join(other)}. '
        if 'GIS_VERIFY_COUNTY' in rec.get('identity_notes_raw', ''):
            note += 'GIS_VERIFY_COUNTY — parcel county requires GIS lookup.'
        site['status_flag'] = note.strip()

    # Manual review queue
    if eid in MANUAL_REVIEW:
        existing_notes = site.get('notes', '')
        site['notes'] = (existing_notes + ' | ' if existing_notes else '') + f'MANUAL_REVIEW: {MANUAL_REVIEW[eid]}'

    # Sleepy Hollow — closed entity
    if 'Sleepy Hollow' in site.get('name', ''):
        site['status'] = 'Closed'
        site['status_flag'] = 'CLOSED: converted to RV park 2019'

# ── Apply resolution to trails ───────────────────────────────────────────────
held_trails = []

for trail in cfg['trails']:
    eid = trail['trail_id']
    rec = record_for_id(eid)
    if rec is None:
        continue

    trail['counties'] = sorted_counties(rec.get('counties_raw', [THIS_COUNTY]))

    cp = rec.get('county_primary', THIS_COUNTY)

    if eid in MC_TRAIL_MAP:
        mc_id = MC_TRAIL_MAP[eid]
        trail['temp_id']        = mc_id
        trail['identity_notes'] = f'KNOWN_MC:{mc_id} — North Coast Inland Trail spans Erie;Huron;Ottawa;Sandusky. This record upserts as {mc_id}.'
        # NCIT is county_primary=Sandusky; it proceeds through normalization but
        # upserts under OH-MC-T-0110 (MC ID), not SAN-T-001.

# ── Apply resolution to access points ───────────────────────────────────────
for ap in cfg['access_points']:
    eid = ap['access_point_id']
    rec = record_for_id(eid)
    if rec is None:
        continue

    # APs use 'county' (singular) not 'counties'
    ap['county'] = sorted_counties(rec.get('counties_raw', [THIS_COUNTY]))
    cp = rec.get('county_primary', THIS_COUNTY)

    if cp != THIS_COUNTY:
        # APs have no status_flag/hold_detail — store in notes + identity_notes
        ap['notes'] = (ap.get('notes', '') or '') + \
            f' HELD|cross_county_held: county_primary={cp}; Scenario A — {cp} County pipeline not yet run.'
        ap['identity_notes'] = (ap.get('identity_notes', '') or '') + \
            f' HELD — cross_county_held (county_primary={cp}).'
        held_aps.append(eid)

    # NCIT parent APs — parent trail will be OH-MC-T-0110 (not SAN-T-001)
    if 'North Coast Inland Trail' in ap.get('name', ''):
        existing = ap.get('identity_notes', '') or ''
        ap['identity_notes'] = existing + \
            ' Parent trail NCIT upserts as OH-MC-T-0110 (KNOWN_MC). parent_entity_id = OH-MC-T-0110.'
        ap['parent_entity_id'] = 'OH-MC-T-0110'

# ── Add resolution metadata block ────────────────────────────────────────────
cfg['resolution'] = {
    'resolution_run':    'sandusky_ohio_2026_05_20_res1',
    'resolution_engine': 'v5.5',
    'phase0_mc_check': {
        'known_mc_entities': [
            {'provisional_id': 'SAN-T-001', 'mc_id': 'OH-MC-T-0110',
             'name': 'North Coast Inland Trail',
             'scenario': 'C_preassigned',
             'note': 'MC ID pre-assigned during bootstrap; DB was empty at discovery start. Proceeds through Sandusky pipeline and upserts as OH-MC-T-0110.'}
        ]
    },
    'phase1_grouping': {
        'groups': {
            '(Site,Sandusky)': 134,
            '(Site,Ottawa)': 5,
            '(Site,Erie)': 2,
            '(Site,Wyandot)': 1,
            '(Trail,Sandusky)': 4,
            '(Access Point,Sandusky)': 7,
            '(Access Point,Erie)': 2,
        }
    },
    'phase2_3_merge_decisions': {
        'merge_clusters': 0,
        'review_sets': 0,
        'no_merges': True,
        'notes': 'All 155 records are single-record clusters (no duplicates detected across tiers). Woodville Cemetery T5 and T6 verified as distinct entities (different locations, different governance).'
    },
    'phase4_field_merging': {
        'note': 'No multi-record clusters — no field merging required.'
    },
    'phase5_parent_resolution': {
        'trail_parents': [
            {'entity_id': 'SAN-AP-004', 'parent_name_raw': 'North Coast Inland Trail', 'resolved_parent_id': 'OH-MC-T-0110'},
            {'entity_id': 'SAN-AP-005', 'parent_name_raw': 'North Coast Inland Trail', 'resolved_parent_id': 'OH-MC-T-0110'},
        ],
        'site_parents': [
            {'entity_id': 'SAN-T-002', 'parent_site_name_raw': 'White Star Park', 'resolved_parent_id': 'SAN-S-023'},
            {'entity_id': 'SAN-T-004', 'parent_site_name_raw': 'Silver Rock Park', 'resolved_parent_id': 'SAN-S-093'},
        ]
    },
    'held_entities': {
        'cross_county_held': {
            'Ottawa_scenario_A': ['SAN-S-079', 'SAN-S-080', 'SAN-S-081', 'SAN-S-105', 'SAN-S-107'],
            'Erie_scenario_A':   ['SAN-S-003', 'SAN-S-004', 'SAN-AP-002', 'SAN-AP-003'],
            'Wyandot_scenario_A': ['SAN-S-005'],
        },
        'total_held': 10
    },
    'cross_county_candidates_not_held': {
        'Sandusky_primary_multi_county': [
            'SAN-S-072','SAN-S-073','SAN-S-074','SAN-S-075',
            'SAN-S-076','SAN-S-077','SAN-S-078',  # Bellevue parks GIS_VERIFY_COUNTY
            'SAN-S-110',  # Green Springs Cemetery (Sandusky+Seneca)
            'SAN-S-111',  # Reformed Church Cemetery (Sandusky+Huron)
        ],
        'note': 'Sandusky is county_primary — proceed through pipeline; CROSS_COUNTY_CANDIDATE flag set; GIS verification required for Bellevue parks.'
    },
    'manual_review_queue': list(MANUAL_REVIEW.keys()),
    'post_resolution_counts': {
        'total_records': 155,
        'held': 10,
        'active_in_pipeline': 145,
        'active_sites': 134,
        'active_trails': 4,
        'active_access_points': 7,
    }
}

# ── Write updated config ─────────────────────────────────────────────────────
CFG_PATH.write_text(json.dumps(cfg, indent=2, ensure_ascii=False), encoding='utf-8')

print('Stage 3 Resolution Pass 1 complete.')
print(f'  Held sites:    {len(held_sites)} -> {held_sites}')
print(f'  Held APs:      {len(held_aps)} -> {held_aps}')
print(f'  MC trail map:  {MC_TRAIL_MAP}')
print(f'  Manual review: {list(MANUAL_REVIEW.keys())}')
print(f'  Active in pipeline: {cfg["resolution"]["post_resolution_counts"]["active_in_pipeline"]}')
