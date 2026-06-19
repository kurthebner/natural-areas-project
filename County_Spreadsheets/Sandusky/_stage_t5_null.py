import yaml, pathlib

f = pathlib.Path('County_Spreadsheets/Sandusky/sandusky_ohio_raw_discovery.yaml')
data = yaml.safe_load(f.read_text(encoding='utf-8'))
data.setdefault('tier5_null_evidence', [])
data.setdefault('records', [])

# Green Creek Township — cemetery name unknown; stage as a NEEDS_VERIFICATION record
data['records'].append({
    'entity_type': 'Site',
    'name_raw': 'Green Creek Township Cemetery (unconfirmed)',
    'counties_raw': ['Sandusky'],
    'county_primary': 'Sandusky',
    'ownership_raw': 'Green Creek Township',
    'governance_raw': 'Green Creek Township',
    'partner_agencies_raw': None,
    'coordination_raw': None,
    'gps_lat_raw': None,
    'gps_lon_raw': None,
    'location_raw': 'Green Creek Township, Sandusky County OH (Clyde area)',
    'description_raw': None,
    'features_raw': None,
    'difficulty_raw': None,
    'accessibility_raw': None,
    'urls_raw': ['https://sites.google.com/site/greencreektownship/'],
    'identity_notes_raw': (
        'NEEDS_VERIFICATION — Green Creek Township website has a "Cemetery Fees" page, '
        'indicating the township manages at least one cemetery. Name and location cannot be '
        'confirmed from web sources. Note: "Green Creek Burial Ground" is in Riley Township, '
        'not Green Creek Township. Contact Green Creek Township at 3106 Limerick Rd, Clyde OH '
        'to confirm name and address of township-managed cemetery/cemeteries.'
    ),
    'township_raw': None,
    'municipality_raw': None,
    'discovery_tier': 5,
    'seeded_from_baseline': False,
    'baseline_id': None
})

# T5 Null Evidence — entity types with no records across all 12 townships

data['tier5_null_evidence'].append({
    'tier': 5,
    'governance_level': 'All 12 Sandusky County townships — Trails',
    'entity_types_checked': ['Trail', 'Trail Segment'],
    'result': 'null',
    'sources_checked': [
        'Ballville: ballville.org — no named township-managed trails found',
        'Green Creek: greencreektownship Google Sites — no trails found',
        'Jackson: jackson-sandusky.com — no trails found',
        'Madison: no website; no township trails found in searches',
        'Rice: ricetownship.com — no trails found',
        'Riley: rileytownship.org — no trails found',
        'Sandusky: sanduskytownship.com — no trails found',
        'Scott: no website; no township trails found',
        'Townsend: townsendtownship.org — no trails found',
        'Washington: Google Sites — no trails found',
        'Woodville: woodvilletownshipoh.gov — no trails found',
        'York: yorktwp.com — NCIT trailhead (TR 292) is SCPD (T3), not township-managed'
    ],
    'reasoning': (
        'No named township-managed trails or trail segments in any of the 12 Sandusky County '
        'townships. NCIT segments are SCPD (T3). Null.'
    )
})

data['tier5_null_evidence'].append({
    'tier': 5,
    'governance_level': 'All 12 Sandusky County townships — Trail Networks',
    'entity_types_checked': ['Trail Network'],
    'result': 'null',
    'sources_checked': ['No township-managed multi-trail networks found in any Sandusky County township'],
    'reasoning': 'No township-managed Trail Networks. Null.'
})

data['tier5_null_evidence'].append({
    'tier': 5,
    'governance_level': 'All 12 Sandusky County townships — Site Networks',
    'entity_types_checked': ['Site Network'],
    'result': 'null',
    'sources_checked': ['No township-managed multi-site networks found in any Sandusky County township'],
    'reasoning': 'No township-managed Site Networks. Null.'
})

data['tier5_null_evidence'].append({
    'tier': 5,
    'governance_level': 'All 12 Sandusky County townships — Access Points',
    'entity_types_checked': ['Access Point'],
    'result': 'null',
    'sources_checked': ['No township-managed dedicated access points found in any Sandusky County township'],
    'reasoning': 'No township-managed Access Points. Township parks do not publish separate APs. Null.'
})

data['tier5_null_evidence'].append({
    'tier': 5,
    'governance_level': 'Green Creek Township — Parks',
    'entity_types_checked': ['Site'],
    'result': 'null',
    'sources_checked': [
        'greencreektownship Google Sites — no parks or recreation pages in navigation',
        'SCPD Green Creek Township & Reserve (90 ac, CR 195) already staged at T3'
    ],
    'reasoning': (
        'No Green Creek Township-owned parks found. The only natural area in Green Creek Township '
        'is SCPD-managed (staged at T3). Township website has cemetery fees but no park program. Null.'
    )
})

data['tier5_null_evidence'].append({
    'tier': 5,
    'governance_level': 'Jackson, Madison, Rice, Riley, Scott, Townsend, Washington, Woodville, York townships — Parks',
    'entity_types_checked': ['Site (Parks only)'],
    'result': 'null',
    'sources_checked': [
        'Individual township websites and searches for each — no township-owned parks found',
        'Jackson: jackson-sandusky.com — cemetery only',
        'Madison: no website; no parks found in searches',
        'Rice: ricetownship.com — cemeteries only, no parks',
        'Riley: rileytownship.org — cemeteries only, no parks',
        'Scott: no website; no parks found',
        'Townsend: townsendtownship.org — cemeteries only',
        'Washington: Google Sites — cemeteries only',
        'Woodville: woodvilletownshipoh.gov — cemeteries only',
        'York: yorktwp.com — cemeteries only'
    ],
    'reasoning': (
        'Only Ballville Township and Sandusky Township confirmed to have township-owned parks. '
        'All other 10 townships have no parks — they rely on SCPD for recreation. Null.'
    )
})

f.write_text(yaml.dump(data, allow_unicode=True, sort_keys=False), encoding='utf-8')
print(f'T5 null evidence staged. Total records: {len(data["records"])}, T5 null blocks: {len(data["tier5_null_evidence"])}')
