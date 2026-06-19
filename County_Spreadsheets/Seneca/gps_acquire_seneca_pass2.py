#!/usr/bin/env python3
"""
Seneca County GPS Acquisition — Pass 2
Targeted cleanup for 34 unresolved sites + one suspect LOW-confidence result.
Also assigns confirmed manual coordinates for Knobbys Prairie WA and Seneca Caverns.

Tighter county bounds used (actual Seneca County TIGER extents):
  Lat: 40.90–41.25°N  |  Lon: 83.42–82.85°W

Run from project root:
  python "County_Spreadsheets/Seneca/gps_acquire_seneca_pass2.py"
"""
import sys, json, time, pathlib, re
import urllib.request, urllib.parse

sys.stdout.reconfigure(encoding='utf-8')

BASE        = pathlib.Path(r"D:\users\user1\Documents\CP Projects\Natural Areas Project v5")
CONFIG_PATH = BASE / "County_Spreadsheets/Seneca/seneca_ohio_pipeline_config.json"

# Tighter actual Seneca County bounding box (TIGER extents)
LAT_MIN, LAT_MAX = 40.90, 41.26
LON_MIN, LON_MAX = -83.43, -82.84

NOMINATIM_URL = "https://nominatim.openstreetmap.org/search"
USER_AGENT    = "NaturalAreasProject/5.0 (khebner@hotmail.com)"
DELAY         = 1.1


def in_bounds(lat, lon):
    return LAT_MIN <= lat <= LAT_MAX and LON_MIN <= lon <= LON_MAX


