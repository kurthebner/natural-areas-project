import yaml, pathlib

f = pathlib.Path(r"D:\users\user1\Documents\CP Projects\Natural Areas Project v5\County_Spreadsheets\Seneca\seneca_ohio_raw_discovery.yaml")
data = yaml.safe_load(f.read_text(encoding="utf-8"))
data.setdefault("records", [])
data.setdefault("tier_nulls", [])

# =====================================================================
# TIER 5 — TOWNSHIP SITES
# =====================================================================

# --- HOPEWELL TOWNSHIP: Meadowbrook Park ---
meadowbrook = {
    "entity_type": "Site",
    "name_raw": "Meadowbrook Park",
    "counties_raw": ["Seneca"],
    "county_primary": "Seneca",
    "ownership_raw": "Hopewell Township",
    "governance_raw": "Hopewell Township Board of Trustees",
    "partner_agencies_raw": None,
    "coordination_raw": None,
    "gps_lat_raw": None,
    "gps_lon_raw": None,
    "location_raw": "5430 W. Tiffin St., Bascom, OH 44809 (PO Box 309)",
    "acres_raw": 160,
    "description_raw": (
        "130+ acre family recreation park owned and operated by Hopewell Township since 1976. "
        "Originated in the late 1890s as part of the Tiffin, Fostoria, and Eastern Railway interurban. "
        "Encompasses approximately 160 acres along Wolf Creek in Bascom with mature deciduous trees "
        "(oak, elm, beech, walnut, poplar, maple, hickory, ash) reflected in the names of 8+ picnic shelters. "
        "The 7,000 sq. ft. Redwood Ballroom (1934) seats 266-470 people. Financially self-sustaining "
        "through campground revenue; over $300,000 in grants secured since township acquisition. "
        "Summer program Camp Lakewood and multiple annual community events."
    ),
    "features_raw": [
        "Campground (214 sites; 168 seasonal)",
        "Swimming pool",
        "Picnic shelters (8+: Oak, Elm, Beech, Walnut, Poplar, Maple, Hickory, Ash, Evergreen)",
        "Playground",
        "Foot trails",
        "Disc golf (18-hole)",
        "Baseball diamond",
        "Tennis court",
        "Basketball court",
        "Sand volleyball",
        "Bocce ball",
        "Gaga ball",
        "Horseshoe pits",
        "Checkers/chess (giant)",
        "Shuffleboard",
        "Roller hockey court",
        "Ballroom/event venue",
        "Restrooms",
        "Concession stand (seasonal)",
        "Fishing pier (handicap-accessible)",
    ],
    "difficulty_raw": None,
    "accessibility_raw": "Handicap-accessible fishing pier noted.",
    "urls_raw": [
        "https://mbpark.org/brief-overview/",
        "https://mbpark.org/park-history/",
        "https://hopewell-township.com/",
        "https://www.hmdb.org/m.asp?m=227943",
    ],
    "identity_notes_raw": (
        "Confirmed township-owned since 1976 per park history. Originally an interurban railway resort "
        "(Camp Sandusky era → Garfield Haugh era → Hopewell Township). "
        "Address: Bascom, OH (Seneca County confirmed — hopewell-township.com lists township office at "
        "5281 W TR 112, Tiffin, OH 44883; park address at Bascom). "
        "Acreage discrepancy: park website says '130 acres' on overview page; history page says '160 acres along Wolf Creek.' "
        "Staged as 160 ac from history page. GPS acquisition required."
    ),
    "township_raw": None,
    "municipality_raw": None,
    "discovery_tier": 5,
    "seeded_from_baseline": False,
    "baseline_id": None,
}

