import yaml, pathlib

f = pathlib.Path('County_Spreadsheets/Sandusky/sandusky_ohio_raw_discovery.yaml')
data = yaml.safe_load(f.read_text(encoding='utf-8'))
data.setdefault('records', [])

# Aldrich Pond Wildlife Area — ODNR per baseline; no web presence confirmed
data['records'].append({
    'entity_type': 'Site',
    'name_raw': 'Aldrich Pond Wildlife Area',
    'counties_raw': ['Sandusky'],
    'county_primary': 'Sandusky',
    'ownership_raw': 'State of Ohio',
    'governance_raw': 'ODNR Division of Wildlife',
    'partner_agencies_raw': None,
    'coordination_raw': None,
    'gps_lat_raw': None,
    'gps_lon_raw': None,
    'location_raw': None,
    'description_raw': 'State wildlife area in Sandusky County. 39.93 acres. No information on ODNR website per baseline notation.',
    'features_raw': None,
    'difficulty_raw': None,
    'accessibility_raw': None,
    'urls_raw': [],
    'identity_notes_raw': (
        'NEEDS_VERIFICATION - no ODNR web page found; known only from baseline. '
        'Acreage 39.93 ac per baseline. May be a small ODNR tract without a public-facing page. '
        'Verify via ODNR Hunting Area Maps PDF or county auditor parcel records.'
    ),
    'township_raw': None,
    'municipality_raw': None,
    'discovery_tier': 2,
    'seeded_from_baseline': True,
    'baseline_id': 'Aldrich Pond Wildlife Area'
})

# Sandusky County Wildlife Areas 1-7 — staged as a group pending verification
# Baseline lists these as ODNR Public Hunting Areas; individual names/locations unknown
data['records'].append({
    'entity_type': 'Site',
    'name_raw': 'Sandusky County Wildlife Areas (ODNR numbered tracts)',
    'counties_raw': ['Sandusky'],
    'county_primary': 'Sandusky',
    'ownership_raw': 'State of Ohio',
    'governance_raw': 'ODNR Division of Wildlife',
    'partner_agencies_raw': None,
    'coordination_raw': None,
    'gps_lat_raw': None,
    'gps_lon_raw': None,
    'location_raw': None,
    'description_raw': (
        'Baseline lists up to 7 numbered ODNR Public Hunting Areas in Sandusky County '
        '(Sandusky County Wildlife Area 1 through 7). Individual names, locations, and '
        'acreages unknown. May be small ODNR-leased or owned tracts without public-facing pages.'
    ),
    'features_raw': 'Public hunting; Trapping',
    'difficulty_raw': None,
    'accessibility_raw': None,
    'urls_raw': [
        'https://ohiodnr.gov/discover-and-learn/safety-conservation/about-ODNR/wildlife/documents-publications/hunting-area-maps'
    ],
    'identity_notes_raw': (
        'NEEDS_VERIFICATION - baseline lists Sandusky County Wildlife Area 1 through 7; no '
        'individual ODNR pages found. These may be wildlife agreement areas or small leased '
        'tracts. Verify via ODNR Hunting Area Maps PDF (Sandusky County entries). Each '
        'confirmed tract will need its own record at resolution. Staging as a placeholder '
        'group record pending authoritative enumeration.'
    ),
    'township_raw': None,
    'municipality_raw': None,
    'discovery_tier': 2,
    'seeded_from_baseline': True,
    'baseline_id': 'Sandusky County Wildlife Areas 1-7'
})

# T2 null evidence for entity types with no records
data.setdefault('tier2_null_evidence', [])

data['tier2_null_evidence'].append({
    'tier': 2,
    'governance_level': 'ODNR Division of Forestry',
    'entity_types_checked': ['Site', 'Trail', 'Trail Segment', 'Trail Network', 'Site Network', 'Access Point'],
    'result': 'null',
    'sources_checked': ['ODNR property listings — no state forests listed in Sandusky County'],
    'reasoning': 'No state forest units in Sandusky County identified. Null confirmed.'
})

data['tier2_null_evidence'].append({
    'tier': 2,
    'governance_level': 'ODNR Division of Natural Areas & Preserves (DNAP)',
    'entity_types_checked': ['Site'],
    'result': 'null',
    'sources_checked': [
        'Wikipedia list of Ohio State Nature Preserves — no Sandusky County entries',
        'ODNR DNAP search'
    ],
    'reasoning': 'No ODNR State Nature Preserves in Sandusky County. Null confirmed via Wikipedia authoritative list.'
})

