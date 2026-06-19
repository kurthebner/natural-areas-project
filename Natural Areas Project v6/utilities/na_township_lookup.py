#!/usr/bin/env python3
"""
na_township_lookup.py — Natural Areas Project Township Lookup Utility
Point-in-polygon derivation of civil township and incorporated municipality
from US Census TIGER/Line 2024 County Subdivisions (COUSUB) shapefile.
v1.2  —  2026-03-21

Zero external dependencies — uses Python stdlib only (struct, zipfile, io).

Shapefile source:
    US Census TIGER/Line 2024 County Subdivisions (COUSUB)
    Ohio state file: GIS_Assets/ohio_townships/tl_2024_39_cousub.zip
    Download from:
      https://www2.census.gov/geo/tiger/TIGER2024/COUSUB/tl_2024_39_cousub.zip

Two lookup modes:
    get_township(lat, lon)      → civil township only (CLASSFP="T1")
    get_municipality(lat, lon)  → best incorporated place or township

Usage:
    from utilities.na_township_lookup import OhioTownshipLookup
    lookup = OhioTownshipLookup()
    twp  = lookup.get_township(39.947, -83.012)      # → "Franklin"
    muni = lookup.get_municipality(40.020, -83.075)  # → "Upper Arlington"
    muni = lookup.get_municipality(39.947, -83.012)  # → "Columbus"

Township naming note:
    TIGER NAME field contains bare township names without "Township" suffix
    (e.g., "Franklin", "Jefferson", "Sharon"). If you want "Franklin Township"
    use get_township() and append " Township" in your calling code.

IMP-035: Resolves missing township lookup capability (Session 12, Franklin Co.)
"""

import io
import os
import struct
import zipfile
from pathlib import Path
from typing import List, Optional, Tuple

_GIS_DIR     = Path(__file__).parent.parent / "GIS_Assets" / "ohio_townships"
_DEFAULT_ZIP = _GIS_DIR / "tl_2024_39_cousub.zip"
_DEFAULT_SHP = _GIS_DIR / "tl_2024_39_cousub.shp"

_SHP_POLYGON = 5


# ---------------------------------------------------------------------------
# Minimal SHP reader
# ---------------------------------------------------------------------------

def _read_shp_records(data: bytes) -> List[Tuple[List[List[Tuple[float,float]]], Tuple]]:
    records = []
    offset = 100
    while offset < len(data):
        if offset + 8 > len(data):
            break
        content_len = struct.unpack_from('>i', data, offset + 4)[0] * 2
        offset += 8
        if offset + content_len > len(data):
            break
        shape_type = struct.unpack_from('<i', data, offset)[0]
        if shape_type == _SHP_POLYGON:
            xmin, ymin, xmax, ymax = struct.unpack_from('<4d', data, offset + 4)
            num_parts  = struct.unpack_from('<i', data, offset + 36)[0]
            num_points = struct.unpack_from('<i', data, offset + 40)[0]
            part_starts = list(struct.unpack_from(f'<{num_parts}i', data, offset + 44))
            part_starts.append(num_points)
            pts_offset = offset + 44 + num_parts * 4
            all_pts = []
            for i in range(num_points):
                x, y = struct.unpack_from('<2d', data, pts_offset + i * 16)
                all_pts.append((x, y))
            parts = [all_pts[part_starts[i]:part_starts[i+1]] for i in range(num_parts)]
            records.append((parts, (xmin, ymin, xmax, ymax)))
        else:
            records.append(([], (0, 0, 0, 0)))
        offset += content_len
    return records


# ---------------------------------------------------------------------------
# Minimal DBF reader  (reads NAME + CLASSFP fields)
# ---------------------------------------------------------------------------

