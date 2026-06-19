"""
wod_site_disposition_v1.py
Wood County site verification disposition — 2026-05-23

Actions:

OH-WOD-SI-028  Nature Trails Park (WCPD)
  Keep Active. Confirmed as a current WCPD property via WCPD Facebook posts
  (new playground installed ~late 2025) and repeated citation in BSBO/Biggest
  Week in American Birding field trip materials. Not listed at its own URL on
  the redesigned wcparks.org; update url_primary to main parks page.
  Clear verification-flag language from notes; replace with current finding.

OH-WOD-SI-034  Wakeman Preserve
  DELETE. AutoRecovered baseline phantom. Zero web evidence of a WCPD property
  by this name. "Wakeman" refers to Wakeman, Ohio (Huron County) -- not a Wood
  County location. The real entities (Wakeman Community Park, Augusta-Anne Olsen
  Nature Preserve) belong in the Huron County pipeline and are not yet in the DB.
  No FK references -- safe to delete.

OH-WOD-SI-035  White Star Park
  DELETE. Duplicate of OH-SAN-S-023 (White Star Park, Sandusky County Park
  District, 797 acres, Gibsonburg, OH 44833). AutoRecovered baseline incorrectly
  attributed this Sandusky County property to Wood County Park District.
  No FK references -- safe to delete.

OH-WOD-SEED-001  Devils Hole Prairie
OH-WOD-SEED-002  Hulls Prairie
OH-WOD-SEED-003  Tontogany Prairie
OH-WOD-SEED-004  North Baltimore Reservoir
  Keep in held_entities. Update hold_detail to clarify GNIS geographic feature
  status with no managing agency. User decision: retain for historical tracking.

Run from project root:
  python utilities/wod_site_disposition_v1.py
"""

import sqlite3
import datetime
import pathlib
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

PROJECT_ROOT = pathlib.Path(__file__).parent.parent
DB_PATH = PROJECT_ROOT / 'NASqlite' / 'natural_areas_v5.db'

now = datetime.datetime.now(datetime.UTC).strftime('%Y-%m-%dT%H:%M:%SZ')

# --- Action definitions ---

SI_028_URL = 'https://wcparks.org/parks/'
SI_028_NOTES = (
    'Confirmed active WCPD property as of 2026-05-23. Cited in WCPD Facebook '
    'posts (new playground installation, ~late 2025) and repeatedly in Black '
    'Swamp Bird Observatory and Biggest Week in American Birding field trip '
    'itineraries as a current Wood County Park District site, paired with '
    'Cedar Creeks Preserve. Not listed at its own URL on redesigned wcparks.org '
    '(wcparks.org/parks/nature-trails-park/ returns 404); url_primary updated '
    'to main parks page. Known location: Gypsy Lane Road, Bowling Green, behind '
    'Wood County Justice Center Complex. Astronomical observation program '
    '(large telescope) noted in original discovery record. GPS still needed.'
)

SEED_DETAILS = {
    'OH-WOD-SEED-001': (
        'GNIS geographic feature: Devils Hole Prairie, Webster Township, Wood County, OH. '
        'Coordinates N41.4501, W83.5624 (USGS Dunbridge quad). Historical place name '
        'for a Black Swamp prairie remnant; mentioned in 2017 Sentinel-Tribune '
        'place-names article. No managing agency identified. Not in ODNR DNAP '
        'registry, BSC owned-land inventory, or any public land database. '
        'Retained for historical tracking only -- not a managed natural area.'
    ),
    'OH-WOD-SEED-002': (
        'GNIS geographic feature: Hulls Prairie, near Perrysburg, Wood County, OH. '
        'Historical place name for a Black Swamp prairie remnant. Location now '
        'largely occupied by Hull Prairie Farms residential subdivision (confirmed '
        'via Nominatim 2026-05-22). No managing agency identified. Not in BSC '
        'owned-land inventory. Prairie likely extirpated. '
        'Retained for historical tracking only -- not a managed natural area.'
    ),
    'OH-WOD-SEED-003': (
        'GNIS geographic feature: Tontogany Prairie, near Tontogany village, '
        'Wood County, OH. Historical place name for a Black Swamp prairie remnant. '
        'No managed public access found via Nominatim, BSC, or web search '
        '(2026-05-22). No managing agency identified. '
        'Retained for historical tracking only -- not a managed natural area.'
    ),
    'OH-WOD-SEED-004': (
        'GNIS/baseline feature: North Baltimore Reservoir, North Baltimore, '
        'Wood County, OH. Municipal water utility reservoir; not a public natural '
        'area. Village Park entity (disc golf/fishing pond, OH-WOD-SI-067) '
        'recorded separately. No managing natural-areas agency. '
        'Retained for historical tracking only -- not a managed natural area.'
    ),
}

