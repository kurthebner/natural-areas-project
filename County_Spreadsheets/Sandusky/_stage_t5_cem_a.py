import yaml, pathlib

f = pathlib.Path('County_Spreadsheets/Sandusky/sandusky_ohio_raw_discovery.yaml')
data = yaml.safe_load(f.read_text(encoding='utf-8'))
data.setdefault('records', [])

# --- Ballville Township ---

data['records'].append({
    'entity_type': 'Site',
    'name_raw': 'Oakwood Cemetery',
    'counties_raw': ['Sandusky'],
    'county_primary': 'Sandusky',
    'ownership_raw': 'Ballville Township',
    'governance_raw': 'Ballville Township',
    'partner_agencies_raw': None,
    'coordination_raw': None,
    'gps_lat_raw': None,
    'gps_lon_raw': None,
    'location_raw': '1225 Oakwood Street, Fremont, OH 43420',
    'description_raw': (
        'Active township cemetery, established 1858. Originally operated by the Oakwood Cemetery '
        'Association; transferred to Ballville Township ownership in 2021 when the association '
        'voted to dissolve and convey its funds and properties to the township. Approximately 26 '
        'acres. Includes a Veterans Section.'
    ),
    'features_raw': 'Active cemetery; Veterans section; Historic burials (est. 1858)',
    'difficulty_raw': None,
    'accessibility_raw': None,
    'urls_raw': ['https://www.ballville.org/cemetery-fee-schedule/'],
    'identity_notes_raw': (
        'Township-owned since 2021. Previously owned by Oakwood Cemetery Association '
        '(est. 1858; 26 ac purchased from James Vallette). Active burials.'
    ),
    'township_raw': None,
    'municipality_raw': None,
    'discovery_tier': 5,
    'seeded_from_baseline': False,
    'baseline_id': None
})

# --- Jackson Township ---

data['records'].append({
    'entity_type': 'Site',
    'name_raw': 'Smith Cemetery',
    'counties_raw': ['Sandusky'],
    'county_primary': 'Sandusky',
    'ownership_raw': 'Jackson Township',
    'governance_raw': 'Jackson Township',
    'partner_agencies_raw': None,
    'coordination_raw': None,
    'gps_lat_raw': None,
    'gps_lon_raw': None,
    'location_raw': 'Burgoon area, Jackson Township, Sandusky County OH',
    'description_raw': (
        'Township-managed cemetery in Jackson Township. Site of annual Memorial Day service '
        'hosted by the American Legion. Located in the Burgoon area of Jackson Township.'
    ),
    'features_raw': 'Active cemetery; Annual Memorial Day service',
    'difficulty_raw': None,
    'accessibility_raw': None,
    'urls_raw': ['http://www.jackson-sandusky.com/'],
    'identity_notes_raw': (
        'MINIMAL_DATA — confirmed township-managed per jackson-sandusky.com website navigation '
        'and Memorial Day service reference. No street address found in web sources. '
        'Address requires field verification.'
    ),
    'township_raw': None,
    'municipality_raw': None,
    'discovery_tier': 5,
    'seeded_from_baseline': False,
    'baseline_id': None
})

# --- Madison Township ---

data['records'].append({
    'entity_type': 'Site',
    'name_raw': 'West Union Cemetery',
    'counties_raw': ['Sandusky'],
    'county_primary': 'Sandusky',
    'ownership_raw': 'Madison Township',
    'governance_raw': 'Madison Township',
    'partner_agencies_raw': None,
    'coordination_raw': None,
    'gps_lat_raw': None,
    'gps_lon_raw': None,
    'location_raw': 'West Madison Street area, Gibsonburg OH 43431 (Madison Township, Sandusky County)',
    'description_raw': (
        'Public cemetery in Madison Township, Sandusky County, near Gibsonburg. '
        'Includes a Veterans Memorial. Located near the hamlet of Rollersville.'
    ),
    'features_raw': 'Active cemetery; Veterans memorial',
    'difficulty_raw': None,
    'accessibility_raw': None,
    'urls_raw': [],
    'identity_notes_raw': (
        'NEEDS_VERIFICATION — township ownership inferred from location in Madison Township; '
        'no official Madison Township website found in OTA roster to confirm directly. '
        'Veterans Memorial documented (hmdb.org/m.asp?m=187750). Address requires confirmation.'
    ),
    'township_raw': None,
    'municipality_raw': None,
    'discovery_tier': 5,
    'seeded_from_baseline': False,
    'baseline_id': None
})

# --- Rice Township --- (5 cemeteries listed on township website)

