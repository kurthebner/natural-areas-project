import yaml, pathlib

f = pathlib.Path('County_Spreadsheets/Sandusky/sandusky_ohio_raw_discovery.yaml')
data = yaml.safe_load(f.read_text(encoding='utf-8'))
data.setdefault('records', [])

# --- Gibsonburg Village Parks (4 Sites + 1 Trail) ---

# Central Park
data['records'].append({
    'entity_type': 'Site',
    'name_raw': 'Central Park',
    'counties_raw': ['Sandusky'],
    'county_primary': 'Sandusky',
    'ownership_raw': 'Village of Gibsonburg',
    'governance_raw': 'Village of Gibsonburg',
    'partner_agencies_raw': None,
    'coordination_raw': None,
    'gps_lat_raw': None,
    'gps_lon_raw': None,
    'location_raw': 'West Yeasting Street at Gibson Street, Gibsonburg, OH 43431',
    'description_raw': (
        'Village of Gibsonburg municipal park at West Yeasting Street and Gibson Street. '
        'Features baseball and T-ball fields, pickleball court, basketball court, concession stand, '
        'playground equipment, open shelter house, grills, picnic tables and benches, '
        'free public WiFi, and 24/7 camera surveillance.'
    ),
    'features_raw': 'Baseball fields; T-ball field; Pickleball court; Basketball court; Concession stand; Playground; Shelter house; Grills; Picnic tables; WiFi',
    'difficulty_raw': None,
    'accessibility_raw': None,
    'urls_raw': ['https://gibsonburgohio.org/central-park/'],
    'identity_notes_raw': 'Village of Gibsonburg municipal park per gibsonburgohio.org/central-park/',
    'township_raw': None,
    'municipality_raw': None,
    'discovery_tier': 6,
    'seeded_from_baseline': False,
    'baseline_id': None,
})

# Log Yard
data['records'].append({
    'entity_type': 'Site',
    'name_raw': 'Log Yard',
    'counties_raw': ['Sandusky'],
    'county_primary': 'Sandusky',
    'ownership_raw': 'Village of Gibsonburg',
    'governance_raw': 'Village of Gibsonburg',
    'partner_agencies_raw': None,
    'coordination_raw': None,
    'gps_lat_raw': None,
    'gps_lon_raw': None,
    'location_raw': 'West Madison Street (across from Library and Police Station), Gibsonburg, OH 43431',
    'description_raw': (
        'Village of Gibsonburg community gathering space on West Madison Street, '
        'across from the library and police station. Features an electronic community '
        'activity sign, free public WiFi, and 24/7 camera surveillance. '
        'One-way traffic flow (Madison to Yeasting). Actively developed 2021–2024.'
    ),
    'features_raw': 'Electronic sign; WiFi; Gathering space',
    'difficulty_raw': None,
    'accessibility_raw': None,
    'urls_raw': ['https://gibsonburgohio.org/log-yard/'],
    'identity_notes_raw': 'Village of Gibsonburg community space per gibsonburgohio.org/log-yard/. Primarily a community gathering/event space rather than a traditional recreation park.',
    'township_raw': None,
    'municipality_raw': None,
    'discovery_tier': 6,
    'seeded_from_baseline': False,
    'baseline_id': None,
})

# Williams Park
data['records'].append({
    'entity_type': 'Site',
    'name_raw': 'Williams Park',
    'counties_raw': ['Sandusky'],
    'county_primary': 'Sandusky',
    'ownership_raw': 'Village of Gibsonburg',
    'governance_raw': 'Village of Gibsonburg',
    'partner_agencies_raw': None,
    'coordination_raw': None,
    'gps_lat_raw': None,
    'gps_lon_raw': None,
    'location_raw': 'East Stone Street at North Main Street, Gibsonburg, OH 43431',
    'description_raw': (
        'Village of Gibsonburg\'s primary recreation and cultural park. Features five '
        'baseball/softball fields, concession stand, multi-use building, two shelter houses '
        '(one open-air, one enclosed), two natural grass volleyball courts, a man-made quarry '
        'lake with 1/3-mile circumference, lighted water fountain and waterfall in lake, '
        '1/3-mile paved walking path around lake, handicap fishing platform, observation platform, '
        'reflection point, 33 unique sculptures by area artists (8 permanent), two age-appropriate '
        'playgrounds, picnic area with grills, basketball court, butterfly garden with observation area, '
        'bird blind, free public WiFi, and 24/7 camera surveillance. '
        'Houses the Northcoast Veterans Museum and the Williams Park Veterans Memorial '
        '(remembrance wall, plane and tank monuments).'
    ),
    'features_raw': 'Baseball/softball fields (5); Volleyball courts; Fishing platform; Walking path; Playground (2); Basketball court; Shelter houses (2); Concession stand; Fishing; Butterfly garden; Bird blind; Veterans memorial; Sculpture walk; WiFi',
    'difficulty_raw': None,
    'accessibility_raw': None,
    'urls_raw': ['https://gibsonburgohio.org/williams-park/'],
    'identity_notes_raw': 'Village of Gibsonburg municipal park per gibsonburgohio.org/williams-park/. Includes Northcoast Veterans Museum and Williams Park Veterans Memorial.',
    'township_raw': None,
    'municipality_raw': None,
    'discovery_tier': 6,
    'seeded_from_baseline': False,
    'baseline_id': None,
})

