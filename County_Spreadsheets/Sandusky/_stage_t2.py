import yaml, pathlib

f = pathlib.Path('County_Spreadsheets/Sandusky/sandusky_ohio_raw_discovery.yaml')
data = yaml.safe_load(f.read_text(encoding='utf-8'))
data.setdefault('records', [])

# ─── TIER 2 SITES ───────────────────────────────────────────────────

data['records'].append({
    'entity_type': 'Site',
    'name_raw': 'Spiegel Grove State Park / Rutherford B. Hayes State Memorial',
    'counties_raw': ['Sandusky'],
    'county_primary': 'Sandusky',
    'ownership_raw': 'State of Ohio',
    'governance_raw': 'Ohio History Connection / Rutherford B. Hayes Presidential Library and Museums',
    'partner_agencies_raw': 'Ohio Department of Natural Resources (state park designation)',
    'coordination_raw': None,
    'gps_lat_raw': '41.341917',
    'gps_lon_raw': '-83.130833',
    'location_raw': 'Corner of Hayes Avenue and Buckland Avenue, Fremont, OH 43420',
    'description_raw': (
        'The site of the nations first presidential library includes the 31-room Victorian '
        'mansion of the 19th U.S. president, a two-story museum, and the burial site of '
        'President Hayes and First Lady Lucy Webb Hayes, all within Spiegel Grove estate. '
        'Originally built c. 1860; expanded 1880 and 1889 to over 30 rooms and 10,000 sq ft. '
        'Wooded grounds with arboretum; deeded to State of Ohio by Col. Webb C. Hayes after '
        'presidents death in 1893.'
    ),
    'features_raw': (
        'Hayes Home (31-room Victorian mansion); Museum; Research Library; Arboretum '
        '(ArbNet Accredited Level 1); White House Gates; Graves of President and First Lady Hayes; '
        'Burial site of Old Whitey (Hayes Civil War horse); Picnic tables; Grills and fire pits; '
        'Open fields; Pavilion rentals; Playground; Hiking/walking trails (approx. 1 mile paved); '
        'Fishing pond'
    ),
    'difficulty_raw': None,
    'accessibility_raw': None,
    'urls_raw': [
        'https://www.ohiohistory.org/visit/browse-historical-sites/hayes-presidential-library-museums/',
        'https://www.rbhayes.org/estate/spiegel-grove/'
    ],
    'identity_notes_raw': (
        'Dual designation: Ohio State Park (ODNR) and Ohio State Memorial (OHC). Managed by '
        'Hayes Presidential Center, Inc. under OHC ownership. National Historic Landmark (1964); '
        'NRHP (1966). Admission charged. No named trail confirmed from authoritative sources; '
        'secondary source cites approx. 1 mile paved trails; GaiaGPS shows zero named trails. '
        'Trail presence to be verified during GPS pass.'
    ),
    'township_raw': None,
    'municipality_raw': None,
    'discovery_tier': 2,
    'seeded_from_baseline': True,
    'baseline_id': 'Spiegel Grove State Park'
})

data['records'].append({
    'entity_type': 'Site',
    'name_raw': 'Pickerel Creek Wildlife Area',
    'counties_raw': ['Sandusky'],
    'county_primary': 'Sandusky',
    'ownership_raw': 'State of Ohio',
    'governance_raw': 'ODNR Division of Wildlife',
    'partner_agencies_raw': None,
    'coordination_raw': None,
    'gps_lat_raw': '41.4161632',
    'gps_lon_raw': '-82.9443582',
    'location_raw': '3451 Co Rd 256, Vickery, OH 43464; between south shore of Sandusky Bay and U.S. Route 6, Townsend and Riley townships, Sandusky County',
    'description_raw': (
        'The majority of the acreage has been restored to wetlands with the remainder in woods, '
        'brush, and native grassland. Division of Wildlife acquired Pickerel Creek Wildlife Area '
        'in 1987. Managed as a public hunting, fishing, trapping, and wildlife observation area '
        'with emphasis on waterfowl and other wetland wildlife. Pickerel Creek flows through the '
        'western half of the area, forming a high quality freshwater estuarine habitat. One of '
        'the best shorebird areas in the state during migration. About 7 miles east of Fremont; '
        'about 8 miles north and west of Castalia.'
    ),
    'features_raw': (
        'Observation deck (year-round, along SR 6); Multiple parking areas (along SR 6 and TR 680); '
        'Network of dikes throughout wetlands; Old Vickery Road (abandoned road bisecting marsh); '
        'No restroom facilities; No parking fees'
    ),
    'difficulty_raw': None,
    'accessibility_raw': 'Observation deck accessible; no restrooms on site',
    'urls_raw': [
        'https://ohiodnr.gov/go-and-do/plan-a-visit/find-a-property/pickerel-creek-wildlife-area'
    ],
    'identity_notes_raw': (
        'Acreage discrepancy: ODNR official 3,200 ac; OOS cites 2,814 ac; use 3,200 per ODNR. '
        'Access to Sandusky Bay limited to boating down Pickerel Creek from US Route 6. '
        'Controlled waterfowl hunting; trapping rights by special drawing. Dike network and '
        'Old Vickery Road are informal trail-type features; no named trails in ODNR materials. '
        'No ODNR scenic river designation for Pickerel Creek.'
    ),
    'township_raw': None,
    'municipality_raw': None,
    'discovery_tier': 2,
    'seeded_from_baseline': True,
    'baseline_id': 'Pickerel Creek Wildlife Area'
})

