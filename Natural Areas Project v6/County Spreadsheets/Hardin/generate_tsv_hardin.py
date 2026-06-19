#!/usr/bin/env python3
"""
generate_tsv_hardin.py — Generate TSV output for Hardin County
Stages 6, 6.5, 7 (TSV Output, Vocabulary Validation Gate, Integrity Check)

Reads hardin_config.json and writes four TSV files per the v6.0 output specs.
Held entities are excluded from all TSV files.

Field counts (v6.0):
  Sites:         31 fields, 30 tabs
  Trailthings:   31 fields, 30 tabs
  Site Networks: 18 fields, 17 tabs
  Access Points: 20 fields, 19 tabs

Usage:
    python County_Spreadsheets/Hardin/generate_tsv_hardin.py
"""

import csv
import json
import os
import sys
from datetime import datetime, timezone

COUNTY_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_FILE = os.path.join(COUNTY_DIR, "hardin_config.json")
TODAY       = "2026-06-01"

# ── Vocabulary sets for validation ────────────────────────────────────────────
SITE_CATEGORIES = {
    "Campground", "Cemetery", "Community Garden", "Conservation Area",
    "Cultural Facility", "Curated Biological Site", "Fishing Area",
    "Historic Site", "Hunting Area", "Memorial", "Museum", "Natural Area",
    "Nature Preserve", "Open Space", "Park", "Recreation Facility",
    "Water Site", "Wildlife Area",
}
SITE_STATUSES = {
    "Active", "Seasonal", "Access Permit Required", "No Public Entry",
    "Under Development", "Proposed", "Abandoned", "Closed", "Defunct", "Unknown",
}
TT_USE_TYPES  = {"Multi-Use", "Hiking", "Bridle", "Water", "Bicycling",
                 "Mountain Bike", "BMX", "Pump Track", "Snowmobile",
                 "Cross Country Ski", "Other", ""}
TT_SURFACES   = {"Paved", "Crushed Stone", "Gravel", "Natural Surface",
                 "Boardwalk", "Water", "Mixed", "Other", ""}
TT_ORIGINS    = {"Rail Trail", "Canal Towpath", "Historic Route",
                 "Greenway Corridor", "Purpose-Built", "Utility Corridor",
                 "Roadside Corridor", "Waterway", "Other", ""}
TT_ORG_TYPES  = {"Federal Agency", "State Agency", "Regional Authority",
                 "County Authority", "Municipal Department", "Land Trust",
                 "Nonprofit Conservancy", "Trail Association",
                 "Coordinating Body", "Other", ""}
TT_STATUSES   = {"Active", "Planned", "Under Construction", "Gap", "Closed",
                 "Under Development", "Partially Open", ""}
SN_NETWORK_TYPES = {
    "National Heritage Area", "Scenic River Corridor", "Heritage Corridor",
    "Historic Corridor", "Conservation Corridor", "Ecological Corridor",
    "Cultural Landscape Network", "Watershed Network", "Greenway Network",
    "Local Historic District", "Park District System", "Municipal Recreation System",
    "State Program Portfolio", "Federal Program Portfolio", "Land Trust Portfolio",
    "Conservation Authority Portfolio", "Nonprofit Conservation Portfolio", "Other", "",
}
SN_ORG_TYPES  = {"Federal Agency", "State Agency", "Regional Authority",
                 "County Authority", "Municipal Department", "Land Trust",
                 "Nonprofit Conservancy", "Trail Association",
                 "Coordinating Body", "Other", ""}
SN_STATUSES   = {"Active", "Inactive", "Proposed", "Discontinued", ""}
AP_TYPES      = {
    "Trailhead", "Parking Area", "Boat Ramp", "Boat Launch",
    "Watercraft Access Point", "River Access", "Fishing Access", "Hazard Portage",
    "Bicycle Access", "Snowmobile Access", "Cross Country Ski Access",
    "Equestrian Access", "Roadside Pull-Off", "Pedestrian Entrance",
    "Vehicle Entrance", "Transit Access", "Ferry Access", "Shuttle Access",
    "Administrative Access", "Other", "",
}
AP_STATUSES   = {"Active", "Seasonal", "Closed", "Restricted", ""}

