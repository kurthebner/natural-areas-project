"""
gps_multicounty_batch3_v1.py
ODNR ArcGIS GIS pass -- 2026-05-23
24 sites resolved via ODNR HuntingRegulations_AGOL_3 ArcGIS REST service:
  MapServer/18 (ODNR_LANDS polygon centroids, returnCentroid=true)
  MapServer/12 (Wildlife Parking Areas PT_COORDS point layer)

Counties: HAN (13), WOD (10), SAN (1)

Source service:
  https://gis.ohiodnr.gov/arcgis/rest/services/DOW_Services/
    HuntingRegulations_AGOL_3/MapServer

Coordinate method:
  WOD WAs: ODNR_LANDS polygon centroid (returnCentroid=true, WGS84)
           via /MapServer/18, CNTY_FIPS IN ('173','063')
  HAN WAs/WPAs: Parking PT_COORDS from /MapServer/12
                NAME LIKE '%Hancock County Wildlife%' + bbox query
  SAN S-008: Computed mean centroid of 7 ODNR numbered WA tracts
             (WPA 14,18,30,31,50,59,63, CNTY_FIPS='143')

Sites STILL unresolved after this batch (absent from all ODNR GIS layers):
  OH-WOD-SI-012  Bairdstown Wildlife Production Area -- not in ODNR_LANDS
                  or parking layer; small impoundment near Bairdstown village
                  (41.171, -83.607); needs ODNR contact or field verification
  OH-WOD-SI-013  Dry Creek Wildlife Area -- not in ODNR_LANDS or parking
                  layer; Dry Creek stream GNIS feature near Walbridge
                  (41.611, -83.397); needs ODNR contact or field verification

Identity note (not resolved here, flag for review):
  HAN-S-003/S-009 (WA1/WPA9), S-004/S-011 (WA3/WPA32), S-005/S-012
  (WA4/WPA41), S-006/S-013 (WA5/WPA43), S-007/S-014 (WA6/WPA45),
  S-008/S-015 (WA7/WPA46) -- each numbered WA pair shares the same
  physical ODNR property (WldlfPAxx LANDS_NAME code). GPS assigned to
  both entities is identical; identity deduplication is a separate issue.
"""

import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import sqlite3
from datetime import datetime, timezone
from utilities.na_plus_code import encode_plus_code

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                       'NASqlite', 'natural_areas_v5.db')

