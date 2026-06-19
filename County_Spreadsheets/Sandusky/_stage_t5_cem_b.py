import yaml, pathlib

f = pathlib.Path('County_Spreadsheets/Sandusky/sandusky_ohio_raw_discovery.yaml')
data = yaml.safe_load(f.read_text(encoding='utf-8'))
data.setdefault('records', [])

# --- Sandusky Township --- (3 cemeteries with addresses)

sandusky_cems = [
    ('Binkley Cemetery', '2529 Oak Harbor Road, Fremont, OH 43420', 'Also known as Lower Muskellunge. Historic burial site.'),
    ('Four Mile House Cemetery', '880 County Road 128, Fremont, OH 43420', 'Historic cemetery honoring early settlers of the area.'),
    ('Slates Cemetery', '551 County Road 128, Fremont, OH 43420', 'Also known as Upper Muskellunge. Historic burial site for community pioneers.'),
]
for name, addr, desc in sandusky_cems:
    data['records'].append({
        'entity_type': 'Site',
        'name_raw': name,
        'counties_raw': ['Sandusky'],
        'county_primary': 'Sandusky',
        'ownership_raw': 'Sandusky Township',
        'governance_raw': 'Sandusky Township',
        'partner_agencies_raw': None,
        'coordination_raw': None,
        'gps_lat_raw': None,
        'gps_lon_raw': None,
        'location_raw': addr,
        'description_raw': desc,
        'features_raw': 'Active cemetery',
        'difficulty_raw': None,
        'accessibility_raw': None,
        'urls_raw': ['http://www.sanduskytownship.com/index.php?page=cemeteries'],
        'identity_notes_raw': 'Township-managed cemetery per Sandusky Township official website. Address confirmed from website.',
        'township_raw': None,
        'municipality_raw': None,
        'discovery_tier': 5,
        'seeded_from_baseline': False,
        'baseline_id': None
    })

# --- Scott Township ---

data['records'].append({
    'entity_type': 'Site',
    'name_raw': 'Chestnut Grove Cemetery',
    'counties_raw': ['Sandusky'],
    'county_primary': 'Sandusky',
    'ownership_raw': 'Scott Township',
    'governance_raw': 'Scott Township',
    'partner_agencies_raw': None,
    'coordination_raw': None,
    'gps_lat_raw': None,
    'gps_lon_raw': None,
    'location_raw': 'US Route 23, approximately 1.2 miles south of US Route 6, Scott Township, Sandusky County OH (on Wood County line)',
    'description_raw': (
        'Cemetery located on US 23, 1.2 miles south of US 6 on the Sandusky/Wood County line. '
        'Located directly across from Bradner Cemetery (Wood County). Contains approximately 1,269 documented burials.'
    ),
    'features_raw': 'Active cemetery',
    'difficulty_raw': None,
    'accessibility_raw': None,
    'urls_raw': ['https://www.findagrave.com/cemetery/2150239/chestnut-grove-cemetery'],
    'identity_notes_raw': (
        'NEEDS_VERIFICATION — township ownership inferred from location in Scott Township; '
        'no Scott Township official website found to confirm management. Scott Township has '
        'no OTA website. Located on county line with Wood County. '
        'GIS_VERIFY_COUNTY — confirm parcel is in Sandusky County, not Wood County.'
    ),
    'township_raw': None,
    'municipality_raw': None,
    'discovery_tier': 5,
    'seeded_from_baseline': False,
    'baseline_id': None
})

# --- Townsend Township --- (2 cemeteries, both on E SR 101)

for cem_name in ['Parkhurst Cemetery', 'Tew Cemetery']:
    data['records'].append({
        'entity_type': 'Site',
        'name_raw': cem_name,
        'counties_raw': ['Sandusky'],
        'county_primary': 'Sandusky',
        'ownership_raw': 'Townsend Township',
        'governance_raw': 'Townsend Township',
        'partner_agencies_raw': None,
        'coordination_raw': None,
        'gps_lat_raw': None,
        'gps_lon_raw': None,
        'location_raw': 'East State Route 101, Townsend Township, Sandusky County OH',
        'description_raw': None,
        'features_raw': 'Active cemetery; Plots available',
        'difficulty_raw': None,
        'accessibility_raw': None,
        'urls_raw': ['https://www.townsendtownship.org/cemetery'],
        'identity_notes_raw': (
            'Township-managed cemetery per Townsend Township official website. '
            'Both Parkhurst and Tew cemeteries are on East SR 101. Active plots available.'
        ),
        'township_raw': None,
        'municipality_raw': None,
        'discovery_tier': 5,
        'seeded_from_baseline': False,
        'baseline_id': None
    })

# --- Washington Township --- (3 cemeteries)