# ── Field formatting helpers ───────────────────────────────────────────────────

def v(val, default=""):
    """Return value as string, or default if null/empty."""
    if val is None:
        return default
    s = str(val).strip()
    return s if s else default

def gps_str(val):
    if val is None or val == "":
        return ""
    try:
        return f"{float(val):.6f}"
    except (ValueError, TypeError):
        return ""

def bool_str(val):
    if val is True or str(val).lower() in ("true", "1", "yes"):
        return "true"
    return "false"

def acres_str(val):
    if val is None:
        return ""
    try:
        f = float(val)
        return f"{f:.2f}" if f != int(f) else str(int(f))
    except (ValueError, TypeError):
        return ""

def join_urls(urls_str):
    """Return semicolon-delimited URL list."""
    if not urls_str:
        return ""
    return urls_str

# ── TSV writers ───────────────────────────────────────────────────────────────

def write_sites_tsv(sites: list, out_path: str) -> list:
    """Write sites TSV (31 fields). Returns list of vocab violations."""
    violations = []
    header = [
        "name", "category", "subtype", "designation", "status",
        "ownership", "governance", "partner_agencies", "coordination",
        "description", "habitat_type", "features", "access_notes",
        "location", "acres", "counties", "municipality", "township",
        "gps_lat", "gps_lon", "plus_code", "notes", "url_primary", "urls",
        "last_verified_date", "field_verified",
        "parent_site_id", "parent_site_name",
        "created_at", "updated_at", "ebird_hotspot_id",
    ]
    assert len(header) == 31, f"Site header count: {len(header)}"

    with open(out_path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n",
                       quoting=csv.QUOTE_NONE, escapechar="\\")
        w.writerow(header)
        for s in sites:
            if s.get("status_flag") in ("cross_county_held", "identity_uncertain",
                                        "parent_held", "gps_missing"):
                continue
            # Vocab validation
            cat = v(s.get("category"))
            if cat and cat not in SITE_CATEGORIES:
                violations.append(f"Site '{s.get('site_id')}': invalid category '{cat}'")
            st = v(s.get("status", "Active"))
            if st and st not in SITE_STATUSES:
                violations.append(f"Site '{s.get('site_id')}': invalid status '{st}'")

            now = TODAY + "T00:00:00+00:00"
            row = [
                v(s.get("name")),
                cat,
                v(s.get("subtype")),
                v(s.get("designation")),
                st,
                v(s.get("ownership")),
                v(s.get("governance")),
                v(s.get("partner_agencies")),
                v(s.get("coordination")),
                v(s.get("description")),
                v(s.get("habitat_type")),
                v(s.get("features")),
                v(s.get("access_notes")),
                v(s.get("location")),
                acres_str(s.get("acres")),
                v(s.get("counties")),
                v(s.get("municipality")),
                v(s.get("township")),
                gps_str(s.get("gps_lat")),
                gps_str(s.get("gps_lon")),
                v(s.get("plus_code")),
                v(s.get("notes")),
                v(s.get("url_primary")),
                join_urls(v(s.get("urls"))),
                v(s.get("last_verified_date", TODAY)),
                bool_str(s.get("field_verified", False)),
                v(s.get("parent_site_id")),
                v(s.get("parent_site_name")),
                now,
                now,
                v(s.get("ebird_hotspot_id")),
            ]
            assert len(row) == 31, f"Row field count {len(row)} for {s.get('site_id')}"
            # Verify 30 tabs
            line = "\t".join(str(x) for x in row)
            assert line.count("\t") == 30, f"Tab count {line.count(chr(9))} for {s.get('site_id')}"
            w.writerow(row)
    return violations