DELETE_SITES = {
    'OH-WOD-SI-034': (
        'Wakeman Preserve -- AutoRecovered baseline phantom. Zero web evidence of '
        'a WCPD property by this name. "Wakeman" refers to Wakeman, Ohio (Huron '
        'County) -- outside WCPD service territory. Real Wakeman entities '
        '(Wakeman Community Park; Augusta-Anne Olsen Nature Preserve) belong in '
        'the Huron County pipeline. No FK references.'
    ),
    'OH-WOD-SI-035': (
        'White Star Park -- duplicate of OH-SAN-S-023 (Sandusky County Park '
        'District, 797 acres, Gibsonburg OH 44833). AutoRecovered baseline '
        'incorrectly attributed this Sandusky County property to WCPD. '
        'No FK references.'
    ),
}


def run():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    try:
        print('Pre-flight checks')
        print('-' * 50)

        # Confirm SI-028 exists
        cur.execute("SELECT site_id, name FROM sites WHERE site_id='OH-WOD-SI-028'")
        r = cur.fetchone()
        print(f'  OH-WOD-SI-028: {"FOUND -- " + r[1] if r else "NOT FOUND"}')

        # Confirm deletions exist and have no FK references
        fk_checks = [
            ('access_points',        'parent_entity_id'),
            ('access_point_parents', 'parent_entity_id'),
            ('trail_parents',        'parent_site_id'),
            ('site_parent',          'site_id'),
            ('site_parent',          'parent_site_id'),
            ('site_network_members', 'site_id'),
        ]
        for sid, reason in DELETE_SITES.items():
            cur.execute('SELECT site_id, name FROM sites WHERE site_id=?', (sid,))
            r = cur.fetchone()
            found = r[1] if r else 'NOT FOUND'
            refs = []
            for tbl, col in fk_checks:
                cur.execute(f'SELECT count(*) FROM {tbl} WHERE {col}=?', (sid,))
                n = cur.fetchone()[0]
                if n:
                    refs.append(f'{tbl}.{col}={n}')
            status = 'FK REFS: ' + ', '.join(refs) if refs else 'no FK refs'
            print(f'  {sid}: {found}  [{status}]')
            if refs:
                print(f'    ERROR: cannot delete -- FK references must be resolved first.')
                sys.exit(1)

        # Confirm SEED entities exist in held_entities
        for seed_id in SEED_DETAILS:
            cur.execute('SELECT record_id, name FROM held_entities WHERE record_id=?', (seed_id,))
            r = cur.fetchone()
            print(f'  {seed_id}: {"FOUND -- " + r[1] if r else "NOT FOUND"}')

        print()
        input('Pre-flight OK. Press Enter to execute (Ctrl-C to abort)...')
        print()

        # --- OH-WOD-SI-028: update url_primary and notes ---
        cur.execute(
            'UPDATE sites SET url_primary=?, notes=?, updated_at=? WHERE site_id=?',
            (SI_028_URL, SI_028_NOTES, now, 'OH-WOD-SI-028')
        )
        print(f'  Updated OH-WOD-SI-028: url_primary + notes ({cur.rowcount} row)')

        # --- Delete OH-WOD-SI-034 and OH-WOD-SI-035 ---
        for sid, reason in DELETE_SITES.items():
            cur.execute('DELETE FROM sites WHERE site_id=?', (sid,))
            n = cur.rowcount
            print(f'  Deleted {sid}: {n} row(s)  [{reason[:60]}...]')

        # --- Update SEED hold_detail ---
        for seed_id, new_detail in SEED_DETAILS.items():
            cur.execute(
                'UPDATE held_entities SET hold_detail=? WHERE record_id=?',
                (new_detail, seed_id)
            )
            print(f'  Updated held_entities: {seed_id} ({cur.rowcount} row)')

        conn.commit()
        print()
        print('COMMIT OK')
        print()

        # --- Post-flight ---
        print('Post-flight verification')
        print('-' * 50)

        cur.execute(
            "SELECT site_id, name, status, url_primary FROM sites WHERE site_id='OH-WOD-SI-028'"
        )
        r = cur.fetchone()
        print(f'  OH-WOD-SI-028: {r}')

        for sid in DELETE_SITES:
            cur.execute('SELECT count(*) FROM sites WHERE site_id=?', (sid,))
            n = cur.fetchone()[0]
            print(f'  {sid} in sites: {n} (expect 0)')

        print()
        print('  SEED hold_detail previews:')
        for seed_id in SEED_DETAILS:
            cur.execute(
                'SELECT record_id, hold_detail FROM held_entities WHERE record_id=?',
                (seed_id,)
            )
            r = cur.fetchone()
            if r:
                preview = r[1][:90] + '...' if len(r[1]) > 90 else r[1]
                print(f'    {r[0]}: {preview}')

        print()
        # Wood County site count after deletions
        cur.execute("SELECT count(*) FROM sites WHERE site_id LIKE 'OH-WOD-%'")
        print(f'  OH-WOD-* sites remaining: {cur.fetchone()[0]}')

    except KeyboardInterrupt:
        conn.rollback()
        print()
        print('Aborted -- rollback. No changes made.')
        sys.exit(0)
    except Exception as e:
        conn.rollback()
        print(f'ERROR: {e}')
        import traceback
        traceback.print_exc()
        sys.exit(1)
    finally:
        conn.close()


if __name__ == '__main__':
    run()
