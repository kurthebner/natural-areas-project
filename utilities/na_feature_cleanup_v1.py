#!/usr/bin/env python3
"""
na_feature_cleanup_v1.py — IMP-131  Feature vocabulary normalization pass

Fixes applied in one transaction:
  1. Site features — vocab-map, move-to-notes, add-feat+note, drop, acreage,
     named-trail removal
  2. Trail status  — string 'None' -> NULL, 'Open' -> 'Active',
                     'Open/Partial' -> 'Active'
  3. Trail use_type — string 'None' or '' -> NULL
  4. Multi-county formatting — strip spaces after semicolons in
     sites.counties and trails.counties

Design intent:
  These are pipeline bug-fixes, not new normalization decisions.
  No normalization_provenance entries are created.
  This script is the audit artifact.

Usage:
  python utilities/na_feature_cleanup_v1.py
"""

import re
import sqlite3
import sys
import pathlib
from datetime import datetime, timezone

# Force UTF-8 output so Unicode characters in notes / arrows don't crash
# on Windows consoles that default to cp1252.
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

DB_PATH = pathlib.Path(__file__).parent.parent / "NASqlite" / "natural_areas_v5.db"

# ---------------------------------------------------------------------------
# DISPOSITION TABLES
# ---------------------------------------------------------------------------

# Lowercase token  ->  canonical vocabulary term
VOCAB_MAP = {
    'playground':                          'Playground',
    'pavilion':                            'Pavilion',
    'pavilions':                           'Pavilion',
    'wetland':                             'Wetland',
    'wetland pond':                        'Pond',
    'disc golf':                           'Disc Golf Course',
    'hiking trails':                       'Hiking Trail',
    'swimming pool':                       'Swimming Pool',
    'pool':                                'Swimming Pool',
    'boat launch':                         'Boat Ramp',
    'parking':                             'Parking Lot',
    'picnic area':                         'Picnic Area',
    'interpretive sign':                   'Interpretive Exhibit',
    'interpretive signage':                'Interpretive Exhibit',
    'bike rack':                           'Bike Rack',
    'athletic fields':                     'Athletic Field',
    'tennis courts':                       'Tennis Court',
    'fenced':                              'Fence',
    'glacial bog':                         'Bog',
    'stream crossings (bridges)':          'Bridge',
    'fishing pier':                        'Fishing Area',
    'woodland trails':                     'Hiking Trail',
    'mountain bike trails':                'Mountain Bike Trail',
    'off-leash dog area':                  'Dog Park',
    'ada accessible':                      'ADA Accessible',
    'historic ruins':                      'Building Ruins',
    'prairie restoration':                 'Habitat Restoration Area',
    'recreation center complex':           'Community Center',
    'gene daniel community center':        'Community Center',
}

