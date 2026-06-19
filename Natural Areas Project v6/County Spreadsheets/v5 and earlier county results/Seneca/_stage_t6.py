import yaml, pathlib

f = pathlib.Path(r"D:\users\user1\Documents\CP Projects\Natural Areas Project v5\County_Spreadsheets\Seneca\seneca_ohio_raw_discovery.yaml")
data = yaml.safe_load(f.read_text(encoding="utf-8"))
data.setdefault("records", [])
data.setdefault("tier_nulls", [])

# ============================================================
# TIER 6 — MUNICIPAL
# Sources:
#   Tiffin: https://www.tiffinohio.gov/departments/parks-rec/parks (all 16 park pages fetched)
#           https://www.tiffinohio.gov/departments/parks-rec/facilities/trails
#           https://www.tiffinohio.gov/departments/parks-rec/facilities/east-green
#           https://www.destinationsenecacounty.org/place-category/things-to-do/outdoors-recreation/
#   Fostoria: https://fostoriaohio.gov/parks-and-rec
#             https://www.destinationsenecacounty.org/place/fostoria-reservoirs/
#   Attica: http://www.atticaohio.us/parks-and-recreation
#   Bloomville: Destination Seneca County (Beeghly Park)
#   New Riegel: https://www.destinationsenecacounty.org/place/new-riegel-park/
#   Bellevue: https://www.bellevueohio.gov/departments/parks_recreation/parks_facilities/parks/index.php
#             DB query confirmed OH-SAN-S-072 through OH-SAN-S-078 cover all 7 current parks exactly
#   Green Springs: gsohio.org (parks page 404); Whirlpool Park confirmed CLOSED (Yelp Dec 2025);
#                  Beaver Creek Reservoir = Sandusky County / City of Clyde — not Seneca T6
#   Republic: no village-owned parks found; Clinton Lake Camping = private
#   Bettsville: H.P. Eells Park already handled at T3 (governance uncertain)
# ============================================================

TIFFIN_GOV = "City of Tiffin Parks and Recreation Department"
TIFFIN_OWN = "City of Tiffin"
TIFFIN_PARKS_INDEX = "https://www.tiffinohio.gov/departments/parks-rec/parks"

FOSTORIA_GOV = "City of Fostoria Parks and Recreation"
FOSTORIA_OWN = "City of Fostoria"

# ============================================================
# TIFFIN SITES (17)
# ============================================================

