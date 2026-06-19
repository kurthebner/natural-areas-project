import yaml, pathlib

f = pathlib.Path(r"D:\users\user1\Documents\CP Projects\Natural Areas Project v5\County_Spreadsheets\Seneca\seneca_ohio_raw_discovery.yaml")
data = yaml.safe_load(f.read_text(encoding="utf-8"))
data.setdefault("tier_nulls", [])

t4_nulls = [
    {
        "tier": 4,
        "governance_level": "Seneca County Commissioners — Direct Parks/Recreation Ownership",
        "entity_type": "All",
        "result": "null",
        "sources_checked": [
            "https://senecacountyohio.gov/departments/",
            "https://www.senecacountyparks.com/about-2",
        ],
        "reasoning": (
            "Seneca County Commissioners do not operate a parks or recreation department. "
            "County departments page lists: Emergency Management, EMS, Dog Warden, Buildings & Grounds, "
            "Youth Center, Job & Family Services, Sewer District, Law Library, Seneca County Museum, "
            "Conservation District, Park District, Health District, Board of Elections, Opportunity Center, "
            "Victim Assistance — no parks or recreation department. "
            "Seneca County Park District (SCPD) is a separate statutory Park/Recreation District entity "
            "(ORC-authorized, independently governed by 5-member board) — staged at Tier 3. "
            "County commissioners authorized formation of SCPD in 1996 but do not own or manage parks directly. "
            "No county commissioner-managed natural areas, parks, or recreation facilities found."
        ),
    },
    {
        "tier": 4,
        "governance_level": "NRHP — Natural Areas, Covered Bridges, Parks (Seneca County)",
        "entity_type": "All",
        "result": "null",
        "sources_checked": [
            "https://en.wikipedia.org/wiki/National_Register_of_Historic_Places_listings_in_Seneca_County,_Ohio",
        ],
        "reasoning": (
            "45 NRHP-listed properties in Seneca County as of August 2025. "
            "Property types include: Heidelberg College campus buildings (private university), "
            "historic districts (Downtown Tiffin, Fort Ball-Railroad, Fostoria Downtown, N Sandusky St, "
            "NE Tiffin, Camp Pittenger), religious properties, industrial/commercial buildings, "
            "farms, and residences. "
            "No covered bridges, natural areas, parks, or publicly accessible outdoor recreation sites found. "
            "No NRHP-listed county-owned natural features in Seneca County."
        ),
    },
    {
        "tier": 4,
        "governance_level": "Seneca County Fairgrounds — Seneca County Agricultural Society",
        "entity_type": "Site",
        "result": "null (T8 candidate)",
        "sources_checked": [
            "https://www.senecacountyfair.com/",
        ],
        "reasoning": (
            "Seneca County Fairgrounds (100 Hopewell Avenue, Tiffin OH 44883) is owned and operated by "
            "the Seneca County Agricultural Society, a nonprofit organization — NOT the county commissioners. "
            "Agricultural Societies in Ohio are nonprofit entities, not county government bodies. "
            "Confirmed null for Tier 4. Flagged as Tier 8 (Private) candidate."
        ),
    },
    {
        "tier": 4,
        "governance_level": "Camp Pittenger Historic District — NWOCYC (private nonprofit)",
        "entity_type": "Site",
        "result": "null (T8 candidate)",
        "sources_checked": [
            "https://nwocyc.org/about/",
            "https://m.yelp.com/biz/pittenger-camp-mc-cutchenville",
        ],
        "reasoning": (
            "Camp Pittenger (8877 S. Township Road 131, McCutchenville, Seneca County) is now operated by "
            "Northwestern Ohio Christian Youth Camp (NWOCYC) as a private Christian youth camp. "
            "Originally Camp Sandusky (Findlay YMCA, 1931), became Camp Pittenger under Tiffin YMCA (1938). "
            "Listed on National Register of Historic Places as Camp Pittenger Historic District (ca. January 2024). "
            "Current ownership: NWOCYC (private religious nonprofit) — NOT county-owned. "
            "Confirmed null for Tier 4. Flagged as Tier 8 candidate (private religious camp)."
        ),
    },
    {
        "tier": 4,
        "governance_level": "Seneca County Museum — county-owned historic house museum",
        "entity_type": "Site",
        "result": "null (non-qualifying)",
        "sources_checked": [
            "https://senecacountyohio.org/",
            "https://www.destinationsenecacounty.org/place/seneca-county-museum/",
        ],
        "reasoning": (
            "Seneca County Museum (Rezin Shawhan house, 1853 Italianate, Tiffin) is county-owned and "
            "operated by the Barnes-Deinzer Seneca County Museum Foundation. "
            "A historic house museum with glass and military collections — no trails, natural areas, "
            "or outdoor recreation component. Confirmed non-qualifying for NAP. Null for Tier 4."
        ),
    },
]

for null in t4_nulls:
    data["tier_nulls"].append(null)

data["current_tier"] = 5

f.write_text(yaml.dump(data, allow_unicode=True, sort_keys=False), encoding="utf-8")
print(f"Added {len(t4_nulls)} T4 null blocks. Total tier_nulls: {len(data['tier_nulls'])}")
print(f"Total records: {len(data['records'])}, current_tier: {data['current_tier']}")
