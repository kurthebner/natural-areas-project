import yaml, pathlib

f = pathlib.Path('County_Spreadsheets/Sandusky/sandusky_ohio_raw_discovery.yaml')
data = yaml.safe_load(f.read_text(encoding='utf-8'))
data.setdefault('records', [])

# --- WR Hunt Club (private hunting/sporting preserve) ---
data['records'].append({
    'entity_type': 'Site',
    'name_raw': 'WR Hunt Club',
    'counties_raw': ['Sandusky'],
    'county_primary': 'Sandusky',
    'ownership_raw': 'WR Hunt Club (private — Wright/Gardner family)',
    'governance_raw': 'WR Hunt Club',
    'partner_agencies_raw': None,
    'coordination_raw': None,
    'gps_lat_raw': None,
    'gps_lon_raw': None,
    'location_raw': '5690 County Road 237, Clyde, OH 43410',
    'description_raw': (
        'Private membership-based hunting and sporting preserve near Clyde. '
        'Founded 1985 by Bob and Betty Wright; currently managed by grandson Jamie Gardner. '
        'Offers pheasant and chukar hunting, 5-stand sporting clays with 40-foot tower, '
        'and overnight accommodations. Also operates as a wedding venue and banquet hall.'
    ),
    'features_raw': 'Hunting (pheasant, chukar); 5-stand sporting clays; Clay tower (40 ft); Overnight accommodations; Banquet/event venue; Pro shop',
    'difficulty_raw': None,
    'accessibility_raw': None,
    'urls_raw': ['https://wrhuntclub.com/'],
    'identity_notes_raw': (
        'Private membership-based hunting preserve. Application/membership required for hunting access. '
        'Limited-access per §4.1. Founded 1985. Source: wrhuntclub.com'
    ),
    'township_raw': None,
    'municipality_raw': None,
    'discovery_tier': 8,
    'seeded_from_baseline': False,
    'baseline_id': None,
})

# --- Schedel Arboretum and Gardens (cross-county Ottawa/Sandusky — GIS_VERIFY) ---
data['records'].append({
    'entity_type': 'Site',
    'name_raw': 'Schedel Arboretum and Gardens',
    'counties_raw': ['Ottawa', 'Sandusky'],
    'county_primary': 'Ottawa',
    'ownership_raw': 'Joseph J. & Marie P. Schedel Foundation (private nonprofit)',
    'governance_raw': 'Joseph J. & Marie P. Schedel Foundation',
    'partner_agencies_raw': None,
    'coordination_raw': None,
    'gps_lat_raw': None,
    'gps_lon_raw': None,
    'location_raw': '19255 W. Portage River South Road, Elmore, OH 43416',
    'description_raw': (
        'Private nonprofit arboretum and gardens established by the Joseph J. and Marie P. Schedel '
        'Foundation in 1963. Approximately 100 acres along the Portage River. Features a Japanese '
        'garden, rose garden, tropical garden, bonsai collection, 25 Japanese maple varieties, '
        '16 pine species, English landscape areas, and sculpture installations. '
        'Also houses the Blair Museum of Lithophanes (relocated 2021; world\'s largest collection '
        'of lithophanes). Greenhouse produces approximately 15,000 plants per year. '
        'Open April–October; admission fee charged.'
    ),
    'features_raw': 'Japanese garden; Rose garden; Tropical garden; Bonsai collection; Sculpture installations; Lithophane museum; Greenhouse; Reception center',
    'difficulty_raw': None,
    'accessibility_raw': None,
    'urls_raw': ['https://www.schedel-gardens.org/'],
    'identity_notes_raw': (
        'GIS_VERIFY_COUNTY — Elmore straddles Ottawa and Sandusky counties; parcel at '
        '19255 W. Portage River South Rd is likely Ottawa County primary per geographic analysis, '
        'but Sandusky County CVB also claims it. GIS parcel lookup required. '
        'county_primary set to Ottawa pending verification. CROSS_COUNTY_CANDIDATE. '
        'Private nonprofit foundation (est. 1963). Seasonal public access with admission fee. '
        'Source: schedel-gardens.org'
    ),
    'township_raw': None,
    'municipality_raw': None,
    'discovery_tier': 8,
    'seeded_from_baseline': False,
    'baseline_id': None,
})

