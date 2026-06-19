"""
gps_multicounty_batch2_v1.py
Web-research GPS batch — 2026-05-23
21 sites resolved via web research (Nominatim, GolfPass, genealogytrails,
  hometownlocator GNIS, lake-link, UDisc, PeopleLegacy, real-estate lookup)

Counties: FUL (1), HAN (16), SC (1), WOD (3)

Sites STILL unresolved after this batch (need ODNR GIS or field work):
  OH-HAN-S-048 Portage Township Cemetery
  OH-FUL-SI-027 Green Memorial Park (Lyons)
  OH-FUL-SI-028 Lyons Community Ball Park
  OH-FR-S-1040 Finnell Park (Columbus)
  OH-WOD-SI-073 Mishe Monoto Preserve — IDENTITY ISSUE (wrong county in discovery;
      Appalachia Ohio Alliance's Mishe Moneto Preserve is in Pickaway Co., not Wood Co.)
  OH-WOD-SI-003..SI-015 (12 sites): Wood County Wildlife Areas — needs ODNR Lake Map GIS
  OH-HAN-S-003..S-015 (13 sites): Hancock County Wildlife Areas — needs ODNR Lake Map GIS
  OH-SAN-S-008: Sandusky County Wildlife Areas — needs ODNR Lake Map GIS
"""

import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import sqlite3
from datetime import datetime, timezone
from utilities.na_plus_code import encode_plus_code

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                       'NASqlite', 'natural_areas_v5.db')

# ─────────────────────────────────────────────────────────────────────────────
# GPS_UPDATES: (site_id, lat, lon, acquisition_method, source_note)
# ─────────────────────────────────────────────────────────────────────────────
GPS_UPDATES = [
    # ── Wood County ──────────────────────────────────────────────────────────
    ('OH-WOD-SI-058', 41.561145, -83.615788,
     'geocoding', 'Nominatim: 429 E Boundary St, Perrysburg OH — Woodlands Park confirmed'),
    ('OH-WOD-SI-061', 41.614100, -83.553225,
     'geocoding', 'Nominatim: 150 Dixie Highway, Rossford OH — Ed Ford Memorial Park'),
    ('OH-WOD-SI-067', 41.179128, -83.671433,
     'geocoding', 'UDisc disc golf listing: North Baltimore Village Park coords'),
    ('OH-WOD-SI-076', 41.427188, -83.490983,
     'geocoding', 'Property listing: 4825 Sugar Ridge Rd, Pemberville OH 43450 — BSC headquarters/Bell Woods'),
    ('OH-WOD-SI-077', 41.427188, -83.490983,
     'geocoding', 'Property listing: 4825 Sugar Ridge Rd, Pemberville OH 43450 — adjacent to Bell Woods'),

    # ── Hancock County — Cemeteries ─────────────────────────────────────────
    ('OH-HAN-S-040', 41.003533, -83.800251,
     'geocoding', 'Nominatim: Benton Ridge Cemetery, Main St, Benton Ridge OH — also known as Baker-Hamlin/Hamlin Cemetery'),
    ('OH-HAN-S-043', 40.942600, -83.594140,
     'geocoding', 'PeopleLegacy/search: Houcktown Cemetery, County Road 8, Houcktown OH'),
    ('OH-HAN-S-044', 41.031667, -83.541667,
     'geocoding', 'genealogytrails.com DMS 410154N 0833230W: Brights Cemetery, Hancock County'),
    ('OH-HAN-S-141', 40.942780, -83.592220,
     'geocoding', 'getamap.net GNIS: Frontiers Repose Cemetery, Houcktown area, Hancock County'),
    ('OH-HAN-S-145', 41.034722, -83.554444,
     'geocoding', 'genealogytrails.com DMS 410205N 0833316W: High Bank Cemetery, Hancock County'),
    ('OH-HAN-S-146', 41.061667, -83.755278,
     'geocoding', 'genealogytrails.com DMS 410342N 0834519W: Indian Grove Cemetery, on SR-15/US-224 W of SR-186'),
    ('OH-HAN-S-153', 41.045278, -83.668333,
     'geocoding', 'genealogytrails.com DMS 410243N 0834006W: Maple Lawn Cemetery, Hancock County'),
    ('OH-HAN-S-157', 41.018611, -83.766944,
     'geocoding', 'genealogytrails.com DMS 410107N 0834601W: Riley Creek Cemetery, Van Buren Twp, Hancock County'),

    # ── Hancock County — Recreation / Golf / Water ───────────────────────────
    ('OH-HAN-S-075', 41.037131, -83.653877,
     'geocoding', 'Nominatim: 300 W Sandusky St, Findlay OH — Downtown Recreation Area (flood mitigation/rec project)'),
    ('OH-HAN-S-084', 41.119385, -83.444888,
     'geocoding', 'lake-link.com: Fostoria Reservoir #5 (Lake LeComte), Washington Twp, Hancock County'),
    ('OH-HAN-S-104', 41.047320, -83.635967,
     'geocoding', 'Nominatim: 18441 US-224 (Tiffin Ave), Findlay OH — Red Hawk Run Golf Club'),
    ('OH-HAN-S-106', 41.027795, -83.531601,
     'geocoding', 'GolfPass: Broken Birdie GC (fmr. Bairds Wayside Golf), 18125 SR-568, Findlay OH — NOTE: CLOSED since 2019'),
    ('OH-HAN-S-108', 40.923857, -83.660760,
     'geocoding', 'GolfPass: Sycamore Springs Golf Course, 11492 Township Rd 25, Arlington OH 45814'),
    ('OH-HAN-S-109', 41.112136, -83.440500,
     'geocoding', 'Nominatim: 3770 County Road 23, West Independence, Hancock County — Lakeland Golf Course'),

    # ── Fulton County ────────────────────────────────────────────────────────
    ('OH-FUL-SI-024', 41.679639, -84.322679,
     'geocoding', 'Nominatim: Park POI in Fayette, Gorham Twp, Fulton County OH — only park feature returned for village'),

    # ── Scioto County ────────────────────────────────────────────────────────
    ('OH-SC-S-0002', 38.810352, -83.177403,
     'geocoding', 'ohio.hometownlocator.com GNIS feature ID 1037387: Alum Rock pillar, Scioto County, ZIP 45657'),
]

# ─────────────────────────────────────────────────────────────────────────────
def run():
    print(f"GPS Batch 2 — {len(GPS_UPDATES)} sites")
    print(f"DB: {DB_PATH}")
    print()

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # Pre-flight: confirm these sites exist and currently have NULL GPS
    print("Pre-flight check:")
    missing, already_have = [], []
    for site_id, lat, lon, method, note in GPS_UPDATES:
        cur.execute("SELECT name, gps_lat FROM sites WHERE site_id = ?", (site_id,))
        row = cur.fetchone()
        if not row:
            print(f"  WARN  {site_id} — NOT FOUND IN DB")
            missing.append(site_id)
        elif row[1] is not None:
            print(f"  SKIP  {site_id} — already has GPS ({row[1]:.6f})")
            already_have.append(site_id)
        else:
            print(f"  READY {site_id} — {row[0]}")

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
            print(f"  PLUS_ERR {site_id}: {e} — using empty string")
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
    print("─" * 60)
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
            print(f"  {site_id}: {row[0]} → ({row[1]}, {row[2]}) plus={row[3]}")
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
