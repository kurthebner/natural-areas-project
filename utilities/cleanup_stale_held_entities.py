"""
cleanup_stale_held_entities.py
IMP-123: Remove stale held_entities rows after pipeline upserts.

Problem:
  When a held entity is released (GPS acquired, cross-county partner run, etc.)
  and the entity is upserted into the main entity table, the corresponding
  held_entities row is never deleted. This creates orphan held rows that
  misrepresent the held count and confuse audit queries.

What this script does:
  1. Finds all held_entities rows where record_id also exists in the
     corresponding entity table (sites, trails, access_points, etc.).
  2. For each stale row: if hold_detail is substantive (not a generic
     pipeline-generated string), appends it to the entity's notes field
     so no information is lost.
  3. Deletes the stale held_entities rows.
  4. Prints a full audit report.

Entity type -> table/PK mapping:
  Site          -> sites.site_id
  Trail         -> trails.trail_id
  Trail Segment -> trail_segments.segment_id
  Trail Network -> trail_networks.network_id
  Site Network  -> site_networks.network_id
  Access Point  -> access_points.access_point_id

Run after any Stage 6 upsert to reconcile held_entities:
  python utilities/cleanup_stale_held_entities.py

Run from project root.
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

# entity_type string -> (entity table, pk column, notes column or None)
ENTITY_MAP = {
    'Site':          ('sites',          'site_id',           'notes'),
    'Trail':         ('trails',         'trail_id',          'notes'),
    'Trail Segment': ('trail_segments', 'segment_id',        None),
    'Trail Network': ('trail_networks', 'network_id',        None),
    'Site Network':  ('site_networks',  'network_id',        None),
    'Access Point':  ('access_points',  'access_point_id',   'notes'),
}

# Strings that are purely pipeline-generated boilerplate — not worth migrating to notes
BOILERPLATE_PATTERNS = [
    'HELD|cross_county_held',
    'HELD - cross-county',
    'HELD: cross-county',
    'cross-county or access unconfirmed',
    'parent_held',
]


def is_boilerplate(text: str) -> bool:
    if not text or not text.strip():
        return True
    t = text.strip().lower()
    for pat in BOILERPLATE_PATTERNS:
        if pat.lower() in t:
            return True
    return False


def run():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    try:
        # --- Detect stale rows ---
        cur.execute(
            'SELECT held_id, record_id, entity_type, hold_reason, hold_detail '
            'FROM held_entities ORDER BY record_id'
        )
        all_held = cur.fetchall()

        stale = []
        skipped_unknown_type = []

        for held_id, record_id, entity_type, hold_reason, hold_detail in all_held:
            if entity_type not in ENTITY_MAP:
                skipped_unknown_type.append((held_id, record_id, entity_type))
                continue
            tbl, pk_col, _ = ENTITY_MAP[entity_type]
            cur.execute(f'SELECT count(*) FROM {tbl} WHERE {pk_col}=?', (record_id,))
            if cur.fetchone()[0] > 0:
                stale.append((held_id, record_id, entity_type, hold_reason, hold_detail))

        print(f'held_entities: {len(all_held)} total, {len(stale)} stale.')
        if skipped_unknown_type:
            print(f'Skipped (unknown entity_type): {skipped_unknown_type}')
        print()

        if not stale:
            print('No stale rows found -- nothing to do.')
            conn.close()
            return

        print('Stale rows to remove:')
        for held_id, record_id, entity_type, hold_reason, hold_detail in stale:
            detail_preview = (hold_detail or '')[:80].replace('\n', ' ')
            migrate = not is_boilerplate(hold_detail)
            flag = '  [NOTE->notes]' if migrate else ''
            print(f'  held_id={held_id}  {record_id}  ({entity_type})  reason={hold_reason}{flag}')
            if migrate:
                print(f'    detail: {detail_preview}...' if len(hold_detail or '') > 80 else f'    detail: {detail_preview}')
        print()
        input('Press Enter to proceed (Ctrl-C to abort)...')
        print()

        # --- Migrate substantive notes, then delete ---
        notes_migrated = 0
        rows_deleted = 0

        for held_id, record_id, entity_type, hold_reason, hold_detail in stale:
            tbl, pk_col, notes_col = ENTITY_MAP[entity_type]

            # Migrate hold_detail to entity notes if substantive
            if notes_col and not is_boilerplate(hold_detail):
                # Read current notes value
                cur.execute(f'SELECT {notes_col} FROM {tbl} WHERE {pk_col}=?', (record_id,))
                row = cur.fetchone()
                current_notes = (row[0] or '').strip() if row else ''

                # Only append if not already present
                detail_clean = (hold_detail or '').strip()
                if detail_clean and detail_clean not in current_notes:
                    if current_notes:
                        new_notes = current_notes + ' | ' + detail_clean
                    else:
                        new_notes = detail_clean
                    cur.execute(
                        f'UPDATE {tbl} SET {notes_col}=?, updated_at=? WHERE {pk_col}=?',
                        (new_notes, now, record_id)
                    )
                    print(f'  Migrated note: {record_id} -> {tbl}.notes')
                    notes_migrated += 1

            # Delete the stale held_entities row
            cur.execute('DELETE FROM held_entities WHERE held_id=?', (held_id,))
            rows_deleted += cur.rowcount
            print(f'  Deleted held_id={held_id}  {record_id}')

        conn.commit()
        print()
        print(f'COMMIT OK -- {rows_deleted} stale held row(s) deleted, {notes_migrated} note(s) migrated.')
        print()

        # --- Post-flight ---
        cur.execute('SELECT count(*) FROM held_entities')
        remaining = cur.fetchone()[0]
        print(f'held_entities remaining: {remaining}')

        # Confirm none of the deleted record_ids are still in held_entities
        stale_ids = [r[1] for r in stale]
        placeholders = ','.join(['?' for _ in stale_ids])
        cur.execute(
            f'SELECT record_id FROM held_entities WHERE record_id IN ({placeholders})',
            stale_ids
        )
        still_present = cur.fetchall()
        if still_present:
            print(f'WARN: {len(still_present)} stale record_ids still in held_entities: {still_present}')
        else:
            print('OK: no stale record_ids remain in held_entities.')

        if notes_migrated:
            print()
            print(f'Notes migrated to entity tables ({notes_migrated}):')
            for held_id, record_id, entity_type, hold_reason, hold_detail in stale:
                if not is_boilerplate(hold_detail):
                    tbl, pk_col, notes_col = ENTITY_MAP[entity_type]
                    if notes_col:
                        cur.execute(
                            f'SELECT {notes_col} FROM {tbl} WHERE {pk_col}=?',
                            (record_id,)
                        )
                        row = cur.fetchone()
                        preview = (row[0] or '')[:120] if row else 'NOT FOUND'
                        print(f'  {record_id}: {preview}...' if len(row[0] or '') > 120 else f'  {record_id}: {preview}')

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
