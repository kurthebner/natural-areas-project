#!/usr/bin/env python3
"""
crosscounty_ottawa.py — Cross-County Pass for Ottawa County, Ohio
Produces TSV rows for 7 cross-county entities held from the main pipeline:

  Trails (appended to ottawa_trails.tsv):
    OH-MC-T-0109  Metzger Marsh Trail           (Condition B; Lucas;Ottawa)
    OH-MC-T-0110  North Coast Inland Trail      (Condition B; Erie;Huron;Ottawa;Sandusky)
    OH-OTT-T-124  Lake Erie Islands Water Trail (Scenario A; Ottawa only provisional)
    OH-MC-TR-002  Portage River Water Trail     (Ottawa first to pipeline)

  Site Network (appended to ottawa_site_networks.tsv):
    OH-MC-SN-0002 Ottawa NWR Complex            (Condition B; Lucas;Ottawa)

  Access Points (appended to ottawa_access_points.tsv):
    OH-OTT-AP-007 Oak Harbor Station... Launch  (parent: OH-MC-TR-002 PRWT)
    OH-OTT-AP-008 LEIT Access Point 9 (Clemons) (parent: OH-OTT-T-124 LEIT)

MC ID assignments (from na_cross_county_resolution_v5.2.md):
  T-084  → OH-MC-T-0109  (Condition B: USFWS, no county anchor)
  SN-001 → OH-MC-SN-0002 (Condition B: USFWS, no county anchor)
  T-125  → OH-MC-T-0110  (Condition B: multi-county)
  T-124  → OH-OTT-T-124  (Scenario A: Ottawa-only counties_raw; Erie not yet run)
  PRWT   → OH-MC-TR-002  (pre-existing; Ottawa first to pipeline it)
  AP-007 → OH-OTT-AP-007 (unblocked; parent PRWT confirmed)
  AP-008 → OH-OTT-AP-008 (unblocked; parent LEIT confirmed)
"""

import pathlib, re, sys
from datetime import date

# ── Paths ────────────────────────────────────────────────────────────────
OUT_DIR   = pathlib.Path("/sessions/jolly-kind-bardeen/mnt/outputs")
TRAILS_TSV = OUT_DIR / "ottawa_trails.tsv"
APS_TSV    = OUT_DIR / "ottawa_access_points.tsv"
SNS_TSV    = OUT_DIR / "ottawa_site_networks.tsv"
LOG_PATH   = OUT_DIR / "crosscounty_validation_log.txt"

TODAY = str(date.today())

# ── Helpers ──────────────────────────────────────────────────────────────

def clean(val):
    if val is None:
        return ""
    s = str(val).strip()
    s = s.replace("\t", " ").replace("\n", " ").replace("\r", " ")
    return s

def fmt_counties(raw):
    if not raw:
        return ""
    parts = [p.strip().replace(" County","").strip()
             for p in re.split(r"[;,]", raw) if p.strip()]
    return ";".join(sorted(set(p for p in parts if p)))

def validate_row(row, expected, entity_id, errors):
    if len(row) != expected:
        errors.append(f"  FIELD COUNT: {entity_id} → {len(row)} (expected {expected})")
    for i, val in enumerate(row):
        if "\t" in val:
            errors.append(f"  TAB IN FIELD: {entity_id} f{i+1}")
        if "\n" in val or "\r" in val:
            errors.append(f"  NEWLINE IN FIELD: {entity_id} f{i+1}")
        if val != val.strip():
            errors.append(f"  WHITESPACE: {entity_id} f{i+1}")

errors = []
log_lines = [f"Cross-County Pass — Ottawa County, Ohio — {TODAY}", "="*60]

# ════════════════════════════════════════════════════════════════════════
# TRAILS (19 fields per row)
# ════════════════════════════════════════════════════════════════════════
# Field order:
# 1 Trail Name | 2 Alternate Names | 3 Trail Use Type | 4 Trail Surface Type
# 5 Trail Origin Type | 6 Total Length (Miles) | 7 Counties | 8 Governance
# 9 Partner Agencies | 10 Status | 11 Difficulty | 12 Accessibility
# 13 Description | 14 Trail History | 15 Identity Notes | 16 Notes
# 17 URL | 18 Maps | 19 Trail ID

