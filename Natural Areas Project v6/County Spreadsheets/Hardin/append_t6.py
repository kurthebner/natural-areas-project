import yaml, pathlib

f = pathlib.Path(r'D:\users\user1\Documents\CP Projects\Natural Areas Project v6\County Spreadsheets\Hardin\hardin_ohio_raw_discovery.yaml')
data = yaml.safe_load(f.read_text(encoding='utf-8'))

def site(name, gov, desc, hab, feat, loc, acres=None, lat=None, lon=None,
         urls=None, ebird=None, ident=None, seeded=False, bid=None, county='Hardin', cc=None):
    return {
        'entity_type': 'Site',
        'name_raw': name,
        'counties_raw': cc if cc else [county],
        'county_primary': county,
        'ownership_raw': gov,
        'governance_raw': gov,
        'partner_agencies_raw': None,
        'coordination_raw': None,
        'description_raw': desc,
        'habitat_type_raw': hab,
        'features_raw': feat,
        'access_notes_raw': None,
        'location_raw': loc,
        'acres_raw': acres,
        'gps_lat_raw': lat,
        'gps_lon_raw': lon,
        'boundary_document_raw': None,
        'urls_raw': urls or [],
        'ebird_hotspot_id': ebird,
        'identity_notes_raw': ident,
        'township_raw': None,
        'municipality_raw': None,
        'last_verified_date': '2026-06-01',
        'field_verified': False,
        'discovery_tier': 6,
        'seeded_from_baseline': seeded,
        'baseline_id': bid,
    }

def ap(name, parent_sites, parent_tts, gov, desc, feat, loc, lat=None, lon=None, urls=None, ident=None):
    return {
        'entity_type': 'Access Point',
        'name_raw': name,
        'counties_raw': ['Hardin'],
        'county_primary': 'Hardin',
        'parent_sites_raw': parent_sites,
        'parent_trailthings_raw': parent_tts,
        'governance_raw': gov,
        'description_raw': desc,
        'features_raw': feat,
        'location_raw': loc,
        'gps_lat_raw': lat,
        'gps_lon_raw': lon,
        'urls_raw': urls or [],
        'identity_notes_raw': ident,
        'last_verified_date': '2026-06-01',
        'field_verified': False,
        'discovery_tier': 6,
        'seeded_from_baseline': False,
        'baseline_id': None,
    }

