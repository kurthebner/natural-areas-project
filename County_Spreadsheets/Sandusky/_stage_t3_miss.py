import yaml, pathlib

f = pathlib.Path('County_Spreadsheets/Sandusky/sandusky_ohio_raw_discovery.yaml')
data = yaml.safe_load(f.read_text(encoding='utf-8'))
data.setdefault('records', [])

# Waggoner's Run Mountain Bike Trail — T3 SCPD miss discovered during T4 review
# SCPD-managed trail within White Star Park; 6 miles; Flatlanders Bicycle Club collaborative build
data['records'].append({
    'entity_type': 'Trail',
    'name_raw': "Waggoner's Run Mountain Bike Trail",
    'counties_raw': ['Sandusky'],
    'county_primary': 'Sandusky',
    'ownership_raw': 'Sandusky County Park District',
    'governance_raw': 'Sandusky County Park District',
    'partner_agencies_raw': 'Flatlanders Bicycle Club (built collaboratively 2019-2020)',
    'coordination_raw': None,
    'gps_lat_raw': None,
    'gps_lon_raw': None,
    'location_raw': '5013 County Road 65, Gibsonburg, OH 43431 — begins at parking lot adjacent to railroad tracks; near White Star Park Barn',
    'description_raw': (
        '6-mile one-way mountain bike trail within White Star Park. Built collaboratively '
        'by Flatlanders Bicycle Club and SCPD, dedicated October 2020 and named after local '
        'cycling enthusiast Dan Waggoner. Features bridges, technical obstacles, man-made '
        'features including a teeter-totter. All features can be attempted or bypassed. '
        'Open year-round dusk to dawn; extended to 9 PM September–April. Free.'
    ),
    'features_raw': 'Mountain biking; Hiking; Natural surfaces; Bridges; Technical features',
    'difficulty_raw': 'Intermediate; advanced features avoidable',
    'accessibility_raw': None,
    'urls_raw': [
        'https://www.sanduskycounty.org/mtbtrails',
        'https://www.lovemyparks.com/things-to-do/biking/mountain-biking'
    ],
    'identity_notes_raw': (
        'T3 miss — discovered during T4 CVB cross-reference. SCPD-managed trail within White '
        'Star Park property. One-way; no horses, pets, or motorized vehicles. '
        'Named after Dan Waggoner, local cycling enthusiast and bicycle shop owner.'
    ),
    'township_raw': None,
    'municipality_raw': None,
    'discovery_tier': 3,
    'seeded_from_baseline': False,
    'baseline_id': None
})

f.write_text(yaml.dump(data, allow_unicode=True, sort_keys=False), encoding='utf-8')
print(f'T3 miss staged. Total records: {len(data["records"])}')
