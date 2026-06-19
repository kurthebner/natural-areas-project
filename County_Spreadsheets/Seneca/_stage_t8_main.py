import yaml, pathlib

f = pathlib.Path(r"D:\users\user1\Documents\CP Projects\Natural Areas Project v5\County_Spreadsheets\Seneca\seneca_ohio_raw_discovery.yaml")
data = yaml.safe_load(f.read_text(encoding="utf-8"))
data.setdefault("records", [])

# ============================================================
# TIER 8 — PRIVATE (MAIN ENTITIES)
# Sub-procedure: na_private_discovery_subproc_v5.7.md (on disk as v5.3)
# Sources:
#   Golf: countyoffice.org/oh-seneca-county-golf-course/, PGA.com, GolfPass, GolfNow,
#         clintonheightsgolf.com, mohawkgolf.com, loudonmeadowsgolfclub.teesnap.net
#   Seneca Caverns: senecacavernsohio.com
#   NWOCYC: nwocyc.org
#   FELC: felctiffin.org, tiffinfranciscans.org
#   Greenlawn: greenlawncemeterytiffin.org
#   Fairmont: buzzfile.com/business/Fairmont-Cemetery-Association
#   Seneca Memory Gardens: everloved.com/cemeteries/OH/tiffin/seneca-memory-gardens-tiffin-oh-44883/
# ============================================================

# ── GOLF COURSES ──────────────────────────────────────────

clinton_heights = {
    "entity_type": "Site",
    "name_raw": "Clinton Heights Golf Course",
    "counties_raw": ["Seneca"],
    "county_primary": "Seneca",
    "ownership_raw": "Private (owner unconfirmed)",
    "governance_raw": "Private for-profit golf course",
    "partner_agencies_raw": None,
    "coordination_raw": None,
    "gps_lat_raw": None,
    "gps_lon_raw": None,
    "location_raw": "2760 E Township Road 122, Tiffin, OH 44883",
    "acres_raw": None,
    "description_raw": (
        "Public-access 18-hole golf course in Tiffin, Ohio. Built in 1957. "
        "Measures 5,643 yards from the longest tees; par 70. "
        "Season: March 15 – November 30."
    ),
    "features_raw": ["18-hole golf course", "Golf (par 70, 5,643 yards)", "Public tee times"],
    "difficulty_raw": None,
    "accessibility_raw": None,
    "urls_raw": [
        "https://clintonheightsgolf.com/",
        "https://www.golfnow.com/courses/1034823-clinton-heights-details",
    ],
    "identity_notes_raw": (
        "IMP-110: Golf course — all types in scope. Public access, open tee times. "
        "Built 1957; 18 holes, par 70, 5,643 yards. Seasonal: March 15–November 30. "
        "Status: Active."
    ),
    "township_raw": None,
    "municipality_raw": None,
    "discovery_tier": 8,
    "seeded_from_baseline": False,
    "baseline_id": None,
}

lakeland_golf = {
    "entity_type": "Site",
    "name_raw": "Lakeland Golf Course",
    "counties_raw": ["Seneca"],
    "county_primary": "Seneca",
    "ownership_raw": "Private (owner unconfirmed)",
    "governance_raw": "Private for-profit golf course",
    "partner_agencies_raw": None,
    "coordination_raw": None,
    "gps_lat_raw": None,
    "gps_lon_raw": None,
    "location_raw": "3770 County Road 23, Fostoria, OH 44830",
    "acres_raw": None,
    "description_raw": (
        "Public-access 18-hole golf course in Fostoria (Seneca County portion). "
        "Measures 5,485 yards; par 70. Two sets of tees."
    ),
    "features_raw": ["18-hole golf course", "Golf (par 70, 5,485 yards)", "Public tee times"],
    "difficulty_raw": None,
    "accessibility_raw": None,
    "urls_raw": [
        "https://www.pga.com/play/oh/fostoria/lakeland-golf-course/0456210",
        "https://www.destinationsenecacounty.org/place/lakeland-golf-course/",
        "https://www.golflink.com/golf-courses/oh/fostoria/lakeland-golf-course",
    ],
    "identity_notes_raw": (
        "IMP-110: Golf course — all types in scope. Public access. 18 holes, par 70, 5,485 yards. "
        "Confirmed in Seneca County by Destination Seneca County listing. "
        "Address CR 23 (County Road 23, Seneca County portion of Fostoria area). "
        "PGA.com confirmed listing. Status: Active."
    ),
    "township_raw": None,
    "municipality_raw": None,
    "discovery_tier": 8,
    "seeded_from_baseline": False,
    "baseline_id": None,
}