trail_rows = []
trail_errors = []

# ── T1: OH-MC-T-0109 — Metzger Marsh Trail ──────────────────────────────
r = [
    "Metzger Marsh Trail",                                          # 1
    "",                                                             # 2
    "",                                                             # 3
    "",                                                             # 4
    "",                                                             # 5
    "",                                                             # 6
    "Lucas;Ottawa",                                                 # 7
    "U.S. Fish & Wildlife Service",                                 # 8
    "Ohio Division of Wildlife",                                    # 9
    "Active",                                                       # 10
    "",                                                             # 11
    "",                                                             # 12
    "A trail within the Ottawa National Wildlife Refuge at the Metzger Marsh Unit, a 740-acre coastal marsh along Lake Erie. The eastern 182 acres of the unit lie in Lucas County, co-owned and co-managed by the Ohio Division of Wildlife and USFWS.",  # 13
    "",                                                             # 14
    "Trail at Ottawa NWR — Metzger Marsh Unit. Metzger Marsh Unit spans Ottawa and Lucas counties. Condition B MC ID assigned: OH-MC-T-0109.",  # 15
    "",                                                             # 16
    "https://www.fws.gov/refuge/ottawa/visit-us/trails",           # 17
    "https://www.fws.gov/refuge/ottawa/map?trail=metzger-marsh-trail",  # 18
    "OH-MC-T-0109",                                                 # 19
]
validate_row(r, 19, "OH-MC-T-0109", trail_errors)
trail_rows.append(r)

# ── T2: OH-MC-T-0110 — North Coast Inland Trail ─────────────────────────
r = [
    "North Coast Inland Trail",                                     # 1
    "NCIT",                                                         # 2
    "",                                                             # 3
    "",                                                             # 4
    "Rail Trail",                                                   # 5
    "",                                                             # 6
    "Erie;Huron;Ottawa;Sandusky",                                   # 7
    "Park District of Ottawa County",                               # 8
    "",                                                             # 9
    "Active",                                                       # 10
    "",                                                             # 11
    "",                                                             # 12
    "Approximately 100-mile rail trail from Lorain to Genoa traversing Erie, Huron, Sandusky, and Ottawa counties. The Ottawa County segment runs from the Sandusky County line northwest through Elmore to Veterans Park in Genoa (terminus). Also designated as US Bike Route 30. Trail converts from multi-use paved to on-road route at Martin-Williston Road then reconnects to multi-use paved to the Genoa terminus.",  # 13
    "",                                                             # 14
    "CROSS_COUNTY_CANDIDATE. Spans Erie; Huron; Ottawa; Sandusky counties. Park District of Ottawa County manages the Ottawa County segment. Condition B MC ID assigned: OH-MC-T-0110.",  # 15
    "",                                                             # 16
    "https://ottawacountyparksoh.org/parks-and-trails/north-coast-inland-trail/",  # 17
    "",                                                             # 18
    "OH-MC-T-0110",                                                 # 19
]
validate_row(r, 19, "OH-MC-T-0110", trail_errors)
trail_rows.append(r)

# ── T3: OH-OTT-T-124 — Lake Erie Islands Water Trail (LEIT) ─────────────
r = [
    "Lake Erie Islands Water Trail",                                # 1
    "LEIT",                                                         # 2
    "",                                                             # 3
    "",                                                             # 4
    "",                                                             # 5
    "",                                                             # 6
    "Ottawa",                                                       # 7 (provisional; Erie not yet run)
    "Put-in-Bay Township Park District",                            # 8
    "",                                                             # 9
    "Active",                                                       # 10
    "",                                                             # 11
    "",                                                             # 12
    "ODNR's 12th designated state water trail. Four island-loop segments in Ottawa County: South Bass Island Trail, Middle Bass Island Trail, North Bass Island Trail, and Mainland Trail. Kelleys Island segment is in Erie County.",  # 13
    "",                                                             # 14
    "CROSS_COUNTY_CANDIDATE. ODNR-designated state water trail. Primary managing entity is Put-in-Bay Township Park District (T3 per management tier rule). Kelleys Island segment is Erie County — out of scope for Ottawa County run. Counties provisional (Ottawa only); Erie County not yet processed — Scenario A: provisional ID OH-OTT-T-124 retained until Erie County run.",  # 15
    "",                                                             # 16
    "https://ottawacountyparksoh.org/",                            # 17
    "",                                                             # 18
    "OH-OTT-T-124",                                                 # 19
]
validate_row(r, 19, "OH-OTT-T-124", trail_errors)
trail_rows.append(r)