tiffin_sites = [
    {
        "entity_type": "Site",
        "name_raw": "Hedges-Boyer Park",
        "counties_raw": ["Seneca"],
        "county_primary": "Seneca",
        "ownership_raw": TIFFIN_OWN,
        "governance_raw": TIFFIN_GOV,
        "partner_agencies_raw": None,
        "coordination_raw": None,
        "gps_lat_raw": None,
        "gps_lon_raw": None,
        "location_raw": "Coe Street and Summit Street, Tiffin, OH 44883",
        "acres_raw": "78",
        "description_raw": (
            "Tiffin's largest community park, 78 acres with Rock Creek running through it, bridging "
            "Coe St. and Summit St. Home to many year-round special events. Contains three baseball/softball "
            "diamonds, two football fields, basketball, sand volleyball, tennis and pickleball courts, 18-hole "
            "disc-golf course, inclusive 10,000-sq-ft playground (opened 2022), entertainment band pavilion, "
            "and Municipal Swimming Pool with 300,000-gallon main pool. Several miles of paved walking/biking "
            "trails (0.8-mile loop + 1.1 miles of finger trails). Trailhead for Rock Creek Trail leading "
            "to downtown Tiffin."
        ),
        "features_raw": [
            "Baseball/Softball (3 diamonds)",
            "Football fields (2)",
            "Basketball",
            "Sand volleyball",
            "Tennis courts",
            "Pickleball courts",
            "Disc golf (18 holes)",
            "Inclusive playground",
            "Picnic shelters (6, with ~10 tables and grill each)",
            "Historic barn (rental)",
            "Band pavilion/stage",
            "Paved walking/biking trail (0.8-mi loop + 1.1-mi finger trails)",
            "Rock Creek Trail trailhead",
            "Swimming pool",
            "Wading pool",
        ],
        "difficulty_raw": None,
        "accessibility_raw": "Inclusive playground with poured-rubber base; ADA-accessible areas",
        "urls_raw": ["https://www.tiffinohio.gov/departments/parks-rec/parks/hedges-boyer"],
        "identity_notes_raw": (
            "Tiffin's primary community park. Rock Creek Trail trailhead here — "
            "Rock Creek Trail staged as separate T6 Trail entity. "
            "Municipal Swimming Pool is associated facility. Baseline seed confirmed."
        ),
        "township_raw": None,
        "municipality_raw": None,
        "discovery_tier": 6,
        "seeded_from_baseline": True,
        "baseline_id": "Hedges-Boyer Park",
    },
    {
        "entity_type": "Site",
        "name_raw": "Schekelhoff Park",
        "counties_raw": ["Seneca"],
        "county_primary": "Seneca",
        "ownership_raw": TIFFIN_OWN,
        "governance_raw": TIFFIN_GOV,
        "partner_agencies_raw": "Tiffin-Seneca Public Library",
        "coordination_raw": "Tiffin Storybook Trail is a joint project with the Tiffin-Seneca Public Library.",
        "gps_lat_raw": None,
        "gps_lon_raw": None,
        "location_raw": "Tiffin, OH 44883 (Sandusky River, near Clinton Nature Preserve)",
        "acres_raw": "37",
        "description_raw": (
            "37-acre nature preserve along the Sandusky River. Features the Tiffin Storybook Trail "
            "(1/2 mile paved trail with 20 reading stations), benches along the trail, a small picnic shelter, "
            "and Eagle's Landing outlook deck. Connects via stone trail to Clinton Nature Preserve "
            "(SCPD-managed, additional 0.5 miles). Joint Tiffin Parks and Recreation / Tiffin-Seneca "
            "Public Library program."
        ),
        "features_raw": [
            "Paved trail (0.5 mi — Tiffin Storybook Trail)",
            "Eagle's Landing outlook deck",
            "Picnic shelter",
            "Benches",
            "Sandusky River access",
            "Connection to Clinton Nature Preserve (stone trail, SCPD-managed)",
        ],
        "difficulty_raw": None,
        "accessibility_raw": "Paved trail",
        "urls_raw": [
            "https://www.tiffinohio.gov/departments/parks-rec/parks/schekelhoff",
            "https://www.tiffinohio.gov/departments/parks-rec/facilities/storybook-trail",
            "https://www.tiffinohio.gov/departments/parks-rec/facilities/trails",
        ],
        "identity_notes_raw": (
            "Baseline seed 'Schekelhoff Nature Preserve' confirmed as Schekelhoff Park — "
            "city parks website uses 'Schekelhoff Park'; natural preserve character confirmed. "
            "Adjacent to SCPD Clinton Nature Preserve (T3 entity already staged). "
            "Storybook Trail is an internal program trail, not a separate entity."
        ),
        "township_raw": None,
        "municipality_raw": None,
        "discovery_tier": 6,
        "seeded_from_baseline": True,
        "baseline_id": "Schekelhoff Nature Preserve",
    },
    {
        "entity_type": "Site",
        "name_raw": "Highland Park",
        "counties_raw": ["Seneca"],
        "county_primary": "Seneca",
        "ownership_raw": TIFFIN_OWN,
        "governance_raw": TIFFIN_GOV,
        "partner_agencies_raw": None,
        "coordination_raw": None,
        "gps_lat_raw": None,
        "gps_lon_raw": None,
        "location_raw": "8th Avenue and N. Washington Street, Tiffin, OH 44883",
        "acres_raw": "18",
        "description_raw": (
            "18-acre park at the corner of 8th Avenue and N. Washington Street. "
            "Home to Bo Reid Baseball Field, the Tiffin Skate Park, and the Tiffin Bark Park."
        ),
        "features_raw": ["Baseball (Bo Reid Field)", "Skate park", "Dog park (Tiffin Bark Park)"],
        "difficulty_raw": None,
        "accessibility_raw": None,
        "urls_raw": ["https://www.tiffinohio.gov/departments/parks-rec/parks/highland"],
        "identity_notes_raw": None,
        "township_raw": None,
        "municipality_raw": None,
        "discovery_tier": 6,
        "seeded_from_baseline": False,
        "baseline_id": None,
    },
    {
        "entity_type": "Site",
        "name_raw": "Kernan Park",
        "counties_raw": ["Seneca"],
        "county_primary": "Seneca",
        "ownership_raw": TIFFIN_OWN,
        "governance_raw": TIFFIN_GOV,
        "partner_agencies_raw": None,
        "coordination_raw": None,
        "gps_lat_raw": None,
        "gps_lon_raw": None,
        "location_raw": "Ohio Avenue, Riverside Drive, and Industrial Avenue, Tiffin, OH 44883",
        "acres_raw": "14",
        "description_raw": (
            "14-acre park bounded by Ohio Avenue, Riverside Drive, and Industrial Avenue. "
            "Once home to an orphanage. Contains two youth softball fields and open grass area."
        ),
        "features_raw": ["Softball (2 youth fields)", "Open grass area"],
        "difficulty_raw": None,
        "accessibility_raw": None,
        "urls_raw": ["https://www.tiffinohio.gov/departments/parks-rec/parks/kernan"],
        "identity_notes_raw": None,
        "township_raw": None,
        "municipality_raw": None,
        "discovery_tier": 6,
        "seeded_from_baseline": False,
        "baseline_id": None,
    },
    {
        "entity_type": "Site",
        "name_raw": "Nature Trails Park",
        "counties_raw": ["Seneca"],
        "county_primary": "Seneca",
        "ownership_raw": TIFFIN_OWN,
        "governance_raw": TIFFIN_GOV,
        "partner_agencies_raw": None,
        "coordination_raw": None,
        "gps_lat_raw": None,
        "gps_lon_raw": None,
        "location_raw": "Off East Davis Street, Sandusky River, Tiffin, OH 44883",
        "acres_raw": "11",
        "description_raw": (
            "11-acre park located off East Davis Street on the banks of the Sandusky River. "
            "Updated in 2022. Features a paved walking path, playground, picnic shelter, and river access."
        ),
        "features_raw": ["Paved walking path", "Playground", "Picnic shelter", "Sandusky River access"],
        "difficulty_raw": None,
        "accessibility_raw": None,
        "urls_raw": ["https://www.tiffinohio.gov/departments/parks-rec/parks/nature-trails"],
        "identity_notes_raw": None,
        "township_raw": None,
        "municipality_raw": None,
        "discovery_tier": 6,
        "seeded_from_baseline": False,
        "baseline_id": None,
    },
    {
        "entity_type": "Site",
        "name_raw": "Oakley Park",
        "counties_raw": ["Seneca"],
        "county_primary": "Seneca",
        "ownership_raw": TIFFIN_OWN,
        "governance_raw": TIFFIN_GOV,
        "partner_agencies_raw": None,
        "coordination_raw": None,
        "gps_lat_raw": None,
        "gps_lon_raw": None,
        "location_raw": "Park Avenue, Grand Avenue, and Sixth Avenue, Tiffin, OH 44883",
        "acres_raw": "6",
        "description_raw": (
            "6-acre park bordered by Park Avenue, Grand Avenue, and Sixth Avenue. "
            "Features two picnic shelters, two baseball fields, basketball court, paved walking trail "
            "(0.7 mi lighted loop), and playground equipment (updated 2016)."
        ),
        "features_raw": [
            "Picnic shelters (2)",
            "Baseball (2 fields)",
            "Basketball",
            "Paved trail (0.7-mi lighted loop)",
            "Playground",
        ],
        "difficulty_raw": None,
        "accessibility_raw": "Lighted loop trail",
        "urls_raw": [
            "https://www.tiffinohio.gov/departments/parks-rec/parks/oakley",
            "https://www.tiffinohio.gov/departments/parks-rec/facilities/trails",
        ],
        "identity_notes_raw": None,
        "township_raw": None,
        "municipality_raw": None,
        "discovery_tier": 6,
        "seeded_from_baseline": False,
        "baseline_id": None,
    },
    {
        "entity_type": "Site",
        "name_raw": "Riverview Park",
        "counties_raw": ["Seneca"],
        "county_primary": "Seneca",
        "ownership_raw": TIFFIN_OWN,
        "governance_raw": TIFFIN_GOV,
        "partner_agencies_raw": None,
        "coordination_raw": None,
        "gps_lat_raw": None,
        "gps_lon_raw": None,
        "location_raw": "Longfellow Drive / Gary Lane / Gale Lane, south Tiffin, OH 44883",
        "acres_raw": "3.5",
        "description_raw": (
            "3.5-acre park on the south side of Tiffin, tucked behind houses on Longfellow Drive, "
            "Gary Lane, and Gale Lane, with entrances on each street. Renovated in 2019. "
            "Features a 0.25-mile paved trail, basketball court, playground, and small picnic shelter."
        ),
        "features_raw": ["Paved trail (0.25 mi)", "Basketball", "Playground", "Picnic shelter"],
        "difficulty_raw": None,
        "accessibility_raw": None,
        "urls_raw": ["https://www.tiffinohio.gov/departments/parks-rec/parks/riverview"],
        "identity_notes_raw": None,
        "township_raw": None,
        "municipality_raw": None,
        "discovery_tier": 6,
        "seeded_from_baseline": False,
        "baseline_id": None,
    },
    {
        "entity_type": "Site",
        "name_raw": "Louisa K. Fast Park",
        "counties_raw": ["Seneca"],
        "county_primary": "Seneca",
        "ownership_raw": TIFFIN_OWN,
        "governance_raw": TIFFIN_GOV,
        "partner_agencies_raw": None,
        "coordination_raw": None,
        "gps_lat_raw": None,
        "gps_lon_raw": None,
        "location_raw": "432 Jackson Street (Apple Street x Jackson Street), Tiffin, OH 44883",
        "acres_raw": "3.25",
        "description_raw": (
            "3.25-acre park at Apple Street and Jackson Street. Formerly named Apple-Jack Park (renamed "
            "2025 to honor Louisa K. Fast, women's suffrage pioneer and Tiffin civic leader, 1878-1979). "
            "Used as a Junior High School football field until 1972, then became city park. "
            "Features playground, ball field, picnic shelter, basketball court, and open grass area."
        ),
        "features_raw": ["Playground", "Ball field", "Picnic shelter", "Basketball", "Open grass area"],
        "difficulty_raw": None,
        "accessibility_raw": None,
        "urls_raw": ["https://www.tiffinohio.gov/departments/parks-rec/parks/louisa-k-fast"],
        "identity_notes_raw": (
            "Formerly Apple-Jack Park; renamed Louisa K. Fast Park by Tiffin City Council in 2025. "
            "Destination Seneca County still lists as Apple-Jack Park (432 Jackson St) — address confirmed. "
            "Staged under current legal name Louisa K. Fast Park."
        ),
        "township_raw": None,
        "municipality_raw": None,
        "discovery_tier": 6,
        "seeded_from_baseline": False,
        "baseline_id": None,
    },
    {
        "entity_type": "Site",
        "name_raw": "Josiah Hedges Park",
        "counties_raw": ["Seneca"],
        "county_primary": "Seneca",
        "ownership_raw": TIFFIN_OWN,
        "governance_raw": TIFFIN_GOV,
        "partner_agencies_raw": None,
        "coordination_raw": None,
        "gps_lat_raw": None,
        "gps_lon_raw": None,
        "location_raw": "Schonhardt Street and Park Place (behind Calvert High School), Tiffin, OH 44883",
        "acres_raw": "3",
        "description_raw": (
            "3-acre shaded park behind Calvert High School at Schonhardt Street and Park Place. "
            "Also known as 'Little Hedges'; named after Tiffin founder Josiah Hedges. "
            "Originally a cemetery until graves were moved to Greenlawn Cemetery in 1915. "
            "The Rock Creek Trail runs through the center of the park, linking it to Heidelberg University "
            "and Hedges-Boyer Park. Features playground (updated 2018) and small picnic shelter."
        ),
        "features_raw": ["Rock Creek Trail (passes through)", "Playground", "Picnic shelter"],
        "difficulty_raw": None,
        "accessibility_raw": None,
        "urls_raw": ["https://www.tiffinohio.gov/departments/parks-rec/parks/josiah-hedges"],
        "identity_notes_raw": (
            "Rock Creek Trail trailhead here (east end). "
            "Rock Creek Trail staged as separate T6 Trail entity."
        ),
        "township_raw": None,
        "municipality_raw": None,
        "discovery_tier": 6,
        "seeded_from_baseline": False,
        "baseline_id": None,
    },
    {
        "entity_type": "Site",
        "name_raw": "Tiffin East Park",
        "counties_raw": ["Seneca"],
        "county_primary": "Seneca",
        "ownership_raw": TIFFIN_OWN,
        "governance_raw": TIFFIN_GOV,
        "partner_agencies_raw": "U.S. Federal Government (original donor via Lands to Parks Program)",
        "coordination_raw": None,
        "gps_lat_raw": None,
        "gps_lon_raw": None,
        "location_raw": "State Route 101 (just east of city limits), Tiffin, OH 44883",
        "acres_raw": "2.3",
        "description_raw": (
            "2.3-acre open green space on State Route 101, just east of Tiffin city limits. "
            "Formerly used by the federal government for grain storage during WWII, later donated to "
            "the City of Tiffin through the Federal Lands to Parks Program. Formerly named Louisa K. Fast Park "
            "until that name was transferred to the Apple St/Jackson St park in 2025. "
            "Note: As of 2025, this park was being considered for auction by the Federal Government."
        ),
        "features_raw": ["Open green space"],
        "difficulty_raw": None,
        "accessibility_raw": None,
        "urls_raw": ["https://www.tiffinohio.gov/departments/parks-rec/parks/tiffin-east-park"],
        "identity_notes_raw": (
            "Federal Lands to Parks Program donation; currently city-owned. "
            "As of 2025, park was being considered for federal auction — future status uncertain. "
            "Staged as active city park per current website listing."
        ),
        "township_raw": None,
        "municipality_raw": None,
        "discovery_tier": 6,
        "seeded_from_baseline": False,
        "baseline_id": None,
    },
    {
        "entity_type": "Site",
        "name_raw": "Rotary Club of Tiffin Centennial Park",
        "counties_raw": ["Seneca"],
        "county_primary": "Seneca",
        "ownership_raw": TIFFIN_OWN,
        "governance_raw": TIFFIN_GOV,
        "partner_agencies_raw": None,
        "coordination_raw": None,
        "gps_lat_raw": None,
        "gps_lon_raw": None,
        "location_raw": "Frost Parkway (between river wall of Sandusky River and Frost Parkway), Tiffin, OH 44883",
        "acres_raw": "1.2",
        "description_raw": (
            "1.2-acre park between the Sandusky River wall and Frost Parkway. "
            "Contains brick-paved trails, a gazebo, and landscaping. "
            "Offers views of the Sandusky River and downtown Tiffin. "
            "Home to Ohio Historical Marker for Camp Ball. "
            "Features Christmas light display along Frost Parkway during holiday season."
        ),
        "features_raw": ["Brick-paved trails", "Gazebo", "Sandusky River views", "Ohio Historical Marker (Camp Ball)"],
        "difficulty_raw": None,
        "accessibility_raw": None,
        "urls_raw": ["https://www.tiffinohio.gov/departments/parks-rec/parks/rotary-club"],
        "identity_notes_raw": None,
        "township_raw": None,
        "municipality_raw": None,
        "discovery_tier": 6,
        "seeded_from_baseline": False,
        "baseline_id": None,
    },
    {
        "entity_type": "Site",
        "name_raw": "Stalter Park",
        "counties_raw": ["Seneca"],
        "county_primary": "Seneca",
        "ownership_raw": TIFFIN_OWN,
        "governance_raw": TIFFIN_GOV,
        "partner_agencies_raw": None,
        "coordination_raw": None,
        "gps_lat_raw": None,
        "gps_lon_raw": None,
        "location_raw": "Ohio Avenue and Clinton Avenue, Tiffin, OH 44883",
        "acres_raw": "1",
        "description_raw": (
            "Triangular 1-acre park at Ohio Avenue and Clinton Avenue, acquired in 1905 from former "
            "city councilman David Stalter. Contains open grass area with picnic table and Ohio Historical "
            "Marker for Camp Noble."
        ),
        "features_raw": ["Picnic table", "Ohio Historical Marker (Camp Noble)", "Open grass area"],
        "difficulty_raw": None,
        "accessibility_raw": None,
        "urls_raw": ["https://www.tiffinohio.gov/departments/parks-rec/parks/stalter"],
        "identity_notes_raw": None,
        "township_raw": None,
        "municipality_raw": None,
        "discovery_tier": 6,
        "seeded_from_baseline": False,
        "baseline_id": None,
    },
    {
        "entity_type": "Site",
        "name_raw": "Beechwood Park",
        "counties_raw": ["Seneca"],
        "county_primary": "Seneca",
        "ownership_raw": TIFFIN_OWN,
        "governance_raw": TIFFIN_GOV,
        "partner_agencies_raw": None,
        "coordination_raw": None,
        "gps_lat_raw": None,
        "gps_lon_raw": None,
        "location_raw": "22 Beechwood Drive (Ashwood Drive x Beechwood Drive), Tiffin, OH 44883",
        "acres_raw": "1",
        "description_raw": "1-acre neighborhood park at Ashwood Drive and Beechwood Drive. Features playground, picnic shelter, and basketball court.",
        "features_raw": ["Playground", "Picnic shelter", "Basketball"],
        "difficulty_raw": None,
        "accessibility_raw": None,
        "urls_raw": ["https://www.tiffinohio.gov/departments/parks-rec/parks/beechwood"],
        "identity_notes_raw": None,
        "township_raw": None,
        "municipality_raw": None,
        "discovery_tier": 6,
        "seeded_from_baseline": False,
        "baseline_id": None,
    },
    {
        "entity_type": "Site",
        "name_raw": "Junior Home Park",
        "counties_raw": ["Seneca"],
        "county_primary": "Seneca",
        "ownership_raw": TIFFIN_OWN,
        "governance_raw": TIFFIN_GOV,
        "partner_agencies_raw": None,
        "coordination_raw": None,
        "gps_lat_raw": None,
        "gps_lon_raw": None,
        "location_raw": "Sandusky River, north side of Tiffin, OH 44883",
        "acres_raw": None,
        "description_raw": (
            "Park along the Sandusky River on the north side of Tiffin. South portion dedicated as memorial "
            "to children from the Tiffin National Orphans Home, Jr. OUAM. Features shade, two picnic shelters, "
            "and Sandusky River access for fishing and kayaking."
        ),
        "features_raw": ["Picnic shelters (2)", "Sandusky River access", "Fishing access", "Kayaking access"],
        "difficulty_raw": None,
        "accessibility_raw": None,
        "urls_raw": ["https://www.tiffinohio.gov/departments/parks-rec/parks/junior-home"],
        "identity_notes_raw": "Acreage not provided on city website.",
        "township_raw": None,
        "municipality_raw": None,
        "discovery_tier": 6,
        "seeded_from_baseline": False,
        "baseline_id": None,
    },
    {
        "entity_type": "Site",
        "name_raw": "Lions Club Park",
        "counties_raw": ["Seneca"],
        "county_primary": "Seneca",
        "ownership_raw": TIFFIN_OWN,
        "governance_raw": TIFFIN_GOV,
        "partner_agencies_raw": None,
        "coordination_raw": None,
        "gps_lat_raw": None,
        "gps_lon_raw": None,
        "location_raw": "Adjacent to City of Tiffin Annex building, downtown Tiffin, OH 44883",
        "acres_raw": "0.03",
        "description_raw": "0.03-acre miniature park adjacent to the City Annex building in downtown Tiffin. Features shade trees, landscaping, and a picnic table.",
        "features_raw": ["Shade trees", "Picnic table", "Landscaping"],
        "difficulty_raw": None,
        "accessibility_raw": None,
        "urls_raw": ["https://www.tiffinohio.gov/departments/parks-rec/parks/lions-club"],
        "identity_notes_raw": None,
        "township_raw": None,
        "municipality_raw": None,
        "discovery_tier": 6,
        "seeded_from_baseline": False,
        "baseline_id": None,
    },
    {
        "entity_type": "Site",
        "name_raw": "Clouse-Kirian Leadership Park",
        "counties_raw": ["Seneca"],
        "county_primary": "Seneca",
        "ownership_raw": TIFFIN_OWN,
        "governance_raw": TIFFIN_GOV,
        "partner_agencies_raw": "Leadership Seneca County (Class of 2014, gazebo donor); Clouse Construction (land donor)",
        "coordination_raw": None,
        "gps_lat_raw": None,
        "gps_lon_raw": None,
        "location_raw": "22 S. Washington Street (S. Washington x S. Monroe), downtown Tiffin, OH 44883",
        "acres_raw": "0.1",
        "description_raw": (
            "0.1-acre park in downtown Tiffin at S. Washington and S. Monroe, overlooking the Sandusky River. "
            "Features a gazebo and brick patio donated by Leadership Seneca County Class of 2014. "
            "Land donated by Lynn and Lenny Clouse (Clouse Construction). Dedicated in memory of Jerry Kirian. "
            "Home to Ohio Historical Marker for the Founding of Tiffin."
        ),
        "features_raw": ["Gazebo", "Brick patio", "Sandusky River overlook", "Ohio Historical Marker (Founding of Tiffin)"],
        "difficulty_raw": None,
        "accessibility_raw": None,
        "urls_raw": ["https://www.tiffinohio.gov/departments/parks-rec/parks/clouse-kirian"],
        "identity_notes_raw": None,
        "township_raw": None,
        "municipality_raw": None,
        "discovery_tier": 6,
        "seeded_from_baseline": False,
        "baseline_id": None,
    },
    {
        "entity_type": "Site",
        "name_raw": "East Green",
        "counties_raw": ["Seneca"],
        "county_primary": "Seneca",
        "ownership_raw": TIFFIN_OWN,
        "governance_raw": TIFFIN_GOV,
        "partner_agencies_raw": None,
        "coordination_raw": None,
        "gps_lat_raw": None,
        "gps_lon_raw": None,
        "location_raw": "Downtown Tiffin, OH 44883",
        "acres_raw": None,
        "description_raw": (
            "Tiffin's newest downtown park, divided into two connected areas: "
            "(1) The National Corner — splash pad, restroom facility, landscaping, and trickling waterfall; "
            "(2) Frost-Kalnow Amphitheater — outdoor performance venue for concerts and events. "
            "Home of the East Green Concert Series."
        ),
        "features_raw": ["Splash pad", "Restrooms", "Amphitheater (Frost-Kalnow)", "Waterfall feature", "Landscaping"],
        "difficulty_raw": None,
        "accessibility_raw": None,
        "urls_raw": ["https://www.tiffinohio.gov/departments/parks-rec/facilities/east-green"],
        "identity_notes_raw": (
            "Listed under Tiffin Parks Facilities page (not the main Parks index); "
            "all evidence confirms this is a city-owned public park. "
            "Not included in the 16-park index page — explains the website's claim of '18 parks' "
            "vs 16 listed (East Green + possibly 1 other = 18)."
        ),
        "township_raw": None,
        "municipality_raw": None,
        "discovery_tier": 6,
        "seeded_from_baseline": False,
        "baseline_id": None,
    },
]