# --- JACKSON TOWNSHIP: Zion Cemetery ---
zion_cem = {
    "entity_type": "Site",
    "name_raw": "Zion Cemetery",
    "counties_raw": ["Seneca"],
    "county_primary": "Seneca",
    "ownership_raw": "Jackson Township",
    "governance_raw": "Jackson Township Board of Trustees",
    "partner_agencies_raw": None,
    "coordination_raw": None,
    "gps_lat_raw": None,
    "gps_lon_raw": None,
    "location_raw": "County Road 592 (SW corner of W County Road 592 and County Road 39), Jackson Township, Seneca County, OH",
    "acres_raw": None,
    "description_raw": "Active township cemetery maintained by Jackson Township Board of Trustees. Accepts new burials for residents and non-residents (price schedule maintained by township). Also known as Zion Lutheran Cemetery in OGS Ohio Cemeteries 1803-2003 (# 11096 or similar); ODRE registration number CGR.0000980335.",
    "features_raw": None,
    "difficulty_raw": None,
    "accessibility_raw": None,
    "urls_raw": [
        "https://jacksontwpseneca.org/cemetery",
    ],
    "identity_notes_raw": (
        "Confirmed township-owned and trustee-managed per Jackson Township of Seneca County official website. "
        "Jackson Township has two cemeteries; this is the active one. "
        "Location: SW corner of W County Road 592 and County Road 39 per GNIS/genealogy sources. "
        "ODRE registration CGR.0000980335 as 'Zion Cemetery' (distinct from 'Zion Lutheran Cemetery' which is "
        "a church-owned entity in the same township)."
    ),
    "township_raw": None,
    "municipality_raw": None,
    "discovery_tier": 5,
    "seeded_from_baseline": False,
    "baseline_id": None,
}

# --- JACKSON TOWNSHIP: Disinger Cemetery ---
disinger_cem = {
    "entity_type": "Site",
    "name_raw": "Disinger Cemetery",
    "counties_raw": ["Seneca"],
    "county_primary": "Seneca",
    "ownership_raw": "Jackson Township",
    "governance_raw": "Jackson Township Board of Trustees",
    "partner_agencies_raw": None,
    "coordination_raw": None,
    "gps_lat_raw": None,
    "gps_lon_raw": None,
    "location_raw": "County Road 25, Jackson Township, Seneca County, OH",
    "acres_raw": None,
    "description_raw": "Non-active (closed to new burials) township cemetery maintained by Jackson Township Board of Trustees. Located on County Road 25.",
    "features_raw": None,
    "difficulty_raw": None,
    "accessibility_raw": None,
    "urls_raw": [
        "https://jacksontwpseneca.org/cemetery",
    ],
    "identity_notes_raw": (
        "Confirmed township-owned and trustee-managed per Jackson Township of Seneca County official website. "
        "Jackson Township has two cemeteries; this is the non-active one. "
        "Location: County Road 25 per township website."
    ),
    "township_raw": None,
    "municipality_raw": None,
    "discovery_tier": 5,
    "seeded_from_baseline": False,
    "baseline_id": None,
}

# --- EDEN TOWNSHIP: Rock Run Cemetery ---
rock_run_cem = {
    "entity_type": "Site",
    "name_raw": "Rock Run Cemetery",
    "counties_raw": ["Seneca"],
    "county_primary": "Seneca",
    "ownership_raw": "Eden Township",
    "governance_raw": "Eden Township Board of Trustees",
    "partner_agencies_raw": None,
    "coordination_raw": None,
    "gps_lat_raw": None,
    "gps_lon_raw": None,
    "location_raw": "West side of S. Township Road 17, approximately 0.2 miles south of US 224 (Benjamin Franklin Highway), Eden Township, Seneca County, OH",
    "acres_raw": None,
    "description_raw": (
        "Historic cemetery in Eden Township, Seneca County. Originally under Methodist Church caretakership; "
        "transferred to Eden Township Trustees in the late 1970s. Also known as Rock Creek Cemetery. "
        "OGS Ohio Cemeteries 1803-2003 reference #11107."
    ),
    "features_raw": None,
    "difficulty_raw": None,
    "accessibility_raw": None,
    "urls_raw": [
        "http://www.historynotebook.com/Rockrun.htm",
    ],
    "identity_notes_raw": (
        "Confirmed township-owned: cemetery 'was finally turned over to the Eden Township Trustees in the late 1970s' "
        "per historynotebook.com historical account of the site. "
        "Also referenced as Rock Creek Cemetery in GNIS. Location: S Township Road 17 x US 224."
    ),
    "township_raw": None,
    "municipality_raw": None,
    "discovery_tier": 5,
    "seeded_from_baseline": False,
    "baseline_id": None,
}