# ── T4: OH-MC-TR-002 — Portage River Water Trail (PRWT) ─────────────────
# Ottawa County is first to pipeline this entity.
r = [
    "Portage River Water Trail",                                    # 1
    "PRWT",                                                         # 2
    "",                                                             # 3
    "",                                                             # 4
    "",                                                             # 5
    "36.0",                                                         # 6 total trail length (miles)
    "Ottawa;Wood",                                                  # 7
    "Toledo Metropolitan Area Council of Governments",              # 8
    "Park District of Ottawa County; U.S. Fish & Wildlife Service; Ohio Department of Natural Resources",  # 9
    "Active",                                                       # 10
    "",                                                             # 11
    "",                                                             # 12
    "A 36-mile state-designated water trail on the Portage River, officially designated July 19, 2022, spanning Ottawa and Wood counties. The Ottawa County segment runs from Lake Erie Beach Access in Port Clinton (Mile 0) to approximately Mile 23 near Elmore, with 8 documented Ottawa County launch sites.",  # 13
    "Officially state-designated by ODNR on July 19, 2022. Coordinated by TMACOG with USFWS, ODNR, and partner organizations.",  # 14
    "KNOWN_MC:OH-MC-TR-002. Ottawa/Wood multi-county water trail. Ottawa County is first county to pipeline this entity. Confirmed via PDOC website.",  # 15
    "",                                                             # 16
    "https://ottawacountyparksoh.org/parks-and-trails/portage-river-water-trail/",  # 17
    "",                                                             # 18
    "OH-MC-TR-002",                                                 # 19
]
validate_row(r, 19, "OH-MC-TR-002", trail_errors)
trail_rows.append(r)

# ── Append trail rows to ottawa_trails.tsv ──────────────────────────────
existing_trails = TRAILS_TSV.read_text(encoding="utf-8")
if not existing_trails.endswith("\n"):
    existing_trails += "\n"
new_trail_lines = "\n".join("\t".join(r) for r in trail_rows) + "\n"
TRAILS_TSV.write_text(existing_trails + new_trail_lines, encoding="utf-8")

trail_count = len(existing_trails.splitlines())
log_lines.append(f"\n[TRAILS] Appended {len(trail_rows)} cross-county rows to ottawa_trails.tsv")
log_lines.append(f"  Previous row count: {trail_count}")
log_lines.append(f"  New total: {trail_count + len(trail_rows)}")
if trail_errors:
    log_lines.append(f"  ERRORS ({len(trail_errors)}):")
    log_lines.extend(trail_errors)
else:
    log_lines.append("  No errors.")
errors.extend(trail_errors)

# ════════════════════════════════════════════════════════════════════════
# SITE NETWORKS (15 fields per row)
# ════════════════════════════════════════════════════════════════════════
# Field order:
# 1 Network Name | 2 Network Type | 3 Status | 4 Ownership | 5 Governance
# 6 Partner Agencies | 7 Counties | 8 States Included | 9 Member Count
# 10 Member Site IDs | 11 Description | 12 Identity Notes | 13 Notes
# 14 URL | 15 Network ID

sn_rows = []
sn_errors = []

