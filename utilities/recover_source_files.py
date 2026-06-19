"""
utilities/recover_source_files.py
IMP-129: Recover qualifying source PDFs for Ottawa, Franklin, and Lucas counties.

§24 Map and Asset File Preservation: binary files (PDFs, maps, brochures) that were
used as authoritative sources during discovery but were not saved at fetch time due to
the wget mechanism being unavailable (blocked in this environment).

Run once from project root:
  python utilities/recover_source_files.py

Uses urllib.request — no external dependencies.
"""

import sys
import pathlib
import urllib.request
import time

# IMP-128: Windows console UTF-8 fix
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

PROJECT_ROOT = pathlib.Path(__file__).parent.parent

# ---------------------------------------------------------------------------
# File manifest — (county, filename, url, description)
# ---------------------------------------------------------------------------
FILES = [
    # --- OTTAWA ---
    (
        "Ottawa",
        "odnr_coastal_access_ottawa_county.pdf",
        "https://dam.assets.ohio.gov/image/upload/ohiodnr.gov/documents/coastal/public-access/pag-le-02-ottawa-county.pdf",
        "ODNR Lake Erie Public Access Guide — Ottawa County (T2 source: 14 coastal sites)",
    ),
    (
        "Ottawa",
        "odnr_lake_erie_islands_chapter3.pdf",
        "https://dam.assets.ohio.gov/image/upload/odnr/coastal/ocmp/CH3_LakeErieIslands_04142026_web.pdf",
        "ODNR Coastal Management Plan — Ch. 3 Lake Erie Islands (T2 source: island park GPS, acreages)",
    ),
    (
        "Ottawa",
        "pibtpd_nature_preserves_brochure_2021.pdf",
        "https://www.putinbayparks.com/wp-content/uploads/2021/03/PIBTPD_Brochure.pdf",
        "Put-in-Bay Township Park District Nature Preserves Brochure 2021 (T3 source: 7 island preserves)",
    ),
    (
        "Ottawa",
        "magee_marsh_wa_trail_map.pdf",
        "https://dam.assets.ohio.gov/image/upload/ohiodnr.gov/documents/wildlife/wildlife-area-maps/mageemarshwildlifearea_trailmap.pdf",
        "ODNR Magee Marsh Wildlife Area trail map (T2 source: 7 Magee Marsh trails)",
    ),
    (
        "Ottawa",
        "little_portage_wa_map.pdf",
        "https://dam.assets.ohio.gov/image/upload/ohiodnr.gov/documents/wildlife/wildlife-area-maps/littleportage.pdf",
        "ODNR Little Portage Wildlife Area map (T2 source: boundary/access data)",
    ),

    # --- FRANKLIN ---
    (
        "Franklin",
        "columbus_nature_preserves_booklet.pdf",
        "https://columbusrecparks.com/wp-content/uploads/2025/02/ColumbusNaturePreserves_Spreads_compressed.pdf",
        "Columbus Recreation & Parks Nature Preserves booklet 2025 (T6 source: city nature preserves)",
    ),

    # --- LUCAS ---
    (
        "Lucas",
        "mallard_club_wa_map.pdf",
        "https://ohiodnr.gov/static/documents/wildlife/wildlife-area-maps/mallardclub.pdf",
        "ODNR Mallard Club Wildlife Area map (T2 source)",
    ),
    (
        "Lucas",
        "metzger_marsh_wa_map.pdf",
        "https://ohiodnr.gov/static/documents/wildlife/wildlife-area-maps/metzgermarsh.pdf",
        "ODNR Metzger Marsh Wildlife Area map (T2 source: GIS_VERIFY_COUNTY Lucas/Ottawa)",
    ),
    (
        "Lucas",
        "meilke_road_savanna_wa_map.pdf",
        "https://ohiodnr.gov/static/documents/wildlife/wildlife-area-maps/Meilke_Road.pdf",
        "ODNR Meilke Road Savanna Wildlife Area map (T2 source)",
    ),
    (
        "Lucas",
        "lanker_wa_map.pdf",
        "https://ohiodnr.gov/static/documents/wildlife/wildlife-area-maps/Lanker.pdf",
        "ODNR Lanker Wildlife Area map (T2 source)",
    ),
    (
        "Lucas",
        "magee_marsh_wa_map.pdf",
        "https://ohiodnr.gov/static/documents/wildlife/wildlife-area-maps/mageemarsh.pdf",
        "ODNR Magee Marsh Wildlife Area boundary map (T2 source: GIS_VERIFY_COUNTY Lucas/Ottawa)",
    ),
    (
        "Lucas",
        "magee_marsh_wa_trail_map.pdf",
        "https://ohiodnr.gov/static/documents/wildlife/wildlife-area-maps/mageemarshwildlifearea_trailmap.pdf",
        "ODNR Magee Marsh Wildlife Area trail map (T2 source: trail lengths)",
    ),
    (
        "Lucas",
        "missionary_island_wa_map.pdf",
        "https://ohiodnr.gov/static/documents/wildlife/wildlife-area-maps/Missionary_Island.pdf",
        "ODNR Missionary Island Wildlife Area map (T2 source: GIS_VERIFY_COUNTY Lucas/Wood)",
    ),
    (
        "Lucas",
        "van_tassel_wa_map.pdf",
        "https://ohiodnr.gov/static/documents/wildlife/wildlife-area-maps/vantassel.pdf",
        "ODNR Van Tassel Wildlife Area map (T2 source: GIS_VERIFY_COUNTY Wood/Lucas)",
    ),
    (
        "Lucas",
        "metroparks_wabash_cannonball_trail_map.pdf",
        "https://metroparkstoledo.com/qrmaps/WabashCannonball.pdf",
        "Metroparks Toledo Wabash Cannonball Trail map (T3 source: North Fork 46 mi / South Fork 17 mi)",
    ),
    (
        "Lucas",
        "metroparks_secor_area_map.pdf",
        "https://metroparkstoledo.com/media/6154/mta-secor-map-website-11032020-rs.pdf",
        "Metroparks Toledo Secor/Oak Openings area map (T3 source: Oak Openings Corridor trail)",
    ),
    (
        "Lucas",
        "metroparks_wiregrass_lake_map.pdf",
        "https://metroparkstoledo.com/media/6150/wiregrass-lake-map-outline-112020-lrs.pdf",
        "Metroparks Toledo Wiregrass Lake map (T3 source: Oak Openings trail system)",
    ),
    (
        "Lucas",
        "metroparks_toledo_all_parks_brochure_2025.pdf",
        "https://metroparkstoledo.com/media/11414/8-2025-all-parks-brochure-web.pdf",
        "Metroparks Toledo All Parks Brochure 2025 (T3 source: system-wide overview, 23 parks)",
    ),
    (
        "Lucas",
        "kitty_todd_nature_preserve_trail_map_2022.pdf",
        "https://www.nature.org/content/dam/tnc/nature/en/documents/OH_Kitty-Todd-Trail-Map_2022.pdf",
        "TNC Ohio Kitty Todd Nature Preserve trail map 2022 (T7 source: 3 trails, GPS)",
    ),
]

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def make_source_dir(county: str) -> pathlib.Path:
    d = PROJECT_ROOT / "County_Spreadsheets" / county / "source_files"
    d.mkdir(parents=True, exist_ok=True)
    return d