# Lowercase token  ->  note sentence (remove from features, append to notes)
TO_NOTES = {
    'dawn to dusk':                        'Open dawn to dusk.',
    'open dawn to dusk':                   'Open dawn to dusk.',
    'sunrise to sunset':                   'Open sunrise to sunset.',
    'no bikes':                            'No bikes.',
    'no pets':                             'No pets.',
    'foot traffic only':                   'Foot traffic only.',
    'no bikes/horses/fires/hunting':       'No bikes, horses, fires, or hunting.',
    'permit required for access':          'Permit required for access.',
    'operating post-ownership transfer':   'Operating post-ownership transfer.',
    'trout-stocked':                       'Trout-stocked.',
    'open to public hunting and fishing per odnr regulations':
                                           'Open to public hunting and fishing per ODNR regulations.',
    'nonprofit trail system':              'Nonprofit trail system.',
    'primitive woodland':                  'Primitive woodland.',
    'rustic woodland':                     'Rustic woodland.',
    'potential wildflower sanctuary':      'Potential wildflower sanctuary.',
    'turtles':                             'Turtles observed.',
    'frogs':                               'Frogs observed.',
    'aquatic life':                        'Aquatic life present.',
    'wildlife hydration source':           'Functions as a wildlife water source.',
    "brown's lake":                        "Contains Brown's Lake.",
    'trees 300-500 years old':             'Contains trees 300–500 years old.',
    '~200-year-old sycamore':              'Contains a ~200-year-old sycamore.',
    'spring wildflowers':                  'Spring wildflowers present.',
    'riparian corridor':                   'Riparian corridor.',
    'riparian habitat':                    'Riparian habitat.',
    'oak-to-maple transitional forest':    'Oak-to-maple transitional forest.',
    'silver creek':                        'Along Silver Creek.',
    'apple creek':                         'Along Apple Creek.',
    'rathburn run':                        'Along Rathburn Run.',
    'killbuck creek':                      'Along Killbuck Creek.',
    'shreve lake':                         'Contains Shreve Lake.',
    "koehler's pond":                      "Contains Koehler's Pond.",
    'no fee':                              'No fee.',
    'no facilities except porta-pots':     'No facilities except porta-potties.',
    'pond/mill race site':                 'Historic pond and mill race site.',
    'chidester mill replica museum':       'Contains a Chidester Mill replica museum.',
    'chippewa local school district track/stadium':
                                           'Adjacent to Chippewa Local School District track and stadium.',
    'rustic':                              'Rustic character.',
    'maintained green field':              'Maintained green field.',
    '11.6 miles foot trails':              '11.6 miles of foot trails.',
    'two trail loops':                     'Two trail loops.',
    'mixed woodland':                      'Mixed woodland.',
    '~50 acres':                           'Approximately 50 acres.',
    '24-25 acres':                         '24–25 acres.',
    'waterfowl hunting':                   'Waterfowl hunting area.',
    '2 van-accessible parking spaces':     '2 van-accessible parking spaces.',
}

# Lowercase token  ->  (canonical_feature, note_sentence)
# Removes original token; adds the canonical feature AND appends the note.
ADD_FEATURE_AND_NOTE = {
    '7 pavilions (reservable)': (
        'Pavilion',
        '7 pavilions, reservable.',
    ),
    '1-mile boardwalk trail': (
        'Boardwalk',
        '1-mile boardwalk trail.',
    ),
    'accessible education trail': (
        'Hiking Trail',
        'Accessible education trail.',
    ),
    'paved trail 1.7mi': (
        'Hiking Trail',
        'Paved trail: 1.7 miles.',
    ),
    'ada-accessible kenwood acres section (1 mile)': (
        'ADA Accessible',
        'ADA-accessible Kenwood Acres section (1 mile).',
    ),
}

# Remove from features entirely — no note, no feature added
DROP = {
    'public access',
    'fishing',
    'multi-use recreation',
    'old-growth forest',
    'white oak',
    'red oak',
    'sphagnum moss',
    'pitcher plants (sarracenia purpurea)',
    'sundews',
    'bog rosemary',
    'rare orchids',
    'living plant collection',
    'research arboretum',
    'woody plant collections',
    '3 named trails',
    'city nature preserve',
    'memorial',
}

# Named trail entity names — remove from features silently (they are entities, not features)
KNOWN_NAMED_TRAILS = {
    'spangler trail 1.5mi',
    'outer trail',
    'old field trail 0.5mi',
    'education trail 0.9mi',
    'kenwood trail 0.8mi',
    'hartman trail 0.2mi',
    'sassafras trail 0.6mi',
    'strock trail 0.4mi',
    'trillium trail',
}

# Simple acreage pattern: "N acres" or "N.N acres" with no prefix/suffix
ACREAGE_RE = re.compile(r'^(\d+(?:\.\d+)?)\s+acres?$', re.IGNORECASE)

# ---------------------------------------------------------------------------
# HELPERS
# ---------------------------------------------------------------------------

def append_to_notes(existing, new_text):
    """Append new_text to existing notes with proper punctuation and a space."""
    if not existing or not existing.strip():
        return new_text
    existing = existing.strip()
    if not existing.endswith('.'):
        existing += '.'
    return existing + ' ' + new_text