# --- VENICE TOWNSHIP: Attica Venice Township Joint Cemetery ---
attica_venice_cem = {
    "entity_type": "Site",
    "name_raw": "Attica Venice Township Joint Cemetery",
    "counties_raw": ["Seneca"],
    "county_primary": "Seneca",
    "ownership_raw": "Venice Township / Village of Attica (joint)",
    "governance_raw": "Venice Township Board of Trustees (joint with Village of Attica)",
    "partner_agencies_raw": ["Village of Attica"],
    "coordination_raw": "Joint cemetery — Venice Township and Village of Attica",
    "gps_lat_raw": None,
    "gps_lon_raw": None,
    "location_raw": "Two blocks east of State Route 4, Attica, OH 44807 (Venice Township, Seneca County)",
    "acres_raw": None,
    "description_raw": (
        "Jointly administered cemetery for Venice Township and the Village of Attica. "
        "Located adjacent to Saints Peter and Paul Catholic Cemetery, two blocks east of SR 4 in Attica. "
        "Registered with Ohio Division of Real Estate and Professional Licensing. "
        "Ohio Auditor audit records on file (Report released 2014 covering 2013-2012)."
    ),
    "features_raw": None,
    "difficulty_raw": None,
    "accessibility_raw": None,
    "urls_raw": [
        "https://www.findagrave.com/cemetery/1983864/attica-venice-township-joint-cemetery",
        "https://ohioauditor.gov/auditsearch/Reports/2014/Attica_Venice_Township_Joint_Cemetery_13_12_Seneca.pdf",
    ],
    "identity_notes_raw": (
        "ODRE registration license number CGR.0000981776. "
        "Ohio Auditor records confirm joint entity. "
        "Joint governance: Venice Township Board of Trustees + Village of Attica. "
        "Classified as Tier 5 (Township governance primary). "
        "2,380+ burials documented in genealogy sources."
    ),
    "township_raw": None,
    "municipality_raw": None,
    "discovery_tier": 5,
    "seeded_from_baseline": False,
    "baseline_id": None,
}

# --- BLOOM TOWNSHIP: Bloom Township Cemetery ---
bloom_cem = {
    "entity_type": "Site",
    "name_raw": "Bloom Township Cemetery",
    "counties_raw": ["Seneca"],
    "county_primary": "Seneca",
    "ownership_raw": "Bloom Township (probable)",
    "governance_raw": "Bloom Township Board of Trustees (probable)",
    "partner_agencies_raw": None,
    "coordination_raw": None,
    "gps_lat_raw": None,
    "gps_lon_raw": None,
    "location_raw": "E Township Road 58 and S County Road 43, Bloomville, OH (Bloom Township, Seneca County); also referenced as 6214-6252 E Township Road 58, Tiffin, OH 44883",
    "acres_raw": None,
    "description_raw": "Cemetery in Bloom Township, Seneca County named 'Bloom Township Cemetery'. 56 memorial records on Find A Grave. GNIS feature ID: 1730838.",
    "features_raw": None,
    "difficulty_raw": None,
    "accessibility_raw": None,
    "urls_raw": [
        "https://www.findagrave.com/cemetery/2327250/bloom-township-cemetery",
        "https://billiongraves.com/cemetery/Bloom-Township-Cemetery/124265",
    ],
    "identity_notes_raw": (
        "Ownership presumed township based on naming convention (named 'Bloom Township Cemetery'). "
        "No explicit township trustee ownership statement found in web sources. "
        "Flag for human verification of governance status. "
        "GNIS feature ID: 1730838. IDENTITY_UNCERTAIN — ownership not confirmed from authoritative source."
    ),
    "township_raw": None,
    "municipality_raw": None,
    "discovery_tier": 5,
    "seeded_from_baseline": False,
    "baseline_id": None,
}