# --- County Home Cemetery (T4 miss — government burial ground) ---
# County Home/Infirmary cemeteries are county-government-managed burial grounds
# for county home (poor farm) residents. This is a T4 miss, staged here for correction.
data['records'].append({
    'entity_type': 'Site',
    'name_raw': 'County Home Cemetery',
    'counties_raw': ['Sandusky'],
    'county_primary': 'Sandusky',
    'ownership_raw': 'Sandusky County (inferred)',
    'governance_raw': 'Sandusky County (inferred)',
    'partner_agencies_raw': None,
    'coordination_raw': None,
    'gps_lat_raw': None,
    'gps_lon_raw': None,
    'location_raw': 'Sandusky County, OH (location unconfirmed — GNIS-sourced)',
    'description_raw': (
        'Cemetery associated with the former Sandusky County Home (county infirmary/poor farm). '
        'County home cemeteries are historically county-government-managed burial grounds '
        'for residents of the county infirmary who died without private burial arrangements.'
    ),
    'features_raw': 'Historic county home burial ground',
    'difficulty_raw': None,
    'accessibility_raw': None,
    'urls_raw': [],
    'identity_notes_raw': (
        'T4 MISS — staged at T8 pending governance verification. '
        'County Home cemeteries are typically county-government-managed (T4). '
        'NEEDS_VERIFICATION — confirm county ownership vs. historical association or private management. '
        'GIS_VERIFY location — GNIS-only, no street address confirmed. '
        'Source: OhioGenealogyExpress sandusky county cemetery list.'
    ),
    'township_raw': None,
    'municipality_raw': None,
    'discovery_tier': 8,
    'seeded_from_baseline': False,
    'baseline_id': None,
})

# --- Old Fremont Cemetery (governance unknown — GNIS-only) ---
data['records'].append({
    'entity_type': 'Site',
    'name_raw': 'Old Fremont Cemetery',
    'counties_raw': ['Sandusky'],
    'county_primary': 'Sandusky',
    'ownership_raw': 'Unknown',
    'governance_raw': 'Unknown',
    'partner_agencies_raw': None,
    'coordination_raw': None,
    'gps_lat_raw': None,
    'gps_lon_raw': None,
    'location_raw': 'Fremont area, Sandusky County, OH (location unconfirmed — GNIS-sourced)',
    'description_raw': None,
    'features_raw': None,
    'difficulty_raw': None,
    'accessibility_raw': None,
    'urls_raw': [],
    'identity_notes_raw': (
        'GNIS-only — active status unconfirmed; verify before upsert. '
        'Governance unknown — may be City of Fremont-managed (T6), historical association, '
        'or absorbed into another cemetery. No corroborating web source found. '
        'Source: OhioGenealogyExpress sandusky county cemetery list.'
    ),
    'township_raw': None,
    'municipality_raw': None,
    'discovery_tier': 8,
    'seeded_from_baseline': False,
    'baseline_id': None,
})

# --- Green Springs Cemetery (possible T6 miss — village-managed) ---
data['records'].append({
    'entity_type': 'Site',
    'name_raw': 'Green Springs Cemetery',
    'counties_raw': ['Sandusky', 'Seneca'],
    'county_primary': 'Sandusky',
    'ownership_raw': 'Village of Green Springs (inferred)',
    'governance_raw': 'Village of Green Springs (inferred)',
    'partner_agencies_raw': None,
    'coordination_raw': None,
    'gps_lat_raw': None,
    'gps_lon_raw': None,
    'location_raw': 'Green Springs, Sandusky/Seneca County, OH (location unconfirmed — GNIS-sourced)',
    'description_raw': None,
    'features_raw': 'Active cemetery (assumed)',
    'difficulty_raw': None,
    'accessibility_raw': None,
    'urls_raw': [],
    'identity_notes_raw': (
        'T6 MISS (possible) — staged at T8 pending governance verification. '
        'Green Springs Cemetery is likely village-managed by the Village of Green Springs (T6). '
        'NEEDS_VERIFICATION — confirm village vs. church vs. private ownership. '
        'GIS_VERIFY_COUNTY — Green Springs straddles Sandusky and Seneca counties; '
        'confirm which county the cemetery parcel is in. '
        'Source: OhioGenealogyExpress sandusky county cemetery list.'
    ),
    'township_raw': None,
    'municipality_raw': None,
    'discovery_tier': 8,
    'seeded_from_baseline': False,
    'baseline_id': None,
})

f.write_text(yaml.dump(data, allow_unicode=True, sort_keys=False), encoding='utf-8')
print(f'T8 private sites staged. Total records: {len(data["records"])}')
