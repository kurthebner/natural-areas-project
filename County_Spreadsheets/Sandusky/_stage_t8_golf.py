import yaml, pathlib

f = pathlib.Path('County_Spreadsheets/Sandusky/sandusky_ohio_raw_discovery.yaml')
data = yaml.safe_load(f.read_text(encoding='utf-8'))
data.setdefault('records', [])

# --- Sandusky County Golf Courses — Tier 8 ---
# Enumerated per IMP-110 mandatory golf course enumeration.
# All golf courses in scope regardless of access model.

golf_courses = [
    (
        'Sycamore Hills Golf Club',
        '3728 W. Hayes Avenue, Fremont, OH 43420',
        (
            'Public 27-hole golf facility with three 9-hole courses (Red/White/Blue). '
            'Opened 1964 (original 18), 1967 (additional 9), 1995 (third 9). '
            'Five lakes on the course. Privately operated.'
        ),
        '27 holes (3x9); 5 lakes; Public tee times',
        'Active',
        'Public access — open tee times. Three 9-hole courses (Red, White, Blue). Privately operated.',
    ),
    (
        'Fremont Country Club',
        '2340 E. State Street, Fremont, OH 43420',
        (
            'Private members-only 18-hole golf club. Founded 1921. '
            '6,650 yards, par 71.'
        ),
        '18 holes; Par 71; 6,650 yards',
        'Active',
        'Members-only — no public tee times. Founded 1921. Private club.',
    ),
    (
        'Green Hills Golf Course',
        '1959 S. Main Street, Clyde, OH 43410',
        (
            'Public 18-hole and 9-hole executive golf facility in Clyde. '
            'Founded 1958. Chamber of Commerce member. Privately operated.'
        ),
        '18 holes; 9-hole executive course; Public tee times',
        'Active',
        'Public access — open tee times. Founded 1958. Includes executive 9-hole West course.',
    ),
    (
        'Hidden Hills Golf Club',
        '4900 County Road 16, Woodville, OH 43469',
        '18-hole golf course in Woodville area, Sandusky County. Privately operated.',
        '18 holes; Public tee times',
        'Active',
        'Public access — open tee times. MINIMAL_DATA — no additional details confirmed from web sources.',
    ),
    (
        'Sleepy Hollow Golf Course',
        '6029 State Route 101 E, Clyde, OH 43410',
        (
            'Former 18-hole golf course in Clyde. Permanently closed at end of 2019. '
            'Property subsequently converted to Sleepy Hollow RV Park.'
        ),
        '18 holes (former)',
        'Closed',
        'CLOSED — permanently closed end of 2019. Property converted to RV park.',
    ),
]

for name, addr, desc, feats, status, notes in golf_courses:
    data['records'].append({
        'entity_type': 'Site',
        'name_raw': name,
        'counties_raw': ['Sandusky'],
        'county_primary': 'Sandusky',
        'ownership_raw': 'Private',
        'governance_raw': name,
        'partner_agencies_raw': None,
        'coordination_raw': None,
        'gps_lat_raw': None,
        'gps_lon_raw': None,
        'location_raw': addr,
        'description_raw': desc,
        'features_raw': feats,
        'difficulty_raw': None,
        'accessibility_raw': None,
        'urls_raw': [],
        'identity_notes_raw': notes,
        'township_raw': None,
        'municipality_raw': None,
        'discovery_tier': 8,
        'seeded_from_baseline': False,
        'baseline_id': None,
    })

# River Cliff Golf Course — governance uncertain (T3 SCPD vs. T8 private)
data['records'].append({
    'entity_type': 'Site',
    'name_raw': 'River Cliff Golf Course',
    'counties_raw': ['Sandusky'],
    'county_primary': 'Sandusky',
    'ownership_raw': 'UNCERTAIN — private or Sandusky County Park District',
    'governance_raw': 'UNCERTAIN — private or Sandusky County Park District',
    'partner_agencies_raw': None,
    'coordination_raw': None,
    'gps_lat_raw': None,
    'gps_lon_raw': None,
    'location_raw': '1313 Tiffin Street, Fremont, OH 43420',
    'description_raw': '9-hole golf course in Fremont at 1313 Tiffin Street.',
    'features_raw': '9 holes; Public tee times (if private-operated)',
    'difficulty_raw': None,
    'accessibility_raw': None,
    'urls_raw': [],
    'identity_notes_raw': (
        'GOVERNANCE_UNCERTAIN — staged at T8 (private) pending verification. '
        'Address (1313 Tiffin St) is adjacent to Sandusky County Park District\'s '
        'Don W. Miller Memorial Park (1329 Tiffin St, formerly River Cliff Park). '
        'If SCPD-operated, reclassify to T3 and add to SCPD records. '
        'GIS parcel lookup required to confirm ownership. '
        'Public access — open tee times per search results.'
    ),
    'township_raw': None,
    'municipality_raw': None,
    'discovery_tier': 8,
    'seeded_from_baseline': False,
    'baseline_id': None,
})

# Sugar Creek Golf Course — cross-county (Ottawa/Sandusky)
data['records'].append({
    'entity_type': 'Site',
    'name_raw': 'Sugar Creek Golf Course & Driving Range',
    'counties_raw': ['Ottawa', 'Sandusky'],
    'county_primary': 'Ottawa',
    'ownership_raw': 'Private',
    'governance_raw': 'Sugar Creek Golf Course & Driving Range',
    'partner_agencies_raw': None,
    'coordination_raw': None,
    'gps_lat_raw': None,
    'gps_lon_raw': None,
    'location_raw': '950 W. Elmore Eastern Road, Elmore, OH 43416',
    'description_raw': '18-hole public golf course and driving range in Elmore.',
    'features_raw': '18 holes; Driving range; Public tee times',
    'difficulty_raw': None,
    'accessibility_raw': None,
    'urls_raw': [],
    'identity_notes_raw': (
        'GIS_VERIFY_COUNTY — Elmore straddles Ottawa and Sandusky counties. '
        'Address alone insufficient to assign county_primary. GIS parcel lookup required. '
        'county_primary set to Ottawa pending verification. '
        'Public access — open tee times. CROSS_COUNTY_CANDIDATE.'
    ),
    'township_raw': None,
    'municipality_raw': None,
    'discovery_tier': 8,
    'seeded_from_baseline': False,
    'baseline_id': None,
})

f.write_text(yaml.dump(data, allow_unicode=True, sort_keys=False), encoding='utf-8')
print(f'T8 golf courses staged. Total records: {len(data["records"])}')
