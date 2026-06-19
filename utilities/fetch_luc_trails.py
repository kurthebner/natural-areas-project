"""
Fetch trail lengths from metroparkstoledo.com individual trail pages.
Prints a structured result for each OH-LUC trail so we can write the update script.
Run from project root:
  python utilities/fetch_luc_trails.py
"""
import sqlite3
import urllib.request
import re
import time
import sys

sys.stdout.reconfigure(encoding='utf-8')

DB = 'NASqlite/natural_areas_v5.db'

# Only the metroparkstoledo.com trails (individual trail pages)
conn = sqlite3.connect(DB)
cur = conn.cursor()
cur.execute("""SELECT trail_id, name, url_primary FROM trails
               WHERE trail_id LIKE 'OH-LUC-T-%'
               AND length_mi IS NULL
               AND url_primary LIKE 'https://metroparkstoledo.com/trails/%'
               ORDER BY trail_id""")
trails = cur.fetchall()
conn.close()

print(f'Fetching {len(trails)} metroparkstoledo.com trail pages...')
print()

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Accept': 'text/html',
}

results = []
for trail_id, name, url in trails:
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=15) as resp:
            html = resp.read().decode('utf-8', errors='replace')

        # Extract length — "Length: 1.6 miles" or "Length: 1.6 mi"
        m = re.search(r'Length[:\s]+([0-9.]+)\s*miles?', html, re.IGNORECASE)
        length = float(m.group(1)) if m else None

        # Extract map PDF link
        pdf_m = re.search(r'href=["\']([^"\']*\.pdf)["\']', html, re.IGNORECASE)
        map_url = pdf_m.group(1) if pdf_m else None
        if map_url and not map_url.startswith('http'):
            map_url = 'https://metroparkstoledo.com' + map_url

        status = 'OK' if length else 'NO_LENGTH'
        print(f'  {trail_id}  {length} mi  {status}  [{name}]')
        if map_url:
            print(f'           map: {map_url}')
        results.append((trail_id, name, url, length, map_url))
        time.sleep(0.3)  # polite crawl delay

    except Exception as e:
        print(f'  {trail_id}  ERROR: {e}  [{name}]')
        results.append((trail_id, name, url, None, None))

print()
print(f'Done. {sum(1 for r in results if r[3] is not None)} of {len(results)} lengths found.')

# Print summary of what was NOT found
no_length = [r for r in results if r[3] is None]
if no_length:
    print('No length found for:')
    for r in no_length:
        print(f'  {r[0]}  {r[1]}')
