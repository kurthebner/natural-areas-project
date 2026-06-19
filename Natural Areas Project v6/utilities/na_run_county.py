#!/usr/bin/env python3
"""
na_run_county.py — Natural Areas Project County Pipeline Driver (v6)
v2.0  |  2026-05-31

v6 changes from v1.1:
  - Four entity types: sites, trailthings, site_networks, access_points
  - trails / trail_segments / trail_networks config keys removed
  - References na_pipeline_core_v6.py (in this directory)

Reads a county pipeline config JSON and invokes PipelineRunner (Stages 3–8).

USAGE
-----
  cd "Natural Areas Project v6"

  python utilities/na_run_county.py \\
      --config "County_Spreadsheets/Franklin/franklin_oh_pipeline_config.json"

  python utilities/na_run_county.py --county-dir "County_Spreadsheets/Franklin"

  python utilities/na_run_county.py --config ... --dry-run
  python utilities/na_run_county.py --config ... --confirm-review

OPTIONS
-------
  --config PATH       Path to *_pipeline_config.json
  --county-dir DIR    Directory containing exactly one *_pipeline_config.json
  --db PATH           SQLite database (default: ../NASqlite/natural_areas_v6.db)
  --dry-run           Print SQL without committing; TSV files are still written
  --skip-gps          Skip Nominatim GPS acquisition (use fallback_gps only)
  --confirm-review    Confirm TSV review complete; allows Stage 8 upsert to proceed

CONFIG FILE FORMAT
------------------
Key top-level fields:

  county          str   — "Franklin"
  state           str   — "Ohio"
  run_id          str   — "franklin_oh_2026_05_31"
  run_date        str   — "2026-05-31"
  prefix          str   — "FR"
  records_input   int   — total raw records from discovery YAML
  bbox            list  — [lat_min, lat_max, lon_min, lon_max]
  run_notes       str   — optional pipeline run notes
  gps_queries     dict  — {entity_id: "Nominatim query string", ...}
  fallback_gps    dict  — {entity_id: [lat, lon], ...}
  fallback_conf   dict  — {entity_id: "MED"|"LOW", ...}
  sites           list  — normalized site dicts
  trailthings     list  — normalized trailthing dicts
  site_networks   list  — normalized site network dicts
  access_points   list  — normalized access point dicts
"""

import argparse
import glob
import json
import os
import sys

# IMP-128: Windows console UTF-8 fix
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

SCRIPT_DIR   = os.path.dirname(os.path.abspath(__file__))
# DB lives in v5 project folder (shared)
V6_ROOT      = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
DEFAULT_DB   = os.path.join(V6_ROOT, "NASqlite", "natural_areas_v6.db")

sys.path.insert(0, SCRIPT_DIR)

try:
    from na_pipeline_core_v6 import PipelineRunner, ReviewRequired
except ImportError as exc:
    print(f"ERROR: Cannot import na_pipeline_core_v6 from {SCRIPT_DIR}.\n"
          f"  Detail: {exc}", file=sys.stderr)
    sys.exit(1)


def find_config(county_dir: str) -> str:
    county_dir = os.path.abspath(county_dir)
    matches = glob.glob(os.path.join(county_dir, "*_pipeline_config.json"))
    if not matches:
        raise FileNotFoundError(
            f"No *_pipeline_config.json found in: {county_dir}"
        )
    if len(matches) > 1:
        names = [os.path.basename(m) for m in matches]
        raise ValueError(f"Multiple config files found: {names}. Use --config.")
    return matches[0]


def load_config(config_path: str) -> dict:
    with open(config_path, encoding="utf-8") as f:
        cfg = json.load(f)

    required = ("county", "state", "run_id", "run_date")
    missing = [k for k in required if not cfg.get(k)]
    if missing:
        raise ValueError(f"Config missing required fields: {missing}")

    # IMP-101: state must be full name, not abbreviation
    state = cfg.get("state", "")
    if len(state) == 2 and state.isupper():
        raise ValueError(
            f"Config field 'state' is an abbreviation ({state!r}). "
            f"Use the full state name (e.g., 'Ohio')."
        )

    return cfg


def check_db_integrity(db_path: str) -> None:
    """IMP-101: PRAGMA integrity_check and foreign_key_check before pipeline writes."""
    import sqlite3
    if not os.path.exists(db_path):
        return
    print(f"  DB integrity check: {db_path}")
    conn = sqlite3.connect(db_path)
    try:
        rows = conn.execute("PRAGMA integrity_check").fetchall()
        if rows and rows[0][0] != "ok":
            errors = "\n    ".join(r[0] for r in rows)
            print(f"\nFATAL: PRAGMA integrity_check failed:\n    {errors}",
                  file=sys.stderr)
            sys.exit(1)
        fk_errors = conn.execute("PRAGMA foreign_key_check").fetchall()
        if fk_errors:
            for e in fk_errors:
                print(f"  WARNING: FK violation — table={e[0]}, rowid={e[1]}, "
                      f"parent={e[2]}", file=sys.stderr)
        print("  DB integrity check: OK")
    finally:
        conn.close()


def coerce_fallback_gps(cfg: dict) -> dict:
    raw = cfg.get("fallback_gps", {})
    result = {}
    for entity_id, coords in raw.items():
        if not (isinstance(coords, (list, tuple)) and len(coords) == 2):
            print(f"  WARNING: fallback_gps[{entity_id!r}] is not [lat, lon] — skipping",
                  file=sys.stderr)
            continue
        result[entity_id] = (float(coords[0]), float(coords[1]))
    return result


def main() -> None:
    parser = argparse.ArgumentParser(
        description="NAP v6 County Pipeline Driver",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    src = parser.add_mutually_exclusive_group(required=True)
    src.add_argument("--config",     metavar="PATH")
    src.add_argument("--county-dir", metavar="DIR")

    parser.add_argument("--db",             metavar="PATH", default=DEFAULT_DB)
    parser.add_argument("--dry-run",        action="store_true")
    parser.add_argument("--skip-gps",       action="store_true")
    parser.add_argument("--confirm-review", action="store_true")

    args = parser.parse_args()

    try:
        config_path = args.config or find_config(args.county_dir)
        cfg = load_config(config_path)
    except (FileNotFoundError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        sys.exit(1)

    county_dir    = os.path.dirname(os.path.abspath(config_path))
    bbox          = cfg.get("bbox")
    county_bbox   = tuple(bbox) if bbox and len(bbox) == 4 else None
    fallback_gps  = coerce_fallback_gps(cfg)
    fallback_conf = cfg.get("fallback_conf", {})
    gps_queries   = {} if args.skip_gps else cfg.get("gps_queries", {})
    db_path       = os.path.abspath(args.db)

    if args.skip_gps:
        print("  --skip-gps: Nominatim queries suppressed.")

    if not os.path.exists(db_path) and not args.dry_run:
        print(f"WARNING: Database not found at {db_path}.", file=sys.stderr)

    if not args.dry_run:
        check_db_integrity(db_path)

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
            trailthings    = cfg.get("trailthings",    []),
            site_networks  = cfg.get("site_networks",  []),
            access_points  = cfg.get("access_points",  []),
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
