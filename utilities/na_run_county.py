#!/usr/bin/env python3
"""
na_run_county.py — Natural Areas Project County Pipeline Driver
v1.1  |  2026-05-07

Reads a county pipeline config JSON and invokes PipelineRunner (Stages 3–6).
Replaces per-county boilerplate scripts — all county-specific data lives in
the config file.  Claude writes the JSON; this script runs it.

USAGE
-----
  cd "Natural Areas Project v5"

  # Explicit config path:
  python utilities/na_run_county.py \\
      --config "County_Spreadsheets/Van Wert/van_wert_oh_pipeline_config.json"

  # Auto-discover config from county dir:
  python utilities/na_run_county.py --county-dir "County_Spreadsheets/Van Wert"

  # Custom DB or dry-run:
  python utilities/na_run_county.py --config ... --db NASqlite/natural_areas_v5.db
  python utilities/na_run_county.py --config ... --dry-run

OPTIONS
-------
  --config PATH       Path to *_pipeline_config.json
  --county-dir DIR    Directory containing exactly one *_pipeline_config.json
  --db PATH           SQLite database (default: NASqlite/natural_areas_v5.db)
  --dry-run           Print SQL without committing; TSV files are still written
  --skip-gps          Skip Nominatim GPS acquisition (use fallback_gps only)

CONFIG FILE FORMAT
------------------
See utilities/na_pipeline_config_template.json for the full schema.
Key top-level fields:

  county          str   — "Van Wert"
  state           str   — "Ohio"
  run_id          str   — "van_wert_oh_2026_04_14"
  run_date        str   — "2026-04-19"  (ISO date)
  prefix          str   — "VNW"  (informational; entity IDs already in data)
  records_input   int   — total raw records from discovery YAML
  bbox            list  — [lat_min, lat_max, lon_min, lon_max]
  run_notes       str   — optional pipeline run notes
  gps_queries     dict  — {entity_id: "Nominatim query string", ...}
  fallback_gps    dict  — {entity_id: [lat, lon], ...}
  fallback_conf   dict  — {entity_id: "MED"|"LOW", ...}  (optional)
  sites           list  — normalized site dicts (Stage 2 output)
  trails          list  — normalized trail dicts
  trail_segments  list  — normalized trail segment dicts
  trail_networks  list  — normalized trail network dicts
  site_networks   list  — normalized site network dicts
  access_points   list  — normalized access point dicts
"""

import argparse
import glob
import json
import os
import sys

# IMP-128: Windows console UTF-8 fix — prevents UnicodeEncodeError on → and em dashes
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# ── Paths ────────────────────────────────────────────────────────────────────

SCRIPT_DIR   = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
DEFAULT_DB   = os.path.join(PROJECT_ROOT, "NASqlite", "natural_areas_v5.db")

sys.path.insert(0, SCRIPT_DIR)

try:
    from na_pipeline_core import PipelineRunner, ReviewRequired
except ImportError as exc:
    print(f"ERROR: Cannot import na_pipeline_core from {SCRIPT_DIR}.\n"
          f"  Run from the project root or ensure utilities/ is importable.\n"
          f"  Detail: {exc}", file=sys.stderr)
    sys.exit(1)


# ── Helpers ──────────────────────────────────────────────────────────────────

def find_config(county_dir: str) -> str:
    """Locate the single *_pipeline_config.json in county_dir."""
    county_dir = os.path.abspath(county_dir)
    matches = glob.glob(os.path.join(county_dir, "*_pipeline_config.json"))
    if not matches:
        raise FileNotFoundError(
            f"No *_pipeline_config.json found in: {county_dir}\n"
            f"  Create one from utilities/na_pipeline_config_template.json"
        )
    if len(matches) > 1:
        names = [os.path.basename(m) for m in matches]
        raise ValueError(
            f"Multiple config files found in {county_dir}: {names}\n"
            f"  Use --config to specify which one."
        )
    return matches[0]


def load_config(config_path: str) -> dict:
    """Load and lightly validate the pipeline config JSON."""
    with open(config_path, encoding="utf-8") as f:
        cfg = json.load(f)

    required = ("county", "state", "run_id", "run_date")
    missing = [k for k in required if not cfg.get(k)]
    if missing:
        raise ValueError(f"Config missing required fields: {missing}")

    # State normalization guard — config must use full state name, not abbreviation.
    # run_metadata.state must be "Ohio", never "OH" (IMP-101).
    state = cfg.get("state", "")
    if len(state) == 2 and state.isupper():
        raise ValueError(
            f"Config field 'state' is an abbreviation ({state!r}). "
            f"Use the full state name (e.g., 'Ohio'). "
            f"run_metadata.state must never be a two-letter abbreviation."
        )

    return cfg