data['records'].append({
    'entity_type': 'Site',
    'name_raw': 'Resthaven Wildlife Area',
    'counties_raw': ['Erie', 'Sandusky'],
    'county_primary': 'Erie',
    'ownership_raw': 'State of Ohio',
    'governance_raw': 'ODNR Division of Wildlife',
    'partner_agencies_raw': None,
    'coordination_raw': None,
    'gps_lat_raw': None,
    'gps_lon_raw': None,
    'location_raw': '1 mile north of Castalia; western boundary is Erie-Sandusky county line road; northern boundary SR 6 and Whitmore Road; Box 155, Castalia, Ohio 44824',
    'description_raw': (
        'Resthaven Wildlife Area lies centered in what was originally a wet marl prairie, known '
        'by the early settlers as the Castalia Prairie. Habitat types include woodland, brushland, '
        'wetlands, cropfields, open water, and remnants of the Castalia Prairie. Resthaven is the '
        'site of Ohios largest prairie remnant.'
    ),
    'features_raw': 'Walking trails throughout; Fishing pier (Pond 8, accessible); Handicapped accessible boat ramp and courtesy dock at northeast parking lot',
    'difficulty_raw': None,
    'accessibility_raw': 'Fishing pier accessible; boat ramp accessible',
    'urls_raw': [
        'https://ohiodnr.gov/go-and-do/plan-a-visit/find-a-property/resthaven-wildlife-area'
    ],
    'identity_notes_raw': (
        'GIS_VERIFY_COUNTY - primarily Erie County; western boundary is Erie-Sandusky county line; '
        'partial Sandusky County footprint. Primary county: Erie. Acreage: ODNR 2,218 ac; one '
        'source 2,272 ac. Primary record to be created in Erie County run. CROSS_COUNTY_CANDIDATE'
    ),
    'township_raw': None,
    'municipality_raw': None,
    'discovery_tier': 2,
    'seeded_from_baseline': False,
    'baseline_id': None
})

data['records'].append({
    'entity_type': 'Site',
    'name_raw': 'Willow Point Wildlife Area',
    'counties_raw': ['Erie', 'Sandusky'],
    'county_primary': 'Erie',
    'ownership_raw': 'State of Ohio',
    'governance_raw': 'ODNR Division of Wildlife',
    'partner_agencies_raw': None,
    'coordination_raw': None,
    'gps_lat_raw': None,
    'gps_lon_raw': None,
    'location_raw': '4 miles northwest of Castalia; primarily Erie County (Margaretta Township), small portion extending south into Sandusky County',
    'description_raw': (
        'About two-thirds of the wildlife area is open water and marshland, with woodlands and '
        'open meadows comprising the remaining acreage. Willow Point supports waterfowl, '
        'songbird, and shorebird populations.'
    ),
    'features_raw': 'Fishing; Hunting; Trapping; Paddling access; Wildlife viewing',
    'difficulty_raw': None,
    'accessibility_raw': None,
    'urls_raw': [
        'https://ohiodnr.gov/go-and-do/plan-a-visit/find-a-property/willow-point-wildlife-area'
    ],
    'identity_notes_raw': (
        'GIS_VERIFY_COUNTY - primarily Erie County (Margaretta Township); small portion extends '
        'south into Sandusky County. Primary county: Erie. Acreage discrepancy: ODNR 432 ac; '
        'other sources 645 ac (acquisition timeline 1975-1991). '
        'Primary record to be created in Erie County run. CROSS_COUNTY_CANDIDATE'
    ),
    'township_raw': None,
    'municipality_raw': None,
    'discovery_tier': 2,
    'seeded_from_baseline': False,
    'baseline_id': None
})

