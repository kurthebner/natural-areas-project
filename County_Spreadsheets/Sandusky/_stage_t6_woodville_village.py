import yaml, pathlib

f = pathlib.Path('County_Spreadsheets/Sandusky/sandusky_ohio_raw_discovery.yaml')
data = yaml.safe_load(f.read_text(encoding='utf-8'))
data.setdefault('records', [])

# --- Woodville Village Parks (4 Sites + 1 Cemetery Site) ---
# Note: "Woodville Cemetery" on Cemetery Drive (village) is distinct from
# "Woodville Cemetery" on CR 30 (Woodville Township, staged at T5).

# H.W. Busdiecker Park (also called Flag Park / Teardrop Park)
data['records'].append({
    'entity_type': 'Site',
    'name_raw': 'H.W. Busdiecker Park',
    'counties_raw': ['Sandusky'],
    'county_primary': 'Sandusky',
    'ownership_raw': 'Village of Woodville',
    'governance_raw': 'Village of Woodville',
    'partner_agencies_raw': None,
    'coordination_raw': None,
    'gps_lat_raw': None,
    'gps_lon_raw': None,
    'location_raw': 'Intersection of Main Street (US Route 20) and Fort Findlay Road, Woodville, OH 43469',
    'description_raw': (
        'Triangular roadway-island park formed by the 1969 US Route 20 bridge widening. '
        'Features fourteen flagpoles in horseshoe formation, each dedicated to one of 14 NASA '
        'astronauts killed in the line of duty. Dedicated June 1995 to honor former Mayor '
        'Herbert W. Busdiecker and astronaut Col. Tom Henricks. '
        'Also known as Flag Park or Teardrop Park.'
    ),
    'features_raw': 'Flagpoles (14); Veterans memorial',
    'difficulty_raw': None,
    'accessibility_raw': None,
    'urls_raw': ['https://www.villageofwoodville.com/parks'],
    'identity_notes_raw': (
        'Village of Woodville municipal park per villageofwoodville.com/parks. '
        'No street number — site is a triangular road island at the US 20 / Fort Findlay Rd intersection. '
        'Also known as Flag Park or Teardrop Park.'
    ),
    'township_raw': None,
    'municipality_raw': None,
    'discovery_tier': 6,
    'seeded_from_baseline': False,
    'baseline_id': None,
})

# Trail Marker Park (also called Pool Park)
data['records'].append({
    'entity_type': 'Site',
    'name_raw': 'Trail Marker Park',
    'counties_raw': ['Sandusky'],
    'county_primary': 'Sandusky',
    'ownership_raw': 'Village of Woodville',
    'governance_raw': 'Village of Woodville',
    'partner_agencies_raw': None,
    'coordination_raw': None,
    'gps_lat_raw': None,
    'gps_lon_raw': None,
    'location_raw': 'Erie Street, Woodville, OH 43469 (east of Cherry Street; community pool at 201 Erie St)',
    'description_raw': (
        'Village of Woodville\'s main multi-use park on Erie Street along the Portage River. '
        'Features a reservable shelter house, Orchard Gazebo (reservable), carport, '
        'playground area, basketball court, picnic tables, restrooms, community swimming pool '
        '(opened July 4, 1967; seasonal), disc golf course, and a boat ramp on the Portage River. '
        'Hosts the village\'s annual Fourth of July celebration (since 1953). '
        'Also known as Pool Park.'
    ),
    'features_raw': 'Shelter house; Gazebo; Playground; Basketball court; Picnic tables; Restrooms; Swimming pool (seasonal); Disc golf; Boat ramp; Portage River access',
    'difficulty_raw': None,
    'accessibility_raw': None,
    'urls_raw': ['https://www.villageofwoodville.com/parks'],
    'identity_notes_raw': (
        'Village of Woodville municipal park per villageofwoodville.com/parks. '
        'Also known as Pool Park. Shelter and gazebo reservations: 419-849-3031.'
    ),
    'township_raw': None,
    'municipality_raw': None,
    'discovery_tier': 6,
    'seeded_from_baseline': False,
    'baseline_id': None,
})

