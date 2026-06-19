import yaml, pathlib

f = pathlib.Path(r"D:\users\user1\Documents\CP Projects\Natural Areas Project v5\County_Spreadsheets\Seneca\seneca_ohio_raw_discovery.yaml")
data = yaml.safe_load(f.read_text(encoding="utf-8"))
data.setdefault("records", [])
data.setdefault("tier_nulls", [])

# ============================================================
# LATE T3 DISCOVERY — Clary Boulee McDonald Preserve
# Governance: Seneca County Park District (SCPD)
# Confirmed during T7 review:
#   BSC website (https://www.blackswampconservancy.org/preserves/clary-boulee-mcdonald-preserve)
#   now states: "Now owned and managed by the Seneca County Park District."
#   SCPD website (https://www.senecacountyparks.com/places/clary-boulee-mcdonald-preserve)
#   still shows outdated BSC-owned text — BSC website treated as more current/authoritative.
# Originally deferred to T7 at T3 stage (result: deferred_to_tier_7 in tier_nulls).
# Re-tiers to T3 upon confirmed ownership transfer.
# ============================================================

SCPD_OWN = "Seneca County Park District"
SCPD_GOV = "Seneca County Park District (SCPD)"

clary_boulee_site = {
    "entity_type": "Site",
    "name_raw": "Clary Boulee McDonald Preserve",
    "counties_raw": ["Seneca"],
    "county_primary": "Seneca",
    "ownership_raw": SCPD_OWN,
    "governance_raw": SCPD_GOV,
    "partner_agencies_raw": "Black Swamp Conservancy (prior owner; H2Ohio program partner)",
    "coordination_raw": "H2Ohio Grant program (Ohio EPA water quality restoration)",
    "gps_lat_raw": None,
    "gps_lon_raw": None,
    "location_raw": (
        "SR 12 Entrance: 4747 W. State Route 12, Kansas OH 44841; "
        "TR 36 Entrance: 5090 W. Township Road 36, Kansas OH 44841; "
        "~1.4 miles SW of Bettsville, Seneca County"
    ),
    "acres_raw": "160",
    "description_raw": (
        "160-acre nature preserve featuring restored wetlands, Wolf Creek riparian habitat, "
        "floodplain forest corridor, and native ecosystems. Includes a 100-acre restoration "
        "component funded through the H2Ohio Grant program for water quality improvement. "
        "Two loop trails begin at the north entrance. Previously owned and managed by Black "
        "Swamp Conservancy; ownership transferred to Seneca County Park District upon "
        "completion of H2Ohio restoration work."
    ),
    "features_raw": [
        "Restored wetlands",
        "Wolf Creek riparian habitat",
        "Floodplain forest",
        "Native ecosystems",
        "Loop trails (2)",
        "H2Ohio water quality project viewing area",
        "Two access entrances (SR 12 and TR 36)",
    ],
    "difficulty_raw": None,
    "accessibility_raw": None,
    "urls_raw": [
        "https://www.blackswampconservancy.org/preserves/clary-boulee-mcdonald-preserve",
        "https://www.senecacountyparks.com/places/clary-boulee-mcdonald-preserve",
    ],
    "identity_notes_raw": (
        "LATE T3 DISCOVERY — confirmed during T7 review. "
        "Originally deferred to T7 (Black Swamp Conservancy ownership) via tier_nulls entry. "
        "BSC website now states: 'Now owned and managed by the Seneca County Park District, "
        "the preserve represents a collaborative effort to balance habitat restoration, water "
        "quality improvement, and public access.' "
        "SCPD website still shows outdated language ('currently owned by Black Swamp Conservancy') "
        "— BSC website treated as more authoritative and current source. "
        "Also referenced as 'Clary Boulee McDonald Nature Preserve' on some sources. "
        "Two unnamed loop trails staged separately as Trail entities (discovery_tier=3)."
    ),
    "township_raw": None,
    "municipality_raw": None,
    "discovery_tier": 3,
    "seeded_from_baseline": False,
    "baseline_id": None,
}