data['records'].append({
    'entity_type': 'Site',
    'name_raw': 'Sandusky State Scenic River',
    'counties_raw': ['Wyandot', 'Seneca', 'Sandusky'],
    'county_primary': 'Wyandot',
    'ownership_raw': 'Multiple (scenic designation, not land ownership)',
    'governance_raw': 'ODNR Scenic Rivers Program',
    'partner_agencies_raw': 'Sandusky River Watershed Coalition',
    'coordination_raw': 'Christina Kuchle, Northwest Ohio Scenic River Manager (ODNR)',
    'gps_lat_raw': None,
    'gps_lon_raw': None,
    'location_raw': '65-mile designated reach from Harrison Smith Park in Upper Sandusky (Wyandot County) to Roger Young Memorial Park in Fremont (Sandusky County)',
    'description_raw': (
        '65-mile state scenic river designation; second scenic river designated in Ohio (1970). '
        'Designated Recreational July 1, 1975; portions re-designated Scenic October 14, 1980 '
        'and April 27, 1982. The Sandusky River is the primary waterway of Sandusky County, '
        'terminating its designated reach at Roger Young Memorial Park in Fremont.'
    ),
    'features_raw': 'Paddling; Fishing; Wildlife observation; Multiple public access points along designated reach',
    'difficulty_raw': None,
    'accessibility_raw': None,
    'urls_raw': [
        'https://ohiodnr.gov/discover-and-learn/land-water/rivers-streams-wetlands/scenic-rivers-program',
        'https://sanduskyriver.org/recreation-information/'
    ],
    'identity_notes_raw': (
        'CROSS_COUNTY_CANDIDATE - spans Wyandot, Seneca, and Sandusky counties. '
        'Scenic designation, not land ownership. Category: Water Site; subtype: River; '
        'designation: State Scenic River. Wolf Creek (tributary in Fremont area) is NOT '
        'separately designated; Wolf Creek Park provides access to this scenic river. '
        'Pickerel Creek also NOT designated. No National Wild and Scenic River designation.'
    ),
    'township_raw': None,
    'municipality_raw': None,
    'discovery_tier': 2,
    'seeded_from_baseline': False,
    'baseline_id': None
})

data['records'].append({
    'entity_type': 'Site',
    'name_raw': 'Ron Abraham Forest',
    'counties_raw': ['Sandusky'],
    'county_primary': 'Sandusky',
    'ownership_raw': 'State of Ohio',
    'governance_raw': 'Ohio State University',
    'partner_agencies_raw': None,
    'coordination_raw': None,
    'gps_lat_raw': None,
    'gps_lon_raw': None,
    'location_raw': None,
    'description_raw': 'OSU-owned forest property in Sandusky County, 130.8 acres. No authoritative web presence found; property known from baseline documentation only.',
    'features_raw': None,
    'difficulty_raw': None,
    'accessibility_raw': None,
    'urls_raw': [],
    'identity_notes_raw': (
        'PUBLIC_UNIVERSITY_T2 - Ohio State University is a public university; natural areas are '
        'Tier 2 per sub-procedure 4.7. Acreage 130.8 ac per baseline. No OSU official web page '
        'found; not on OSU SENR or OSU Extension Sandusky County site. Public access status '
        'unknown. NEEDS_VERIFICATION - may not meet Tier 2 inclusion if no public access or '
        'formal designation. Recommend inquiry: extension.osu.edu/sandusky-county-office'
    ),
    'township_raw': None,
    'municipality_raw': None,
    'discovery_tier': 2,
    'seeded_from_baseline': True,
    'baseline_id': 'Ron Abraham Forest'
})

# ─── TIER 2 ACCESS POINTS ───────────────────────────────────────────

