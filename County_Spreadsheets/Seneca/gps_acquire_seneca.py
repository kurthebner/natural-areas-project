#!/usr/bin/env python3
"""
Seneca County GPS Acquisition Script — Stage 2b
Queries Nominatim (+ USGS GNIS fallback for cemeteries) for all sites without GPS.

County centroid: 41.09°N, 83.13°W  (Seneca County, Ohio)
Bounding box:  ±0.35° (~25–30 mi) per IMP-081 §5.8
Nominatim delay: 1.1s between requests (usage policy)

Run from project root:
  python "County_Spreadsheets/Seneca/gps_acquire_seneca.py"
"""
import sys, json, time, pathlib, re
import urllib.request, urllib.parse, urllib.error

sys.stdout.reconfigure(encoding='utf-8')

BASE        = pathlib.Path(r"D:\users\user1\Documents\CP Projects\Natural Areas Project v5")
CONFIG_PATH = BASE / "County_Spreadsheets/Seneca/seneca_ohio_pipeline_config.json"

# Seneca County approximate centroid
COUNTY_CENTROID = (41.09, -83.13)
GPS_BUFFER      = 0.35          # degrees, ~25–30 mi in Ohio

NOMINATIM_URL = "https://nominatim.openstreetmap.org/search"
GNIS_URL      = "https://geonames.usgs.gov/api/fts/database/export"
USER_AGENT    = "NaturalAreasProject/5.0 (khebner@hotmail.com)"
DELAY         = 1.1             # seconds between Nominatim requests


# ---------------------------------------------------------------------------
# HELPERS
# ---------------------------------------------------------------------------
def within_county_bounds(lat, lon):
    clat, clon = COUNTY_CENTROID
    return (abs(lat - clat) <= GPS_BUFFER and abs(lon - clon) <= GPS_BUFFER)


def nominatim_query(query_str):
    """Query Nominatim; return (lat, lon) or None."""
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
        print(f"      [NOM ERR] {e}")
    return None


def fetch_gnis_cemeteries():
    """Fetch all GNIS cemetery records for Seneca County, OH.
    Returns dict: {name_lower: (lat, lon)}
    FIPS: Ohio=39, Seneca County=147 → county_numeric=147
    """
    params = urllib.parse.urlencode({
        'state_alpha':   'OH',
        'county_numeric': '147',
        'feature_class': 'Cemetery',
    })
    url = f"{GNIS_URL}?{params}"
    req = urllib.request.Request(url, headers={'User-Agent': USER_AGENT})
    result = {}
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            content = resp.read().decode('utf-8', errors='replace')
            # GNIS export is pipe-delimited text
            # Header line contains field names; data lines contain records
            lines = content.strip().splitlines()
            if not lines:
                return result
            # Find field indices
            header = lines[0].split('|')
            try:
                name_idx  = next(i for i, h in enumerate(header) if 'feature_name' in h.lower() or h.lower() == 'name')
                lat_idx   = next(i for i, h in enumerate(header) if 'prim_lat_dec' in h.lower() or 'lat' in h.lower())
                lon_idx   = next(i for i, h in enumerate(header) if 'prim_long_dec' in h.lower() or 'lon' in h.lower() or 'long' in h.lower())
            except StopIteration:
                print(f"    [GNIS] Unexpected header format: {header[:10]}")
                return result
            for line in lines[1:]:
                parts = line.split('|')
                if len(parts) <= max(name_idx, lat_idx, lon_idx):
                    continue
                try:
                    name  = parts[name_idx].strip()
                    lat   = float(parts[lat_idx].strip())
                    lon   = float(parts[lon_idx].strip())
                    result[name.lower()] = (lat, lon)
                except (ValueError, IndexError):
                    continue
        print(f"    [GNIS] Loaded {len(result)} cemetery records for Seneca County")
    except Exception as e:
        print(f"    [GNIS ERR] {e}")
    return result


def try_nominatim_with_fallbacks(site_name, primary_query):
    """Try primary query, then IMP-081 fallback formats.
    Returns (lat, lon, confidence, used_query) or (None, None, None, None).
    """
    # Primary
    r = nominatim_query(primary_query)
    time.sleep(DELAY)
    if r and within_county_bounds(*r):
        return r[0], r[1], "MED", primary_query

    # Fallback 1: name + county
    fb1 = f"{site_name}, Seneca County, Ohio"
    if fb1 != primary_query:
        r = nominatim_query(fb1)
        time.sleep(DELAY)
        if r and within_county_bounds(*r):
            return r[0], r[1], "MED", fb1

    # Fallback 2: name + Ohio only
    fb2 = f"{site_name}, Ohio"
    r = nominatim_query(fb2)
    time.sleep(DELAY)
    if r and within_county_bounds(*r):
        return r[0], r[1], "LOW", fb2

    return None, None, None, None