# ============================================================
# TIFFIN TRAIL: Rock Creek Trail
# ============================================================

rock_creek_trail = {
    "entity_type": "Trail",
    "name_raw": "Rock Creek Trail",
    "counties_raw": ["Seneca"],
    "county_primary": "Seneca",
    "ownership_raw": TIFFIN_OWN,
    "governance_raw": TIFFIN_GOV,
    "partner_agencies_raw": "Heidelberg University (trail passes through campus)",
    "coordination_raw": "Trail passes through Heidelberg University campus — possible access agreement.",
    "gps_lat_raw": None,
    "gps_lon_raw": None,
    "location_raw": "Hedges-Boyer Park to Josiah Hedges Park via Heidelberg University, Tiffin, OH 44883",
    "acres_raw": None,
    "description_raw": (
        "2-mile paved trail connecting Hedges-Boyer Park (trailhead) and Josiah Hedges Park (east trailhead), "
        "winding through the Heidelberg University campus along Rock Creek. "
        "Suitable for walking, running, and biking."
    ),
    "features_raw": None,
    "difficulty_raw": None,
    "accessibility_raw": "Paved surface",
    "urls_raw": ["https://www.tiffinohio.gov/departments/parks-rec/facilities/trails"],
    "identity_notes_raw": (
        "Named trail confirmed by Tiffin Parks Recreational Trails page. "
        "2 trailheads: Hedges-Boyer Park (west end) and Josiah Hedges Park (east end). "
        "Both trailhead APs to be staged during Access Point pass."
    ),
    "township_raw": None,
    "municipality_raw": None,
    "discovery_tier": 6,
    "seeded_from_baseline": False,
    "baseline_id": None,
}