loudon_meadows = {
    "entity_type": "Site",
    "name_raw": "Loudon Meadows Golf Club",
    "counties_raw": ["Seneca"],
    "county_primary": "Seneca",
    "ownership_raw": "Private (owner unconfirmed)",
    "governance_raw": "Private members-only golf club",
    "partner_agencies_raw": None,
    "coordination_raw": None,
    "gps_lat_raw": None,
    "gps_lon_raw": None,
    "location_raw": "11072 W State Route 18, Fostoria, OH 44830",
    "acres_raw": None,
    "description_raw": (
        "Private members-only golf club on W State Route 18 west of Fostoria, in Loudon Township. "
        "18-hole course; par 71; 6,144 yards. Built 1962. Bent grass greens and fairways."
    ),
    "features_raw": ["18-hole golf course", "Golf (par 71, 6,144 yards)", "Members-only club"],
    "difficulty_raw": None,
    "accessibility_raw": None,
    "urls_raw": [
        "https://loudonmeadowsgolfclub.teesnap.net/",
        "https://www.pga.com/play/oh/fostoria/loudon-meadows-golf-course/0496890",
        "https://www.ohiogolf.org/clubs/loudon-meadows-golf-club-fostoria-oh",
    ],
    "identity_notes_raw": (
        "IMP-110: Golf course — all types in scope regardless of access model. "
        "Members-only facility — no public tee times. "
        "18 holes, par 71, 6,144 yards. Built 1962. Bent grass greens. "
        "Located in Loudon Township (Seneca County), W SR 18 west of Fostoria city limits. "
        "PGA.com confirmed listing. Status: Active."
    ),
    "township_raw": None,
    "municipality_raw": None,
    "discovery_tier": 8,
    "seeded_from_baseline": True,
    "baseline_id": None,
}

mohawk_golf = {
    "entity_type": "Site",
    "name_raw": "Mohawk Golf & Country Club",
    "counties_raw": ["Seneca"],
    "county_primary": "Seneca",
    "ownership_raw": "Private (owner unconfirmed — member-owned country club probable)",
    "governance_raw": "Private country club",
    "partner_agencies_raw": None,
    "coordination_raw": None,
    "gps_lat_raw": None,
    "gps_lon_raw": None,
    "location_raw": "4399 S State Route 231, Tiffin, OH 44883",
    "acres_raw": None,
    "description_raw": (
        "18-hole private country club and the only private country club in the Tiffin area. "
        "Original nine holes designed by world-renowned architect Donald Ross. "
        "Known for fast, smooth greens and a bi-directional driving range."
    ),
    "features_raw": [
        "18-hole golf course",
        "Golf (Donald Ross design, original 9 holes)",
        "Driving range (bi-directional)",
        "Putting green",
        "Chipping area",
        "Private club facilities",
    ],
    "difficulty_raw": None,
    "accessibility_raw": None,
    "urls_raw": [
        "https://www.mohawkgolf.com/",
        "https://www.mohawkgolf.com/course-details/",
        "https://www.destinationsenecacounty.org/place/mohawk-golf-and-country-club/",
    ],
    "identity_notes_raw": (
        "IMP-110: Golf course — all types in scope regardless of access model. "
        "Only private country club in Tiffin area. 18-hole course, Donald Ross design (original 9). "
        "Members-only; no public tee times. Status: Active."
    ),
    "township_raw": None,
    "municipality_raw": None,
    "discovery_tier": 8,
    "seeded_from_baseline": False,
    "baseline_id": None,
}

seneca_hills_golf = {
    "entity_type": "Site",
    "name_raw": "Seneca Hills Golf Course",
    "counties_raw": ["Seneca"],
    "county_primary": "Seneca",
    "ownership_raw": "Private (owner unconfirmed)",
    "governance_raw": "Private golf course (status: possibly closed)",
    "partner_agencies_raw": None,
    "coordination_raw": None,
    "gps_lat_raw": None,
    "gps_lon_raw": None,
    "location_raw": "4044 W Township Road 98, Tiffin, OH 44883",
    "acres_raw": None,
    "description_raw": None,
    "features_raw": ["18-hole golf course"],
    "difficulty_raw": None,
    "accessibility_raw": None,
    "urls_raw": [
        "https://www.golfdigest.com/courses/oh/seneca-hills-golf-club-seneca-hills",
        "https://www.golfnow.com/courses/1035182-seneca-hills-golf-course-details",
    ],
    "identity_notes_raw": (
        "IMP-110: Golf course — all types in scope regardless of access model; closed courses staged with status: Closed. "
        "Golf Digest lists as 'Closed.' GolfNow/GolfPass still show course listing — conflicting. "
        "Staged as status: Closed per Golf Digest (treated as golf-specific authoritative source). "
        "If confirmed open, update status to Active and identity_notes_raw accordingly."
    ),
    "township_raw": None,
    "municipality_raw": None,
    "discovery_tier": 8,
    "seeded_from_baseline": False,
    "baseline_id": None,
}