def process_features(raw_features, raw_notes, raw_acres):
    """
    Process a single entity's features string.

    Returns:
        new_features_str  — updated semicolon-delimited features (or None if empty)
        new_notes_str     — updated notes string
        new_acres         — updated acres value (float or original)
        changes           — list of (action, original_token, detail) tuples
        kept_unchanged    — list of tokens kept as-is (vocab expansion candidates)
    """
    if not raw_features or not raw_features.strip():
        return raw_features, raw_notes, raw_acres, [], []

    tokens = [t.strip() for t in raw_features.split(';') if t.strip()]
    new_feature_set = []
    new_notes = raw_notes
    new_acres = raw_acres
    changes = []
    kept_unchanged = []

    for token in tokens:
        tok_lc = token.lower()

        # Priority 1: ADD_FEATURE_AND_NOTE
        if tok_lc in ADD_FEATURE_AND_NOTE:
            canonical_feat, note_text = ADD_FEATURE_AND_NOTE[tok_lc]
            new_feature_set.append(canonical_feat)
            new_notes = append_to_notes(new_notes, note_text)
            changes.append(('ADD_FEAT+NOTE', token,
                            f'feature="{canonical_feat}"  note="{note_text}"'))
            continue

        # Priority 2: VOCAB_MAP
        if tok_lc in VOCAB_MAP:
            canonical = VOCAB_MAP[tok_lc]
            new_feature_set.append(canonical)
            if canonical != token:
                changes.append(('VOCAB_MAP', token, f'-> "{canonical}"'))
            continue

        # Priority 3: TO_NOTES
        if tok_lc in TO_NOTES:
            note_text = TO_NOTES[tok_lc]
            new_notes = append_to_notes(new_notes, note_text)
            changes.append(('TO_NOTES', token, f'-> notes: "{note_text}"'))
            continue

        # Priority 4: Acreage regex (e.g. "5 acres", "12.3 acres")
        m = ACREAGE_RE.match(token)
        if m:
            acres_val = float(m.group(1))
            if raw_acres is None or str(raw_acres).strip() in ('', 'None'):
                new_acres = acres_val
                changes.append(('ACREAGE->FIELD', token,
                                f'-> acres={new_acres}'))
            else:
                note_text = f'{m.group(1)} acres.'
                new_notes = append_to_notes(new_notes, note_text)
                changes.append(('ACREAGE->NOTES', token,
                                f'-> notes: "{note_text}"  (acres already={raw_acres})'))
            continue

        # Priority 5: Known named trail entity
        if tok_lc in KNOWN_NAMED_TRAILS:
            changes.append(('DROP_NAMED_TRAIL', token,
                            'named trail entity — removed from features'))
            continue

        # Priority 6: Explicit DROP
        if tok_lc in DROP:
            changes.append(('DROP', token, 'removed'))
            continue

        # Default: keep as-is — log as vocabulary expansion candidate
        new_feature_set.append(token)
        kept_unchanged.append(token)

    # Deduplicate and sort alphabetically
    deduped = sorted(set(new_feature_set))
    new_features_str = '; '.join(deduped) if deduped else None

    return new_features_str, new_notes, new_acres, changes, kept_unchanged


# ---------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------

