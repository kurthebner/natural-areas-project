import yaml, pathlib

f = pathlib.Path(r'D:\users\user1\Documents\CP Projects\Natural Areas Project v6\County Spreadsheets\Hardin\hardin_ohio_raw_discovery.yaml')
data = yaml.safe_load(f.read_text(encoding='utf-8'))

t2_records = [

# --- T2 SITE 1: Lawrence Woods State Nature Preserve ---
{
    'entity_type': 'Site',
    'name_raw': 'Lawrence Woods State Nature Preserve',
    'counties_raw': ['Hardin'],
    'county_primary': 'Hardin',
    'ownership_raw': 'State of Ohio',
    'governance_raw': 'ODNR Division of Natural Areas and Preserves',
    'partner_agencies_raw': None,
    'coordination_raw': None,
    'description_raw': (
        'Largest known mature forest in northwest Ohio; home to numerous rare plant and animal species. '
        'Multiple forest community types depending on elevation: oak-hickory on highest/driest sites grading '
        'to beech-maple, beech-oak-red maple, and maple-ash-oak swamp communities. Large trees of many species '
        'including white, yellow, red, and bur oaks, beech, white ash, shagbark hickory, red maple, sugar maple, '
        'and sycamore. Substantial buttonbush swamps inundated for most of the year. Heart-leaf plantain '
        '(Plantago cordata), an Ohio endangered species known from only three state sites, occurs here. '
        'Excellent for birding and spring wildflowers.'
    ),
    'habitat_type_raw': 'Old-growth/mature upland forest (oak-hickory, beech-maple); buttonbush swamp wetlands; spring wildflower groundlayer',
    'features_raw': '1.1-mile accessible boardwalk; hiking; birding; summer and spring wildflowers; wetlands; woods',
    'access_notes_raw': 'Open 1/2 hour before sunrise to 1/2 hour after sunset. Stay on designated trails. Pets not permitted. No restrooms.',
    'location_raw': '13278 County Road 190, Kenton, OH 43326; approximately 4 miles south of Kenton',
    'acres_raw': '1034.93',
    'gps_lat_raw': '40.6833',
    'gps_lon_raw': '-83.6092',
    'boundary_document_raw': None,
    'urls_raw': [
        'https://ohiodnr.gov/go-and-do/plan-a-visit/find-a-property/lawrence-woods-state-nature-preserve',
        'https://naturepreserves.ohiodnr.gov/lawrencewoods',
    ],
    'ebird_hotspot_id': 'L324903',
    'identity_notes_raw': None,
    'township_raw': None,
    'municipality_raw': None,
    'last_verified_date': '2026-06-01',
    'field_verified': False,
    'discovery_tier': 2,
    'seeded_from_baseline': True,
    'baseline_id': 'Lawrence Woods State Nature Preserve',
},

# --- T2 SITE 2: Lawrence Woods Wildlife Area ---
{
    'entity_type': 'Site',
    'name_raw': 'Lawrence Woods Wildlife Area',
    'counties_raw': ['Hardin', 'Wyandot'],
    'county_primary': 'Hardin',
    'ownership_raw': 'State of Ohio',
    'governance_raw': 'ODNR Division of Wildlife',
    'partner_agencies_raw': None,
    'coordination_raw': None,
    'description_raw': (
        'Wildlife area located on the north side of County Road 190 opposite Lawrence Woods State Nature '
        'Preserve. Adjacent to old-growth forest preserve complex. Includes grassland habitat and upland '
        'fields; ODNR Division of Wildlife grassland bird research conducted at the property (2023). '
        'Wheelchair accessible trail documented. Spans Hardin and Wyandot counties.'
    ),
    'habitat_type_raw': 'Upland grassland; upland fields; adjacent to mature old-growth forest; restored/managed agricultural land',
    'features_raw': 'Hunting; trapping; wildlife viewing; wheelchair accessible trail',
    'access_notes_raw': 'Public hunting and trapping. ODNR website page notes more information coming soon; detailed amenity list not yet published.',
    'location_raw': 'North side of County Road 190 opposite Lawrence Woods State Nature Preserve, near Kenton, Hardin County; also extends into Wyandot County',
    'acres_raw': None,
    'gps_lat_raw': None,
    'gps_lon_raw': None,
    'boundary_document_raw': None,
    'urls_raw': [
        'https://ohiodnr.gov/go-and-do/plan-a-visit/find-a-property/lawrence-woods-wildlife-area',
        'https://dam.assets.ohio.gov/image/upload/ohiodnr.gov/documents/wildlife/wildlife-area-maps/LawrenceWoods.pdf',
    ],
    'ebird_hotspot_id': 'L36417313',
    'identity_notes_raw': (
        'CROSS_COUNTY_CANDIDATE — spans Hardin and Wyandot counties per eBird hotspot county label '
        '(L36417313 labeled Hardin; Wyandot County portion confirmed by location description) and ODNR '
        'research documents. Wyandot County not yet run under v6. Provisional Hardin-prefixed ID; hold '
        'pending Wyandot County pipeline run per Scenario A. Acreage not confirmed — ODNR page says coming soon.'
    ),
    'township_raw': None,
    'municipality_raw': None,
    'last_verified_date': '2026-06-01',
    'field_verified': False,
    'discovery_tier': 2,
    'seeded_from_baseline': True,
    'baseline_id': 'Lawrence Woods Wildlife Area',
},

# --- T2 SITE 3: Andreoff Wildlife Area ---
{
    'entity_type': 'Site',
    'name_raw': 'Andreoff Wildlife Area',
    'counties_raw': ['Hardin', 'Wyandot'],
    'county_primary': 'Hardin',
    'ownership_raw': 'State of Ohio',
    'governance_raw': 'ODNR Division of Wildlife',
    'partner_agencies_raw': 'Ducks Unlimited; Pheasants Forever; U.S. Department of Agriculture (Wetlands Reserve Program); H2Ohio program (Wyandot County portion)',
    'coordination_raw': None,
    'description_raw': (
        'Approximately 861-acre wildlife area spanning Hardin and Wyandot counties. Consists of two Hardin '
        'County tracts (north: 584 acres; south: 135 acres) plus an H2Ohio-funded Wyandot County addition. '
        'All tracts are former agricultural land restored through the USDA Wetlands Reserve Program. Habitat '
        'includes restored wetlands, native warm-season grassland, and a 36-acre woodlot on the south tract. '
        'The northern site is located just south of the village of Forest; the southern site is south of '
        'Kenton adjacent to the Lawrence Woods complex. Dedicated October 5, 2019. Named for Alexander '
        'Andreoff of Pheasants Forever. Both tracts are former agricultural property. The H2Ohio Wyandot '
        'County portion is open to public wildlife viewing, hunting, and trapping.'
    ),
    'habitat_type_raw': 'Restored wetlands; native warm-season grassland/prairie; woodlot (36 acres on south tract)',
    'features_raw': 'Hunting; trapping; wildlife viewing; waterfowl habitat; fishing (possible)',
    'access_notes_raw': 'Two separate Hardin County tracts with different road access points. H2Ohio Wyandot County portion also publicly accessible.',
    'location_raw': (
        'North tract: County Road 205 and Township Road 50, just south of Forest, Hardin County. '
        'South tract: County Road 190 west of OH-292, south of Kenton, Hardin County. '
        'Wyandot County portion: location TBD from Wyandot County run.'
    ),
    'acres_raw': '861 total approximate (584 north Hardin + 135 south Hardin + H2Ohio Wyandot portion TBD)',
    'gps_lat_raw': None,
    'gps_lon_raw': None,
    'boundary_document_raw': None,
    'urls_raw': [
        'https://dam.assets.ohio.gov/image/upload/ohiodnr.gov/documents/wildlife/wildlife-area-maps/AndreoffWA.pdf',
        'https://www.ducks.org/newsroom/conservationists-dedicate-ohios-andreoff-wildlife-area',
        'https://www.facebook.com/ohiodivisionofwildlife/posts/andreoff-wildlife-area-located-in-hardin-county-was-dedicated-on-saturday-oct-5-/2617700738252058/',
    ],
    'ebird_hotspot_id': 'L14044415',
    'identity_notes_raw': (
        'CROSS_COUNTY_CANDIDATE — spans Hardin and Wyandot counties. Hardin County: two tracts '
        '(north 584 acres + south 135 acres). Wyandot County: H2Ohio-funded addition, size TBD. '
        'Wyandot County not yet run under v6. Provisional Hardin-prefixed ID; hold pending Wyandot '
        'County pipeline run per Scenario A. eBird hotspot L12331122 is labeled Wyandot Co. and is '
        '1.6 miles from the Hardin Co. Rd. 205 hotspot, confirming cross-county extent.'
    ),
    'township_raw': None,
    'municipality_raw': None,
    'last_verified_date': '2026-06-01',
    'field_verified': False,
    'discovery_tier': 2,
    'seeded_from_baseline': False,
    'baseline_id': None,
},

# --- T2 TRAILTHING: Lawrence Woods SNP Boardwalk ---
{
    'entity_type': 'Trailthing',
    'name_raw': 'Lawrence Woods Boardwalk',
    'source_term_raw': 'accessible boardwalk',
    'source_hierarchy_context_raw': 'Listed as the sole trail at Lawrence Woods State Nature Preserve under Available Trails > Hiking Trails; described as 1.1 miles of accessible boardwalk',
    'counties_raw': ['Hardin'],
    'county_primary': 'Hardin',
    'parent_id_raw': None,
    'site_parent_raw': 'Lawrence Woods State Nature Preserve',
    'parent_site_network_raw': None,
    'member_trailthing_names_raw': None,
    'ownership_raw': 'State of Ohio',
    'governance_raw': 'ODNR Division of Natural Areas and Preserves',
    'partner_agencies_raw': None,
    'coordination_raw': None,
    'description_raw': (
        'Accessible boardwalk trail through old-growth forest and buttonbush swamp habitats at Lawrence '
        'Woods State Nature Preserve. Provides access to rare plant communities including sites where the '
        'Ohio-endangered Heart-leaf plantain occurs. Primary access to the preserve interior for hikers '
        'and birders.'
    ),
    'use_type_raw': 'Hiking; birding',
    'surface_type_raw': 'Boardwalk',
    'origin_type_raw': None,
    'status_raw': 'Open',
    'difficulty_raw': None,
    'accessibility_raw': 'ADA accessible boardwalk',
    'total_length_raw': '1.1 miles',
    'urls_raw': ['https://ohiodnr.gov/go-and-do/plan-a-visit/find-a-property/lawrence-woods-state-nature-preserve'],
    'maps_raw': [],
    'identity_notes_raw': 'eBird sub-hotspot L3930284 (Lawrence Woods State Nature Preserve--Woods Boardwalk) corresponds to this trail.',
    'last_verified_date': '2026-06-01',
    'field_verified': False,
    'discovery_tier': 2,
    'seeded_from_baseline': True,
    'baseline_id': 'Hardin County Veterans Memorial Park Trail',
},

# --- T2 SITE NETWORKS: NULL ---
{
    'entity_type_result': {
        'tier': 2,
        'governance_level': 'State',
        'entity_type': 'Site Network',
        'result': 'null',
        'sources_checked': [
            'ODNR DNAP — 1 SNP in Hardin County; Rule 2 threshold (2+ member sites) not met for county-scoped network. Statewide DNAP portfolio is not cataloged per-county.',
            'ODNR Division of Wildlife — 2 wildlife areas but both cross-county; no qualifying county-scoped wildlife portfolio network.',
            'ODNR Scenic Rivers — Blanchard and Scioto are not designated scenic rivers in Ohio (17 total); no scenic river Site in Hardin County.',
            'No NHAs or other formal multi-site state designations encompassing Hardin County entities found.',
        ],
        'reasoning': 'No T2 Site Network threshold met for Hardin County. Single SNP; two cross-county wildlife areas; no scenic river designation; no state-level multi-site umbrella designation present.',
    }
},

# --- T2 ACCESS POINT 1: Lawrence Woods SNP Entrance ---
{
    'entity_type': 'Access Point',
    'name_raw': 'Lawrence Woods State Nature Preserve Entrance',
    'counties_raw': ['Hardin'],
    'county_primary': 'Hardin',
    'parent_sites_raw': ['Lawrence Woods State Nature Preserve'],
    'parent_trailthings_raw': ['Lawrence Woods Boardwalk'],
    'governance_raw': 'ODNR Division of Natural Areas and Preserves',
    'description_raw': 'Parking area and boardwalk trailhead at the preserve entrance on County Road 190. Gateway to 1.1-mile accessible boardwalk through old-growth forest and wetlands.',
    'features_raw': 'Parking; boardwalk trailhead; no restrooms; no pets',
    'location_raw': '13278 County Road 190, Kenton, OH 43326',
    'gps_lat_raw': '40.6833',
    'gps_lon_raw': '-83.6092',
    'urls_raw': ['https://ohiodnr.gov/go-and-do/plan-a-visit/find-a-property/lawrence-woods-state-nature-preserve'],
    'identity_notes_raw': None,
    'last_verified_date': '2026-06-01',
    'field_verified': False,
    'discovery_tier': 2,
    'seeded_from_baseline': False,
    'baseline_id': None,
},

# --- T2 ACCESS POINT 2: Andreoff WA North Tract ---
{
    'entity_type': 'Access Point',
    'name_raw': 'Andreoff Wildlife Area North Tract Access',
    'counties_raw': ['Hardin'],
    'county_primary': 'Hardin',
    'parent_sites_raw': ['Andreoff Wildlife Area'],
    'parent_trailthings_raw': [],
    'governance_raw': 'ODNR Division of Wildlife',
    'description_raw': 'Public access to the northern 584-acre tract of Andreoff Wildlife Area, just south of the village of Forest. Restored wetland and native grassland habitat.',
    'features_raw': 'Parking; hunting access; wildlife viewing; waterfowl observation',
    'location_raw': 'County Road 205 and Township Road 50, south of Forest, Hardin County',
    'gps_lat_raw': None,
    'gps_lon_raw': None,
    'urls_raw': ['https://dam.assets.ohio.gov/image/upload/ohiodnr.gov/documents/wildlife/wildlife-area-maps/AndreoffWA.pdf'],
    'identity_notes_raw': 'eBird hotspot L14044415 (Andreoff Wildlife Area--Hardin Co. Rd. 205) corresponds to this access area.',
    'last_verified_date': '2026-06-01',
    'field_verified': False,
    'discovery_tier': 2,
    'seeded_from_baseline': False,
    'baseline_id': None,
},

# --- T2 ACCESS POINT 3: Andreoff WA South Tract ---
{
    'entity_type': 'Access Point',
    'name_raw': 'Andreoff Wildlife Area South Tract Access',
    'counties_raw': ['Hardin'],
    'county_primary': 'Hardin',
    'parent_sites_raw': ['Andreoff Wildlife Area'],
    'parent_trailthings_raw': [],
    'governance_raw': 'ODNR Division of Wildlife',
    'description_raw': 'Public access to the southern 135-acre tract of Andreoff Wildlife Area, south of Kenton near the Lawrence Woods complex. Restored wetlands, native grassland, and 36-acre woodlot.',
    'features_raw': 'Parking; hunting access; wildlife viewing; wetland access',
    'location_raw': 'County Road 190 west of OH-292, south of Kenton, Hardin County',
    'gps_lat_raw': None,
    'gps_lon_raw': None,
    'urls_raw': ['https://dam.assets.ohio.gov/image/upload/ohiodnr.gov/documents/wildlife/wildlife-area-maps/AndreoffWA.pdf'],
    'identity_notes_raw': None,
    'last_verified_date': '2026-06-01',
    'field_verified': False,
    'discovery_tier': 2,
    'seeded_from_baseline': False,
    'baseline_id': None,
},

# --- T2 NULL DOCUMENTATION: all other T2 sources ---
{
    'entity_type_result': {
        'tier': 2,
        'governance_level': 'State — Null Sources Documented',
        'entity_type': 'Multiple',
        'result': 'null_items_documented',
        'null_items': [
            'ODNR State Parks — none in Hardin County',
            'ODNR State Forests — none in Hardin County',
            'ODOT rest stops — baseline null confirmed; US-30 rest areas in Allen Co. (mm 42) and Wyandot Co. (mm 0), not Hardin; no US-68 rest areas',
            'Ohio History Connection — no OHC-managed memorial or historic site in Hardin County; Fort Amanda is in Auglaize County',
            'OTIC — Ohio Turnpike (I-80/90) does not pass through Hardin County; OTIC not applicable',
            'Public universities — ONU (Ada) is private (United Methodist Church affiliation); no public university in Hardin County',
            'ODNR Scenic Rivers — Blanchard River and Scioto River not among Ohio 17 designated scenic rivers; no scenic river in Hardin County',
            'ODNR Water Trails — Blanchard River Water Trail managed by Hancock Park District (T3); all access points in Hancock County; no Hardin County water trail',
            'ODNR river/stream fishing maps — 12 entries total; none for Blanchard, Scioto, or Hardin County rivers',
            'ODNR fishing lake maps — no ODNR-managed fishing lakes in Hardin County',
            'EPA/DEFA, ODA — no publicly accessible conservation lands identified in Hardin County',
        ],
        'sources_checked': [
            'ohiodnr.gov/discover-and-learn/safety-conservation/about-ODNR/wildlife/documents-publications/hunting-area-maps',
            'ohiodnr.gov/discover-and-learn/safety-conservation/about-ODNR/wildlife/documents-publications/fishing-lake-maps',
            'ohiodnr.gov/discover-and-learn/safety-conservation/about-ODNR/wildlife/documents-publications/river-stream-fishing-maps',
            'ohiodnr.gov/discover-and-learn/land-water/rivers-streams-wetlands/scenic-rivers-program',
            'ohiodnr.gov/discover-and-learn/land-water/rivers-streams-wetlands/ohio-water-trails',
            'ohiohistory.org/visit/browse-historic-sites/',
            'transportation.ohio.gov/home/traveling/rest-areas',
            'SORP_Parcels_2023.csv — 10 NATURAL RESOURCES parcels in Hardin County confirmed, consistent with known state entities',
        ],
    }
},

]

data.setdefault('records', [])
data['records'].extend(t2_records)
f.write_text(yaml.dump(data, allow_unicode=True, sort_keys=False), encoding='utf-8')
print(f'Total records now: {len(data["records"])}')