# ── RECREATION / NATURE SITES ─────────────────────────────

seneca_caverns = {
    "entity_type": "Site",
    "name_raw": "Seneca Caverns",
    "counties_raw": ["Seneca"],
    "county_primary": "Seneca",
    "ownership_raw": "Private (owner unconfirmed)",
    "governance_raw": "Private for-profit tourist attraction",
    "partner_agencies_raw": "ODNR (Registered Natural Landmark designation)",
    "coordination_raw": None,
    "gps_lat_raw": None,
    "gps_lon_raw": None,
    "location_raw": "15248 E Township Road 178, Bellevue, OH 44811 (northeastern Seneca County, ~3 miles south of Bellevue)",
    "acres_raw": None,
    "description_raw": (
        "Natural limestone show cave in northeastern Seneca County, Ohio. Discovered 1872, open as "
        "tourist attraction since 1933. Features guided one-hour tours descending to the 'Ole Mist'ry River' "
        "(crystal-clear underground stream), natural stone steps, narrow passages, and low ceilings. "
        "Contains a rare 'Earth Crack' geological formation. Designated an ODNR Registered Natural Landmark. "
        "Operating hours: May weekends; Memorial Day–Labor Day daily; Fall weekends; closed November–April."
    ),
    "features_raw": [
        "Show cave (guided tours)",
        "Underground stream (Ole Mist'ry River)",
        "Earth Crack geological formation",
        "ODNR Registered Natural Landmark",
        "Seasonal operation",
    ],
    "difficulty_raw": None,
    "accessibility_raw": "Natural stone steps and narrow passages — limited accessibility",
    "urls_raw": [
        "https://senecacavernsohio.com/",
        "https://www.destinationsenecacounty.org/blog/secrets-of-seneca-county-historical-driving-tour-seneca-caverns/",
    ],
    "identity_notes_raw": (
        "Private tourist attraction in northeastern Seneca County, just outside Flat Rock. "
        "ODNR Registered Natural Landmark. Address uses Bellevue mailing area but confirmed Seneca County location. "
        "Yelp (March 2026) showed 'TEMP. CLOSED' — consistent with winter seasonal closure; "
        "official website shows 2026 May opening (seasonal). Staged as Active (seasonal operation). "
        "Address 15248 E TR 178, Bellevue OH 44811 confirmed Seneca County by multiple sources."
    ),
    "township_raw": None,
    "municipality_raw": None,
    "discovery_tier": 8,
    "seeded_from_baseline": True,
    "baseline_id": "Seneca Caverns",
}

camp_pittenger = {
    "entity_type": "Site",
    "name_raw": "Camp Pittenger (NWOCYC)",
    "counties_raw": ["Seneca"],
    "county_primary": "Seneca",
    "ownership_raw": "Northwestern Ohio Christian Youth Camp (NWOCYC)",
    "governance_raw": "Northwestern Ohio Christian Youth Camp, Inc. (NWOCYC) — private religious nonprofit",
    "partner_agencies_raw": None,
    "coordination_raw": None,
    "gps_lat_raw": None,
    "gps_lon_raw": None,
    "location_raw": "8877 S Township Road 131, McCutchenville, OH 44844",
    "acres_raw": None,
    "description_raw": (
        "Historic Christian youth camp on the Sandusky River in McCutchenville, Seneca County. "
        "Features woodland with magnificent beech trees, a gorge, Sandusky River frontage, "
        "outdoor amphitheatre in the woods, and cabin accommodations. "
        "Originally Camp Sandusky (Findlay YMCA, 1931), then Camp Pittenger under Tiffin YMCA (1938); "
        "board purchased site in 1979 and formed NWOCYC. "
        "Listed on National Register of Historic Places as Camp Pittenger Historic District. "
        "Programs: summer youth camps (All Ages Weeks, Teen Week, Camp of Champs), Wellness Weekend, "
        "Spring Rally 5K, weekend retreats. Hiking to Howard Collier State Nature Preserve nearby."
    ),
    "features_raw": [
        "Woodland (beech trees)",
        "Gorge",
        "Sandusky River frontage",
        "Outdoor amphitheatre",
        "Cabin accommodations",
        "Fire circle",
        "NRHP-listed district (Camp Pittenger Historic District)",
        "Proximity to Howard Collier State Nature Preserve",
    ],
    "difficulty_raw": None,
    "accessibility_raw": None,
    "urls_raw": [
        "https://nwocyc.org/",
        "https://nwocyc.org/about/",
    ],
    "identity_notes_raw": (
        "Private Christian youth camp (NWOCYC). Limited public access — primarily organized youth groups and "
        "retreat participants; has opened for special events (e.g., 2024 solar eclipse weekend). "
        "NRHP-listed as Camp Pittenger Historic District (ca. January 2024). "
        "Acreage not confirmed from web sources. "
        "Originally 40 acres at Tiffin YMCA acquisition (1969 purchase); current McCutchenville property acreage TBD. "
        "Camp Pittenger T8 candidate confirmed from T4 null block."
    ),
    "township_raw": None,
    "municipality_raw": None,
    "discovery_tier": 8,
    "seeded_from_baseline": False,
    "baseline_id": None,
}