def _read_dbf_attrs(data: bytes) -> List[Tuple[str, str]]:
    """Return list of (name, classfp) for each record."""
    num_records = struct.unpack_from('<I', data, 4)[0]
    header_size = struct.unpack_from('<H', data, 8)[0]
    record_size = struct.unpack_from('<H', data, 10)[0]

    fields = []
    offset = 32
    while data[offset] != 0x0D:
        fname = data[offset:offset+11].rstrip(b'\x00').decode('ascii', errors='replace')
        flen  = data[offset+16]
        fields.append((fname, flen))
        offset += 32

    # Locate NAME and CLASSFP field offsets within a record
    def find_field(target: str):
        col_off = 1
        for fname, flen in fields:
            if fname.upper() == target:
                return col_off, flen
            col_off += flen
        return None, 0

    name_start, name_len   = find_field('NAME')
    class_start, class_len = find_field('CLASSFP')

    attrs = []
    rec_offset = header_size
    for _ in range(num_records):
        name  = data[rec_offset+name_start  : rec_offset+name_start +name_len ].decode('latin-1','replace').strip() if name_start  else ''
        classfp = data[rec_offset+class_start: rec_offset+class_start+class_len].decode('latin-1','replace').strip() if class_start else ''
        attrs.append((name, classfp))
        rec_offset += record_size

    return attrs


# ---------------------------------------------------------------------------
# Ray casting point-in-polygon
# ---------------------------------------------------------------------------

def _point_in_ring(x: float, y: float, ring: List[Tuple[float,float]]) -> bool:
    inside = False
    n = len(ring)
    j = n - 1
    for i in range(n):
        xi, yi = ring[i]
        xj, yj = ring[j]
        if ((yi > y) != (yj > y)) and (x < (xj-xi)*(y-yi)/(yj-yi) + xi):
            inside = not inside
        j = i
    return inside


def _point_in_polygon(lon, lat, parts, bbox) -> bool:
    xmin, ymin, xmax, ymax = bbox
    if not (xmin <= lon <= xmax and ymin <= lat <= ymax):
        return False
    count = sum(1 for ring in parts if _point_in_ring(lon, lat, ring))
    return count % 2 == 1


# ---------------------------------------------------------------------------
# Main lookup class
# ---------------------------------------------------------------------------

class OhioTownshipLookup:
    """
    Loads Ohio MCD polygons once; supports township and municipality lookups.

    Two index lists are maintained:
        _townships    — CLASSFP="T1"  (civil townships only)
        _all_entries  — all records (cities, villages, townships)

    Cities and villages are prioritized over townships in get_municipality().
    """

    def __init__(self, shapefile_path: Optional[str] = None):
        if shapefile_path is None:
            if _DEFAULT_ZIP.exists():
                shapefile_path = str(_DEFAULT_ZIP)
            elif _DEFAULT_SHP.exists():
                shapefile_path = str(_DEFAULT_SHP)
            else:
                raise FileNotFoundError(
                    f"Ohio township shapefile not found.\n"
                    f"Expected: {_DEFAULT_ZIP}\n"
                    "Download tl_2024_39_cousub.zip from:\n"
                    "  https://www2.census.gov/geo/tiger/TIGER2024/COUSUB/"
                )

        # (parts, bbox, name, classfp)
        self._townships:   List[Tuple] = []   # CLASSFP == "T1"
        self._nontwp:      List[Tuple] = []   # cities, villages, etc.
        self._all_entries: List[Tuple] = []

        self._load(shapefile_path)

    def _load(self, path: str):
        path = str(path)
        if path.lower().endswith('.zip'):
            with zipfile.ZipFile(path) as zf:
                nl = zf.namelist()
                shp_data = zf.read(next(n for n in nl if n.lower().endswith('.shp')))
                dbf_data = zf.read(next(n for n in nl if n.lower().endswith('.dbf')))
        else:
            with open(path, 'rb') as f:
                shp_data = f.read()
            with open(path[:-4]+'.dbf', 'rb') as f:
                dbf_data = f.read()

        records = _read_shp_records(shp_data)
        attrs   = _read_dbf_attrs(dbf_data)
        n       = min(len(records), len(attrs))

        twp_count = 0
        for i in range(n):
            parts, bbox = records[i]
            if not parts:
                continue
            name, classfp = attrs[i]
            entry = (parts, bbox, name, classfp)
            self._all_entries.append(entry)
            if classfp == 'T1':
                self._townships.append(entry)
                twp_count += 1
            else:
                self._nontwp.append(entry)

        print(f"[na_township_lookup] Loaded {len(self._all_entries)} Ohio MCDs "
              f"({twp_count} townships, {len(self._nontwp)} cities/villages)")

    # ------------------------------------------------------------------

    def get_township(self, lat: float, lon: float) -> Optional[str]:
        """
        Return the CIVIL TOWNSHIP name for (lat, lon), or None.
        Only checks CLASSFP="T1" records.

        The returned name is the bare NAME field (e.g. "Franklin", "Jefferson").
        Callers may append " Township" as appropriate.
        """
        for parts, bbox, name, classfp in self._townships:
            if _point_in_polygon(lon, lat, parts, bbox):
                return name
        return None

    def get_municipality(self, lat: float, lon: float) -> Optional[str]:
        """
        Return the most specific incorporated place name (city or village)
        containing (lat, lon).  Falls back to township if no city/village found.
        """
        # Check non-township entries first (cities/villages)
        for parts, bbox, name, classfp in self._nontwp:
            if _point_in_polygon(lon, lat, parts, bbox):
                return name
        # Fall back to civil township
        return self.get_township(lat, lon)

    def get_both(self, lat: float, lon: float) -> Tuple[Optional[str], Optional[str]]:
        """
        Return (township, municipality) tuple.
        township   — civil township name (T1 class)
        municipality — city/village name, or same as township if no city found
        """
        township     = self.get_township(lat, lon)
        municipality = self.get_municipality(lat, lon)
        return township, municipality


