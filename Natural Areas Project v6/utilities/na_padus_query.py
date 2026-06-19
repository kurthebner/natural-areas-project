"""
na_padus_query.py — PAD-US GDB spatial query utility for Natural Areas Project v6

Reads PADUS4_0_StateOH.gdb (Fee layer), filters to a county polygon using
TIGER/Line 2024 county subdivision boundaries, and fuzzy-matches against the
NAP sites table to produce a completeness report.

County polygon is derived by dissolving Ohio MCD (cousub) polygons sharing the
same COUNTYFP value. This replaces the former bbox (bounding rectangle) filter,
eliminating false positives from adjacent counties whose centroids or polygons
extend into a rectangular bounding box but not into the county itself.

The intersection operator is used (not centroid-within), so genuine cross-county
PAD-US entities whose polygons straddle a county boundary appear in both counties'
queries — consistent with IMP-027 design intent.

Usage:
    python na_padus_query.py <county_name>
    python na_padus_query.py Wayne
    python na_padus_query.py Franklin
    python na_padus_query.py "Van Wert"
    python na_padus_query.py --list-counties   # show all supported counties

Requirements:
    pip install geopandas fiona rapidfuzz --break-system-packages

Data sources:
    PAD-US:  PADUS4_0_StateOH.gdb  (project root)
    County:  GIS_Assets/ohio_townships/tl_2024_39_cousub.shp  (TIGER/Line 2024)
    NAP DB:  NASqlite/natural_areas_v6.db

IMP-027 (2026-06-12): Replaced SetSpatialFilterRect/bbox approach with county
    polygon intersection using TIGER/Line 2024 cousub boundaries.
"""

import sys
import sqlite3
import geopandas as gpd
import pandas as pd
from pathlib import Path
from rapidfuzz import fuzz

# ── Paths ──────────────────────────────────────────────────────────────────────
PROJECT = Path(__file__).parent.parent
GDB_PATH = PROJECT / "PADUS4_0_StateOH.gdb"
DB_PATH  = PROJECT / "NASqlite" / "natural_areas_v6.db"
LAYER    = "PADUS4_0Fee_State_OH"

COUSUB_SHP = PROJECT / "GIS_Assets" / "ohio_townships" / "tl_2024_39_cousub.shp"
COUSUB_ZIP = PROJECT / "GIS_Assets" / "ohio_townships" / "tl_2024_39_cousub.zip"

# ── Ohio county name → TIGER/Line COUNTYFP (3-digit FIPS) ─────────────────────
OHIO_COUNTY_FIPS = {
    "Adams":       "001",
    "Allen":       "003",
    "Ashland":     "005",
    "Ashtabula":   "007",
    "Athens":      "009",
    "Auglaize":    "011",
    "Belmont":     "013",
    "Brown":       "015",
    "Butler":      "017",
    "Carroll":     "019",
    "Champaign":   "021",
    "Clark":       "023",
    "Clermont":    "025",
    "Clinton":     "027",
    "Columbiana":  "029",
    "Coshocton":   "031",
    "Crawford":    "033",
    "Cuyahoga":    "035",
    "Darke":       "037",
    "Defiance":    "039",
    "Delaware":    "041",
    "Erie":        "043",
    "Fairfield":   "045",
    "Fayette":     "047",
    "Franklin":    "049",
    "Fulton":      "051",
    "Gallia":      "053",
    "Geauga":      "055",
    "Greene":      "057",
    "Guernsey":    "059",
    "Hamilton":    "061",
    "Hancock":     "063",
    "Hardin":      "065",
    "Harrison":    "067",
    "Henry":       "069",
    "Highland":    "071",
    "Hocking":     "073",
    "Holmes":      "075",
    "Huron":       "077",
    "Jackson":     "079",
    "Jefferson":   "081",
    "Knox":        "083",
    "Lake":        "085",
    "Lawrence":    "087",
    "Licking":     "089",
    "Logan":       "091",
    "Lorain":      "093",
    "Lucas":       "095",
    "Madison":     "097",
    "Mahoning":    "099",
    "Marion":      "101",
    "Medina":      "103",
    "Meigs":       "105",
    "Mercer":      "107",
    "Miami":       "109",
    "Monroe":      "111",
    "Montgomery":  "113",
    "Morgan":      "115",
    "Morrow":      "117",
    "Muskingum":   "119",
    "Noble":       "121",
    "Ottawa":      "123",
    "Paulding":    "125",
    "Perry":       "127",
    "Pickaway":    "129",
    "Pike":        "131",
    "Portage":     "133",
    "Preble":      "135",
    "Putnam":      "137",
    "Richland":    "139",
    "Ross":        "141",
    "Sandusky":    "143",
    "Scioto":      "145",
    "Seneca":      "147",
    "Shelby":      "149",
    "Stark":       "151",
    "Summit":      "153",
    "Trumbull":    "155",
    "Tuscarawas":  "157",
    "Union":       "159",
    "Van Wert":    "161",
    "Vinton":      "163",
    "Warren":      "165",
    "Washington":  "167",
    "Wayne":       "169",
    "Williams":    "171",
    "Wood":        "173",
    "Wyandot":     "175",
}