felc = {
    "entity_type": "Site",
    "name_raw": "Franciscan Earth Literacy Center",
    "counties_raw": ["Seneca"],
    "county_primary": "Seneca",
    "ownership_raw": "Sisters of St. Francis of Tiffin (or FELC Board of Directors)",
    "governance_raw": "Franciscan Earth Literacy Center (private religious nonprofit) — ministry of Sisters of St. Francis",
    "partner_agencies_raw": None,
    "coordination_raw": None,
    "gps_lat_raw": None,
    "gps_lon_raw": None,
    "location_raw": "194 St. Francis Ave., Tiffin, OH 44883",
    "acres_raw": None,
    "description_raw": (
        "Environmental education center and demonstration facility on the Sisters of St. Francis campus "
        "in Tiffin, OH. Promotes appreciation of nature and sustainable living. "
        "Features community gardens (Seeds of Hope Farm), solar PV array, Straw Bale House, "
        "Peaceable Kingdom, outdoor classrooms, and woodland trails. "
        "Programs include school field trips (~4,500 visitors/year), scout groups, summer camps, "
        "Wildflower Walks, and adult environmental education workshops."
    ),
    "features_raw": [
        "Woodland trails",
        "Community gardens (Seeds of Hope Farm)",
        "Outdoor classrooms",
        "Straw Bale House",
        "Solar PV demonstration array",
        "Worm bin / composting demonstration",
        "Peaceable Kingdom area",
        "Farm stand",
    ],
    "difficulty_raw": None,
    "accessibility_raw": None,
    "urls_raw": [
        "https://felctiffin.org/",
        "https://www.tiffinfranciscans.org/st-francis-campus/franciscan-earth-literacy-center/",
        "https://www.destinationsenecacounty.org/place/franciscan-earth-literacy-center/",
    ],
    "identity_notes_raw": (
        "Private religious nonprofit environmental education center. "
        "T7 null block candidate confirmed as T8 (Sisters of St. Francis — religious order, not land trust). "
        "FELC serves ~4,500 children and adults per year primarily through organized programs (field trips, camps, "
        "retreats). General public trail access not explicitly stated on website — access appears program-based. "
        "Acreage not confirmed from web sources."
    ),
    "township_raw": None,
    "municipality_raw": None,
    "discovery_tier": 8,
    "seeded_from_baseline": False,
    "baseline_id": None,
}

# ── PRIVATE CEMETERIES (independent associations) ─────────