def main():
    print(f"Database : {DB_PATH}")
    if not DB_PATH.exists():
        print("ERROR: database file not found.")
        return

    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row

    now = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

    stats = {
        'sites_features_changed':        0,
        'sites_notes_changed':           0,
        'sites_acres_changed':           0,
        'trails_status_fixed':           0,
        'trails_use_type_fixed':         0,
        'counties_format_sites':         0,
        'counties_format_trails':        0,
        'tok_vocab_mapped':              0,
        'tok_to_notes':                  0,
        'tok_add_feat_note':             0,
        'tok_dropped':                   0,
        'tok_named_trail_dropped':       0,
        'tok_acreage_moved':             0,
    }

    all_expansion_candidates = {}   # token -> [site_ids]

    try:
        conn.execute("BEGIN")

        # ------------------------------------------------------------
        # PASS 1: Sites — features / notes / acres
        # ------------------------------------------------------------
        print()
        print("=" * 72)
        print("PASS 1: Sites — features / notes / acres")
        print("=" * 72)

        sites = conn.execute(
            "SELECT site_id, name, features, notes, acres FROM sites"
        ).fetchall()

        pass1_changes = 0
        for row in sites:
            site_id = row['site_id']
            name    = row['name']
            orig_f  = row['features']
            orig_n  = row['notes']
            orig_a  = row['acres']

            new_f, new_n, new_a, changes, kept = process_features(
                orig_f, orig_n, orig_a
            )

            # Track vocabulary expansion candidates
            for tok in kept:
                all_expansion_candidates.setdefault(tok, []).append(site_id)

            if not changes:
                continue

            feat_chg  = (new_f != orig_f)
            notes_chg = (new_n != orig_n)
            acres_chg = (new_a != orig_a)

            if not (feat_chg or notes_chg or acres_chg):
                continue

            pass1_changes += 1
            print(f"\n  [{site_id}] {name}")
            if feat_chg:
                print(f"    features BEFORE : {orig_f}")
                print(f"    features AFTER  : {new_f}")
            if notes_chg:
                before_n = (orig_n or '').strip()
                if before_n:
                    print(f"    notes    BEFORE : {before_n}")
                print(f"    notes    AFTER  : {(new_n or '').strip()}")
            if acres_chg:
                print(f"    acres    BEFORE : {orig_a}")
                print(f"    acres    AFTER  : {new_a}")

            for action, token, detail in changes:
                print(f"      [{action}] \"{token}\"  {detail}")
                if action == 'VOCAB_MAP':
                    stats['tok_vocab_mapped'] += 1
                elif action == 'TO_NOTES':
                    stats['tok_to_notes'] += 1
                elif action == 'ADD_FEAT+NOTE':
                    stats['tok_add_feat_note'] += 1
                elif action == 'DROP':
                    stats['tok_dropped'] += 1
                elif action == 'DROP_NAMED_TRAIL':
                    stats['tok_named_trail_dropped'] += 1
                elif action in ('ACREAGE->FIELD', 'ACREAGE->NOTES'):
                    stats['tok_acreage_moved'] += 1

            conn.execute(
                """UPDATE sites
                   SET features = ?,
                       notes    = ?,
                       acres    = ?,
                       updated_at = ?
                   WHERE site_id = ?""",
                (new_f, new_n, new_a, now, site_id),
            )

            if feat_chg:
                stats['sites_features_changed'] += 1
            if notes_chg:
                stats['sites_notes_changed'] += 1
            if acres_chg:
                stats['sites_acres_changed'] += 1

        if pass1_changes == 0:
            print("  (no feature changes needed)")

        # ------------------------------------------------------------
        # PASS 2: Trails — status / use_type
        # ------------------------------------------------------------
        print()
        print("=" * 72)
        print("PASS 2: Trails — status / use_type")
        print("=" * 72)

        STATUS_FIX = {
            'None':         None,
            'Open':         'Active',
            'Open/Partial': 'Active',
        }

        trails = conn.execute(
            "SELECT trail_id, name, status, use_type FROM trails"
        ).fetchall()

        pass2_changes = 0
        for row in trails:
            trail_id    = row['trail_id']
            name        = row['name']
            orig_status = row['status']
            orig_use    = row['use_type']
            new_status  = orig_status
            new_use     = orig_use
            changes     = []

            if orig_status in STATUS_FIX:
                new_status = STATUS_FIX[orig_status]
                changes.append(('STATUS', repr(orig_status), f'-> {new_status!r}'))

            if orig_use is not None and orig_use.strip() in ('', 'None'):
                new_use = None
                changes.append(('USE_TYPE', repr(orig_use), '-> NULL'))

            if not changes:
                continue

            pass2_changes += 1
            print(f"\n  [{trail_id}] {name}")
            for action, before, detail in changes:
                print(f"    [{action}] {before}  {detail}")

            conn.execute(
                """UPDATE trails
                   SET status   = ?,
                       use_type = ?,
                       updated_at = ?
                   WHERE trail_id = ?""",
                (new_status, new_use, now, trail_id),
            )

            if new_status != orig_status:
                stats['trails_status_fixed'] += 1
            if new_use != orig_use:
                stats['trails_use_type_fixed'] += 1

        if pass2_changes == 0:
            print("  (no trail status/use_type fixes needed)")

        # ------------------------------------------------------------
        # PASS 3: Multi-county formatting
        # ------------------------------------------------------------
        print()
        print("=" * 72)
        print("PASS 3: Multi-county formatting (remove spaces after semicolons)")
        print("=" * 72)

        pass3_changes = 0
        for table, id_col in (('sites', 'site_id'), ('trails', 'trail_id')):
            rows = conn.execute(
                f"SELECT {id_col}, counties FROM {table} WHERE counties LIKE '%; %'"
            ).fetchall()
            for row in rows:
                entity_id = row[id_col]
                orig_val  = row['counties']
                fixed_val = orig_val.replace('; ', ';')
                print(f"  [{table}:{entity_id}]  {orig_val!r}  ->  {fixed_val!r}")
                conn.execute(
                    f"""UPDATE {table}
                        SET counties   = ?,
                            updated_at = ?
                        WHERE {id_col} = ?""",
                    (fixed_val, now, entity_id),
                )
                pass3_changes += 1
                if table == 'sites':
                    stats['counties_format_sites'] += 1
                else:
                    stats['counties_format_trails'] += 1

        if pass3_changes == 0:
            print("  (no county formatting issues found)")

        # ------------------------------------------------------------
        # COMMIT
        # ------------------------------------------------------------
        conn.execute("COMMIT")
        print()
        print("OK: COMMIT successful.")

    except Exception as exc:
        conn.execute("ROLLBACK")
        print(f"\nERROR: ROLLBACK executed.")
        print(f"  {exc}")
        raise

    finally:
        conn.close()

    # ------------------------------------------------------------
    # SUMMARY
    # ------------------------------------------------------------
    print()
    print("=" * 72)
    print("SUMMARY")
    print("=" * 72)
    print(f"  Sites — features changed        : {stats['sites_features_changed']}")
    print(f"  Sites — notes updated           : {stats['sites_notes_changed']}")
    print(f"  Sites — acres field set         : {stats['sites_acres_changed']}")
    print(f"  Trails — status fixed           : {stats['trails_status_fixed']}")
    print(f"  Trails — use_type nulled        : {stats['trails_use_type_fixed']}")
    print(f"  County format fixed (sites)     : {stats['counties_format_sites']}")
    print(f"  County format fixed (trails)    : {stats['counties_format_trails']}")
    print(f"  --- Token dispositions ---")
    print(f"  Vocab-mapped                    : {stats['tok_vocab_mapped']}")
    print(f"  Moved to notes                  : {stats['tok_to_notes']}")
    print(f"  Added feat + note               : {stats['tok_add_feat_note']}")
    print(f"  Dropped                         : {stats['tok_dropped']}")
    print(f"  Named trails removed            : {stats['tok_named_trail_dropped']}")
    print(f"  Acreage relocated               : {stats['tok_acreage_moved']}")

    if all_expansion_candidates:
        print()
        print("VOCABULARY EXPANSION CANDIDATES (kept as-is; review for future vocab)")
        print("-" * 72)
        for tok in sorted(all_expansion_candidates.keys()):
            ids = ', '.join(all_expansion_candidates[tok])
            print(f"  \"{tok}\"  [{ids}]")
    else:
        print()
        print("No vocabulary expansion candidates found.")


if __name__ == '__main__':
    main()