washington_cems = [
    ('Lindsey Cemetery', 'Lindsey OH 43442 area, Washington Township, Sandusky County'),
    ('Washington Chapel Cemetery', 'Township Road 96, Washington Township, Sandusky County OH'),
    ('Hessville Cemetery', 'State Route 600, Washington Township, Sandusky County OH'),
]
for name, addr in washington_cems:
    data['records'].append({
        'entity_type': 'Site',
        'name_raw': name,
        'counties_raw': ['Sandusky'],
        'county_primary': 'Sandusky',
        'ownership_raw': 'Washington Township',
        'governance_raw': 'Washington Township',
        'partner_agencies_raw': None,
        'coordination_raw': None,
        'gps_lat_raw': None,
        'gps_lon_raw': None,
        'location_raw': addr,
        'description_raw': None,
        'features_raw': 'Active cemetery',
        'difficulty_raw': None,
        'accessibility_raw': None,
        'urls_raw': ['https://sites.google.com/view/washington-sandusky/home'],
        'identity_notes_raw': (
            'Township-managed cemetery per Washington Township (Sandusky County) website '
            'and county sources. Cemetery Sexton: Sal Copley (419) 307-9148.'
        ),
        'township_raw': None,
        'municipality_raw': None,
        'discovery_tier': 5,
        'seeded_from_baseline': False,
        'baseline_id': None
    })

# --- Woodville Township --- (3 cemeteries)

woodville_cems = [
    ('Westwood Cemetery', 'Intersection of State Route 105 and State Route 582, Woodville Township, Sandusky County OH', 'Active; approximately 15 acres. Created 1956 when Standard Lime & Stone donated $25,000 for development.'),
    ('Woodville Cemetery', 'County Road 30 (Lime Road), north of the Village of Woodville, in the Martin Marietta Plant area, Sandusky County OH', 'Active; accessible via causeway-like roadway between quarries.'),
    ('Sugar Creek Cemetery', 'US Route 20, approximately 2 miles east of the Village of Woodville, Sandusky County OH', 'Active.'),
]
for name, addr, desc in woodville_cems:
    data['records'].append({
        'entity_type': 'Site',
        'name_raw': name,
        'counties_raw': ['Sandusky'],
        'county_primary': 'Sandusky',
        'ownership_raw': 'Woodville Township',
        'governance_raw': 'Woodville Township',
        'partner_agencies_raw': None,
        'coordination_raw': None,
        'gps_lat_raw': None,
        'gps_lon_raw': None,
        'location_raw': addr,
        'description_raw': desc,
        'features_raw': 'Active cemetery',
        'difficulty_raw': None,
        'accessibility_raw': None,
        'urls_raw': ['https://woodvilletownshipoh.gov/cemeteries/'],
        'identity_notes_raw': 'Township-managed cemetery per Woodville Township official website.',
        'township_raw': None,
        'municipality_raw': None,
        'discovery_tier': 5,
        'seeded_from_baseline': False,
        'baseline_id': None
    })

# --- York Township --- (5 cemeteries: 3 active, 2 inactive)

york_cems = [
    ('Ellsworth Cemetery', 'State Route 101, York Township, Sandusky County OH', 'Active'),
    ('Wales Corners Cemetery', 'County Road 175, York Township, Sandusky County OH', 'Active'),
    ('York Chapel Cemetery', 'County Road 292, York Township, Sandusky County OH', 'Active'),
]
for name, addr, status in york_cems:
    data['records'].append({
        'entity_type': 'Site',
        'name_raw': name,
        'counties_raw': ['Sandusky'],
        'county_primary': 'Sandusky',
        'ownership_raw': 'York Township',
        'governance_raw': 'York Township',
        'partner_agencies_raw': None,
        'coordination_raw': None,
        'gps_lat_raw': None,
        'gps_lon_raw': None,
        'location_raw': addr,
        'description_raw': None,
        'features_raw': 'Active cemetery',
        'difficulty_raw': None,
        'accessibility_raw': None,
        'urls_raw': ['https://www.yorktwp.com/cemetery-information.html'],
        'identity_notes_raw': f'Township-owned cemetery per York Township official website. Status: {status}.',
        'township_raw': None,
        'municipality_raw': None,
        'discovery_tier': 5,
        'seeded_from_baseline': False,
        'baseline_id': None
    })

york_inactive = [
    ('Gilbert Cemetery', 'County Road 177, York Township, Sandusky County OH'),
    ('Wickwyre Cemetery', 'County Road 308, York Township, Sandusky County OH'),
]
for name, addr in york_inactive:
    data['records'].append({
        'entity_type': 'Site',
        'name_raw': name,
        'counties_raw': ['Sandusky'],
        'county_primary': 'Sandusky',
        'ownership_raw': 'York Township',
        'governance_raw': 'York Township',
        'partner_agencies_raw': None,
        'coordination_raw': None,
        'gps_lat_raw': None,
        'gps_lon_raw': None,
        'location_raw': addr,
        'description_raw': None,
        'features_raw': 'Inactive cemetery; Township-maintained',
        'difficulty_raw': None,
        'accessibility_raw': None,
        'urls_raw': ['https://www.yorktwp.com/cemetery-information.html'],
        'identity_notes_raw': 'Township-owned cemetery per York Township official website. Listed as INACTIVE (no new burials).',
        'township_raw': None,
        'municipality_raw': None,
        'discovery_tier': 5,
        'seeded_from_baseline': False,
        'baseline_id': None
    })

f.write_text(yaml.dump(data, allow_unicode=True, sort_keys=False), encoding='utf-8')
print(f'T5 cemeteries B staged. Total records: {len(data["records"])}')
