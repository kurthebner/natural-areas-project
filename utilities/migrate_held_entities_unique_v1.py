"""
migrate_held_entities_unique_v1.py
IMP-127: Add UNIQUE(record_id) constraint to the held_entities table.

Background:
  held_entities has no UNIQUE constraint on record_id. INSERT OR IGNORE
  suppresses only PRIMARY KEY conflicts, so every pipeline re-run on a county
  with remaining held entities silently inserts duplicate rows. Found 2026-05-22;
  11 duplicate rows required manual deduplication during Sandusky GPS release.

Approach:
  SQLite does not support ADD CONSTRAINT after the fact. Required steps:
    1. Create held_entities_new with identical schema + UNIQUE(record_id)
    2. INSERT INTO held_entities_new SELECT * FROM held_entities
       (fails fast if any duplicate record_id exists — fix first)
    3. DROP TABLE held_entities
    4. ALTER TABLE held_entities_new RENAME TO held_entities

Pre-flight:
  - Confirm no duplicate record_id values (deduplication required before migration)
  - Show row count to be preserved
  - Verify held_entities_new does not already exist

Post-flight:
  - Confirm row count matches
  - Confirm UNIQUE index is present via PRAGMA index_list
  - Spot-check a few record_ids

Run from project root:
  python utilities/migrate_held_entities_unique_v1.py
"""

import sqlite3
import pathlib
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

PROJECT_ROOT = pathlib.Path(__file__).parent.parent
DB_PATH = PROJECT_ROOT / 'NASqlite' / 'natural_areas_v5.db'

NEW_TABLE_DDL = """
CREATE TABLE held_entities_new (
    held_id     INTEGER PRIMARY KEY AUTOINCREMENT,
    record_id   TEXT NOT NULL,
    entity_type TEXT NOT NULL,
    name        TEXT NOT NULL,
    county      TEXT,
    hold_reason TEXT,
    hold_detail TEXT,
    run_id      TEXT,
    created_at  TEXT,
    UNIQUE(record_id)
)
""".strip()