clary_boulee_trail_1mile = {
    "entity_type": "Trail",
    "name_raw": "Clary Boulee McDonald Preserve — Wetland Loop Trail",
    "counties_raw": ["Seneca"],
    "county_primary": "Seneca",
    "ownership_raw": SCPD_OWN,
    "governance_raw": SCPD_GOV,
    "partner_agencies_raw": None,
    "coordination_raw": None,
    "gps_lat_raw": None,
    "gps_lon_raw": None,
    "location_raw": "Clary Boulee McDonald Preserve, north entrance, Kansas OH 44841",
    "acres_raw": None,
    "description_raw": None,
    "features_raw": None,
    "difficulty_raw": None,
    "accessibility_raw": None,
    "urls_raw": [
        "https://www.blackswampconservancy.org/preserves/clary-boulee-mcdonald-preserve",
        "https://www.senecacountyparks.com/places/clary-boulee-mcdonald-preserve",
    ],
    "identity_notes_raw": (
        "No official trail name found — name_raw is descriptive. "
        "BSC website describes as 'the one-mile trail [that] winds through lush wetland habitats.' "
        "Loop trail beginning at north entrance of preserve. Approximate length: 1.0 mile. "
        "LATE T3 DISCOVERY — confirmed during T7 review."
    ),
    "township_raw": None,
    "municipality_raw": None,
    "discovery_tier": 3,
    "seeded_from_baseline": False,
    "baseline_id": None,
}

clary_boulee_trail_h2ohio = {
    "entity_type": "Trail",
    "name_raw": "Clary Boulee McDonald Preserve — H2Ohio Loop Trail",
    "counties_raw": ["Seneca"],
    "county_primary": "Seneca",
    "ownership_raw": SCPD_OWN,
    "governance_raw": SCPD_GOV,
    "partner_agencies_raw": None,
    "coordination_raw": None,
    "gps_lat_raw": None,
    "gps_lon_raw": None,
    "location_raw": "Clary Boulee McDonald Preserve, north entrance, Kansas OH 44841",
    "acres_raw": None,
    "description_raw": None,
    "features_raw": None,
    "difficulty_raw": None,
    "accessibility_raw": None,
    "urls_raw": [
        "https://www.blackswampconservancy.org/preserves/clary-boulee-mcdonald-preserve",
        "https://www.senecacountyparks.com/places/clary-boulee-mcdonald-preserve",
    ],
    "identity_notes_raw": (
        "No official trail name found — name_raw is descriptive. "
        "BSC website describes as 'the shorter 0.4-mile trail [that] provides a quick and informative "
        "view of the H2Ohio-sponsored water quality project.' "
        "Loop trail beginning at north entrance of preserve. Approximate length: 0.4 mile. "
        "LATE T3 DISCOVERY — confirmed during T7 review."
    ),
    "township_raw": None,
    "municipality_raw": None,
    "discovery_tier": 3,
    "seeded_from_baseline": False,
    "baseline_id": None,
}

data["records"].append(clary_boulee_site)
data["records"].append(clary_boulee_trail_1mile)
data["records"].append(clary_boulee_trail_h2ohio)

# Update T3 deferred null block to reflect resolution
for nb in data["tier_nulls"]:
    if (nb.get("tier") == 3
            and "Clary Boulee" in nb.get("governance_level", "")
            and nb.get("result") == "deferred_to_tier_7"):
        nb["result"] = "deferred_to_tier_7 — RESOLVED: ownership confirmed transferred to SCPD during T7 review; staged as 3 T3 entities (1 Site + 2 Trails)"
        nb["sources_checked"].append(
            "https://www.blackswampconservancy.org/preserves/clary-boulee-mcdonald-preserve (BSC confirms SCPD now owns)"
        )

f.write_text(yaml.dump(data, allow_unicode=True, sort_keys=False), encoding="utf-8")
print(f"Staged 3 late-T3 Clary Boulee McDonald entities (1 Site + 2 Trails).")
print(f"Total records: {len(data['records'])}, current_tier: {data['current_tier']}")
print(f"Total tier_nulls: {len(data['tier_nulls'])}")