# Silver Rock Park (Site — extraterritorial, village-owned)
data['records'].append({
    'entity_type': 'Site',
    'name_raw': 'Silver Rock Park',
    'counties_raw': ['Sandusky'],
    'county_primary': 'Sandusky',
    'ownership_raw': 'Village of Gibsonburg',
    'governance_raw': 'Village of Gibsonburg',
    'partner_agencies_raw': 'ODNR Division of Wildlife',
    'coordination_raw': 'ODNR publishes fishing maps and enforces Ohio watercraft/fishing regulations; Village retains ownership and management',
    'gps_lat_raw': None,
    'gps_lon_raw': None,
    'location_raw': 'Township Road 42, west of Gibsonburg, between State Route 85 and State Route 600, Gibsonburg, OH 43431',
    'description_raw': (
        'Village of Gibsonburg-owned quarry lake park established 2008, located west of the village '
        'limits on Township Road 42. Approximately 173 acres with 4.1 miles of shoreline. '
        'Provides fishing (annual permit required; fish stocked annually), non-gas-powered boating '
        '(permit required; boat dock and launch), picnic area with benches, gravel parking, '
        'winter sled run, and beginner skiing/snowboarding area. No swimming, no camping, '
        'no gas-powered motors. Boating restricted to sunrise–sunset. '
        'ODNR publishes a fishing map for the site but does not manage it.'
    ),
    'features_raw': 'Fishing; Non-motorized boating; Boat dock; Boat launch; Picnic area; Walking trail; Winter sled run; Skiing/snowboarding (beginner); Annual permit required',
    'difficulty_raw': None,
    'accessibility_raw': None,
    'urls_raw': ['https://gibsonburgohio.org/silver-rock-park/'],
    'identity_notes_raw': (
        'Village of Gibsonburg-owned per gibsonburgohio.org/silver-rock-park/ and village municipal '
        'code §941.14 Water Usage Permit (Silverock Park). Located outside village limits '
        '(extraterritorial). ODNR role is regulatory, not managerial. '
        'Also spelled "Silverock Park" in village code. Correct governance: Village of Gibsonburg.'
    ),
    'township_raw': None,
    'municipality_raw': None,
    'discovery_tier': 6,
    'seeded_from_baseline': False,
    'baseline_id': None,
})

# Silver Rock Park Walking Trail (Trail)
data['records'].append({
    'entity_type': 'Trail',
    'name_raw': 'Silver Rock Park Walking Trail',
    'counties_raw': ['Sandusky'],
    'county_primary': 'Sandusky',
    'ownership_raw': 'Village of Gibsonburg',
    'governance_raw': 'Village of Gibsonburg',
    'partner_agencies_raw': None,
    'coordination_raw': None,
    'gps_lat_raw': None,
    'gps_lon_raw': None,
    'location_raw': 'Silver Rock Park, Township Road 42, west of Gibsonburg, OH 43431',
    'description_raw': (
        'Approximately 1-mile walking trail within Silver Rock Park. '
        'Runs along the quarry lake shoreline. Village annual park permit required for access.'
    ),
    'features_raw': None,
    'difficulty_raw': None,
    'accessibility_raw': None,
    'urls_raw': ['https://gibsonburgohio.org/silver-rock-park/'],
    'identity_notes_raw': 'Trail within Silver Rock Park per park description at gibsonburgohio.org/silver-rock-park/. Village of Gibsonburg-managed.',
    'township_raw': None,
    'municipality_raw': None,
    'discovery_tier': 6,
    'seeded_from_baseline': False,
    'baseline_id': None,
})

f.write_text(yaml.dump(data, allow_unicode=True, sort_keys=False), encoding='utf-8')
print(f'T6 Gibsonburg staged. Total records: {len(data["records"])}')
