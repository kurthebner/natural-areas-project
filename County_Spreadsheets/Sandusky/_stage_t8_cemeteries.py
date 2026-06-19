import yaml, pathlib

f = pathlib.Path('County_Spreadsheets/Sandusky/sandusky_ohio_raw_discovery.yaml')
data = yaml.safe_load(f.read_text(encoding='utf-8'))
data.setdefault('records', [])

BASE_NOTES_GNIS = 'GNIS-only — active status unconfirmed; address and details require field verification. Source: OhioGenealogyExpress sandusky county cemetery list.'
BASE_URL = 'https://ohiogenealogyexpress.com/sandusky/sanduskyco_cems.htm'

# --- Church Cemeteries (T8) ---

church_cems = [
    ('Reformed Church Cemetery', 'Bellevue area, Sandusky/Huron County OH',
     'Reformed Church congregation-affiliated cemetery in the Bellevue area. GIS_VERIFY_COUNTY — Bellevue straddles Sandusky and Huron counties.',
     ['Sandusky', 'Huron'], 'Sandusky',
     BASE_NOTES_GNIS + ' GIS_VERIFY_COUNTY — Bellevue straddles Sandusky and Huron counties. CROSS_COUNTY_CANDIDATE.'),
    ('Saint Ann\'s Cemetery', 'Sandusky County, OH', None, ['Sandusky'], 'Sandusky', BASE_NOTES_GNIS),
    ('Saint Joseph\'s Cemetery', 'Sandusky County, OH', None, ['Sandusky'], 'Sandusky', BASE_NOTES_GNIS),
    ('Saint Lawrence Cemetery', 'Sandusky County, OH', None, ['Sandusky'], 'Sandusky', BASE_NOTES_GNIS),
    ('Saint Mary\'s Cemetery', 'Sandusky County, OH', None, ['Sandusky'], 'Sandusky',
     BASE_NOTES_GNIS + ' Multiple entries on GNIS list — likely distinct parishes (Fremont, Clyde, or other municipalities). Verify locations; may warrant multiple separate records.'),
    ('Saint Paul\'s Cemetery', 'Sandusky County, OH', None, ['Sandusky'], 'Sandusky', BASE_NOTES_GNIS),
    ('Saint Philomena Cemetery', 'Sandusky County, OH', None, ['Sandusky'], 'Sandusky', BASE_NOTES_GNIS),
    ('Mount Lebanon Cemetery', 'Sandusky County, OH', None, ['Sandusky'], 'Sandusky',
     BASE_NOTES_GNIS + ' Likely church-affiliated (Mount Lebanon is a common church/congregation cemetery name).'),
    ('Trinity Cemetery', 'Sandusky County, OH', None, ['Sandusky'], 'Sandusky',
     BASE_NOTES_GNIS + ' Multiple entries on GNIS list — may be two distinct locations. Verify before upsert.'),
    ('North Union Cemetery', 'Sandusky County, OH', None, ['Sandusky'], 'Sandusky',
     BASE_NOTES_GNIS + ' May be church or community cemetery. Governance requires field verification.'),
]

for name, addr, desc, counties, county_primary, notes in church_cems:
    data['records'].append({
        'entity_type': 'Site',
        'name_raw': name,
        'counties_raw': counties,
        'county_primary': county_primary,
        'ownership_raw': 'Church/Religious organization (inferred from name)',
        'governance_raw': 'Church/Religious organization (inferred)',
        'partner_agencies_raw': None,
        'coordination_raw': None,
        'gps_lat_raw': None,
        'gps_lon_raw': None,
        'location_raw': addr,
        'description_raw': desc,
        'features_raw': 'Cemetery',
        'difficulty_raw': None,
        'accessibility_raw': None,
        'urls_raw': [BASE_URL],
        'identity_notes_raw': notes,
        'township_raw': None,
        'municipality_raw': None,
        'discovery_tier': 8,
        'seeded_from_baseline': False,
        'baseline_id': None,
    })

# --- Commercial Cemetery (T8) ---

data['records'].append({
    'entity_type': 'Site',
    'name_raw': 'Greenlawn Memory Gardens',
    'counties_raw': ['Sandusky'],
    'county_primary': 'Sandusky',
    'ownership_raw': 'Private (commercial cemetery — operator unconfirmed)',
    'governance_raw': 'Greenlawn Memory Gardens (private)',
    'partner_agencies_raw': None,
    'coordination_raw': None,
    'gps_lat_raw': None,
    'gps_lon_raw': None,
    'location_raw': 'Sandusky County, OH (location unconfirmed — GNIS-sourced)',
    'description_raw': None,
    'features_raw': 'Cemetery',
    'difficulty_raw': None,
    'accessibility_raw': None,
    'urls_raw': [BASE_URL],
    'identity_notes_raw': (
        'Commercial/for-profit cemetery inferred from "Memory Gardens" naming convention. '
        + BASE_NOTES_GNIS
    ),
    'township_raw': None,
    'municipality_raw': None,
    'discovery_tier': 8,
    'seeded_from_baseline': False,
    'baseline_id': None,
})

# --- Family Cemeteries (T8) ---

family_cems = [
    'Bakertown Cemetery',
    'Bowlus Cemetery',
    'Collins Cemetery',
    'Colwell Cemetery',
    'Dana Cemetery',
    'Decker Cemetery',
    'Fuller Cemetery',
    'Halters Cemetery',
    'Hayes Cemetery',
    'Hill Cemetery',
    'Hite Cemetery',
    'Lathrop Cemetery',
    'Ludwig Cemetery',
    'McCreary Farm Cemetery',
    'McGormley Cemetery',
    'Metzgar Cemetery',
    'Overmyer Cemetery',
    'Pember Farm Cemetery',
    'Quinshan Cemetery',
    'Shawl Cemetery',
    'Whittlesey Cemetery',
]

for name in family_cems:
    extra = ''
    if name == 'Bowlus Cemetery':
        extra = ' Multiple entries on GNIS list — may be two distinct locations or duplicate entry. Verify.'
    elif name == 'Hite Cemetery':
        extra = ' Multiple entries on GNIS list — may be two distinct locations or duplicate entry. Verify.'
    elif name in ('McCreary Farm Cemetery', 'Pember Farm Cemetery'):
        extra = ' Explicitly named as a farm cemetery — family/private burial ground on farm property.'
    data['records'].append({
        'entity_type': 'Site',
        'name_raw': name,
        'counties_raw': ['Sandusky'],
        'county_primary': 'Sandusky',
        'ownership_raw': 'Private family or unknown (inferred from name)',
        'governance_raw': 'Private family or unknown',
        'partner_agencies_raw': None,
        'coordination_raw': None,
        'gps_lat_raw': None,
        'gps_lon_raw': None,
        'location_raw': 'Sandusky County, OH (location unconfirmed — GNIS-sourced)',
        'description_raw': None,
        'features_raw': 'Cemetery',
        'difficulty_raw': None,
        'accessibility_raw': None,
        'urls_raw': [BASE_URL],
        'identity_notes_raw': BASE_NOTES_GNIS + extra,
        'township_raw': None,
        'municipality_raw': None,
        'discovery_tier': 8,
        'seeded_from_baseline': False,
        'baseline_id': None,
    })

f.write_text(yaml.dump(data, allow_unicode=True, sort_keys=False), encoding='utf-8')
print(f'T8 cemeteries staged. Total records: {len(data["records"])}')