greenlawn_cem = {
    "entity_type": "Site",
    "name_raw": "Greenlawn Cemetery",
    "counties_raw": ["Seneca"],
    "county_primary": "Seneca",
    "ownership_raw": "Greenlawn Cemetery Association",
    "governance_raw": "Greenlawn Cemetery Association (501(c)(13) nonprofit cemetery corporation)",
    "partner_agencies_raw": None,
    "coordination_raw": None,
    "gps_lat_raw": None,
    "gps_lon_raw": None,
    "location_raw": "914 E County Road 36 (Coe Road), Tiffin, OH 44883 (also listed as 895 E CR 36)",
    "acres_raw": None,
    "description_raw": (
        "Large nonprofit cemetery in Tiffin, operated by the Greenlawn Cemetery Association since 1874. "
        "Has many acres yet to be developed. Well-maintained grounds. "
        "Known birding hotspot on BirdingHotspots.org."
    ),
    "features_raw": ["Cemetery (private association)", "Birding area"],
    "difficulty_raw": None,
    "accessibility_raw": None,
    "urls_raw": [
        "https://www.greenlawncemeterytiffin.org/",
    ],
    "identity_notes_raw": (
        "Greenlawn Cemetery Association (501(c)(13)) — independent nonprofit cemetery corporation, "
        "formed January 23, 1874. NOT city-owned. "
        "T6 null block: 'Greenlawn = private 501(c)(13); no city cemetery.' "
        "Address discrepancy: official website says 914 E CR 36; other sources say 895 E CR 36. "
        "Confirmed T8 Private Cemetery. Hours: Mon–Fri 7am–5pm, Sat 8am–5pm. "
        "Phone: 419-447-2010."
    ),
    "township_raw": None,
    "municipality_raw": None,
    "discovery_tier": 8,
    "seeded_from_baseline": False,
    "baseline_id": None,
}

fairmont_cem = {
    "entity_type": "Site",
    "name_raw": "Fairmont Cemetery",
    "counties_raw": ["Seneca"],
    "county_primary": "Seneca",
    "ownership_raw": "Fairmont Cemetery Association",
    "governance_raw": "Fairmont Cemetery Association (independent nonprofit cemetery corporation)",
    "partner_agencies_raw": None,
    "coordination_raw": None,
    "gps_lat_raw": None,
    "gps_lon_raw": None,
    "location_raw": "1855 W Township Road 132, Tiffin, OH 44883 (Clinton Township)",
    "acres_raw": None,
    "description_raw": None,
    "features_raw": ["Cemetery (private association)"],
    "difficulty_raw": None,
    "accessibility_raw": None,
    "urls_raw": [
        "https://www.findagrave.com/cemetery/40779/fairmont-cemetery",
    ],
    "identity_notes_raw": (
        "Fairmont Cemetery Association — independent nonprofit cemetery organization. "
        "Located in Clinton Township, Seneca County. "
        "Phone: 419-447-1740. "
        "T8 Private Cemetery."
    ),
    "township_raw": None,
    "municipality_raw": None,
    "discovery_tier": 8,
    "seeded_from_baseline": False,
    "baseline_id": None,
}

seneca_memory_gardens = {
    "entity_type": "Site",
    "name_raw": "Seneca Memory Gardens",
    "counties_raw": ["Seneca"],
    "county_primary": "Seneca",
    "ownership_raw": "Private partnership (Jeff Roberts, CFO)",
    "governance_raw": "Private for-profit cemetery (partnership)",
    "partner_agencies_raw": None,
    "coordination_raw": None,
    "gps_lat_raw": None,
    "gps_lon_raw": None,
    "location_raw": "4565 US Route 224, Tiffin, OH 44883",
    "acres_raw": None,
    "description_raw": None,
    "features_raw": ["Cemetery (private memorial garden)"],
    "difficulty_raw": None,
    "accessibility_raw": None,
    "urls_raw": [
        "https://everloved.com/cemeteries/OH/tiffin/seneca-memory-gardens-tiffin-oh-44883/",
        "https://www.bbb.org/us/oh/tiffin/profile/cemetery/seneca-memory-gardens-0422-27000064",
    ],
    "identity_notes_raw": (
        "Private for-profit memorial garden cemetery. Established 1970. "
        "Operated as a partnership by Jeff Roberts (CFO). "
        "Associated with 'Greenlawn & Seneca Memory Gardens' (greenlawnclyde.com) — "
        "joint operation with Greenlawn Cemetery in Clyde OH (Sandusky County). "
        "Note: different from Greenlawn Cemetery Association in Tiffin (greenlawncemeterytiffin.org). "
        "Phone: 419-447-0072. "
        "T8 Private Cemetery (memorial park style)."
    ),
    "township_raw": None,
    "municipality_raw": None,
    "discovery_tier": 8,
    "seeded_from_baseline": False,
    "baseline_id": None,
}

records = [
    clinton_heights,
    lakeland_golf,
    loudon_meadows,
    mohawk_golf,
    seneca_hills_golf,
    seneca_caverns,
    camp_pittenger,
    felc,
    greenlawn_cem,
    fairmont_cem,
    seneca_memory_gardens,
]

for rec in records:
    data["records"].append(rec)

f.write_text(yaml.dump(data, allow_unicode=True, sort_keys=False), encoding="utf-8")
print(f"Staged {len(records)} T8 main entities.")
print(f"Total records: {len(data['records'])}, current_tier: {data['current_tier']}")
