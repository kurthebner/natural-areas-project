import yaml, pathlib

f = pathlib.Path('County_Spreadsheets/Sandusky/sandusky_ohio_raw_discovery.yaml')
data = yaml.safe_load(f.read_text(encoding='utf-8'))
data.setdefault('records', [])

SCPD = 'Sandusky County Park District'
SAN  = 'Sandusky'
OH   = 'State of Ohio'
LMP  = 'https://www.lovemyparks.com'

# ─── TIER 3 SITES — SCPD PARKS ──────────────────────────────────────

data['records'].append({
    'entity_type': 'Site',
    'name_raw': 'Blue Heron Reserve',
    'counties_raw': [SAN],
    'county_primary': SAN,
    'ownership_raw': OH,
    'governance_raw': SCPD,
    'partner_agencies_raw': 'The Nature Conservancy (donated); federal Land and Water Conservation Fund (grant)',
    'coordination_raw': None,
    'gps_lat_raw': None,
    'gps_lon_raw': None,
    'location_raw': '2134 County Road 260, Vickery, OH 43464',
    'description_raw': 'Located in northeast Sandusky County on the edge of Lake Erie marshes, this property features constructed wetlands and wet woods. The site is a birder\'s paradise with habitat supporting migrating warblers, waterfowl, and bald eagles.',
    'features_raw': 'Constructed wetlands; Wet woods; Part of Lake Erie Birding Trail (ODNR/Ohio Sea Grant, 88 birding locations along Lake Erie Coast)',
    'difficulty_raw': None,
    'accessibility_raw': None,
    'urls_raw': [LMP + '/parks/blue-heron-reserve'],
    'identity_notes_raw': 'Part of Lake Erie Birding Trail. No named trails listed. Birding/wildlife observation primary use.',
    'township_raw': None,
    'municipality_raw': None,
    'discovery_tier': 3,
    'seeded_from_baseline': True,
    'baseline_id': 'Blue Heron Reserve'
})

data['records'].append({
    'entity_type': 'Site',
    'name_raw': 'Christy Farm Nature Preserve',
    'counties_raw': [SAN],
    'county_primary': SAN,
    'ownership_raw': OH,
    'governance_raw': SCPD,
    'partner_agencies_raw': None,
    'coordination_raw': None,
    'gps_lat_raw': None,
    'gps_lon_raw': None,
    'location_raw': '2020 Old Oak Harbor Road, Fremont, OH 43420',
    'description_raw': 'Named after the Christy Family, who established the Christy Knife Company in 1891 in Fremont, Ohio, this 151-acre property consists of woodlands and wetland areas.',
    'features_raw': 'Walking paths along Muskellunge Creek; Active heron rookery; The Cabin (built 1936 by Christy family and Kiwanis Club of Fremont, available for youth group overnights)',
    'difficulty_raw': None,
    'accessibility_raw': None,
    'urls_raw': [LMP + '/parks/christy-farm-nature-preserve'],
    'identity_notes_raw': 'Walking paths along Muskellunge Creek present; no named trails. Youth cabin rentals available.',
    'township_raw': None,
    'municipality_raw': None,
    'discovery_tier': 3,
    'seeded_from_baseline': True,
    'baseline_id': 'Christy Farm Nature Preserve'
})

data['records'].append({
    'entity_type': 'Site',
    'name_raw': 'Creek Bend Farm',
    'counties_raw': [SAN],
    'county_primary': SAN,
    'ownership_raw': OH,
    'governance_raw': SCPD,
    'partner_agencies_raw': None,
    'coordination_raw': None,
    'gps_lat_raw': None,
    'gps_lon_raw': None,
    'location_raw': '720 South Main Street, Lindsey, OH 43442',
    'description_raw': 'Located along the banks of Muddy Creek, Creek Bend Farm is home to the Wilson Nature Center and the Homestead House. Visitors can experience this 310-acre property on over two miles of trails travelling through riparian, field, and woodland habitats as well as active farm land.',
    'features_raw': 'Wilson Nature Center; Homestead House (1940s); Rentable barn; Over 2 miles of trails; Riparian, field, and woodland habitats; Active farmland; Spring and fall migration birding',
    'difficulty_raw': None,
    'accessibility_raw': None,
    'urls_raw': [
        LMP + '/parks/creek-bend-farm',
        LMP + '/parks/creek-bend-park/wilson-nature-center',
        LMP + '/parks/creek-bend-park/homestead-house'
    ],
    'identity_notes_raw': 'Wilson Nature Center is identity-bearing internal feature; may warrant child Site. 2+ miles of trails present; no individual trail names stated on SCPD website. Note: baseline listed as "has nature center."',
    'township_raw': None,
    'municipality_raw': None,
    'discovery_tier': 3,
    'seeded_from_baseline': True,
    'baseline_id': 'Creek Bend Farm'
})

