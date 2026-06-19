# Hancock County — Batch Resolution Log
**Date:** 2026-06-10
**Run ID:** `BATCH_HAN_2026-06-10`
**Source:** Quality review 2026-06-08; QR status: FAIL (partial upsert + PAD-US gaps)

---

## 1. Supplemental T4 — County Conservation Land (2 new sites, S-0167–S-0168)

| Site ID | Name | Acres | GAP | Township | GPS |
|---------|------|-------|-----|----------|-----|
| OH-HAN-S-0167 | Sponsler Property Acquisition - Cricket Frog Cove | 156 | GAP2 | Henry Twp | 41.237317, -83.683578 |
| OH-HAN-S-0168 | Rudolph-Savanna Preserve | 52 | GAP2 | Liberty Twp | 41.303174, -83.665726 |

Both confirmed Hancock County via centroid + township lookup.

---

## 2. Supplemental T2 — ODNR Sites (11 new sites, S-0169–S-0179)

| Site ID | Name | Acres | Township | GPS |
|---------|------|-------|----------|-----|
| OH-HAN-S-0169 | District 2 - Findlay Wildlife Area | 6 | — / Findlay | 41.025270, -83.666214 |
| OH-HAN-S-0170 | ODNR Wildlife Production Area 6 | 77 | Portage Twp | 41.307567, -83.623573 |
| OH-HAN-S-0171 | ODNR Wildlife Production Area 8 | 73 | Portage Twp | 41.264872, -83.643031 |
| OH-HAN-S-0172 | ODNR Wildlife Production Area 9 | 57 | Allen Twp | 41.158052, -83.615715 |
| OH-HAN-S-0173 | ODNR Wildlife Production Area 11 | 72 | Jackson Twp* | 41.249601, -83.799506 |
| OH-HAN-S-0174 | ODNR Wildlife Production Area 20 | 72 | Bloom Twp* | 41.171015, -83.599772 |
| OH-HAN-S-0175 | ODNR Wildlife Production Area 21 | 39 | Milton Twp* | 41.339213, -83.872357 |
| OH-HAN-S-0176 | ODNR Wildlife Production Area 41 | 53 | Liberty Twp | 41.045963, -83.701415 |
| OH-HAN-S-0177 | ODNR Wildlife Production Area 42 | 39 | Henry Twp* | 41.231785, -83.714912 |
| OH-HAN-S-0178 | ODNR Wildlife Production Area 46 | 40 | Blanchard Twp | 41.056506, -83.863935 |
| OH-HAN-S-0179 | ODNR Wildlife Production Area 58 | 40 | Jackson Twp* | 41.176424, -83.817926 |

\* Township name not in canonical Hancock County township list — county attribution MRQ-flagged (possible Wood County bleed for WPAs 11, 20, 21, 42, 58). County attribution per Hancock PAD-US spatial audit QR 2026-06-08.

---

## 3. Supplemental T6 — Small Parks (3 new sites, S-0180–S-0182)

| Site ID | Name | Acres | Municipality | GPS |
|---------|------|-------|--------------|-----|
| OH-HAN-S-0180 | Anchor Park | 5 | Findlay | 41.040360, -83.645848 |
| OH-HAN-S-0181 | Douglas Park | 1 | Findlay | 41.023804, -83.652125 |
| OH-HAN-S-0182 | Civitan Park | 2 | Findlay | 41.041890, -83.647728 |

Note: PAD-US also has Civitan Park (33ac City) at 39.27N (Washington County) and Douglas Park (14ac City) at 39.50N (SW Ohio) — both confirmed as different entities from the Hancock parks above.

---

## 4. Trail Segments Upserted from TSV (35 records, TS-0001–TS-0035)

Previously in `hancock_ohio_2026_05_12_trail_segments.tsv` but never upserted to DB.

**Van Buren State Park hiking segments (TS-0001–TS-0009) → parent OH-HAN-T-0001:**
Green, Blue, Orange, Haiku, Sensory, Pink, Red, White, Yellow

**Van Buren State Park MTB segments (TS-0010–TS-0016) → parent OH-HAN-T-0002:**
Green, Blue, Red, Pink, White, Yellow, Purple

**Van Buren State Park bridle segments (TS-0017–TS-0019) → parent OH-HAN-T-0003:**
Campground Connector, Day Use Connector, Cable Line Road Trail

**Heritage Trail named segments (TS-0020–TS-0035) → parent OH-HAN-T-0004:**
Segment 1 through Segment 16

---

## 5. Site Network Upserted from TSV (OH-HAN-SN-0001)

