import yaml, pathlib

f = pathlib.Path(r"D:\users\user1\Documents\CP Projects\Natural Areas Project v5\County_Spreadsheets\Seneca\seneca_ohio_raw_discovery.yaml")
data = yaml.safe_load(f.read_text(encoding="utf-8"))
data.setdefault("records", [])
data.setdefault("tier_nulls", [])

# ============================================================
# TIER 7 — CONSERVANCY & LAND TRUST
# Sub-procedure: na_conservancy_discovery_subproc_v5.6.md
# Sources checked (§4 Known Organizations + additional):
#   BSC land-we-own: https://blackswamp.org/properties/land-we-own/
#   BSC land-we-protect: https://blackswamp.org/land-we-protect/
#   BSC Clary-Boulee confirm: https://www.blackswampconservancy.org/preserves/clary-boulee-mcdonald-preserve
#   TNC Ohio: https://www.nature.org/en-us/about-us/where-we-work/united-states/ohio/places-we-protect/
#   NORTA/Wabash Cannonball: https://www.wabashcannonballtrail.org/trail-access/
#   WCOLC: https://www.wcolc.org/about
#   WRLC: https://wrlandconservancy.org/parks-preserves/
#   Cardinal LC: https://www.cardinallandconservancy.org/about-cardinal/
#   NCOLC: https://www.ncolc.org/what-we-protect
#   ONAPA preserve map: https://www.onapa.org/preserve-map.html
#   Land Trust Alliance: https://landtrustalliance.org/land-trusts/explore/ (403)
#   Land Trust search: web search for Seneca County OH land trusts
#   TrekOhio Seneca: https://trekohio.com/seneca/
#   FELC: https://felctiffin.org/ + https://www.tiffinfranciscans.org/st-francis-campus/franciscan-earth-literacy-center/
#
# RESULT: 0 new T7 entities.
# Late-T3 discovery: Clary Boulee McDonald Preserve (SCPD ownership confirmed;
#   staged as 3 T3 entities via _stage_t3_late_clary_boulee.py)
# T8 candidate identified: Franciscan Earth Literacy Center (private nonprofit)
# ============================================================

