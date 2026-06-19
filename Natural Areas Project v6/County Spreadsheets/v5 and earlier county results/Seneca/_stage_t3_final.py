import yaml, pathlib

f = pathlib.Path(r"D:\users\user1\Documents\CP Projects\Natural Areas Project v5\County_Spreadsheets\Seneca\seneca_ohio_raw_discovery.yaml")
data = yaml.safe_load(f.read_text(encoding="utf-8"))
data.setdefault("records", [])
data.setdefault("tier_nulls", [])

# H.P. Eells Park — Bettsville Recreation Board / possibly Village of Bettsville
hp_eells = {
    "entity_type": "Site",
    "name_raw": "H.P. Eells Park",
    "counties_raw": ["Seneca"],
    "county_primary": "Seneca",
    "ownership_raw": "Village of Bettsville (probable — formerly Bettsville Recreation Board)",
    "governance_raw": "Bettsville Recreation Board (possibly dissolved 2009) OR Village of Bettsville",
    "partner_agencies_raw": None,
    "coordination_raw": None,
    "gps_lat_raw": None,
    "gps_lon_raw": None,
    "location_raw": "7461 N. TR. 70, Bettsville area, Seneca County, OH (address listed as Tiffin 44883)",
    "acres_raw": None,
    "description_raw": (
        "Municipal recreational park located next to the quarry in Bettsville. "
        "Features include parking, picnic and play areas, baseball fields, tennis court, and volleyball court."
    ),
    "features_raw": ["Parking", "Picnic area", "Playground", "Baseball fields", "Tennis court", "Volleyball court"],
    "difficulty_raw": None,
    "accessibility_raw": None,
    "urls_raw": [
        "https://villageofbettsville.com/departments/park/",
        "https://www.destinationsenecacounty.org/place/bettsvilles-h-p-eells-park/",
    ],
    "identity_notes_raw": (
        "GOVERNANCE UNCERTAIN: Ohio Auditor lists Bettsville Recreation Board as a Park/Recreation District "
        "with last audit covering 01/01/2008-04/30/2009 (released 04/08/2010). No audits since 2010 strongly "
        "suggests the Recreation Board was dissolved and park management transferred to Village of Bettsville. "
        "Village of Bettsville has a Parks Department but website has minimal content. "
        "If Recreation Board dissolved → entity re-tiers to Tier 6 (Village of Bettsville). "
        "Flag for human verification of governance status."
    ),
    "township_raw": None,
    "municipality_raw": None,
    "discovery_tier": 3,
    "seeded_from_baseline": False,
    "baseline_id": None,
}
data["records"].append(hp_eells)

# T3 null blocks
t3_nulls = [
    {
        "tier": 3,
        "governance_level": "Bettsville Recreation Board (Park/Recreation District — possibly dissolved)",
        "entity_type": "Site",
        "result": "1 entity found (H.P. Eells Park) — governance uncertain",
        "sources_checked": [
            "https://ohioauditor.gov/AuditSearch/Search.aspx (Park/Recreation District, Seneca County)",
            "https://villageofbettsville.com/departments/park/",
            "https://www.destinationsenecacounty.org/place/bettsvilles-h-p-eells-park/",
        ],
        "reasoning": (
            "Ohio Auditor confirms Bettsville Recreation Board as a Park/Recreation District, last audit "
            "covering period 01/01/2008-04/30/2009. No audits since 2010 — likely dissolved around 2009. "
            "H.P. Eells Park is the associated park (7461 N. TR. 70, Bettsville area). "
            "Staged as Tier 3 with governance uncertainty flag. If board dissolved, "
            "H.P. Eells Park re-tiers to Tier 6 (Village of Bettsville)."
        ),
    },
    {
        "tier": 3,
        "governance_level": "Seneca County Soil and Water Conservation District (SWCD)",
        "entity_type": "All",
        "result": "null",
        "sources_checked": [
            "https://ohioauditor.gov/AuditSearch/Search.aspx (SWCD, Seneca County)",
            "https://conservesenecacounty.com/ (403 Forbidden)",
            "https://www.habitatcan.org/local-resources/Seneca-Soil-and-Water-Conservation-District/5306/",
        ],
        "reasoning": (
            "Seneca County SWCD is active (Ohio Auditor last audit FY 2022-2023). "
            "SWCD website returned 403. No publicly accessible nature areas, demonstration forests, "
            "or conservation lands found for the Seneca County SWCD via web search. "
            "SWCDs in Ohio typically provide technical assistance and education rather than owning "
            "public recreational land. Confirmed null — no NAP entities."
        ),
    },
    {
        "tier": 3,
        "governance_level": "Seneca County Regional Planning Commission",
        "entity_type": "All",
        "result": "null",
        "sources_checked": [
            "https://ohioauditor.gov/AuditSearch/Search.aspx (Regional Planning, Seneca County)",
            "https://www.senecarpc.org/ (redirects to County Auditor — website dissolved)",
        ],
        "reasoning": (
            "Seneca County RPC is active per Ohio Auditor (last audit FY 2022-2023). "
            "RPC website (senecarpc.org) now redirects to Seneca County Auditor — website appears inactive. "
            "RPC has an Active Transportation Plan for planning purposes but does not own or manage "
            "trails, natural areas, or parks. Regional Planning Commissions in Ohio are planning bodies "
            "without land management authority. Confirmed null — no NAP entities."
        ),
    },
    {
        "tier": 3,
        "governance_level": "Clary Boulee McDonald Preserve (Black Swamp Conservancy — deferred to Tier 7)",
        "entity_type": "Site",
        "result": "deferred_to_tier_7",
        "sources_checked": [
            "https://www.senecacountyparks.com/places/clary-boulee-mcdonald-preserve",
        ],
        "reasoning": (
            "Clary Boulee McDonald Preserve (5090 W. Township Road 36 / 4747 W. SR 12, Kansas, OH 44841) "
            "is currently owned by the Black Swamp Conservancy and enrolled in H2Ohio Grant program "
            "for water quality improvements. After improvements complete, slated to transfer to SCPD. "
            "Current governance: Black Swamp Conservancy (nonprofit) → Tier 7. "
            "Will be staged during Tier 7 discovery. Location: ~1.4 miles SW of Bettsville."
        ),
    },
    {
        "tier": 3,
        "governance_level": "Conservancy Districts (Seneca County)",
        "entity_type": "All",
        "result": "null",
        "sources_checked": [
            "https://ohioauditor.gov/AuditSearch/Search.aspx (Conservancy District, Seneca County)",
        ],
        "reasoning": "Ohio Auditor search: 0 Conservancy District entities in Seneca County.",
    },
    {
        "tier": 3,
        "governance_level": "Water/Sewer/Sanitary Districts (Seneca County)",
        "entity_type": "All",
        "result": "null",
        "sources_checked": [
            "https://ohioauditor.gov/AuditSearch/Search.aspx (Water/Sewer/Sanitary District, Seneca County)",
        ],
        "reasoning": "Ohio Auditor search: 0 Water/Sewer/Sanitary District entities in Seneca County.",
    },
]

for null in t3_nulls:
    data["tier_nulls"].append(null)

data["current_tier"] = 4

f.write_text(yaml.dump(data, allow_unicode=True, sort_keys=False), encoding="utf-8")
print(f"Staged 1 T3 site (H.P. Eells) + {len(t3_nulls)} T3 null blocks.")
print(f"Total records: {len(data['records'])}, Total tier_nulls: {len(data['tier_nulls'])}")