# ============================================================
# FOSTORIA SITES (Seneca County only)
# ============================================================

fostoria_sites = [
    {
        "entity_type": "Site",
        "name_raw": "Foundation Park",
        "counties_raw": ["Seneca"],
        "county_primary": "Seneca",
        "ownership_raw": FOSTORIA_OWN,
        "governance_raw": FOSTORIA_GOV,
        "partner_agencies_raw": None,
        "coordination_raw": None,
        "gps_lat_raw": None,
        "gps_lon_raw": None,
        "location_raw": "1225 S. Union Street and Woodland Avenue, Fostoria, OH 44830 (Seneca County)",
        "acres_raw": "50",
        "description_raw": (
            "Formerly known as Meadowlark Park. 50-acre park in Seneca County portion of Fostoria. "
            "Features 13 baseball and softball fields, a tennis court, playground, dog park, "
            "shelter house, concession stand, and free brush drop-off/mulch center for Fostoria residents."
        ),
        "features_raw": [
            "Baseball/Softball (13 fields)",
            "Tennis",
            "Playground",
            "Dog park",
            "Shelter house",
            "Concession stand",
            "Brush drop-off/mulch center",
        ],
        "difficulty_raw": None,
        "accessibility_raw": None,
        "urls_raw": ["https://www.fostoriaohio.gov/parks-and-rec"],
        "identity_notes_raw": "Seneca County per Fostoria Parks page (explicitly labeled). Formerly Meadowlark Park.",
        "township_raw": None,
        "municipality_raw": None,
        "discovery_tier": 6,
        "seeded_from_baseline": False,
        "baseline_id": None,
    },
    {
        "entity_type": "Site",
        "name_raw": "Iron Triangle Rail Park",
        "counties_raw": ["Seneca"],
        "county_primary": "Seneca",
        "ownership_raw": FOSTORIA_OWN,
        "governance_raw": FOSTORIA_GOV,
        "partner_agencies_raw": None,
        "coordination_raw": None,
        "gps_lat_raw": None,
        "gps_lon_raw": None,
        "location_raw": "499 S. Poplar Street (Columbus Avenue and Poplar Street), Fostoria, OH 44830 (Seneca County)",
        "acres_raw": "5",
        "description_raw": (
            "5-acre rail-watching park at the famous 'Iron Triangle' railroad intersection in Fostoria, "
            "one of the busiest railroad junctions in the United States. Features a covered viewing pavilion "
            "with seating, lighting, Wi-Fi capability, heated restrooms, perimeter fencing, and parking "
            "for 32 cars and 5 buses/RVs. More than 10 years in planning before groundbreaking."
        ),
        "features_raw": [
            "Covered viewing pavilion",
            "Seating",
            "Lighting",
            "Wi-Fi",
            "Heated restrooms",
            "Parking (32 cars, 5 buses/RVs)",
            "Perimeter fencing",
        ],
        "difficulty_raw": None,
        "accessibility_raw": "Paved, covered pavilion",
        "urls_raw": [
            "https://www.fostoriaohio.gov/parks-and-rec",
            "https://www.destinationsenecacounty.org/place/fostoria-iron-triangle-rail-park/",
        ],
        "identity_notes_raw": (
            "Seneca County per Destination Seneca County listing and address verification. "
            "A unique railroad-watching park — the Iron Triangle is one of the busiest rail junctions in the US."
        ),
        "township_raw": None,
        "municipality_raw": None,
        "discovery_tier": 6,
        "seeded_from_baseline": True,
        "baseline_id": "Iron Triangle Rail Park",
    },
    {
        "entity_type": "Site",
        "name_raw": "Jackson Park",
        "counties_raw": ["Seneca"],
        "county_primary": "Seneca",
        "ownership_raw": FOSTORIA_OWN,
        "governance_raw": FOSTORIA_GOV,
        "partner_agencies_raw": None,
        "coordination_raw": None,
        "gps_lat_raw": None,
        "gps_lon_raw": None,
        "location_raw": "Jackson Street west of Buckley Street, Fostoria, OH 44830 (Seneca County)",
        "acres_raw": "8",
        "description_raw": "8-acre park in Seneca County portion of Fostoria. Features playground, shelter house, and picnic tables.",
        "features_raw": ["Playground", "Shelter house", "Picnic tables"],
        "difficulty_raw": None,
        "accessibility_raw": None,
        "urls_raw": ["https://www.fostoriaohio.gov/parks-and-rec"],
        "identity_notes_raw": "Seneca County per Fostoria Parks page (explicitly labeled).",
        "township_raw": None,
        "municipality_raw": None,
        "discovery_tier": 6,
        "seeded_from_baseline": False,
        "baseline_id": None,
    },
    {
        "entity_type": "Site",
        "name_raw": "Harmon Park",
        "counties_raw": ["Seneca"],
        "county_primary": "Seneca",
        "ownership_raw": FOSTORIA_OWN,
        "governance_raw": FOSTORIA_GOV,
        "partner_agencies_raw": None,
        "coordination_raw": None,
        "gps_lat_raw": None,
        "gps_lon_raw": None,
        "location_raw": "Wood Street and Fourth Street, Fostoria, OH 44830 (Seneca County)",
        "acres_raw": "0.5",
        "description_raw": "0.5-acre park at the corner of Wood and Fourth Streets in the Seneca County portion of Fostoria. Features playground equipment.",
        "features_raw": ["Playground"],
        "difficulty_raw": None,
        "accessibility_raw": None,
        "urls_raw": ["https://www.fostoriaohio.gov/parks-and-rec"],
        "identity_notes_raw": "Seneca County per Fostoria Parks page (explicitly labeled).",
        "township_raw": None,
        "municipality_raw": None,
        "discovery_tier": 6,
        "seeded_from_baseline": False,
        "baseline_id": None,
    },
    {
        "entity_type": "Site",
        "name_raw": "Buckley Street Courts",
        "counties_raw": ["Seneca"],
        "county_primary": "Seneca",
        "ownership_raw": FOSTORIA_OWN,
        "governance_raw": FOSTORIA_GOV,
        "partner_agencies_raw": None,
        "coordination_raw": None,
        "gps_lat_raw": None,
        "gps_lon_raw": None,
        "location_raw": "Buckley Street at Eastern Avenue, Fostoria, OH 44830 (Seneca County)",
        "acres_raw": None,
        "description_raw": "Outdoor sports court facility in the Seneca County portion of Fostoria, featuring 3 recently resurfaced tennis courts and 1 basketball court.",
        "features_raw": ["Tennis (3 courts, recently resurfaced)", "Basketball"],
        "difficulty_raw": None,
        "accessibility_raw": None,
        "urls_raw": ["https://www.fostoriaohio.gov/parks-and-rec"],
        "identity_notes_raw": "Seneca County per Fostoria Parks page (explicitly labeled). Acreage not provided.",
        "township_raw": None,
        "municipality_raw": None,
        "discovery_tier": 6,
        "seeded_from_baseline": False,
        "baseline_id": None,
    },
    {
        "entity_type": "Site",
        "name_raw": "Veterans Memorial Reservoir",
        "counties_raw": ["Seneca"],
        "county_primary": "Seneca",
        "ownership_raw": FOSTORIA_OWN,
        "governance_raw": FOSTORIA_GOV,
        "partner_agencies_raw": None,
        "coordination_raw": None,
        "gps_lat_raw": None,
        "gps_lon_raw": None,
        "location_raw": "State Route 12, north of Lake LeComte (Reservoir 5), Seneca County, OH (nearest: Fostoria, OH 44830). Boat ramp off Washington Township Road 218.",
        "acres_raw": "300",
        "description_raw": (
            "Fostoria City Reservoir #6 (Veterans Memorial Reservoir) — 180 water acres, 300 land acres. "
            "Named to honor all veterans. Features a 2.3-mile stone walking trail surrounded by woods "
            "and farmland, fishing, ice fishing, boating, and waterfowl hunting. "
            "Boat ramp located on the northern edge off Washington Township Road 218."
        ),
        "features_raw": [
            "Stone walking trail (2.3 mi)",
            "Fishing",
            "Ice fishing",
            "Boating",
            "Waterfowl hunting",
            "Boat ramp",
        ],
        "difficulty_raw": None,
        "accessibility_raw": None,
        "urls_raw": [
            "https://www.destinationsenecacounty.org/place/fostoria-reservoirs/",
            "https://mapcarta.com/W238991445",
        ],
        "identity_notes_raw": (
            "Confirmed Seneca County per mapcarta.com ('Seneca, Ohio'). "
            "Reservoirs 1-5 (Lake Daughtery, Mottram, Lamberjack, Mosier, LeComte) are Hancock County — "
            "not staged for Seneca County T6. "
            "All 6 reservoirs city-owned by City of Fostoria. "
            "Valid Ohio fishing license required. Washington Township, Seneca County."
        ),
        "township_raw": None,
        "municipality_raw": None,
        "discovery_tier": 6,
        "seeded_from_baseline": False,
        "baseline_id": None,
    },
]