Previously in `hancock_ohio_2026_05_12_site_networks.tsv` but never upserted to DB.

**OH-HAN-SN-0001: Flag City Sports Complex**
- 10 member sites: OH-HAN-S-0055/0056/0057/0059/0060/0062/0065/0066/0067/0069
- Member IDs corrected from 3-digit format (S-055) to 4-digit (S-0055) at upsert

---

## 6. Trail Parents Added (15 entries)

| Trail | Parent Site | Note |
|-------|-------------|------|
| OH-HAN-T-0001 Van Buren Hiking | OH-HAN-S-0001 Van Buren State Park | |
| OH-HAN-T-0002 Van Buren MTB | OH-HAN-S-0001 | |
| OH-HAN-T-0003 Van Buren Bridle | OH-HAN-S-0001 | |
| OH-HAN-T-0004 Heritage Trail | OH-HAN-S-0018 Riverbend Recreation Area | Rail trail starting at Riverbend |
| OH-HAN-T-0006 Blanchard River Greenway | OH-HAN-S-0018 Riverbend Recreation Area | |
| OH-HAN-T-0013 Emory Adams Park Path W | OH-HAN-S-0053 Emory Adams Park | |
| OH-HAN-T-0014 Emory Adams Park Path E | OH-HAN-S-0053 Emory Adams Park | |
| OH-HAN-T-0015 Flag City Sports Complex Path | OH-HAN-S-0055 Flag City Sports Complex | |
| OH-HAN-T-0016 Lake Daugherty Walking Trail | OH-HAN-S-0080 Lake Daugherty (Reservoir 1) | |
| OH-HAN-T-0017 Lake Mottram Walking Trail | OH-HAN-S-0081 Lake Mottram (Reservoir 2) | |
| OH-HAN-T-0018 Lake Lamberjack Walking Trail | OH-HAN-S-0082 Lake Lamberjack (Reservoir 3) | |
| OH-HAN-T-0019 Lake Mosier Walking Trail | OH-HAN-S-0083 Lake Mosier (Reservoir 4) | |
| OH-HAN-T-0020 Lake LeComte Walking Trail | OH-HAN-S-0084 Lake LeComte (Reservoir 5) | |
| OH-HAN-T-0021 Veterans Memorial Reservoir Walking Trail | OH-HAN-S-0085 Veterans Memorial Reservoir | |
| OH-HAN-T-0022 Benton Ridge Community Park Walking Track | OH-HAN-S-0089 Benton Ridge Community Park | |

**10 trails without confirmable trail_parents (MRQ-flagged):**
T-0005 (Blanchard River Water Trail, no single parent expected), T-0007 (Riverwalk), T-0008 (Highline Trail), T-0009 (Upland Trail), T-0010 (Ladybug Loop), T-0011 (Backwoods Trail), T-0012 (Old Mill Stream Scenic Byway — cross-county, no parent), T-0023 (Bluffton Bicycle Pathway — cross-county), T-0024 (Findlay Reservoir Dike Trail), T-0025 (McComb Reservoir Walk Trail).

---

## 7. MRQ Entries (15 total)

County attribution flags: S-0173, S-0174, S-0175, S-0177, S-0179 (Jackson/Bloom/Milton/Henry townships not confirmed Hancock).
GPS flags: AP-0005 through AP-0010 (WA parking areas, null GPS).
Data quality: S-0021 acreage discrepancy (27.3ac vs PAD-US 81ac).
Trail parents: T-0005/0007-0012/0023-0025 without confirmed parents.
Identity: T-0012 Old Mill Stream Scenic Byway (possible driving byway misclassified as trail).
Pipeline: LOCAL-006 speculative entries (7 records to review).

---

## 8. Final Counts

| Entity Type | Before | After |
|---|---|---|
| Sites | 159 | 175 |
| Trail Segments | 0 | 35 |
| Site Networks | 0 | 1 |
| Trail Parents | 0 | 15 |
| Access Points | 19 | 19 (AP-0005–0010 GPS still null) |

---

## 9. Open Items

- WPAs 11/20/21/42/58: county attribution uncertain (Jackson/Bloom/Milton/Henry twps) — verify against Wood County run
- AP-0005–AP-0010: GPS acquisition for WA parking areas
- Indian Green-Worden CA: acreage discrepancy 27.3ac vs PAD-US 81ac
- 10 trails missing trail_parents (T-0005/0007-0012/0023-0025)
- T-0012 Old Mill Stream Scenic Byway: reclassify or confirm as trail
- LOCAL-006 speculative entries: review and retire or confirm
