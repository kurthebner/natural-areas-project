import yaml, pathlib

f = pathlib.Path('County_Spreadsheets/Sandusky/sandusky_ohio_raw_discovery.yaml')
data = yaml.safe_load(f.read_text(encoding='utf-8'))
data.setdefault('records', [])

# Darr-Root Fishing Access — T2 ODNR miss discovered during T4 review
# ODNR-managed public boat ramp on Sandusky River at Fremont; donated by Darr and Root families
data['records'].append({
    'entity_type': 'Access Point',
    'name_raw': 'Darr-Root Fishing Access',
    'counties_raw': ['Sandusky'],
    'county_primary': 'Sandusky',
    'ownership_raw': 'State of Ohio',
    'governance_raw': 'Ohio Department of Natural Resources',
    'partner_agencies_raw': None,
    'coordination_raw': None,
    'gps_lat_raw': None,
    'gps_lon_raw': None,
    'location_raw': '201 Walnut Street, Fremont, OH — on the Sandusky River',
    'description_raw': (
        "Fremont's first ODNR public boat ramp on the Sandusky River. Land donated by the "
        "Darr and Root families (named after Don and Violet Darr and Hob and Anne Root). "
        'Features truck-and-trailer parking and easy river access. Developed in collaboration '
        'with county and city officials. Access point to the Sandusky Scenic River.'
    ),
    'features_raw': 'Boat ramp; Parking (truck/trailer); River access; Fishing',
    'difficulty_raw': None,
    'accessibility_raw': None,
    'urls_raw': ['https://www.sanduskycounty.org/fishing'],
    'identity_notes_raw': (
        'T2 miss — ODNR-managed access point discovered during T4 CVB fishing-page review. '
        'Serves as access point for the Sandusky Scenic River (Sandusky River ODNR scenic '
        'river designation). Baseline seed "Fremont Boat Ramp" likely refers to this site '
        'or the adjacent Sand Docks (City of Fremont). Upper Sandusky Reservoir #1 '
        'association in baseline seed is incorrect — that reservoir is in Wyandot County.'
    ),
    'township_raw': None,
    'municipality_raw': None,
    'discovery_tier': 2,
    'seeded_from_baseline': True,
    'baseline_id': 'Fremont Boat Ramp'
})

f.write_text(yaml.dump(data, allow_unicode=True, sort_keys=False), encoding='utf-8')
print(f'T2 miss staged. Total records: {len(data["records"])}')
