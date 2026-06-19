import yaml, pathlib

f = pathlib.Path('County_Spreadsheets/Sandusky/sandusky_ohio_raw_discovery.yaml')
data = yaml.safe_load(f.read_text(encoding='utf-8'))
data.setdefault('records', [])

# --- Ballville Township Parks ---

data['records'].append({
    'entity_type': 'Site',
    'name_raw': 'Conner Park',
    'counties_raw': ['Sandusky'],
    'county_primary': 'Sandusky',
    'ownership_raw': 'Ballville Township',
    'governance_raw': 'Ballville Township',
    'partner_agencies_raw': None,
    'coordination_raw': None,
    'gps_lat_raw': None,
    'gps_lon_raw': None,
    'location_raw': '2220 Tiffin Road, Fremont, OH 43420',
    'description_raw': (
        'Community recreational park operated by Ballville Township Parks Board. '
        'Hosts community events including Halloween parties and Easter egg hunts.'
    ),
    'features_raw': 'Playground; Ball field; Basketball court; Tennis courts; Volleyball court; Shelter house; Shelter rental',
    'difficulty_raw': None,
    'accessibility_raw': None,
    'urls_raw': ['https://www.ballville.org/conner-park/'],
    'identity_notes_raw': (
        'Ballville Township Park Board-managed community park. Shelter house available for rental.'
    ),
    'township_raw': None,
    'municipality_raw': None,
    'discovery_tier': 5,
    'seeded_from_baseline': False,
    'baseline_id': None
})

data['records'].append({
    'entity_type': 'Site',
    'name_raw': 'Chudzinski-Johannsen Park',
    'counties_raw': ['Sandusky'],
    'county_primary': 'Sandusky',
    'ownership_raw': 'Ballville Township',
    'governance_raw': 'Ballville Township',
    'partner_agencies_raw': None,
    'coordination_raw': None,
    'gps_lat_raw': None,
    'gps_lon_raw': None,
    'location_raw': 'Adjacent to Tindall Bridge, Fremont OH 43420 — Sandusky River waterfront',
    'description_raw': (
        '74.5-acre natural area along the Sandusky River, opened 2018. Features 1,900 feet of '
        'river-edge property and gently rolling terrain with wooded trails. Wildlife including '
        'turkeys and ducks inhabit the grounds. Land came from the Gary and Ruth Chudzinski Trust '
        'through a combination of township purchase, grant funding, and family donation; honors '
        'Kathryn H. Chudzinski and Marie T. Johannsen. Master plan for the park to be developed '
        'by Ballville Township Park Board.'
    ),
    'features_raw': 'Wooded trails; River access; Wildlife viewing; Sandusky River waterfront',
    'difficulty_raw': None,
    'accessibility_raw': None,
    'urls_raw': [
        'https://www.ballville.org/chudzinski-johannsen-park/',
        'https://www.ballville.org/2020/06/27/chudzinski-johannsen-conservacy-park-walking-paths-open/'
    ],
    'identity_notes_raw': (
        'Ballville Township largest natural park; newest (2018). Sandusky River waterfront. '
        'Long-term master plan pending. Sometimes referred to as Conservancy Park in early coverage.'
    ),
    'township_raw': None,
    'municipality_raw': None,
    'discovery_tier': 5,
    'seeded_from_baseline': False,
    'baseline_id': None
})

data['records'].append({
    'entity_type': 'Site',
    'name_raw': 'Hydraulic Square',
    'counties_raw': ['Sandusky'],
    'county_primary': 'Sandusky',
    'ownership_raw': 'Ballville Township',
    'governance_raw': 'Ballville Township',
    'partner_agencies_raw': None,
    'coordination_raw': None,
    'gps_lat_raw': None,
    'gps_lon_raw': None,
    'location_raw': 'Fremont, OH 43420 (Ballville Township)',
    'description_raw': None,
    'features_raw': None,
    'difficulty_raw': None,
    'accessibility_raw': None,
    'urls_raw': ['https://www.ballville.org/hydraulic-square/'],
    'identity_notes_raw': (
        'MINIMAL_DATA — listed as a township park on Ballville Township website alongside '
        'Conner Park and Chudzinski-Johannsen Park. No description, acreage, or address '
        'available from web sources. Physical character and features require field verification. '
        'May be a small historic public square or plaza.'
    ),
    'township_raw': None,
    'municipality_raw': None,
    'discovery_tier': 5,
    'seeded_from_baseline': False,
    'baseline_id': None
})

# --- Sandusky Township Community Park ---

data['records'].append({
    'entity_type': 'Site',
    'name_raw': 'Sandusky Township Park',
    'counties_raw': ['Sandusky'],
    'county_primary': 'Sandusky',
    'ownership_raw': 'Sandusky Township',
    'governance_raw': 'Sandusky Township',
    'partner_agencies_raw': None,
    'coordination_raw': None,
    'gps_lat_raw': None,
    'gps_lon_raw': None,
    'location_raw': 'Along Oak Harbor Road and Thomas Drive, Fremont OH 43420 area (Sandusky Township)',
    'description_raw': (
        'Approximately 11-acre township park in early development. Signed with "Sandusky Township '
        'Park" sign. Rolling terrain precludes traditional sports fields. A seven-member Parks '
        'Committee is in preliminary planning stages for amenity development. Park designated '
        'as public space with tree sponsorship program.'
    ),
    'features_raw': None,
    'difficulty_raw': None,
    'accessibility_raw': None,
    'urls_raw': ['https://www.sanduskytownship.com/park'],
    'identity_notes_raw': (
        'Township park in early development; Parks Committee appointed. Named on signage; '
        'identity-bearing per §4.8. Features not yet installed at time of discovery. '
        'PLANNED — amenities pending Parks Committee development plan.'
    ),
    'township_raw': None,
    'municipality_raw': None,
    'discovery_tier': 5,
    'seeded_from_baseline': False,
    'baseline_id': None
})

f.write_text(yaml.dump(data, allow_unicode=True, sort_keys=False), encoding='utf-8')
print(f'T5 parks staged. Total records: {len(data["records"])}')
