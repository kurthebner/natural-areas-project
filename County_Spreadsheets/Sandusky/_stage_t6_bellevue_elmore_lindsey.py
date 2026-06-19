import yaml, pathlib

f = pathlib.Path('County_Spreadsheets/Sandusky/sandusky_ohio_raw_discovery.yaml')
data = yaml.safe_load(f.read_text(encoding='utf-8'))
data.setdefault('records', [])

# --- Bellevue City Parks (7 Sites — cross-county: Erie/Huron/Sandusky/Seneca) ---
# All parks require GIS_VERIFY_COUNTY to determine which fall in Sandusky County portion.
# Bellevue Cemetery confirmed in Huron County (Lyme Township) — not staged here.

bellevue_parks = [
    (
        'Magdalyn Aigler Recreation Complex',
        '110 Cherry Boulevard, Bellevue, OH 44811',
        'Athletic fields, shelter house, pond, playground, and skateboard park.',
        'Athletic fields; Shelter house; Pond; Playground; Skate park',
    ),
    (
        'Amsden Park',
        'Amsden Street, Bellevue, OH 44811',
        'Neighborhood park with playground.',
        'Playground',
    ),
    (
        'Buckingham Park',
        'Buckingham Drive, Bellevue, OH 44811',
        'Neighborhood park with playground, basketball court, and baseball field.',
        'Playground; Basketball court; Baseball field',
    ),
    (
        'Ellis Park',
        'Ellis Avenue, Bellevue, OH 44811',
        'Neighborhood park with playground.',
        'Playground',
    ),
    (
        'Kern Street Park',
        'Kern Street, Bellevue, OH 44811',
        'Neighborhood park with playground.',
        'Playground',
    ),
    (
        'Ridge Park',
        'Ridge Drive, Bellevue, OH 44811',
        'Neighborhood park with playground.',
        'Playground',
    ),
    (
        'Robert Peters Athletic Field',
        'Greenwood Heights, Bellevue, OH 44811',
        (
            'Athletic park with shelter house, playground, tennis courts, basketball courts, and '
            'ball fields. Includes the Bellevue Community Bark Park (dog park).'
        ),
        'Shelter house; Playground; Tennis courts; Basketball courts; Ball fields; Dog park',
    ),
]

for name, addr, desc, feats in bellevue_parks:
    data['records'].append({
        'entity_type': 'Site',
        'name_raw': name,
        'counties_raw': ['Sandusky', 'Huron', 'Erie', 'Seneca'],
        'county_primary': 'Sandusky',
        'ownership_raw': 'City of Bellevue',
        'governance_raw': 'City of Bellevue',
        'partner_agencies_raw': None,
        'coordination_raw': None,
        'gps_lat_raw': None,
        'gps_lon_raw': None,
        'location_raw': addr,
        'description_raw': desc,
        'features_raw': feats,
        'difficulty_raw': None,
        'accessibility_raw': None,
        'urls_raw': ['https://www.bellevuerec.com/parks'],
        'identity_notes_raw': (
            'City of Bellevue municipal park per bellevuerec.com/parks. '
            'GIS_VERIFY_COUNTY — Bellevue straddles Erie, Huron, Sandusky, and Seneca counties. '
            'Street address alone does not confirm which county this parcel falls in. '
            'GIS parcel lookup required to assign final county_primary.'
        ),
        'township_raw': None,
        'municipality_raw': None,
        'discovery_tier': 6,
        'seeded_from_baseline': False,
        'baseline_id': None,
    })

# --- Elmore Village Parks (3 Sites — cross-county: Ottawa/Sandusky) ---
# Elmore village straddles Ottawa and Sandusky counties.
# All three parks require GIS_VERIFY_COUNTY.

elmore_parks = [
    ('Walter Ory Park', 'Elmore, OH 43416'),
    ('Well Park', 'Elmore, OH 43416'),
    ('Witty Park', 'Elmore, OH 43416'),
]

for name, addr in elmore_parks:
    data['records'].append({
        'entity_type': 'Site',
        'name_raw': name,
        'counties_raw': ['Ottawa', 'Sandusky'],
        'county_primary': 'Ottawa',
        'ownership_raw': 'Village of Elmore',
        'governance_raw': 'Village of Elmore',
        'partner_agencies_raw': None,
        'coordination_raw': None,
        'gps_lat_raw': None,
        'gps_lon_raw': None,
        'location_raw': addr,
        'description_raw': None,
        'features_raw': None,
        'difficulty_raw': None,
        'accessibility_raw': None,
        'urls_raw': [],
        'identity_notes_raw': (
            'Village of Elmore municipal park. GIS_VERIFY_COUNTY — Elmore straddles Ottawa and '
            'Sandusky counties. Street-level address insufficient to assign county. '
            'GIS parcel lookup required; county_primary set to Ottawa pending verification. '
            'MINIMAL_DATA — no address or feature details found in web sources.'
        ),
        'township_raw': None,
        'municipality_raw': None,
        'discovery_tier': 6,
        'seeded_from_baseline': False,
        'baseline_id': None,
    })

# --- Lindsey Village Park (1 Site) ---

data['records'].append({
    'entity_type': 'Site',
    'name_raw': 'Wendelle Miller Park',
    'counties_raw': ['Sandusky'],
    'county_primary': 'Sandusky',
    'ownership_raw': 'Village of Lindsey',
    'governance_raw': 'Village of Lindsey',
    'partner_agencies_raw': None,
    'coordination_raw': None,
    'gps_lat_raw': None,
    'gps_lon_raw': None,
    'location_raw': '240 S. Main Street, Lindsey, OH 43442',
    'description_raw': (
        'Village of Lindsey municipal park at 240 S. Main Street. '
        'Located adjacent to the North Coast Inland Trail (KNOWN_MC:OH-MC-T-0110), '
        'providing a trail access and rest point for NCIT users.'
    ),
    'features_raw': 'NCIT access; Park amenities (details unconfirmed)',
    'difficulty_raw': None,
    'accessibility_raw': None,
    'urls_raw': [],
    'identity_notes_raw': (
        'Village of Lindsey municipal park. Baseline seed. '
        'Located at NCIT (KNOWN_MC:OH-MC-T-0110) trailhead/access point in Lindsey. '
        'MINIMAL_DATA — no village website found; amenity details unconfirmed from web sources.'
    ),
    'township_raw': None,
    'municipality_raw': None,
    'discovery_tier': 6,
    'seeded_from_baseline': True,
    'baseline_id': 'Wendelle Miller Park',
})

f.write_text(yaml.dump(data, allow_unicode=True, sort_keys=False), encoding='utf-8')
print(f'T6 Bellevue/Elmore/Lindsey staged. Total records: {len(data["records"])}')
