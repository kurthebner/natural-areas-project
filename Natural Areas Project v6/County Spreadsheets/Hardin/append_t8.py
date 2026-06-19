import yaml, pathlib

f = pathlib.Path(r'D:\users\user1\Documents\CP Projects\Natural Areas Project v6\County Spreadsheets\Hardin\hardin_ohio_raw_discovery.yaml')
data = yaml.safe_load(f.read_text(encoding='utf-8'))

def cem8(name, owner, subtype, location, notes=None):
    return {
        'entity_type': 'Site',
        'name_raw': name,
        'counties_raw': ['Hardin'],
        'county_primary': 'Hardin',
        'ownership_raw': owner,
        'governance_raw': owner,
        'partner_agencies_raw': None,
        'coordination_raw': None,
        'description_raw': f'{subtype} in Hardin County, Ohio.',
        'habitat_type_raw': None,
        'features_raw': 'Cemetery',
        'access_notes_raw': None,
        'location_raw': location,
        'acres_raw': None,
        'gps_lat_raw': None,
        'gps_lon_raw': None,
        'boundary_document_raw': None,
        'urls_raw': ['https://sites.rootsweb.com/~ohcps/hardin.html'],
        'ebird_hotspot_id': None,
        'identity_notes_raw': notes,
        'township_raw': None,
        'municipality_raw': None,
        'last_verified_date': '2026-06-01',
        'field_verified': False,
        'discovery_tier': 8,
        'seeded_from_baseline': False,
        'baseline_id': None,
    }