# --- LOUDON TOWNSHIP: Loudon Township Cemetery ---
loudon_cem = {
    "entity_type": "Site",
    "name_raw": "Loudon Township Cemetery",
    "counties_raw": ["Seneca"],
    "county_primary": "Seneca",
    "ownership_raw": "Loudon Township (probable)",
    "governance_raw": "Loudon Township Board of Trustees (probable)",
    "partner_agencies_raw": None,
    "coordination_raw": None,
    "gps_lat_raw": 41.13533,
    "gps_lon_raw": -83.38742,
    "location_raw": "State Route 18 East, Fostoria, OH 44830 (Loudon Township, Seneca County)",
    "acres_raw": None,
    "description_raw": "Cemetery in Loudon Township southeast of Fostoria on SR 18 East. Named 'Loudon Township Cemetery'. 217 memorial records on Find A Grave (72% photographed).",
    "features_raw": None,
    "difficulty_raw": None,
    "accessibility_raw": None,
    "urls_raw": [
        "https://www.findagrave.com/cemetery/2168073/loudon-township-cemetery",
    ],
    "identity_notes_raw": (
        "Ownership presumed township based on naming convention ('Loudon Township Cemetery'). "
        "GPS coordinates from geographic sources: 41.13533, -83.38742. "
        "Historical note: Oak Grove Cemetery Association of Loudon Township organized 1857 — "
        "may have been predecessor organization before transfer to township. "
        "Flag for human verification of governance status. IDENTITY_UNCERTAIN."
    ),
    "township_raw": None,
    "municipality_raw": None,
    "discovery_tier": 5,
    "seeded_from_baseline": False,
    "baseline_id": None,
}

# --- PLEASANT TOWNSHIP: 5 cemeteries maintained by township ---
pleasant_cems = [
    {
        "name_raw": "Chenoweth Cemetery",
        "location_raw": "Gay Road area, Pleasant Township, Seneca County, OH",
        "description_raw": "Township-maintained cemetery in Pleasant Township on Gay Road.",
    },
    {
        "name_raw": "Gundy Cemetery",
        "location_raw": "Norton Road, Pleasant Township, Seneca County, OH",
        "description_raw": "Township-maintained cemetery in Pleasant Township on Norton Road.",
    },
    {
        "name_raw": "Ebenezer M.E. Cemetery",
        "location_raw": "Johnson Road, Pleasant Township, Seneca County, OH",
        "description_raw": "Township-maintained cemetery in Pleasant Township on Johnson Road. 'M.E.' = Methodist Episcopal — may be former church cemetery now under township maintenance.",
    },
    {
        "name_raw": "Little Pennsylvania Cemetery",
        "location_raw": "State Route 665, Pleasant Township, Seneca County, OH",
        "description_raw": "Township-maintained cemetery in Pleasant Township on SR 665.",
    },
    {
        "name_raw": "Oak Grove Cemetery",
        "location_raw": "Alkire Road, Pleasant Township, Seneca County, OH",
        "description_raw": "Township-maintained cemetery in Pleasant Township on Alkire Road.",
    },
]

pleasant_cem_records = []
for pc in pleasant_cems:
    pleasant_cem_records.append({
        "entity_type": "Site",
        "name_raw": pc["name_raw"],
        "counties_raw": ["Seneca"],
        "county_primary": "Seneca",
        "ownership_raw": "Pleasant Township (maintained by township; ownership unconfirmed)",
        "governance_raw": "Pleasant Township Board of Trustees",
        "partner_agencies_raw": None,
        "coordination_raw": None,
        "gps_lat_raw": None,
        "gps_lon_raw": None,
        "location_raw": pc["location_raw"],
        "acres_raw": None,
        "description_raw": pc["description_raw"],
        "features_raw": None,
        "difficulty_raw": None,
        "accessibility_raw": None,
        "urls_raw": ["https://www.pleasanttownshipsenecacounty.com/"],
        "identity_notes_raw": (
            "Source: pleasanttownshipsenecacounty.com states 'Pleasant Township maintains 5 cemeteries "
            "within the township borders.' Township as governance entity confirmed. "
            "Ownership vs. maintenance distinction not explicitly stated on website. "
            "Flag for human verification: confirm whether township owns vs. only maintains. "
            "IDENTITY_UNCERTAIN — ownership not confirmed from authoritative source."
        ),
        "township_raw": None,
        "municipality_raw": None,
        "discovery_tier": 5,
        "seeded_from_baseline": False,
        "baseline_id": None,
    })

