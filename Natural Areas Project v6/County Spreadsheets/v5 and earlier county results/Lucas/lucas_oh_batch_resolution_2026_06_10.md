# Lucas County — Batch Resolution Log
**Date:** 2026-06-10
**Run ID:** `BATCH_LUC_2026-06-10`
**Source:** Quality review 2026-06-08; QR status: PASS with pipeline work
**Script:** `outputs/batch_luc.py`

---

## 1. Site Networks (3 new, OH-LUC-SN-0001–0003)

Sourced from `LUC_site_networks.tsv`. All inserted. One data fix applied.

| SN ID | Name | Members | Counties | Fix Applied |
|-------|------|---------|----------|-------------|
| OH-LUC-SN-0001 | Metroparks Toledo | 23 | Fulton;Lucas;Ottawa;Wood | TSV used 3-digit, "; " separator — padded to 4-digit, semicolon-only |
| OH-LUC-SN-0002 | Sylvania Area Joint Recreation District | 4 | Lucas | TSV counties field "Lucas, Ohio" → "Lucas" |
| OH-LUC-SN-0003 | Olander Park System | 6 | Lucas | Member IDs padded: 3-digit → 4-digit |

**Metroparks Toledo member IDs** (all confirmed in DB before insert):
OH-LUC-S-0013; OH-LUC-S-0014; OH-LUC-S-0015; OH-LUC-S-0016; OH-LUC-S-0017;
OH-LUC-S-0018; OH-LUC-S-0019; OH-LUC-S-0020; OH-MC-S-0021; OH-LUC-S-0022;
OH-LUC-S-0023; OH-MC-S-0024; OH-MC-S-0025; OH-LUC-S-0026; OH-MC-S-0027;
OH-LUC-S-0028; OH-LUC-S-0029; OH-LUC-S-0030; OH-LUC-S-0031; OH-LUC-S-0032;
OH-LUC-S-0033; OH-LUC-S-0034; OH-LUC-S-0035

**Sylvania AJRD member IDs:** OH-LUC-S-0037; OH-LUC-S-0038; OH-LUC-S-0039; OH-LUC-S-0040

**Olander member IDs:** OH-LUC-S-0046; OH-LUC-S-0047; OH-LUC-S-0048; OH-LUC-S-0049; OH-LUC-S-0050; OH-LUC-S-0051

---

## 2. Trail Segment: WCT North Fork (OH-MC-TS-0007)

`LUC_trail_segments.tsv` had 2 records:
- **WCT South Fork** — already in DB as OH-MC-TS-0005. No action.
- **WCT North Fork** — not in DB. Inserted as OH-MC-TS-0007.

| Field | Value |
|-------|-------|
| segment_id | OH-MC-TS-0007 |
| parent_trail_id | OH-MC-T-0221 |
| name | Wabash Cannonball Trail — North Fork |
| counties | Fulton;Henry;Lucas;Williams |
| governance | Metropolitan Park District of the Toledo Area |
| status | Active |

Prior MC-TS sequences in DB: 0002, 0005, 0006. Next available was 0007.

---

## 3. Trail Parents (48 new entries)

Pre-batch: 7 trail_parents existed for OH-LUC-T-0001 through OH-LUC-T-0007 (from original pipeline).
Added 48 entries for T-0008 onward (T-0011, T-0078, T-0080, T-0081 sent to MRQ).
Post-batch: 55 total LUC trail_parents.

### Mapping Summary