t7_nulls = [
    {
        "tier": 7,
        "governance_level": "Black Swamp Conservancy — Land We Own (§4.2)",
        "entity_type": "All",
        "result": "null",
        "sources_checked": [
            "https://blackswamp.org/properties/land-we-own/",
        ],
        "reasoning": (
            "BSC owns 16 nature preserves in northwest Ohio. Full list reviewed: "
            "Bell Woods, Buttonwood Island, Dr. Robert L. Nehls Memorial, "
            "Forder Bridge River Access Site (Forrest Woods), Forrest Woods, "
            "Heron Crest, Howard Island, Little Auglaize Wildlife Reserve, "
            "Pat & Clint Mauk's Prairie, Quinstock Woods, Rotary Riverside, "
            "St. Joseph River Confluence, St. Joseph River Floodplain, "
            "Water's Edge, Webber Woods (confirmed Lucas County, Toledo), "
            "Weisgerber-Pohlman. "
            "BSC website does not list county for each property. Targeted searches for "
            "Heron Crest, Quinstock Woods, Webber Woods confirmed they are in core "
            "Black Swamp counties (Lucas, Wood, Fulton, Defiance, etc.) — not Seneca. "
            "St. Joseph River properties = far northwest Ohio (Williams/Defiance/Fulton). "
            "No Seneca County properties identified in land-we-own portfolio."
        ),
    },
    {
        "tier": 7,
        "governance_level": "Black Swamp Conservancy — Land We Protect / Clary Boulee McDonald Preserve (§4.2)",
        "entity_type": "Site",
        "result": "re-tiered to T3 — ownership transferred to SCPD",
        "sources_checked": [
            "https://blackswamp.org/land-we-protect/",
            "https://www.blackswampconservancy.org/preserves/clary-boulee-mcdonald-preserve",
        ],
        "reasoning": (
            "Clary Boulee McDonald Preserve was the only Seneca County property on BSC land-we-protect list. "
            "Previously deferred to T7 during T3 stage (BSC-owned at time of T3 discovery). "
            "During T7 review, BSC website now states: 'Now owned and managed by the Seneca County Park District.' "
            "SCPD website confirms property is in their portfolio at senecacountyparks.com/places. "
            "Staged as T3 SCPD entities (1 Site + 2 loop Trails) via _stage_t3_late_clary_boulee.py. "
            "No remaining BSC-owned properties in Seneca County found on either land-we-own or land-we-protect pages. "
            "T7 result for BSC in Seneca County: null."
        ),
    },
    {
        "tier": 7,
        "governance_level": "The Nature Conservancy — Ohio (§4.1)",
        "entity_type": "All",
        "result": "null",
        "sources_checked": [
            "https://www.nature.org/en-us/about-us/where-we-work/united-states/ohio/places-we-protect/",
        ],
        "reasoning": (
            "TNC Ohio open preserves reviewed: Great Egret Marsh, Kitty Todd Preserve, "
            "Morgan Swamp, Herrick Fen, Lucia S. Nash, Brown's Lake Bog (Wayne), "
            "Big Darby Headwaters (Logan), Edge of Appalachia (Adams). "
            "None in Seneca County. TNC Ohio has protected ~65,000 acres statewide "
            "but no Seneca County preserves confirmed."
        ),
    },
    {
        "tier": 7,
        "governance_level": "Northwestern Ohio Rails-to-Trails Association (NORTA) — Wabash Cannonball Trail (§4.4)",
        "entity_type": "All",
        "result": "null",
        "sources_checked": [
            "https://www.wabashcannonballtrail.org/trail-access/",
            "https://en.wikipedia.org/wiki/Wabash_Cannonball_Trail",
        ],
        "reasoning": (
            "Wabash Cannonball Trail runs 66 miles through Fulton, Henry, Lucas, and Williams counties only. "
            "Trail does not pass through Seneca County. "
            "North Fork: Maumee to Montpelier. South Fork: Maumee to Liberty Center. "
            "No NORTA-managed trails or sites in Seneca County."
        ),
    },
    {
        "tier": 7,
        "governance_level": "West Central Ohio Land Conservancy (WCOLC)",
        "entity_type": "All",
        "result": "null",
        "sources_checked": [
            "https://www.wcolc.org/about",
        ],
        "reasoning": (
            "WCOLC service area: Allen, Auglaize, Hardin, Mercer, Putnam, Van Wert, and Hancock counties. "
            "Seneca County is NOT in WCOLC service area. Confirmed null."
        ),
    },
    {
        "tier": 7,
        "governance_level": "Western Reserve Land Conservancy (WRLC)",
        "entity_type": "All",
        "result": "null",
        "sources_checked": [
            "https://wrlandconservancy.org/parks-preserves/",
            "https://landtrustalliance.org/land-trusts/explore/western-reserve-land-conservancy-oh",
        ],
        "reasoning": (
            "WRLC operates in Seneca County (among 29 Ohio counties) and holds 6,200 acres owned + "
            "57,443 acres under conservation easement statewide. "
            "No publicly accessible WRLC-owned preserves identified specifically in Seneca County. "
            "WRLC publicly accessible parks/preserves confirmed in Geauga, Ashtabula, Lorain, Trumbull, "
            "Richland, and Erie counties — none in Seneca. "
            "WRLC parks-preserves page does not list properties by county — 247 parks/preserves across "
            "29 counties total but no Seneca-specific public preserves surfaced in targeted searches. "
            "WRLC's Seneca County activity appears to be primarily conservation easements on private farmland, "
            "not publicly accessible nature preserves."
        ),
    },
    {
        "tier": 7,
        "governance_level": "Cardinal Land Conservancy",
        "entity_type": "All",
        "result": "null",
        "sources_checked": [
            "https://www.cardinallandconservancy.org/about-cardinal/",
        ],
        "reasoning": (
            "Cardinal Land Conservancy serves southwest Ohio (Adams, Brown, Clermont, Clinton, Hamilton, "
            "Highland, Warren) and 11 southeast Indiana counties. "
            "Seneca County is NOT in service area. Confirmed null."
        ),
    },
    {
        "tier": 7,
        "governance_level": "North Central Ohio Land Conservancy (NCOLC)",
        "entity_type": "All",
        "result": "null",
        "sources_checked": [
            "https://www.ncolc.org/what-we-protect",
        ],
        "reasoning": (
            "NCOLC is based in Mansfield and focuses on Richland County and surrounding north-central Ohio. "
            "12 properties listed: Hammon Woods, Gregory Woods, Tugend Prairie, Hemlock Falls, "
            "Cole Road Prairie, Hartman Woods, Swadner Woods, Marguerite Smith Woods, Gorman Nature Center, "
            "Audubon Wetlands, Blue Heron Reserve, White Star Park. "
            "None in Seneca County. Seneca County not mentioned in NCOLC service area description."
        ),
    },
    {
        "tier": 7,
        "governance_level": "ONAPA Preserve Map — Seneca County",
        "entity_type": "All",
        "result": "null (T2 entity identified; no new T7)",
        "sources_checked": [
            "https://www.onapa.org/preserve-map.html",
            "https://birdinghotspots.org/hotspot/L333745",
        ],
        "reasoning": (
            "ONAPA preserve map reviewed (interactive map; text search supplemented). "
            "ONAPA is an advocacy/stewardship organization — they do not own land. "
            "Seneca County preserves identified: Springville Marsh State Nature Preserve "
            "(201 acres, ODNR, Township Rd 24, Carey OH 43316 — Seneca County despite Carey mailing address). "
            "Springville Marsh already staged at T2 (discovery_tier=2, seeded_from_baseline=true). "
            "Howard Collier State Nature Preserve also T2 (previously staged). "
            "No T7 entities identified via ONAPA check."
        ),
    },
    {
        "tier": 7,
        "governance_level": "Franciscan Earth Literacy Center (FELC) — Sisters of St. Francis, Tiffin",
        "entity_type": "Site",
        "result": "null (T8 candidate — private religious nonprofit)",
        "sources_checked": [
            "https://felctiffin.org/",
            "https://www.tiffinfranciscans.org/st-francis-campus/franciscan-earth-literacy-center/",
            "https://www.yelp.com/biz/franciscan-earth-literacy-center-tiffin",
        ],
        "reasoning": (
            "Franciscan Earth Literacy Center (194 St. Francis Ave., Tiffin OH 44883) is a ministry of "
            "the Sisters of St. Francis of Tiffin (private Roman Catholic religious order). "
            "FELC is an environmental education center with woodland trails, community gardens, "
            "outdoor classrooms, Peaceable Kingdom, Seeds of Hope Farm, Straw Bale House. "
            "Serves ~4,500 children and adults per year through school field trips, scouts, summer camps. "
            "Governance: FELC Board of Directors / Sisters of St. Francis (private religious nonprofit). "
            "Not a conservancy or land trust — T7 entity type does not apply. "
            "Flagged as T8 candidate: private religious/nonprofit nature education center with trails."
        ),
    },
    {
        "tier": 7,
        "governance_level": "Land Trust Alliance / Coalition of Ohio Land Trusts — Seneca County",
        "entity_type": "All",
        "result": "null",
        "sources_checked": [
            "https://landtrustalliance.org/land-trusts/explore/ (403 Forbidden)",
            "http://www.ohiolandtrusts.org/find-a-land-trust/ (redirected to LTA)",
            "Web search: 'Seneca County Ohio land trust conservancy nature preserve'",
        ],
        "reasoning": (
            "Land Trust Alliance and Coalition of Ohio Land Trusts directories reviewed via search "
            "(direct access blocked). Land trusts operating in or near Seneca County identified: "
            "Black Swamp Conservancy (checked — null), WRLC (checked — null for public access), "
            "WCOLC (Seneca not in service area), Cardinal LC (southwest Ohio), NCOLC (Richland focus). "
            "No additional Seneca County-specific land trusts identified. "
            "Comprehensive T7 coverage achieved — no new entities."
        ),
    },
]

for null in t7_nulls:
    data["tier_nulls"].append(null)

data["current_tier"] = 8

f.write_text(yaml.dump(data, allow_unicode=True, sort_keys=False), encoding="utf-8")
print(f"Added {len(t7_nulls)} T7 null blocks. Total tier_nulls: {len(data['tier_nulls'])}")
print(f"Total records: {len(data['records'])}, current_tier: {data['current_tier']}")