t8_records = [

# --- GOLF COURSE (mandatory IMP-110) ---
{
    'entity_type': 'Site',
    'name_raw': 'Memorial Park Golf Club',
    'counties_raw': ['Hardin'],
    'county_primary': 'Hardin',
    'ownership_raw': 'Hardin County Golf Foundation',
    'governance_raw': 'Hardin County Golf Foundation',
    'partner_agencies_raw': 'Hardin County Veterans Memorial Park District (adjacent land)',
    'coordination_raw': None,
    'description_raw': '18-hole public golf course along the Scioto River in Kenton, Ohio. Originally designed by Barry Serafin in 1929. The Hardin County Golf Foundation expanded to 18 holes in 1991 by purchasing land on both sides of the Scioto River with the anticipation of eventually deeding the land to the Veterans Memorial Park District. Par 72, approximately 6,300 yards, course rating 69.7.',
    'habitat_type_raw': None,
    'features_raw': '18 holes; Par 72; ~6,300 yards; public access; along Scioto River',
    'access_notes_raw': 'Public course; open tee times available.',
    'location_raw': '15906 OH-309, Kenton, OH 43326 (adjacent to Veterans Memorial Park)',
    'acres_raw': None,
    'gps_lat_raw': '40.6470',
    'gps_lon_raw': '-83.6095',
    'boundary_document_raw': None,
    'urls_raw': ['https://www.memorialparkgolfclub.com/'],
    'ebird_hotspot_id': None,
    'identity_notes_raw': 'Public access — open tee times. Managed by Hardin County Golf Foundation (nonprofit). Adjacent to Hardin County Veterans Memorial Park. Designed 1929 by Barry Serafin. Expanded to 18 holes 1991.',
    'township_raw': None,
    'municipality_raw': None,
    'last_verified_date': '2026-06-01',
    'field_verified': False,
    'discovery_tier': 8,
    'seeded_from_baseline': False,
    'baseline_id': None,
},

# --- ONU PRIVATE UNIVERSITY (T8 — ONU is a private university) ---
{
    'entity_type': 'Trailthing',
    'name_raw': 'ONU Green Monster Trail',
    'source_term_raw': 'paved trail',
    'source_hierarchy_context_raw': 'Described as the "Green Monster," an emerald paved trail on the Ohio Northern University campus in Ada; 2.5 miles; offers nature views and the Remington Walk (American western art)',
    'counties_raw': ['Hardin'],
    'county_primary': 'Hardin',
    'parent_id_raw': None,
    'site_parent_raw': None,
    'parent_site_network_raw': None,
    'member_trailthing_names_raw': None,
    'ownership_raw': 'Ohio Northern University',
    'governance_raw': 'Ohio Northern University',
    'partner_agencies_raw': None,
    'coordination_raw': None,
    'description_raw': '2.5-mile paved campus trail at Ohio Northern University in Ada (private institution, T8). Known as the "Green Monster" for its emerald color. Offers views of nature, changing seasons, and features the Remington Walk of American western art. Open to campus community and visitors.',
    'use_type_raw': 'Walking; running; campus recreation',
    'surface_type_raw': 'Paved (emerald)',
    'origin_type_raw': None,
    'status_raw': 'Open',
    'difficulty_raw': None,
    'accessibility_raw': 'Paved; campus accessibility assumed',
    'total_length_raw': '2.5 miles',
    'urls_raw': ['https://www.innatonu.com/best-local-hikes/'],
    'maps_raw': [],
    'identity_notes_raw': 'ONU is a private United Methodist-affiliated university (T8 entity). Campus in Ada, Hardin County. Trail is on private university campus land. Open to public/visitors.',
    'last_verified_date': '2026-06-01',
    'field_verified': False,
    'discovery_tier': 8,
    'seeded_from_baseline': False,
    'baseline_id': None,
},

# --- CHURCH CEMETERIES ---
cem8('Hickory Grove Cemetery',
     'Amish congregation (private religious)',
     'Church Cemetery (Amish)',
     'North side of TR 265, near Dudley Township line, Buck Township, Hardin County',
     notes='Amish cemetery — private religious congregation ownership. Not township-managed.'),

cem8('Grassy Point Cemetery',
     'Amish congregation (private religious)',
     'Church Cemetery (Amish)',
     'SE corner SR 292 and CR 200, Hale Township, Hardin County',
     notes='Amish cemetery — private religious congregation ownership.'),

cem8('Saint Johns Cemetery',
     'Saint Johns / Saint Paul congregation',
     'Church Cemetery',
     'West side TR 25, 1/2 mile north of CR 60, Liberty Township, Hardin County',
     notes='Alternate name: Saint Paul Cemetery. Religious congregation ownership.'),

cem8('Grove Cemetery',
     'Grove Union / Saint Marys Catholic congregation',
     'Church Cemetery',
     'Jacob Parrot Blvd (CR 171) between SR 67 and SR 309, Kenton/Pleasant Township, Hardin County. c.1872',
     notes='Alternate names: Grove Union Cemetery, Saint Mary\'s Cemetery. c.1872. Church/union cemetery.'),

cem8('Pleasant Hill (New) Cemetery',
     'Pleasant Hill Church congregation',
     'Church Cemetery',
     'SR 235 north of SR 67 and CR 150, east side at church, Roundhead Township, Hardin County',
     notes='Cemetery at church location. Distinct from Pleasant Hill Old Cemetery (township-owned at same road).'),

# --- FAMILY/PIONEER/PRIVATE CEMETERIES (rootsweb list - unstaged) ---
# Blanchard Township
cem8('Briedenbaugh Cemetery',
     'Unknown (private/family)',
     'Family Cemetery',
     'Near SW corner of CR 64 and CR 167, Blanchard Township, Hardin County'),

cem8('Draper Cemetery',
     'Unknown (private/family)',
     'Family Cemetery',
     '660 feet north of CR 70, Blanchard Township, Hardin County'),

cem8('Fry Cemetery',
     'Unknown (private/family)',
     'Family Cemetery',
     '800 feet east of CR 135, 1/2 mi TR 40, Blanchard Township, Hardin County',
     notes='Alternate name: Lynch Cemetery.'),

cem8('Show Cemetery',
     'Unknown (private/family)',
     'Family Cemetery',
     'CR 167 near Blanchard River, Blanchard Township, Hardin County'),

cem8('Sorgen Cemetery',
     'Unknown (private/family)',
     'Family Cemetery',
     '500 ft south of CR 60, east of CR 135, Blanchard Township, Hardin County'),

# Buck Township
cem8('Hatcher Cemetery',
     'Unknown (private/family)',
     'Family Cemetery',
     'SR 31, Buck Township, Hardin County. c.1882',
     notes='GNIS-listed.'),

cem8('Lynn Grove Cemetery',
     'Unknown (private/family)',
     'Family Cemetery',
     'SR 3 north of TR 265, Buck Township, Hardin County'),

cem8('Wolfcreek Cemetery',
     'Unknown (private/family)',
     'Family Cemetery',
     'SR 31 north of TR 265, Buck Township, Hardin County'),

cem8('Indian Burial Grounds (Buck Township)',
     'Unknown (heritage site)',
     'Archaeological/Heritage Site',
     'North of TR 184 and east of CR 155, Buck Township, Hardin County',
     notes='GNIS-listed heritage site. Burial grounds of pre-historic or indigenous origin. Not a township cemetery. Ownership and public access status unconfirmed. GNIS-only — active status unconfirmed; verify before upsert.'),

# Cessna Township additional
cem8('Behler Cemetery',
     'Unknown (private/family)',
     'Family Cemetery',
     '800 feet west of CR 135 and 1320 feet south of CR 90, Cessna Township, Hardin County',
     notes='Alternate name: Cessna Cemetery (different from the main Cessna Cemetery staged at T5). No easement noted.'),

cem8('Bunn Cemetery',
     'Unknown (private/family)',
     'Family Cemetery',
     'South side of CR 106 and 880 feet west of CR 135, Cessna Township, Hardin County',
     notes='Alternate name: Wheeler Cemetery.'),

cem8('Fulton Cemetery',
     'Unknown (private/family)',
     'Family Cemetery',
     'East side of TR 115 and 1/4 mile south of US 309, Cessna Township, Hardin County'),

cem8('Huntersville Cemetery',
     'Unknown (private/family)',
     'Family Cemetery',
     'TR 74 east of CR 75 and north of SR 309, Cessna Township, Hardin County'),

cem8('Salem Cemetery',
     'Unknown (private/family/church)',
     'Cemetery',
     'North of TR 80 and west of CR 135, Cessna Township, Hardin County'),

cem8('Strahm Cemetery',
     'Unknown (private/family)',
     'Family Cemetery',
     'NE 1/4 mile on 526 north of TR 106, Cessna Township, Hardin County'),

# Dudley Township
cem8('Craig Cemetery',
     'Unknown (private/family)',
     'Family Cemetery',
     '40 feet off CR 200, between CR 219 and TR 217, Dudley Township, Hardin County'),

cem8('Fisher Cemetery',
     'Unknown (private/family)',
     'Family Cemetery',
     'NE corner CR 200 and CR 219 on Wildcat Creek, Dudley Township, Hardin County'),

cem8('Hepburn Cemetery',
     'Unknown (private/family)',
     'Family Cemetery',
     'North side of CR 144, east of CR 265 and Pfeiffer Station, Dudley Township, Hardin County',
     notes='Alternate name: Lee Cemetery.'),

cem8('Vanfleet Cemetery',
     'Unknown (private/family)',
     'Family Cemetery',
     'South CR 144, Dudley Township, Hardin County'),

cem8('Otterbein Cemetery',
     'Unknown (private/family/church)',
     'Cemetery',
     'SE corner of CR 190 and CR 209, Dudley Township, Hardin County',
     notes='Alternate name: Otterbien Cemetery.'),

cem8('Pfeiffer Cemetery',
     'Unknown (private/family)',
     'Family Cemetery',
     'CR 144 between TR 205 and TR 209, Dudley Township, Hardin County',
     notes='Alternate name: Morrison Cemetery.'),

cem8('Ward Cemetery',
     'Unknown (private/family)',
     'Family Cemetery',
     'West side of TR 24, 1000 feet off SR 309, Dudley Township, Hardin County',
     notes='Alternate name: Hastings Cemetery.'),

cem8('Wheeler Cemetery',
     'Unknown (private/family)',
     'Family Cemetery',
     'Marion CR 29 between CR 219 and 2405, 100 yards north side, Dudley Township, Hardin County',
     notes='4 graves. Very small family plot.'),

# Hale Township
cem8('Dille Cemetery',
     'Unknown (private/family)',
     'Family Cemetery',
     'Old Mt. Victory, south off Marion Street, east of SR 31, Hale Township, Hardin County',
     notes='Alternate name: Pioneer Cemetery.'),

cem8('Jennings Cemetery',
     'Unknown (private/family)',
     'Family Cemetery',
     'West part of Hale Township, Hardin County'),

cem8('Rarey Cemetery',
     'Unknown (private/family)',
     'Family Cemetery',
     'A.K. Rarey farm on SR 292, west side, south of CR 190, Hale Township, Hardin County',
     notes='Alternate name: Andrews Cemetery.'),

cem8('Schurtzer Cemetery',
     'Unknown (private/family)',
     'Family Cemetery',
     'Curve near intersection CR 20 and CR 2, south side, Hale Township, Hardin County',
     notes='Alternate name: Mt. Pleasant Cemetery.'),

# Jackson Township
cem8('Briggs Cemetery',
     'Unknown (private/family)',
     'Family Cemetery',
     'West of Forest, north side of railroad, Jackson Township, Hardin County'),

cem8('Glenn Cemetery',
     'Unknown (private/family)',
     'Family Cemetery',
     'East Lima Street, Forest, Jackson Township, Hardin County'),

cem8('Price-Patterson Cemetery',
     'Unknown (private/family)',
     'Family Cemetery',
     'TR 195 north of SR 81 at Patterson on west side, Jackson Township, Hardin County',
     notes='Alternate name: Old Cemetery.'),

# Liberty Township
cem8('Armorsville Cemetery',
     'Unknown (private/family)',
     'Family Cemetery',
     'CR 15, 1/2 mile south of CR 10, east side, Liberty Township, Hardin County'),

cem8('Candler Cemetery',
     'Unknown (private/family)',
     'Family Cemetery',
     '50 feet NE CR 15 and TR 30, Liberty Township, Hardin County'),

cem8('Kindle Cemetery',
     'Unknown (private/family)',
     'Family Cemetery',
     '250 feet north of TR 30, east of CR 15, Liberty Township, Hardin County',
     notes='Alternate name: McClure Cemetery.'),

cem8('Maysville Cemetery',
     'Unknown (private/family)',
     'Family Cemetery',
     '300 ft north SR 309, east of Allen/Hardin line, Liberty Township, Hardin County'),

cem8('McElroy Cemetery',
     'Unknown (private/family)',
     'Family Cemetery',
     'East side CR 65, 900 feet north of CR 20, Liberty Township, Hardin County'),

cem8('Thorn Cemetery',
     'Unknown (private/family)',
     'Family Cemetery',
     'SR 235 and TR 30, SE corner, Liberty Township, Hardin County'),

# Marion Township
cem8('Carman Cemetery',
     'Unknown (private/family)',
     'Family Cemetery',
     'South side SR 309, 1 mile east of Maysville, Marion Township, Hardin County'),

cem8('Preston Cemetery',
     'Unknown (private/family)',
     'Family Cemetery',
     'South side CR 90, south of SR 309, east of Alger, Marion Township, Hardin County'),

cem8('Shadley Cemetery',
     'Unknown (private/family)',
     'Family Cemetery',
     'North side CR 90, 1 mile west of SR 195, Marion Township, Hardin County',
     notes='4 markers. Very small.'),

# McDonald Township
cem8('Fultz Cemetery',
     'Unknown (private/family)',
     'Family Cemetery',
     'East of CR 75, north of SR 67, behind church, McDonald Township, Hardin County',
     notes='Alternate names: Fuls Cemetery, Lightner Cemetery. c.1835.'),

cem8('Harvey Cemetery',
     'Unknown (private/family)',
     'Family Cemetery',
     '5226 SR 67, south side across from Fairview Cemetery, McDonald Township, Hardin County'),

cem8('Indian Burial Grounds (McDonald Township)',
     'Unknown (heritage site)',
     'Archaeological/Heritage Site',
     'TR 39 (Reed Road) east side, McDonald Township, Hardin County',
     notes='GNIS-listed heritage site. Burial grounds of pre-historic or indigenous origin. Near Zimmerman Kame area. GNIS-only — active status unconfirmed; verify before upsert.'),

cem8('McArthur Cemetery',
     'Unknown (private/family)',
     'Family Cemetery',
     '16481 Reed Road (TR 39), 1/2 mile south back lane, McDonald Township, Hardin County'),

cem8('Poe Cemetery',
     'Unknown (private/family)',
     'Family Cemetery',
     '3463 CR 200, east of SR 235, 1/2 mile from Roundhead Township, in woods, McDonald Township, Hardin County'),

# Pleasant Township additional
cem8('Chesney Cemetery',
     'Unknown (private/family)',
     'Family Cemetery',
     'Pleasant Township, Hardin County'),

cem8('County Home Cemetery',
     'Hardin County (former county home)',
     'Private Cemetery',
     'CR 1143A, 1/2 mile south of SR 309, Kenton/Pleasant Township, Hardin County',
     notes='Cemetery associated with former county infirmary/home. County government or successor entity governance.'),

cem8('Pioneer Cemetery (Kenton)',
     'Unknown (private/historical)',
     'Private Cemetery',
     'Corner of Franklin and Sciota Street, Kenton, Pleasant Township, Hardin County'),

cem8('Osborn Cemetery',
     'Unknown (private/family)',
     'Family Cemetery',
     '222 Harrison Street, Kenton/Pleasant Township, Hardin County',
     notes='2 markers. Very small.'),

cem8('Spitzer Cemetery',
     'Unknown (private/family)',
     'Family Cemetery',
     'South of TR 104 between TR 189 and CR 195, Pleasant Township, Hardin County',
     notes='No easement noted.'),

# Roundhead Township
cem8('Bowdle Cemetery',
     'Unknown (private/family)',
     'Family Cemetery',
     '15346 SR 117, north of SR 67, west side of road on hill, Roundhead Township, Hardin County'),

cem8('H. Hemphill Cemetery',
     'Unknown (private/family)',
     'Family Cemetery',
     'TR 180, Roundhead Township, Hardin County'),

cem8('Marsh Cemetery',
     'Unknown (private/family)',
     'Family Cemetery',
     '14553 NE corner TR 152 and TR 21, Roundhead Township, Hardin County',
     notes='2 graves. Very small.'),

cem8('Pleasant Hill (Old) Cemetery',
     'Unknown (private/township)',
     'Family Cemetery',
     'SR 235 north of SR 67 and CR 150, west side, Roundhead Township, Hardin County'),

cem8('Rutledge Cemetery',
     'Unknown (private/family)',
     'Family Cemetery',
     '15609 SR 117, north of SR 67, west field, Roundhead Township, Hardin County',
     notes='Alternate name: Rutedge Cemetery.'),

cem8('Schneider Cemetery',
     'Unknown (private/family)',
     'Family Cemetery',
     '200 yards north TR 160, Roundhead Township, Hardin County'),

# Taylor Creek Township
cem8('Bailey Cemetery',
     'Unknown (private/family)',
     'Family Cemetery',
     'SW corner CR 155, off CR 200, in field near tree, Taylor Creek Township, Hardin County',
     notes='Alternate name: Collins Cemetery.'),

cem8('Wroten Cemetery',
     'Unknown (private/family)',
     'Family Cemetery',
     'CR 180, south side of road, between CR 115 and TR 119, Taylor Creek Township, Hardin County'),

# Washington Township additional
cem8('Jones Cemetery',
     'Unknown (private/family)',
     'Family Cemetery',
     'North side CR 14, east of CR 95, Washington Township, Hardin County',
     notes='Alternate name: Kridler-Helms Cemetery.'),

cem8('Smith Cemetery',
     'Unknown (private/family)',
     'Family Cemetery',
     'NW corner SR 701 and TR 105, Washington Township, Hardin County'),

cem8('Waggoner Cemetery',
     'Unknown (private/family)',
     'Family Cemetery',
     'SE corner SR 81 and CR 135, Washington Township, Hardin County'),

cem8('Wagner Cemetery',
     'Unknown (private/family)',
     'Family Cemetery',
     'Between CR 115 and TR 105, south of SR 81, Washington Township, Hardin County'),

# --- T8 SITE NETWORKS: NULL ---
{
    'entity_type_result': {
        'tier': 8,
        'governance_level': 'Private',
        'entity_type': 'Site Network',
        'result': 'null',
        'sources_checked': ['No private multi-site organization with 3+ identity-bearing natural area Sites found in Hardin County'],
        'reasoning': 'No private or organizational Site Network threshold met.',
    }
},

# --- T8 NULL DOCUMENTATION ---
{
    'entity_type_result': {
        'tier': 8,
        'governance_level': 'Private — Sources and Methods',
        'entity_type': 'Multiple',
        'result': 'documented',
        'golf_courses': {
            'method': 'GolfWeather.com, GolfNow.com, golfday.us, direct search',
            'result': 'Memorial Park Golf Club is the only confirmed golf course in Hardin County, OH. No country clubs, semi-private, or 9-hole courses found.',
        },
        'gnis_cemetery_enumeration': {
            'source': 'sites.rootsweb.com/~ohcps/hardin.html (community-maintained GNIS supplement)',
            'note': 'OhioGenealogyExpress.com Hardin page 404 (URL changed); rootsweb list used as primary enumeration source. Covers all 15 townships. All named cemeteries staged at T5 (township-owned) or T8 (church/family/private).',
            'total_staged_t5': 22,
            'total_staged_t8_cemeteries': 52,
        },
        'private_camps': {
            'result': 'No private camp, scout camp, church camp, or retreat center with natural area identity confirmed in Hardin County. Cross Oak Camp = Auglaize County. Camp Cotubic = Logan County. Great Oaks BSA District serves Hardin but no camp facility within county.',
        },
        'private_preserves': {
            'result': 'No private nature preserves or nonprofit-owned natural areas beyond those captured at T7.',
        },
        'university': {
            'result': 'ONU Metzger Nature Center = Tuscarawas County (not Hardin). ONU campus (Ada) is private (T8); Green Monster Trail staged as T8 Trailthing. No ONU-owned natural area with formal public access on Ada campus identified beyond campus trail.',
        },
        'hunting_preserves': {
            'result': 'No licensed private hunting preserves found in Hardin County.',
        },
        'sources_checked': [
            'memorialparkgolfclub.com', 'golfweather.com', 'golfnow.com',
            'onu.edu (Metzger Nature Center, Green Monster)',
            'sites.rootsweb.com/~ohcps/hardin.html',
            'crossoakcamp.com (Auglaize County)', 'campcotubic.com (Logan County)',
            'ODNR hunting preserves — no Hardin County entries found',
        ],
    }
},

]

data.setdefault('records', [])
data['records'].extend(t8_records)
f.write_text(yaml.dump(data, allow_unicode=True, sort_keys=False, default_flow_style=False), encoding='utf-8')
print(f'Total records now: {len(data["records"])}')