# -----------------------------------------------------------------------------
# GPS_UPDATES: (site_id, lat, lon, acquisition_method, source_note)
# Centroids from ODNR_LANDS polygon layer (MapServer/18) unless noted.
# Parking PT_COORDS from MapServer/12 have 8-decimal precision.
# ODNR_LANDS centroids are 4-decimal precision (polygon centroid, ~10-100m).
# -----------------------------------------------------------------------------
GPS_UPDATES = [
    # -- Wood County -- ODNR_LANDS polygon centroids (WldlfPAxxWA codes) ------
    ('OH-WOD-SI-003', 41.388600, -83.812900,
     'gis',
     'ODNR_LANDS polygon centroid: WldlfPA3WA = Wood County Wildlife Area 1, '
     'HuntingRegulations_AGOL_3/MapServer/18, CNTY_FIPS=173'),
    ('OH-WOD-SI-004', 41.309500, -83.623300,
     'gis',
     'ODNR_LANDS polygon centroid: WldlfPA6WA = Wood County Wildlife Area 2, '
     'HuntingRegulations_AGOL_3/MapServer/18, CNTY_FIPS=173'),
    ('OH-WOD-SI-005', 41.266400, -83.642700,
     'gis',
     'ODNR_LANDS polygon centroid: WldlfPA8WA = Wood County Wildlife Area 4, '
     'HuntingRegulations_AGOL_3/MapServer/18, CNTY_FIPS=173'),
    ('OH-WOD-SI-006', 41.249700, -83.799600,
     'gis',
     'ODNR_LANDS polygon centroid: WldlfPA11WA = Wood County Wildlife Area 5, '
     'HuntingRegulations_AGOL_3/MapServer/18, CNTY_FIPS=173'),
    ('OH-WOD-SI-007', 41.170400, -83.599400,
     'gis',
     'ODNR_LANDS polygon centroid: WldlfPA20WA = Wood County Wildlife Area 6, '
     'HuntingRegulations_AGOL_3/MapServer/18, CNTY_FIPS=173'),
    ('OH-WOD-SI-008', 41.339200, -83.872200,
     'gis',
     'ODNR_LANDS polygon centroid: WldlfPA21WA = Wood County Wildlife Area 7, '
     'HuntingRegulations_AGOL_3/MapServer/18, CNTY_FIPS=173'),
    ('OH-WOD-SI-009', 41.231800, -83.714800,
     'gis',
     'ODNR_LANDS polygon centroid: WldlfPA42WA = Wood County Wildlife Area 8, '
     'HuntingRegulations_AGOL_3/MapServer/18, CNTY_FIPS=173'),
    ('OH-WOD-SI-010', 41.525000, -83.500900,
     'gis',
     'ODNR_LANDS polygon centroid: WldlfPA44WA = Wood County Wildlife Area 9, '
     'HuntingRegulations_AGOL_3/MapServer/18, CNTY_FIPS=173'),
    ('OH-WOD-SI-011', 41.175900, -83.818200,
     'gis',
     'ODNR_LANDS polygon centroid: WldlfPA58WA = Wood County Wildlife Area 10, '
     'HuntingRegulations_AGOL_3/MapServer/18, CNTY_FIPS=173'),
    ('OH-WOD-SI-015', 41.429900, -83.823500,
     'gis',
     'ODNR_LANDS polygon centroid: VanTasselWA = Van Tassel WA (102 ac), '
     'HuntingRegulations_AGOL_3/MapServer/18, CNTY_FIPS=173'),

    # -- Hancock County WAs -- parking PT_COORDS (MapServer/12) ---------------
    # WldlfPA9WA = HAN WA 1 (also = WPA 9, same physical property)
    ('OH-HAN-S-003', 41.159104, -83.612051,
     'gis',
     'ODNR parking PT_COORDS: WldlfPA9WA = Hancock County Wildlife Area 1, '
     'HuntingRegulations_AGOL_3/MapServer/12'),
    # WldlfPA32WA = HAN WA 3 (also = WPA 32, same physical property)
    ('OH-HAN-S-004', 40.848684, -83.798731,
     'gis',
     'ODNR parking PT_COORDS: WldlfPA32WA = Hancock County Wildlife Area 3, '
     'HuntingRegulations_AGOL_3/MapServer/12'),
    # WldlfPA41WA = HAN WA 4 (also = WPA 41, same physical property)
    ('OH-HAN-S-005', 41.047362, -83.704073,
     'gis',
     'ODNR parking PT_COORDS: WldlfPA41WA = Hancock County Wildlife Area 4, '
     'HuntingRegulations_AGOL_3/MapServer/12'),
    # WldlfPA43WA = HAN WA 5 (also = WPA 43, same physical property)
    ('OH-HAN-S-006', 40.819418, -83.623099,
     'gis',
     'ODNR parking PT_COORDS: WldlfPA43WA = Hancock County Wildlife Area 5, '
     'HuntingRegulations_AGOL_3/MapServer/12'),
    # WldlfPA45WA = HAN WA 6 (also = WPA 45, same physical property)
    ('OH-HAN-S-007', 40.936453, -83.743686,
     'gis',
     'ODNR parking PT_COORDS: WldlfPA45WA = Hancock County Wildlife Area 6, '
     'HuntingRegulations_AGOL_3/MapServer/12'),
    # WldlfPA46WA = HAN WA 7 (also = WPA 46, same physical property)
    ('OH-HAN-S-008', 41.058228, -83.861574,
     'gis',
     'ODNR parking PT_COORDS: WldlfPA46WA = Hancock County Wildlife Area 7, '
     'HuntingRegulations_AGOL_3/MapServer/12'),

    # -- Hancock County WPAs -- same coordinates as corresponding WA ----------
    # WPA 9 = Hancock County WA 1 (WldlfPA9WA)
    ('OH-HAN-S-009', 41.159104, -83.612051,
     'gis',
     'ODNR parking PT_COORDS: WldlfPA9WA = Hancock County WA 1 / WPA 9 '
     '(same property); HuntingRegulations_AGOL_3/MapServer/12'),
    # WPA 25 = Hancock County WA 2 (WldlfPA25WA) -- not separately in DB as named WA
    ('OH-HAN-S-010', 41.124883, -83.722117,
     'gis',
     'ODNR parking PT_COORDS: WldlfPA25WA = Hancock County Wildlife Area 2 / WPA 25, '
     'HuntingRegulations_AGOL_3/MapServer/12'),
    # WPA 32 = Hancock County WA 3 (WldlfPA32WA)
    ('OH-HAN-S-011', 40.848684, -83.798731,
     'gis',
     'ODNR parking PT_COORDS: WldlfPA32WA = Hancock County WA 3 / WPA 32 '
     '(same property); HuntingRegulations_AGOL_3/MapServer/12'),
    # WPA 41 = Hancock County WA 4 (WldlfPA41WA)
    ('OH-HAN-S-012', 41.047362, -83.704073,
     'gis',
     'ODNR parking PT_COORDS: WldlfPA41WA = Hancock County WA 4 / WPA 41 '
     '(same property); HuntingRegulations_AGOL_3/MapServer/12'),
    # WPA 43 = Hancock County WA 5 (WldlfPA43WA)
    ('OH-HAN-S-013', 40.819418, -83.623099,
     'gis',
     'ODNR parking PT_COORDS: WldlfPA43WA = Hancock County WA 5 / WPA 43 '
     '(same property); HuntingRegulations_AGOL_3/MapServer/12'),
    # WPA 45 = Hancock County WA 6 (WldlfPA45WA)
    ('OH-HAN-S-014', 40.936453, -83.743686,
     'gis',
     'ODNR parking PT_COORDS: WldlfPA45WA = Hancock County WA 6 / WPA 45 '
     '(same property); HuntingRegulations_AGOL_3/MapServer/12'),
    # WPA 46 = Hancock County WA 7 (WldlfPA46WA)
    ('OH-HAN-S-015', 41.058228, -83.861574,
     'gis',
     'ODNR parking PT_COORDS: WldlfPA46WA = Hancock County WA 7 / WPA 46 '
     '(same property); HuntingRegulations_AGOL_3/MapServer/12'),

    # -- Sandusky County -- computed centroid of 7 numbered WA tracts ---------
    # WPA 14,18,30,31,50,59,63 (CNTY_FIPS=143); mean of 7 polygon centroids
    # Individual centroids: (41.319,-83.303),(41.335,-83.256),(41.395,-83.070),
    #   (41.262,-83.033),(41.289,-83.376),(41.379,-83.240),(41.412,-83.035)
    ('OH-SAN-S-008', 41.341571, -83.187571,
     'gis',
     'Computed mean centroid of 7 ODNR numbered WA tracts (WPA 14,18,30,31,50,59,63), '
     'CNTY_FIPS=143, HuntingRegulations_AGOL_3/MapServer/18'),
]