# ── Excluded PAD-US categories (never flag as discovery miss) ──────────────────
EXCLUDED_OWN_TYPES = {"PVT"}   # Private
EXCLUDED_ACCESS    = {"Closed"}
EXCLUDED_NAME_KEYWORDS = [
    "fairground", "country club", "shooting range", "gun club",
    "rifle range", "fish hatchery", "national guard", "army reserve",
]

MATCH_THRESHOLD = 80

# ── Cached county polygon (avoid re-loading cousub for repeated calls) ─────────
_county_polygon_cache: dict = {}


def get_county_polygon(county_name: str):
    """
    Return a Shapely polygon for the given Ohio county in EPSG:4326.

    Derived by dissolving all TIGER/Line 2024 cousub (MCD) polygons that share
    the county's COUNTYFP value. Ohio has no unorganized territory, so every
    square mile of each county belongs to at least one MCD.
    """
    if county_name in _county_polygon_cache:
        return _county_polygon_cache[county_name]

    if county_name not in OHIO_COUNTY_FIPS:
        raise ValueError(
            f"County '{county_name}' not in OHIO_COUNTY_FIPS table.\n"
            f"Run --list-counties to see supported names."
        )
    fips = OHIO_COUNTY_FIPS[county_name]

    cousub_path = COUSUB_SHP if COUSUB_SHP.exists() else COUSUB_ZIP
    if not cousub_path.exists():
        raise FileNotFoundError(
            f"Ohio cousub shapefile not found.\n"
            f"Expected: {COUSUB_SHP}\n"
            "Download tl_2024_39_cousub.zip from:\n"
            "  https://www2.census.gov/geo/tiger/TIGER2024/COUSUB/"
        )

    print(f"  Loading TIGER/Line 2024 cousub for {county_name} (FIPS={fips})…", flush=True)
    cousub = gpd.read_file(str(cousub_path))
    county_parts = cousub[cousub["COUNTYFP"] == fips]

    if county_parts.empty:
        raise ValueError(
            f"No TIGER cousub features found for {county_name} County (FIPS={fips})."
        )

    # Dissolve all MCDs → single county polygon; convert to WGS84
    county_gdf = county_parts.dissolve().to_crs("EPSG:4326")
    poly = county_gdf.geometry.iloc[0]
    _county_polygon_cache[county_name] = poly
    return poly


def load_padus_for_county(county_name: str) -> gpd.GeoDataFrame:
    """
    Load PAD-US fee records whose geometries intersect the county polygon.

    Uses county polygon intersection (IMP-027) rather than a bounding rectangle,
    eliminating false positives from adjacent-county entities that bleed into a
    rectangular bbox.  Cross-county entities whose polygons straddle the county
    boundary are included in both counties' results by design.
    """
    county_poly = get_county_polygon(county_name)

    print(f"  Loading PAD-US GDB (layer={LAYER})…", flush=True)
    gdf = gpd.read_file(str(GDB_PATH), layer=LAYER)
    gdf = gdf.to_crs("EPSG:4326")  # WGS84

    # Polygon intersection filter
    mask = gdf.geometry.intersects(county_poly)
    result = gdf[mask].copy()
    print(f"  PAD-US records intersecting {county_name} County: {len(result)}")
    return result


