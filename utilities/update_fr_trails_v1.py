"""
OH-FR trail length_mi and maps backfill — Columbus Metroparks (Step 2)
Sources: metroparks.net park pages, visited 2026-05-23.
Updates length_mi and maps for OH-FR-T trails sourced from metroparks.net.

Trails still NULL after this script (need separate resolution):
  OH-FR-T-0011  Edgewood Trail         — combined group (Edgewood/Lake/Prairie Way = 2.3 mi total)
  OH-FR-T-0012  Prairie Way Trail      — combined group (same)
  OH-FR-T-0013  Harrier Loop Trail     — combined group (Harrier Loop/Rail Way/Teal = 2.7 mi total)
  OH-FR-T-0014  Rail Way Trail         — combined group (same)
  OH-FR-T-0015  Teal Trail             — combined group (same)
  OH-FR-T-0070  Columbus Rotary Running Track — not listed on current Scioto Audubon page
  OH-FR-T-0071  Wetland Trail          — not listed on current Scioto Audubon page
  OH-FR-T-0076  Hickory Trail          — not listed on current Scioto Grove page
  OH-FR-T-0078  Quarry Trails Boardwalk Trail — not listed on current Quarry Trails page
  OH-FR-T-0082  Quarry Trails Mountain Bike Trail — not listed on current Quarry Trails page
  OH-FR-T-0098  Hamilton Township Park Trail — hamtwpfcoh.gov (not yet visited)
  OH-FR-T-0111  Paddle Gahanna & Blueways — gahanna.gov (not yet visited)
  OH-FR-T-0120  Big Run Trail          — columbusrecparks.com (not yet visited)

Run from project root:
  python utilities/update_fr_trails_v1.py
"""
import sqlite3
import datetime
import sys

sys.stdout.reconfigure(encoding='utf-8')

DB = 'NASqlite/natural_areas_v5.db'
now = datetime.datetime.now(datetime.UTC).strftime('%Y-%m-%dT%H:%M:%SZ')

BDC_MAP = 'https://www.metroparks.net/wp-content/uploads/2021/12/BDC-full-park-map-lg.jpg'
BLN_MAP = 'https://www.metroparks.net/wp-content/uploads/2026/05/BLN_map_web-print-2026.pdf'
RKF_MAP = 'https://www.metroparks.net/wp-content/uploads/2026/05/Rocky-Fork-map-web-print-2026.pdf'
SGR_MAP = 'https://www.metroparks.net/wp-content/uploads/2026/05/SGR_map_web-print_2026.pdf'
THC_MAP = 'https://www.metroparks.net/wp-content/uploads/2026/05/THC-map_web-print_2026.pdf'
INN_MAP = 'https://www.metroparks.net/wp-content/uploads/2026/05/INN-map-web-print-2026.pdf'
QTR_MAP = 'https://www.metroparks.net/wp-content/uploads/2026/05/QTR-map_web-print-2026.pdf'
SHW_MAP = 'https://www.metroparks.net/wp-content/uploads/2026/05/SHW_map_web-print_2026.pdf'
GLR_MAP = 'https://www.metroparks.net/wp-content/uploads/2025/08/GLR-map-2025-printable-from-web.pdf'
SAU_MAP = 'https://www.metroparks.net/wp-content/uploads/2026/05/SAU_map_web-print_2026.pdf'
WAL_MAP = 'https://www.metroparks.net/wp-content/uploads/2026/05/WAL_map_web-print_2026.pdf'
HST_MAP = 'https://www.metroparks.net/wp-content/uploads/2021/07/HST-parkmap@2x.pdf'