| Trails | Parent Site | Basis |
|--------|-------------|-------|
| T-0012 | OH-LUC-S-0150 | "University/Parks Trail" — Ottawa Park |
| T-0014 | OH-MC-S-0024 | Oak Openings Corridor Trail — Oak Openings Preserve Metropark |
| T-0015 | OH-LUC-S-0030 | Swan Creek Connector — Swan Creek Preserve Metropark |
| T-0018 | OH-LUC-S-0014 | Blue Creek Quarry Loop — Blue Creek Metropark |
| T-0019 | OH-LUC-S-0017 | Fallen Timbers NW Territory Trail — Fallen Timbers Battlefield Metropark |
| T-0031–T-0037 (7) | OH-LUC-S-0026 | Pearson Metropark (trail name prefix match) |
| T-0040–T-0048 (9) | OH-LUC-S-0028 | Secor Metropark (trail name prefix match) |
| T-0049–T-0052 (4) | OH-LUC-S-0029 | Side Cut Metropark (trail name prefix match) |
| T-0053–T-0059 (7) | OH-LUC-S-0030 | Swan Creek Preserve Metropark (trail name prefix match) |
| T-0060 | OH-LUC-S-0032 | Westwinds Trail — Westwinds Metropark |
| T-0061–T-0067 (7) | OH-LUC-S-0033 | Wildwood Preserve Metropark (trail name prefix match) |
| T-0068 | OH-LUC-S-0034 | Wiregrass Loop — Wiregrass Lake Metropark |
| T-0069 | OH-LUC-S-0023 | Middlegrounds Island Trail — Middlegrounds Metropark |
| T-0070–T-0071 (2) | OH-LUC-S-0016 | Cannonball Prairie Metropark |
| T-0077 | OH-LUC-S-0022 | Manhattan Marsh Buckeye Basin Loop — Manhattan Marsh Preserve Metropark |
| T-0079 | OH-LUC-S-0228 | Oak Savanna & Cactus Loop — Kitty Todd Nature Preserve (prickly pear cactus = Kitty Todd) |
| T-0082–T-0083 (2) | OH-LUC-S-0231 | Camp Miakonda trails |

### Trails MRQ'd (4)

| Trail | Reason |
|-------|--------|
| T-0011 WCT Connector | Likely MC-S-0024 or MC-T-0002 (WCT); route verification needed |
| T-0078 Anthony Wayne Trail | Linear corridor; no single natural area parent; verify route |
| T-0080 Salamander Flats Wetland Trail | "Salamander Flats" may be Swan Creek, Wiregrass, or other property — verify |
| T-0081 Sandhill Crane Wetland Viewing Area | Could be Maumee Bay SP (S-0003), Metzger Marsh (S-0007), or Metroparks property — verify |

---

## 4. Supplemental Sites (11 new, S-0234–S-0244)

All confirmed Lucas County (FIPS 095) via TIGER/Line 2024 Ohio COUSUB spatial audit (geopandas point-in-polygon). GPS from PAD-US 4.0 centroids.

| Site ID | Name | Acres | Governance | GPS | Township/Mun | GAP |
|---------|------|-------|------------|-----|--------------|-----|
| OH-LUC-S-0234 | Keil Farm | 165 | City of Toledo | 41.6426, -83.6595 | Toledo | 2 |
| OH-LUC-S-0235 | Devilbliss Boy Scout Reservation | 153 | Boy Scouts of America | 41.6947, -83.6795 | Sylvania Twp / Sylvania | 4 |
| OH-LUC-S-0236 | Lucas County Recreation Center | 108 | Lucas County | 41.5854, -83.6432 | Maumee | 4 |
| OH-LUC-S-0237 | International Park | 77 | City of Toledo | 41.6461, -83.5287 | Toledo | 4 |
| OH-LUC-S-0238 | Riverfront North | 63 | City of Toledo | 41.6818, -83.4892 | Toledo | 4 |
| OH-LUC-S-0239 | Rogers Park | 41 | City of Toledo | 41.6423, -83.6744 | Toledo | 4 |
| OH-LUC-S-0240 | Harroun Park | 28 | City of Sylvania | 41.7130, -83.6985 | Sylvania / Sylvania | 4 |
| OH-LUC-S-0241 | Jackman Park | 12 | City of Toledo | 41.7150, -83.5913 | Toledo | 4 |
| OH-LUC-S-0242 | Hawthorne Hills Park | 10 | City of Toledo | 41.6069, -83.6726 | Toledo | 2 |
| OH-LUC-S-0243 | Horseshoe Island | 10 | City of Toledo | 41.6094, -83.5883 | Toledo | 4 |
| OH-LUC-S-0244 | Imperial Woods Park | 2 | City of Toledo | 41.6908, -83.6456 | Toledo | 2 |

