#!/usr/bin/env python3
"""
henry_oh_gps_merge_stage3.py — Stage 3 GPS Merge
Henry County, Ohio | Run ID: henry_oh_2026_04_20

Merges GPS acquisition results into the normalized entities:
  - For HIGH/MED/LOW confidence: re-normalizes held entity with GPS injected,
    appends to normalized_entities.yaml, removes from held_entities.yaml
  - For NONE confidence: entity stays held; hold_detail updated
  - Runs vocabulary gate on newly normalized entities
  - Updates normalized_entities.yaml and held_entities.yaml
  - Copies finalized normalization script to processing/

Imports normalization functions directly from the Stage 2 script.
"""

import sys, os, re, yaml, logging, pathlib, datetime

BASE = "/sessions/trusting-sweet-gates/mnt/Natural Areas Project v5"
PROCESSING = f"{BASE}/processing"
UTIL_PATH  = f"{BASE}/utilities"

sys.path.insert(0, UTIL_PATH)
sys.path.insert(0, PROCESSING)

# Import Stage 2 normalization functions by loading the module
import importlib.util

stage2_path = f"{PROCESSING}/henry_oh_normalization_stage2.py"
spec = importlib.util.spec_from_file_location("stage2", stage2_path)
stage2 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(stage2)

# Pull the functions we need
normalize_site    = stage2.normalize_site
vocabulary_gate   = stage2.vocabulary_gate
gis_lookup        = stage2.gis_lookup
get_plus_code     = stage2.get_plus_code
parse_gps         = stage2.parse_gps
derived_label     = stage2.derived_label

from na_vocab_constants import ALLOWED_FEATURES

logging.basicConfig(level=logging.INFO, format="%(levelname)s | %(message)s")
logger = logging.getLogger(__name__)

# ── File paths ────────────────────────────────────────────────────────────────
GPS_RESULTS   = f"{BASE}/henry_oh_gps_results.yaml"
NORM_FILE     = f"{BASE}/henry_oh_normalized_entities.yaml"
HELD_FILE     = f"{BASE}/henry_oh_held_entities.yaml"
RESOLVED_FILE = f"{BASE}/henry_oh_resolved_entities.yaml"
REPORT_FILE   = f"{BASE}/henry_oh_gps_report.md"

RUN_ID    = "henry_oh_2026_04_20"
NORM_DATE = "2026-04-26"


def load_yaml(path: str) -> dict:
    return yaml.safe_load(pathlib.Path(path).read_text())


def save_yaml(path: str, data: dict):
    pathlib.Path(path).write_text(yaml.dump(data, allow_unicode=True, sort_keys=False))