# -----------------------------------------------------------------------------
def run():
    print(f"GPS Batch 3 -- {len(GPS_UPDATES)} sites")
    print(f"DB: {DB_PATH}")
    print()

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # Pre-flight: confirm sites exist and currently have NULL GPS
    print("Pre-flight check:")
    missing, already_have = [], []
    for site_id, lat, lon, method, note in GPS_UPDATES:
        cur.execute("SELECT name, gps_lat FROM sites WHERE site_id = ?", (site_id,))
        row = cur.fetchone()
        if not row:
            print(f"  WARN  {site_id} -- NOT FOUND IN DB")
            missing.append(site_id)
        elif row[1] is not None:
            print(f"  SKIP  {site_id} -- already has GPS ({row[1]:.6f})")
            already_have.append(site_id)
        else:
            print(f"  READY {site_id} -- {row[0]}")

    print()
    if missing:
        print(f"WARNING: {len(missing)} site_ids not found in DB: {missing}")
        print("Aborting.")
        conn.close()
        return

    to_update = [r for r in GPS_UPDATES
                 if r[0] not in missing and r[0] not in already_have]
    print(f"Will update {len(to_update)} sites (skipping {len(already_have)} already with GPS).")
    print()

    if not to_update:
        print("Nothing to do.")
        conn.close()
        return

    # Acquire + commit
    updated_at = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    success, fail = [], []

    for site_id, lat, lon, method, note in to_update:
        try:
            plus = encode_plus_code(lat, lon)
        except Exception as e:
            print(f"  PLUS_ERR {site_id}: {e} -- using empty string")
            plus = ''

        cur.execute("""
            UPDATE sites
               SET gps_lat    = ?,
                   gps_lon    = ?,
                   plus_code  = ?,
                   updated_at = ?
             WHERE site_id = ?
        """, (lat, lon, plus, updated_at, site_id))

        if cur.rowcount == 1:
            success.append((site_id, lat, lon, plus))
            print(f"  OK  {site_id}: ({lat:.6f}, {lon:.6f})  plus={plus}")
        else:
            fail.append(site_id)
            print(f"  FAIL {site_id}: rowcount={cur.rowcount}")

    conn.commit()
    conn.close()

    print()
    print("-" * 60)
    print(f"Committed: {len(success)} sites")
    print(f"Failed:    {len(fail)} sites")
    if fail:
        print(f"  Failed IDs: {fail}")
    print()

    # Post-flight verification
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    print("Post-flight: spot-check 3 sites")
    for site_id, lat, lon, plus in success[:3]:
        cur.execute("SELECT name, gps_lat, gps_lon, plus_code FROM sites WHERE site_id = ?", (site_id,))
        row = cur.fetchone()
        if row:
            print(f"  {site_id}: {row[0]} -> ({row[1]}, {row[2]}) plus={row[3]}")
        else:
            print(f"  {site_id}: NOT FOUND (should not happen)")
    conn.close()

    print()
    print("Remaining null-GPS sites (sample):")
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        SELECT site_id, name FROM sites
        WHERE gps_lat IS NULL
        ORDER BY site_id
        LIMIT 30
    """)
    for r in cur.fetchall():
        print(f"  {r[0]}: {r[1]}")
    conn.close()


if __name__ == '__main__':
    run()
