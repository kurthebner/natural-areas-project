import yaml, pathlib

f = pathlib.Path(r'D:\users\user1\Documents\CP Projects\Natural Areas Project v6\County Spreadsheets\Hardin\hardin_ohio_raw_discovery.yaml')
data = yaml.safe_load(f.read_text(encoding='utf-8'))

t3_records = [

# --- T3 SITE 1: Hardin County Veterans Memorial Park ---
{
    'entity_type': 'Site',
    'name_raw': 'Hardin County Veterans Memorial Park',
    'counties_raw': ['Hardin'],
    'county_primary': 'Hardin',
    'ownership_raw': 'Hardin County Veterans Memorial Park District',
    'governance_raw': 'Board of Park Commissioners, Hardin County Veterans Memorial Park District',
    'partner_agencies_raw': None,
    'coordination_raw': None,
    'description_raw': (
        '26-acre county park district property centered on Boy Scout Lake (4.1 acres). '
        'Created July 30, 1946 by order of the Hardin County Probate Court; governed by '
        'Board of Park Commissioners appointed by the Probate Judge. District covers '
        'Buck, Cessna, Goshen, Lynn, Pleasant, and Washington Townships plus the City '
        'of Kenton. Features a 4.1-acre fishing lake (no license required), paved '
        'walking path, dog run, children\'s playground, and three shelter houses. '
        'Entirely handicap accessible. First paved walking path segment completed 2009.'
    ),
    'habitat_type_raw': None,
    'features_raw': (
        'Boy Scout Lake (4.1 acres, fishing); paved walking path; dog run area; '
        'children\'s playground (swings, slides, jungle gym); three shelter houses with '
        'power outlets; charcoal grills; two full basketball courts; three parking lots; '
        'handicap accessible; no license required for fishing'
    ),
    'access_notes_raw': None,
    'location_raw': '15906 OH-309, Kenton, OH 43326',
    'acres_raw': '26',
    'gps_lat_raw': '40.6470',
    'gps_lon_raw': '-83.6095',
    'boundary_document_raw': None,
    'urls_raw': ['https://hardinvetspark.org/'],
    'ebird_hotspot_id': None,
    'identity_notes_raw': (
        'Statutory park district (T3) under ORC. Board of Park Commissioners appointed '
        'by Hardin County Probate Judge. Not a county-managed park (T4). District '
        'created 1946.'
    ),
    'township_raw': None,
    'municipality_raw': None,
    'last_verified_date': '2026-06-01',
    'field_verified': False,
    'discovery_tier': 3,
    'seeded_from_baseline': True,
    'baseline_id': 'Hardin County Veterans Memorial Park',
},

# --- T3 CHILD SITE: Boy Scout Lake ---
{
    'entity_type': 'Site',
    'name_raw': 'Boy Scout Lake',
    'counties_raw': ['Hardin'],
    'county_primary': 'Hardin',
    'ownership_raw': 'Hardin County Veterans Memorial Park District',
    'governance_raw': 'Board of Park Commissioners, Hardin County Veterans Memorial Park District',
    'partner_agencies_raw': None,
    'coordination_raw': None,
    'description_raw': (
        '4.1-acre lake within Hardin County Veterans Memorial Park. Named "Boy Scout Lake" '
        'from original plans for a boys\' camp. Primary fishing feature of the park — no '
        'fishing license required. Shelter house located at the north end. '
        'Walking path circles the lake.'
    ),
    'habitat_type_raw': 'Pond/lake; park setting',
    'features_raw': 'Fishing (no license required); shelter house at north end; paved walking path; fishing access',
    'access_notes_raw': None,
    'location_raw': 'Within Hardin County Veterans Memorial Park, 15906 OH-309, Kenton, OH 43326',
    'acres_raw': '4.1',
    'gps_lat_raw': '40.6470',
    'gps_lon_raw': '-83.6095',
    'boundary_document_raw': None,
    'urls_raw': ['https://hardinvetspark.org/'],
    'ebird_hotspot_id': None,
    'identity_notes_raw': 'Child site of Hardin County Veterans Memorial Park. Named feature with distinct recreational identity (fishing, shelter house, lake circuit trail).',
    'township_raw': None,
    'municipality_raw': None,
    'last_verified_date': '2026-06-01',
    'field_verified': False,
    'discovery_tier': 3,
    'seeded_from_baseline': True,
    'baseline_id': 'Boy Scout Lake',
},

# --- T3 SITE 2: Silver Creek Center for Environmental Studies ---
{
    'entity_type': 'Site',
    'name_raw': 'Silver Creek Center for Environmental Studies',
    'counties_raw': ['Hardin'],
    'county_primary': 'Hardin',
    'ownership_raw': 'Hardin Soil and Water Conservation District',
    'governance_raw': 'Hardin Soil and Water Conservation District',
    'partner_agencies_raw': None,
    'coordination_raw': None,
    'description_raw': (
        '25-acre educational and natural area managed by the Hardin SWCD on the north side '
        'of State Route 67 approximately 2-3 miles west of Kenton. Features a wooded area '
        'with paved handicap-accessible trail leading to a small wetland with bridge access. '
        'Mowed walking paths continue beyond the wetland to a shelter house and throughout '
        'the property. Self-guided nature trail with markers identifying trees and plants. '
        'Scenic woodlands, meadow, and streamlet. Used for environmental education '
        '(4-H groups, school programs). Named for Silver Creek which flows through '
        'or near the property.'
    ),
    'habitat_type_raw': 'Wooded upland; small wetland; meadow; streamlet',
    'features_raw': (
        'Paved handicap-accessible trail; small wetland with bridge; mowed walking paths; '
        'shelter house; self-guided nature trail with interpretive markers; no restrooms; '
        'educational programming available'
    ),
    'access_notes_raw': (
        'Open to groups and families. Group visits require reservations; contact SWCD '
        'at (419) 673-0456. No restrooms. Educational programming available for groups.'
    ),
    'location_raw': '12525 State Route 67W, Kenton, OH 43326; on north side of SR-67, 2-3 miles west of Kenton',
    'acres_raw': '25',
    'gps_lat_raw': '40.625433',
    'gps_lon_raw': '-83.649567',
    'boundary_document_raw': None,
    'urls_raw': [
        'https://hardincountyohio.gov/swcd-silver-creek-environmental-center/',
    ],
    'ebird_hotspot_id': None,
    'identity_notes_raw': 'SWCD-managed natural area; T3 per IMP-004 (Soil & Water Conservation Districts under ORC Chapter 1515). Not in baseline; discovered via TrekOhio overview page.',
    'township_raw': None,
    'municipality_raw': None,
    'last_verified_date': '2026-06-01',
    'field_verified': False,
    'discovery_tier': 3,
    'seeded_from_baseline': False,
    'baseline_id': None,
},

# --- T3 TRAILTHING 1: Veterans Memorial Park Walking Path ---
{
    'entity_type': 'Trailthing',
    'name_raw': 'Veterans Memorial Park Walking Path',
    'source_term_raw': 'paved walking path',
    'source_hierarchy_context_raw': 'Described as a paved walking path within Hardin County Veterans Memorial Park; circles Boy Scout Lake; first half completed in 2009; listed under park amenities alongside walking paths',
    'counties_raw': ['Hardin'],
    'county_primary': 'Hardin',
    'parent_id_raw': None,
    'site_parent_raw': 'Hardin County Veterans Memorial Park',
    'parent_site_network_raw': None,
    'member_trailthing_names_raw': None,
    'ownership_raw': 'Hardin County Veterans Memorial Park District',
    'governance_raw': 'Board of Park Commissioners, Hardin County Veterans Memorial Park District',
    'partner_agencies_raw': None,
    'coordination_raw': None,
    'description_raw': 'Paved walking path within the Veterans Memorial Park, circling Boy Scout Lake. First half of path completed in 2009 along with dog park construction. Baseline notes fitness stations and benches along route.',
    'use_type_raw': 'Walking',
    'surface_type_raw': 'Paved',
    'origin_type_raw': None,
    'status_raw': 'Open',
    'difficulty_raw': None,
    'accessibility_raw': 'Paved; park described as entirely handicap accessible',
    'total_length_raw': None,
    'urls_raw': ['https://hardinvetspark.org/'],
    'maps_raw': [],
    'identity_notes_raw': 'Baseline entry "Hardin County Veterans Memorial Park Trail" describes this as a walking trail around Boy Scout Lake with fitness stations and benches.',
    'last_verified_date': '2026-06-01',
    'field_verified': False,
    'discovery_tier': 3,
    'seeded_from_baseline': True,
    'baseline_id': 'Hardin County Veterans Memorial Park Trail',
},

# --- T3 TRAILTHING 2: Silver Creek Paved Trail ---
{
    'entity_type': 'Trailthing',
    'name_raw': 'Silver Creek Paved Trail',
    'source_term_raw': 'paved handicap trail',
    'source_hierarchy_context_raw': 'Described as a paved handicap trail through a wooded area leading to a small wetland with bridge access; part of the Silver Creek Center trail system; mowed walking paths continue beyond the paved section',
    'counties_raw': ['Hardin'],
    'county_primary': 'Hardin',
    'parent_id_raw': None,
    'site_parent_raw': 'Silver Creek Center for Environmental Studies',
    'parent_site_network_raw': None,
    'member_trailthing_names_raw': None,
    'ownership_raw': 'Hardin Soil and Water Conservation District',
    'governance_raw': 'Hardin Soil and Water Conservation District',
    'partner_agencies_raw': None,
    'coordination_raw': None,
    'description_raw': 'Paved handicap-accessible trail at the Silver Creek Center for Environmental Studies. Leads through wooded area to a small wetland with bridge. Primary accessible route for the nature center; connects to mowed paths throughout the property.',
    'use_type_raw': 'Walking; nature education',
    'surface_type_raw': 'Paved; mowed paths',
    'origin_type_raw': None,
    'status_raw': 'Open',
    'difficulty_raw': None,
    'accessibility_raw': 'ADA accessible (paved handicap trail)',
    'total_length_raw': None,
    'urls_raw': ['https://hardincountyohio.gov/swcd-silver-creek-environmental-center/'],
    'maps_raw': [],
    'identity_notes_raw': 'Trail map available on SWCD website (front and back of Silver Creek sections). Mowed paths extend beyond paved section; treat as part of same trail system.',
    'last_verified_date': '2026-06-01',
    'field_verified': False,
    'discovery_tier': 3,
    'seeded_from_baseline': False,
    'baseline_id': None,
},

# --- T3 SITE NETWORKS: NULL ---
{
    'entity_type_result': {
        'tier': 3,
        'governance_level': 'District',
        'entity_type': 'Site Network',
        'result': 'null',
        'sources_checked': [
            'Hardin County Veterans Memorial Park District — single site; Rule 2 threshold (2+ member sites) not met',
            'Hardin SWCD — single site (Silver Creek Center); threshold not met',
            'Maumee Watershed Conservancy District — flood control only; no recreation lands in Hardin County',
            'Upper Scioto Drainage and Conservancy District — river maintenance/drainage only; no recreation lands',
        ],
        'reasoning': 'No T3 district manages multiple natural area Sites in Hardin County. All four T3 districts confirmed; none meet Site Network threshold.',
    }
},

# --- T3 ACCESS POINT 1: Veterans Memorial Park Entrance ---
{
    'entity_type': 'Access Point',
    'name_raw': 'Hardin County Veterans Memorial Park Main Entrance',
    'counties_raw': ['Hardin'],
    'county_primary': 'Hardin',
    'parent_sites_raw': ['Hardin County Veterans Memorial Park'],
    'parent_trailthings_raw': ['Veterans Memorial Park Walking Path'],
    'governance_raw': 'Board of Park Commissioners, Hardin County Veterans Memorial Park District',
    'description_raw': 'Primary entrance and parking area for Veterans Memorial Park on OH-309. Access to Boy Scout Lake, dog run, playground, shelter houses, and paved walking path.',
    'features_raw': 'Three parking lots; fishing lake access; dog run; playground; shelter houses; walking path trailhead',
    'location_raw': '15906 OH-309, Kenton, OH 43326',
    'gps_lat_raw': '40.6470',
    'gps_lon_raw': '-83.6095',
    'urls_raw': ['https://hardinvetspark.org/'],
    'identity_notes_raw': None,
    'last_verified_date': '2026-06-01',
    'field_verified': False,
    'discovery_tier': 3,
    'seeded_from_baseline': False,
    'baseline_id': None,
},

# --- T3 ACCESS POINT 2: Silver Creek Center Entrance ---
{
    'entity_type': 'Access Point',
    'name_raw': 'Silver Creek Center for Environmental Studies Entrance',
    'counties_raw': ['Hardin'],
    'county_primary': 'Hardin',
    'parent_sites_raw': ['Silver Creek Center for Environmental Studies'],
    'parent_trailthings_raw': ['Silver Creek Paved Trail'],
    'governance_raw': 'Hardin Soil and Water Conservation District',
    'description_raw': 'Entrance and parking area for Silver Creek Center on SR-67W west of Kenton. Turn right at Silver Creek Environmental Center sign just beyond the bridge. Trailhead for paved accessible trail and mowed paths.',
    'features_raw': 'Parking; paved trail trailhead; no restrooms; group use by reservation',
    'location_raw': '12525 State Route 67W, Kenton, OH 43326; just beyond bridge on SR-67W heading west',
    'gps_lat_raw': '40.625433',
    'gps_lon_raw': '-83.649567',
    'urls_raw': ['https://hardincountyohio.gov/swcd-silver-creek-environmental-center/'],
    'identity_notes_raw': None,
    'last_verified_date': '2026-06-01',
    'field_verified': False,
    'discovery_tier': 3,
    'seeded_from_baseline': False,
    'baseline_id': None,
},

# --- T3 NULL DOCUMENTATION ---
{
    'entity_type_result': {
        'tier': 3,
        'governance_level': 'District — Pre-Enumeration and Null Sources',
        'entity_type': 'Multiple',
        'result': 'null_items_documented',
        'ohio_auditor_canvass': {
            'date': '2026-06-01',
            'url': 'https://www.auditor.state.oh.us/AuditSearch/Entities',
            'note': 'Ohio Auditor entity search website returned error page; pre-enumeration completed via alternative sources (park website, SWCD website, WebSearch, audit report citations)',
            'county_filter': 'Hardin',
            'entity_types_searched': [
                'Park Districts',
                'Joint Recreation Districts',
                'Conservancy Districts',
                'Watershed Districts',
                'Soil and Water Conservation Districts',
                'Special Districts',
            ],
            'entities_found': [
                'Hardin County Veterans Memorial Park District (park district; statutory under ORC; Board of Park Commissioners)',
                'Hardin Soil and Water Conservation District (SWCD; ORC Chapter 1515)',
                'Maumee Watershed Conservancy District (multi-county conservancy district; ORC 6101; 15 counties including Hardin)',
                'Upper Scioto Drainage and Conservancy District (drainage/conservancy district; Hardin County; formed 1915)',
                'Kenton-Hardin General Health District (health district; not recreation/natural areas)',
            ],
            'web_dark_districts': 'None — all four relevant districts have web presence or audit documentation',
        },
        'null_items': [
            'Maumee Watershed Conservancy District — flood control and drainage projects only; no recreation lands or natural area Sites in Hardin County',
            'Upper Scioto Drainage and Conservancy District — river maintenance only (log jam removal, bank maintenance); no recreation access or natural area Sites',
            'Kenton-Hardin General Health District — health services; not a park/conservation entity',
            'No joint recreation districts found in Hardin County',
            'No metroparks system in Hardin County',
        ],
        'sources_checked': [
            'hardinvetspark.org',
            'hardincountyohio.gov/swcd-about/',
            'hardincountyohio.gov/swcd-silver-creek-environmental-center/',
            'sites.google.com/view/usdcd',
            'maumeewatershed.com',
            'trekohio.com/hardin/',
            'ohioauditor.gov — audit reports for Upper Scioto DCD and Kenton-Hardin Health District',
            'agri.ohio.gov/divisions/soil-and-water-conservation',
        ],
    }
},

]

data.setdefault('records', [])
data['records'].extend(t3_records)
f.write_text(yaml.dump(data, allow_unicode=True, sort_keys=False, default_flow_style=False), encoding='utf-8')
print(f'Total records now: {len(data["records"])}')
