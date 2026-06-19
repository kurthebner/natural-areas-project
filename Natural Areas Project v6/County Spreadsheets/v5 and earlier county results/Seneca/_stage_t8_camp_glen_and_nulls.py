import yaml, pathlib

f = pathlib.Path(r"D:\users\user1\Documents\CP Projects\Natural Areas Project v5\County_Spreadsheets\Seneca\seneca_ohio_raw_discovery.yaml")
data = yaml.safe_load(f.read_text(encoding="utf-8"))
data.setdefault("records", [])
data.setdefault("tier_nulls", [])

# ============================================================
# TIER 8 — CAMP GLEN (Camp Fire Sandusky County)
# Source: ACA Find-A-Camp, campfiresc.org, Fishbrain (Sandusky River location)
# Confirmed Seneca County: 6580 S Township Road 131, Tiffin, OH 44883
# ============================================================

camp_glen = {
    "entity_type": "Site",
    "name_raw": "Camp Glen",
    "counties_raw": ["Seneca"],
    "county_primary": "Seneca",
    "ownership_raw": "Camp Fire Sandusky County",
    "governance_raw": "Camp Fire Sandusky County (nonprofit, affiliated with Camp Fire USA)",
    "partner_agencies_raw": None,
    "coordination_raw": None,
    "gps_lat_raw": None,
    "gps_lon_raw": None,
    "location_raw": "6580 S Township Road 131, Tiffin, OH 44883",
    "acres_raw": None,
    "description_raw": (
        "Youth camp and retreat center on the banks of the Sandusky River south of Tiffin, with "
        "unusually hilly terrain ideal for hiking and outdoor activities. ACA-accredited facility "
        "offering residential and day camp programs for youth (swimming, fishing, canoeing, archery, "
        "arts and crafts). Facilities also available for rental by outside groups for retreats, "
        "corporate meetings, and youth gatherings. Peaceful riverside setting with natural Sandusky "
        "River corridor. Founded 1959."
    ),
    "features_raw": [
        "Sandusky River frontage",
        "Hilly terrain / hiking",
        "Swimming",
        "Fishing",
        "Canoeing",
        "Archery range",
        "Retreat center with meeting room",
        "Overnight accommodations (cabins)",
        "Fire pit",
        "Arts and crafts",
    ],
    "difficulty_raw": None,
    "accessibility_raw": None,
    "urls_raw": [
        "https://find.acacamps.org/camp_profile.php?camp_id=1870",
        "https://www.campfiresc.org/facility/",
    ],
    "identity_notes_raw": (
        "T8 DISCOVERY — private youth camp and retreat center. "
        "Camp Fire Sandusky County (org. office: 2100 Baker Road, Fremont OH 43420) owns Camp Glen in Seneca County "
        "(address 6580 S TR 131, Tiffin OH 44883; ZIP 44883 confirms Seneca County). "
        "Camp Fire Sandusky County is affiliated with Camp Fire USA (national nonprofit). "
        "Camp is named for and situated on the Sandusky River with hilly, wooded terrain. "
        "Operates residential summer camp programs and rents facilities to outside groups. "
        "ACA (American Camp Association) accredited. Founded 1959. Active as of 2026. "
        "campfiresc.org website confirms 'Camp Glen' as one of two Camp Fire Sandusky County venues "
        "(alongside Misty Meadows). "
        "Note: do NOT confuse with Camp Pittenger/NWOCYC (8877 S TR 131, McCutchenville) — different camp, "
        "different address on the same road corridor."
    ),
    "township_raw": None,
    "municipality_raw": None,
    "discovery_tier": 8,
    "seeded_from_baseline": False,
    "baseline_id": None,
}

data["records"].append(camp_glen)
print(f"Staged Camp Glen. Records now: {len(data['records'])}")

# ============================================================
# TIER 8 — NULL BLOCKS
# Documents all T8 search categories with null or non-qualifying results.
# Sources investigated during T8 discovery phase.
# ============================================================