# ── SN1: OH-MC-SN-0002 — Ottawa National Wildlife Refuge Complex ─────────
r = [
    "Ottawa National Wildlife Refuge Complex",                      # 1
    "Wildlife Refuge Complex",                                      # 2
    "Active",                                                       # 3
    "Federal",                                                      # 4
    "U.S. Fish & Wildlife Service",                                 # 5
    "",                                                             # 6
    "Lucas;Ottawa",                                                 # 7
    "",                                                             # 8 (Ohio-only scope; Schoonover WPA Michigan out of scope)
    "",                                                             # 9 (Ohio member count not pinned)
    "",                                                             # 10 (member site IDs not yet resolved)
    "Ohio's only National Wildlife Refuge Complex, formally designated by USFWS. Ohio members include Ottawa NWR (Ottawa County), Cedar Point NWR (Lucas County), and West Sister Island NWR (Lucas County). Schoonover Waterfowl Production Area in Michigan is administratively part of the complex but is out of Ohio scope.",  # 11
    "USFWS formally designates this as the 'Ottawa National Wildlife Refuge Complex' — Ohio's only NWR complex. Spans Ottawa and Lucas counties. Schoonover WPA (Michigan) out of Ohio scope. Condition B MC ID assigned: OH-MC-SN-0002.",  # 12
    "",                                                             # 13
    "https://www.fws.gov/refuge/ottawa",                           # 14
    "OH-MC-SN-0002",                                               # 15
]
validate_row(r, 15, "OH-MC-SN-0002", sn_errors)
sn_rows.append(r)

# ── Append SN rows to ottawa_site_networks.tsv ──────────────────────────
existing_sn = SNS_TSV.read_text(encoding="utf-8")
if not existing_sn.endswith("\n"):
    existing_sn += "\n"
new_sn_lines = "\n".join("\t".join(r) for r in sn_rows) + "\n"
SNS_TSV.write_text(existing_sn + new_sn_lines, encoding="utf-8")

sn_count = len(existing_sn.splitlines())
log_lines.append(f"\n[SITE NETWORKS] Appended {len(sn_rows)} cross-county rows to ottawa_site_networks.tsv")
log_lines.append(f"  Previous row count: {sn_count}")
log_lines.append(f"  New total: {sn_count + len(sn_rows)}")
if sn_errors:
    log_lines.append(f"  ERRORS ({len(sn_errors)}):")
    log_lines.extend(sn_errors)
else:
    log_lines.append("  No errors.")
errors.extend(sn_errors)

# ════════════════════════════════════════════════════════════════════════
# ACCESS POINTS (17 fields per row)
# ════════════════════════════════════════════════════════════════════════
# Field order:
# 1 Access Point Name | 2 Access Point Type | 3 Status
# 4 Identity Parent Entity Type | 5 Identity Parent Entity Name
# 6 County | 7 Township | 8 Municipality | 9 Address
# 10 GPS Lat | 11 GPS Lon | 12 Plus Code | 13 Features
# 14 Identity Notes | 15 Notes | 16 URL | 17 Access Point ID

ap_rows = []
ap_errors = []

# ── AP1: OH-OTT-AP-007 — Oak Harbor Station Interurban Overlook ─────────
r = [
    "Oak Harbor Station Interurban Overlook and Hand Powered Boat Launch",  # 1
    "",                                                             # 2 (ap_type_raw was blank)
    "Active",                                                       # 3
    "Trail",                                                        # 4
    "Portage River Water Trail",                                    # 5
    "Ottawa",                                                       # 6
    "",                                                             # 7 (GIS-derived; GPS unavailable)
    "Oak Harbor",                                                   # 8
    "South end of Church Street, Oak Harbor, OH 43449",            # 9
    "",                                                             # 10
    "",                                                             # 11
    "",                                                             # 12
    "ADA accessible overlook; Seating; Floating docks for hand-powered watercraft; Fishing access",  # 13
    "Water access point on Portage River (Portage River Water Trail; OH-MC-TR-002). 'Interurban' name refers to historical interurban rail corridor.",  # 14
    "",                                                             # 15
    "https://www.oakharbor.oh.us/departments/public_works/parks.php",  # 16
    "OH-OTT-AP-007",                                               # 17
]
validate_row(r, 17, "OH-OTT-AP-007", ap_errors)
ap_rows.append(r)