def main():
    logger.info("Stage 3 GPS Merge — Henry County, OH")

    # ── Load data ─────────────────────────────────────────────────────────────
    gps_data     = load_yaml(GPS_RESULTS)
    norm_data    = load_yaml(NORM_FILE)
    held_data    = load_yaml(HELD_FILE)
    resolved_data = load_yaml(RESOLVED_FILE)

    gps_results   = gps_data["results"]
    norm_entities  = norm_data["normalized_entities"]
    held_entities  = held_data["held_entities"]
    resolved_map   = {e["resolved_entity_id"]: e for e in resolved_data["resolved_entities"]}

    # ── Process each held entity ──────────────────────────────────────────────
    newly_normalized = []
    remaining_held   = []
    merge_log        = []

    for held in held_entities:
        eid = held["record_id"]
        gps_r = gps_results.get(eid, {})
        confidence = gps_r.get("confidence", "NONE")
        lat = gps_r.get("gps_lat")
        lon = gps_r.get("gps_lon")

        logger.info(f"\n{eid} — {held['name']} | GPS conf: {confidence}")

        if confidence == "NONE" or lat is None:
            # Entity stays held
            held["hold_detail"] = (
                f"IMP-069: GPS null — GPS Acquisition Module: all queries failed or NONE confidence "
                f"({gps_r.get('method', 'no_query')}). Entity excluded from TSV/upsert."
            )
            remaining_held.append(held)
            merge_log.append({
                "entity_id": eid,
                "name":       held["name"],
                "action":     "REMAINS_HELD",
                "confidence": confidence,
                "reason":     gps_r.get("notes", "no GPS acquirable"),
            })
            logger.info(f"  → Remains held (NONE confidence)")
            continue

        # Entity has GPS — re-normalize
        resolved_entity = resolved_map.get(eid)
        if not resolved_entity:
            logger.error(f"  !! Could not find resolved entity for {eid}")
            remaining_held.append(held)
            continue

        # Inject GPS into resolved entity payload
        payload = resolved_entity.get("payload", {})
        payload["gps_lat_raw"] = str(lat)
        payload["gps_lon_raw"] = str(lon)

        # GIS lookup with acquired GPS
        twp, muni = gis_lookup(lat, lon)
        logger.info(f"  GIS: township={twp!r}, municipality={muni!r}")

        provenance = []
        norm = normalize_site(resolved_entity, provenance)

        if norm is None:
            logger.error(f"  !! normalize_site returned None for {eid}")
            remaining_held.append(held)
            continue

        # GPS was injected but normalize_site re-parses from payload;
        # if it came back blank (shouldn't happen), force it
        if not norm.get("gps_lat") and lat:
            norm["gps_lat"] = round(lat, 6)
            norm["gps_lon"] = round(lon, 6)
            norm["plus_code"] = get_plus_code(lat, lon)
            norm["township"]    = twp
            norm["municipality"] = muni

        # Tag GPS confidence in identity_notes
        conf_note = f"GPS confidence: {confidence} (Stage 3 acquisition: {gps_r.get('method','')[:80]})"
        existing_notes = norm.get("identity_notes", "")
        if existing_notes:
            norm["identity_notes"] = f"{existing_notes} | {conf_note}"
        else:
            norm["identity_notes"] = conf_note

        # For LOW confidence, add note to notes field
        if confidence == "LOW":
            low_note = f"GPS is LOW confidence (city/village centroid — {gps_r.get('notes','')[:100]}). Verify before mapping."
            existing = norm.get("notes", "")
            norm["notes"] = f"{existing} {low_note}".strip() if existing else low_note

        # Validate features (Stage 4.5 gate)
        feats = norm.get("features", "")
        violations = []
        for term in (feats or "").split(";"):
            term = term.strip()
            if term and term not in ALLOWED_FEATURES:
                violations.append(term)
        if violations:
            logger.warning(f"  !! Features violations: {violations} — blanking features")
            norm["features"] = ""

        newly_normalized.append(norm)
        merge_log.append({
            "entity_id":  eid,
            "name":        norm["name"],
            "action":      "NORMALIZED",
            "confidence":  confidence,
            "gps_lat":     norm.get("gps_lat"),
            "gps_lon":     norm.get("gps_lon"),
            "plus_code":   norm.get("plus_code"),
            "township":    norm.get("township"),
            "municipality": norm.get("municipality"),
            "notes":       gps_r.get("notes", "")[:120],
        })
        logger.info(f"  → Normalized: ({norm.get('gps_lat')}, {norm.get('gps_lon')}) | {norm.get('plus_code')}")

    # ── Merge newly normalized into normalized_entities.yaml ─────────────────
    norm_entities.extend(newly_normalized)

    # Re-compute entity_by_type counts
    type_counts: dict = {}
    for e in norm_entities:
        et = e.get("entity_type", "Unknown")
        type_counts[et] = type_counts.get(et, 0) + 1

    norm_data["normalized_entities"] = norm_entities
    norm_data["normalized"] = len(norm_entities)
    norm_data["held"] = len(remaining_held)
    norm_data["entities_by_type"] = type_counts
    save_yaml(NORM_FILE, norm_data)
    logger.info(f"\nNormalized entities: {len(norm_entities)} total ({len(newly_normalized)} newly added)")

    # ── Update held_entities.yaml ─────────────────────────────────────────────
    held_data["held_entities"] = remaining_held
    held_data["count"] = len(remaining_held)
    save_yaml(HELD_FILE, held_data)
    logger.info(f"Held entities: {len(remaining_held)} remaining")

    # ── Append GPS merge results to gps_report.md ────────────────────────────
    report_lines = [
        "",
        "## GPS Merge Results (Stage 3 → Normalized)",
        "",
        "| ID | Name | Action | Confidence | GPS Lat | GPS Lon | Plus Code | Township | Municipality |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for entry in merge_log:
        lat_str = f"{entry['gps_lat']:.6f}" if entry.get("gps_lat") else "—"
        lon_str = f"{entry['gps_lon']:.6f}" if entry.get("gps_lon") else "—"
        report_lines.append(
            f"| {entry['entity_id']} | {entry['name']} | {entry['action']} "
            f"| {entry['confidence']} | {lat_str} | {lon_str} "
            f"| {entry.get('plus_code','—')} | {entry.get('township','—')} | {entry.get('municipality','—')} |"
        )

    existing_report = pathlib.Path(REPORT_FILE).read_text()
    pathlib.Path(REPORT_FILE).write_text(existing_report + "\n" + "\n".join(report_lines))
    logger.info(f"GPS report updated → {REPORT_FILE}")

    # ── Summary ───────────────────────────────────────────────────────────────
    logger.info(f"\n{'='*60}")
    logger.info(f"Stage 3 GPS Merge COMPLETE")
    logger.info(f"  Newly normalized: {len(newly_normalized)}")
    logger.info(f"  Remaining held:   {len(remaining_held)}")
    logger.info(f"  Total normalized: {len(norm_entities)}")
    logger.info(f"  Total entities:   {len(norm_entities) + len(remaining_held)}")

    # Print summary of remaining held
    if remaining_held:
        logger.info("\nRemaining held entities (NONE GPS):")
        for h in remaining_held:
            logger.info(f"  {h['record_id']} — {h['name']}")


if __name__ == "__main__":
    main()