# ============================================================
# OTHER MUNICIPAL SITES
# ============================================================

other_municipal_sites = [
    # ATTICA
    {
        "entity_type": "Site",
        "name_raw": "Myers Park",
        "counties_raw": ["Seneca"],
        "county_primary": "Seneca",
        "ownership_raw": "Village of Attica",
        "governance_raw": "Village of Attica Parks and Recreation",
        "partner_agencies_raw": None,
        "coordination_raw": None,
        "gps_lat_raw": None,
        "gps_lon_raw": None,
        "location_raw": "14999 E. County Road 56, Attica, OH 44807",
        "acres_raw": None,
        "description_raw": "Village of Attica community park with pavilion available for rental. Only park listed on Village of Attica Parks and Recreation website.",
        "features_raw": ["Pavilion (rental available)", "Playground (likely)"],
        "difficulty_raw": None,
        "accessibility_raw": None,
        "urls_raw": ["http://www.atticaohio.us/parks-and-recreation"],
        "identity_notes_raw": "Only park on Village of Attica website. Acreage not provided.",
        "township_raw": None,
        "municipality_raw": None,
        "discovery_tier": 6,
        "seeded_from_baseline": False,
        "baseline_id": None,
    },
    # BLOOMVILLE
    {
        "entity_type": "Site",
        "name_raw": "Beeghly Park",
        "counties_raw": ["Seneca"],
        "county_primary": "Seneca",
        "ownership_raw": "Village of Bloomville",
        "governance_raw": "Village of Bloomville",
        "partner_agencies_raw": "Bloomville Lions Club (park development)",
        "coordination_raw": None,
        "gps_lat_raw": None,
        "gps_lon_raw": None,
        "location_raw": "Bloomville, OH 44818",
        "acres_raw": None,
        "description_raw": (
            "Village of Bloomville community park developed largely through the efforts of the "
            "Bloomville Lions Club. Has hosted a petting zoo, horseshoe tournaments, and baseball games."
        ),
        "features_raw": ["Baseball", "Horseshoe (historical)", "Open area"],
        "difficulty_raw": None,
        "accessibility_raw": None,
        "urls_raw": ["https://www.destinationsenecacounty.org/place-category/things-to-do/outdoors-recreation/"],
        "identity_notes_raw": (
            "Village of Bloomville website (citydirectory.us) confirms village provides parks. "
            "Park name confirmed from Destination Seneca County and Tiffin-Seneca Public Library blog. "
            "No street address found from authoritative source — GPS acquisition required."
        ),
        "township_raw": None,
        "municipality_raw": None,
        "discovery_tier": 6,
        "seeded_from_baseline": False,
        "baseline_id": None,
    },
    # NEW RIEGEL
    {
        "entity_type": "Site",
        "name_raw": "New Riegel Park",
        "counties_raw": ["Seneca"],
        "county_primary": "Seneca",
        "ownership_raw": "Village of New Riegel",
        "governance_raw": "Village of New Riegel",
        "partner_agencies_raw": None,
        "coordination_raw": None,
        "gps_lat_raw": None,
        "gps_lon_raw": None,
        "location_raw": "13 Near West Street, New Riegel, OH 44853",
        "acres_raw": None,
        "description_raw": (
            "New Riegel community park. Features three ball fields, a shelter, basketball courts, "
            "and playground equipment. Evening gathering spot for local sports enthusiasts and families."
        ),
        "features_raw": ["Baseball/Softball (3 ball fields)", "Basketball", "Playground", "Shelter"],
        "difficulty_raw": None,
        "accessibility_raw": None,
        "urls_raw": ["https://www.destinationsenecacounty.org/place/new-riegel-park/"],
        "identity_notes_raw": "Address from Destination Seneca County. Governance assumed Village of New Riegel — no official village website found to confirm.",
        "township_raw": None,
        "municipality_raw": None,
        "discovery_tier": 6,
        "seeded_from_baseline": False,
        "baseline_id": None,
    },
]