def download_file(dest: pathlib.Path, url: str) -> tuple[bool, str]:
    """Download url to dest. Returns (success, message)."""
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Natural Areas Project research)"})
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = resp.read()
        dest.write_bytes(data)
        size_kb = len(data) // 1024
        return True, f"{size_kb} KB"
    except Exception as e:
        return False, str(e)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    print("=== §24 Source File Recovery (IMP-129) ===\n")
    print(f"Project root: {PROJECT_ROOT}\n")

    results = {"ok": [], "fail": [], "skip": []}

    current_county = None
    for county, filename, url, desc in FILES:
        if county != current_county:
            current_county = county
            dest_dir = make_source_dir(county)
            print(f"\n--- {county} ---  ({dest_dir})")

        dest = dest_dir / filename

        if dest.exists():
            size_kb = dest.stat().st_size // 1024
            print(f"  SKIP (exists {size_kb} KB)  {filename}")
            results["skip"].append((county, filename))
            continue

        print(f"  Downloading: {filename}")
        print(f"    URL: {url}")
        ok, msg = download_file(dest, url)
        if ok:
            print(f"    -> Saved: {msg}")
            results["ok"].append((county, filename))
        else:
            print(f"    -> FAILED: {msg}")
            results["fail"].append((county, filename, msg))

        time.sleep(0.5)   # polite pause between requests

    # Summary
    print(f"\n{'='*55}")
    print(f"Downloaded:   {len(results['ok'])}")
    print(f"Already had:  {len(results['skip'])}")
    print(f"Failed:       {len(results['fail'])}")

    if results["fail"]:
        print("\nFailed files:")
        for county, fname, err in results["fail"]:
            print(f"  [{county}] {fname}")
            print(f"    {err}")

    # Final dir listing
    print("\nFinal source_files/ contents:")
    for county in ("Ottawa", "Franklin", "Lucas"):
        d = PROJECT_ROOT / "County_Spreadsheets" / county / "source_files"
        if d.exists():
            files = sorted(d.iterdir())
            print(f"\n  {county}/ ({len(files)} files):")
            for f in files:
                print(f"    {f.name}  ({f.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