def write_trailthings_tsv(tts: list, out_path: str) -> list:
    """Write trailthings TSV (31 fields)."""
    violations = []
    header = [
        "name", "alternate_names", "source_term", "source_hierarchy_context",
        "parent_id", "parent_name", "site_parent_id", "site_parent_name",
        "parent_site_network_id", "parent_site_network_name",
        "use_type", "surface_type", "origin_type", "org_type", "status",
        "difficulty", "accessibility", "ownership", "governance",
        "partner_agencies", "coordination", "counties", "states_included",
        "total_length", "description", "trail_history", "identity_notes",
        "notes", "url", "maps", "trailthing_id",
    ]
    assert len(header) == 31

    with open(out_path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n",
                       quoting=csv.QUOTE_NONE, escapechar="\\")
        w.writerow(header)
        for t in tts:
            if t.get("status_flag") in ("parent_held", "gps_missing"):
                continue
            # source_term warn if blank
            if not v(t.get("source_term")):
                print(f"  WARN: Trailthing {t.get('trailthing_id')} source_term is blank")

            use  = v(t.get("use_type"))
            surf = v(t.get("surface_type"))
            orig = v(t.get("origin_type"))
            org  = v(t.get("org_type"))
            stat = v(t.get("status"))

            if use and use not in TT_USE_TYPES:
                violations.append(f"TT {t.get('trailthing_id')}: invalid use_type '{use}'")
            if surf and surf not in TT_SURFACES:
                violations.append(f"TT {t.get('trailthing_id')}: invalid surface_type '{surf}'")
            if orig and orig not in TT_ORIGINS:
                violations.append(f"TT {t.get('trailthing_id')}: invalid origin_type '{orig}'")
            if org and org not in TT_ORG_TYPES:
                violations.append(f"TT {t.get('trailthing_id')}: invalid org_type '{org}'")
            if stat and stat not in TT_STATUSES:
                violations.append(f"TT {t.get('trailthing_id')}: invalid status '{stat}'")

            length = v(t.get("total_length"))
            if length:
                try: length = str(float(length))
                except ValueError: pass

            row = [
                v(t.get("name")),
                v(t.get("alternate_names")),
                v(t.get("source_term")),
                v(t.get("source_hierarchy_context")),
                v(t.get("parent_id")),
                v(t.get("parent_name")),
                v(t.get("site_parent_id")),
                v(t.get("site_parent_name")),
                v(t.get("parent_site_network_id")),
                v(t.get("parent_site_network_name")),
                use, surf, orig, org, stat,
                v(t.get("difficulty")),
                v(t.get("accessibility")),
                v(t.get("ownership")),
                v(t.get("governance")),
                v(t.get("partner_agencies")),
                v(t.get("coordination")),
                v(t.get("counties")),
                v(t.get("states_included")),
                length,
                v(t.get("description")),
                v(t.get("trail_history")),
                v(t.get("identity_notes")),
                v(t.get("notes")),
                v(t.get("url")),
                v(t.get("maps")),
                v(t.get("trailthing_id")),
            ]
            assert len(row) == 31
            w.writerow(row)
    return violations


def write_site_networks_tsv(sns: list, out_path: str) -> list:
    """Write site networks TSV (18 fields)."""
    violations = []
    header = [
        "network_name", "network_type", "org_type", "status",
        "ownership", "governance", "partner_agencies", "coordination",
        "counties", "states_included", "member_count", "member_site_ids",
        "member_site_names", "description", "identity_notes", "notes",
        "url", "network_id",
    ]
    assert len(header) == 18

    with open(out_path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n",
                       quoting=csv.QUOTE_NONE, escapechar="\\")
        w.writerow(header)
        for sn in sns:
            nt  = v(sn.get("network_type"))
            org = v(sn.get("org_type"))
            st  = v(sn.get("status", "Active"))
            if nt and nt not in SN_NETWORK_TYPES:
                violations.append(f"SN {sn.get('network_id')}: invalid network_type '{nt}'")
            if org and org not in SN_ORG_TYPES:
                violations.append(f"SN {sn.get('network_id')}: invalid org_type '{org}'")
            if st and st not in SN_STATUSES:
                violations.append(f"SN {sn.get('network_id')}: invalid status '{st}'")

            mc = sn.get("member_count")
            row = [
                v(sn.get("name")),
                nt, org, st,
                v(sn.get("ownership")),
                v(sn.get("governance")),
                v(sn.get("partner_agencies")),
                v(sn.get("coordination")),
                v(sn.get("counties")),
                v(sn.get("states_included")),
                str(mc) if mc else "",
                v(sn.get("member_site_ids")),
                v(sn.get("member_site_names")),
                v(sn.get("description")),
                v(sn.get("identity_notes")),
                v(sn.get("notes")),
                v(sn.get("url")),
                v(sn.get("network_id")),
            ]
            assert len(row) == 18
            w.writerow(row)
    return violations


