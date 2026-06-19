"""
_run_pipeline.py — Sandusky County pipeline driver (Stages 4–6).

Filters held entities from the config, renames NCIT trail ID (SAN-T-001 →
OH-MC-T-0110), and invokes PipelineRunner.

Run from project root:
  python County_Spreadsheets/Sandusky/_run_pipeline.py
  python County_Spreadsheets/Sandusky/_run_pipeline.py --confirm-review
  python County_Spreadsheets/Sandusky/_run_pipeline.py --confirm-review --dry-run

Stage 5.5 halts the run unless --confirm-review is passed.
Post-upsert steps (held_entities, access_point_parents, run_metadata held count)
execute only when --confirm-review is active and no --dry-run.
"""

import argparse, json, os, sqlite3, sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
CFG_PATH     = PROJECT_ROOT / 'County_Spreadsheets' / 'Sandusky' / 'sandusky_config.json'
DB_PATH      = PROJECT_ROOT / 'NASqlite' / 'natural_areas_v5.db'
OUTPUT_DIR   = str(PROJECT_ROOT / 'County_Spreadsheets' / 'Sandusky')

sys.path.insert(0, str(PROJECT_ROOT / 'utilities'))
from na_pipeline_core import PipelineRunner, ReviewRequired

# ── CLI ───────────────────────────────────────────────────────────────────────
parser = argparse.ArgumentParser(description='Sandusky County pipeline driver')
parser.add_argument('--confirm-review', action='store_true',
                    help='Confirm TSV review — proceed past Stage 5.5 to Stage 6')
parser.add_argument('--dry-run', action='store_true',
                    help='Print SQL without committing; TSV files still written')
args = parser.parse_args()

# ── Load config ───────────────────────────────────────────────────────────────
cfg = json.loads(CFG_PATH.read_text(encoding='utf-8'))
RUN_ID = cfg['run_id']

# ── Held entity detection ─────────────────────────────────────────────────────
def is_held(rec):
    sf = rec.get('status_flag') or ''
    if sf.startswith('HELD'):
        return True
    notes = rec.get('notes') or ''
    return 'HELD' in notes and (
        'cross_county_held' in notes
        or 'gps_missing' in notes
        or 'parent_held' in notes
    )

# ── Split active / held ───────────────────────────────────────────────────────
all_sites  = cfg.get('sites',          [])
all_trails = cfg.get('trails',         [])
all_aps    = cfg.get('access_points',  [])

held_sites  = [s  for s  in all_sites  if is_held(s)]
held_trails = [t  for t  in all_trails if is_held(t)]
held_aps    = [ap for ap in all_aps    if is_held(ap)]

active_sites  = [s  for s  in all_sites  if not is_held(s)]
active_trails = [t  for t  in all_trails if not is_held(t)]
active_aps    = [ap for ap in all_aps    if not is_held(ap)]

total_held = len(held_sites) + len(held_trails) + len(held_aps)
total_active = len(active_sites) + len(active_trails) + len(active_aps)

print(f'Active : {len(active_sites)} sites, {len(active_trails)} trails, {len(active_aps)} APs  (total {total_active})')
print(f'Held   : {len(held_sites)} sites, {len(held_trails)} trails, {len(held_aps)} APs  (total {total_held})')

# ── NCIT: SAN-T-001 → OH-MC-T-0110 (IMP-104 Scenario A resolution) ───────────
NCIT_PROVISIONAL = 'SAN-T-001'
NCIT_FINAL       = 'OH-MC-T-0110'
for t in active_trails:
    if t.get('trail_id') == NCIT_PROVISIONAL:
        t['trail_id'] = NCIT_FINAL
        print(f'  ID swap: {NCIT_PROVISIONAL} -> {NCIT_FINAL}')
        break
# Parent references in APs already set to OH-MC-T-0110 during normalization.

# ── url_secondary → urls (CLAUDE.md §7 DB column name mapping) ───────────────
for ent in active_sites + active_aps:
    if 'urls' not in ent:
        ent['urls'] = ent.get('url_secondary', '') or ''

# ── IMP-115: Pre-upsert MC county format scan ─────────────────────────────────
print('\n[IMP-115] MC county format scan:')
mc_bad = []
for t in active_trails:
    if t.get('trail_id', '').startswith('OH-MC-'):
        counties = t.get('counties', '')
        if '; ' in counties:
            mc_bad.append(f"  MALFORMED: {t['trail_id']} counties='{counties}'")
if mc_bad:
    for msg in mc_bad:
        print(msg)
    print('  FATAL: Fix county format (semicolon-delimited, no spaces) before upserting.')
    sys.exit(1)
print('  OK — no malformed OH-MC county fields.')

