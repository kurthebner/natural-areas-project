# Ottawa County — Batch Resolution Log
**Date:** 2026-06-10
**Run ID:** `BATCH_HEN_OTT_WAY_2026-06-10`
**Source:** Quality review 2026-06-08; QR status: FAIL

---

## 1. AP-0006 Parent Assignment

**OH-OTT-AP-0006** (West Harbor Boat Launch) had null `parent_entity_id`.
Updated: `parent_entity_id='OH-OTT-S-0003'`, `parent_entity_type='Site'`
(Ottawa NWR — West Harbor Landing)

---

## 2. Trail Parents Added (9 entries)

| Trail | Parent Site |
|-------|-------------|
| OH-OTT-T-0072 | OH-MC-S-0021 (Howard Marsh Metropark) |
| OH-OTT-T-0073 | OH-MC-S-0021 |
| OH-OTT-T-0074 | OH-MC-S-0021 |
| OH-OTT-T-0075 | OH-MC-S-0021 |
| OH-OTT-T-0076 | OH-MC-S-0021 |
| OH-OTT-T-0126 | OH-OTT-S-0012 (Catawba Island SP) |
| OH-OTT-T-0127 | OH-OTT-S-0042 (Cedar Meadow Preserve) |
| OH-OTT-T-0128 | OH-OTT-S-0046 (Meadowbrook Marsh) |
| OH-OTT-T-0129 | OH-OTT-S-0079 (Veterans Memorial Park, Salem Twp) |

---

## 3. Data Fix — S-0016 Honey Point WA

Updated `acres=8.0` on OH-OTT-S-0016 (Honey Point Wildlife Area). PAD-US: 8ac, Put-in-Bay
Township, Ottawa County (FIPS 123). Confirmed Ottawa County. Distinct entity from Willow Point
WA (391+42ac) which is Erie County (see §5 below).

---

## 4. Supplemental Sites (5 new, S-0134–S-0138)

| Site ID | Name | Acres | Township | GPS |
|---------|------|-------|----------|-----|
| OH-OTT-S-0134 | Southwestern Lake Erie Marshes and Islands | 153 | Danbury | 41.543414, -82.825637 |
| OH-OTT-S-0135 | Wildlife Production Area 65 | 31 | Salem | 41.476255, -83.092367 |
| OH-OTT-S-0136 | Port Clinton Waterfront | 15 | — | 41.514273, -82.931414 |
| OH-OTT-S-0137 | Portage River Fishing Access | 10 | Erie | 41.519965, -82.971085 |
| OH-OTT-S-0138 | Genoa Recreation Complex | 39 | Clay | 41.518808, -83.354826 |

**Notes:**
- S-0134: TNC conservation area, GAP1. Danbury Township confirmed Ottawa via TIGER.
- S-0135: ODNR WPA, GAP2. Salem Township confirmed Ottawa (FIPS 123).
- S-0136: ODNR waterfront, GAP4. Port Clinton (Ottawa County seat). Township null (city).
- S-0137: ODNR fishing access, GAP4. Erie Township confirmed Ottawa.
- S-0138: City of Genoa, GAP4. Clay Township confirmed Ottawa (Genoa is in Ottawa County).
  Note: S-0083 "Genoa Quarry" is a distinct Ottawa entity.

---

## 5. QR Gap Analysis — False Positives (Neighboring County Attribution)

This county had the largest number of cross-county false positives in the batch.
All confirmed via TIGER FIPS spatial audit.

| QR Gap | Claimed County | Actual County | TIGER MCD |
|--------|---------------|---------------|-----------|
| Resthaven Wildlife Area 2151+65ac | Ottawa | **Erie (043)** | Margaretta |
| Willow Point WA 391+42ac | Ottawa | **Erie (043)** | Margaretta/Townsend |
| Bayview West Marsh 221ac | Ottawa | **Erie (043)** | Margaretta |
| Howard Farms Land Acquisition 987ac | Ottawa | **Lucas (095)** | Jerusalem |
| Decoy Marsh Acquisition 69ac | Ottawa | **Sandusky (143)** | Riley |
| WPA 30 56ac | Ottawa | **Sandusky (143)** | Sandusky Twp |
| WPA 59 48ac | Ottawa | **Sandusky (143)** | Washington Twp |
| WPA 63 40ac | Ottawa | **Sandusky (143)** | Riley |
| Millers Blue Hole WA 13ac | Ottawa | **Sandusky (143)** | Townsend |
| Darr-Root Fishing Access 34ac | Ottawa | **Sandusky (143)** | Fremont |
| Alumni Park 12ac | Ottawa | **Sandusky (143)** | Fremont |
| Birchard Park 12ac | Ottawa | **Sandusky (143)** | Fremont |
| Firemans Park 5ac | Ottawa | **Wood (173)** | Lake Twp |

The Fremont-attributed parks (Darr-Root, Alumni, Birchard) are in Fremont, Ohio — county seat
of Sandusky County, not Ottawa. The "Southwestern Lake Erie Marshes" (153ac Danbury/Ottawa) is
the Ottawa-confirmed portion of a larger conservation complex; the Bayview and other parcels in
that complex fall in Erie County.

---

## 6. MRQ Entries (4)

1. Resthaven WA → Erie County; stage for Erie County T2 run (2151+65ac ODNR GAP2)
2. Willow Point WA → Erie County entity; S-0016 Honey Point WA confirmed Ottawa (8ac, Put-in-Bay)
3. Howard Farms → Lucas County; not related to MC-S-0021 Howard Marsh Metropark
4. Sandusky County parks cluster → stage Alumni Park, Birchard Park, Darr-Root FA,
   WPA 30/59/63, Millers Blue Hole, Decoy Marsh, Firemans Park for Sandusky/Erie/Wood runs

---

## 7. Final Counts

| Entity Type | Before | After |
|---|---|---|
| Sites (OTT) | 133 | 138 |
| Trail parents (OTT) | 47 | 56 |
| APs with parent | 8/9 | 9/9 |

---

## 8. Open Items

- T-0072–T-0076: verify trail names vs Howard Marsh Metropark trail inventory
- Resthaven WA (2151+65ac, ODNR, Erie Co): major entity for Erie County run
- WPA 44 (64ac, Erie Twp, Ottawa Co, lat=41.525, lon=-83.504): not in QR but PAD-US shows
  it in Ottawa County — investigate for next Ottawa pass
- S-0134 Southwestern Lake Erie Marshes: governance confirm (TNC vs USFWS vs other NGO)
