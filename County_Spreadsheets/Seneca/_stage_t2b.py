import yaml, pathlib

f = pathlib.Path(r"D:\users\user1\Documents\CP Projects\Natural Areas Project v5\County_Spreadsheets\Seneca\seneca_ohio_raw_discovery.yaml")
data = yaml.safe_load(f.read_text(encoding="utf-8"))
data.setdefault("records", [])

wma_records = []
for n in range(1, 5):
    wma_records.append({
        "entity_type": "Site",
        "name_raw": f"Seneca County Wildlife Area {n}",
        "counties_raw": ["Seneca"],
        "county_primary": "Seneca",
        "ownership_raw": "Ohio Department of Natural Resources (ODNR) — Division of Wildlife",
        "governance_raw": "Ohio Department of Natural Resources (ODNR) — Division of Wildlife",
        "partner_agencies_raw": None,
        "coordination_raw": None,
        "gps_lat_raw": None,
        "gps_lon_raw": None,
        "location_raw": None,
        "acres_raw": None,
        "description_raw": None,
        "features_raw": ["Public hunting"],
        "difficulty_raw": None,
        "accessibility_raw": None,
        "urls_raw": ["https://codes.ohio.gov/ohio-administrative-code/rule-1501:31-15-04"],
        "identity_notes_raw": (
            f"Confirmed as public hunting area via Ohio Administrative Code Rule 1501:31-15-04 "
            f"(state-owned lands designated as public hunting areas, Division of Wildlife section). "
            f"No GPS, acreage, or exact parcel address found from web sources. "
            f"Distinct from named wildlife areas (Sugar Creek, Knobbys Prairie, Silver Creek). "
            f"Location and acreage unknown — GPS acquisition required."
        ),
        "township_raw": None,
        "municipality_raw": None,
        "discovery_tier": 2,
        "seeded_from_baseline": True,
        "baseline_id": f"Seneca County Wildlife Area {n}",
    })

for r in wma_records:
    data["records"].append(r)

f.write_text(yaml.dump(data, allow_unicode=True, sort_keys=False), encoding="utf-8")
print(f"Staged {len(wma_records)} Wildlife Area records. Total records now: {len(data['records'])}")