data['records'].append({
    'entity_type': 'Site',
    'name_raw': 'Decoy Marsh',
    'counties_raw': [SAN],
    'county_primary': SAN,
    'ownership_raw': OH,
    'governance_raw': SCPD,
    'partner_agencies_raw': None,
    'coordination_raw': None,
    'gps_lat_raw': None,
    'gps_lon_raw': None,
    'location_raw': '2700 County Road 259, Fremont, OH 43420',
    'description_raw': 'Previously a private hunt club, this 67-acre property consists of wetlands and diked marsh areas. Bordered by privately owned conservation lands and Green Creek this area is an important part of the Lake Erie marshes and is an excellent area for spring birding.',
    'features_raw': 'Wetlands; Diked marsh areas; Green Creek border; Spring birding access (opens May)',
    'difficulty_raw': None,
    'accessibility_raw': None,
    'urls_raw': [LMP + '/parks/decoy-march'],
    'identity_notes_raw': 'Program use only; opens during May for spring migration only. Not generally open to public. URL on SCPD site contains typo "decoy-march" (correct: "decoy-marsh").',
    'township_raw': None,
    'municipality_raw': None,
    'discovery_tier': 3,
    'seeded_from_baseline': True,
    'baseline_id': 'Decoy Marsh'
})

data['records'].append({
    'entity_type': 'Site',
    'name_raw': 'Don W. Miller Memorial Park',
    'counties_raw': [SAN],
    'county_primary': SAN,
    'ownership_raw': OH,
    'governance_raw': SCPD,
    'partner_agencies_raw': 'Black Swamp Conservancy (donated)',
    'coordination_raw': None,
    'gps_lat_raw': None,
    'gps_lon_raw': None,
    'location_raw': '1329 Tiffin Street, Fremont, OH 43420',
    'description_raw': 'Located on the Sandusky River adjacent to the Blue Banks. The portion of river holds state scenic designation. Donated by Black Swamp Conservancy. Renamed in 2023 to honor Don W. Miller (founder of Miller Pipeline and Miller Cable Company). Renovations funded by donations totaling $500,000+.',
    'features_raw': 'Fishing; Birding; Hiking trails; Fremont Rotary Lodge (renovations ongoing); Administrative offices (SCPD HQ)',
    'difficulty_raw': None,
    'accessibility_raw': None,
    'urls_raw': [LMP + '/parks/don-w-miller-memorial-park'],
    'identity_notes_raw': 'Formerly known as River Cliff Park. Renamed April 27, 2023. Located on Sandusky State Scenic River. Hiking trails present; no individual trail names stated. Also serves as SCPD administrative HQ. This is a different park than Wolf Creek Park.',
    'township_raw': None,
    'municipality_raw': None,
    'discovery_tier': 3,
    'seeded_from_baseline': True,
    'baseline_id': 'Don W. Miller Memorial Park'
})

data['records'].append({
    'entity_type': 'Site',
    'name_raw': 'Franklin & Phillip Rosa Wildlife Preserve',
    'counties_raw': [SAN],
    'county_primary': SAN,
    'ownership_raw': OH,
    'governance_raw': SCPD,
    'partner_agencies_raw': None,
    'coordination_raw': None,
    'gps_lat_raw': None,
    'gps_lon_raw': None,
    'location_raw': '3861 County Road 184, Fremont, OH 43420',
    'description_raw': 'Located at the mouth of Muddy Creek this wetland area is used for programming purposes only.',
    'features_raw': None,
    'difficulty_raw': None,
    'accessibility_raw': None,
    'urls_raw': [LMP + '/parks/franklin-and-phillip-rosa-wildlife-preserve'],
    'identity_notes_raw': 'Program use only; not open to general public. Baseline used "Rose" but SCPD website uses "Rosa" — name_raw uses official website spelling. Wetland at Muddy Creek mouth.',
    'township_raw': None,
    'municipality_raw': None,
    'discovery_tier': 3,
    'seeded_from_baseline': True,
    'baseline_id': 'Franklin & Phillip Rose Wildlife Preserve'
})

