"""
utilities/update_gps_coordinates.py
GPS re-acquisition pass — writes acquired coordinates into raw discovery YAMLs.
Covers all 48 gps_missing entities: 44 Sandusky + 4 Paulding.
Run once; re-run is idempotent (overwrites same values).
"""
import sys
import yaml
import pathlib

# IMP-128: Windows console UTF-8 fix — prevents UnicodeEncodeError on → and em dashes
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

PROJECT_ROOT = pathlib.Path(__file__).parent.parent

# ---------------------------------------------------------------------------
# Sandusky GPS map  (name_raw → (lat, lon))
# Confidence notes embedded in comments; approximate entries flagged.
# ---------------------------------------------------------------------------
SAN_GPS_BY_NAME = {
    # Access Points
    "Pickerel Creek Wildlife Area - SR 6 Observation Deck": (41.40992, -82.94858),   # MEDIUM - manual estimate
    "North Coast Inland Trail - Mosser Park Access":        (41.3670099, -83.1518776),

    # State/ODNR
    "Aldrich Pond Wildlife Area":    (41.4490345, -83.252608),

    # SCPD reserves (approximate — road/area geocoding, no public GPS)
    "Green Creek Township & Reserve": (41.2727011, -83.0083963),  # APPROX CR 195
    "Muddy Creek Reserve":            (41.4572304, -83.0912877),  # APPROX CR 157
    "Shelley Wetland":                (41.2724467, -82.8980809),  # APPROX CR 292

    # FC/private parks
    "Ringneck Ridge":                     (41.3912939, -83.2800276),
    "White Star Barn and Historical Cabins": (41.3674803, -83.3173664),
    "Doug Haubert Wetland":              (41.3755979, -83.3018001),

    # Municipal parks
    "Conner Park":              (41.3121019, -83.1302356),
    "Chudzinski-Johannsen Park": (41.3090819, -83.1537715),
    "Sandusky Township Park":   (41.3778773, -83.1349355),
    "Amsden Park":              (41.2657527, -82.8572347),
    "Buckingham Park":          (41.2657239, -82.8469607),
    "Robert Peters Athletic Field": (41.2795082, -82.8459942),
    "Paden Park":               (41.3007012, -82.9801118),
    "Central Park":             (41.3832823, -83.3228757),
    "H.W. Busdiecker Park":     (41.4490322, -83.3595781),
    "Veterans Park":            (41.451426,  -83.362528),

    # Golf courses
    "Sycamore Hills Golf Club": (41.3427842, -83.185926),
    "Hidden Hills Golf Club":   (41.4794468, -83.3971739),

    # Cemeteries — surveyed/GeoNames/Nominatim
    "Smith Cemetery":           (41.28893,   -83.25443),   # GeoNames 5172269
    "Briar Hill Cemetery":      (41.41046,   -83.09477),   # GeoNames 5148206 ("Brier Hill")
    "Greenwood Cemetery":       (41.4287128, -83.1058393), # Nominatim
    "Hineline Cemetery":        (41.4335923, -83.1739964), # Nominatim
    "Beeler Cemetery":          (41.3491876, -83.0169166), # Nominatim
    "Green Creek Burial Ground": (41.4048813, -83.0212801),
    "Four Mile House Cemetery": (41.3654574, -83.175762),  # 880 4 Mile House Rd
    "Slates Cemetery":          (41.3531925, -83.1736943), # 551 4 Mile House Rd
    "Chestnut Grove Cemetery":  (41.3252637, -83.4169581), # Nominatim
    "Wickwyre Cemetery":        (41.32073,   -82.84998),   # GeoNames 5176772
    "Old Fremont Cemetery":     (41.3411305, -83.1217771), # Nominatim ("Whittlesey")
    "Saint Ann's Cemetery":     (41.3307777, -83.1302880), # Nominatim
    "Saint Joseph's Cemetery":  (41.3333868, -83.1299223), # Nominatim
    "Saint Mary's Cemetery":    (41.3060134, -82.9806959), # Nominatim
    "Saint Paul's Cemetery":    (41.4324329, -83.1731984), # Nominatim

    # Cemeteries — calculated/approximate
    "LaPrairie Cemetery":       (41.413,   -83.098),   # APPROX SR53+CR129 intersection
    "Faith Lutheran Cemetery":  (41.403,   -83.174),   # APPROX CR128 4.1mi N of US20
    "Parkhurst Cemetery":       (41.34,    -82.90),    # APPROX SR101 Townsend Twp
    "Sugar Creek Cemetery":     (41.453,   -83.326),   # APPROX US20 2mi E of Woodville
    "Green Creek Township Cemetery (unconfirmed)": (41.2926942, -83.0131206),  # APPROX Twp center — UNCONFIRMED entity

    # Trails
    "Waggoner's Run Mountain Bike Trail": (41.3674803, -83.3173664),
    "Silver Rock Park Walking Trail":     (41.3958358, -83.3379287),
}