# Veterans Park (also called Waterworks Park)
data['records'].append({
    'entity_type': 'Site',
    'name_raw': 'Veterans Park',
    'counties_raw': ['Sandusky'],
    'county_primary': 'Sandusky',
    'ownership_raw': 'Village of Woodville',
    'governance_raw': 'Village of Woodville',
    'partner_agencies_raw': None,
    'coordination_raw': None,
    'gps_lat_raw': None,
    'gps_lon_raw': None,
    'location_raw': 'West First Street between Walnut Street and Perry Street, Woodville, OH 43469',
    'description_raw': (
        'Village of Woodville park featuring a World War I Doughboy statue (erected 1927), '
        'decommissioned cannons, playground, and open space for sports. '
        'Houses the village water treatment plant and water tower. '
        'Hosts annual Memorial Day services. Also known as Waterworks Park.'
    ),
    'features_raw': 'Veterans memorial; Doughboy statue (WWI); Cannons; Playground; Open space',
    'difficulty_raw': None,
    'accessibility_raw': None,
    'urls_raw': ['https://www.villageofwoodville.com/parks'],
    'identity_notes_raw': (
        'Village of Woodville municipal park per villageofwoodville.com/parks. '
        'Also known as Waterworks Park. Village water treatment plant co-located on parcel.'
    ),
    'township_raw': None,
    'municipality_raw': None,
    'discovery_tier': 6,
    'seeded_from_baseline': False,
    'baseline_id': None,
})

# Limelite Eagle Park
data['records'].append({
    'entity_type': 'Site',
    'name_raw': 'Limelite Eagle Park',
    'counties_raw': ['Sandusky'],
    'county_primary': 'Sandusky',
    'ownership_raw': 'Village of Woodville',
    'governance_raw': 'Village of Woodville',
    'partner_agencies_raw': None,
    'coordination_raw': None,
    'gps_lat_raw': None,
    'gps_lon_raw': None,
    'location_raw': 'Main Street (US Route 20), Woodville, OH 43469 (former Limelite Theatre site)',
    'description_raw': (
        'Small village park developed 2017–2019 on the site of the former Limelite Theatre '
        'through Boy Scout Eagle Scout projects. Features a concrete sidewalk and patio, '
        'picnic benches, 45-ton river rock bed, and 180 plants and shrubs.'
    ),
    'features_raw': 'Picnic benches; Plantings/landscaping; River rock bed',
    'difficulty_raw': None,
    'accessibility_raw': None,
    'urls_raw': ['https://www.villageofwoodville.com/parks'],
    'identity_notes_raw': (
        'Village of Woodville municipal park per villageofwoodville.com/parks. '
        'No street number — located on former Limelite Theatre site on Main Street (US 20). '
        'Developed through Boy Scout Eagle Scout projects 2017–2019.'
    ),
    'township_raw': None,
    'municipality_raw': None,
    'discovery_tier': 6,
    'seeded_from_baseline': False,
    'baseline_id': None,
})

# Woodville Cemetery (Village — Cemetery Drive)
# DISTINCT from Woodville Township Cemetery (CR 30, Martin Marietta Plant area, staged T5).
data['records'].append({
    'entity_type': 'Site',
    'name_raw': 'Woodville Cemetery',
    'counties_raw': ['Sandusky'],
    'county_primary': 'Sandusky',
    'ownership_raw': 'Village of Woodville',
    'governance_raw': 'Village of Woodville',
    'partner_agencies_raw': None,
    'coordination_raw': None,
    'gps_lat_raw': None,
    'gps_lon_raw': None,
    'location_raw': 'Cemetery Drive (also recorded as County Road 907), Woodville, OH 43469',
    'description_raw': (
        'Principal municipal cemetery for the Village of Woodville. Established ca. 1827/1828. '
        'Approximately 3,454 documented burials. Located on Cemetery Drive (County Road 907).'
    ),
    'features_raw': 'Active cemetery; Historic burials (est. ca. 1827)',
    'difficulty_raw': None,
    'accessibility_raw': None,
    'urls_raw': ['https://www.villageofwoodville.com/'],
    'identity_notes_raw': (
        'NEEDS_VERIFICATION — governance inferred as Village of Woodville based on location '
        'within village limits and genealogical sources identifying it as the principal '
        'village cemetery. Village office (419-849-2731) should confirm ownership vs. '
        'township or county management. '
        'DISTINCT ENTITY from "Woodville Cemetery" on CR 30 (Woodville Township, staged T5). '
        'This cemetery is on Cemetery Drive (CR 907); the township cemetery is in the '
        'Martin Marietta Plant area on CR 30.'
    ),
    'township_raw': None,
    'municipality_raw': None,
    'discovery_tier': 6,
    'seeded_from_baseline': False,
    'baseline_id': None,
})

f.write_text(yaml.dump(data, allow_unicode=True, sort_keys=False), encoding='utf-8')
print(f'T6 Woodville village staged. Total records: {len(data["records"])}')
