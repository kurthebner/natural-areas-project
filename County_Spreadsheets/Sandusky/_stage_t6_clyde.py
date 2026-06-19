import yaml, pathlib

f = pathlib.Path('County_Spreadsheets/Sandusky/sandusky_ohio_raw_discovery.yaml')
data = yaml.safe_load(f.read_text(encoding='utf-8'))
data.setdefault('records', [])

# --- Clyde City Parks (5 Sites) ---

clyde_parks = [
    (
        'Cherry Street Park',
        '135 E. Cherry Street, Clyde, OH 43410',
        'Neighborhood park with basketball courts, children\'s play station, and swings. '
        'Walk-in entrance from East Forest Street; parking on East Cherry Street.',
        'Basketball courts; Playground; Swings',
    ),
    (
        'Community Park',
        '246 South Street, Clyde, OH 43410',
        (
            'City of Clyde\'s largest park. Features baseball/softball diamonds, tennis courts, '
            'volleyball courts, pickleball, fishing pond (Canadian geese and ducks), walking paths, '
            'concession stand, covered bridge, playground, open shelter houses, restrooms, and a dog area. '
            'Wheelchair accessible. Entrances on Race Street, South Street, and Fair Street.'
        ),
        'Baseball/softball diamonds; Tennis courts; Volleyball courts; Fishing pond; Walking paths; Playground; Shelter houses; Restrooms; Concession stand; Covered bridge; Dog park; Wheelchair accessible',
    ),
    (
        'Gus Wolf Park',
        'Vine Street, Clyde, OH 43410',
        (
            'Park along Raccoon Creek with a skate park (opened 2015), basketball hoop, '
            'children\'s play equipment, and large open grassy areas. '
            'Parking at West Maple Street at Vine Street entrance.'
        ),
        'Skate park; Basketball court; Playground; Open green space; Raccoon Creek frontage',
    ),
    (
        'Hendricks Park',
        'South Main Street (at the base of Raccoon Creek Reservoir), Clyde, OH 43410',
        'Neighborhood park at the base of the Raccoon Creek Reservoir with children\'s swings, climbing equipment, and tennis courts.',
        'Playground; Swings; Climbing equipment; Tennis courts',
    ),
    (
        'Paden Park',
        'Mulberry Street at South Street, Clyde, OH 43410',
        'Small neighborhood park; open grassy area.',
        None,
    ),
]

for name, addr, desc, feats in clyde_parks:
    data['records'].append({
        'entity_type': 'Site',
        'name_raw': name,
        'counties_raw': ['Sandusky'],
        'county_primary': 'Sandusky',
        'ownership_raw': 'City of Clyde',
        'governance_raw': 'City of Clyde',
        'partner_agencies_raw': None,
        'coordination_raw': None,
        'gps_lat_raw': None,
        'gps_lon_raw': None,
        'location_raw': addr,
        'description_raw': desc,
        'features_raw': feats,
        'difficulty_raw': None,
        'accessibility_raw': None,
        'urls_raw': ['https://www.clydeohio.org/165/Parks'],
        'identity_notes_raw': 'City of Clyde municipal park per clydeohio.org/165/Parks',
        'township_raw': None,
        'municipality_raw': None,
        'discovery_tier': 6,
        'seeded_from_baseline': False,
        'baseline_id': None,
    })

# --- Raccoon Creek Reservoir (Site) ---
# City of Clyde-owned, 36 acres. ODNR cooperative agreement (ODNR provides fishing regulation
# oversight under Ohio watercraft/fisheries rules; City retains ownership and management).
# Permits required: annual fishing/boating permit. No swimming. No motorized vehicles around perimeter.
# Hours: boating 4 AM – 10 PM.

data['records'].append({
    'entity_type': 'Site',
    'name_raw': 'Raccoon Creek Reservoir',
    'counties_raw': ['Sandusky'],
    'county_primary': 'Sandusky',
    'ownership_raw': 'City of Clyde',
    'governance_raw': 'City of Clyde',
    'partner_agencies_raw': 'ODNR Division of Wildlife',
    'coordination_raw': 'ODNR cooperative agreement for fishing and watercraft regulation',
    'gps_lat_raw': None,
    'gps_lon_raw': None,
    'location_raw': 'South Main Street area, Clyde, OH 43410 (adjacent to Hendricks Park)',
    'description_raw': (
        'City of Clyde-owned reservoir, approximately 36 acres. Located adjacent to Hendricks Park '
        'at the south end of South Main Street. Provides fishing and non-motorized boating; annual '
        'permit required. No swimming; no motorized vehicles around perimeter. Boating permitted '
        '4 AM – 10 PM. Ohio fishing license required in addition to city permit. ODNR cooperative '
        'agreement governs fishing and watercraft rules.'
    ),
    'features_raw': 'Fishing; Non-motorized boating; Boat launch; Annual permit required',
    'difficulty_raw': None,
    'accessibility_raw': None,
    'urls_raw': ['https://www.clydeohio.org/165/Parks'],
    'identity_notes_raw': (
        'City of Clyde-owned reservoir per clydeohio.org parks page. '
        'ODNR role is cooperative/regulatory, not managerial — City of Clyde is the '
        'correct owner/governance for T6. Baseline seed confirmed. '
        'Also referenced as "Raccoon Creek/Beaver Creek Reservoir" on city parks page.'
    ),
    'township_raw': None,
    'municipality_raw': None,
    'discovery_tier': 6,
    'seeded_from_baseline': True,
    'baseline_id': 'Raccoon Creek Reservoir',
})

# --- McPherson Cemetery (Site) ---

data['records'].append({
    'entity_type': 'Site',
    'name_raw': 'McPherson Cemetery',
    'counties_raw': ['Sandusky'],
    'county_primary': 'Sandusky',
    'ownership_raw': 'City of Clyde',
    'governance_raw': 'City of Clyde',
    'partner_agencies_raw': None,
    'coordination_raw': None,
    'gps_lat_raw': None,
    'gps_lon_raw': None,
    'location_raw': '422 E. McPherson Highway (US Route 20), Clyde, OH 43410',
    'description_raw': (
        'City of Clyde-managed cemetery located at 422 E. McPherson Highway (US Route 20), '
        'at the northeast corner of E. McPherson Hwy and E. Maple Street. '
        'Governed under Chapter 951 of Clyde\'s codified ordinances. '
        'Hours: Monday–Friday 7 AM–3:30 PM. Includes a Veterans section.'
    ),
    'features_raw': 'Active cemetery; Veterans section',
    'difficulty_raw': None,
    'accessibility_raw': None,
    'urls_raw': ['https://www.clydeohio.org/172/Cemetery'],
    'identity_notes_raw': (
        'City of Clyde-managed cemetery per clydeohio.org/172/Cemetery. '
        'Cemetery Superintendent: Joel Roberts, 419-547-8181, cem@clydeohio.org. '
        'Mailing address: 222 N. Main St., Clyde, OH 43410.'
    ),
    'township_raw': None,
    'municipality_raw': None,
    'discovery_tier': 6,
    'seeded_from_baseline': False,
    'baseline_id': None,
})

f.write_text(yaml.dump(data, allow_unicode=True, sort_keys=False), encoding='utf-8')
print(f'T6 Clyde staged. Total records: {len(data["records"])}')