def load_nap_sites(county_name: str) -> list:
    """
    Load NAP sites for this county from the DB (live + held entities).

    Returns list of (id, name, status) where status is 'live' or 'held'.
    Including held entities prevents cross-county entities like Funk Bottoms
    or Killbuck Marsh from appearing as false discovery misses.
    """
    conn = sqlite3.connect(str(DB_PATH))
    c = conn.cursor()

    c.execute(
        "SELECT site_id, name FROM sites WHERE counties LIKE ?",
        (f"%{county_name}%",)
    )
    live = [(r[0], r[1], "live") for r in c.fetchall()]

    c.execute(
        """SELECT record_id, name FROM held_entities
           WHERE county = ? AND entity_type IN ('Site','Trailthing','Trail','Trail Network')""",
        (county_name,)
    )
    held = [(r[0], r[1], "held") for r in c.fetchall()]

    conn.close()
    return live + held


def is_excluded(row) -> tuple[bool, str]:
    """Return (True, reason) if this PAD-US record should be skipped."""
    own    = row.get("Own_Type", "")
    access = row.get("d_Pub_Access", "")
    name   = (row.get("Unit_Nm", "") or "").lower()

    if own in EXCLUDED_OWN_TYPES:
        return True, "private ownership"
    if access in EXCLUDED_ACCESS:
        return True, "closed access"
    for kw in EXCLUDED_NAME_KEYWORDS:
        if kw in name:
            return True, f"excluded keyword ({kw})"
    return False, ""


def padus_completeness_check(county_name: str):
    """Full PAD-US completeness check for a county. Prints report."""
    print(f"\n{'='*60}")
    print(f"PAD-US Completeness Check — {county_name} County")
    print(f"{'='*60}")

    padus     = load_padus_for_county(county_name)
    nap_sites = load_nap_sites(county_name)

    matched   = []
    unmatched = []
    skipped   = []

    for _, row in padus.iterrows():
        p_name     = row.get("Unit_Nm", "") or ""
        p_own      = row.get("d_Own_Name", "")
        p_mang     = row.get("d_Mang_Name", "")
        p_gap      = row.get("d_GAP_Sts", "")
        p_acres    = row.get("GIS_Acres", "")
        p_access   = row.get("d_Pub_Access", "")

        excluded, reason = is_excluded(dict(row))
        if excluded:
            skipped.append((p_name, reason))
            continue

        best_score = 0
        best_match = None
        for sid, s_name, status in nap_sites:
            score = fuzz.token_set_ratio(p_name.lower(), s_name.lower())
            if score > best_score:
                best_score = score
                best_match = (sid, s_name, status)

        entry = {
            "padus_name": p_name,
            "owner":      p_own,
            "manager":    p_mang,
            "gap":        p_gap[:1] if p_gap else "?",
            "acres":      p_acres,
            "access":     p_access,
            "score":      best_score,
            "nap_id":     best_match[0] if best_match else None,
            "nap_name":   best_match[1] if best_match else None,
            "nap_status": best_match[2] if best_match else None,
        }
        if best_score >= MATCH_THRESHOLD:
            matched.append(entry)
        else:
            unmatched.append(entry)

    # ── Report ──────────────────────────────────────────────────────────────────
    print(f"\n  MATCHED ({len(matched)}):")
    for m in sorted(matched, key=lambda x: x["padus_name"]):
        variant  = " [name variant]" if m["score"] < 100 else ""
        held_tag = " [HELD]" if m["nap_status"] == "held" else ""
        print(f"  [GAP{m['gap']} {m['score']:3.0f}] \"{m['padus_name']}\" ({m['acres']:.0f}ac)"
              f" → {m['nap_id']} \"{m['nap_name']}\"{variant}{held_tag}")

    print(f"\n  UNMATCHED — potential discovery gaps ({len(unmatched)}):")
    if unmatched:
        for u in sorted(unmatched, key=lambda x: -float(x.get("gap") or 4)):
            print(f"  [GAP{u['gap']} {u['score']:3.0f}] \"{u['padus_name']}\""
                  f" | {u['owner']} | {u['acres']:.0f}ac | {u['access']}")
    else:
        print("  None.")

    print("\n  SKIPPED -- out of scope ({}):" .format(len(skipped)))
    for name, reason in sorted(skipped):
        print("  \"{}\": ({})".format(name, reason))

    print("\n  Summary: {} matched, {} unmatched, {} skipped".format(
        len(matched), len(unmatched), len(skipped)))
    return matched, unmatched, skipped


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python na_padus_query.py <CountyName>")
        print("       python na_padus_query.py --list-counties")
        sys.exit(1)
    if sys.argv[1] == "--list-counties":
        for c in sorted(OHIO_COUNTY_FIPS.keys()):
            print("  {}".format(c))
    else:
        county = " ".join(sys.argv[1:])
        padus_completeness_check(county)