data['records'].append({
    'entity_type': 'Access Point',
    'name_raw': 'Pickerel Creek Wildlife Area - SR 6 Observation Deck',
    'counties_raw': ['Sandusky'],
    'county_primary': 'Sandusky',
    'ownership_raw': 'State of Ohio',
    'governance_raw': 'ODNR Division of Wildlife',
    'partner_agencies_raw': None,
    'coordination_raw': None,
    'gps_lat_raw': None,
    'gps_lon_raw': None,
    'location_raw': 'Along SR 6 (US Route 6), Townsend Township, Sandusky County; at Pickerel Creek Wildlife Area',
    'description_raw': 'Year-round observation deck along SR 6 at Pickerel Creek Wildlife Area; primary wildlife viewing access point for the marsh.',
    'features_raw': 'Observation deck; Parking area',
    'difficulty_raw': None,
    'accessibility_raw': None,
    'urls_raw': [
        'https://ohiodnr.gov/go-and-do/plan-a-visit/find-a-property/pickerel-creek-wildlife-area'
    ],
    'identity_notes_raw': 'Parent site: Pickerel Creek Wildlife Area. GPS needed - exact coordinates not stated in sources.',
    'township_raw': None,
    'municipality_raw': None,
    'discovery_tier': 2,
    'seeded_from_baseline': False,
    'baseline_id': None
})

data['records'].append({
    'entity_type': 'Access Point',
    'name_raw': 'Resthaven Wildlife Area - Pond 8 Fishing Pier',
    'counties_raw': ['Erie', 'Sandusky'],
    'county_primary': 'Erie',
    'ownership_raw': 'State of Ohio',
    'governance_raw': 'ODNR Division of Wildlife',
    'partner_agencies_raw': None,
    'coordination_raw': None,
    'gps_lat_raw': None,
    'gps_lon_raw': None,
    'location_raw': 'Pond 8, Resthaven Wildlife Area, near Castalia, OH (Erie-Sandusky county line)',
    'description_raw': 'Accessible fishing pier at Pond 8 within Resthaven Wildlife Area.',
    'features_raw': 'Fishing pier (accessible); Parking',
    'difficulty_raw': None,
    'accessibility_raw': 'Accessible to people with disabilities',
    'urls_raw': [
        'https://ohiodnr.gov/go-and-do/plan-a-visit/find-a-property/resthaven-wildlife-area'
    ],
    'identity_notes_raw': 'GIS_VERIFY_COUNTY - parent site straddles Erie-Sandusky county line; AP likely in Erie County. Primary county: Erie. CROSS_COUNTY_CANDIDATE',
    'township_raw': None,
    'municipality_raw': None,
    'discovery_tier': 2,
    'seeded_from_baseline': False,
    'baseline_id': None
})

data['records'].append({
    'entity_type': 'Access Point',
    'name_raw': 'Resthaven Wildlife Area - Northeast Boat Ramp',
    'counties_raw': ['Erie', 'Sandusky'],
    'county_primary': 'Erie',
    'ownership_raw': 'State of Ohio',
    'governance_raw': 'ODNR Division of Wildlife',
    'partner_agencies_raw': None,
    'coordination_raw': None,
    'gps_lat_raw': None,
    'gps_lon_raw': None,
    'location_raw': 'Northeast parking area, Resthaven Wildlife Area, near Castalia, OH',
    'description_raw': 'Handicapped accessible boat ramp with courtesy dock at northeast parking lot of Resthaven Wildlife Area.',
    'features_raw': 'Boat ramp (accessible); Courtesy dock; Parking',
    'difficulty_raw': None,
    'accessibility_raw': 'Handicapped accessible',
    'urls_raw': [
        'https://ohiodnr.gov/go-and-do/plan-a-visit/find-a-property/resthaven-wildlife-area'
    ],
    'identity_notes_raw': 'GIS_VERIFY_COUNTY - parent site straddles Erie-Sandusky county line; AP likely in Erie County. Primary county: Erie. CROSS_COUNTY_CANDIDATE',
    'township_raw': None,
    'municipality_raw': None,
    'discovery_tier': 2,
    'seeded_from_baseline': False,
    'baseline_id': None
})

f.write_text(yaml.dump(data, allow_unicode=True, sort_keys=False), encoding='utf-8')
print(f'Done. Total records: {len(data["records"])}')