def nominatim_query(query_str):
    params = urllib.parse.urlencode({
        'q':            query_str,
        'format':       'json',
        'limit':        1,
        'countrycodes': 'us',
    })
    url = f"{NOMINATIM_URL}?{params}"
    req = urllib.request.Request(url, headers={'User-Agent': USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            if data:
                return float(data[0]['lat']), float(data[0]['lon'])
    except Exception as e:
        print(f"      [ERR] {e}")
    return None


# ---------------------------------------------------------------------------
# MANUAL / CONFIRMED COORDINATES (from authoritative web sources)
# Knobbys Prairie WA: birdinghotspots.org (eBird GNIS coordinates)
# Seneca Caverns: i-s-c-a.org confirmed cave coordinates
# ---------------------------------------------------------------------------
MANUAL_GPS = {
    "OH-SEN-S-004": (41.196737, -83.131825, "HIGH", "authoritative_page",
                     "birdinghotspots.org eBird hotspot L1915202 (GNIS)"),
    "OH-SEN-S-070": (41.225536, -82.875702, "MED",  "authoritative_page",
                     "International Show Caves Association i-s-c-a.org/show-cave/177"),
    # Rock Run Cemetery — clear the bad LOW-confidence result (40.82 is outside county)
    # Will be re-queried below or left unresolved
}

# ---------------------------------------------------------------------------
# TARGETED QUERY MAP for unresolved sites
# Cleaner queries than the default gps_queries dict
# ---------------------------------------------------------------------------
TARGETED_QUERIES = {
    # ODNR T2 — intersection or place queries
    "OH-SEN-S-005": [
        "Township Road 48, Bloomville, Ohio 44818",
        "Silver Creek Wildlife Area, Bloomville, Ohio",
        "Township Road 181, Bloomville, Ohio 44818",
    ],
    # SCPD T3
    "OH-SEN-S-010": [
        "11891 County Road 24, Republic, Ohio 44867",
        "Bowen Nature Preserve, Republic, Ohio",
        "County Road 24, Republic, Ohio 44867",
    ],
    "OH-SEN-S-020": [
        "2320 W County Road 6, Tiffin, Ohio 44883",
        "St Johns Mill, Tiffin, Ohio",
        "County Road 6, Tiffin, Ohio 44883",
    ],
    "OH-SEN-S-060": [
        "4747 W State Route 12, Kansas, Ohio 44841",
        "Clary Boulee McDonald Preserve, Seneca County, Ohio",
        "State Route 12, Kansas, Ohio 44841",
    ],
    # T3 governance-uncertain
    "OH-SEN-S-021": [
        "7461 N Township Road 70, Tiffin, Ohio 44883",
        "HP Eells Park, Bettsville, Ohio",
        "Bettsville, Ohio 44815",
    ],
    # T5 cemeteries — intersection/road queries
    "OH-SEN-S-024": [
        "Disinger Cemetery, Jackson Township, Seneca County, Ohio",
        "County Road 25, Jackson Township, Ohio",
    ],
    "OH-SEN-S-026": [
        "Attica-Venice Joint Cemetery, Attica, Ohio 44807",
        "Cemetery, Venice Township, Seneca County, Ohio",
        "Attica, Ohio 44807",
    ],
    "OH-SEN-S-029": [
        "Chenoweth Cemetery, Pleasant Township, Seneca County, Ohio",
        "Gay Road, Pleasant Township, Ohio",
    ],
    "OH-SEN-S-030": [
        "Gundy Cemetery, Pleasant Township, Seneca County, Ohio",
        "Norton Road, Pleasant Township, Ohio",
    ],
    "OH-SEN-S-031": [
        "Ebenezer ME Cemetery, Pleasant Township, Seneca County, Ohio",
        "Johnson Road, Pleasant Township, Ohio",
    ],
    "OH-SEN-S-032": [
        "Little Pennsylvania Cemetery, Pleasant Township, Seneca County, Ohio",
        "State Route 665, Pleasant Township, Ohio",
    ],
    "OH-SEN-S-033": [
        "Oak Grove Cemetery, Pleasant Township, Seneca County, Ohio",
        "Alkire Road, Pleasant Township, Ohio",
    ],
    # T5 Rock Run Cemetery — clear bad result, retry with tighter query
    "OH-SEN-S-025": [
        "Rock Run Cemetery, Eden Township, Seneca County, Ohio",
        "Rock Run Cemetery, Seneca County, Ohio",
    ],
    # T6 Tiffin parks
    "OH-SEN-S-036": [
        "8th Avenue, Tiffin, Ohio 44883",
        "N Washington Street, Tiffin, Ohio 44883",
    ],
    "OH-SEN-S-041": [
        "432 Jackson Street, Tiffin, Ohio 44883",
        "Jackson Street, Tiffin, Ohio 44883",
    ],
    "OH-SEN-S-043": [
        "State Route 101, Tiffin, Ohio 44883",
        "Tiffin East Park, Tiffin, Ohio",
    ],
    "OH-SEN-S-044": [
        "Frost Parkway, Tiffin, Ohio 44883",
        "Rotary Park, Tiffin, Ohio",
    ],
    "OH-SEN-S-045": [
        "Ohio Avenue, Tiffin, Ohio 44883",
        "Clinton Avenue, Tiffin, Ohio 44883",
    ],
    "OH-SEN-S-048": [
        "Lions Club Park, Tiffin, Ohio",
        "City of Tiffin Annex, Tiffin, Ohio 44883",
    ],
    "OH-SEN-S-049": [
        "22 S Washington Street, Tiffin, Ohio 44883",
        "S Washington Street, Tiffin, Ohio 44883",
    ],
    # T6 village parks
    "OH-SEN-S-058": [
        "Beeghly Park, Bloomville, Ohio 44818",
        "Bloomville, Ohio 44818",
    ],
    "OH-SEN-S-059": [
        "13 Near West Street, New Riegel, Ohio 44853",
        "Near West Street, New Riegel, Ohio",
        "New Riegel, Ohio 44853",
    ],
    # T8 golf
    "OH-SEN-S-066": [
        "3770 County Road 23, Fostoria, Ohio 44830",
        "Lakeland Golf Course, Fostoria, Ohio",
    ],
    "OH-SEN-S-068": [
        "4399 S State Route 231, Tiffin, Ohio 44883",
        "Mohawk Golf Country Club, Tiffin, Ohio",
    ],
    "OH-SEN-S-069": [
        "4044 W Township Road 98, Tiffin, Ohio 44883",
        "Seneca Hills Golf Course, Tiffin, Ohio",
    ],
    # T8 private — has addresses
    "OH-SEN-S-071": [
        "8877 S Township Road 131, McCutchenville, Ohio 44844",
        "Camp Pittenger, McCutchenville, Ohio",
        "Township Road 131, McCutchenville, Ohio 44844",
    ],
    "OH-SEN-S-142": [
        "6580 S Township Road 131, Tiffin, Ohio 44883",
        "Camp Glen, Tiffin, Ohio",
        "Township Road 131, Tiffin, Ohio 44883",
    ],
    # OGE duplicate cemeteries — no distinct location data; use parent proximity only
    "OH-SEN-S-086": [
        "Reformed Cemetery, Seneca County, Ohio",
    ],
    "OH-SEN-S-134": [
        "Rock Creek Cemetery, Tiffin, Ohio",
        "Rock Creek Cemetery, Seneca County, Ohio",
    ],
}


def try_queries(queries):
    """Try a list of queries in order; return first in-bounds result."""
    for q in queries:
        r = nominatim_query(q)
        time.sleep(DELAY)
        if r and in_bounds(*r):
            return r[0], r[1], q
    return None, None, None


def main():
    config = json.loads(CONFIG_PATH.read_text(encoding='utf-8'))
    sites  = config['sites']
    trails = config['trails']
    id_map = {s['site_id']: s for s in sites}

    fixed   = 0
    cleared = 0

    # -- 1. Clear bad Rock Run Cemetery GPS (40.82 is south of Seneca County) --
    rrc = id_map.get("OH-SEN-S-025")
    if rrc and rrc.get("gps_lat") and rrc["gps_lat"] < LAT_MIN:
        print(f"Clearing bad GPS for Rock Run Cemetery: ({rrc['gps_lat']}, {rrc['gps_lon']}) — outside county")
        rrc["gps_lat"]        = None
        rrc["gps_lon"]        = None
        rrc["gps_confidence"] = None
        cleared += 1

    # -- 2. Apply manual confirmed coordinates --
    print("\nApplying manual/confirmed GPS…")
    for sid, (lat, lon, conf, method, source) in MANUAL_GPS.items():
        s = id_map.get(sid)
        if s and s.get("gps_lat") is None:
            s["gps_lat"]        = lat
            s["gps_lon"]        = lon
            s["gps_confidence"] = conf
            print(f"  {sid}  {s['name'][:42]} → {lat:.5f}, {lon:.5f} [{conf}] ({method})")
            fixed += 1

    # -- 3. Targeted Nominatim queries --
    print("\nRunning targeted queries…")
    all_target_ids = (
        list(TARGETED_QUERIES.keys()) +
        (["OH-SEN-S-025"] if id_map.get("OH-SEN-S-025", {}).get("gps_lat") is None else [])
    )

    for sid in all_target_ids:
        s = id_map.get(sid)
        if s is None:
            continue
        if s.get("gps_lat") is not None:
            continue  # already has GPS
        queries = TARGETED_QUERIES.get(sid, [f"{s['name']}, Seneca County, Ohio"])
        lat, lon, used_q = try_queries(queries)
        if lat is not None:
            s["gps_lat"]        = round(lat, 6)
            s["gps_lon"]        = round(lon, 6)
            s["gps_confidence"] = "MED"
            fixed += 1
            print(f"  {sid}  {s['name'][:42]} → {lat:.5f}, {lon:.5f}  q='{used_q[:60]}'")
        else:
            print(f"  {sid}  {s['name'][:42]} → STILL UNRESOLVED")

    # -- 4. Try Nominatim for ODNR WA 2-4 (no address) --
    print("\nTrying ODNR WA 2-4 by number+county…")
    for sid in ["OH-SEN-S-006", "OH-SEN-S-007", "OH-SEN-S-008", "OH-SEN-S-009"]:
        s = id_map.get(sid)
        if s and s.get("gps_lat") is None:
            # Generic fallback queries for unnamed ODNR parcels
            queries = [
                f"{s['name']}, Seneca County, Ohio",
                f"ODNR Wildlife Area, Seneca County, Ohio",
            ]
            lat, lon, used_q = try_queries(queries)
            if lat is not None:
                s["gps_lat"] = round(lat, 6)
                s["gps_lon"] = round(lon, 6)
                s["gps_confidence"] = "LOW"
                fixed += 1
                print(f"  {sid}  {s['name'][:42]} → {lat:.5f}, {lon:.5f} [LOW]")
            else:
                print(f"  {sid}  {s['name'][:42]} → STILL UNRESOLVED (unnamed parcels)")

    # -- 5. Trail GPS --
    print("\nTrail GPS pass…")
    tid_map = {t.get('trail_id', ''): t for t in trails}
    trail_queries = {
        "OH-SEN-T-002": ["Rock Creek Trail, Tiffin, Ohio", "Rock Creek Trail, Seneca County, Ohio"],
        "OH-SEN-T-003": ["4747 W State Route 12, Kansas, Ohio 44841",
                          "Clary Boulee McDonald Preserve, Seneca County, Ohio"],
        "OH-SEN-T-004": ["4747 W State Route 12, Kansas, Ohio 44841",
                          "Clary Boulee McDonald Preserve, Seneca County, Ohio"],
    }
    for tid, queries in trail_queries.items():
        t = tid_map.get(tid)
        if t and t.get('gps_lat') is None and not t.get('gps_unresolvable'):
            lat, lon, used_q = try_queries(queries)
            if lat is not None:
                t['gps_lat']        = round(lat, 6)
                t['gps_lon']        = round(lon, 6)
                t['gps_confidence'] = 'MED'
                print(f"  {tid}  {t['name'][:42]} → {lat:.5f}, {lon:.5f}")
            else:
                print(f"  {tid}  {t['name'][:42]} → UNRESOLVED")

    # -- Save --
    CONFIG_PATH.write_text(
        json.dumps(config, indent=2, ensure_ascii=False), encoding='utf-8')

    # Summary
    total = len(sites)
    with_gps = sum(1 for s in sites if s.get('gps_lat') is not None)
    still_unresolved = [s for s in sites if s.get('gps_lat') is None]

    print(f"""
Pass 2 Summary
  Cleared (bad GPS):   {cleared}
  Newly acquired:      {fixed}
  Total with GPS:      {with_gps}/{total}  ({with_gps/total*100:.1f}%)
  Still unresolved:    {len(still_unresolved)}
""")

    if still_unresolved:
        print("Still unresolved after Pass 2:")
        for s in still_unresolved:
            print(f"  {s['site_id']}  {s['name']}")

    print(f"\nSaved → {CONFIG_PATH}")


if __name__ == '__main__':
    main()
