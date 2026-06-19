"""
Wayne County small village park description update
Fills in descriptions, features, notes, and URLs for 13 parks with
stub or missing descriptions. Source: official village websites and
authoritative secondary sources, researched 2026-05-22.
"""
import sqlite3
import datetime
import sys

sys.stdout.reconfigure(encoding='utf-8')

DB = 'NASqlite/natural_areas_v5.db'
now = datetime.datetime.now(datetime.UTC).strftime('%Y-%m-%dT%H:%M:%SZ')

UPDATES = {
    'OH-WA-S-0022': {
        'description': (
            'Village of Apple Creek community park featuring Mayer Carson Hall, a large pavilion, a small pavilion, '
            'a lighted ball diamond, and a stage. Facilities are available for community events and private rentals '
            'through Village Hall at 63 East Main Street.'
        ),
        'features': 'Ball Diamond;Pavilion',
        'notes': 'Pavilion and facility rentals require a completed Park-Facility Usage Agreement; contact Village Hall at 330-698-5462.',
        'url_primary': 'https://www.apple-creek.org/park',
    },
    'OH-WA-S-0023': {
        'description': (
            'Primary community park in Creston at 10399 Wooster Pike, featuring paved walking paths, athletic fields, '
            'and recreational amenities. Multiple rentable event spaces include the Creston Community Center (capacity 105), '
            'Murray Hall (capacity 80), and two additional buildings (each capacity 45). Athletic fields and tree plantings '
            'throughout the park serve as community memorials honoring local residents.'
        ),
        'features': 'Ball Diamond;Community Center;Playground',
        'notes': 'Facility rentals through Village Hall (330-435-6021). Community Center full-day rate: $75 residents / $100 non-residents.',
        'url_primary': 'https://www.crestonvillage.org',
    },
    'OH-WA-S-0024': {
        'description': (
            'Small neighborhood park in Creston at 165 N Main Street, located near the western terminus of the County Line '
            'Trail. Serves as a community green space and provides parking and trail access for the County Line Trail.'
        ),
        'features': 'Parking Lot',
        'notes': 'Western trailhead access point for the County Line Trail, which connects to Martin Fritz Memorial Park (Rittman) to the east.',
        'url_primary': 'https://www.crestonvillage.org',
    },
    'OH-WA-S-0028': {
        'description': (
            'Hilltop recreation area in Rittman named for E.J. Young, founder of the Wayne Salt Company, which later became '
            'the Ohio Salt Company and eventually Morton Salt. The elevated site offers views across the city and features '
            'baseball and softball diamonds, a pavilion with picnic areas, and playground equipment.'
        ),
        'features': 'Ball Diamond;Pavilion;Picnic Area;Playground',
        'notes': 'GPS coordinates are approximate (intersection geocode only); no standalone Google Maps listing. Listed on the City of Rittman City Parks page.',
        'url_primary': 'https://www.rittman.com/page/city-parks',
    },
    'OH-WA-S-0029': {
        'description': (
            'Small neighborhood park in Rittman at the corner of Washington Street and North Metzger Avenue. '
            'Provides basic play equipment including a swing set.'
        ),
        'features': 'Playground',
        'notes': 'GPS coordinates are approximate (intersection geocode only); no standalone Google Maps listing.',
        'url_primary': 'https://www.rittman.com/page/city-parks',
    },
    'OH-WA-S-0031': {
        'description': (
            'Community park in Marshallville at 48 Park Street featuring a playground, basketball court, ball fields, '
            'and an outdoor pavilion. Klusch Hall, located within the park complex, serves as a community meeting and '
            'election venue. The north end of the park hosts the annual Marshallville Antique Tractor Pull.'
        ),
        'features': 'Ball Diamond;Basketball Court;Pavilion;Playground',
        'notes': 'Klusch Hall used as Wayne County Board of Elections polling location. Annual Marshallville Antique Tractor Pull held on the north end of the park (330-464-1314).',
        'url_primary': '',
    },
    'OH-WA-S-0032': {
        'description': (
            'Central community park in Smithville serving as the primary gathering space for residents. Features two baseball '
            'fields including Nate Butcher Field No. 1 and Field No. 2 with a batting cage (added 2024), paved walking paths '
            '(completed 2023), basketball courts, a soccer field, a Veterans Memorial, and a rentable pavilion with restrooms. '
            'Ongoing improvements are guided by a Village Citizens Park Committee with support from the Wayne County Community Foundation.'
        ),
        'features': 'Ball Diamond;Basketball Court;Pavilion;Restrooms;Soccer Pitch',
        'notes': 'Open March 1-Oct 31: 8am-11pm; Nov 1-March 1: 8am-9pm. Upper Park closed Nov-March. Pavilion reservable through Village Hall (330-669-2311); $30 rental fee.',
        'url_primary': 'https://thevillageofsmithville.com/parks-recreation/',
    },
    'OH-WA-S-0033': {
        'description': (
            'Community park and rentable gathering facility in West Salem. The community building offers a full kitchen, '
            'heating, two restrooms, and six indoor picnic tables, with four additional tables under an adjacent outdoor '
            'pavilion. A fishing pond next to the building is open to the public at no charge. Construction was funded '
            'in part through the Ohio Department of Natural Resources.'
        ),
        'features': 'Fishing Area;Pavilion;Picnic Area;Restrooms',
        'notes': 'Building reservable through Village Hall; $100 rental fee plus $50 refundable security deposit. Key must be picked up the business day before the reservation.',
        'url_primary': 'https://westsalemvillage.com',
    },
    'OH-WA-S-0034': {
        'description': (
            'Village of Burbank community park at 100 W Middle Street, serving as the primary outdoor recreational space for the village.'
        ),
        'features': None,
        'notes': None,
        'url_primary': None,
    },
    'OH-WA-S-0038': {
        'description': (
            'Village of Fredericksburg community park serving as the primary recreation area for the village, '
            'located near the northern trailhead of the Holmes County Trail.'
        ),
        'features': None,
        'notes': None,
        'url_primary': None,
    },
    'OH-WA-S-0040': {
        'description': (
            'Small community park in the Village of Mt. Eaton. An Ohio Nature Works grant funded resurfacing of asphalt '
            'recreational surfaces and replacement of benches as part of a family fitness and recreation improvement project.'
        ),
        'features': None,
        'notes': None,
        'url_primary': None,
    },
    'OH-WA-S-0041': {
        'description': (
            'Primary village park in Shreve at 250 Park Drive, serving as a community gathering and recreational space '
            'with a pavilion available for events.'
        ),
        'features': 'Pavilion',
        'notes': None,
        'url_primary': 'https://www.shrevevillagehall.org',
    },
    'OH-WA-S-0042': {
        'description': (
            'Sports and recreation park in Shreve named for Harold D. Miller, featuring baseball fields. A 2024 capital '
            'improvement project funded with $300,000 in state grants is adding a pavilion and stage for community festivals, '
            'two parking areas off Market and Wells Streets, grounds lighting, and utility service connections.'
        ),
        'features': 'Ball Diamond',
        'notes': '2024 improvement project funded through Ohio Senate District 31 Capital Budget. Improvements include pavilion/stage, parking areas, lighting, and power/water service.',
        'url_primary': 'https://www.shrevevillagehall.org/shreve-announces-300-000-for-harold-d-miller-park',
    },
}

conn = sqlite3.connect(DB)
cur = conn.cursor()
ok = 0
try:
    for site_id, vals in UPDATES.items():
        cur.execute(
            'UPDATE sites SET description=?, features=?, notes=?, url_primary=?, updated_at=? WHERE site_id=?',
            (vals['description'], vals['features'], vals['notes'], vals['url_primary'], now, site_id)
        )
        print(f'  {site_id}: {cur.rowcount} row(s) updated')
        ok += cur.rowcount
    conn.commit()
    print(f'OK: COMMIT successful. {ok} total rows updated.')
except Exception as e:
    conn.rollback()
    print(f'ERROR: {e}')
finally:
    conn.close()