# (trail_id, length_mi, maps_url, note)
# maps_url=None means skip maps update for that row
UPDATES = [
    # --- Battelle Darby Creek ---
    # Source: https://www.metroparks.net/parks-and-trails/battelle-darby-creek/
    ('OH-FR-T-0008', 1.7,  BDC_MAP, 'Ancient Trail'),
    ('OH-FR-T-0009', 0.9,  BDC_MAP, 'Cobshell Trail'),
    ('OH-FR-T-0010', 3.0,  BDC_MAP, 'Dyer Mill Trail'),
    ('OH-FR-T-0016', 0.8,  BDC_MAP, 'Hawthorn Trail'),
    ('OH-FR-T-0017', 0.6,  BDC_MAP, 'Indian Ridge Trail'),
    ('OH-FR-T-0018', 0.5,  BDC_MAP, 'Osprey Lake Trail'),
    ('OH-FR-T-0019', 0.2,  BDC_MAP, 'Riffle Run Trail'),
    ('OH-FR-T-0020', 2.1,  BDC_MAP, 'Terrace Trail'),
    ('OH-FR-T-0021', 0.5,  BDC_MAP, 'Turkey Foot Trail'),
    ('OH-FR-T-0022', 1.9,  BDC_MAP, 'Wagtail Trail'),
    # Combined groups — maps only (lengths resolved separately)
    ('OH-FR-T-0011', None, BDC_MAP, 'Edgewood Trail — combined group, length TBD'),
    ('OH-FR-T-0012', None, BDC_MAP, 'Prairie Way Trail — combined group, length TBD'),
    ('OH-FR-T-0013', None, BDC_MAP, 'Harrier Loop Trail — combined group, length TBD'),
    ('OH-FR-T-0014', None, BDC_MAP, 'Rail Way Trail — combined group, length TBD'),
    ('OH-FR-T-0015', None, BDC_MAP, 'Teal Trail — combined group, length TBD'),

    # --- Greenway Trails ---
    # Source: https://www.metroparks.net/parks-and-trails/greenway-trails/
    # Darby Creek: 8.3 mi total (4.9 mi Battelle Darby Creek + 3.4 mi Prairie Oaks)
    ('OH-FR-T-0003', 8.3,  None, 'Darby Creek Greenway Trail'),
    ('OH-FR-T-0005', 16.0, None, 'Blacklick Creek Greenway Trail'),
    ('OH-FR-T-0006', 10.0, None, 'Scioto Greenway Trail'),
    ('OH-FR-T-0007', 24.5, None, 'Alum Creek Greenway Trail (confirmed by Three Creeks page)'),

    # --- Glacier Ridge ---
    # Source: https://www.metroparks.net/parks-and-trails/glacier-ridge/
    ('OH-FR-T-0042', 2.8, GLR_MAP, 'Ironweed Trail'),
    ('OH-FR-T-0043', 3.7, GLR_MAP, 'Marsh Hawk Trail'),
    ('OH-FR-T-0044', 0.8, GLR_MAP, 'Red Oak Trail'),
    ('OH-FR-T-0045', 5.2, GLR_MAP, 'Savannah Trail'),

    # --- Sharon Woods ---
    # Source: https://www.metroparks.net/parks-and-trails/sharon-woods/
    ('OH-FR-T-0046', 1.1, SHW_MAP, 'Edward S. Thomas Trail'),
    ('OH-FR-T-0047', 1.8, SHW_MAP, 'Spring Creek Trail'),
    ('OH-FR-T-0048', 3.8, SHW_MAP, 'Sharon Woods Multipurpose Trail'),
    ('OH-FR-T-0049', 0.4, SHW_MAP, 'Sharon Woods Lake Trail'),
    ('OH-FR-T-0050', 0.2, SHW_MAP, 'Oak Openings Trail'),

    # --- Blendon Woods ---
    # Source: https://www.metroparks.net/parks-and-trails/blendon-woods/
    ('OH-FR-T-0051', 0.9, BLN_MAP, 'Goldenrod Trail (page: "Goldenrod Pet")'),
    ('OH-FR-T-0052', 1.2, BLN_MAP, 'Sugarbush Trail'),
    ('OH-FR-T-0053', 0.6, BLN_MAP, 'Blendon Woods Overlook Trail (page: "Overlook")'),
    ('OH-FR-T-0054', 0.4, BLN_MAP, 'Ripple Rock Trail'),
    ('OH-FR-T-0055', 0.4, BLN_MAP, 'Blendon Woods Lake Trail (page: "Lake")'),
    ('OH-FR-T-0056', 0.2, BLN_MAP, 'Hickory Ridge Trail'),
    ('OH-FR-T-0057', 0.8, BLN_MAP, 'Brookside Trail'),

    # --- Three Creeks ---
    # Source: https://www.metroparks.net/parks-and-trails/three-creeks/
    ('OH-FR-T-0063', 1.0, THC_MAP, 'Bluebell Trail'),
    ('OH-FR-T-0064', 1.0, THC_MAP, 'Confluence Trail'),
    ('OH-FR-T-0065', 0.5, THC_MAP, 'Evergreen Trail (page: "Evergreen Pet")'),
    ('OH-FR-T-0066', 0.6, THC_MAP, 'Heron Pond Trail'),
    ('OH-FR-T-0067', 0.4, THC_MAP, 'Turtle Pond Trail'),
    ('OH-FR-T-0068', 1.2, THC_MAP, 'Sycamore Fields and Smith Farm Trail'),

    # --- Scioto Audubon ---
    # Source: https://www.metroparks.net/parks-and-trails/scioto-audubon/
    ('OH-FR-T-0069', 0.1, SAU_MAP, 'Hermit Thrush Trail'),
    # Maps only for trails not found on current page
    ('OH-FR-T-0070', None, SAU_MAP, 'Columbus Rotary Running Track — not on current page, length TBD'),
    ('OH-FR-T-0071', None, SAU_MAP, 'Wetland Trail — not on current page, length TBD'),

    # --- Scioto Grove ---
    # Source: https://www.metroparks.net/parks-and-trails/scioto-grove/
    ('OH-FR-T-0072', 2.5, SGR_MAP, 'Mingo Trail'),
    ('OH-FR-T-0073', 1.8, SGR_MAP, 'REI River Trail'),
    ('OH-FR-T-0074', 1.2, SGR_MAP, 'Scioto Grove Overlook Trail (page: "Overlook")'),
    ('OH-FR-T-0075', 0.7, SGR_MAP, 'Scioto Grove Arrowhead Trail (page: "Arrowhead")'),
    # Hickory Trail not found on current page — map only
    ('OH-FR-T-0076', None, SGR_MAP, 'Hickory Trail — not on current page, length TBD'),
    ('OH-FR-T-0077', 2.0, SGR_MAP, 'Scioto Grove Multipurpose Trail (page: "Multipurpose")'),

    # --- Quarry Trails ---
    # Source: https://www.metroparks.net/parks-and-trails/quarry-trails/
    # 0079: page lists as "Tall Wall Trail" 0.75 mi
    ('OH-FR-T-0079', 0.75, QTR_MAP, 'Tall Wall and Connector Loop (page: "Tall Wall Trail")'),
    ('OH-FR-T-0080', 0.25, QTR_MAP, 'Quarry Trails Lake View Loop (page: "Lake View Trail")'),
    ('OH-FR-T-0081', 0.6,  QTR_MAP, 'Milliken Falls Lower Trail (page: "Millikin Falls Trail")'),
    # Boardwalk and Mountain Bike not on current page — maps only
    ('OH-FR-T-0078', None, QTR_MAP, 'Quarry Trails Boardwalk Trail — not on current page, length TBD'),
    ('OH-FR-T-0082', None, QTR_MAP, 'Quarry Trails Mountain Bike Trail — not on current page, length TBD'),

    # --- Rocky Fork ---
    # Source: https://www.metroparks.net/parks-and-trails/rocky-fork/
    ('OH-FR-T-0083', 3.0, RKF_MAP, 'Rocky Fork Bridle Trail (page: "Bridle")'),
    ('OH-FR-T-0084', 1.0, RKF_MAP, 'North Meadow Trail'),
    ('OH-FR-T-0085', 0.5, RKF_MAP, 'Millstone Connector Trail'),
    ('OH-FR-T-0086', 0.3, RKF_MAP, 'Dog Trail (page: "Dog")'),
    ('OH-FR-T-0087', 1.3, RKF_MAP, 'Beech Woodland Trail'),
    ('OH-FR-T-0088', 0.5, RKF_MAP, 'Bevelhymer Trail'),

    # --- Walnut Woods ---
    # Source: https://www.metroparks.net/parks-and-trails/walnut-woods/
    ('OH-FR-T-0089', 2.6, WAL_MAP, 'Sweetgum Trail'),
    ('OH-FR-T-0090', 2.0, WAL_MAP, 'Walnut Woods Buckeye Trail (page: "Buckeye")'),
    # Kestrel (1.3 mi) + Monarch (1.4 mi) listed separately; DB has them as one combined loop
    ('OH-FR-T-0091', 2.7, WAL_MAP, 'Kestrel and Monarch Trail Loop (Kestrel 1.3 mi + Monarch 1.4 mi)'),

    # --- Inniswood ---
    # Source: https://www.metroparks.net/parks-and-trails/inniswood-metro-gardens/
    ('OH-FR-T-0092', 0.6,  INN_MAP, 'Boardwalk Trail'),
    ('OH-FR-T-0093', 0.4,  INN_MAP, 'Brookwood Trail'),
    ('OH-FR-T-0094', 0.6,  INN_MAP, 'Chipmunk Chatter Trail'),
    ('OH-FR-T-0095', 0.1,  INN_MAP, 'Frog Talk Walk'),
    # Sister\'s Garden Loop listed as "Garden Loop" (0.25 mi) on current page
    ('OH-FR-T-0096', 0.25, INN_MAP, "Sister's Garden Loop (page: \"Garden Loop\")"),

    # --- Homestead ---
    # Source: https://www.metroparks.net/parks-and-trails/homestead/
    ('OH-FR-T-0097', 0.8, HST_MAP, 'Homestead Metro Park Trail (page: "Multiuse Trail")'),
]