data['records'].append({
    'entity_type': 'Site',
    'name_raw': 'Green Creek Township & Reserve',
    'counties_raw': [SAN],
    'county_primary': SAN,
    'ownership_raw': OH,
    'governance_raw': SCPD,
    'partner_agencies_raw': 'US Fish and Wildlife Service; Ohio Division of Wildlife (restoration partners)',
    'coordination_raw': None,
    'gps_lat_raw': None,
    'gps_lon_raw': None,
    'location_raw': 'Off County Road 195 south of Clyde, Sandusky County',
    'description_raw': 'Acquired October 2005. Partnered with US Fish and Wildlife Service and Ohio Division of Wildlife to restore the farmland back to a grassland habitat. 72 acres planted with native grasses and wildflowers.',
    'features_raw': 'Native grassland (72 ac restored); Native grasses and wildflowers',
    'difficulty_raw': None,
    'accessibility_raw': None,
    'urls_raw': [LMP + '/parks/green-creek-township-reserve'],
    'identity_notes_raw': 'Closed to public; program use only. Baseline called this "Green Creek Township Property." Official SCPD name is "Green Creek Township & Reserve." 90 ac total; 72 ac native grasses/wildflowers.',
    'township_raw': None,
    'municipality_raw': None,
    'discovery_tier': 3,
    'seeded_from_baseline': True,
    'baseline_id': 'Green Creek Township Property'
})

data['records'].append({
    'entity_type': 'Site',
    'name_raw': 'Muddy Creek Reserve',
    'counties_raw': [SAN],
    'county_primary': SAN,
    'ownership_raw': OH,
    'governance_raw': SCPD,
    'partner_agencies_raw': None,
    'coordination_raw': None,
    'gps_lat_raw': None,
    'gps_lon_raw': None,
    'location_raw': 'Rice Township, off CR 157, Fremont, OH 43420',
    'description_raw': 'Acquired June 2010. Wetland and wet woods habitat, as well as a portion of Muddy Creek near the mouth of Muddy Creek Bay.',
    'features_raw': 'Purple Martin colony; American Lotus blooms; Abundant waterfowl; Wetlands; Wet woods; Muddy Creek waterway',
    'difficulty_raw': None,
    'accessibility_raw': None,
    'urls_raw': [LMP + '/parks/muddy-creek-reserve'],
    'identity_notes_raw': 'Program use only. Distinct entity from Muddy Creek Preserve (Western Wildlife Corridor/Black Swamp Conservancy — Tier 7). 80 ac per SCPD and baseline.',
    'township_raw': None,
    'municipality_raw': None,
    'discovery_tier': 3,
    'seeded_from_baseline': True,
    'baseline_id': 'Muddy Creek Reserve'
})

data['records'].append({
    'entity_type': 'Site',
    'name_raw': 'Mull Covered Bridge',
    'counties_raw': [SAN],
    'county_primary': SAN,
    'ownership_raw': OH,
    'governance_raw': SCPD,
    'partner_agencies_raw': 'Sandusky County Commissioners; Sandusky County Engineers Office (joint operation)',
    'coordination_raw': None,
    'gps_lat_raw': None,
    'gps_lon_raw': None,
    'location_raw': '1515 County Road 9, Fremont, OH 43420',
    'description_raw': 'Listed on the National Register of Historic Places this "town lattice" truss type bridge is one of the last remaining covered bridges in Northwest Ohio. Built 1851 by the Henry Mull family; originally for trade access to the Mull Mill. Closed to vehicle traffic 1962 when road was diverted. 2016 renovation completed.',
    'features_raw': 'Covered bridge (pedestrian use); Reservable shelter area; Limited parking',
    'difficulty_raw': None,
    'accessibility_raw': None,
    'urls_raw': [LMP + '/parks/mull-covered-bridge'],
    'identity_notes_raw': 'NRHP-listed. Bridge ID 35-72-01 per baseline. Jointly operated by SCPD, Sandusky County Commissioners, and Sandusky County Engineers. Open for pedestrian use.',
    'township_raw': None,
    'municipality_raw': None,
    'discovery_tier': 3,
    'seeded_from_baseline': True,
    'baseline_id': 'Mull Covered Bridge'
})

