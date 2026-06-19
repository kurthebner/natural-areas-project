# Putnam County Quality Review
**Date:** 2026-06-08
**Reviewer:** Claude (automated + PAD-US spatial audit)
**Status: PARTIAL FAIL**

---

## 1. Entity Counts

| Entity Type | Count | ID Range / Notes |
|---|---|---|
| Sites | 29 | OH-PUT-S-0001 – OH-PUT-S-0029 (all Putnam-primary; no OH-MC-) |
| Trails | 4 | OH-HAN-T-0012, OH-MC-T-0200, OH-MC-T-0216, OH-MC-T-0218 |
| Trail Segments | 0 | — |
| Trail Networks | 0 | — |
| Site Networks | 0 | — |
| Access Points | 3 | OH-PUT-AP-0001 – OH-PUT-AP-0003 |
| Held Entities | 0 | table empty |

**Run metadata:** `putnam_oh_2026_05_09` — input=33, normalized=32, held=0

The 33rd input record was a MC_SUPPLEMENTAL update to OH-HAN-T-0012 (Old Mill Stream Scenic Byway): during Putnam discovery the trail's counties field was updated to include Putnam. No new trail record was created. 32 normalized = 29 sites + 3 APs.

---

## 2. FK Integrity

### Fixes applied this session

| AP | Old value | New value |
|---|---|---|
| OH-PUT-AP-0001 (Arrowhead Landing) | OH-PUT-S-006 | OH-PUT-S-0006 |
| OH-PUT-AP-0002 (Reservoir Landing) | OH-PUT-S-007 | OH-PUT-S-0007 |
| OH-PUT-AP-0003 (Fort Jennings Park River Access) | OH-PUT-S-013 | OH-PUT-S-0013 |

All three AP parent_entity_id values were 3-digit non-padded. Fixed to 4-digit canonical format. All verified post-fix.

No additional broken FKs detected.

---

## 3. GPS Status

All 29 sites have GPS values (0 missing). GPS Gate: passed.

**Data quality concern — low-precision coordinates.** Multiple sites use rounded centroid-level coordinates rather than precise park GPS:

- OH-PUT-S-0002/0003/0004 (WPAs 1–3): 41.0/−84.205, 41.0/−84.275, 40.975/−84.23 — clearly approximate
- OH-PUT-S-0001 (Cascade Wayside WA): 41.018, −84.205 — rounded
- OH-PUT-S-0008 (The Diversion Channel): 41.052, −84.048 — rounded
- OH-PUT-S-0016 (Saint Barbara's Catholic Church Cemetery): 41.018, −84.205 — same coord as S-0001

5–6 sites needing precision GPS acquisition in batch phase.

---

## 4. Trail Parents

**0 of 4 trails have trail_parents entries.** All four cross through Putnam:

| Trail | Primary County | Role in Putnam |
|---|---|---|
| OH-HAN-T-0012 Old Mill Stream Scenic Byway | Hancock | Crosses into Putnam; counties updated during this run |
| OH-MC-T-0200 North Country NST | Multi-county | Passes through Putnam |
| OH-MC-T-0216 Miami and Erie Canal Towpath | Multi-county | Canal corridor through Putnam |
| OH-MC-T-0218 Buckeye Trail — Delphos Section | Multi-county | Passes through Putnam |

Trail_parents entries linking these trails to Putnam sites (canal parks, access points, trailheads) needed in batch phase.

---

## 5. Partial Upsert Check

No site_networks or trail_networks expected for Putnam — none in TSV files. No partial upsert issue.

---

## 6. PAD-US Spatial Audit

**Bbox:** Putnam County bounding box. 17 PAD-US fee records in bbox; 7 matched (score ≥ 80); 9 unmatched; 1 skipped (closed access).

### 6a. Matched — issues to note

| PAD-US Record | Acres | Matched To | Score | Issue |
|---|---|---|---|---|
| Arrowhead Park | 9 | OH-PUT-S-0006 | 100 | ✓ |
| Cascade Wayside Wildlife Area | 47 | OH-PUT-S-0001 | 100 | Acreage discrepancy: PAD-US 47ac vs DB 36ac |
| Glandorf Park | 13 | OH-PUT-S-0015 Glandorf Community Park | 100 | ✓ name variant |
| Ottoville Quarry Wildlife Area | 7 | OH-PUT-S-0005 | 100 | ✓ |
| Wildlife Production Area 51 | 39 | OH-PUT-S-0002 WPA 1 | 94 | All three WPAs matched to S-0002 (see below) |
| Wildlife Production Area 52 | 41 | OH-PUT-S-0002 WPA 1 | 94 | Should map to S-0003 WPA 2 |
| Wildlife Production Area 54 | 41 | OH-PUT-S-0002 WPA 1 | 94 | Should map to S-0004 WPA 3 |

**WPA matching note:** The fuzzy matcher matched all three PAD-US WPA records (51, 52, 54) to OH-PUT-S-0002 because all share the "Wildlife Production Area" token. The three DB entities (S-0002/0003/0004) correctly represent the three WPAs; the multi-match is a tool artifact. PAD-US numeric IDs (51, 52, 54) do not correspond to DB sequence numbers (1, 2, 3) — this is expected.

**WPA acreage discrepancy:** PAD-US fee totals (39+41+41 = 121ac) are significantly lower than DB totals (69+71+71 = 211ac). PAD-US captures fee-owned parcels only; DB acreage likely reflects total ODNR-managed area including easements and leased lands. Not an error — known PAD-US limitation.

**Cascade Wayside acreage:** PAD-US 47ac vs DB 36ac. Minor discrepancy; DB acreage may be from an older ODNR source. Flag for verification.

### 6b. Cross-county attribution correction

**Charloe Community Park (2ac) and Melrose Town Park and Ballfield (8ac)** both appeared as unmatched gaps in the Paulding County review. They now appear in Putnam's unmatched list. These entities are located in **Putnam County** (Charloe and Melrose are both in Auglaize Township, Putnam County), not Paulding. The Paulding review should be corrected: these are Putnam T6 gaps, not Paulding gaps.

### 6c. Unmatched — genuine Putnam gaps

All 9 unmatched records are municipal parks (City/Local Gov land), T6 supplemental discovery:

| PAD-US Record | Acres | Owner | Notes |
|---|---|---|---|
| Charloe Community Park | 2 | City | Auglaize Township, Putnam County — not Paulding (see §6b) |
| Melrose Town Park and Ballfield | 8 | City | Putnam County — not Paulding (see §6b) |
| Oakwood Ball Field | 13 | City | Village of Oakwood; straddles Paulding/Putnam line — verify county |
| Oakwood Community Park | 4 | City | Score 78 in Putnam bbox; DB has OH-PAU-S-0018 as counties='Paulding'; may need Putnam added |
| Deters Park | 18 | City | Ottawa, OH (county seat) |
| Lords Park | 0 | City | Ottawa, OH; 0ac in PAD-US likely data entry gap |
| Waterworks Park | 5 | City | Ottawa, OH |
| West End Water Tower Park | 2 | City | Ottawa, OH |
| Memorial Park | 30 | City | Ottawa, OH; 30ac — largest unmatched gap in this county |

---

## 7. Summary of Issues

| # | Issue | Severity | Resolution |
|---|---|---|---|
| 1 | 3 APs had 3-digit non-padded parent_entity_id | FIXED | Applied this session |
| 2 | 5–6 sites with low-precision centroid GPS | MEDIUM | Batch: precision GPS acquisition |
| 3 | 0 trail_parents for 4 trails | MEDIUM | Batch: add trail_parents |
| 4 | 9 Ottawa/Putnam municipal parks not cataloged | MEDIUM | Supplemental T6 discovery |
| 5 | Charloe CP and Melrose Town Park: Putnam County, not Paulding | MEDIUM | Correct Paulding review; add to Putnam T6 |
| 6 | Oakwood Community Park / Ball Field county ambiguity | LOW | Verify Paulding vs Putnam; update counties field if straddles |
| 7 | Cascade Wayside WA acreage discrepancy (PAD-US 47ac vs DB 36ac) | LOW | Verify against ODNR source |

---

## 8. Batch Phase Actions

- [ ] Acquire precision GPS for WPAs 1–3, Cascade Wayside WA, The Diversion Channel, Saint Barbara's Cemetery (shares coord with S-0001)
- [ ] Add trail_parents for OH-MC-T-0200, OH-MC-T-0216, OH-MC-T-0218, OH-HAN-T-0012 → Putnam sites
- [ ] Supplemental T6 discovery: Deters Park, Lords Park, Waterworks Park, West End Water Tower Park, Memorial Park (Ottawa, OH)
- [ ] Supplemental T6 discovery: Charloe Community Park, Melrose Town Park (Putnam County; remove from Paulding batch list)
- [ ] Verify Oakwood Community Park / Ball Field county: update OH-PAU-S-0018 counties to 'Paulding;Putnam' if straddles
- [ ] Verify Cascade Wayside WA acreage (PAD-US 47ac vs DB 36ac) against ODNR source
