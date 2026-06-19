import yaml, pathlib

f = pathlib.Path(r"D:\users\user1\Documents\CP Projects\Natural Areas Project v5\County_Spreadsheets\Seneca\seneca_ohio_raw_discovery.yaml")
data = yaml.safe_load(f.read_text(encoding="utf-8"))
data.setdefault("records", [])

# ============================================================
# TIER 8 — PRIVATE CEMETERIES (OGE GNIS ENUMERATION)
# Source: OhioGenealogyExpress.com Seneca County cemetery list
# https://ohiogenealogyexpress.com/seneca/cemeteries.html
# IMP-111: GNIS cemetery enumeration mandatory before search queries.
#
# ALREADY STAGED (excluded from this script):
#   T5:  Bloom Township Cemetery, Loudon Township Cemetery,
#        Scipio Township Cemetery (late T5), Thompson Center Cemetery (late T5),
#        Liberty Cemetery (late T5), Big Spring Cemetery (late T5)
#   T8 main: Greenlawn Cemetery, Fairmont Cemetery, Seneca Memory Gardens
#
# DEDUPLICATION NOTES (staged with warnings):
#   Attica Cemetery — may = T5 Attica-Venice Township Joint Cemetery (CGR.0000981776)
#   Zion Lutheran Cemetery — may = T5 Zion Cemetery (Jackson Twp, CR 592)
#   Pleasant Ridge/Union/View — may relate to T5 Pleasant Twp maintained cemeteries
#     (T5 names: Chenoweth, Gundy, Ebenezer M.E., Little Pennsylvania, Oak Grove —
#      none match OGE "Pleasant Ridge/Union/View"; staging as separate T8 entities)
#   County Home Cemetery — possible T4 (county commissioner infirmary cemetery);
#      staged T8 pending governance verification
#   Bloomville Cemetery — possible T6 (Village of Bloomville); staged T8 pending
#      governance verification
#
# OGE "Reformed Cemetery (×2)" and "Rock Creek Cemetery (×2)" are distinct entries;
# staged as "[name]" and "[name] [2]" per GNIS convention.
# ============================================================

OGE_URL = "https://ohiogenealogyexpress.com/seneca/cemeteries.html"
SEN = "Seneca County, OH"

def cem(name, ownership, governance, location, notes):
    return {
        "entity_type": "Site",
        "name_raw": name,
        "counties_raw": ["Seneca"],
        "county_primary": "Seneca",
        "ownership_raw": ownership,
        "governance_raw": governance,
        "partner_agencies_raw": None,
        "coordination_raw": None,
        "gps_lat_raw": None,
        "gps_lon_raw": None,
        "location_raw": location,
        "acres_raw": None,
        "description_raw": None,
        "features_raw": None,
        "difficulty_raw": None,
        "accessibility_raw": None,
        "urls_raw": [OGE_URL],
        "identity_notes_raw": notes,
        "township_raw": None,
        "municipality_raw": None,
        "discovery_tier": 8,
        "seeded_from_baseline": False,
        "baseline_id": None,
    }