data['records'].append({
    'entity_type': 'Site',
    'name_raw': 'Redhorse Bend',
    'counties_raw': [SAN],
    'county_primary': SAN,
    'ownership_raw': OH,
    'governance_raw': SCPD,
    'partner_agencies_raw': 'Black Swamp Conservancy (land restoration); ODNR H2Ohio program (grant funding)',
    'coordination_raw': None,
    'gps_lat_raw': None,
    'gps_lon_raw': None,
    'location_raw': '1616 North River Road, Fremont, OH 43420',
    'description_raw': 'This property sits on both sides of the Route 20 bypass (between exits 6 and 53) and encompasses nearly a mile of Sandusky River frontage plus 16 acres of forest and wetlands. Previously farmland prone to flooding. Black Swamp Conservancy restored over 60 acres of former farmland into wetlands and established a pollinator meadow using ODNR H2Ohio grant funding. Received as a gift to SCPD in June 2022. Name references the Redhorse Sucker fish as an indicator of river health.',
    'features_raw': 'Wetlands (60+ ac restored); Pollinator meadow; Sandusky River frontage (nearly 1 mile)',
    'difficulty_raw': None,
    'accessibility_raw': None,
    'urls_raw': [LMP + '/parks/redhorse-bend'],
    'identity_notes_raw': 'Program use only. Acquired June 2022. Located on Sandusky State Scenic River. Split by Route 20 bypass between exits 6 and 53.',
    'township_raw': None,
    'municipality_raw': None,
    'discovery_tier': 3,
    'seeded_from_baseline': True,
    'baseline_id': 'Redhorse Bend'
})

data['records'].append({
    'entity_type': 'Site',
    'name_raw': 'Ringneck Ridge',
    'counties_raw': [SAN],
    'county_primary': SAN,
    'ownership_raw': OH,
    'governance_raw': SCPD,
    'partner_agencies_raw': 'ODNR Division of Wildlife (pheasant releases)',
    'coordination_raw': None,
    'gps_lat_raw': None,
    'gps_lon_raw': None,
    'location_raw': '1818 Township Road 74 (south entrance/archery); 2026 Township Road 74, Gibsonburg, OH 43431 (north entrance)',
    'description_raw': 'Previously a private hunt club, this area is still managed as a wildlife area to provide public hunting opportunities. The diverse habitats include open fields, woodlands, wet meadows, and limestone barrens.',
    'features_raw': 'Food plots throughout the property; Pheasant releases (fall, in conjunction with ODNR); Archery range',
    'difficulty_raw': None,
    'accessibility_raw': None,
    'urls_raw': [LMP + '/parks/ringneck-ridge'],
    'identity_notes_raw': (
        'Managed by SCPD, NOT ODNR directly. ODNR releases pheasants here under special permit. '
        'Previously noted as "Ringneck Ridge Wildlife Area" in baseline with state wildlife area '
        'designation — this is SCPD-managed; no separate ODNR state wildlife area record confirmed. '
        'Baseline acreage 360 ac (not listed on SCPD website). Public hunting and archery access. '
        'Two entrances on TR 74.'
    ),
    'township_raw': None,
    'municipality_raw': None,
    'discovery_tier': 3,
    'seeded_from_baseline': True,
    'baseline_id': 'Ringneck Ridge'
})

data['records'].append({
    'entity_type': 'Site',
    'name_raw': 'Shelley Wetland',
    'counties_raw': [SAN],
    'county_primary': SAN,
    'ownership_raw': OH,
    'governance_raw': SCPD,
    'partner_agencies_raw': None,
    'coordination_raw': None,
    'gps_lat_raw': None,
    'gps_lon_raw': None,
    'location_raw': 'Intersection of CR 292 & TR 177, Bellevue, OH 44811',
    'description_raw': 'Bowl-shaped wetland was created when gravel was removed for railway construction in the late 1800s (New York, Chicago and St. Louis Railway / Nickel Plate Railroad). Donated by Mr. & Mrs. James Shelley in honor of his parents, Paul & Kate Shelley.',
    'features_raw': None,
    'difficulty_raw': None,
    'accessibility_raw': None,
    'urls_raw': [LMP + '/parks/shelley-wetland'],
    'identity_notes_raw': 'Closed to the public; scheduled program use only. 17 ac. Address uses Bellevue OH 44811 zip but Bellevue straddles Huron-Sandusky county line. GIS_VERIFY_COUNTY — confirm this parcel is in Sandusky County.',
    'township_raw': None,
    'municipality_raw': None,
    'discovery_tier': 3,
    'seeded_from_baseline': True,
    'baseline_id': 'Shelley Wetland'
})