def check_db_integrity(db_path: str) -> None:
    """
    Run PRAGMA integrity_check and PRAGMA foreign_key_check before any pipeline
    writes. Raises SystemExit if either check finds errors (IMP-101).

    Why: SQLite page corruption and incomplete prior writes can silently corrupt
    data if the pipeline runs against a damaged DB. Catching this pre-run is far
    cheaper than diagnosing errors mid-upsert or post-upsert.
    """
    import sqlite3

    if not os.path.exists(db_path):
        # DB does not exist yet — first run, nothing to check.
        return

    print(f"  DB integrity check: {db_path}")
    conn = sqlite3.connect(db_path)
    try:
        # integrity_check: page structure, index consistency, type rules
        rows = conn.execute("PRAGMA integrity_check").fetchall()
        if rows and rows[0][0] != "ok":
            errors = "\n    ".join(r[0] for r in rows)
            print(
                f"\nFATAL: PRAGMA integrity_check failed on {db_path}:\n"
                f"    {errors}\n"
                f"  Do not run the pipeline against a damaged database.\n"
                f"  Restore from backup or run the DB rebuild procedure.",
                file=sys.stderr,
            )
            sys.exit(1)

        # foreign_key_check: dangling FK references
        fk_errors = conn.execute("PRAGMA foreign_key_check").fetchall()
        if fk_errors:
            for e in fk_errors:
                print(f"  WARNING: FK violation — table={e[0]}, rowid={e[1]}, "
                      f"parent={e[2]}, fkid={e[3]}", file=sys.stderr)
            print(
                f"  {len(fk_errors)} foreign key violation(s) found. "
                f"Pipeline will continue — review after upsert.",
                file=sys.stderr,
            )

        print("  DB integrity check: OK")
    finally:
        conn.close()


def coerce_fallback_gps(cfg: dict) -> dict:
    """
    JSON stores fallback_gps as {id: [lat, lon]}.
    PipelineRunner expects {id: (lat, lon)}.
    """
    raw = cfg.get("fallback_gps", {})
    result = {}
    for entity_id, coords in raw.items():
        if not (isinstance(coords, (list, tuple)) and len(coords) == 2):
            print(f"  WARNING: fallback_gps[{entity_id!r}] is not [lat, lon] — skipping",
                  file=sys.stderr)
            continue
        result[entity_id] = (float(coords[0]), float(coords[1]))
    return result


# ── Main ─────────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(
        description="NAP County Pipeline Driver — reads JSON config, runs PipelineRunner",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    src = parser.add_mutually_exclusive_group(required=True)
    src.add_argument("--config",     metavar="PATH",
                     help="Path to county *_pipeline_config.json")
    src.add_argument("--county-dir", metavar="DIR",
                     help="Directory containing *_pipeline_config.json (auto-discovered)")

    parser.add_argument("--db",       metavar="PATH", default=DEFAULT_DB,
                        help=f"SQLite DB path (default: {DEFAULT_DB})")
    parser.add_argument("--dry-run",  action="store_true",
                        help="Print SQL without committing; TSVs still written")
    parser.add_argument("--skip-gps", action="store_true",
                        help="Skip Nominatim; only apply fallback_gps entries")
    parser.add_argument("--confirm-review", action="store_true",
                        help="Confirm TSV review complete — allows Stage 6 upsert to proceed")

    args = parser.parse_args()

    # ── Locate and load config ────────────────────────────────────────────────
    try:
        config_path = args.config or find_config(args.county_dir)
        cfg = load_config(config_path)
    except (FileNotFoundError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        sys.exit(1)

    county_dir = os.path.dirname(os.path.abspath(config_path))

    # ── Resolve parameters ────────────────────────────────────────────────────
    bbox = cfg.get("bbox")
    county_bbox = tuple(bbox) if bbox and len(bbox) == 4 else None

    fallback_gps  = coerce_fallback_gps(cfg)
    fallback_conf = cfg.get("fallback_conf", {})

    # --skip-gps: clear gps_queries so PipelineRunner skips Nominatim
    gps_queries = {} if args.skip_gps else cfg.get("gps_queries", {})
    if args.skip_gps:
        print("  --skip-gps: Nominatim queries suppressed; fallback_gps will still apply.")

    db_path = os.path.abspath(args.db)
    if not os.path.exists(db_path) and not args.dry_run:
        print(f"WARNING: Database not found at {db_path}. "
              f"Upsert will fail unless --dry-run is set.", file=sys.stderr)

    # ── Pre-run DB integrity check (IMP-101) ──────────────────────────────────
    if not args.dry_run:
        check_db_integrity(db_path)

    # ── Build and run PipelineRunner ─────────────────────────────────────────
    runner = PipelineRunner(
        run_id        = cfg["run_id"],
        county        = cfg["county"],
        state         = cfg["state"],
        run_date      = cfg["run_date"],
        records_input = int(cfg.get("records_input", 0)),
        output_dir    = county_dir,
        db_path       = db_path,
        county_bbox   = county_bbox,
    )

    try:
        runner.run(
            sites          = cfg.get("sites",          []),
            trails         = cfg.get("trails",         []),
            access_points  = cfg.get("access_points",  []),
            trail_segments = cfg.get("trail_segments", []),
            trail_networks = cfg.get("trail_networks", []),
            site_networks  = cfg.get("site_networks",  []),
            gps_queries    = gps_queries,
            fallback_gps   = fallback_gps,
            fallback_conf  = fallback_conf,
            run_notes      = cfg.get("run_notes", ""),
            dry_run        = args.dry_run,
            confirm_review = args.confirm_review,
        )
    except ReviewRequired as e:
        print(f"\n{e}", file=sys.stderr)
        sys.exit(2)


if __name__ == "__main__":
    main()