data['tier2_null_evidence'].append({
    'tier': 2,
    'governance_level': 'Ohio History Connection (OHC) — non-Spiegel Grove',
    'entity_types_checked': ['Site'],
    'result': 'null',
    'sources_checked': ['OHC site listings — Spiegel Grove is the only OHC property in Sandusky County'],
    'reasoning': 'No additional OHC state memorials, archaeological preserves, or historic landscapes in Sandusky County beyond Spiegel Grove.'
})

data['tier2_null_evidence'].append({
    'tier': 2,
    'governance_level': 'ODOT (scenic overlooks, bikeways, rest areas)',
    'entity_types_checked': ['Site', 'Trail'],
    'result': 'null',
    'sources_checked': [
        'ODOT rest area page review — no ODOT-managed rest areas confirmed in Sandusky County',
        'Note: I-80/90 rest areas are OTIC (Ohio Turnpike), not ODOT'
    ],
    'reasoning': 'No ODOT scenic overlooks, bikeway corridors, or rest areas with recreation features confirmed in Sandusky County.'
})

data['tier2_null_evidence'].append({
    'tier': 2,
    'governance_level': 'Ohio Turnpike Infrastructure Commission (OTIC)',
    'entity_types_checked': ['Site', 'Trail'],
    'result': 'null',
    'sources_checked': [
        'https://www.ohioturnpike.org/travelers/service-plazas — four service plazas in Sandusky County confirmed: Blue Heron (MP 76.9 WB), Wyandot (MP 76.9 EB), Erie Islands (MP 100.0 WB), Commodore Perry (MP 100.0 EB)'
    ],
    'reasoning': (
        'Four OTIC service plazas confirmed in Sandusky County. All are fuel/food/trucker '
        'facilities with no outdoor hiking trails, nature areas, dog walks, or storybook trails. '
        'None meet the threshold for Site or Trail records per T2 sub-procedure 4.5. Null.'
    )
})

data['tier2_null_evidence'].append({
    'tier': 2,
    'governance_level': 'Trails and Trail Networks (state-managed)',
    'entity_types_checked': ['Trail', 'Trail Segment', 'Trail Network'],
    'result': 'null',
    'sources_checked': [
        'Spiegel Grove: no named trail confirmed from authoritative sources (noted in site record)',
        'Pickerel Creek WA: dike network and Old Vickery Road are informal features, no named ODNR trail',
        'Sandusky Scenic River: no ODNR-managed water trail designation found for this reach'
    ],
    'reasoning': (
        'No named state-managed trails, trail segments, or trail networks confirmed from '
        'authoritative ODNR sources in Sandusky County. Informal features at Pickerel Creek WA '
        'noted in site record identity_notes. Trail presence at Spiegel Grove to be verified. Null.'
    )
})

data['tier2_null_evidence'].append({
    'tier': 2,
    'governance_level': 'Site Networks (state-managed)',
    'entity_types_checked': ['Site Network'],
    'result': 'null',
    'sources_checked': ['No multi-site state designation with Site Network identity found in Sandusky County'],
    'reasoning': 'Sandusky State Scenic River is a Site (Water Site), not a Site Network. No other Site Network candidates. Null.'
})

data['tier2_null_evidence'].append({
    'tier': 2,
    'governance_level': 'Ringneck Ridge Wildlife Area (re-tiered)',
    'entity_types_checked': ['Site'],
    'result': 'MOVED_TO_T3',
    'sources_checked': [
        'ODNR pheasant release program data — Ringneck Ridge listed as SCPD-managed, requiring ODNR coordination permit'
    ],
    'reasoning': (
        'Ringneck Ridge Wildlife Area (360 ac, 1818 CR 74, Gibsonburg) is managed by Sandusky '
        'County Park District, not ODNR directly. ODNR releases pheasants there under a special '
        'permit arrangement. This is a Tier 3 (District) entity. Will be discovered and staged at T3.'
    )
})

f.write_text(yaml.dump(data, allow_unicode=True, sort_keys=False), encoding='utf-8')
print(f'Done. Records: {len(data["records"])}, T2 null blocks: {len(data["tier2_null_evidence"])}')