data['records'].append({
    'entity_type': 'Site',
    'name_raw': 'Tea Kaufman Homestead',
    'counties_raw': [SAN],
    'county_primary': SAN,
    'ownership_raw': OH,
    'governance_raw': SCPD,
    'partner_agencies_raw': None,
    'coordination_raw': None,
    'gps_lat_raw': None,
    'gps_lon_raw': None,
    'location_raw': '2091 County Road 292, Bellevue, OH 44811',
    'description_raw': 'This 14-acre property is directly adjacent to the North Coast Inland Trail and serves as an access point to the trail. The Tea Kaufman Homestead property has a mowed loop trail that takes visitors through a small prairie.',
    'features_raw': 'Mowed loop trail (prairie); North Coast Inland Trail access point; Parking',
    'difficulty_raw': None,
    'accessibility_raw': None,
    'urls_raw': [LMP + '/parks/tea-kaufman-homestead'],
    'identity_notes_raw': (
        'Serves as official NCIT access point (listed as Access Point 1 on SCPD NCIT page). '
        'Address uses Bellevue OH 44811 zip — confirm Sandusky County parcel. GIS_VERIFY_COUNTY. '
        'KNOWN_MC:OH-MC-T-0110 — this is an Access Point for the North Coast Inland Trail.'
    ),
    'township_raw': None,
    'municipality_raw': None,
    'discovery_tier': 3,
    'seeded_from_baseline': True,
    'baseline_id': 'Tea Kaufman Homestead'
})

data['records'].append({
    'entity_type': 'Site',
    'name_raw': 'The Woods at the Luscombe Farm',
    'counties_raw': [SAN],
    'county_primary': SAN,
    'ownership_raw': OH,
    'governance_raw': SCPD,
    'partner_agencies_raw': None,
    'coordination_raw': None,
    'gps_lat_raw': None,
    'gps_lon_raw': None,
    'location_raw': '2341 County Road 213, Clyde, OH 43410',
    'description_raw': 'A 1-mile loop trail meanders through this picturesque 55-acre woodlot which consists of maples, hickories, oaks, and spicebush.',
    'features_raw': '1-mile loop trail; Maples, hickories, oaks, spicebush forest',
    'difficulty_raw': None,
    'accessibility_raw': None,
    'urls_raw': [LMP + '/parks/the-woods-at-the-luscombe-farm'],
    'identity_notes_raw': 'Loop trail present; no individual trail name stated on SCPD website.',
    'township_raw': None,
    'municipality_raw': None,
    'discovery_tier': 3,
    'seeded_from_baseline': True,
    'baseline_id': 'The Woods at the Luscombe Farm'
})

# White Star Park — parent + 4 child sites
data['records'].append({
    'entity_type': 'Site',
    'name_raw': 'White Star Park',
    'counties_raw': [SAN],
    'county_primary': SAN,
    'ownership_raw': OH,
    'governance_raw': SCPD,
    'partner_agencies_raw': 'Federal Land and Water Conservation Fund (development funding)',
    'coordination_raw': None,
    'gps_lat_raw': None,
    'gps_lon_raw': None,
    'location_raw': '925 South Main Street, Gibsonburg, OH 43431',
    'description_raw': 'White Star was a quarry operation for mining limestone. It was developed with Federal Land & Water Conservation Fund money and the sale of scrap metal from the site. 797-acre park with four distinct areas: White Star Quarry, White Star Campground, White Star Barn and Historical Cabins, and Doug Haubert Wetland.',
    'features_raw': 'Quarry swimming/beach (seasonal); Scuba diving; Fishing; Boating (hand-powered and electric only); Campground (48 sites, water/electric); Shelter rentals; Reconstructed 1870s log cabins; Trail system; Sledding hill; Horseback riding (selected trails); Hunting; Birding',
    'difficulty_raw': None,
    'accessibility_raw': None,
    'urls_raw': [
        LMP + '/parks/white-star-park',
        LMP + '/parks/white-star-park/white-star-quarry',
        LMP + '/parks/white-star-park/white-star-barn-and-cabins',
        LMP + '/parks/white-star-park/doug-haubert-wetland'
    ],
    'identity_notes_raw': '797 ac total across 4 sub-areas. Child sites: White Star Quarry, White Star Campground, White Star Barn and Historical Cabins, Doug Haubert Wetland. Quarry has 0.8-mile loop trail. Campground address is 910 S Main St, Gibsonburg. Barn/Cabins address is 5013 CR 65. Doug Haubert Wetland address is 1330 CR 66.',
    'township_raw': None,
    'municipality_raw': None,
    'discovery_tier': 3,
    'seeded_from_baseline': True,
    'baseline_id': 'White Star Park'
})