# ── GPS already filled into entity records; pass fallback_gps for IMP-031 ────
fallback_gps = {k: tuple(v) for k, v in cfg.get('fallback_gps', {}).items()}

# ── PipelineRunner (Stages 3–6) ───────────────────────────────────────────────
# Expected integrity warnings (non-fatal):
#   SAN-S-008: gps_lat=None (gps_unresolvable=True — ODNR distributed tracts)
#   SAN-AP-004: parent_entity_id=OH-MC-T-0110 not in site_ids (it is a trail, correct)
runner = PipelineRunner(
    run_id        = RUN_ID,
    county        = cfg['county'],
    state         = cfg['state'],
    run_date      = cfg['run_date'],
    records_input = int(cfg.get('records_input', 0)),
    output_dir    = OUTPUT_DIR,
    db_path       = str(DB_PATH),
    tsv_prefix    = 'sandusky',
    county_bbox   = tuple(cfg['bbox']) if cfg.get('bbox') else None,
)

try:
    runner.run(
        sites          = active_sites,
        trails         = active_trails,
        access_points  = active_aps,
        trail_segments = [],
        trail_networks = [],
        site_networks  = [],
        gps_queries    = {},          # Nominatim suppressed — GPS already acquired
        fallback_gps   = fallback_gps,
        run_notes      = cfg.get('run_notes', ''),
        dry_run        = args.dry_run,
        confirm_review = args.confirm_review,
    )
except ReviewRequired as e:
    print(f'\n{e}', file=sys.stderr)
    sys.exit(2)

# ── Post-upsert: held_entities + access_point_parents + run_metadata ──────────
# Executes only when --confirm-review succeeded (Stage 6 ran).
if args.dry_run:
    print('\n[DRY-RUN] Skipping post-upsert steps.')
    sys.exit(0)

print('\n[Post-upsert] Inserting held_entities, access_point_parents, fixing run_metadata...')

def _hold_reason_detail(rec):
    """Return (hold_reason, hold_detail) for a held entity record."""
    hd    = rec.get('hold_detail') or ''
    notes = rec.get('notes') or ''
    if 'cross_county_held' in hd or 'cross_county_held' in notes:
        detail = hd if hd else notes.strip().split('\n')[0]
        return 'cross_county_held', detail[:250]
    if 'parent_held' in hd:
        return 'parent_held', hd[:250]
    if 'gps_missing' in hd or 'gps_missing' in notes:
        return 'gps_missing', 'gps_missing'
    return 'unknown', (hd or notes[:100])

now  = runner.now
conn = sqlite3.connect(str(DB_PATH))
try:
    cur = conn.cursor()

    # held_entities
    held_sql = """
    INSERT OR IGNORE INTO held_entities
        (record_id, entity_type, name, county, hold_reason, hold_detail, run_id, created_at)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """
    held_ct = 0
    for s in held_sites:
        reason, detail = _hold_reason_detail(s)
        cur.execute(held_sql,
            (s['site_id'], 'Site', s['name'], 'Sandusky', reason, detail, RUN_ID, now))
        held_ct += 1
    for t in held_trails:
        reason, detail = _hold_reason_detail(t)
        cur.execute(held_sql,
            (t['trail_id'], 'Trail', t['name'], 'Sandusky', reason, detail, RUN_ID, now))
        held_ct += 1
    for ap in held_aps:
        reason, detail = _hold_reason_detail(ap)
        cur.execute(held_sql,
            (ap['access_point_id'], 'Access Point', ap['name'], 'Sandusky',
             reason, detail, RUN_ID, now))
        held_ct += 1
    print(f'  held_entities:        {held_ct} rows')

    # access_point_parents
    ap_sql = """
    INSERT OR IGNORE INTO access_point_parents
        (access_point_id, parent_entity_type, parent_entity_id)
    VALUES (?, ?, ?)
    """
    ap_ct = 0
    for ap in active_aps:
        ptype = ap.get('parent_entity_type', '')
        pid   = ap.get('parent_entity_id',   '')
        if ptype and pid:
            cur.execute(ap_sql, (ap['access_point_id'], ptype, pid))
            ap_ct += 1
    print(f'  access_point_parents: {ap_ct} rows')

    # Correct run_metadata held count (PipelineRunner inserts held=0)
    cur.execute('UPDATE run_metadata SET held = ? WHERE run_id = ?', (total_held, RUN_ID))
    print(f'  run_metadata.held:    updated to {total_held}')

    conn.commit()
    print('  Post-upsert committed.')

except Exception as exc:
    conn.rollback()
    print(f'  ERROR in post-upsert: {exc}', file=sys.stderr)
    raise
finally:
    conn.close()

print(f'\nSandusky pipeline complete.')
print(f'  Active upserted:  {total_active}')
print(f'  Held (logged):    {total_held}')