# ---------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------
def main():
    config     = json.loads(CONFIG_PATH.read_text(encoding='utf-8'))
    sites      = config['sites']
    trails     = config['trails']
    gps_queries = config.get('gps_queries', {})

    # ---- Fetch GNIS cemetery data for fallback ----
    print("Fetching GNIS cemetery data for Seneca County…")
    gnis_cems = fetch_gnis_cemeteries()

    total      = len(sites)
    acquired   = 0
    unresolved = 0
    from_raw   = 0
    from_gnis  = 0
    checkpoint_every = 25

    print(f"\nProcessing {total} sites…\n")

    for i, site in enumerate(sites):
        sid  = site['site_id']
        name = site['name']

        # Skip if GPS already set (from raw or prior pass)
        if site.get('gps_lat') is not None:
            from_raw += 1
            continue

        q = gps_queries.get(sid, f"{name}, Seneca County, Ohio")
        short_name = name[:42]
        print(f"  [{i+1:3d}/{total}] {sid}  {short_name}", flush=True)

        lat, lon, conf, used_q = None, None, None, None

        # For cemeteries, try GNIS first (authoritative, no rate-limit cost)
        if site.get('category') == 'Cemetery' and gnis_cems:
            gnis_key = name.lower()
            if gnis_key in gnis_cems:
                lat, lon = gnis_cems[gnis_key]
                if within_county_bounds(lat, lon):
                    conf   = "HIGH"
                    used_q = f"GNIS:{name}"
                    from_gnis += 1
                    print(f"          → GNIS  {lat:.5f}, {lon:.5f} [HIGH]")
                else:
                    lat, lon = None, None  # GNIS result outside bounds, fall through

        # Nominatim if not resolved by GNIS
        if lat is None:
            lat, lon, conf, used_q = try_nominatim_with_fallbacks(name, q)
            if lat is not None:
                print(f"          → NOM   {lat:.5f}, {lon:.5f} [{conf}]  q='{used_q[:50]}'")

        if lat is not None:
            site['gps_lat']        = round(lat, 6)
            site['gps_lon']        = round(lon, 6)
            site['gps_confidence'] = conf
            acquired += 1
        else:
            unresolved += 1
            print(f"          → UNRESOLVED")

        # Checkpoint save
        if (i + 1) % checkpoint_every == 0:
            CONFIG_PATH.write_text(
                json.dumps(config, indent=2, ensure_ascii=False), encoding='utf-8')
            print(f"  [checkpoint: {i+1} sites processed, {acquired} acquired so far]\n")

    # ---- Trails ----
    print("\nProcessing 4 trails…")
    for trail in trails:
        tid = trail.get('trail_id', '')
        n   = trail.get('name', '').lower()

        if 'sandusky' in n and 'scenic river' in n:
            # Linear water corridor — gps_unresolvable per §7.2
            trail['gps_unresolvable'] = True
            existing_notes = trail.get('notes', '')
            if 'GPS unresolvable' not in existing_notes:
                trail['notes'] = (
                    existing_notes.rstrip() +
                    ' GPS unresolvable: 65-mile linear water corridor; '
                    'no meaningful centroid. Determined 2026-05-28.'
                ).strip()
            print(f"  {tid}  {trail['name']} → gps_unresolvable (linear corridor)")
            continue

        if trail.get('gps_lat') is not None:
            print(f"  {tid}  {trail['name']} → already has GPS")
            continue

        q = gps_queries.get(tid, f"{trail['name']}, Seneca County, Ohio")
        r = nominatim_query(q)
        time.sleep(DELAY)
        if r and within_county_bounds(*r):
            trail['gps_lat']        = round(r[0], 6)
            trail['gps_lon']        = round(r[1], 6)
            trail['gps_confidence'] = 'MED'
            print(f"  {tid}  {trail['name']} → {r[0]:.5f}, {r[1]:.5f} [MED]")
        else:
            print(f"  {tid}  {trail['name']} → UNRESOLVED")

    # ---- Final save ----
    CONFIG_PATH.write_text(
        json.dumps(config, indent=2, ensure_ascii=False), encoding='utf-8')

    print(f"""
GPS Acquisition Summary
  Total sites:        {total}
  Already had GPS:    {from_raw}
  From GNIS:          {from_gnis}
  From Nominatim:     {acquired - from_gnis}
  Total acquired:     {acquired}
  Unresolved:         {unresolved}
  Resolution rate:    {(from_raw + acquired) / total * 100:.1f}%

Saved → {CONFIG_PATH}
""")

    if unresolved > 0:
        print("Unresolved sites (need manual GPS or gps_unresolvable flag):")
        for s in sites:
            if s.get('gps_lat') is None:
                print(f"  {s['site_id']}  {s['name']}")


if __name__ == '__main__':
    main()