data['records'].append({
    'entity_type': 'Site',
    'name_raw': 'White Star Quarry',
    'counties_raw': [SAN],
    'county_primary': SAN,
    'ownership_raw': OH,
    'governance_raw': SCPD,
    'partner_agencies_raw': None,
    'coordination_raw': None,
    'gps_lat_raw': None,
    'gps_lon_raw': None,
    'location_raw': '925 South Main Street, Gibsonburg, OH 43431',
    'description_raw': 'Limestone quarry area of White Star Park. Features beach swimming, scuba diving, fishing, and boating. Seasonal (Memorial Day through Labor Day).',
    'features_raw': 'Beach (seasonal); Scuba diving; Shelter rentals; Fishing; Boating (hand-powered and electric motors only); 0.8-mile trail circling the quarry',
    'difficulty_raw': None,
    'accessibility_raw': None,
    'urls_raw': [LMP + '/parks/white-star-park/white-star-quarry'],
    'identity_notes_raw': 'Child site of White Star Park. 0.8-mile quarry loop trail present.',
    'township_raw': None,
    'municipality_raw': None,
    'discovery_tier': 3,
    'seeded_from_baseline': False,
    'baseline_id': None
})

data['records'].append({
    'entity_type': 'Site',
    'name_raw': 'White Star Campground',
    'counties_raw': [SAN],
    'county_primary': SAN,
    'ownership_raw': OH,
    'governance_raw': SCPD,
    'partner_agencies_raw': None,
    'coordination_raw': None,
    'gps_lat_raw': None,
    'gps_lon_raw': None,
    'location_raw': '910 South Main Street, Gibsonburg, OH 43431',
    'description_raw': '48-site campground within White Star Park. Open April 15 through November 1.',
    'features_raw': '48 sites with water and electric hookups; Shower house; Open April 15 - November 1; Online reservations only',
    'difficulty_raw': None,
    'accessibility_raw': None,
    'urls_raw': [LMP + '/parks/white-star-park'],
    'identity_notes_raw': 'Child site of White Star Park. Reservation-only; no walk-ins. Check-in 2 PM, check-out noon.',
    'township_raw': None,
    'municipality_raw': None,
    'discovery_tier': 3,
    'seeded_from_baseline': False,
    'baseline_id': None
})

data['records'].append({
    'entity_type': 'Site',
    'name_raw': 'White Star Barn and Historical Cabins',
    'counties_raw': [SAN],
    'county_primary': SAN,
    'ownership_raw': OH,
    'governance_raw': SCPD,
    'partner_agencies_raw': None,
    'coordination_raw': None,
    'gps_lat_raw': None,
    'gps_lon_raw': None,
    'location_raw': '5013 County Road 65, Gibsonburg, OH 43431',
    'description_raw': 'Sub-area of White Star Park featuring two reconstructed 1870s log cabins, an extensive trail system, and a sledding hill. Rentable barn and shed.',
    'features_raw': 'Two reconstructed 1870s log cabins; Extensive trail system (lengths/surfaces not specified); Sledding hill; Rentable barn and shed',
    'difficulty_raw': None,
    'accessibility_raw': None,
    'urls_raw': [LMP + '/parks/white-star-park/white-star-barn-and-cabins'],
    'identity_notes_raw': 'Child site of White Star Park. Trail system present; no individual trail names or lengths stated. Log cabins are reconstructed historic structures.',
    'township_raw': None,
    'municipality_raw': None,
    'discovery_tier': 3,
    'seeded_from_baseline': False,
    'baseline_id': None
})

data['records'].append({
    'entity_type': 'Site',
    'name_raw': 'Doug Haubert Wetland',
    'counties_raw': [SAN],
    'county_primary': SAN,
    'ownership_raw': OH,
    'governance_raw': SCPD,
    'partner_agencies_raw': None,
    'coordination_raw': None,
    'gps_lat_raw': None,
    'gps_lon_raw': None,
    'location_raw': '1330 County Road 66, Gibsonburg, OH 43431',
    'description_raw': 'Constructed wetland habitat sub-area of White Star Park. Open for birding, horseback riding, and hunting.',
    'features_raw': 'Constructed wetland habitat; Birding; Horseback riding on selected trails; Hunting permitted',
    'difficulty_raw': None,
    'accessibility_raw': None,
    'urls_raw': [LMP + '/parks/white-star-park/doug-haubert-wetland'],
    'identity_notes_raw': 'Child site of White Star Park.',
    'township_raw': None,
    'municipality_raw': None,
    'discovery_tier': 3,
    'seeded_from_baseline': False,
    'baseline_id': None
})

