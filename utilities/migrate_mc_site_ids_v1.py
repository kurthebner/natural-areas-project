"""
migrate_mc_site_ids_v1.py
IMP-125: Fix non-zero-padded OH-MC-S-* site IDs to canonical 4-digit format.

Background:
  The Sandusky County pipeline generated OH-MC-S-* IDs without zero-padding
  (e.g. OH-MC-S-010 instead of OH-MC-S-0010). IMP-125 requires all OH-MC-S-*
  sequence numbers to be exactly 4 digits.

Collision:
  OH-MC-S-0012 already exists (Highbanks Metro Park, correctly padded from an
  earlier county run). OH-MC-S-012 (Van Tassel Wildlife Area) therefore cannot
  simply be padded -- it is remapped to OH-MC-S-0029 (next free sequence).

ID mapping:
  OH-MC-S-010  ->  OH-MC-S-0010   Magee Marsh Wildlife Area
  OH-MC-S-011  ->  OH-MC-S-0011   Missionary Island Wildlife Area
  OH-MC-S-012  ->  OH-MC-S-0029   Van Tassel Wildlife Area  [collision remap]
  OH-MC-S-021  ->  OH-MC-S-0021   Howard Marsh Metropark
  OH-MC-S-024  ->  OH-MC-S-0024   Oak Openings Preserve Metropark
  OH-MC-S-025  ->  OH-MC-S-0025   Oak Openings Beach Ridge Area
  OH-MC-S-027  ->  OH-MC-S-0027   Providence Metropark

FK cascade (confirmed by pre-script audit 2026-05-23):
  sites.site_id                   -- all 7
  access_points.parent_entity_id  -- OH-MC-S-010 (2), -024 (2), -025 (1), -027 (1)
  access_point_parents.parent_entity_id  -- OH-MC-S-010 (1)
  trail_parents.parent_site_id    -- OH-MC-S-010 (8)
  [OH-MC-S-012 has no FK references -- only sites.site_id updated]

Run from project root:
  python utilities/migrate_mc_site_ids_v1.py
"""

import sqlite3
import pathlib
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

PROJECT_ROOT = pathlib.Path(__file__).parent.parent
DB_PATH = PROJECT_ROOT / 'NASqlite' / 'natural_areas_v5.db'

# Explicit OLD -> NEW mapping (collision-safe)
ID_MAP = {
    'OH-MC-S-010': 'OH-MC-S-0010',
    'OH-MC-S-011': 'OH-MC-S-0011',
    'OH-MC-S-012': 'OH-MC-S-0029',   # collision remap
    'OH-MC-S-021': 'OH-MC-S-0021',
    'OH-MC-S-024': 'OH-MC-S-0024',
    'OH-MC-S-025': 'OH-MC-S-0025',
    'OH-MC-S-027': 'OH-MC-S-0027',
}

# (table, column) pairs — order: PKs first, then FKs
# Each entry also records which old IDs could appear in that column.
# We update all non_padded IDs for each column (safe — non-matching WHEREs are no-ops).
DB_TARGETS = [
    ('sites',                   'site_id'),
    ('access_points',           'parent_entity_id'),
    ('access_point_parents',    'parent_entity_id'),
    ('trail_parents',           'parent_site_id'),
]