records = [

    # ---- CHURCH CEMETERIES ----

    cem(
        "Adams Lutheran Cemetery",
        "Private — Lutheran congregation (presumed)",
        "Unknown — Lutheran church congregation or church body (presumed)",
        "Adams Township area, Seneca County, OH",
        "T8 CEMETERY — GNIS enumeration via OhioGenealogyExpress Seneca County cemetery list. "
        "Name indicates Lutheran church affiliation. Governance: private religious congregation per ORC 517.10. "
        "No independent website or address found — GPS and location to be acquired during pipeline pass.",
    ),
    cem(
        "Assumption Cemetery",
        "Private — Roman Catholic congregation (presumed)",
        "Unknown — Roman Catholic parish or diocese (presumed)",
        "Seneca County, OH",
        "T8 CEMETERY — GNIS enumeration via OhioGenealogyExpress Seneca County cemetery list. "
        "Name indicates Roman Catholic affiliation (Assumption of Mary). Governance: parish or diocese per ORC 517.10. "
        "No independent website or address found — GPS and location to be acquired during pipeline pass.",
    ),
    cem(
        "Bethel Cemetery",
        "Private — church congregation or community association (presumed)",
        "Unknown — Bethel church congregation or private community association (presumed)",
        "Seneca County, OH",
        "T8 CEMETERY — GNIS enumeration via OhioGenealogyExpress Seneca County cemetery list. "
        "'Bethel' may indicate a church affiliation (Bethel Church/Meeting House) or a community cemetery "
        "named for a local landmark. Governance: private religious or community association per ORC 517.10. "
        "No independent website or address found.",
    ),
    cem(
        "Caroline Lutheran Cemetery",
        "Private — Lutheran congregation (presumed)",
        "Unknown — Lutheran church congregation or church body (presumed)",
        "Seneca County, OH",
        "T8 CEMETERY — GNIS enumeration via OhioGenealogyExpress Seneca County cemetery list. "
        "Name indicates Lutheran church affiliation, possibly associated with a Caroline Township-area congregation. "
        "Governance: private religious congregation per ORC 517.10. "
        "No independent website or address found — GPS and location to be acquired during pipeline pass.",
    ),
    cem(
        "Dunkard Cemetery",
        "Private — Dunkard Brethren congregation (presumed)",
        "Unknown — Dunkard Brethren church congregation (presumed)",
        "Seneca County, OH",
        "T8 CEMETERY — GNIS enumeration via OhioGenealogyExpress Seneca County cemetery list. "
        "Name indicates Dunkard Brethren (German Baptist Brethren) affiliation. "
        "Governance: private religious congregation per ORC 517.10. "
        "No independent website or address found — GPS and location to be acquired during pipeline pass.",
    ),
    cem(
        "East Baseline Baptist Cemetery",
        "Private — Baptist congregation (presumed)",
        "Unknown — Baptist church congregation (presumed)",
        "Seneca County, OH (East Baseline Road area)",
        "T8 CEMETERY — GNIS enumeration via OhioGenealogyExpress Seneca County cemetery list. "
        "Name indicates Baptist church affiliation along East Baseline Road. "
        "Governance: private religious congregation per ORC 517.10. "
        "No independent website or address found — GPS and location to be acquired during pipeline pass.",
    ),
    cem(
        "Jerusalem Cemetery",
        "Private — church congregation or community association (presumed)",
        "Unknown — Jerusalem church congregation or private community association (presumed)",
        "Seneca County, OH",
        "T8 CEMETERY — GNIS enumeration via OhioGenealogyExpress Seneca County cemetery list. "
        "'Jerusalem' is a common Ohio church/congregation name. May indicate a church affiliation or "
        "a community cemetery named for a local community or crossroads. "
        "Governance: private religious or community association per ORC 517.10. "
        "No independent website or address found.",
    ),
    cem(
        "Mennonite Cemetery",
        "Private — Mennonite congregation (presumed)",
        "Unknown — Mennonite church congregation (presumed)",
        "Seneca County, OH",
        "T8 CEMETERY — GNIS enumeration via OhioGenealogyExpress Seneca County cemetery list. "
        "Name indicates Mennonite church affiliation. Mennonite communities have historic presence in north-central Ohio. "
        "Governance: private religious congregation per ORC 517.10. "
        "No independent website or address found — GPS and location to be acquired during pipeline pass.",
    ),
    cem(
        "Methodist Cemetery",
        "Private — Methodist congregation (presumed)",
        "Unknown — United Methodist or Methodist church congregation (presumed)",
        "Seneca County, OH",
        "T8 CEMETERY — GNIS enumeration via OhioGenealogyExpress Seneca County cemetery list. "
        "Name indicates Methodist church affiliation. Governance: private religious congregation per ORC 517.10. "
        "No independent website or address found — GPS and location to be acquired during pipeline pass.",
    ),
    cem(
        "Reformed Cemetery",
        "Private — Reformed church congregation (presumed)",
        "Unknown — Reformed Church congregation (presumed)",
        "Seneca County, OH",
        "T8 CEMETERY — GNIS enumeration via OhioGenealogyExpress Seneca County cemetery list. "
        "OGE lists 'Reformed Cemetery' TWICE — two distinct cemeteries with the same name exist in Seneca County. "
        "This record is instance 1 of 2. The second instance is staged as 'Reformed Cemetery [2]'. "
        "Name indicates Reformed Church (German Reformed / United Church of Christ) affiliation. "
        "Governance: private religious congregation per ORC 517.10. "
        "No independent website or address found — identity verification required during GPS acquisition pass.",
    ),
    cem(
        "Reformed Cemetery [2]",
        "Private — Reformed church congregation (presumed)",
        "Unknown — Reformed Church congregation (presumed)",
        "Seneca County, OH",
        "T8 CEMETERY — GNIS enumeration via OhioGenealogyExpress Seneca County cemetery list. "
        "OGE lists 'Reformed Cemetery' TWICE — two distinct cemeteries with the same name exist in Seneca County. "
        "This record is instance 2 of 2. The first instance is staged as 'Reformed Cemetery'. "
        "Name indicates Reformed Church (German Reformed / United Church of Christ) affiliation. "
        "Governance: private religious congregation per ORC 517.10. "
        "Name_raw uses '[2]' suffix to distinguish; actual official name is 'Reformed Cemetery' for both. "
        "GPS acquisition pass required to distinguish locations.",
    ),
    cem(
        "Saint Andrews Cemetery",
        "Private — church congregation (presumed)",
        "Unknown — Saint Andrews church congregation (Anglican, Catholic, or other) (presumed)",
        "Seneca County, OH",
        "T8 CEMETERY — GNIS enumeration via OhioGenealogyExpress Seneca County cemetery list. "
        "Name indicates a Saint Andrews parish affiliation (may be Catholic, Anglican, or other denomination). "
        "Governance: private religious congregation per ORC 517.10. "
        "No independent website or address found — GPS and location to be acquired during pipeline pass.",
    ),
    cem(
        "Saint Boniface Cemetery",
        "Private — Roman Catholic congregation (presumed)",
        "Unknown — Roman Catholic parish or diocese (Saint Boniface) (presumed)",
        "Seneca County, OH",
        "T8 CEMETERY — GNIS enumeration via OhioGenealogyExpress Seneca County cemetery list. "
        "Saint Boniface is a Roman Catholic patron saint; name indicates Catholic parish affiliation. "
        "Governance: parish or diocese per ORC 517.10. "
        "No independent website or address found — GPS and location to be acquired during pipeline pass.",
    ),
    cem(
        "Saint Jacobs Cemetery",
        "Private — church congregation (presumed)",
        "Unknown — Saint Jacobs church congregation (Lutheran, Reformed, or other) (presumed)",
        "Seneca County, OH",
        "T8 CEMETERY — GNIS enumeration via OhioGenealogyExpress Seneca County cemetery list. "
        "Saint Jacobs (Saint James) cemeteries in Ohio commonly associated with Lutheran or Reformed congregations. "
        "Governance: private religious congregation per ORC 517.10. "
        "No independent website or address found — GPS and location to be acquired during pipeline pass.",
    ),
    cem(
        "Saint Josephs Cemetery",
        "Private — Roman Catholic congregation (presumed)",
        "Unknown — Roman Catholic parish or diocese (Saint Joseph) (presumed)",
        "Seneca County, OH",
        "T8 CEMETERY — GNIS enumeration via OhioGenealogyExpress Seneca County cemetery list. "
        "Saint Joseph is a Roman Catholic patron; name indicates Catholic parish affiliation. "
        "Governance: parish or diocese per ORC 517.10. "
        "No independent website or address found — GPS and location to be acquired during pipeline pass.",
    ),
    cem(
        "Saint Marys Cemetery",
        "Private — Roman Catholic congregation (presumed)",
        "Unknown — Roman Catholic parish or diocese (Saint Mary) (presumed)",
        "Seneca County, OH",
        "T8 CEMETERY — GNIS enumeration via OhioGenealogyExpress Seneca County cemetery list. "
        "Saint Mary cemeteries are commonly Roman Catholic. Governance: parish or diocese per ORC 517.10. "
        "No independent website or address found — GPS and location to be acquired during pipeline pass.",
    ),
    cem(
        "Saint Michaels Cemetery",
        "Private — church congregation (presumed)",
        "Unknown — Saint Michaels church congregation (Catholic, Lutheran, or other) (presumed)",
        "Seneca County, OH",
        "T8 CEMETERY — GNIS enumeration via OhioGenealogyExpress Seneca County cemetery list. "
        "Saint Michael is associated with both Catholic and Lutheran parishes. "
        "Governance: private religious congregation per ORC 517.10. "
        "No independent website or address found — GPS and location to be acquired during pipeline pass.",
    ),
    cem(
        "Saint Patricks Cemetery",
        "Private — Roman Catholic congregation (presumed)",
        "Unknown — Roman Catholic parish or diocese (Saint Patrick) (presumed)",
        "Seneca County, OH",
        "T8 CEMETERY — GNIS enumeration via OhioGenealogyExpress Seneca County cemetery list. "
        "Saint Patrick is a Roman Catholic patron; name indicates Catholic parish affiliation. "
        "Governance: parish or diocese per ORC 517.10. "
        "No independent website or address found — GPS and location to be acquired during pipeline pass.",
    ),
    cem(
        "Saint Peters Cemetery",
        "Private — church congregation (presumed)",
        "Unknown — Saint Peters church congregation (Catholic, Lutheran, or other) (presumed)",
        "Seneca County, OH",
        "T8 CEMETERY — GNIS enumeration via OhioGenealogyExpress Seneca County cemetery list. "
        "Saint Peter cemeteries are common across Catholic and Lutheran traditions. "
        "Governance: private religious congregation per ORC 517.10. "
        "No independent website or address found — GPS and location to be acquired during pipeline pass.",
    ),
    cem(
        "Saint Stephens Cemetery",
        "Private — church congregation (presumed)",
        "Unknown — Saint Stephens church congregation (Catholic, Lutheran, or other) (presumed)",
        "Seneca County, OH",
        "T8 CEMETERY — GNIS enumeration via OhioGenealogyExpress Seneca County cemetery list. "
        "Saint Stephen cemeteries are common across Catholic and Lutheran traditions. "
        "Governance: private religious congregation per ORC 517.10. "
        "No independent website or address found — GPS and location to be acquired during pipeline pass.",
    ),
    cem(
        "Saints Peter and Paul Cemetery",
        "Private — Roman Catholic congregation (presumed)",
        "Unknown — Roman Catholic parish or diocese (Saints Peter and Paul) (presumed)",
        "Seneca County, OH",
        "T8 CEMETERY — GNIS enumeration via OhioGenealogyExpress Seneca County cemetery list. "
        "Saints Peter and Paul is a common Roman Catholic parish dedication. "
        "Governance: parish or diocese per ORC 517.10. "
        "No independent website or address found — GPS and location to be acquired during pipeline pass.",
    ),
    cem(
        "Shiloh Cemetery",
        "Private — church congregation or community association (presumed)",
        "Unknown — Shiloh church congregation or private community association (presumed)",
        "Seneca County, OH",
        "T8 CEMETERY — GNIS enumeration via OhioGenealogyExpress Seneca County cemetery list. "
        "'Shiloh' is a common Ohio church/congregation name (Baptist, Methodist, or other Protestant traditions). "
        "Governance: private religious or community association per ORC 517.10. "
        "No independent website or address found — GPS and location to be acquired during pipeline pass.",
    ),
    cem(
        "Zion Lutheran Cemetery",
        "Private — Lutheran congregation (presumed)",
        "Unknown — Lutheran church congregation (presumed)",
        "Seneca County, OH",
        "T8 CEMETERY — GNIS enumeration via OhioGenealogyExpress Seneca County cemetery list. "
        "POSSIBLE DUPLICATE WARNING: T5 staged 'Zion Cemetery' (Jackson Township, CR 592, Active) "
        "managed by Jackson Township Trustees. If Zion Cemetery is associated with a Lutheran congregation "
        "that deeded management to the township, these may be the same entity. "
        "If confirmed identical → remove this T8 record; retain T5 staged record. "
        "If confirmed separate → Zion Lutheran Cemetery is a distinct T8 private cemetery. "
        "Governance verification required during GPS acquisition pass.",
    ),

    # ---- COMMUNITY / FAMILY / PRIVATE CEMETERIES ----

    cem(
        "Armstrong Cemetery",
        "Private — family or community association (presumed)",
        "Unknown — private family, community association, or nonprofit (presumed)",
        "Seneca County, OH",
        "T8 CEMETERY — GNIS enumeration via OhioGenealogyExpress Seneca County cemetery list. "
        "Surname-based name indicates private family or community cemetery. "
        "Governance: private per ORC 517. "
        "No independent website or address found — GPS and location to be acquired during pipeline pass.",
    ),
    cem(
        "Attica Cemetery",
        "Unknown — Village of Attica, Venice Township, or private association (presumed)",
        "Unknown — see identity note",
        "Attica area, Seneca County, OH",
        "T8 CEMETERY — GNIS enumeration via OhioGenealogyExpress Seneca County cemetery list. "
        "POSSIBLE DUPLICATE WARNING: T5 staged 'Attica-Venice Township Joint Cemetery' "
        "(ODRE registered CGR.0000981776, Venice Township, Attica area). "
        "If OGE 'Attica Cemetery' = the Attica-Venice Joint Cemetery → this is a duplicate; "
        "remove this T8 record and retain T5 staged record. "
        "If 'Attica Cemetery' is a distinct village-owned or private cemetery → stage here. "
        "Governance verification required. If village-owned → re-tier to T6.",
    ),
    cem(
        "Bare Cemetery",
        "Private — family or community association (presumed)",
        "Unknown — private family, community association, or nonprofit (presumed)",
        "Seneca County, OH",
        "T8 CEMETERY — GNIS enumeration via OhioGenealogyExpress Seneca County cemetery list. "
        "Surname-based name indicates private family or community cemetery. "
        "Governance: private per ORC 517. "
        "No independent website or address found.",
    ),
    cem(
        "Baugher Cemetery",
        "Private — family or community association (presumed)",
        "Unknown — private family, community association, or nonprofit (presumed)",
        "Seneca County, OH",
        "T8 CEMETERY — GNIS enumeration via OhioGenealogyExpress Seneca County cemetery list. "
        "Surname-based name indicates private family or community cemetery. "
        "Governance: private per ORC 517. "
        "No independent website or address found.",
    ),
    cem(
        "Block Cemetery",
        "Private — family or community association (presumed)",
        "Unknown — private family, community association, or nonprofit (presumed)",
        "Seneca County, OH",
        "T8 CEMETERY — GNIS enumeration via OhioGenealogyExpress Seneca County cemetery list. "
        "May be surname-based or named for a geographic block. "
        "Governance: private per ORC 517. "
        "No independent website or address found.",
    ),
    cem(
        "Bloomville Cemetery",
        "Unknown — Village of Bloomville or private cemetery association (presumed)",
        "Unknown — Village of Bloomville (possible T6) or private cemetery association (presumed)",
        "Bloomville, Seneca County, OH",
        "T8 CEMETERY — GNIS enumeration via OhioGenealogyExpress Seneca County cemetery list. "
        "NAME SUGGESTS MUNICIPAL AFFILIATION: 'Bloomville Cemetery' may be owned by the Village of Bloomville. "
        "T6 Bloomville was checked (Beeghly Park staged) but no village cemetery was identified during T6. "
        "If confirmed village-owned → re-tier to T6 (Village of Bloomville). "
        "Staged T8 pending governance verification.",
    ),
    cem(
        "Brundedge Cemetery",
        "Private — family or community association (presumed)",
        "Unknown — private family, community association, or nonprofit (presumed)",
        "Seneca County, OH",
        "T8 CEMETERY — GNIS enumeration via OhioGenealogyExpress Seneca County cemetery list. "
        "Surname-based name indicates private family cemetery. "
        "Governance: private per ORC 517. "
        "No independent website or address found.",
    ),
    cem(
        "Bunker Hill Cemetery",
        "Private — community or church association (presumed)",
        "Unknown — private community or church association (presumed)",
        "Seneca County, OH",
        "T8 CEMETERY — GNIS enumeration via OhioGenealogyExpress Seneca County cemetery list. "
        "'Bunker Hill' is a common Ohio community name; may be a community or church cemetery. "
        "Governance: private per ORC 517. "
        "No independent website or address found.",
    ),
    cem(
        "Clay Cemetery",
        "Private — family or community association (presumed)",
        "Unknown — private family, community association, or nonprofit (presumed)",
        "Seneca County, OH",
        "T8 CEMETERY — GNIS enumeration via OhioGenealogyExpress Seneca County cemetery list. "
        "May be surname-based or named for a clay soil area. "
        "Governance: private per ORC 517. "
        "No independent website or address found.",
    ),
    cem(
        "Coffman Cemetery",
        "Private — family or community association (presumed)",
        "Unknown — private family, community association, or nonprofit (presumed)",
        "Seneca County, OH",
        "T8 CEMETERY — GNIS enumeration via OhioGenealogyExpress Seneca County cemetery list. "
        "Surname-based name indicates private family cemetery. "
        "Governance: private per ORC 517. "
        "No independent website or address found.",
    ),
    cem(
        "County Home Cemetery",
        "Unknown — Seneca County (historical infirmary/poorhouse) or private successor (presumed)",
        "Unknown — possibly Seneca County Commissioners (historical T4) or private successor",
        "Seneca County, OH (former county infirmary / poorhouse grounds)",
        "T8 CEMETERY — GNIS enumeration via OhioGenealogyExpress Seneca County cemetery list. "
        "GOVERNANCE FLAG — T4 CANDIDATE: Ohio county home (infirmary/poorhouse) cemeteries were historically "
        "owned by county commissioners (ORC Chapter 5155). If the Seneca County Infirmary/Home grounds are still "
        "county-owned, this cemetery should re-tier to T4 (County Commissioner-managed). "
        "T4 discovery found no county-managed parks; county home cemetery was not on the T4 checklist. "
        "Staged T8 pending T4 governance verification with Seneca County Engineer or GIS parcel data.",
    ),
    cem(
        "Crissa Cemetery",
        "Private — family or community association (presumed)",
        "Unknown — private family, community association, or nonprofit (presumed)",
        "Seneca County, OH",
        "T8 CEMETERY — GNIS enumeration via OhioGenealogyExpress Seneca County cemetery list. "
        "Possibly surname-based or named for a local community. "
        "Governance: private per ORC 517. "
        "No independent website or address found.",
    ),
    cem(
        "Dysinger Cemetery",
        "Private — family or community association (presumed)",
        "Unknown — private family, community association, or nonprofit (presumed)",
        "Seneca County, OH",
        "T8 CEMETERY — GNIS enumeration via OhioGenealogyExpress Seneca County cemetery list. "
        "Surname-based name indicates private family cemetery. "
        "Governance: private per ORC 517. "
        "No independent website or address found.",
    ),
    cem(
        "Egbert Cemetery",
        "Private — family or community association (presumed)",
        "Unknown — private family, community association, or nonprofit (presumed)",
        "Seneca County, OH",
        "T8 CEMETERY — GNIS enumeration via OhioGenealogyExpress Seneca County cemetery list. "
        "Surname-based name indicates private family cemetery. "
        "Governance: private per ORC 517. "
        "No independent website or address found.",
    ),
    cem(
        "Farewell Retreat Cemetery",
        "Private — family or community association (presumed)",
        "Unknown — private family, community association, or nonprofit (presumed)",
        "Seneca County, OH",
        "T8 CEMETERY — GNIS enumeration via OhioGenealogyExpress Seneca County cemetery list. "
        "Unusual name; may be a small family cemetery associated with a 'Farewell Retreat' property or community. "
        "Governance: private per ORC 517. "
        "No independent website or address found.",
    ),
    cem(
        "Feaselburg Cemetery",
        "Private — community association (presumed)",
        "Unknown — private community association or nonprofit (presumed)",
        "Feaselburg community, Seneca County, OH",
        "T8 CEMETERY — GNIS enumeration via OhioGenealogyExpress Seneca County cemetery list. "
        "Named for the Feaselburg community (small unincorporated settlement in Seneca County). "
        "Community cemetery — governance likely private association or unconfirmed township (ORC 517). "
        "No independent website or address found.",
    ),
    cem(
        "Fireside Cemetery",
        "Private — family or community association (presumed)",
        "Unknown — private family, community association, or nonprofit (presumed)",
        "Seneca County, OH",
        "T8 CEMETERY — GNIS enumeration via OhioGenealogyExpress Seneca County cemetery list. "
        "Governance: private per ORC 517. "
        "No independent website or address found.",
    ),
    cem(
        "Flat Rock Cemetery",
        "Unknown — Flat Rock community, Village of Flat Rock (unincorporated), or private association (presumed)",
        "Unknown — community, township, or private association (Flat Rock CDP area)",
        "Flat Rock area, Seneca County, OH",
        "T8 CEMETERY — GNIS enumeration via OhioGenealogyExpress Seneca County cemetery list. "
        "Named for the Flat Rock community (unincorporated CDP in Seneca County). "
        "Flat Rock is unincorporated — no municipal T6 entity. Governance may be township (T5) or private (T8). "
        "Staged T8 pending governance verification. If confirmed township-managed → re-tier T5.",
    ),
    cem(
        "Fravel Cemetery",
        "Private — family or community association (presumed)",
        "Unknown — private family, community association, or nonprofit (presumed)",
        "Seneca County, OH",
        "T8 CEMETERY — GNIS enumeration via OhioGenealogyExpress Seneca County cemetery list. "
        "Surname-based name indicates private family cemetery. "
        "Governance: private per ORC 517. "
        "No independent website or address found.",
    ),
    cem(
        "French Town Cemetery",
        "Private — community association (presumed)",
        "Unknown — private community association or nonprofit (presumed)",
        "French Town area, Seneca County, OH",
        "T8 CEMETERY — GNIS enumeration via OhioGenealogyExpress Seneca County cemetery list. "
        "Named for the French Town community (historic French-American settlement area in Seneca County). "
        "Community cemetery — governance likely private association. "
        "No independent website or address found.",
    ),
    cem(
        "Hopewell Cemetery",
        "Private — community or township association (uncertain)",
        "Unknown — private community association or Hopewell Township trustees (uncertain)",
        "Hopewell Township area, Seneca County, OH",
        "T8 CEMETERY — GNIS enumeration via OhioGenealogyExpress Seneca County cemetery list. "
        "POSSIBLE T5: Name suggests Hopewell Township association. T5 Hopewell Township was searched; "
        "only Meadowbrook Park was found (no township cemetery confirmed at T5). "
        "If Hopewell Cemetery is confirmed as township-managed → re-tier to T5. "
        "Staged T8 pending governance verification.",
    ),
    cem(
        "Kagy Cemetery",
        "Private — family or community association (presumed)",
        "Unknown — private family, community association, or nonprofit (presumed)",
        "Seneca County, OH",
        "T8 CEMETERY — GNIS enumeration via OhioGenealogyExpress Seneca County cemetery list. "
        "Surname-based name indicates private family cemetery. "
        "Governance: private per ORC 517. "
        "No independent website or address found.",
    ),
    cem(
        "Lay Cemetery",
        "Private — family or community association (presumed)",
        "Unknown — private family, community association, or nonprofit (presumed)",
        "Seneca County, OH",
        "T8 CEMETERY — GNIS enumeration via OhioGenealogyExpress Seneca County cemetery list. "
        "Surname-based name indicates private family cemetery. "
        "Governance: private per ORC 517. "
        "No independent website or address found.",
    ),
    cem(
        "Lowell Cemetery",
        "Private — community association (presumed)",
        "Unknown — private community association or nonprofit (presumed)",
        "Seneca County, OH",
        "T8 CEMETERY — GNIS enumeration via OhioGenealogyExpress Seneca County cemetery list. "
        "May be named for the Lowell community or a person named Lowell. "
        "Governance: private per ORC 517. "
        "No independent website or address found.",
    ),
    cem(
        "McMeen Cemetery",
        "Private — family or community association (presumed)",
        "Unknown — private family, community association, or nonprofit (presumed)",
        "Seneca County, OH",
        "T8 CEMETERY — GNIS enumeration via OhioGenealogyExpress Seneca County cemetery list. "
        "Surname-based name indicates private family cemetery. "
        "Governance: private per ORC 517. "
        "No independent website or address found.",
    ),
    cem(
        "Null Cemetery",
        "Private — family or community association (presumed)",
        "Unknown — private family, community association, or nonprofit (presumed)",
        "Seneca County, OH",
        "T8 CEMETERY — GNIS enumeration via OhioGenealogyExpress Seneca County cemetery list. "
        "Surname-based name — 'Null' is an established Seneca County family surname. "
        "Governance: private per ORC 517. "
        "No independent website or address found.",
    ),
    cem(
        "Omar Cemetery",
        "Private — community or family association (presumed)",
        "Unknown — private community or family association (presumed)",
        "Seneca County, OH",
        "T8 CEMETERY — GNIS enumeration via OhioGenealogyExpress Seneca County cemetery list. "
        "May be named for a community, a given name, or a surname. "
        "Governance: private per ORC 517. "
        "No independent website or address found.",
    ),
    cem(
        "Payne Cemetery",
        "Private — family or community association (presumed)",
        "Unknown — private family, community association, or nonprofit (presumed)",
        "Seneca County, OH",
        "T8 CEMETERY — GNIS enumeration via OhioGenealogyExpress Seneca County cemetery list. "
        "Surname-based name indicates private family cemetery. "
        "Governance: private per ORC 517. "
        "No independent website or address found.",
    ),
    cem(
        "Pleasant Ridge Cemetery",
        "Private — community or association (uncertain; possible T5 Pleasant Township)",
        "Unknown — private community association or Pleasant Township Trustees (uncertain)",
        "Pleasant Township area, Seneca County, OH",
        "T8 CEMETERY — GNIS enumeration via OhioGenealogyExpress Seneca County cemetery list. "
        "POSSIBLE T5 RELATION: T5 staged 5 Pleasant Township cemeteries (Chenoweth/Gay Rd, Gundy/Norton Rd, "
        "Ebenezer M.E./Johnson Rd, Little Pennsylvania/SR 665, Oak Grove/Alkire Rd) maintained by township. "
        "Those T5 names do not match 'Pleasant Ridge Cemetery' — treating as a separate entity. "
        "If field verification confirms Pleasant Township trustees manage this cemetery → re-tier T5.",
    ),
    cem(
        "Pleasant Union Cemetery",
        "Private — community or association (uncertain; possible T5 Pleasant Township)",
        "Unknown — private community association or Pleasant Township Trustees (uncertain)",
        "Pleasant Township area, Seneca County, OH",
        "T8 CEMETERY — GNIS enumeration via OhioGenealogyExpress Seneca County cemetery list. "
        "POSSIBLE T5 RELATION: Same reasoning as Pleasant Ridge Cemetery above. "
        "T5 Pleasant Twp cemetery names do not match 'Pleasant Union Cemetery' — treating as separate entity. "
        "If field verification confirms Pleasant Township trustees manage this cemetery → re-tier T5.",
    ),
    cem(
        "Pleasant View Cemetery",
        "Private — community or association (uncertain; possible T5 Pleasant Township)",
        "Unknown — private community association or Pleasant Township Trustees (uncertain)",
        "Pleasant Township area, Seneca County, OH",
        "T8 CEMETERY — GNIS enumeration via OhioGenealogyExpress Seneca County cemetery list. "
        "POSSIBLE T5 RELATION: Same reasoning as Pleasant Ridge Cemetery above. "
        "T5 Pleasant Twp cemetery names do not match 'Pleasant View Cemetery' — treating as separate entity. "
        "If field verification confirms Pleasant Township trustees manage this cemetery → re-tier T5.",
    ),
    cem(
        "Randall Cemetery",
        "Private — family or community association (presumed)",
        "Unknown — private family, community association, or nonprofit (presumed)",
        "Seneca County, OH",
        "T8 CEMETERY — GNIS enumeration via OhioGenealogyExpress Seneca County cemetery list. "
        "Surname-based name indicates private family cemetery. "
        "Governance: private per ORC 517. "
        "No independent website or address found.",
    ),
    cem(
        "Raymond Cemetery",
        "Private — family or community association (presumed)",
        "Unknown — private family, community association, or nonprofit (presumed)",
        "Seneca County, OH",
        "T8 CEMETERY — GNIS enumeration via OhioGenealogyExpress Seneca County cemetery list. "
        "Surname-based name indicates private family cemetery. "
        "Governance: private per ORC 517. "
        "No independent website or address found.",
    ),
    cem(
        "Reisz Cemetery",
        "Private — family or community association (presumed)",
        "Unknown — private family, community association, or nonprofit (presumed)",
        "Seneca County, OH",
        "T8 CEMETERY — GNIS enumeration via OhioGenealogyExpress Seneca County cemetery list. "
        "Surname-based name indicates private family cemetery. "
        "Governance: private per ORC 517. "
        "No independent website or address found.",
    ),
    cem(
        "Rock Creek Cemetery",
        "Private — community or church association (presumed)",
        "Unknown — private community or church association (presumed)",
        "Seneca County, OH",
        "T8 CEMETERY — GNIS enumeration via OhioGenealogyExpress Seneca County cemetery list. "
        "OGE lists 'Rock Creek Cemetery' TWICE — two distinct cemeteries with the same name exist in Seneca County. "
        "This record is instance 1 of 2. The second instance is staged as 'Rock Creek Cemetery [2]'. "
        "Named for the Rock Creek waterway. Note: City of Tiffin 'Rock Creek Trail' (T6) follows the same waterway — "
        "this is a separate entity (cemetery, not trail). "
        "GPS acquisition pass required to distinguish locations of the two Rock Creek Cemeteries.",
    ),
    cem(
        "Rock Creek Cemetery [2]",
        "Private — community or church association (presumed)",
        "Unknown — private community or church association (presumed)",
        "Seneca County, OH",
        "T8 CEMETERY — GNIS enumeration via OhioGenealogyExpress Seneca County cemetery list. "
        "OGE lists 'Rock Creek Cemetery' TWICE — two distinct cemeteries with the same name exist in Seneca County. "
        "This record is instance 2 of 2. The first instance is staged as 'Rock Creek Cemetery'. "
        "Name_raw uses '[2]' suffix to distinguish; actual official name is 'Rock Creek Cemetery' for both. "
        "GPS acquisition pass required to distinguish locations.",
    ),
    cem(
        "Sand Ridge Cemetery",
        "Private — community or family association (presumed)",
        "Unknown — private community or family association (presumed)",
        "Seneca County, OH",
        "T8 CEMETERY — GNIS enumeration via OhioGenealogyExpress Seneca County cemetery list. "
        "Named for a sand ridge geographical feature. Community or family cemetery. "
        "Governance: private per ORC 517. "
        "No independent website or address found.",
    ),
    cem(
        "Sheller Cemetery",
        "Private — family or community association (presumed)",
        "Unknown — private family, community association, or nonprofit (presumed)",
        "Seneca County, OH",
        "T8 CEMETERY — GNIS enumeration via OhioGenealogyExpress Seneca County cemetery list. "
        "Surname-based name indicates private family cemetery. "
        "Governance: private per ORC 517. "
        "No independent website or address found.",
    ),
    cem(
        "Shock Cemetery",
        "Private — family or community association (presumed)",
        "Unknown — private family, community association, or nonprofit (presumed)",
        "Seneca County, OH",
        "T8 CEMETERY — GNIS enumeration via OhioGenealogyExpress Seneca County cemetery list. "
        "Surname-based name indicates private family cemetery. "
        "Governance: private per ORC 517. "
        "No independent website or address found.",
    ),
    cem(
        "Swamp Cemetery",
        "Private — community or family association (presumed)",
        "Unknown — private community or family association (presumed)",
        "Seneca County, OH",
        "T8 CEMETERY — GNIS enumeration via OhioGenealogyExpress Seneca County cemetery list. "
        "Descriptive/geographic name indicating location in or near a swampy area. "
        "Governance: private per ORC 517. "
        "No independent website or address found.",
    ),
    cem(
        "Underhill Cemetery",
        "Private — family or community association (presumed)",
        "Unknown — private family, community association, or nonprofit (presumed)",
        "Seneca County, OH",
        "T8 CEMETERY — GNIS enumeration via OhioGenealogyExpress Seneca County cemetery list. "
        "Surname-based name indicates private family cemetery. "
        "Governance: private per ORC 517. "
        "No independent website or address found.",
    ),
    cem(
        "Union Cemetery",
        "Private — community or multi-congregation association (presumed)",
        "Unknown — private community or multi-congregation association (presumed)",
        "Seneca County, OH",
        "T8 CEMETERY — GNIS enumeration via OhioGenealogyExpress Seneca County cemetery list. "
        "'Union' cemeteries in Ohio are typically shared cemeteries serving multiple denominations or communities. "
        "Governance: private per ORC 517. "
        "No independent website or address found.",
    ),
    cem(
        "Woodlawn Cemetery",
        "Private — cemetery association or nonprofit (presumed)",
        "Unknown — private cemetery association, nonprofit, or possibly Village of Tiffin",
        "Seneca County, OH",
        "T8 CEMETERY — GNIS enumeration via OhioGenealogyExpress Seneca County cemetery list. "
        "'Woodlawn' is a common name for private nonprofit cemetery associations in Ohio. "
        "May be associated with Tiffin (Woodlawn Cemetery Associations are common in Ohio cities). "
        "T6 Tiffin discovery found no city-owned cemetery — if this is Tiffin-associated, it is private. "
        "Governance: private cemetery association per ORC 1721. "
        "No independent website or address found — GPS and location to be acquired during pipeline pass.",
    ),

]

print(f"Records to stage: {len(records)}")
assert len(records) == 66, f"Expected 66 records, got {len(records)}"

for rec in records:
    data["records"].append(rec)

f.write_text(yaml.dump(data, allow_unicode=True, sort_keys=False), encoding="utf-8")
print(f"Staged {len(records)} T8 cemetery entities.")
print(f"Total records: {len(data['records'])}, current_tier: {data['current_tier']}")