---

## 5. False Positives — QR Gaps Confirmed as Other Counties

The following QR-identified Lucas County gaps are in adjacent counties per TIGER spatial audit. Not inserted.

### Wood County (FIPS 173) — for future Wood County batch

| PAD-US Name | Acres | GAP | Governance | Location |
|-------------|-------|-----|------------|----------|
| WPA 44 | 64 | 2 | State/ODNR Wildlife Division | Lake Township, Wood County |
| Buttonwood/Betty C. Black | 24 | 4 | City/Perrysburg | Perrysburg, Wood County |
| Cedar Creeks Preserve | 39 | 2 | County | Lake Township, Wood County |
| Orleans Park | 34 | 4 | City/Perrysburg | Perrysburg, Wood County |
| Rivercrest Park | 34 | 4 | City/Perrysburg | Perrysburg, Wood County |
| Woodlands Park | 42 | 4 | City/Perrysburg | Perrysburg, Wood County |

All 6 MRQ-flagged as `LUC-QR-FALSEPOS-WOOD` for Wood County discovery/pipeline.

---

## 6. Howard Farms Identity Resolution

**Howard Farms Land Acquisition** (987ac, County Land, GAP2, lat=41.6482, lon=-83.2659) from PAD-US is the **same entity as OH-MC-S-0021 Howard Marsh Metropark** (lat=41.6465, lon=-83.2613, 1000ac, Lucas;Ottawa). Coordinate delta: 0.002° lat, 0.005° lon — within PAD-US centroid rounding. PAD-US uses the pre-development acquisition name; DB record uses current branded park name. No insert needed. MRQ logged for documentation.

---

## 7. MRQ Entries (10 total)

| Record ID | Entity Type | Issue |
|-----------|-------------|-------|
| OH-LUC-T-0011 | Trail | WCT Connector — parent unclear, route verification needed |
| OH-LUC-T-0078 | Trail | Anthony Wayne Trail — linear corridor, no natural area parent identified |
| OH-LUC-T-0080 | Trail | Salamander Flats — parent property ambiguous |
| OH-LUC-T-0081 | Trail | Sandhill Crane Viewing — parent property ambiguous |
| LUC-QR-FALSEPOS-WOOD | Site (batch) | 6 Wood County entities in QR gap list — stage for Wood County run |
| LUC-HOWARDFARMS-ID | Site | Howard Farms = MC-S-0021 (documentation only) |
| OH-LUC-S-0234 | Site | Keil Farm — public access "Unknown" per PAD-US; verify before finalizing |
| LUC-F-07 | Access Point | Grand Rapids AP — may be Wood County; verify attribution |
| LUC-F-09 | Access Point | Lucas County Recreation Ramp — identity vs S-0190 unclear |
| (open flags from handoff) | — | LUC-F-03/04/05/11/12/13: pre-existing QR open items, not modified |

---

## 8. Final Counts

| Entity Type | Before | After |
|-------------|--------|-------|
| Sites (LUC) | 225 | 236 |
| Site Networks (LUC) | 0 | 3 |
| Trail Parents (LUC) | 7 | 55 |
| MC Trail Segments | 3 | 4 |

---

## 9. Not Actioned This Session

- `LUC_access_points.tsv` — no new APs inserted; AP pipeline not run for this batch
- Held entities (held from original pipeline): no change; GPS acquisition pass needed
- Open flags LUC-F-03, F-04, F-05, F-11, F-12, F-13 — pre-existing; carry forward