def run():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    try:
        # --- Pre-flight ---
        print('Pre-flight checks')
        print('-' * 50)

        # Confirm current schema has record_id
        cur.execute('PRAGMA table_info(held_entities)')
        cols = {r[1]: r for r in cur.fetchall()}
        if 'record_id' not in cols:
            print('ERROR: held_entities does not have a record_id column. Check schema.')
            sys.exit(1)
        print(f'  Columns confirmed: {list(cols.keys())}')

        # Confirm no UNIQUE constraint already exists on record_id
        cur.execute('PRAGMA index_list(held_entities)')
        indexes = cur.fetchall()
        for idx in indexes:
            if idx[2]:  # unique flag
                cur.execute(f'PRAGMA index_info({idx[1]})')
                idx_cols = [r[2] for r in cur.fetchall()]
                if 'record_id' in idx_cols:
                    print('  UNIQUE(record_id) already exists -- nothing to do.')
                    sys.exit(0)
        print('  No existing UNIQUE(record_id) constraint -- migration needed.')

        # Row count
        cur.execute('SELECT count(*) FROM held_entities')
        row_count = cur.fetchone()[0]
        print(f'  Current row count: {row_count}')

        # Duplicate check
        cur.execute(
            'SELECT record_id, count(*) as n FROM held_entities '
            'GROUP BY record_id HAVING n > 1'
        )
        dups = cur.fetchall()
        if dups:
            print(f'  ERROR: {len(dups)} duplicate record_id value(s) found:')
            for d in dups:
                print(f'    {d[0]}  ({d[1]} rows)')
            print()
            print('  Deduplicate first (keep MIN(held_id) per record_id) then re-run.')
            print('  SQL to deduplicate:')
            print('    DELETE FROM held_entities')
            print('    WHERE held_id NOT IN (')
            print('      SELECT MIN(held_id) FROM held_entities GROUP BY record_id')
            print('    );')
            sys.exit(1)
        print(f'  No duplicate record_ids -- safe to migrate.')

        # Confirm held_entities_new does not exist
        cur.execute(
            "SELECT count(*) FROM sqlite_master "
            "WHERE type='table' AND name='held_entities_new'"
        )
        if cur.fetchone()[0]:
            print('  ERROR: held_entities_new already exists. Drop it first.')
            sys.exit(1)
        print('  held_entities_new does not exist -- clear to create.')

        print()
        input('Pre-flight OK. Press Enter to execute migration (Ctrl-C to abort)...')
        print()

        # --- Execute migration in one transaction ---
        print('Step 1: Create held_entities_new with UNIQUE(record_id)...')
        cur.execute(NEW_TABLE_DDL)

        print('Step 2: Copy all rows from held_entities to held_entities_new...')
        cur.execute(
            'INSERT INTO held_entities_new '
            '(held_id, record_id, entity_type, name, county, '
            ' hold_reason, hold_detail, run_id, created_at) '
            'SELECT held_id, record_id, entity_type, name, county, '
            '       hold_reason, hold_detail, run_id, created_at '
            'FROM held_entities'
        )
        copied = cur.rowcount
        print(f'  Copied: {copied} row(s)')

        print('Step 3: Drop old held_entities...')
        cur.execute('DROP TABLE held_entities')

        print('Step 4: Rename held_entities_new -> held_entities...')
        cur.execute('ALTER TABLE held_entities_new RENAME TO held_entities')

        conn.commit()
        print()
        print('COMMIT OK')
        print()

        # --- Post-flight ---
        print('Post-flight verification')
        print('-' * 50)

        cur.execute('SELECT count(*) FROM held_entities')
        new_count = cur.fetchone()[0]
        count_ok = new_count == row_count
        print(f'  Row count: {new_count} (expected {row_count}) -- {"OK" if count_ok else "MISMATCH!"}')

        # Confirm UNIQUE index present
        cur.execute('PRAGMA index_list(held_entities)')
        indexes = cur.fetchall()
        unique_found = False
        for idx in indexes:
            if idx[2]:  # unique flag
                cur.execute(f'PRAGMA index_info({idx[1]})')
                idx_cols = [r[2] for r in cur.fetchall()]
                if 'record_id' in idx_cols:
                    unique_found = True
                    print(f'  UNIQUE(record_id) index confirmed: {idx[1]}')
        if not unique_found:
            print('  WARN: UNIQUE(record_id) index NOT found -- check migration.')

        # Confirm schema
        cur.execute('PRAGMA table_info(held_entities)')
        new_cols = [r[1] for r in cur.fetchall()]
        print(f'  Columns: {new_cols}')

        # Spot-check a few record_ids
        cur.execute(
            'SELECT held_id, record_id, entity_type, hold_reason '
            'FROM held_entities ORDER BY held_id LIMIT 5'
        )
        print()
        print('  First 5 rows (spot-check):')
        for r in cur.fetchall():
            print(f'    {r}')

        print()
        if count_ok and unique_found:
            print('IMP-127 migration complete. held_entities now has UNIQUE(record_id).')
        else:
            print('WARNING: post-flight checks failed -- review output above.')

    except KeyboardInterrupt:
        conn.rollback()
        print()
        print('Aborted -- rollback.')
        # Clean up new table if it was created
        try:
            cur.execute('DROP TABLE IF EXISTS held_entities_new')
            conn.commit()
            print('held_entities_new dropped (cleanup).')
        except Exception:
            pass
        sys.exit(0)
    except Exception as e:
        conn.rollback()
        print(f'ERROR: {e}')
        import traceback
        traceback.print_exc()
        print()
        print('Rolled back. held_entities unchanged.')
        # Try to clean up new table
        try:
            cur2 = conn.cursor()
            cur2.execute('DROP TABLE IF EXISTS held_entities_new')
            conn.commit()
            print('held_entities_new dropped (cleanup).')
        except Exception:
            pass
        sys.exit(1)
    finally:
        conn.close()


if __name__ == '__main__':
    run()
