import yaml, pathlib

f = pathlib.Path('County_Spreadsheets/Sandusky/sandusky_ohio_raw_discovery.yaml')
data = yaml.safe_load(f.read_text(encoding='utf-8'))
data.setdefault('records', [])

# --- Fremont City Parks (9 Sites) ---

fremont_parks = [
    (
        'Anderson Fields',
        '1313 Oak Harbor Road, Fremont, OH 43420',
        (
            'Three-diamond Little League baseball fields, basketball court, playground, restrooms. '
            'Replaced the historic Anderson Field in 1996.'
        ),
        'Baseball/softball fields (3); Basketball court; Playground; Restrooms',
    ),
    (
        'Biggs-Kettner Memorial East Side Park',
        '601 St. Joseph Street, Fremont, OH 43420',
        (
            'Fremont\'s largest recreation complex. Outdoor amenities include basketball courts, '
            'playground, skate park, restrooms, soccer fields, tennis courts, and six shelter houses. '
            'The recreation building features indoor courts, seasonal ice rink, and heated pool. '
            'North Coast Inland Trail (KNOWN_MC:OH-MC-T-0110) access point located on site.'
        ),
        'Basketball courts; Playground; Skate park; Restrooms; Soccer fields; Tennis courts; Shelter houses (6); Indoor recreation center; Seasonal ice rink; Heated pool; NCIT access',
    ),
    (
        'Birchard Park',
        '1400 Birchard Avenue, Fremont, OH 43420',
        (
            'Established 1871; land donated by Sardis Birchard (uncle of President Rutherford B. Hayes). '
            'Features basketball courts, tennis courts, shelter houses, shuffleboard courts, walking path, '
            'and a bandstand.'
        ),
        'Basketball courts; Tennis courts; Shelter houses; Shuffleboard courts; Walking path; Bandstand',
    ),
    (
        'Richard D. Maier Park',
        '1019 Birchard Avenue, Fremont, OH 43420',
        (
            'Small neighborhood park with mature trees, gazebo, and benches. '
            'Renamed in 1986 in honor of former Fremont mayor Richard D. Maier.'
        ),
        'Gazebo; Benches; Mature trees',
    ),
    (
        'Swartzlander-Rotary Park',
        '329 Avis Street, Fremont, OH 43420',
        'Small downtown park.',
        None,
    ),
    (
        'Tschumy Corner',
        'Corner of State Street and Front Street, Fremont, OH 43420',
        'Decorative downtown plaza; dedicated 2001.',
        None,
    ),
    (
        'Robert L. Walsh Park',
        '610 Morrison Street, Fremont, OH 43420',
        (
            'Described as Fremont\'s largest city park. Features walking trails, playground, large shelter '
            'house, restrooms, fountain, and memorial garden. Dedicated 1996.'
        ),
        'Walking trails; Playground; Shelter house (large); Restrooms; Fountain; Memorial garden',
    ),
    (
        'Rodger W. Young Park',
        '1111 Tiffin Street, Fremont, OH 43420',
        (
            'Large athletic park dedicated 1943 to Sandusky County\'s WWII Medal of Honor recipient '
            'Rodger W. Young. Features six baseball/softball fields, eight tennis courts, two basketball '
            'courts, playground, two shelter houses, and four multi-purpose fields.'
        ),
        'Baseball/softball fields (6); Tennis courts (8); Basketball courts (2); Playground; Shelter houses (2); Multi-purpose fields (4)',
    ),
    (
        'Ozzie Rauch Park',
        '344 2nd Street, Fremont, OH 43420',
        'Small neighborhood park; revamped 2021. Features half-court basketball, picnic area, and play area.',
        'Basketball court (half-court); Picnic area; Play area',
    ),
]

for name, addr, desc, feats in fremont_parks:
    data['records'].append({
        'entity_type': 'Site',
        'name_raw': name,
        'counties_raw': ['Sandusky'],
        'county_primary': 'Sandusky',
        'ownership_raw': 'City of Fremont',
        'governance_raw': 'City of Fremont',
        'partner_agencies_raw': None,
        'coordination_raw': None,
        'gps_lat_raw': None,
        'gps_lon_raw': None,
        'location_raw': addr,
        'description_raw': desc,
        'features_raw': feats,
        'difficulty_raw': None,
        'accessibility_raw': None,
        'urls_raw': ['https://www.fremontohio.org/departments/parks/'],
        'identity_notes_raw': 'City of Fremont municipal park per fremontohio.org/departments/parks/',
        'township_raw': None,
        'municipality_raw': None,
        'discovery_tier': 6,
        'seeded_from_baseline': False,
        'baseline_id': None,
    })

# --- Fremont Access Points (2 APs) ---

# Sand Docks — city-managed boat ramp / river bank access on Sandusky River
data['records'].append({
    'entity_type': 'Access Point',
    'name_raw': 'Sand Docks',
    'counties_raw': ['Sandusky'],
    'county_primary': 'Sandusky',
    'ownership_raw': 'City of Fremont',
    'governance_raw': 'City of Fremont',
    'partner_agencies_raw': None,
    'coordination_raw': None,
    'gps_lat_raw': None,
    'gps_lon_raw': None,
    'location_raw': 'End of North Street / Sand Road, Fremont, OH 43420',
    'description_raw': (
        'City of Fremont boat ramp and river bank access area on the Sandusky River. '
        'Provides public fishing access and boat launch access to the Sandusky River.'
    ),
    'features_raw': 'Boat ramp; Fishing access; River bank access',
    'difficulty_raw': None,
    'accessibility_raw': None,
    'urls_raw': ['https://www.fremontohio.org/departments/parks/'],
    'identity_notes_raw': (
        'City of Fremont-managed river access per fremontohio.org parks page. '
        'Distinct from Darr-Root Fishing Access (T2/ODNR-managed, 201 Walnut St).'
    ),
    'township_raw': None,
    'municipality_raw': None,
    'discovery_tier': 6,
    'seeded_from_baseline': True,
    'baseline_id': 'Sand Docks',
})

# Miles Newton Bridge — city fishing access area on Sandusky River
data['records'].append({
    'entity_type': 'Access Point',
    'name_raw': 'Miles Newton Bridge Fishing Access',
    'counties_raw': ['Sandusky'],
    'county_primary': 'Sandusky',
    'ownership_raw': 'City of Fremont',
    'governance_raw': 'City of Fremont',
    'partner_agencies_raw': None,
    'coordination_raw': None,
    'gps_lat_raw': None,
    'gps_lon_raw': None,
    'location_raw': 'Between State Street Bridge and Miles Newton Bridge, downtown Fremont, OH 43420',
    'description_raw': (
        'City of Fremont public fishing access area on the Sandusky River, '
        'located along the river bank in downtown Fremont between the State Street Bridge '
        'and the Miles Newton Bridge.'
    ),
    'features_raw': 'Fishing access; River bank access',
    'difficulty_raw': None,
    'accessibility_raw': None,
    'urls_raw': ['https://www.fremontohio.org/departments/parks/'],
    'identity_notes_raw': 'City of Fremont-managed fishing access per fremontohio.org parks page.',
    'township_raw': None,
    'municipality_raw': None,
    'discovery_tier': 6,
    'seeded_from_baseline': False,
    'baseline_id': None,
})

f.write_text(yaml.dump(data, allow_unicode=True, sort_keys=False), encoding='utf-8')
print(f'T6 Fremont staged. Total records: {len(data["records"])}')