conn = sqlite3.connect(DB)
cur = conn.cursor()
len_ok = 0
map_ok = 0

try:
    # Pre-flight: confirm all trail_ids exist
    missing = []
    for trail_id, *_ in UPDATES:
        cur.execute('SELECT count(*) FROM trails WHERE trail_id=?', (trail_id,))
        if cur.fetchone()[0] == 0:
            missing.append(trail_id)
    if missing:
        print(f'ERROR: trail_ids not found in DB: {missing}')
        sys.exit(1)
    print(f'Pre-flight OK: all {len(UPDATES)} trail_ids exist.')
    print()

    # Execute updates
    for trail_id, length_mi, maps_url, note in UPDATES:
        if length_mi is not None and maps_url is not None:
            cur.execute(
                'UPDATE trails SET length_mi=?, maps=?, updated_at=? WHERE trail_id=? AND length_mi IS NULL',
                (length_mi, maps_url, now, trail_id)
            )
            n = cur.rowcount
            len_ok += n
            map_ok += n
            print(f'  {trail_id}  length={length_mi} mi  maps=set  rows={n}  [{note}]')
        elif length_mi is not None:
            cur.execute(
                'UPDATE trails SET length_mi=?, updated_at=? WHERE trail_id=? AND length_mi IS NULL',
                (length_mi, now, trail_id)
            )
            n = cur.rowcount
            len_ok += n
            print(f'  {trail_id}  length={length_mi} mi  maps=skip  rows={n}  [{note}]')
        elif maps_url is not None:
            # Maps-only update — only set if currently NULL or empty
            cur.execute(
                'UPDATE trails SET maps=?, updated_at=? WHERE trail_id=? AND (maps IS NULL OR maps="")',
                (maps_url, now, trail_id)
            )
            n = cur.rowcount
            map_ok += n
            print(f'  {trail_id}  length=skip  maps=set  rows={n}  [{note}]')

    conn.commit()
    print()
    print(f'OK: COMMIT successful.')
    print(f'    length_mi updated: {len_ok} trail(s)')
    print(f'    maps updated:      {map_ok} trail(s)')
    print()

    # Post-flight
    print('Post-flight:')
    cur.execute("SELECT count(*) FROM trails WHERE trail_id LIKE 'OH-FR-T-%' AND length_mi IS NULL")
    remaining_null = cur.fetchone()[0]
    cur.execute("SELECT count(*) FROM trails WHERE trail_id LIKE 'OH-FR-T-%' AND length_mi IS NOT NULL")
    filled = cur.fetchone()[0]
    print(f'  OH-FR trails with length_mi filled: {filled}')
    print(f'  OH-FR trails still NULL:             {remaining_null}')
    if remaining_null:
        cur.execute("SELECT trail_id, name FROM trails WHERE trail_id LIKE 'OH-FR-T-%' AND length_mi IS NULL ORDER BY trail_id")
        for r in cur.fetchall():
            print(f'    {r[0]}  {r[1]}')

except Exception as e:
    conn.rollback()
    print(f'ERROR: {e}')
    sys.exit(1)
finally:
    conn.close()