# ============================================================
# TIER 6 NULL BLOCKS
# ============================================================

t6_nulls = [
    {
        "tier": 6,
        "governance_level": "Tiffin — City cemetery (municipal)",
        "entity_type": "All",
        "result": "null",
        "sources_checked": [
            "https://www.greenlawncemeterytiffin.org/",
            "Web search: 'Tiffin Ohio municipal cemetery city-owned'",
        ],
        "reasoning": (
            "No city-owned cemetery in Tiffin. Greenlawn Cemetery (895 E County Rd 36, Tiffin) is a "
            "501(c)(13) non-profit association — NOT city-owned. St. Joseph's Catholic Cemetery is church-owned. "
            "Confirmed null for T6 Tiffin municipal cemetery. Greenlawn = T8 candidate (private cemetery nonprofit)."
        ),
    },
    {
        "tier": 6,
        "governance_level": "Tiffin — Golf courses (municipal)",
        "entity_type": "All",
        "result": "null (T8 candidates)",
        "sources_checked": [
            "https://clintonheightsgolf.com/",
            "https://www.ohiogolf.com/golfcourses/seneca-hills-golf-course",
        ],
        "reasoning": (
            "Two golf courses near Tiffin: Clinton Heights Golf Course (2760 E Township Rd 122) and "
            "Seneca Hills Golf Course — both privately owned. Neither is city-owned. "
            "Confirmed null for T6. Both are T8 (Private) candidates."
        ),
    },
    {
        "tier": 6,
        "governance_level": "Fostoria — Hancock/Wood County parks (excluded from Seneca T6)",
        "entity_type": "All",
        "result": "null (county exclusion)",
        "sources_checked": [
            "https://www.fostoriaohio.gov/parks-and-rec",
        ],
        "reasoning": (
            "Fostoria straddles Seneca, Hancock, and Wood counties. The following Fostoria parks are "
            "NOT in Seneca County and are excluded from Seneca T6: "
            "City Park (Hancock), Gray Park (Hancock), Portage Park (Wood). "
            "Also Reservoirs 1-5 (Lake Daughtery, Mottram, Lamberjack, Mosier, LeComte) = Hancock County. "
            "Only Seneca County parks staged: Foundation Park, Iron Triangle Rail Park, Jackson Park, "
            "Harmon Park, Buckley Street Courts, Veterans Memorial Reservoir."
        ),
    },
    {
        "tier": 6,
        "governance_level": "Fostoria — Cemetery and golf courses (municipal)",
        "entity_type": "All",
        "result": "null (T8 candidates)",
        "sources_checked": [
            "Web search: 'Fostoria Ohio city-owned municipal cemetery golf course'",
        ],
        "reasoning": (
            "No city-owned cemetery found in Fostoria. Golf courses: Fostoria Country Club (private, est. 1916), "
            "Loudon Meadows Golf Club (public but privately-owned by Andy and Renae Clouse). "
            "Both golf courses are T8 (Private) candidates. Confirmed null for T6."
        ),
    },
    {
        "tier": 6,
        "governance_level": "Bellevue — Village/City parks (municipal)",
        "entity_type": "All",
        "result": "null — all parks already KNOWN_MC in DB",
        "sources_checked": [
            "https://www.bellevueohio.gov/departments/parks_recreation/parks_facilities/parks/index.php",
            "DB query: SELECT site_id, name FROM sites WHERE site_id BETWEEN 'OH-SAN-S-072' AND 'OH-SAN-S-078'",
        ],
        "reasoning": (
            "Bellevue Ohio Parks page lists 7 parks: Magdalyn Aigler Recreation Complex, Amsden Park, "
            "Buckingham Park, Ellis Park, Kern Street Park, Ridge Park, Robert Peters Athletic Field. "
            "DB query confirms OH-SAN-S-072 through OH-SAN-S-078 are exactly these 7 parks "
            "(Erie;Huron;Sandusky;Seneca counties). "
            "All Bellevue parks already in DB as KNOWN_MC. No new T6 entities."
        ),
    },
    {
        "tier": 6,
        "governance_level": "Bettsville — Village parks (municipal)",
        "entity_type": "All",
        "result": "null (deferred — H.P. Eells Park handled at T3)",
        "sources_checked": [
            "https://villageofbettsville.com/departments/park/",
        ],
        "reasoning": (
            "H.P. Eells Park (7461 N. TR. 70, Bettsville area) was staged at T3 as a Park/Recreation District "
            "entity (Bettsville Recreation Board — governance uncertain, possibly dissolved ~2009). "
            "If Bettsville Recreation Board is confirmed dissolved, H.P. Eells Park re-tiers to T6 "
            "(Village of Bettsville). This re-tiering requires human verification — flagged in Open Questions."
        ),
    },
    {
        "tier": 6,
        "governance_level": "Green Springs — Village parks (municipal)",
        "entity_type": "All",
        "result": "null",
        "sources_checked": [
            "https://www.gsohio.org/departments/parks-rentals (404 Not Found)",
            "https://www.yelp.com/biz/whirlpool-park-green-springs (CLOSED Dec 2025)",
            "https://www.lake-link.com/ohio-lakes/sandusky/beaver-creek-reservoir/23476/",
            "Web search: 'Green Springs Ohio village park playground municipal'",
        ],
        "reasoning": (
            "Village of Green Springs parks page returned 404. "
            "Whirlpool Park (2220 E County Rd 181, Green Springs) confirmed CLOSED as of December 2025 (Yelp). "
            "Beaver Creek Reservoir (7478 TR 0196, Green Springs 44836) is in Sandusky County and owned by "
            "City of Clyde (per lake-link.com: 'sandusky county' URL and Ohio EPA public water supply records). "
            "No active village-owned parks confirmed in Seneca County portion of Green Springs. "
            "KNOWN_MC entity OH-SAN-S-110 (Green Springs Cemetery) already in DB — cemetery only, not a park. "
            "Confirmed null for T6 Green Springs municipal parks."
        ),
    },
    {
        "tier": 6,
        "governance_level": "Republic — Village parks (municipal)",
        "entity_type": "All",
        "result": "null",
        "sources_checked": [
            "Web search: 'Republic Ohio village park recreation Village of Republic'",
        ],
        "reasoning": (
            "No village-owned parks found in Republic, Ohio. "
            "Clinton Lake Camping (near Republic) is a private campground. "
            "Bowen Nature Preserve (SCPD, 11891 E. Co. Rd. 24) is near Republic but is T3 (SCPD), "
            "already staged. Confirmed null for T6 Republic municipal parks."
        ),
    },
    {
        "tier": 6,
        "governance_level": "Attica Upground Reservoir — public access status",
        "entity_type": "Site",
        "result": "null (deferred — public recreation access unconfirmed)",
        "sources_checked": [
            "Ohio EPA Attica Regionalization review PDF",
            "https://ohio.hometownlocator.com/maps/feature-map,ftc,2,fid,1079004,n,attica%20upground%20reservoir.cfm",
            "https://www.fishingworks.com/ohio/seneca-oh/lake/attica-upground-reservoir/",
        ],
        "reasoning": (
            "Attica Upground Reservoir is a Village of Attica water supply reservoir (confirmed per "
            "Ohio EPA Attica Regionalization review). Fishing access mentioned on fishing sites but "
            "no walking trail or formal public recreation access confirmed. "
            "No Destination Seneca County listing or SCPD affiliation found. "
            "Staged as null pending confirmation of formal public recreation access. "
            "If confirmed public walking/recreation access: stage as T6 (Village of Attica) Site."
        ),
    },
    {
        "tier": 6,
        "governance_level": "Tiffin — 18th park (unidentified)",
        "entity_type": "Site",
        "result": "null (unresolvable count discrepancy)",
        "sources_checked": [
            "https://www.tiffinohio.gov/departments/parks-rec/parks (16 parks listed)",
            "https://www.tiffinohio.gov/departments/parks-rec/facilities/east-green",
        ],
        "reasoning": (
            "Tiffin Parks intro text claims '18 parks'; the Parks index shows 16 named parks. "
            "East Green (under Facilities) accounts for a 17th park. "
            "One additional park remains unaccounted for. The website count may be outdated, "
            "or one park has no dedicated web page. "
            "All 17 identified parks staged. The count discrepancy is noted but unresolvable from "
            "available web sources. Confirmed no additional parks found from any source."
        ),
    },
]

# Append all records
for site in tiffin_sites:
    data["records"].append(site)

data["records"].append(rock_creek_trail)

for site in fostoria_sites:
    data["records"].append(site)

for site in other_municipal_sites:
    data["records"].append(site)

for null in t6_nulls:
    data["tier_nulls"].append(null)

data["current_tier"] = 7

f.write_text(yaml.dump(data, allow_unicode=True, sort_keys=False), encoding="utf-8")

t6_count = len(tiffin_sites) + 1 + len(fostoria_sites) + len(other_municipal_sites)
print(f"Staged {t6_count} T6 entities: {len(tiffin_sites)} Tiffin sites + 1 Rock Creek Trail + {len(fostoria_sites)} Fostoria sites + {len(other_municipal_sites)} other municipal sites")
print(f"Added {len(t6_nulls)} T6 null blocks.")
print(f"Total records: {len(data['records'])}, Total tier_nulls: {len(data['tier_nulls'])}, current_tier: {data['current_tier']}")