# Assemble all T5 records
t5_records = [
    meadowbrook,
    zion_cem,
    disinger_cem,
    rock_run_cem,
    attica_venice_cem,
    bloom_cem,
    loudon_cem,
] + pleasant_cem_records

for r in t5_records:
    data["records"].append(r)

# =====================================================================
# TIER 5 NULL BLOCKS (per township + entity type)
# =====================================================================

t5_nulls = [
    # --- PARKS: All townships except Hopewell ---
    {
        "tier": 5,
        "governance_level": "Adams Township — Parks/Recreation",
        "entity_type": "Site / Trail / Access Point",
        "result": "null",
        "sources_checked": ["https://adamstwpoh.com/"],
        "reasoning": "Adams Township website (adamstwpoh.com — confirmed Seneca County) has no parks, recreation, or natural areas. No county-hosted parks page found. No parks or trails found in web searches.",
    },
    {
        "tier": 5,
        "governance_level": "Big Spring Township — Parks/Recreation",
        "entity_type": "Site / Trail / Access Point",
        "result": "null",
        "sources_checked": [
            "Web search: Big Spring Township Seneca County Ohio parks recreation",
        ],
        "reasoning": "No township website found for Big Spring Township, Seneca County. Web searches returned no parks, recreation areas, or trails managed by Big Spring Township. No county-hosted Big Spring Township parks page found.",
    },
    {
        "tier": 5,
        "governance_level": "Bloom Township — Parks/Recreation",
        "entity_type": "Site / Trail / Access Point",
        "result": "null",
        "sources_checked": [
            "Web search: Bloom Township Seneca County Ohio parks recreation",
        ],
        "reasoning": "No township website found for Bloom Township, Seneca County. No parks or recreation areas found in web searches. Bloom Township Cemetery staged separately.",
    },
    {
        "tier": 5,
        "governance_level": "Clinton Township — Parks/Recreation",
        "entity_type": "Site / Trail / Access Point",
        "result": "null",
        "sources_checked": [
            "https://clintontwpsenecacounty.com/",
            "https://www.senecacountyparks.com/places/clinton-nature-preserve",
        ],
        "reasoning": (
            "Clinton Township website (clintontwpsenecacounty.com — 'senecacounty' in domain, verified Seneca County) "
            "has no parks or recreation pages. Clinton Nature Preserve is SCPD (Tier 3) with Clinton Township as "
            "co-management partner — NOT a T5 Township entity. No Clinton Township-owned parks found."
        ),
    },
    {
        "tier": 5,
        "governance_level": "Eden Township — Parks/Recreation",
        "entity_type": "Site / Trail / Access Point",
        "result": "null",
        "sources_checked": [
            "Web search: Eden Township Seneca County Ohio parks recreation",
        ],
        "reasoning": "No township website found for Eden Township, Seneca County. No parks or recreation areas found. Eden Township cemetery (Rock Run) staged separately.",
    },
    {
        "tier": 5,
        "governance_level": "Hopewell Township — Parks/Recreation (additional)",
        "entity_type": "Trail / Access Point (additional to Meadowbrook Park)",
        "result": "null",
        "sources_checked": [
            "https://mbpark.org/brief-overview/",
            "https://hopewell-township.com/",
        ],
        "reasoning": "Meadowbrook Park staged as T5 Site. No additional named trails, trail networks, or access points found beyond Meadowbrook Park's internal foot trails. Internal park trails are part of the park entity, not separate T5 trail entities.",
    },
    {
        "tier": 5,
        "governance_level": "Jackson Township — Parks/Recreation",
        "entity_type": "Site / Trail / Access Point",
        "result": "null",
        "sources_checked": [
            "https://jacksontwpseneca.org/",
        ],
        "reasoning": "Jackson Township website (jacksontwpseneca.org — confirmed Seneca County; address: 10014 W County Road 28, Fostoria, OH 44830) lists no parks, recreation areas, or trails. Two cemeteries staged separately.",
    },
    {
        "tier": 5,
        "governance_level": "Liberty Township — Parks/Recreation",
        "entity_type": "Site / Trail / Access Point",
        "result": "null",
        "sources_checked": [
            "Web search: Liberty Township Seneca County Ohio parks recreation",
        ],
        "reasoning": (
            "No website found for Liberty Township, Seneca County. "
            "§4.2a caution: search results returned Liberty Township websites for Delaware County, Hancock County, "
            "and other counties — all discarded as wrong-county. "
            "No township parks, recreation, or trails found for Liberty Township, Seneca County specifically."
        ),
    },
    {
        "tier": 5,
        "governance_level": "Loudon Township — Parks/Recreation",
        "entity_type": "Site / Trail / Access Point",
        "result": "null",
        "sources_checked": [
            "https://www.loudontownship.com/",
        ],
        "reasoning": "Loudon Township website is minimal (confirmed Seneca County via OTA roster). No parks, recreation areas, or trails listed. Loudon Township Cemetery staged separately.",
    },
    {
        "tier": 5,
        "governance_level": "Pleasant Township — Parks/Recreation",
        "entity_type": "Site / Trail / Access Point",
        "result": "null",
        "sources_checked": [
            "https://www.pleasanttownshipsenecacounty.com/",
        ],
        "reasoning": "Pleasant Township website ('senecacounty' in domain — verified Seneca County) lists no parks, recreation areas, or trails. 5 cemeteries staged separately.",
    },
    {
        "tier": 5,
        "governance_level": "Reed Township — Parks/Recreation",
        "entity_type": "Site / Trail / Access Point",
        "result": "null",
        "sources_checked": [
            "Web search: Reed Township Seneca County Ohio parks recreation",
            "https://www.senecarpc.org/housing-and-zoning/zoning/reed",
        ],
        "reasoning": "No township website found for Reed Township, Seneca County (meeting place: Reed Township House, 14027 SR 162, Republic, Ohio 44867). No parks, recreation, or trails found in web searches.",
    },
    {
        "tier": 5,
        "governance_level": "Scipio Township — Parks/Recreation",
        "entity_type": "Site / Trail / Access Point",
        "result": "null",
        "sources_checked": [
            "Web search: Scipio Township Seneca County Ohio parks recreation",
        ],
        "reasoning": "No township website found for Scipio Township, Seneca County. No parks, recreation, or trails found in web searches.",
    },
    {
        "tier": 5,
        "governance_level": "Seneca Township — Parks/Recreation",
        "entity_type": "Site / Trail / Access Point",
        "result": "null",
        "sources_checked": [
            "Web search: Seneca Township Seneca County Ohio parks recreation",
        ],
        "reasoning": "No township website found for Seneca Township, Seneca County. No parks, recreation, or trails found in web searches.",
    },
    {
        "tier": 5,
        "governance_level": "Thompson Township — Parks/Recreation",
        "entity_type": "Site / Trail / Access Point",
        "result": "null",
        "sources_checked": [
            "Web search: Thompson Township Seneca County Ohio parks recreation",
            "https://www.thompsonohio.org/ (DISCARDED — §4.2a: website confirmed Geauga County OH 44086, not Seneca County)",
        ],
        "reasoning": (
            "thompsonohio.org appears to be Thompson Township, Geauga County (zip 44086, Geauga County Public Library reference) "
            "— discarded per §4.2a county verification. "
            "No authoritative website or parks page found for Thompson Township, Seneca County. "
            "Thompson Township, Seneca County includes the census-designated place of Flat Rock (per Wikipedia). "
            "No parks, recreation, or trails confirmed."
        ),
    },
    {
        "tier": 5,
        "governance_level": "Venice Township — Parks/Recreation",
        "entity_type": "Site / Trail / Access Point",
        "result": "null",
        "sources_checked": [
            "Web search: Venice Township Seneca County Ohio parks recreation",
        ],
        "reasoning": "No township website found for Venice Township, Seneca County. No parks, recreation, or trails found. Attica Venice Township Joint Cemetery staged separately.",
    },
    # --- CEMETERIES: Townships with no confirmed township-owned cemetery staged ---
    {
        "tier": 5,
        "governance_level": "Adams Township — Township-owned cemeteries",
        "entity_type": "Site (Cemetery)",
        "result": "null (cemeteries exist; township-owned name(s) unconfirmed)",
        "sources_checked": [
            "https://adamstwpoh.com/",
            "Web search: Adams Township Seneca County Ohio cemetery findagrave",
            "https://www.findagrave.com/cemetery/2136539/adams-lutheran-cemetery",
        ],
        "reasoning": (
            "Adams Township Facebook page references April 1 clean-up of township cemetery, confirming a township-owned "
            "cemetery exists. Specific name not found from official sources. "
            "Confirmed church-owned cemeteries in Adams Township (excluded from T5): "
            "Adams Lutheran Cemetery (Zion Lutheran Church ownership, GNIS 1730834), "
            "Union Cemetery / Albright Cemetery (ODRE CGR.0000983352 — ownership unclear). "
            "Township-owned cemetery name not confirmed — flagged for further verification."
        ),
    },
    {
        "tier": 5,
        "governance_level": "Big Spring Township — Township-owned cemeteries",
        "entity_type": "Site (Cemetery)",
        "result": "null (cemeteries known to exist; township-owned name(s) unconfirmed)",
        "sources_checked": [
            "Web search: Big Spring Township Seneca County Ohio cemetery",
        ],
        "reasoning": "Big Spring Township maintains cemetery services per county records. No specific township-owned cemetery name confirmed from web sources. No township website found. Flagged for further verification.",
    },
    {
        "tier": 5,
        "governance_level": "Clinton Township — Township-owned cemeteries",
        "entity_type": "Site (Cemetery)",
        "result": "null (cemeteries known; township-owned unconfirmed)",
        "sources_checked": [
            "https://clintontwpsenecacounty.com/",
            "Web search: Clinton Township Seneca County Ohio cemetery names",
        ],
        "reasoning": (
            "Clinton Township website mentions cemetery maintenance services. "
            "Confirmed church-owned cemeteries in Clinton Township (excluded from T5): "
            "St. Mary's Catholic Cemetery (referenced on township website). "
            "Brundage Cemetery (also Buckeye/Brundedge) and Fairmont Cemetery (Stoner) mentioned in genealogy sources; "
            "ownership not confirmed as township. No township-owned cemetery name confirmed."
        ),
    },
    {
        "tier": 5,
        "governance_level": "Hopewell Township — Township-owned cemeteries",
        "entity_type": "Site (Cemetery)",
        "result": "null (cemeteries exist; township-owned not confirmed)",
        "sources_checked": [
            "https://hopewell-township.com/",
            "Web search: Hopewell Township Seneca County Ohio cemetery trustees",
        ],
        "reasoning": (
            "Hopewell Cemetery / Britt Cemetery (0.5 acres, Township Road 121, within farm field) is listed in "
            "Hopewell Township but no township ownership confirmed. "
            "Seneca Memory Gardens is a large commercial cemetery (800+ graves) in Hopewell Township — "
            "likely private/for-profit, not township-owned. "
            "No Hopewell Township-specific cemetery ownership confirmed from web sources."
        ),
    },
    {
        "tier": 5,
        "governance_level": "Liberty Township — Township-owned cemeteries",
        "entity_type": "Site (Cemetery)",
        "result": "null (Liberty Cemetery may be township-owned; unconfirmed)",
        "sources_checked": [
            "Web search: Liberty Township Seneca County Ohio cemetery findagrave",
            "https://www.findagrave.com/cemetery/41825/liberty-cemetery (Liberty Cemetery, 954 memorials)",
        ],
        "reasoning": (
            "Liberty Cemetery (coordinates: 41.21750, -83.28670; Find A Grave ID 41825, 954 memorials) in "
            "Liberty Township, Seneca County may be township-owned based on name matching. "
            "Church-owned cemeteries confirmed in Liberty Township (excluded): Saint Andrew Catholic Cemetery. "
            "Township ownership of Liberty Cemetery not confirmed from authoritative source. "
            "§4.2a: liberty-township.com and similar domains discarded — confirmed wrong counties. "
            "Flagged for human verification."
        ),
    },
    {
        "tier": 5,
        "governance_level": "Reed Township — Township-owned cemeteries",
        "entity_type": "Site (Cemetery)",
        "result": "null (cemeteries known; township-owned name(s) unconfirmed)",
        "sources_checked": [
            "Web search: Reed Township Seneca County Ohio cemetery",
        ],
        "reasoning": "Reed Township maintains cemetery services per county records (meeting place: 14027 SR 162, Republic, OH 44867). No township website found. Specific township-owned cemetery name not confirmed from web sources.",
    },
    {
        "tier": 5,
        "governance_level": "Scipio Township — Township-owned cemeteries",
        "entity_type": "Site (Cemetery)",
        "result": "null (cemeteries known; township-owned name(s) unconfirmed)",
        "sources_checked": [
            "Web search: Scipio Township Seneca County Ohio cemetery",
        ],
        "reasoning": "Scipio Township maintains cemetery services per county records. No township website found. Specific township-owned cemetery name not confirmed from web sources.",
    },
    {
        "tier": 5,
        "governance_level": "Seneca Township — Township-owned cemeteries",
        "entity_type": "Site (Cemetery)",
        "result": "null (cemeteries known; township-owned name(s) unconfirmed)",
        "sources_checked": [
            "Web search: Seneca Township Seneca County Ohio cemetery",
        ],
        "reasoning": (
            "Seneca Township maintains cemetery services per county records. No township website found. "
            "South Bend Cemetery and Methodist Cemetery referenced in genealogy sources as being in Seneca Township "
            "area — ownership not confirmed as township (Methodist = likely church-owned). "
            "Specific township-owned cemetery name not confirmed."
        ),
    },
    {
        "tier": 5,
        "governance_level": "Thompson Township (Seneca County) — Township-owned cemeteries",
        "entity_type": "Site (Cemetery)",
        "result": "null (cemeteries known; §4.2a website discarded)",
        "sources_checked": [
            "https://www.thompsonohio.org/ (DISCARDED — confirmed Geauga County per §4.2a)",
            "Web search: Thompson Township Seneca County Ohio cemetery",
        ],
        "reasoning": (
            "thompsonohio.org was investigated but confirmed to be Geauga County Thompson Township (zip 44086, "
            "Geauga County Public Library reference) per §4.2a county verification — discarded. "
            "No authoritative website or cemetery page found for Thompson Township, Seneca County. "
            "Thompson Township (Seneca County) includes the census-designated place of Flat Rock. "
            "Specific township-owned cemetery name not confirmed for Seneca County Thompson Township."
        ),
    },
]

for null in t5_nulls:
    data["tier_nulls"].append(null)

data["current_tier"] = 6

f.write_text(yaml.dump(data, allow_unicode=True, sort_keys=False), encoding="utf-8")
print(f"Staged {len(t5_records)} T5 records + {len(t5_nulls)} T5 null blocks.")
print(f"Total records: {len(data['records'])}, Total tier_nulls: {len(data['tier_nulls'])}")
print(f"current_tier: {data['current_tier']}")
