import yaml, pathlib

f = pathlib.Path(r"D:\users\user1\Documents\CP Projects\Natural Areas Project v5\County_Spreadsheets\Seneca\seneca_ohio_raw_discovery.yaml")
data = yaml.safe_load(f.read_text(encoding="utf-8"))
data.setdefault("records", [])

SCPD_GOV = "Seneca County Park District"
SCPD_OWN = "Seneca County Park District"
SCPD_URL = "https://www.senecacountyparks.com/"

t3_scpd = [
    {
        "entity_type": "Site",
        "name_raw": "Bowen Nature Preserve",
        "counties_raw": ["Seneca"],
        "county_primary": "Seneca",
        "ownership_raw": SCPD_OWN,
        "governance_raw": SCPD_GOV,
        "partner_agencies_raw": None,
        "coordination_raw": None,
        "gps_lat_raw": None,
        "gps_lon_raw": None,
        "location_raw": "11891 East CR 24, Republic, OH 44867",
        "acres_raw": "64",
        "description_raw": (
            "Bowen Nature Preserve became a reality in 2007 with a gift of 58 acres of land from "
            "Johnathan E. Bowen; an additional 6 acres of woodland donated in 2008 by his parents "
            "Yvonne J. and Norman Bowen. Features grassland, restored wetland, historic 1872 house "
            "and 1830s church."
        ),
        "features_raw": ["Grassland", "Wetlands", "Historic house (1872)", "Historic church (1830s)", "Wildlife viewing"],
        "difficulty_raw": None,
        "accessibility_raw": None,
        "urls_raw": ["https://www.senecacountyparks.com/places/bowen-nature-preserve"],
        "identity_notes_raw": "Baseline seed confirmed. Baseline listed 66 ac; authoritative source (SCPD website) lists 64 ac (58+6).",
        "township_raw": None,
        "municipality_raw": None,
        "discovery_tier": 3,
        "seeded_from_baseline": True,
        "baseline_id": "Bowen Nature Preserve",
    },
    {
        "entity_type": "Site",
        "name_raw": "Clinton Nature Preserve",
        "counties_raw": ["Seneca"],
        "county_primary": "Seneca",
        "ownership_raw": "Ohio Department of Natural Resources (ODNR) — leased to Seneca County Park District",
        "governance_raw": SCPD_GOV,
        "partner_agencies_raw": "Clinton Township Trustees; Ohio Department of Natural Resources (ODNR)",
        "coordination_raw": (
            "Cooperative effort between Seneca County Park District, Clinton Township Trustees, "
            "and the Ohio Department of Natural Resources. Land leased from ODNR."
        ),
        "gps_lat_raw": None,
        "gps_lon_raw": None,
        "location_raw": "400 East TR 132, Tiffin, OH 44883",
        "acres_raw": "33",
        "description_raw": (
            "Clinton Nature Preserve and Sandusky River Access is a cooperative effort between the "
            "Seneca County Park District, Clinton Township Trustees, and the Ohio Department of Natural "
            "Resources. Land is leased from ODNR. Includes Sandusky River access and trail on Clinton TR 141. "
            "Access lane and parking close seasonally Nov 1 through Apr 1; year-round access via adjacent "
            "Schekelhoff entrance."
        ),
        "features_raw": ["Sandusky River access", "Trail (principal trail on TR 141)", "Parking (seasonal)"],
        "difficulty_raw": None,
        "accessibility_raw": None,
        "urls_raw": ["https://www.senecacountyparks.com/places/clinton-nature-preserve"],
        "identity_notes_raw": (
            "ODNR-owned land managed by SCPD under lease. "
            "Per NAP protocol, management tier governs (Tier 3 — SCPD). "
            "Adjacent to Schekelhoff Nature Preserve (Tiffin Parks and Recreation — Tier 6)."
        ),
        "township_raw": None,
        "municipality_raw": None,
        "discovery_tier": 3,
        "seeded_from_baseline": True,
        "baseline_id": "Clinton Nature Preserve",
    },
    {
        "entity_type": "Site",
        "name_raw": "Forrest Nature Preserve",
        "counties_raw": ["Seneca"],
        "county_primary": "Seneca",
        "ownership_raw": SCPD_OWN,
        "governance_raw": SCPD_GOV,
        "partner_agencies_raw": None,
        "coordination_raw": None,
        "gps_lat_raw": None,
        "gps_lon_raw": None,
        "location_raw": "701 E. County Road 6, Tiffin, OH 44883",
        "acres_raw": "47",
        "description_raw": (
            "George Forrest family donated five acres in 2002; Clean Ohio grant enabled acquisition of "
            "23.5 acres total. An additional 23.4 acres acquired in 2011, bringing total to 47 acres. "
            "Riparian habitat preserve supporting park district conservation mission. "
            "Two parking areas: upper lot (6390 S TR 151) and lower lot (701 E CR 6)."
        ),
        "features_raw": ["Riparian habitat", "Parking (upper lot at 6390 S TR 151)", "Parking (lower lot at 701 E CR 6)"],
        "difficulty_raw": None,
        "accessibility_raw": None,
        "urls_raw": ["https://www.senecacountyparks.com/places/forrest-nature-preserve"],
        "identity_notes_raw": "Baseline listed 47 ac — confirmed. SCPD website initially showed 23.5 ac (original acquisition); full 47 ac confirmed on property page.",
        "township_raw": None,
        "municipality_raw": None,
        "discovery_tier": 3,
        "seeded_from_baseline": True,
        "baseline_id": "Forrest Nature Preserve",
    },
    {
        "entity_type": "Site",
        "name_raw": "Fruth Wetland Nature Preserve",
        "counties_raw": ["Seneca"],
        "county_primary": "Seneca",
        "ownership_raw": SCPD_OWN,
        "governance_raw": SCPD_GOV,
        "partner_agencies_raw": None,
        "coordination_raw": None,
        "gps_lat_raw": None,
        "gps_lon_raw": None,
        "location_raw": "10130 West SR 18, Fostoria, OH 44830",
        "acres_raw": "20",
        "description_raw": "20-acre wetland nature preserve. The Seneca County Park District office is located at this address.",
        "features_raw": ["Wetlands"],
        "difficulty_raw": None,
        "accessibility_raw": None,
        "urls_raw": ["https://www.senecacountyparks.com/places/fruth-wetland-nature-preserve"],
        "identity_notes_raw": "SCPD park office co-located at 10130 West SR 18. Baseline listed 20 ac — confirmed.",
        "township_raw": None,
        "municipality_raw": None,
        "discovery_tier": 3,
        "seeded_from_baseline": True,
        "baseline_id": "Fruth Wetland Nature Preserve",
    },
    {
        "entity_type": "Site",
        "name_raw": "Garlo Heritage Nature Preserve",
        "counties_raw": ["Seneca"],
        "county_primary": "Seneca",
        "ownership_raw": SCPD_OWN,
        "governance_raw": SCPD_GOV,
        "partner_agencies_raw": None,
        "coordination_raw": None,
        "gps_lat_raw": None,
        "gps_lon_raw": None,
        "location_raw": "6777 South SR 19, Bloomville, OH 44818",
        "acres_raw": "292",
        "description_raw": (
            "Established in 1997 through a gift of 256 acres by Dolly and Alma Garlo. Honors physicians "
            "Olgier and Maria Garlo and their son Alex, who immigrated from Eastern Europe in 1948 and began "
            "acquiring the land in 1961. Encompasses fields, wetlands, and deciduous forest. "
            "7.4 miles of developed equestrian and hiking trails."
        ),
        "features_raw": ["Equestrian trails (7.4 mi total)", "Hiking trails", "Fields", "Wetlands", "Deciduous forest"],
        "difficulty_raw": None,
        "accessibility_raw": None,
        "urls_raw": ["https://www.senecacountyparks.com/places/garlo-heritage-nature-preserve"],
        "identity_notes_raw": "Baseline listed 292 ac — confirmed. Original gift was 256 ac (1997); additional acquisitions brought total to 292 ac.",
        "township_raw": None,
        "municipality_raw": None,
        "discovery_tier": 3,
        "seeded_from_baseline": True,
        "baseline_id": "Garlo Heritage Nature Preserve",
    },
    {
        "entity_type": "Site",
        "name_raw": "Mercy Community Nature Preserve",
        "counties_raw": ["Seneca"],
        "county_primary": "Seneca",
        "ownership_raw": "Mercy Tiffin Hospital / Seneca County Park District (cooperative partnership)",
        "governance_raw": SCPD_GOV,
        "partner_agencies_raw": "Mercy Tiffin Hospital",
        "coordination_raw": "Cooperative partnership between Mercy Tiffin Hospital and Seneca County District Parks.",
        "gps_lat_raw": None,
        "gps_lon_raw": None,
        "location_raw": "45 St. Lawrence Drive, Tiffin, OH 44883",
        "acres_raw": "22",
        "description_raw": (
            "Opening in 2013 as part of the 100th anniversary of the founding of Mercy Tiffin Hospital, "
            "the hospital in partnership with the park district dedicated the 22-acre nature preserve to "
            "the health and wellness of Tiffin and Seneca County."
        ),
        "features_raw": ["Walking trail", "Footbridge", "Totem pole (entrance)", "Picnic area"],
        "difficulty_raw": None,
        "accessibility_raw": None,
        "urls_raw": ["https://www.senecacountyparks.com/places/mercy-community-nature-preserve"],
        "identity_notes_raw": "Co-managed preserve on Mercy Tiffin Hospital grounds. SCPD governs per management agreement.",
        "township_raw": None,
        "municipality_raw": None,
        "discovery_tier": 3,
        "seeded_from_baseline": True,
        "baseline_id": "Mercy Community Nature Preserve",
    },
    {
        "entity_type": "Site",
        "name_raw": "Opportunity Park",
        "counties_raw": ["Seneca"],
        "county_primary": "Seneca",
        "ownership_raw": "Seneca County Commissioners / Opportunity Center / Seneca County Park District (cooperative)",
        "governance_raw": SCPD_GOV,
        "partner_agencies_raw": "Seneca County Commissioners; Seneca County Opportunity Center",
        "coordination_raw": (
            "Cooperative partnership among Seneca County Commissioners, Opportunity Center, and Seneca Parks. "
            "Maintenance by Opportunity Center."
        ),
        "gps_lat_raw": None,
        "gps_lon_raw": None,
        "location_raw": "780 East CR 20, Tiffin, OH 44883",
        "acres_raw": None,
        "description_raw": (
            "Rural park established in 2008 with W.K. Kellogg Foundation support, adjacent to the Seneca "
            "County Opportunity Center on farmland. Open daily sunrise to sunset. "
            "Features fully-accessible inclusive playground, 820-foot paved exercise track, paved trails, "
            "and picnic shelters."
        ),
        "features_raw": ["Accessible playground", "Paved exercise track (820 ft)", "Paved trails", "Picnic shelters", "Picnic tables"],
        "difficulty_raw": None,
        "accessibility_raw": "Fully accessible (paved track, accessible playground)",
        "urls_raw": ["https://www.senecacountyparks.com/places/opportunity-park"],
        "identity_notes_raw": "Co-managed park. SCPD listed on website. County Commissioners and Opportunity Center as co-partners.",
        "township_raw": None,
        "municipality_raw": None,
        "discovery_tier": 3,
        "seeded_from_baseline": True,
        "baseline_id": "Opportunity Park",
    },
    {
        "entity_type": "Site",
        "name_raw": "Steyer Nature Preserve",
        "counties_raw": ["Seneca"],
        "county_primary": "Seneca",
        "ownership_raw": SCPD_OWN,
        "governance_raw": SCPD_GOV,
        "partner_agencies_raw": None,
        "coordination_raw": None,
        "gps_lat_raw": None,
        "gps_lon_raw": None,
        "location_raw": "5901 North CR 33, Tiffin, OH 44883",
        "acres_raw": "141",
        "description_raw": (
            "Originated in 2003 from a land donation by Tony and Kathy Steyer, supplemented by Clean Ohio "
            "grants and ODNR Scenic River funding. Encompasses nearly a mile of Sandusky River frontage. "
            "4.17 miles of trails with eight bridges over beautiful ravines. Northern 71 acres are "
            "non-hunting conservation area; southern 70 acres open for seasonal hunting. "
            "Adjacent to Sugar Creek State Wildlife Area."
        ),
        "features_raw": [
            "Sandusky River frontage (~1 mi)",
            "Trails (4.17 mi, 8 bridges)",
            "Scenic ravines",
            "Abbott's Bridge Scenic River Access parking (North CR 33)",
            "Pleasant TR 148 access (southern section)",
            "Hunting (southern 70 ac, seasonal only)",
        ],
        "difficulty_raw": None,
        "accessibility_raw": None,
        "urls_raw": ["https://www.senecacountyparks.com/places/steyer-nature-preserve"],
        "identity_notes_raw": (
            "Baseline listed 141 ac — confirmed. Two named access points: Abbott's Bridge Scenic River "
            "Access (off North CR 33) and Pleasant TR 148 southern access — may qualify as Access Points "
            "to Sandusky State Scenic River. Resolve during Access Point pass."
        ),
        "township_raw": None,
        "municipality_raw": None,
        "discovery_tier": 3,
        "seeded_from_baseline": True,
        "baseline_id": "Steyer Nature Preserve",
    },
    {
        "entity_type": "Site",
        "name_raw": "Tiffin University Nature Preserve",
        "counties_raw": ["Seneca"],
        "county_primary": "Seneca",
        "ownership_raw": "Tiffin University (land); Seneca County Park District (management)",
        "governance_raw": SCPD_GOV,
        "partner_agencies_raw": "Tiffin University; W.K. Kellogg Foundation",
        "coordination_raw": "Cooperative management agreement between Tiffin University and Seneca County Park District.",
        "gps_lat_raw": None,
        "gps_lon_raw": None,
        "location_raw": "2471 West CR 26, Tiffin, OH 44883",
        "acres_raw": None,
        "description_raw": (
            "Regionally significant ecosystem dedicated June 5, 2007, featuring restored wetlands and "
            "streamside forests with interpretive elements for learning and recreation. "
            "Developed through partnership with W.K. Kellogg Foundation, Seneca County Park District, "
            "and the state of Ohio. Located on Tiffin University land."
        ),
        "features_raw": [
            "Restored wetland (2 acres)",
            "Vernal pool",
            "Streamside forested walkway with three bridges",
            "Hiking trail (1.23 mi)",
            "Picnic area",
            "Gazebo",
        ],
        "difficulty_raw": None,
        "accessibility_raw": None,
        "urls_raw": ["https://www.senecacountyparks.com/places/tiffin-university-nature-preserve"],
        "identity_notes_raw": (
            "Located on Tiffin University (private university) land, managed under cooperative agreement "
            "with SCPD. Governance by SCPD → Tier 3. Tiffin University is private → not a Tier 2 entity. "
            "No acreage found from authoritative source."
        ),
        "township_raw": None,
        "municipality_raw": None,
        "discovery_tier": 3,
        "seeded_from_baseline": True,
        "baseline_id": "Tiffin University Nature Preserve",
    },
    {
        "entity_type": "Site",
        "name_raw": "Zimmerman Nature Preserve",
        "counties_raw": ["Seneca"],
        "county_primary": "Seneca",
        "ownership_raw": SCPD_OWN,
        "governance_raw": SCPD_GOV,
        "partner_agencies_raw": None,
        "coordination_raw": None,
        "gps_lat_raw": None,
        "gps_lon_raw": None,
        "location_raw": "680 East SR 18, Tiffin, OH 44883",
        "acres_raw": "5.5",
        "description_raw": None,
        "features_raw": [],
        "difficulty_raw": None,
        "accessibility_raw": None,
        "urls_raw": ["https://www.senecacountyparks.com/places/zimmerman-nature-preserve"],
        "identity_notes_raw": "Baseline listed 5.5 ac at 680 East SR 18, Tiffin — confirmed from SCPD website.",
        "township_raw": None,
        "municipality_raw": None,
        "discovery_tier": 3,
        "seeded_from_baseline": True,
        "baseline_id": "Zimmerman Nature Preserve",
    },
    {
        "entity_type": "Site",
        "name_raw": "St. John's Mill River Access",
        "counties_raw": ["Seneca"],
        "county_primary": "Seneca",
        "ownership_raw": SCPD_OWN,
        "governance_raw": SCPD_GOV,
        "partner_agencies_raw": "Seneca County Land Bank (property donor)",
        "coordination_raw": None,
        "gps_lat_raw": None,
        "gps_lon_raw": None,
        "location_raw": "2320 West CR 6, Tiffin, OH 44883",
        "acres_raw": None,
        "description_raw": (
            "Scheduled to open in 2023. Property donated by Seneca County Land Bank in 2021. "
            "Located along the Sandusky Scenic River at the former site of the St. John's Dam."
        ),
        "features_raw": ["Sandusky River access", "Former dam site"],
        "difficulty_raw": None,
        "accessibility_raw": None,
        "urls_raw": ["https://www.senecacountyparks.com/places/st-johns-mill-river-access"],
        "identity_notes_raw": (
            "River access park on Sandusky Scenic River at former St. John's Dam site. "
            "May qualify as an Access Point to the Sandusky State Scenic River (T2, CROSS_COUNTY_CANDIDATE). "
            "Staged as Site; resolve as AP candidate during Access Point pass. No acreage found."
        ),
        "township_raw": None,
        "municipality_raw": None,
        "discovery_tier": 3,
        "seeded_from_baseline": True,
        "baseline_id": "St. John's Mill River Access",
    },
]

for r in t3_scpd:
    data["records"].append(r)

f.write_text(yaml.dump(data, allow_unicode=True, sort_keys=False), encoding="utf-8")
print(f"Staged {len(t3_scpd)} SCPD T3 Sites. Total records now: {len(data['records'])}")
