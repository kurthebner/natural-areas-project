import yaml, pathlib

f = pathlib.Path(r"D:\users\user1\Documents\CP Projects\Natural Areas Project v5\County_Spreadsheets\Seneca\seneca_ohio_raw_discovery.yaml")
data = yaml.safe_load(f.read_text(encoding="utf-8"))
data.setdefault("records", [])

t2_records = [
    {
        "entity_type": "Site",
        "name_raw": "Howard Collier State Nature Preserve",
        "counties_raw": ["Seneca"],
        "county_primary": "Seneca",
        "ownership_raw": "Ohio Department of Natural Resources (ODNR) — Division of Natural Areas and Preserves (DNAP)",
        "governance_raw": "Ohio Department of Natural Resources (ODNR) — Division of Natural Areas and Preserves (DNAP)",
        "partner_agencies_raw": None,
        "coordination_raw": None,
        "gps_lat_raw": None,
        "gps_lon_raw": None,
        "location_raw": "1655 W Township Rd 38, Tiffin, OH 44883",
        "acres_raw": "114.86",
        "description_raw": "State nature preserve featuring woods, wetlands, and spring wildflowers. Approximately 1.2 miles of trails along the Sandusky River corridor.",
        "features_raw": ["Woods", "Wetlands", "Spring wildflowers", "Trails (1.2 mi)"],
        "difficulty_raw": None,
        "accessibility_raw": None,
        "urls_raw": [],
        "identity_notes_raw": (
            "Baseline also lists 'Collier Scenic River Area (Sandusky River)' as a possible alias. "
            "These appear to be distinct: Howard Collier SNP is a terrestrial preserve managed by DNAP; "
            "Sandusky State Scenic River is a separate ODNR scenic river designation. Resolve during T2 close. "
            "Confirmed via ODNR Nature Preserves Guide PDF."
        ),
        "township_raw": None,
        "municipality_raw": None,
        "discovery_tier": 2,
        "seeded_from_baseline": True,
        "baseline_id": "Howard Collier State Nature Preserve",
    },
    {
        "entity_type": "Site",
        "name_raw": "Springville Marsh State Nature Preserve",
        "counties_raw": ["Seneca"],
        "county_primary": "Seneca",
        "ownership_raw": "Ohio Department of Natural Resources (ODNR) — Division of Natural Areas and Preserves (DNAP)",
        "governance_raw": "Ohio Department of Natural Resources (ODNR) — Division of Natural Areas and Preserves (DNAP)",
        "partner_agencies_raw": None,
        "coordination_raw": None,
        "gps_lat_raw": None,
        "gps_lon_raw": None,
        "location_raw": "12250 Township Rd 24, Carey, OH 43316",
        "acres_raw": "201.37",
        "description_raw": "State nature preserve featuring wetland habitat and 0.8 miles of trail. Bird watching in calcareous fen and wet prairie.",
        "features_raw": ["Wetlands", "Bird watching", "Trail (0.8 mi)"],
        "difficulty_raw": None,
        "accessibility_raw": None,
        "urls_raw": [],
        "identity_notes_raw": (
            "Confirmed via ODNR Nature Preserves Guide PDF. 201.37 acres per baseline. "
            "Address TR 24 / Carey OH aligns with SORP NATURAL RESOURCES agency parcels."
        ),
        "township_raw": None,
        "municipality_raw": None,
        "discovery_tier": 2,
        "seeded_from_baseline": True,
        "baseline_id": "Springville Marsh State Nature Preserve",
    },
    {
        "entity_type": "Site",
        "name_raw": "Sugar Creek Wildlife Area",
        "counties_raw": ["Seneca"],
        "county_primary": "Seneca",
        "ownership_raw": "Ohio Department of Natural Resources (ODNR) — Division of Wildlife",
        "governance_raw": "Ohio Department of Natural Resources (ODNR) — Division of Wildlife",
        "partner_agencies_raw": None,
        "coordination_raw": None,
        "gps_lat_raw": None,
        "gps_lon_raw": None,
        "location_raw": "Township Road 157 and Township Road 148, Seneca County, OH",
        "acres_raw": "125",
        "description_raw": (
            "Public hunting wildlife area with grassland and brushland habitat. "
            "Two parking areas at T-157 and T-148. Approximately 0.5 miles from Knobbys Prairie Wildlife Area."
        ),
        "features_raw": ["Public hunting", "Parking (two lots)", "Grassland", "Brushland"],
        "difficulty_raw": None,
        "accessibility_raw": None,
        "urls_raw": [],
        "identity_notes_raw": "Confirmed via ODNR Sugar Creek & Knobbys Prairie WA PDF. 125 acres.",
        "township_raw": None,
        "municipality_raw": None,
        "discovery_tier": 2,
        "seeded_from_baseline": True,
        "baseline_id": "Sugar Creek Wildlife Area",
    },
    {
        "entity_type": "Site",
        "name_raw": "Knobbys Prairie Wildlife Area",
        "counties_raw": ["Seneca"],
        "county_primary": "Seneca",
        "ownership_raw": "Ohio Department of Natural Resources (ODNR) — Division of Wildlife",
        "governance_raw": "Ohio Department of Natural Resources (ODNR) — Division of Wildlife",
        "partner_agencies_raw": None,
        "coordination_raw": None,
        "gps_lat_raw": None,
        "gps_lon_raw": None,
        "location_raw": "County Road 15 at Township Road 148, Seneca County, OH",
        "acres_raw": "47",
        "description_raw": "Public hunting wildlife area located approximately 0.5 miles from Sugar Creek Wildlife Area.",
        "features_raw": ["Public hunting", "Parking"],
        "difficulty_raw": None,
        "accessibility_raw": None,
        "urls_raw": [],
        "identity_notes_raw": (
            "Confirmed via ODNR Sugar Creek & Knobbys Prairie WA PDF. 47 acres. "
            "ODNR PDF renders as \"Knobby's Prairie\"; baseline renders as \"Knobbys Prairie\" — staging verbatim from ODNR source."
        ),
        "township_raw": None,
        "municipality_raw": None,
        "discovery_tier": 2,
        "seeded_from_baseline": True,
        "baseline_id": "Knobbys Prairie Wildlife Area",
    },
    {
        "entity_type": "Site",
        "name_raw": "Silver Creek Wildlife Area",
        "counties_raw": ["Seneca"],
        "county_primary": "Seneca",
        "ownership_raw": "Ohio Department of Natural Resources (ODNR) — Division of Wildlife",
        "governance_raw": "Ohio Department of Natural Resources (ODNR) — Division of Wildlife",
        "partner_agencies_raw": None,
        "coordination_raw": None,
        "gps_lat_raw": None,
        "gps_lon_raw": None,
        "location_raw": "Township Road 58 at Township Roads 181 / County Road 6, near Bloomville, Seneca County, OH",
        "acres_raw": "42",
        "description_raw": (
            "Public hunting wildlife area near Bloomville. "
            "Features marshland, grassland, and brushland habitat. Near US-19, US-224, and SR-67/100/4."
        ),
        "features_raw": ["Public hunting", "Parking", "Marshland", "Grassland", "Brushland"],
        "difficulty_raw": None,
        "accessibility_raw": None,
        "urls_raw": [],
        "identity_notes_raw": "Confirmed via ODNR Silver Creek WA PDF. 42 acres.",
        "township_raw": None,
        "municipality_raw": None,
        "discovery_tier": 2,
        "seeded_from_baseline": True,
        "baseline_id": "Silver Creek Wildlife Area",
    },
    {
        "entity_type": "Trail",
        "name_raw": "Sandusky State Scenic River",
        "counties_raw": ["Sandusky", "Seneca", "Wyandot"],
        "county_primary": "Seneca",
        "ownership_raw": "Multiple — state-designated scenic river corridor, land ownership varies",
        "governance_raw": "Ohio Department of Natural Resources (ODNR) — Ohio Scenic Rivers Program",
        "partner_agencies_raw": None,
        "coordination_raw": None,
        "gps_lat_raw": None,
        "gps_lon_raw": None,
        "location_raw": "Sandusky River corridor, Wyandot/Seneca/Sandusky counties, OH",
        "description_raw": (
            "65-mile state scenic river designation along the Sandusky River. "
            "Designated 1970. Flows from Wyandot County through Seneca County to Sandusky County."
        ),
        "features_raw": ["Canoeing", "Fishing", "Wildlife viewing"],
        "difficulty_raw": None,
        "accessibility_raw": None,
        "urls_raw": [],
        "identity_notes_raw": (
            "CROSS_COUNTY_CANDIDATE — spans Sandusky/Seneca/Wyandot counties. "
            "Not currently in DB as of 2026-05-25. Designated 1970. 65 miles. Water trail (type TR). "
            "Distinct from baseline seed 'Collier Scenic River Area' which likely refers to a specific "
            "access segment near Howard Collier SNP."
        ),
        "township_raw": None,
        "municipality_raw": None,
        "discovery_tier": 2,
        "seeded_from_baseline": False,
        "baseline_id": None,
    },
]

for r in t2_records:
    data["records"].append(r)

f.write_text(yaml.dump(data, allow_unicode=True, sort_keys=False), encoding="utf-8")
print(f"Staged {len(t2_records)} T2 records. Total records now: {len(data['records'])}")
