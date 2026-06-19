import yaml, pathlib

f = pathlib.Path(r"D:\users\user1\Documents\CP Projects\Natural Areas Project v5\County_Spreadsheets\Seneca\seneca_ohio_raw_discovery.yaml")
data = yaml.safe_load(f.read_text(encoding="utf-8"))
data.setdefault("records", [])

# ============================================================
# LATE T5 DISCOVERIES — Township cemeteries confirmed during T8 GNIS enumeration
# Source: OhioGenealogyExpress.com Seneca County cemetery list
# https://ohiogenealogyexpress.com/seneca/cemeteries.html
# These townships were marked "unconfirmed" at T5 (no township website found).
# OGE list confirms existence; governance = township trustees per ORC 517.
# ============================================================

late_t5 = [
    {
        "entity_type": "Site",
        "name_raw": "Scipio Township Cemetery",
        "counties_raw": ["Seneca"],
        "county_primary": "Seneca",
        "ownership_raw": "Scipio Township (presumed)",
        "governance_raw": "Scipio Township Trustees",
        "partner_agencies_raw": None,
        "coordination_raw": None,
        "gps_lat_raw": None,
        "gps_lon_raw": None,
        "location_raw": "Scipio Township, Seneca County, OH",
        "acres_raw": None,
        "description_raw": None,
        "features_raw": None,
        "difficulty_raw": None,
        "accessibility_raw": None,
        "urls_raw": [
            "https://ohiogenealogyexpress.com/seneca/cemeteries.html",
        ],
        "identity_notes_raw": (
            "LATE T5 DISCOVERY — confirmed via OhioGenealogyExpress Seneca County cemetery list during T8 GNIS enumeration. "
            "Scipio Township was marked 'unconfirmed' at T5 (no township website found). "
            "Cemetery name pattern matches township governance (ORC 517). "
            "Governance confirmed as township trustees by convention. "
            "No independent website or address found — GPS and location data to be acquired during pipeline pass."
        ),
        "township_raw": None,
        "municipality_raw": None,
        "discovery_tier": 5,
        "seeded_from_baseline": False,
        "baseline_id": None,
    },
    {
        "entity_type": "Site",
        "name_raw": "Thompson Center Cemetery",
        "counties_raw": ["Seneca"],
        "county_primary": "Seneca",
        "ownership_raw": "Thompson Township (presumed)",
        "governance_raw": "Thompson Township Trustees",
        "partner_agencies_raw": None,
        "coordination_raw": None,
        "gps_lat_raw": None,
        "gps_lon_raw": None,
        "location_raw": "Thompson Township, Seneca County, OH (near Thompson Center community)",
        "acres_raw": None,
        "description_raw": None,
        "features_raw": None,
        "difficulty_raw": None,
        "accessibility_raw": None,
        "urls_raw": [
            "https://ohiogenealogyexpress.com/seneca/cemeteries.html",
        ],
        "identity_notes_raw": (
            "LATE T5 DISCOVERY — confirmed via OhioGenealogyExpress Seneca County cemetery list during T8 GNIS enumeration. "
            "Thompson Township was marked 'unconfirmed' at T5 (no township website; thomsonohio.org discarded per §4.2a as Geauga County site). "
            "Cemetery name includes 'Center' suggesting location near the township center community. "
            "Governance: township trustees by convention (ORC 517)."
        ),
        "township_raw": None,
        "municipality_raw": None,
        "discovery_tier": 5,
        "seeded_from_baseline": False,
        "baseline_id": None,
    },
    {
        "entity_type": "Site",
        "name_raw": "Liberty Cemetery",
        "counties_raw": ["Seneca"],
        "county_primary": "Seneca",
        "ownership_raw": "Liberty Township (presumed) OR private congregation/association",
        "governance_raw": "Governance uncertain — Liberty Township Trustees probable",
        "partner_agencies_raw": None,
        "coordination_raw": None,
        "gps_lat_raw": None,
        "gps_lon_raw": None,
        "location_raw": "Liberty Township, Seneca County, OH",
        "acres_raw": None,
        "description_raw": None,
        "features_raw": None,
        "difficulty_raw": None,
        "accessibility_raw": None,
        "urls_raw": [
            "https://ohiogenealogyexpress.com/seneca/cemeteries.html",
        ],
        "identity_notes_raw": (
            "LATE T5 DISCOVERY — confirmed via OhioGenealogyExpress Seneca County cemetery list during T8 GNIS enumeration. "
            "Liberty Township was marked 'null — unconfirmed' at T5 (no township website, high-risk common name §4.2a). "
            "Cemetery name 'Liberty Cemetery' could indicate township governance (T5) or a Liberty congregation/association (T8). "
            "Staged at T5 pending governance verification. Re-tier to T8 if confirmed private/church ownership."
        ),
        "township_raw": None,
        "municipality_raw": None,
        "discovery_tier": 5,
        "seeded_from_baseline": False,
        "baseline_id": None,
    },
    {
        "entity_type": "Site",
        "name_raw": "Big Spring Cemetery",
        "counties_raw": ["Seneca"],
        "county_primary": "Seneca",
        "ownership_raw": "Big Spring Township (presumed) OR private congregation",
        "governance_raw": "Governance uncertain — Big Spring Township Trustees probable",
        "partner_agencies_raw": None,
        "coordination_raw": None,
        "gps_lat_raw": None,
        "gps_lon_raw": None,
        "location_raw": "Big Spring Township, Seneca County, OH",
        "acres_raw": None,
        "description_raw": None,
        "features_raw": None,
        "difficulty_raw": None,
        "accessibility_raw": None,
        "urls_raw": [
            "https://ohiogenealogyexpress.com/seneca/cemeteries.html",
        ],
        "identity_notes_raw": (
            "LATE T5 DISCOVERY — confirmed via OhioGenealogyExpress Seneca County cemetery list during T8 GNIS enumeration. "
            "Big Spring Township was marked 'null — unconfirmed' at T5 (no township website). "
            "Name 'Big Spring Cemetery' matches Big Spring Township (likely township-governed). "
            "Staged at T5 pending governance verification. Re-tier to T8 if confirmed private/church ownership."
        ),
        "township_raw": None,
        "municipality_raw": None,
        "discovery_tier": 5,
        "seeded_from_baseline": False,
        "baseline_id": None,
    },
]

for rec in late_t5:
    data["records"].append(rec)

f.write_text(yaml.dump(data, allow_unicode=True, sort_keys=False), encoding="utf-8")
print(f"Staged {len(late_t5)} late T5 cemetery entities.")
print(f"Total records: {len(data['records'])}, current_tier: {data['current_tier']}")
