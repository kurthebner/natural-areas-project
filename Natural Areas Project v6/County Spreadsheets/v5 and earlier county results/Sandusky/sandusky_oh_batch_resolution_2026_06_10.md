# Sandusky County — Batch Resolution Log
**Date:** 2026-06-10
**Run ID:** `BATCH_SAN_2026-06-10`
**Source:** Quality review 2026-06-08; QR status: FAIL

---

## 1. Trail Parents Added (2 entries)

| Trail | Parent Site | Note |
|-------|-------------|------|
| OH-SAN-T-0004 Silver Rock Park Walking Trail | OH-SAN-S-0093 Silver Rock Park | Missing trail_parent per QR §6 |
| OH-MC-T-0110 North Coast Inland Trail | OH-SAN-S-0021 Tea Kaufman Homestead | Missing NCIT trail_parent per QR §6 |

**Mosser Park note:** AP-0005 (North Coast Inland Trail - Mosser Park Access) references T-0110 as parent but no Mosser Park site record exists in DB. Could not add trail_parent for Mosser Park. If Mosser Park is inserted in a future discovery pass, add trail_parent T-0110 → Mosser Park site.

---

## 2. Acreage Updates (3 sites)

| Site ID | Name | Old Acres | New Acres | Source |
|---------|------|-----------|-----------|--------|
| OH-SAN-S-0002 | Pickerel Creek Wildlife Area | NULL | 3,148ac | PAD-US 4.0 GDB |
| OH-SAN-S-0009 | Blue Heron Reserve | NULL | 158ac | PAD-US 4.0 GDB |
| OH-SAN-S-0029 | Conner Park | NULL | 18ac | PAD-US 4.0 GDB |

---

## 3. MRQ — Acreage Discrepancies / Verification Needed

| Entity | Issue |
|--------|-------|
| OH-SAN-S-0001 Spiegel Grove SP | No DB acreage. PAD-US record named "Park" shows 765ac. Verify actual Spiegel Grove SP acreage from ODNR. |
| OH-SAN-S-0023 White Star Park | DB=797ac vs PAD-US=666ac. Verify current official acreage. |

---

## 4. Sugar Creek Golf Course — Released from Held (S-0105)

**QR §4:** Held as `cross_county_held`, Ottawa County primary (Scenario A). Ottawa pipeline ran 2026-06-10 and did NOT catalog this entity.

**Resolution:** Township lookup on PAD-US centroid (41.469923, -83.282706) → Harris Township, Sandusky County. Entity is Sandusky County primary.

- Removed OH-SAN-S-0105 from `held_entities`
- Inserted OH-SAN-S-0105 as active Site: Sugar Creek Golf Course & Driving Range
  - Category: Recreation / Golf Course | 103ac (PAD-US) | GPS: 41.469923, -83.282706
  - Ownership: Private | Governance: Private | Township: Harris

---

## 5. Supplemental T2 Sites (11 new sites, S-0143–S-0153)

### Knobbys Prairie WA, Green Springs SF, Abbotts Bridge SR

| Site ID | Name | Acres | Township | GPS |
|---------|------|-------|----------|-----|
| OH-SAN-S-0143 | Knobbys Prairie Wildlife Area | 48 | Pleasant | 41.199363, -83.117147 |
| OH-SAN-S-0144 | Green Springs State Forest | 120 | Ballville | 41.258396, -83.075751 |
| OH-SAN-S-0145 | Sandusky Abbotts Bridge State Scenic River | 22 | Pleasant | 41.210754, -83.154240 |

### WPAs (8 of 12 confirmed Sandusky County by township lookup)