t6_records = [

# =============================================================================
# TIER 6 — MUNICIPAL
# Municipalities: Kenton (city), Ada, Alger, Dunkirk, Forest,
#                McGuffey, Mount Victory, Patterson, Ridgeway
# =============================================================================

# --- KENTON SITES ---

site('Saulisberry Park',
     'City of Kenton Parks & Recreation',
     '167-acre former stone quarry site west of Kenton featuring France Lake (quarry lake) for fishing, boating, and kayaking. Includes a campground with 33 campsites (electric, water/electric, and full hookup options), primitive tent camping, and monthly hookup sites. Playground, basketball court, picnic tables scattered around the lake, kayak launcher. Permit required for lake activities; purchased through City of Kenton. No swimming permitted.',
     'Former quarry lake; open water; grassy areas; flat terrain',
     'France Lake (fishing, boating, kayaking, no swimming); 33 campsites; tent camping; electric/water hookups; kayak launcher; basketball court; playground; picnic tables; permit required for lake activities',
     '13344 State Route 67W, Kenton, OH 43326',
     acres='167.4',
     lat='40.6209', lon='-83.6374',
     urls=['https://cityofkenton.recdesk.com/Community/Facility/Detail?facilityId=1',
           'https://www.hipcamp.com/en-US/land/ohio-saulisberry-park-france-lake-campground-2ejhwxd1'],
     ebird='L3661530',
     seeded=True, bid='Saulisberry Park'),

site('France Lake',
     'City of Kenton Parks & Recreation',
     'Former stone quarry lake at Saulisberry Park, west of Kenton. Used for fishing, boating, and kayaking. No swimming permitted. Permit required for lake activities. Surrounded by flat grassy campground terrain.',
     'Former quarry lake; open water',
     'Fishing; boating; kayaking; no swimming; kayak launcher; permit required',
     'Within Saulisberry Park, 13344 State Route 67W, Kenton, OH 43326',
     lat='40.6209', lon='-83.6374',
     urls=['https://cityofkenton.recdesk.com/Community/Facility/Detail?facilityId=1'],
     ident='Child site of Saulisberry Park. Former quarry; identity-bearing lake within the park.',
     seeded=True, bid='Boy Scout Lake'),

site('C.E. Wharton Memorial Park',
     'City of Kenton Parks & Recreation',
     '21.4-acre municipal park in Kenton featuring an 18-hole disc golf course that hosts local tournaments. Walking and running paths through green space. Leisure Playground; basketball and soccer facilities. Wharton Park Bark Park (dog park) located within the park. Known as a premier disc golf venue in Hardin County.',
     None,
     '18-hole disc golf course; Leisure Playground; basketball court; soccer court; walking/running paths; Bark Park (dog park); 21.4 acres',
     'Kenton, OH (specific address TBD)',
     acres='21.4',
     urls=['https://cityofkenton.com/parks/'],
     seeded=True, bid='C.E. Wharton Memorial Park'),

site('Home Run Memorial Park',
     'City of Kenton Parks & Recreation',
     '40.8-acre baseball and softball complex in Kenton. Seven fields with a 1/2-mile walking track, full concession stand with board office and umpire locker room, indoor batting cages, picnic areas, and parking for approximately 400 cars. Home of Kenton Little League.',
     None,
     '7 baseball/softball fields; 1/2-mile walking track; indoor batting cages; concession stand; picnic areas; parking 400+ cars',
     '13625 State Route 292, Kenton, OH 43326',
     acres='40.8',
     urls=['https://www.kentonlittleleague.com/Default.aspx?tabid=1389798'],
     seeded=False, bid=None),

site('Gene Autry Park',
     'City of Kenton Parks & Recreation',
     'Small downtown memorial park at the corner of Market Street and State Route 309, dedicated June 26, 2004. Features a 30x80-foot mural of Gene Autry (painted on adjacent building wall) on his horse Champion. Park includes a bench adorned with wagon wheels, shrubs, and a stone commemorating Gene Autry\'s connection to Kenton. Primarily a mural/memorial experience; small urban green space.',
     None,
     'Gene Autry mural (30x80 ft); memorial bench; stone marker; small urban green space',
     'Corner of Market Street and State Route 309, downtown Kenton, OH',
     urls=['https://www.lasr.net/travel/city.php?TravelTo=OH0506007&Attraction_ID=OH0506007a005&VA=Y'],
     seeded=False, bid=None),

site('Pioneer Park',
     'City of Kenton Parks & Recreation',
     'Municipal park on King Street in Kenton offering green space for walking and running.',
     None,
     'Open green space; walking; running',
     'King Street, Kenton, OH',
     urls=['https://cityofkenton.com/parks/'],
     seeded=True, bid='Pioneer Park'),

site('Murray Park',
     'City of Kenton Parks & Recreation',
     'Small municipal park located on North Cherry Street in Kenton, situated around a small water body.',
     None,
     'Small water body; green space; open space',
     '511-599 N Cherry St, Kenton, OH 43326',
     urls=['https://cityofkenton.com/parks/'],
     seeded=False, bid=None),

# --- KENTON SITE NETWORK (PROVISIONAL) ---
{
    'entity_type': 'Site Network',
    'network_name_raw': 'City of Kenton Parks & Recreation',
    'network_type_raw': 'Municipal Recreation System',
    'org_type_raw': 'Municipal Department',
    'status_raw': 'Active',
    'ownership_raw': None,
    'governance_raw': 'City of Kenton Parks & Recreation Department',
    'partner_agencies_raw': None,
    'coordination_raw': None,
    'counties_raw': ['Hardin'],
    'states_raw': None,
    'member_count_raw': None,
    'member_site_names_raw': 'Saulisberry Park; C.E. Wharton Memorial Park; Home Run Memorial Park; Gene Autry Park; Pioneer Park; Murray Park',
    'description_raw': 'City of Kenton municipal park system managed by the Parks & Recreation Department. Operates multiple parks and recreation facilities across Kenton including Saulisberry Park/France Lake Campground, Wharton Memorial Park (disc golf), Home Run Memorial Park (baseball complex), Gene Autry Park, Pioneer Park, and Murray Park.',
    'identity_notes_raw': 'SITE_NETWORK_PROVISIONAL — City of Kenton Parks & Recreation; first member site cataloged 2026-06-01; 6+ member sites expected. Threshold: Rule 3 — Municipal Department, 3+ in-scope member Sites confirmed.',
    'notes_raw': None,
    'urls_raw': ['https://cityofkenton.com/parks/'],
    'discovery_tier': 6,
    'seeded_from_baseline': False,
    'baseline_id': None,
},

# --- KENTON ACCESS POINTS ---
ap('Saulisberry Park Entrance',
   ['Saulisberry Park'], [],
   'City of Kenton Parks & Recreation',
   'Main entrance to Saulisberry Park and France Lake Campground on SR-67W west of Kenton.',
   'Parking; campsite check-in; lake access; permit sales',
   '13344 State Route 67W, Kenton, OH 43326',
   lat='40.6209', lon='-83.6374',
   urls=['https://cityofkenton.recdesk.com/Community/Facility/Detail?facilityId=1']),

ap('Home Run Memorial Park Entrance',
   ['Home Run Memorial Park'], [],
   'City of Kenton Parks & Recreation',
   'Main entrance to Home Run Memorial Park baseball complex on SR 292.',
   'Parking (400+ cars); field access; concession',
   '13625 State Route 292, Kenton, OH 43326',
   urls=['https://www.kentonlittleleague.com/Default.aspx?tabid=1389798']),

# --- ADA SITES ---

site('Ada War Memorial Park',
     'Village of Ada',
     'Large municipal park covering 70+ acres in the Village of Ada, established in the 1930s as a memorial to World War I veterans. Features a historic log cabin from the early 19th century restored as a public museum. Contains a stocked fishing pond for fishing, boating, and picnicking. Several hiking trails wind through wooded areas. Recreational amenities include playground, picnic shelters, basketball court, and pavilion. Ice skating in winter.',
     'Wooded areas; stocked pond; open park lawns',
     'Historic log cabin museum; stocked fishing pond; hiking trails; playground; picnic shelters; basketball court; pavilion; ice skating (winter); 70+ acres',
     '401 N Park Dr, Ada, OH 45810',
     acres='70+',
     lat='40.7683', lon='-83.8250',
     urls=['https://www.adaoh.gov/taxonomy/term/56',
           'https://www.facebook.com/AdaWarMemoralPark/'],
     seeded=True, bid='Ada Memorial Park'),

site('Ada Railroad Park',
     'Village of Ada',
     'Historic village park at the site of the former Ada Pennsylvania Railroad Station. The village purchased the lot in 1958. Features a surface parking lot, park benches, picnic tables, and new plantings while retaining historic configuration, open space, view sheds, and memorial cannon. NRHP-listed (1998) as "Ada Pennsylvania Station and Railroad Park" — a former railroad station building associated with the park.',
     None,
     'Historic railroad station context; open green space; park benches; picnic tables; memorial cannon; parking; NRHP listed',
     '112 E Central Ave, Ada, OH 45810',
     urls=['https://www.adaoh.gov/', 'https://www.historic-structures.com/oh/ada/ada-pennsylvania-station/'],
     ident='NRHP #98001014 — "Ada Pennsylvania Station and Railroad Park" listed 1998. Village-managed park on former railroad station site.',
     seeded=True, bid='Ada Railroad Park'),

# Ada Railroad Park Path (Trailthing)
{
    'entity_type': 'Trailthing',
    'name_raw': 'Ada Railroad Park Path',
    'source_term_raw': 'linear park',
    'source_hierarchy_context_raw': 'Baseline describes as "short paved path extending from Ada Railroad Park; no signage or formal designation." Village of Ada manages Ada Railroad Park.',
    'counties_raw': ['Hardin'],
    'county_primary': 'Hardin',
    'parent_id_raw': None,
    'site_parent_raw': 'Ada Railroad Park',
    'parent_site_network_raw': None,
    'member_trailthing_names_raw': None,
    'ownership_raw': 'Village of Ada',
    'governance_raw': 'Village of Ada',
    'partner_agencies_raw': None,
    'coordination_raw': None,
    'description_raw': 'Short paved path extending from Ada Railroad Park. Baseline notes no signage or formal designation. Part of the Ada Railroad Park historic complex.',
    'use_type_raw': 'Walking',
    'surface_type_raw': 'Paved',
    'origin_type_raw': None,
    'status_raw': None,
    'difficulty_raw': None,
    'accessibility_raw': None,
    'total_length_raw': None,
    'urls_raw': ['https://www.adaoh.gov/'],
    'maps_raw': [],
    'identity_notes_raw': 'Baseline entry "Ada Railroad Park Path" describes this. Baseline also notes "Ada Trail Spur (Unmarked)" as a separate short segment — may be the same entity or an extension. See unconfirmed baseline seeds.',
    'last_verified_date': '2026-06-01',
    'field_verified': False,
    'discovery_tier': 6,
    'seeded_from_baseline': True,
    'baseline_id': 'Ada Railroad Park Path',
},

# Ada access point
ap('Ada War Memorial Park Main Entrance',
   ['Ada War Memorial Park'], [],
   'Village of Ada',
   'Main entrance to Ada War Memorial Park on N Park Dr.',
   'Parking; trail access; pond access; log cabin museum access; playground',
   '401 N Park Dr, Ada, OH 45810',
   lat='40.7683', lon='-83.8250',
   urls=['https://www.adaoh.gov/']),

# --- FOREST SITES ---

site('Gormley Park',
     'Village of Forest',
     'Village park on Mary Street on the east side of Forest. Features a beautiful stocked pond, scenic walking trails, playgrounds, softball/baseball fields, tennis courts, basketball courts, and sand volleyball courts. Three pavilion buildings available for rental (including an All-Weather Pavilion with AC, kitchen, and capacity for 115 people). Gazebo. Home of the Jackson-Forest Fire Department\'s annual Tree Town Festival in July.',
     'Stocked pond; park lawns; wooded edges',
     'Stocked pond; walking trails; playground; softball/baseball fields; tennis courts; basketball courts; sand volleyball; gazebo; 3 pavilions (rentable); Tree Town Festival site',
     'Mary Street, Forest, OH 45843 (east side of village)',
     urls=['https://www.villageofforest.com/parks-and-recreation/'],
     seeded=True, bid='Gormley Park'),

site('Ranger Sports Complex',
     'Village of Forest',
     'Multi-field soccer complex on the site of the former Riverdale Forest Elementary School on West Dixon Street in Forest. Home of the Riverdale Youth Soccer Club (member of Black Swamp Soccer League). Hosts soccer practices and games from multiple area communities each spring and fall. Site of the Riverdale Spring Classic Soccer Tournament in May, drawing 2000+ visitors. Features a pavilion built with a Nature Works Grant (2011), handicap accessible restrooms, concession area, and covered picnic area.',
     None,
     'Soccer fields; Nature Works grant pavilion; handicap accessible restrooms; concession; covered picnic area; parking',
     'West Dixon Street, Forest, OH 45843 (former Riverdale Forest Elementary site)',
     urls=['https://www.villageofforest.com/parks-and-recreation/'],
     ident='Former elementary school site. Village-managed complex hosting Riverdale Youth Soccer Club.',
     seeded=True, bid='Ranger Sports Complex'),

# --- DUNKIRK SITE ---

site('Dunkirk Community Park',
     'Village of Dunkirk',
     'Village park in Dunkirk. Features playground equipment, ball field, and picnic shelter.',
     None,
     'Playground; ball field; picnic shelter',
     'Dunkirk, OH 45836',
     urls=['https://villageofdunkirk.com/'],
     seeded=True, bid='Dunkirk Community Park'),

# --- McGUFFEY SITE ---

site('McGuffey Village Park',
     'Village of McGuffey',
     'Village park in McGuffey featuring playground equipment (slides, swings, monkey bars, tether ball) located near the pool area. Gazebo along the south border of the former railroad right-of-way. Small community park with active recreational use.',
     None,
     'Playground (slides, swings, monkey bars, tether ball); gazebo; pool area adjacency; former railroad ROW edge',
     'McGuffey, OH 45859',
     lat='40.6932', lon='-83.7835',
     urls=['https://www.facebook.com/villageofmcguffey/'],
     seeded=True, bid='McGuffey Village Park'),

# --- MOUNT VICTORY SITE ---

site('Mount Victory Village Park',
     'Village of Mount Victory',
     'Community park in Mount Victory featuring a walking path, natural toddler playground, baseball diamond with new lights, basketball court, concession stand, bleachers, and shelter houses. Walking path completed in phases 2018-2020. Natural toddler playground area completed Spring 2020. Ongoing community improvement project funded through grants and donations led by Mt. Victory CIC (Community Improvement Corporation). Community Building (Sportsman\'s Club) on site available for rentals.',
     None,
     'Walking path; natural toddler playground; baseball diamond; basketball court; concession stand; bleachers; shelter houses; Community Building (rentable)',
     'Mount Victory, OH 43340',
     urls=['https://mountvictory.com/village-park-progress/',
           'https://www.mountvictoryohio.gov/'],
     seeded=True, bid='Mount Victory Park'),

# --- ALGER SITE ---

site('Ray Brown Memorial Park',
     'Village of Alger',
     'Community park and baseball complex in Alger, officially dedicated May 14, 2026 as Ray Brown Memorial Park in honor of Baseball Hall of Fame player Ray Brown (born Alger, 1908; Negro League star with Pittsburgh Homestead Grays; inducted 2006). Features a 30x80-foot mural of Ray Brown painted by Ohio Northern University alumna Aubrey Davis. Original Alger ballpark site with baseball diamonds, playground, and pavilions; refurbished with ODNR grants in 2021 and 2023. Dedicated at event attended by Ohio Governor Mike DeWine.',
     None,
     'Baseball diamonds; playground; pavilions; Ray Brown mural; ODNR-grant-refurbished facilities',
     'Alger, OH 45812',
     urls=['https://www.limaohio.com/top-stories/2026/05/14/alger-residents-celebrate-opening-of-ray-brown-memorial-park/'],
     ident='Renamed/rededicated as Ray Brown Memorial Park at grand opening May 14, 2026. Formerly known as Alger Ballpark. ODNR grant refurbishments 2021 and 2023. Not in baseline — new entity.',
     seeded=False, bid=None),

# --- UNCONFIRMED BASELINE SEEDS (T6) ---
{
    'entity_type_result': {
        'tier': 6,
        'governance_level': 'Municipal — Unconfirmed Baseline Seeds',
        'entity_type': 'Multiple',
        'result': 'unconfirmed_baseline_seeds',
        'seeds': [
            {
                'baseline_id': 'Ada Trail Spur (Unmarked)',
                'status': 'UNCONFIRMED_BASELINE_SEED',
                'hold_detail': 'Baseline describes a short paved segment extending from Ada Railroad Park with no signage or formal designation. No authoritative source found confirming a distinct trail entity separate from Ada Railroad Park Path. May be same entity as Ada Railroad Park Path or an informal extension. Hold pending field verification.',
            },
            {
                'baseline_id': 'Simon Kenton Trail (Planned Extension)',
                'status': 'UNCONFIRMED_BASELINE_SEED',
                'hold_detail': 'Baseline describes a proposed/planned extension of a regional trail network into Hardin County — not yet constructed as of baseline date. No authoritative source found confirming active construction or formal designation. Status: Planned only. Not a catalogable entity until constructed or formally designated.',
            },
            {
                'baseline_id': 'Kenton Greenbelt Parcel',
                'status': 'UNCONFIRMED_BASELINE_SEED',
                'hold_detail': 'Baseline describes wooded and grassy parcel along river near Kenton with informal trails and wildlife sightings. Unknown ownership. No authoritative source found confirming public ownership, formal access, or managed identity. Likely informal open space or private land.',
            },
            {
                'baseline_id': 'Ada Reservoir',
                'status': 'UNCONFIRMED_BASELINE_SEED',
                'hold_detail': 'Baseline GPS (40.7685,-83.8232) matches Ada War Memorial Park location (40.7683,-83.8250). The stocked fishing pond described in Ada War Memorial Park is likely the same entity as "Ada Reservoir." If the Ada Reservoir is the pond inside Ada Memorial Park, it is captured as a feature of that Site, not a separate entity. If it is a separate municipal water reservoir, it would be out of scope (utility infrastructure). Hold pending field verification to confirm identity.',
            },
            {
                'baseline_id': 'Ada Reservoir Woodlot Buffer',
                'status': 'UNCONFIRMED_BASELINE_SEED',
                'hold_detail': 'Baseline describes wooded edge and drainage swale adjacent to Ada Reservoir with informal access and habitat value. No authoritative source confirms a managed natural area identity. GPS matches Ada Memorial Park cluster. Likely informal edge habitat; does not meet cataloging threshold as a distinct managed Site.',
            },
            {
                'baseline_id': 'Kenton Water Treatment Plant Buffer',
                'status': 'UNCONFIRMED_BASELINE_SEED',
                'hold_detail': 'Baseline describes grassy and wooded buffer surrounding municipal water infrastructure north of Kenton. Managed by City of Kenton. Access is restricted (buffer only). Does not meet public access threshold for cataloging as a natural area Site.',
            },
        ],
    }
},

# --- MUNICIPAL NULL DOCUMENTATION ---
{
    'entity_type_result': {
        'tier': 6,
        'governance_level': 'Municipal — Additional Sources and Nulls',
        'entity_type': 'Multiple',
        'result': 'documented',
        'municipality_results': {
            'Kenton': 'cityofkenton.com confirmed; 7+ parks cataloged; city pool (920 W Franklin St) and skate park noted as built facilities, not natural area Sites; Kenton Greenbelt Parcel = unconfirmed baseline seed',
            'Ada': 'adaoh.gov confirmed; Ada War Memorial Park (70+ ac) and Ada Railroad Park cataloged; Ada Railroad Park Path (Trailthing) staged; Ada Trail Spur and Ada Reservoir = unconfirmed baseline seeds',
            'Forest': 'villageofforest.com confirmed; Gormley Park and Ranger Sports Complex cataloged',
            'Dunkirk': 'villageofdunkirk.com confirmed; Dunkirk Community Park cataloged from baseline (parks page 404 — using baseline data)',
            'McGuffey': 'No official website; Village Facebook only; McGuffey Village Park cataloged from Facebook/search descriptions; McGuffey Reservoir = unconfirmed baseline seed (unknown ownership)',
            'Mount Victory': 'mountvictoryohio.gov and mountvictory.com confirmed; Mount Victory Village Park cataloged',
            'Alger': 'No official website; Lima News article and bloggerbill.com; Ray Brown Memorial Park cataloged (opened May 14, 2026)',
            'Patterson': 'Village of 130 people; no official website; no parks found; null',
            'Ridgeway': 'Village spans Hardin AND Logan counties (population 314); no parks found; null for natural area entities',
        },
        'sources_checked': [
            'cityofkenton.com/parks', 'cityofkenton.recdesk.com',
            'adaoh.gov', 'villageofforest.com/parks-and-recreation/',
            'villageofdunkirk.com', 'facebook.com/villageofmcguffey',
            'mountvictoryohio.gov, mountvictory.com',
            'limaohio.com (Ray Brown Memorial Park)',
            'bloggerbill.com/ohio/hardin-county/alger-oh-things-to-do',
            'Wikipedia articles for Patterson and Ridgeway',
        ],
    }
},

]

data.setdefault('records', [])
data['records'].extend(t6_records)
f.write_text(yaml.dump(data, allow_unicode=True, sort_keys=False, default_flow_style=False), encoding='utf-8')
print(f'Total records now: {len(data["records"])}')
