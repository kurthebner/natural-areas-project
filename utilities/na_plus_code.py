#!/usr/bin/env python3
"""
na_plus_code.py — Natural Areas Project Plus Code Utility
Open Location Code (OLC / Plus Code) encoder — v1.0
2026-03-21

Encodes WGS84 (lat, lon) decimal degrees to a 10-character Plus Code.

Usage (import):
    from utilities.na_plus_code import encode_plus_code
    code = encode_plus_code(39.947, -83.012)   # → "86FRWXWQ+R5"

Usage (standalone — runs self-test):
    python3 na_plus_code.py

Specification:
    https://github.com/google/open-location-code/blob/main/docs/olc_definition.adoc

Algorithm notes:
    - Five resolution steps, each consuming two digits (one lat, one lon).
    - PAIR_RESOLUTIONS = [20.0, 1.0, 0.05, 0.0025, 0.000125]
      (each step is 1/20 of the previous; lat/lon grids differ at step 0)
    - Separator '+' inserted after position 8 in the raw 10-digit code.
    - Latitude clamped to (-90, 90); longitude wrapped to (-180, 180].

IMP-032: This module resolves the inline Plus Code bug (resolution=400 → 20)
         discovered during Session 12 of the Franklin County pipeline run.
"""

CODE_ALPHABET = "23456789CFGHJMPQRVWX"
PAIR_RESOLUTIONS = [20.0, 1.0, 0.05, 0.0025, 0.000125]
SEPARATOR_POSITION = 8


def encode_plus_code(lat: float, lon: float) -> str:
    """
    Encode a WGS84 coordinate pair to a 10-character Plus Code.

    Args:
        lat: Latitude in decimal degrees (-90 to 90).
        lon: Longitude in decimal degrees (-180 to 180).

    Returns:
        10-character Plus Code string, e.g. "86FRWXWQ+R5".

    Raises:
        ValueError: If lat or lon cannot be converted to float.
    """
    lat = float(lat)
    lon = float(lon)

    # Clamp latitude; wrap longitude into [-180, 180)
    lat = max(-90.0, min(90.0 - 1e-10, lat))
    lon = ((lon + 180.0) % 360.0) - 180.0

    # Shift to positive coordinates
    adj_lat = lat + 90.0
    adj_lon = lon + 180.0

    digits = []
    for res in PAIR_RESOLUTIONS:
        lat_d = int(adj_lat / res)
        lon_d = int(adj_lon / res)
        adj_lat -= lat_d * res
        adj_lon -= lon_d * res
        digits.append(CODE_ALPHABET[lat_d % len(CODE_ALPHABET)])
        digits.append(CODE_ALPHABET[lon_d % len(CODE_ALPHABET)])

    code = "".join(digits)
    return code[:SEPARATOR_POSITION] + "+" + code[SEPARATOR_POSITION:]


# ---------------------------------------------------------------------------
# Self-test vectors (verified manually against Google Maps Plus Code tool)
# ---------------------------------------------------------------------------
_TEST_VECTORS = [
    # (lat, lon, expected_code, description)
    # ★ = manually verified against Google Maps Plus Code tool (Session 12, Franklin County pipeline)
    (39.947,  -83.012, "86FRWXWQ+R5", "★ Franklin County — Scioto Audubon Metro Park area"),
    (39.961,  -82.999, "86FVX262+CC", "★ Franklin County — Easton area"),
    (39.9612, -82.9988, "86FVX262+FF", "Franklin County — slight offset"),
    (40.0,    -83.0,   "86GV2222+22", "Franklin County — round coordinates"),
    (0.0,     0.0,     "6FG22222+22", "Null Island"),
    (51.5074, -0.1278, "9C3XGV4C+XV", "London, UK"),
    (35.6762, 139.6503, "8Q7XMMG2+F4", "Tokyo, Japan"),
]


def run_tests() -> bool:
    """Run self-test vectors. Returns True if all pass."""
    print("na_plus_code.py — self-test")
    print("-" * 60)
    passed = 0
    failed = 0
    for lat, lon, expected, desc in _TEST_VECTORS:
        result = encode_plus_code(lat, lon)
        ok = result == expected
        status = "PASS" if ok else "FAIL"
        print(f"  [{status}] ({lat:+.4f}, {lon:+.4f}) → {result}  (expected {expected})  {desc}")
        if ok:
            passed += 1
        else:
            failed += 1
    print("-" * 60)
    print(f"  {passed} passed, {failed} failed")
    return failed == 0


if __name__ == "__main__":
    import sys
    ok = run_tests()
    sys.exit(0 if ok else 1)