data['records'].append({
    'entity_type': 'Site',
    'name_raw': 'Wolf Creek Park',
    'counties_raw': [SAN],
    'county_primary': SAN,
    'ownership_raw': 'Ohio Department of Natural Resources (owned); State of Ohio',
    'governance_raw': SCPD,
    'partner_agencies_raw': 'ODNR (land owner; SCPD manages under agreement)',
    'coordination_raw': None,
    'gps_lat_raw': None,
    'gps_lon_raw': None,
    'location_raw': 'North Entrance: 2409 South State Route 53, Fremont, OH 43420; South Entrance: 2701 State Route 53, Fremont, OH 43420',
    'description_raw': 'Nestled along the banks of the Sandusky River, Wolf Creek Park is an excellent area for birding, hiking, and spring wildflowers.',
    'features_raw': 'Canoe/kayak launch (North Entrance); Rentable shelter (North Entrance); Hiking trails (approximately 1.5 miles at South Entrance); Camping area (currently closed to public)',
    'difficulty_raw': None,
    'accessibility_raw': None,
    'urls_raw': [LMP + '/parks/wolf-creek-park'],
    'identity_notes_raw': (
        'ODNR-owned; SCPD-managed (per baseline: owned by ODNR, managed by SCPD). Located on '
        'Sandusky State Scenic River; Wolf Creek is a tributary of Sandusky River. Two entrances '
        'on SR 53. Birding databases list as "Wolf Creek Park - Sandusky Scenic River Access." '
        'Approx. 1.5 miles of trails at South Entrance; no named trails. Camping currently closed.'
    ),
    'township_raw': None,
    'municipality_raw': None,
    'discovery_tier': 3,
    'seeded_from_baseline': True,
    'baseline_id': 'Wolf Creek Park'
})

# ─── TIER 3 TRAILS ──────────────────────────────────────────────────

# North Coast Inland Trail — KNOWN MC entity
data['records'].append({
    'entity_type': 'Trail',
    'name_raw': 'North Coast Inland Trail',
    'counties_raw': ['Erie', 'Huron', 'Ottawa', SAN],
    'county_primary': SAN,
    'ownership_raw': OH,
    'governance_raw': SCPD,
    'partner_agencies_raw': None,
    'coordination_raw': None,
    'gps_lat_raw': None,
    'gps_lon_raw': None,
    'location_raw': '28-mile segment in Sandusky County, Ohio; travels between Elmore (Ottawa County) and Bellevue (Huron County)',
    'description_raw': None,
    'features_raw': None,
    'difficulty_raw': None,
    'accessibility_raw': 'Multi-use: walking, biking, in-line skating; open year-round; motorized vehicles prohibited',
    'urls_raw': [LMP + '/parks/north-coast-inland-trail'],
    'identity_notes_raw': (
        'KNOWN_MC:OH-MC-T-0110 — this is the Sandusky County segment of the existing multi-county '
        'North Coast Inland Trail. DB record OH-MC-T-0110 counties: Erie;Huron;Ottawa;Sandusky. '
        'Also designated as part of the Buckeye Trail (statewide). SCPD manages the 28-mile '
        'Sandusky County segment. 10 documented access points in Sandusky County (see APs below). '
        'Walter Ory Park (Elmore, OH 43416) is in Ottawa County, not Sandusky County.'
    ),
    'township_raw': None,
    'municipality_raw': None,
    'discovery_tier': 3,
    'seeded_from_baseline': True,
    'baseline_id': 'North Coast Inland Trail segment'
})

# White Star Quarry loop trail
data['records'].append({
    'entity_type': 'Trail',
    'name_raw': 'White Star Quarry Loop Trail',
    'counties_raw': [SAN],
    'county_primary': SAN,
    'ownership_raw': OH,
    'governance_raw': SCPD,
    'partner_agencies_raw': None,
    'coordination_raw': None,
    'gps_lat_raw': None,
    'gps_lon_raw': None,
    'location_raw': 'White Star Quarry, 925 South Main Street, Gibsonburg, OH 43431',
    'description_raw': None,
    'features_raw': None,
    'difficulty_raw': None,
    'accessibility_raw': None,
    'urls_raw': [LMP + '/parks/white-star-park/white-star-quarry'],
    'identity_notes_raw': '0.8-mile loop circling the quarry. Name inferred from description; SCPD page says "0.8-mile trail circling the quarry" — no formal name given. Parent site: White Star Quarry.',
    'township_raw': None,
    'municipality_raw': None,
    'discovery_tier': 3,
    'seeded_from_baseline': False,
    'baseline_id': None
})

# ─── TIER 3 ACCESS POINTS — NCIT ────────────────────────────────────