| Site ID | Name | Acres | Township | GPS |
|---------|------|-------|----------|-----|
| OH-SAN-S-0146 | ODNR Wildlife Production Area 50 | 48 | Scott | 41.288516, -83.376556 |
| OH-SAN-S-0147 | ODNR Wildlife Production Area 14 | 40 | Scott | 41.317850, -83.304243 |
| OH-SAN-S-0148 | ODNR Wildlife Production Area 59 | 48 | Washington | 41.380359, -83.239557 |
| OH-SAN-S-0149 | ODNR Wildlife Production Area 62 | 70 | Pleasant | 41.205881, -83.095732 |
| OH-SAN-S-0150 | ODNR Wildlife Production Area 47 | 40 | Pleasant | 41.229151, -83.076171 |
| OH-SAN-S-0151 | ODNR Wildlife Production Area 30 | 56 | Sandusky | 41.395302, -83.070625 |
| OH-SAN-S-0152 | ODNR Wildlife Production Area 63 | 40 | Riley | 41.411922, -83.037620 |
| OH-SAN-S-0153 | ODNR Wildlife Production Area 31 | 75 | Green Creek | 41.263645, -83.033597 |

**WPA catch-all (S-0008):** Replaced by S-0143 through S-0153. S-0008 should be deprecated in a future cleanup pass once all individual WPAs are confirmed.

**WPA bbox false positives excluded (4 of 12):**
- WPA 64 (Liberty Twp) → Seneca County
- WPA 18 (Jackson Twp) → Seneca County
- WPA 65 (Salem Twp) → Ottawa County
- WPA typo (Bay Twp) → Erie County

All 4 added to MRQ as bbox false positives.

---

## 6. Supplemental T6 Sites (9 new sites, S-0154–S-0162)

All confirmed Sandusky County via township lookup.

| Site ID | Name | Acres | Municipality/Township | GPS |
|---------|------|-------|-----------------------|-----|
| OH-SAN-S-0154 | Alumni Park | 12 | Fremont | 41.366059, -83.121815 |
| OH-SAN-S-0155 | Harmon Field | 4 | Fremont | 41.357098, -83.123046 |
| OH-SAN-S-0156 | Limerick Park | 14 | Clyde | 41.286476, -82.979568 |
| OH-SAN-S-0157 | Triangle Park | 1 | Fremont | 41.344169, -83.123099 |
| OH-SAN-S-0158 | Fremont Community Recreation Complex | 27 | Fremont | 41.335129, -83.096239 |
| OH-SAN-S-0159 | Portage Trail Park | 17 | Ballville Twp | 41.322265, -83.152230 |
| OH-SAN-S-0160 | Veteran's Memorial Park | 20 | Salem Twp | 41.509851, -83.134201 |
| OH-SAN-S-0161 | Countryside Park | 5 | Fremont | 41.360395, -83.083916 |
| OH-SAN-S-0162 | Stephenson Park | 1 | Fremont | 41.346826, -83.116756 |

**Portage Park excluded:** Both PAD-US records excluded — 12ac record is Port Clinton (Ottawa County); 23ac record at 41.175251,-83.426962 is Perry Township = Seneca County.

**Bradner Preserve excluded:** QR listed as Sandusky T3 gap, but PAD-US centroid (41.321666,-83.420227) is Montgomery Township = Wood County. Bbox bleed. Added to MRQ.

---

## 7. Confirmed Bbox False Positives (Not Sandusky Gaps)

Added to manual_review_queue with county attribution notes:
- Little Portage WA (358ac) → Bay Township = Erie County
- Bradner Preserve (124ac) → Montgomery Township = Wood County
- Portage River Fishing Access (10ac) → Erie Township = Erie County
- Lover's Portage River Access (1ac) → Freedom Township = not Sandusky
- WPA 64 (49ac) → Liberty Township = Seneca County
- WPA 18 (50ac) → Jackson Township = Seneca County
- WPA 65 (31ac) → Salem Township = Ottawa County
- Portage Park 23ac → Perry Township = Seneca County

---

## 8. Open Items

- Spiegel Grove SP acreage — MRQ
- White Star Park acreage discrepancy (797 vs 666ac) — MRQ
- Mosser Park site not in DB — AP-0005 NCIT access has no site parent; insert when discovered
- WPA catch-all S-0008 — deprecated in practice; formal deletion deferred
- S-0079/0080/0081, S-0107 sequence gaps — document in session log; likely Bellevue reclassification (QR §3)
- Portage Trail Park (S-0159) NCIT trail_parent — needs route map verification
- Veteran's Memorial Park (S-0160) — verify distinct from S-0096 Veterans Park (Clyde)