t8_nulls = [
    {
        "tier": 8,
        "governance_level": "Tiffin Drive-In Theater — private entertainment venue",
        "entity_type": "Site",
        "result": "null — non-qualifying",
        "sources_checked": [
            "Destination Seneca County tourism listings",
        ],
        "reasoning": (
            "Tiffin Drive-In Theater (4101 OH-53, Tiffin OH 44883) is a private drive-in movie theater. "
            "Entertainment/commercial venue — no natural area, trail, or open space component. "
            "Does not meet NAP scope criteria (natural area, park, trail, or open space). "
            "Not staged."
        ),
    },
    {
        "tier": 8,
        "governance_level": "Seneca County Agricultural Society — County Fairgrounds",
        "entity_type": "Site",
        "result": "null — non-qualifying",
        "sources_checked": [
            "Destination Seneca County tourism listings",
            "Ohio Agricultural Society registry",
        ],
        "reasoning": (
            "Seneca County Agricultural Society owns the county fairgrounds at 100 Hopewell Ave, Tiffin OH 44883. "
            "Agricultural Society fairgrounds are classified as commercial/agricultural exhibition facilities "
            "(grandstands, show buildings, midway, livestock barns). "
            "No natural area, nature trail, wildlife habitat, or open space component identified. "
            "Fair grounds do not meet NAP scope criteria. Not staged. "
            "(Agricultural Society = private nonprofit under ORC 1711; T4 ruled null for county commissioner ownership.)"
        ),
    },
    {
        "tier": 8,
        "governance_level": "Mohawk Lake Dam — privately owned lake/reservoir (baseline seed)",
        "entity_type": "Site",
        "result": "null — no confirmed managed park or public natural area",
        "sources_checked": [
            "https://ohio.hometownlocator.com/maps/feature-map,ftc,2,fid,1078432,n,mohawk%20lake.cfm",
            "https://fishbrain.com/fishing-waters/KpbV2VSD/mohawk-lake",
            "GNIS Feature Detail Report (ownership not listed)",
        ],
        "reasoning": (
            "Mohawk Lake (GNIS) is a reservoir in Seneca County at approximately 41.063553, -83.168301, "
            "about 3.8 miles south of Tiffin (ZIP 44883). Mohawk Lake Dam is the impoundment structure. "
            "Fishbrain documents it as a fishing location for bass and crappie. "
            "No confirmed managed park, recreational facility, trail system, or public access point found. "
            "GNIS does not list ownership. Baseline entry 'Mohawk Lake Dam — privately owned park' could not "
            "be verified from any authoritative source. "
            "Treated as private lake/reservoir with informal fishing access — no managed natural area confirmed. "
            "Not staged. If authoritative source confirms managed public park → re-open as T8 Site."
        ),
    },
    {
        "tier": 8,
        "governance_level": "Heidelberg University — private university natural areas (Tiffin)",
        "entity_type": "Site",
        "result": "null — no confirmed publicly accessible natural area separate from T6 city trail",
        "sources_checked": [
            "https://www.heidelberg.edu/about",
            "https://animalsofohio.com/heidelberg-university/",
            "Web search: Heidelberg University Tiffin arboretum natural area 2026",
        ],
        "reasoning": (
            "Heidelberg University (310 E Market St, Tiffin OH 44883) is a private liberal arts university "
            "occupying approximately 110 acres in Tiffin. Campus features arboretum plantings, "
            "river corridor access (Sandusky River tributary), and woodland areas used for biology field studies. "
            "The Rock Creek Trail (T6, City of Tiffin) passes through the Heidelberg campus — that trail is "
            "city-managed and already staged at T6. "
            "No independently managed, publicly accessible natural area (distinct from the T6 trail) was confirmed. "
            "University campus is private; no separately managed preserve, arboretum open to public, or nature "
            "trail beyond the city-managed Rock Creek Trail corridor was identified. "
            "Not staged. If university designates and manages an accessible natural area → re-open as T8."
        ),
    },
    {
        "tier": 8,
        "governance_level": "Seneca Hills Bible Camp and Retreat Center (SHBC)",
        "entity_type": "Site",
        "result": "null — entity is in Pennsylvania, not Seneca County Ohio",
        "sources_checked": [
            "https://www.senecahills.org/location",
            "https://www.paohgives.org/programs-1/seneca-hills-bible-camp-and-retreat-center",
            "https://find.acacamps.org/camp_profile.php?camp_id=2836",
        ],
        "reasoning": (
            "Seneca Hills Bible Camp and Retreat Center is located in Polk, Venango County, Pennsylvania "
            "(northwestern PA), not in Seneca County, Ohio. "
            "The camp name 'Seneca Hills' refers to the Seneca Nation geographic region of northwestern PA/NY. "
            "250 acres, on Sandy Creek, serves PA/OH border region campers. "
            "paohgives.org (Pennsylvania/Ohio Gives) confirms PA registration. "
            "Not in Seneca County, Ohio — confirmed null for NAP purposes."
        ),
    },
    {
        "tier": 8,
        "governance_level": "Cross Oak Camp (Christian youth camp, S TR 131 area)",
        "entity_type": "Site",
        "result": "null — wrong county (Auglaize County, not Seneca County)",
        "sources_checked": [
            "Address verification: 272 Jack Oak Point Rd, St. Marys OH 45885",
            "ZIP code 45885 = St. Marys, Auglaize County, Ohio",
        ],
        "reasoning": (
            "Cross Oak Camp was investigated as a potential Seneca County T8 entity. "
            "Address confirmed as 272 Jack Oak Point Rd, St. Marys OH 45885. "
            "ZIP 45885 = St. Marys, Auglaize County, Ohio — NOT Seneca County. "
            "Web search result erroneously reported this as Seneca County. "
            "Address-confirmed as Auglaize County. Not staged for Seneca County."
        ),
    },
    {
        "tier": 8,
        "governance_level": "Fostoria Country Club (golf course, Independence Ave)",
        "entity_type": "Site",
        "result": "null — wrong county (Hancock County, not Seneca County)",
        "sources_checked": [
            "747 Independence Ave, Fostoria OH 44830",
            "Findlay-Hancock County Chamber of Commerce listing",
            "GolfPass Seneca County listing (incorrect — conflated with Lakeland GC)",
        ],
        "reasoning": (
            "Fostoria Country Club (747 Independence Ave, Fostoria OH 44830) was flagged during golf enumeration "
            "as a possible Seneca County course. "
            "Findlay-Hancock County Chamber of Commerce confirmed it as a Hancock County entity. "
            "GolfPass listing assigned it to Seneca County — confirmed incorrect. "
            "Address 747 Independence Ave is in the Hancock County portion of Fostoria. "
            "Not staged for Seneca County. "
            "(Note: Lakeland Golf Course at 3770 CR 23, Fostoria = confirmed Seneca County, already staged T8.)"
        ),
    },
    {
        "tier": 8,
        "governance_level": "ODNR Licensed Hunting Preserves Registry — Seneca County",
        "entity_type": "All",
        "result": "null",
        "sources_checked": [
            "ODNR Division of Wildlife — licensed hunting preserves registry (web search)",
            "https://wildlife.ohiodnr.gov/",
        ],
        "reasoning": (
            "ODNR Division of Wildlife maintains a registry of licensed hunting preserves in Ohio. "
            "Web search for licensed hunting preserves in Seneca County returned no results. "
            "Hunting activity found at ODNR lands (Howard Collier SNP special deer hunt — already T2) "
            "and SCPD Steyer Nature Preserve (hunting by registration — already T3). "
            "No privately licensed hunting preserves (put-and-take commercial operations) found in Seneca County. "
            "Confirmed null."
        ),
    },
    {
        "tier": 8,
        "governance_level": "Agritourism / Farm Trails — Seneca County Ohio",
        "entity_type": "All",
        "result": "null",
        "sources_checked": [
            "https://agritourismworld.com/directory/ohio/all/",
            "Ohio Department of Agriculture agritourism listings",
            "Web search: agritourism farm trail Seneca County Ohio",
        ],
        "reasoning": (
            "Web search for agritourism operations in Seneca County Ohio yielded no qualifying natural area entities. "
            "Results primarily returned Seneca County New York (Cornell Cooperative Extension Seneca County NY). "
            "Ohio agritourism directories (Agritourism World, Farm Flavor) list no Seneca County OH operations "
            "that qualify as natural areas, parks, trails, or open spaces under NAP scope. "
            "U-pick farms and harvest festivals are commercial operations not meeting NAP criteria. "
            "Confirmed null."
        ),
    },
    {
        "tier": 8,
        "governance_level": "Scout Camps (BSA / GSA) — Seneca County",
        "entity_type": "Site",
        "result": "partial — Camp Glen (Camp Fire) staged; Camp Pleasant Valley (GSNEO) closed/sold",
        "sources_checked": [
            "https://find.acacamps.org/camp_profile.php?camp_id=1870 (Camp Glen / Camp Fire)",
            "https://www.campfiresc.org/facility/ (Camp Fire Sandusky County facility page)",
            "GSNEO camps page: https://www.gsneo.org/en/members/for-girl-scouts/camp-and-outdoors.html",
            "https://www.cleveland19.com/story/14458968/camps-closed-5-of-7-remaining-girl-scout-camps-closing/",
        ],
        "reasoning": (
            "Boy Scouts of America (BSA): Seneca Waterways Council serves Seneca County (Arrowwood District). "
            "No BSA-owned camp property confirmed in Seneca County. "
            "Camp Glen (6580 S TR 131, Tiffin OH 44883) is operated by Camp Fire Sandusky County (Camp Fire USA), "
            "NOT Boy Scouts — staged as T8 Site. "
            "Girl Scouts of North East Ohio (GSNEO): Camp Pleasant Valley (Seneca County) was one of 5 GSNEO camps "
            "announced for closure/sale in 2011. GSNEO currently operates only Camp Ledgewood (Summit Co.) and "
            "Camp Timberlane (Erie Co.). Camp Pleasant Valley is presumed sold and no longer GSNEO-managed. "
            "If Camp Pleasant Valley is confirmed as a still-operating private entity → re-open as T8."
        ),
    },
    {
        "tier": 8,
        "governance_level": "Private Nature Centers / Retreat Centers — Seneca County (general search)",
        "entity_type": "Site",
        "result": "partial — FELC and Camp Glen staged; no others found",
        "sources_checked": [
            "Web search: private nature center retreat center Seneca County Ohio",
            "TrekOhio Seneca County: https://trekohio.com/seneca/",
            "Destination Seneca County: https://www.destinationsenecacounty.org/",
        ],
        "reasoning": (
            "General search for private nature centers, retreat centers, and private preserves in Seneca County. "
            "Franciscan Earth Literacy Center (FELC, 194 St. Francis Ave., Tiffin) — staged at T8 (T7 candidate). "
            "Camp Glen (Camp Fire Sandusky County) — staged at T8. "
            "Camp Pittenger / NWOCYC (8877 S TR 131, McCutchenville) — staged at T8 (T4 null block candidate). "
            "No additional private nature centers, retreat centers, or private preserves with natural area "
            "characteristics identified in Seneca County. "
            "TrekOhio and Destination Seneca County tourism listings cross-checked — all qualifying entities accounted for."
        ),
    },
]

for null in t8_nulls:
    data["tier_nulls"].append(null)

print(f"Added {len(t8_nulls)} T8 null blocks.")
print(f"Total tier_nulls: {len(data['tier_nulls'])}")
print(f"Total records: {len(data['records'])}, current_tier: {data['current_tier']}")

f.write_text(yaml.dump(data, allow_unicode=True, sort_keys=False), encoding="utf-8")
print("YAML written successfully.")