# SCPD-managed NCIT access points (municipal APs will be staged at T6)
data['records'].append({
    'entity_type': 'Access Point',
    'name_raw': 'North Coast Inland Trail - Tea Kaufman Homestead Access',
    'counties_raw': [SAN],
    'county_primary': SAN,
    'ownership_raw': OH,
    'governance_raw': SCPD,
    'partner_agencies_raw': None,
    'coordination_raw': None,
    'gps_lat_raw': None,
    'gps_lon_raw': None,
    'location_raw': '2091 County Road 292, Bellevue, OH 44811',
    'description_raw': 'NCIT access point at Tea Kaufman Homestead (Access Point 1 on SCPD NCIT map). Adjacent to Tea Kaufman Homestead site.',
    'features_raw': 'NCIT trailhead; Parking; Mowed loop trail access (Tea Kaufman Homestead prairie)',
    'difficulty_raw': None,
    'accessibility_raw': None,
    'urls_raw': [LMP + '/parks/north-coast-inland-trail'],
    'identity_notes_raw': 'KNOWN_MC:OH-MC-T-0110. GIS_VERIFY_COUNTY — Bellevue 44811 zip straddles Huron-Sandusky county line.',
    'township_raw': None,
    'municipality_raw': None,
    'discovery_tier': 3,
    'seeded_from_baseline': False,
    'baseline_id': None
})

data['records'].append({
    'entity_type': 'Access Point',
    'name_raw': 'North Coast Inland Trail - Mosser Park Access',
    'counties_raw': [SAN],
    'county_primary': SAN,
    'ownership_raw': OH,
    'governance_raw': SCPD,
    'partner_agencies_raw': None,
    'coordination_raw': None,
    'gps_lat_raw': None,
    'gps_lon_raw': None,
    'location_raw': '1630 Walter Avenue, Fremont, OH 43420',
    'description_raw': 'NCIT access/shelter facility at Mosser Park (Access Point 7 on SCPD NCIT map). Open-sided shelter with 60-person capacity.',
    'features_raw': 'NCIT trailhead; Shelter (open-sided, 10 picnic tables, 60-person capacity); Parking; Portable toilets; Bike rack; Water fountain',
    'difficulty_raw': None,
    'accessibility_raw': None,
    'urls_raw': [LMP + '/register-reserve/mossar-park'],
    'identity_notes_raw': 'KNOWN_MC:OH-MC-T-0110. Shelter reservable ($50 county residents, $75 non-residents). This is a shelter facility on the NCIT, not a standalone natural area park.',
    'township_raw': None,
    'municipality_raw': None,
    'discovery_tier': 3,
    'seeded_from_baseline': False,
    'baseline_id': None
})

# Wolf Creek Park access points
data['records'].append({
    'entity_type': 'Access Point',
    'name_raw': 'Wolf Creek Park - North Entrance Canoe/Kayak Launch',
    'counties_raw': [SAN],
    'county_primary': SAN,
    'ownership_raw': 'Ohio Department of Natural Resources (owned)',
    'governance_raw': SCPD,
    'partner_agencies_raw': None,
    'coordination_raw': None,
    'gps_lat_raw': None,
    'gps_lon_raw': None,
    'location_raw': '2409 South State Route 53, Fremont, OH 43420',
    'description_raw': 'Canoe and kayak launch at the north entrance of Wolf Creek Park on the Sandusky River.',
    'features_raw': 'Canoe/kayak launch; Rentable shelter; Parking',
    'difficulty_raw': None,
    'accessibility_raw': None,
    'urls_raw': [LMP + '/parks/wolf-creek-park'],
    'identity_notes_raw': 'Parent site: Wolf Creek Park (ODNR-owned, SCPD-managed). On Sandusky State Scenic River. North entrance at 2409 S SR 53.',
    'township_raw': None,
    'municipality_raw': None,
    'discovery_tier': 3,
    'seeded_from_baseline': False,
    'baseline_id': None
})

f.write_text(yaml.dump(data, allow_unicode=True, sort_keys=False), encoding='utf-8')
t3 = [r for r in data['records'] if r.get('discovery_tier') == 3]
sites = [r for r in t3 if r['entity_type'] == 'Site']
trails = [r for r in t3 if r['entity_type'] == 'Trail']
aps = [r for r in t3 if r['entity_type'] == 'Access Point']
print(f'T3 staged: {len(sites)} Sites, {len(trails)} Trails, {len(aps)} APs')
print(f'Total records in file: {len(data["records"])}')
