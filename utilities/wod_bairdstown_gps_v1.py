#!/usr/bin/env python3
"""
wod_bairdstown_gps_v1.py
Set GPS coordinates for OH-WOD-SI-012 (Bairdstown Wildlife Production Area).

Source: eBird hotspot L3683779
  https://ebird.org/hotspot/L3683779
  Google Maps query link embedded in page: query=41.1735954915085,-83.6020849942997
  Hotspot name: "Bairdstown Wildlife Production Area (view from roadside only),
                 Wood, Ohio, United States"

Entity is confirmed in Wood County (Wood County is in the hotspot breadcrumb).
GPS: 41.173595, -83.602085  (rounded to 6 dp from eBird source)
Plus Code: 86HR59FX+C5
"""

import sqlite3
import pathlib
from datetime import datetime, timezone

DB_PATH = pathlib.Path(__file__).parent.parent / "NASqlite" / "natural_areas_v5.db"
SITE_ID = "OH-WOD-SI-012"
GPS_LAT  = 41.173595
GPS_LON  = -83.602085
PLUS_CODE = "86HR59FX+C5"
NOW = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')


def run():
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row

    row = conn.execute(
        "SELECT site_id, name, gps_lat, gps_lon, plus_code FROM sites WHERE site_id=?",
        (SITE_ID,)
    ).fetchone()

    if not row:
        print(f"ERROR: {SITE_ID} not found in sites.")
        conn.close()
        return

    print(f"Found: {row['site_id']} — {row['name']}")
    print(f"  gps_lat before  : {row['gps_lat']}")
    print(f"  gps_lon before  : {row['gps_lon']}")
    print(f"  plus_code before: {row['plus_code']!r}")

    try:
        conn.execute("BEGIN")
        conn.execute("""
            UPDATE sites
               SET gps_lat   = ?,
                   gps_lon   = ?,
                   plus_code = ?,
                   updated_at = ?
             WHERE site_id = ?
        """, (GPS_LAT, GPS_LON, PLUS_CODE, NOW, SITE_ID))
        conn.commit()
        print("Committed.")
    except Exception as e:
        conn.rollback()
        print(f"ERROR — rolled back: {e}")
        conn.close()
        return

    # Verify
    after = conn.execute(
        "SELECT gps_lat, gps_lon, plus_code, updated_at FROM sites WHERE site_id=?",
        (SITE_ID,)
    ).fetchone()
    print(f"\n  gps_lat after   : {after['gps_lat']}")
    print(f"  gps_lon after   : {after['gps_lon']}")
    print(f"  plus_code after : {after['plus_code']}")
    print(f"  updated_at      : {after['updated_at']}")
    conn.close()


if __name__ == "__main__":
    run()