for cem_name in ['Briar Hill Cemetery', 'Greenwood Cemetery', 'Hineline Cemetery', 'LaPrairie Cemetery']:
    data['records'].append({
        'entity_type': 'Site',
        'name_raw': cem_name,
        'counties_raw': ['Sandusky'],
        'county_primary': 'Sandusky',
        'ownership_raw': 'Rice Township',
        'governance_raw': 'Rice Township',
        'partner_agencies_raw': None,
        'coordination_raw': None,
        'gps_lat_raw': None,
        'gps_lon_raw': None,
        'location_raw': 'Rice Township, Sandusky County OH',
        'description_raw': None,
        'features_raw': 'Active cemetery',
        'difficulty_raw': None,
        'accessibility_raw': None,
        'urls_raw': ['http://ricetownship.com/cemeteries/'],
        'identity_notes_raw': (
            'Township-managed cemetery listed on Rice Township official website. '
            'MINIMAL_DATA — no street address confirmed from web sources; field verification required.'
        ),
        'township_raw': None,
        'municipality_raw': None,
        'discovery_tier': 5,
        'seeded_from_baseline': False,
        'baseline_id': None
    })

data['records'].append({
    'entity_type': 'Site',
    'name_raw': 'Faith Lutheran Cemetery',
    'counties_raw': ['Sandusky'],
    'county_primary': 'Sandusky',
    'ownership_raw': 'Rice Township',
    'governance_raw': 'Rice Township',
    'partner_agencies_raw': None,
    'coordination_raw': None,
    'gps_lat_raw': None,
    'gps_lon_raw': None,
    'location_raw': 'Rice Township, Sandusky County OH',
    'description_raw': None,
    'features_raw': 'Active cemetery',
    'difficulty_raw': None,
    'accessibility_raw': None,
    'urls_raw': ['http://ricetownship.com/cemeteries/'],
    'identity_notes_raw': (
        'Listed on Rice Township official website. Name suggests possible Lutheran church origin; '
        'current management by Rice Township trustees. MINIMAL_DATA — address requires field verification. '
        'NEEDS_VERIFICATION — confirm township vs. private church ownership if church congregation still active.'
    ),
    'township_raw': None,
    'municipality_raw': None,
    'discovery_tier': 5,
    'seeded_from_baseline': False,
    'baseline_id': None
})

# --- Riley Township --- (4 cemeteries from website with addresses)

riley_cems = [
    ('Beeler Cemetery', '363-369 N Erlin Road, Fremont, OH 43420'),
    ('Faust Cemetery', '1800-1828 US Route 6, Fremont, OH 43420'),
    ('Schoch Cemetery', 'County Road 233, Fremont, OH 43420'),
]
for name, addr in riley_cems:
    data['records'].append({
        'entity_type': 'Site',
        'name_raw': name,
        'counties_raw': ['Sandusky'],
        'county_primary': 'Sandusky',
        'ownership_raw': 'Riley Township',
        'governance_raw': 'Riley Township',
        'partner_agencies_raw': None,
        'coordination_raw': None,
        'gps_lat_raw': None,
        'gps_lon_raw': None,
        'location_raw': addr,
        'description_raw': None,
        'features_raw': 'Active cemetery',
        'difficulty_raw': None,
        'accessibility_raw': None,
        'urls_raw': ['https://www.rileytownship.org/cemeteries/locations'],
        'identity_notes_raw': 'Township-managed cemetery per Riley Township official website. Address confirmed from website.',
        'township_raw': None,
        'municipality_raw': None,
        'discovery_tier': 5,
        'seeded_from_baseline': False,
        'baseline_id': None
    })

data['records'].append({
    'entity_type': 'Site',
    'name_raw': 'Green Creek Burial Ground',
    'counties_raw': ['Sandusky'],
    'county_primary': 'Sandusky',
    'ownership_raw': 'Riley Township',
    'governance_raw': 'Riley Township',
    'partner_agencies_raw': None,
    'coordination_raw': None,
    'gps_lat_raw': None,
    'gps_lon_raw': None,
    'location_raw': 'County Road 265, Fremont, OH 43420 (Riley Township)',
    'description_raw': None,
    'features_raw': 'Active cemetery',
    'difficulty_raw': None,
    'accessibility_raw': None,
    'urls_raw': ['https://www.rileytownship.org/cemeteries/locations'],
    'identity_notes_raw': (
        'Also known as Gibbs Cemetery. Township-managed per Riley Township website. '
        'Located in Riley Township (not Green Creek Township despite the name).'
    ),
    'township_raw': None,
    'municipality_raw': None,
    'discovery_tier': 5,
    'seeded_from_baseline': False,
    'baseline_id': None
})

f.write_text(yaml.dump(data, allow_unicode=True, sort_keys=False), encoding='utf-8')
print(f'T5 cemeteries A staged. Total records: {len(data["records"])}')