# ── AP2: OH-OTT-AP-008 — LEIT Access Point 9 (Lucien M. Clemons Park) ───
r = [
    "Lake Erie Islands Water Trail — Access Point 9 (Lucien M. Clemons Park)",  # 1
    "Kayak-Canoe Launch",                                           # 2
    "Active",                                                       # 3
    "Trail",                                                        # 4
    "Lake Erie Islands Water Trail",                                # 5
    "Ottawa",                                                       # 6
    "",                                                             # 7 (GIS-derived; GPS unavailable)
    "Marblehead",                                                   # 8
    "East end of Lucien M. Clemons Park, Marblehead, OH 43440",   # 9
    "",                                                             # 10
    "",                                                             # 11
    "",                                                             # 12
    "Kayak/canoe launch; Lake Erie access",                         # 13
    "Access Point 9 of Lake Erie Islands Water Trail (LEIT; OH-OTT-T-124). Parent site: Lucien M. Clemons Park. Physical access managed by Village of Marblehead within the park.",  # 14
    "",                                                             # 15
    "https://www.marbleheadohio.org/parks/page/lucien-m-clemons-park",  # 16
    "OH-OTT-AP-008",                                               # 17
]
validate_row(r, 17, "OH-OTT-AP-008", ap_errors)
ap_rows.append(r)

# ── Append AP rows to ottawa_access_points.tsv ──────────────────────────
existing_aps = APS_TSV.read_text(encoding="utf-8")
if not existing_aps.endswith("\n"):
    existing_aps += "\n"
new_ap_lines = "\n".join("\t".join(r) for r in ap_rows) + "\n"
APS_TSV.write_text(existing_aps + new_ap_lines, encoding="utf-8")

ap_count = len(existing_aps.splitlines())
log_lines.append(f"\n[ACCESS POINTS] Appended {len(ap_rows)} cross-county rows to ottawa_access_points.tsv")
log_lines.append(f"  Previous row count: {ap_count}")
log_lines.append(f"  New total: {ap_count + len(ap_rows)}")
if ap_errors:
    log_lines.append(f"  ERRORS ({len(ap_errors)}):")
    log_lines.extend(ap_errors)
else:
    log_lines.append("  No errors.")
errors.extend(ap_errors)

# ════════════════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════════════════
log_lines.append("\n" + "="*60)
log_lines.append("CROSS-COUNTY PASS SUMMARY")
log_lines.append("-"*40)
log_lines.append(f"  Trail rows appended:        {len(trail_rows)}")
log_lines.append(f"  Site Network rows appended: {len(sn_rows)}")
log_lines.append(f"  Access Point rows appended: {len(ap_rows)}")
log_lines.append(f"  Total cross-county rows:    {len(trail_rows)+len(sn_rows)+len(ap_rows)}")
log_lines.append(f"  Total errors:               {len(errors)}")
log_lines.append("")
log_lines.append("MC ID assignments:")
log_lines.append("  OH-OTT-T-084  → OH-MC-T-0109   (Metzger Marsh Trail; Condition B)")
log_lines.append("  OH-OTT-T-125  → OH-MC-T-0110   (North Coast Inland Trail; Condition B)")
log_lines.append("  OH-OTT-T-124  → OH-OTT-T-124   (LEIT; Scenario A; provisional)")
log_lines.append("  PRWT          → OH-MC-TR-002    (pre-existing; Ottawa first to pipeline)")
log_lines.append("  OH-OTT-SN-001 → OH-MC-SN-0002  (Ottawa NWR Complex; Condition B)")
log_lines.append("  OH-OTT-AP-007 → OH-OTT-AP-007  (Oak Harbor; unblocked; parent PRWT)")
log_lines.append("  OH-OTT-AP-008 → OH-OTT-AP-008  (Clemons/LEIT; unblocked; parent LEIT)")

LOG_PATH.write_text("\n".join(log_lines) + "\n", encoding="utf-8")
print("\n".join(log_lines))

if errors:
    print(f"\n*** {len(errors)} ERRORS — review log before proceeding ***")
    sys.exit(1)
else:
    print("\n✓ Cross-county pass complete. All rows validated. No errors.")