# Special case: two YAML records share name_raw "Woodville Cemetery"
# OH-SAN-S-055 is the Woodville Township record at index [64]
WOODVILLE_CEMETERY_INDEX = 64
WOODVILLE_CEMETERY_GPS = (41.4633939, -83.3620929)

# ---------------------------------------------------------------------------
# Paulding GPS map  (name_raw → (lat, lon))
# ---------------------------------------------------------------------------
PAU_GPS_BY_NAME = {
    "Lake Wayne R. Carr Wildlife Area":  (41.1580269, -84.7863068),  # 12525 Rd 11 Antwerp OH
    "Guilda H. Culler Memorial Park":    (41.2159711, -84.6269824),  # APPROX Crane Twp centroid
    "Flat Rock Creek Nature Preserve":   (41.1077358, -84.6586975),  # eBird hotspot L4718683
    "Viall's Lock Campsite":             (41.1625559, -84.4516157),  # Road 163 approximate
}

# ---------------------------------------------------------------------------
# Helper
# ---------------------------------------------------------------------------
def update_yaml(yaml_path: pathlib.Path, records_key: str, gps_by_name: dict,
                special_index: int | None = None, special_gps: tuple | None = None,
                special_name: str | None = None):
    text = yaml_path.read_text(encoding="utf-8")
    data = yaml.safe_load(text)
    records = data[records_key]

    updated = 0
    skipped_missing = []

    for name_raw, (lat, lon) in gps_by_name.items():
        matched = [i for i, r in enumerate(records) if r.get("name_raw") == name_raw]
        if not matched:
            skipped_missing.append(name_raw)
            continue
        if len(matched) > 1:
            print(f"  WARNING: {len(matched)} records match '{name_raw}' — skipping (use index override)")
            continue
        idx = matched[0]
        records[idx]["gps_lat_raw"] = lat
        records[idx]["gps_lon_raw"] = lon
        updated += 1

    # Special-case index override for duplicate names
    if special_index is not None and special_gps is not None:
        records[special_index]["gps_lat_raw"] = special_gps[0]
        records[special_index]["gps_lon_raw"] = special_gps[1]
        updated += 1
        print(f"  Special-case index [{special_index}] '{special_name}': {special_gps}")

    yaml_path.write_text(yaml.dump(data, allow_unicode=True, sort_keys=False), encoding="utf-8")
    print(f"  Updated {updated} records")
    if skipped_missing:
        print(f"  NOT FOUND in YAML: {skipped_missing}")
    return updated


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    print("=== GPS coordinate write-back ===\n")

    # --- Sandusky ---
    san_yaml = PROJECT_ROOT / "County_Spreadsheets/Sandusky/sandusky_ohio_raw_discovery.yaml"
    print(f"Sandusky YAML: {san_yaml}")
    san_updated = update_yaml(
        yaml_path=san_yaml,
        records_key="records",
        gps_by_name=SAN_GPS_BY_NAME,
        special_index=WOODVILLE_CEMETERY_INDEX,
        special_gps=WOODVILLE_CEMETERY_GPS,
        special_name="Woodville Cemetery (index 64, OH-SAN-S-055)",
    )

    # --- Paulding ---
    pau_yaml = PROJECT_ROOT / "County_Spreadsheets/Paulding/paulding_oh_raw_discovery.yaml"
    print(f"\nPaulding YAML: {pau_yaml}")
    pau_updated = update_yaml(
        yaml_path=pau_yaml,
        records_key="entities",
        gps_by_name=PAU_GPS_BY_NAME,
    )

    print(f"\nTotal records updated: {san_updated + pau_updated}")

    # --- Verification: read back and confirm ---
    print("\n=== Verification (spot-check) ===")
    san_data = yaml.safe_load(san_yaml.read_text(encoding="utf-8"))
    for r in san_data["records"]:
        if r.get("name_raw") in ("Aldrich Pond Wildlife Area", "Wickwyre Cemetery",
                                 "Waggoner's Run Mountain Bike Trail"):
            print(f"  SAN [{r['name_raw']}]: {r.get('gps_lat_raw')}, {r.get('gps_lon_raw')}")
    # Woodville at index 64
    wv = san_data["records"][64]
    print(f"  SAN [Woodville idx=64]: {wv['name_raw']} → {wv.get('gps_lat_raw')}, {wv.get('gps_lon_raw')}")
    wv110 = san_data["records"][110]
    print(f"  SAN [Woodville idx=110]: {wv110['name_raw']} → {wv110.get('gps_lat_raw')}, {wv110.get('gps_lon_raw')} (should be untouched)")

    pau_data = yaml.safe_load(pau_yaml.read_text(encoding="utf-8"))
    for r in pau_data["entities"]:
        if r.get("name_raw") in PAU_GPS_BY_NAME:
            print(f"  PAU [{r['name_raw']}]: {r.get('gps_lat_raw')}, {r.get('gps_lon_raw')}")


if __name__ == "__main__":
    main()