def run():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    try:
        # --- Pre-flight ---
        print('Pre-flight checks')
        print('-' * 50)

        # Confirm all old IDs exist in sites
        missing = []
        for old_id in ID_MAP:
            cur.execute('SELECT count(*) FROM sites WHERE site_id=?', (old_id,))
            if cur.fetchone()[0] == 0:
                missing.append(old_id)
        if missing:
            print(f'ERROR: old IDs not found in sites: {missing}')
            sys.exit(1)
        print(f'  All {len(ID_MAP)} source IDs confirmed in sites.')

        # Confirm new IDs don't already exist (collision check) -- except 0012 which we know about
        collisions = []
        for old_id, new_id in ID_MAP.items():
            cur.execute('SELECT site_id, name FROM sites WHERE site_id=?', (new_id,))
            r = cur.fetchone()
            if r and old_id != 'OH-MC-S-012':
                # Unexpected collision
                collisions.append((new_id, r[1]))
            elif r and old_id == 'OH-MC-S-012':
                # Known collision -- we already remapped 012 -> 0029, so 0029 should be free
                # This branch checks that 0029 itself is actually free
                pass
        if collisions:
            print(f'ERROR: unexpected collisions: {collisions}')
            sys.exit(1)

        # Confirm the remap target (0029) is free
        cur.execute("SELECT count(*) FROM sites WHERE site_id='OH-MC-S-0029'")
        if cur.fetchone()[0] != 0:
            print('ERROR: OH-MC-S-0029 already exists -- choose a different remap target.')
            sys.exit(1)
        print('  Remap target OH-MC-S-0029 is free.')

        # Pre-flight row counts
        print()
        print('Expected row counts per table/column:')
        for tbl, col in DB_TARGETS:
            old_ids = list(ID_MAP.keys())
            placeholders = ','.join(['?' for _ in old_ids])
            cur.execute(f'SELECT count(*) FROM {tbl} WHERE {col} IN ({placeholders})', old_ids)
            n = cur.fetchone()[0]
            print(f'  {tbl}.{col}: {n} row(s) to update')

        print()
        input('Pre-flight OK. Press Enter to execute migration (Ctrl-C to abort)...')
        print()

        # --- Execute updates in one transaction ---
        total_updated = 0
        for tbl, col in DB_TARGETS:
            tbl_updated = 0
            for old_id, new_id in ID_MAP.items():
                cur.execute(
                    f'UPDATE {tbl} SET {col}=? WHERE {col}=?',
                    (new_id, old_id)
                )
                n = cur.rowcount
                if n:
                    print(f'  {tbl}.{col}: {old_id} -> {new_id}  ({n} row)')
                tbl_updated += n
            total_updated += tbl_updated

        conn.commit()
        print()
        print(f'COMMIT OK -- {total_updated} total rows updated.')
        print()

        # --- Post-flight ---
        print('Post-flight verification')
        print('-' * 50)

        # Confirm no old IDs remain
        all_old = list(ID_MAP.keys())
        placeholders = ','.join(['?' for _ in all_old])
        for tbl, col in DB_TARGETS:
            cur.execute(f'SELECT {col} FROM {tbl} WHERE {col} IN ({placeholders})', all_old)
            stale = cur.fetchall()
            if stale:
                print(f'  WARN: stale old IDs in {tbl}.{col}: {stale}')
            else:
                print(f'  OK:  {tbl}.{col} -- no old IDs remain')

        print()
        # Confirm all new IDs exist in sites
        all_new = list(ID_MAP.values())
        cur.execute(f'SELECT site_id, name FROM sites WHERE site_id IN ({placeholders})', all_new)
        found = cur.fetchall()
        print(f'New site IDs now in DB ({len(found)}/{len(all_new)}):')
        for sid, name in sorted(found):
            print(f'  {sid}  {name}')

        print()
        # Spot-check trail_parents integrity
        cur.execute("SELECT count(*) FROM trail_parents WHERE parent_site_id='OH-MC-S-0010'")
        n = cur.fetchone()[0]
        print(f'trail_parents -> OH-MC-S-0010: {n} row(s) (expect 8)')

        cur.execute("SELECT count(*) FROM access_points WHERE parent_entity_id='OH-MC-S-0010'")
        n = cur.fetchone()[0]
        print(f'access_points -> OH-MC-S-0010: {n} row(s) (expect 2)')

        # Show all OH-MC-S IDs for final sanity check
        print()
        cur.execute("SELECT site_id, name FROM sites WHERE site_id LIKE 'OH-MC-S-%' ORDER BY site_id")
        rows = cur.fetchall()
        print(f'All OH-MC-S sites after migration ({len(rows)}):')
        for sid, name in rows:
            seq = sid.split('-')[-1]
            flag = '  WARN: not 4-digit' if len(seq) != 4 else ''
            print(f'  {sid}  {name}{flag}')

    except KeyboardInterrupt:
        conn.rollback()
        print()
        print('Aborted -- rollback.')
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