def write_access_points_tsv(aps: list, out_path: str) -> list:
    """Write access points TSV (20 fields)."""
    violations = []
    header = [
        "access_point_name", "access_point_type", "status",
        "identity_parent_entity_type", "identity_parent_entity_id",
        "identity_parent_entity_name", "county", "township", "municipality",
        "address", "gps_lat", "gps_lon", "plus_code", "features",
        "identity_notes", "notes", "url",
        "last_verified_date", "field_verified", "access_point_id",
    ]
    assert len(header) == 20

    with open(out_path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n",
                       quoting=csv.QUOTE_NONE, escapechar="\\")
        w.writerow(header)
        for ap in aps:
            if ap.get("status_flag") in ("parent_held", "gps_missing"):
                continue
            apt = v(ap.get("ap_type"))
            st  = v(ap.get("status", "Active"))
            if apt and apt not in AP_TYPES:
                violations.append(f"AP {ap.get('access_point_id')}: invalid ap_type '{apt}'")
            if st and st not in AP_STATUSES:
                violations.append(f"AP {ap.get('access_point_id')}: invalid status '{st}'")

            row = [
                v(ap.get("name")),
                apt, st,
                v(ap.get("identity_parent_entity_type")),
                v(ap.get("identity_parent_entity_id")),
                v(ap.get("identity_parent_entity_name")),
                v(ap.get("county")),
                v(ap.get("township")),
                v(ap.get("municipality")),
                v(ap.get("address")),
                gps_str(ap.get("gps_lat")),
                gps_str(ap.get("gps_lon")),
                v(ap.get("plus_code")),
                v(ap.get("features")),
                v(ap.get("identity_notes")),
                v(ap.get("notes")),
                v(ap.get("url")),
                v(ap.get("last_verified_date", TODAY)),
                bool_str(ap.get("field_verified", False)),
                v(ap.get("access_point_id")),
            ]
            assert len(row) == 20
            w.writerow(row)
    return violations


# ── Stage 7: TSV integrity check ──────────────────────────────────────────────

def integrity_check(tsv_path: str, expected_fields: int, expected_tabs: int,
                    entity_type: str) -> list:
    warnings = []
    with open(tsv_path, encoding="utf-8") as f:
        for i, line in enumerate(f):
            line = line.rstrip("\n")
            tabs = line.count("\t")
            if tabs != expected_tabs:
                warnings.append(f"{entity_type} row {i}: expected {expected_tabs} tabs, got {tabs}")
    return warnings


# ── Stage 6.5: Vocabulary expansion candidates ────────────────────────────────

def surface_vocab_candidates(config: dict) -> list:
    """Surface any features_raw tokens that didn't map to vocabulary."""
    candidates = []
    # Quick check for common Hardin-specific terms
    hardin_terms = set()
    for s in config.get("sites", []):
        raw = s.get("features_raw", "")
        if raw:
            hardin_terms.add(raw[:80])
    # Just report any with features_raw but empty features
    for s in config.get("sites", []):
        if s.get("features_raw") and not s.get("features"):
            candidates.append(f"Site {s.get('site_id')} '{s.get('name', '')[:30]}': features_raw has content but no mapped features")
    return candidates


# ── Main ───────────────────────────────────────────────────────────────────────