# ---------------------------------------------------------------------------
# Self-test
# ---------------------------------------------------------------------------

def run_tests(lookup: Optional[OhioTownshipLookup] = None) -> bool:
    if lookup is None:
        lookup = OhioTownshipLookup()

    # (lat, lon, expected_twp_substr, expected_muni_substr, desc)
    # NOTE: In Ohio, incorporated cities leave their township, so get_township()
    # returns None for points inside incorporated cities.  This is correct.
    vectors = [
        # Columbus: incorporated city — no township; municipality = Columbus
        (39.9526, -83.0007, None,       "Columbus",        "Columbus city center"),
        # Upper Arlington: incorporated city — no township
        (40.020,  -83.075,  None,       "Upper Arlington", "Upper Arlington city"),
        # Bexley: incorporated city — no township
        (39.975,  -82.930,  None,       "Bexley",          "Bexley city"),
        # Liberty Township (unincorporated N Franklin County)
        (40.200,  -83.050,  "Liberty",  "Liberty",         "Liberty Township (unincorporated)"),
        # Westerville: incorporated city — no township
        (40.110,  -82.930,  None,       "Westerville",     "Westerville city"),
    ]

    print("na_township_lookup.py — self-test")
    print("-" * 70)
    passed = 0
    for lat, lon, exp_twp, exp_muni, desc in vectors:
        twp, muni = lookup.get_both(lat, lon)
        ok_twp  = (exp_twp  is None) or (twp  is not None and exp_twp.lower()  in twp.lower())
        ok_muni = (exp_muni is None) or (muni is not None and exp_muni.lower() in muni.lower())
        ok = ok_twp and ok_muni
        status = "PASS" if ok else "FAIL"
        print(f"  [{status}] ({lat:.3f},{lon:.4f}) twp='{twp}' muni='{muni}'")
        print(f"          expected twp~'{exp_twp}' muni~'{exp_muni}'  — {desc}")
        if ok:
            passed += 1

    print("-" * 70)
    print(f"  {passed}/{len(vectors)} passed")
    return passed == len(vectors)


if __name__ == "__main__":
    import sys
    try:
        ok = run_tests()
        sys.exit(0 if ok else 1)
    except FileNotFoundError as e:
        print(f"ERROR: {e}")
        sys.exit(2)
