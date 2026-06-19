"""
na_gnis_query.py — GNIS Ohio statewide feature query utility

Source file: OH_Features_GNIS_20210825.txt (project root)
  - 2021 GNIS Ohio archive; 69,226 features; pipe-delimited
  - Current DomesticNames distribution (May 2026) lacks Cemetery/Park/Trail classes
  - Use this 2021 archive for all county discovery and GPS acquisition work

Relevant feature classes for Natural Areas Project:
  Park, Cemetery, Reservoir, Lake, Trail, Area, Forest, Swamp, Reserve,
  Woods, Summit, Spring, Falls, Cliff, Valley, Stream

Usage:
    from na_gnis_query import gnis_by_county

    # All parks and trails in Ottawa County
    features = gnis_by_county('Ottawa', ['Park', 'Trail'])
    for f in features:
        print(f['name'], f['lat'], f['lon'])

    # All natural-area-relevant features in a county
    features = gnis_by_county('Hardin', NAP_CLASSES)
"""

import pathlib
import sys

# Path to the GNIS source file (project root)
_PROJECT_ROOT = pathlib.Path(__file__).parent.parent
GNIS_FILE = _PROJECT_ROOT / 'OH_Features_GNIS_20210825.txt'

# Feature classes relevant to the Natural Areas Project
# (excludes Church, School, Building, Post Office, Airport, Hospital, Bridge, etc.)
NAP_CLASSES = {
    'Park',
    'Trail',
    'Area',
    'Forest',
    'Reserve',
    'Swamp',
    'Woods',
    'Cemetery',
    'Reservoir',
    'Lake',
    'Summit',
    'Spring',
    'Falls',
    'Cliff',
    'Valley',
    'Stream',
    'Island',
    'Bar',
    'Bay',
    'Cape',
    'Flat',
    'Ridge',
    'Mine',
    'Military',
}

# Column indices in the pipe-delimited file
_COL = {
    'feature_id':   0,
    'name':         1,
    'feature_class': 2,
    'state_alpha':  3,
    'county_name':  5,
    'map_name':     7,
    'lat':          9,
    'lon':          10,
}


def _load_file():
    """Load and return parsed GNIS lines (all Ohio features)."""
    if not GNIS_FILE.exists():
        raise FileNotFoundError(
            f'GNIS file not found: {GNIS_FILE}\n'
            'Expected at project root: OH_Features_GNIS_20210825.txt'
        )
    text = GNIS_FILE.read_text(encoding='utf-8-sig', errors='replace')
    lines = text.splitlines()
    return lines[1:]  # skip header


def gnis_by_county(county_name: str, feature_classes=None, include_no_coords: bool = False):
    """
    Return GNIS features for a given Ohio county.

    Args:
        county_name: County name as it appears in GNIS (e.g. 'Hardin', 'Ottawa').
                     Case-sensitive; matches the COUNTY_NAME column exactly.
        feature_classes: Collection of GNIS feature class strings to include.
                         None = all classes. Use NAP_CLASSES for natural-area-relevant only.
        include_no_coords: If False (default), exclude features with no lat/lon.

    Returns:
        List of dicts with keys: feature_id, name, feature_class, lat, lon, map_name
    """
    if feature_classes is not None:
        wanted = set(feature_classes)
    else:
        wanted = None

    results = []
    for line in _load_file():
        parts = line.split('|')
        if len(parts) <= 10:
            continue
        if parts[_COL['state_alpha']] != 'OH':
            continue
        if parts[_COL['county_name']] != county_name:
            continue
        fc = parts[_COL['feature_class']]
        if wanted is not None and fc not in wanted:
            continue

        lat_s = parts[_COL['lat']].strip()
        lon_s = parts[_COL['lon']].strip()
        try:
            lat = float(lat_s) if lat_s else None
            lon = float(lon_s) if lon_s else None
        except ValueError:
            lat = lon = None

        if not include_no_coords and (lat is None or lon is None):
            continue

        results.append({
            'feature_id':    parts[_COL['feature_id']].strip(),
            'name':          parts[_COL['name']].strip(),
            'feature_class': fc,
            'lat':           lat,
            'lon':           lon,
            'map_name':      parts[_COL['map_name']].strip(),
        })

    return results


def gnis_county_summary(county_name: str):
    """
    Print a count of all GNIS features by class for a county.
    Useful at the start of a county discovery run.
    """
    from collections import Counter
    all_features = gnis_by_county(county_name, feature_classes=None, include_no_coords=True)
    counts = Counter(f['feature_class'] for f in all_features)
    nap = gnis_by_county(county_name, feature_classes=NAP_CLASSES, include_no_coords=False)
    print(f'GNIS features for {county_name} County, Ohio (2021 archive):')
    print(f'  Total features: {len(all_features)}')
    print(f'  NAP-relevant features with GPS: {len(nap)}')
    print()
    print('  Feature class counts (all):')
    for cls, cnt in counts.most_common():
        marker = ' *' if cls in NAP_CLASSES else ''
        print(f'    {cls:<22} {cnt}{marker}')
    print()
    print('  (* = included in NAP_CLASSES)')
    return nap


def gnis_cemetery_gps(county_name: str):
    """
    Return all cemetery GPS coordinates for a county.
    Primary use case: GPS fill-forward for cemetery sites during Stage 4b.

    Returns list of dicts: {feature_id, name, lat, lon}
    """
    return gnis_by_county(county_name, feature_classes={'Cemetery'})


if __name__ == '__main__':
    # CLI: python na_gnis_query.py <CountyName> [ClassName ...]
    # Example: python na_gnis_query.py Hardin Park Trail
    # Example: python na_gnis_query.py Ottawa  (uses NAP_CLASSES)
    args = sys.argv[1:]
    if not args:
        print('Usage: na_gnis_query.py <CountyName> [ClassName ...]')
        print('       na_gnis_query.py Hardin            # NAP-relevant classes')
        print('       na_gnis_query.py Ottawa Park Trail Cemetery')
        sys.exit(0)

    county = args[0]
    classes = set(args[1:]) if len(args) > 1 else None

    if classes:
        features = gnis_by_county(county, classes)
        print(f'{county} County — {", ".join(sorted(classes))} ({len(features)} features with GPS):')
        for f in sorted(features, key=lambda x: x['name']):
            print(f'  {f["feature_id"]:<10} {f["name"]:<42} {f["feature_class"]:<12} {f["lat"]:.6f}, {f["lon"]:.6f}')
    else:
        gnis_county_summary(county)