def main():
    print(f"\n{'='*60}")
    print(f"Hardin County TSV Generation — Stages 6, 6.5, 7")
    print(f"{'='*60}\n")

    with open(CONFIG_FILE, encoding="utf-8") as f:
        config = json.load(f)

    sites = config.get("sites", [])
    tts   = config.get("trailthings", [])
    sns   = config.get("site_networks", [])
    aps   = config.get("access_points", [])

    # Count non-held entities
    sites_active = [s for s in sites if not s.get("status_flag") in
                    ("cross_county_held","identity_uncertain","parent_held","gps_missing")]
    tts_active   = [t for t in tts if not t.get("status_flag") in ("parent_held",)]
    aps_active   = [ap for ap in aps if not ap.get("status_flag") in ("parent_held","gps_missing")]

    print(f"Writing TSV for:")
    print(f"  Sites:         {len(sites_active)} (of {len(sites)} normalized)")
    print(f"  Trailthings:   {len(tts_active)}")
    print(f"  Site Networks: {len(sns)}")
    print(f"  Access Points: {len(aps_active)}")
    print()

    # Stage 6: Write TSV files
    site_tsv = os.path.join(COUNTY_DIR, "hardin_sites.tsv")
    tt_tsv   = os.path.join(COUNTY_DIR, "hardin_trailthings.tsv")
    sn_tsv   = os.path.join(COUNTY_DIR, "hardin_site_networks.tsv")
    ap_tsv   = os.path.join(COUNTY_DIR, "hardin_access_points.tsv")

    v_site = write_sites_tsv(sites, site_tsv)
    v_tt   = write_trailthings_tsv(tts, tt_tsv)
    v_sn   = write_site_networks_tsv(sns, sn_tsv)
    v_ap   = write_access_points_tsv(aps, ap_tsv)

    all_violations = v_site + v_tt + v_sn + v_ap

    print("Stage 6: TSV files written")
    print(f"  {site_tsv}")
    print(f"  {tt_tsv}")
    print(f"  {sn_tsv}")
    print(f"  {ap_tsv}")
    print()

    # Stage 6.5: Vocabulary validation gate
    print("Stage 6.5: Vocabulary Validation Gate")
    if all_violations:
        print("  VIOLATIONS FOUND — pipeline halted:")
        for v_ in all_violations:
            print(f"  !! {v_}")
        sys.exit(1)
    else:
        print("  PASS — no vocabulary violations")
    print()

    # Vocabulary expansion candidates (informational)
    candidates = surface_vocab_candidates(config)
    if candidates:
        print("  Vocabulary expansion candidates (informational):")
        for c_ in candidates[:10]:
            print(f"    - {c_}")
    print()

    # Stage 7: TSV integrity check
    print("Stage 7: TSV Integrity Check")
    w_site = integrity_check(site_tsv, 31, 30, "Site")
    w_tt   = integrity_check(tt_tsv,   31, 30, "Trailthing")
    w_sn   = integrity_check(sn_tsv,   18, 17, "Site Network")
    w_ap   = integrity_check(ap_tsv,   20, 19, "Access Point")

    all_warnings = w_site + w_tt + w_sn + w_ap
    if all_warnings:
        print("  INTEGRITY WARNINGS:")
        for w_ in all_warnings[:20]:
            print(f"  WARN: {w_}")
        print(f"  Total warnings: {len(all_warnings)}")
    else:
        print("  PASS — all files pass delimiter integrity check")
    print()

    # Stage 7.5 gate message
    print("="*60)
    print("STAGE 7.5 — HUMAN REVIEW GATE")
    print("="*60)
    print()
    print("The pipeline halts here. Before Stage 8 upsert, please review:")
    print(f"  Sites:         {len(sites_active)} entities")
    print(f"  Trailthings:   {len(tts_active)} entities")
    print(f"  Site Networks: {len(sns)} entities")
    print(f"  Access Points: {len(aps_active)} entities")
    print()
    print("Review checklist:")
    print("  [ ] Entity counts look reasonable — no unexpected zeros or inflated counts")
    print("  [ ] Category/subtype assignments are substantively correct")
    print("  [ ] GPS spot-check: a few coordinates look plausible on a map")
    print("  [ ] Held entities are expected — no surprises")
    print("  [ ] AP-to-Site reclassification check (IMP-114) — no APs should be reclassified")
    print("  [ ] Vocabulary expansion candidates reviewed")
    print()

    # Summary
    held = config.get("held_entities", [])
    from collections import Counter
    held_counts = Counter(h["hold_reason"] for h in held)
    print("Held entity summary:")
    for reason, count in held_counts.items():
        print(f"  {reason}: {count}")
    print()
    print("TSV files to review:")
    print(f"  {site_tsv}")
    print(f"  {tt_tsv}")
    print(f"  {sn_tsv}")
    print(f"  {ap_tsv}")
    print()
    print("To proceed to Stage 8, confirm review in session and run upsert script.")
    print("="*60)


if __name__ == "__main__":
    main()
