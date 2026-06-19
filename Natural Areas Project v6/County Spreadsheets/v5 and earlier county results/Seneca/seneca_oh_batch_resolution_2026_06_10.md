# Seneca County — Batch Resolution Log
**Date:** 2026-06-10
**Run ID:** `BATCH_SEN_2026-06-10`
**Source:** Quality review 2026-06-08; QR status: PARTIAL FAIL

---

## 1. Franklin County Cemeteries Deleted from held_entities (5 records)

OH-SEN-S-0029 through S-0033 (Chenoweth, Gundy, Ebenezer M.E., Little Pennsylvania, Oak Grove cemeteries) were Pleasant Township, Franklin County entities erroneously staged as Seneca County during the pipeline run. All 5 deleted from Seneca `held_entities`.

**Next action:** Stage for Franklin County supplemental T8 discovery when Franklin County runs.

---

## 2. Trail Parent Added (1 entry)

| Trail | Parent Site | Note |
|-------|-------------|------|
| OH-SEN-T-0002 Rock Creek Trail | OH-SEN-S-0034 Hedges-Boyer Park | Trail runs through park's 78ac corridor along Rock Creek |

---

## 3. Supplemental T2 WPA Sites (3 new sites, S-0143–S-0145)

| Site ID | Name | Acres | Township | GPS | Note |
|---------|------|-------|----------|-----|------|
| OH-SEN-S-0143 | ODNR Wildlife Production Area 61 | 40 | Seneca Twp | 41.009666, -83.217094 | Confirmed Seneca County |
| OH-SEN-S-0144 | ODNR Wildlife Production Area 64 | 49 | Liberty Twp | 41.251535, -83.257413 | Liberty Twp = Seneca County; also appeared in Sandusky bbox |
| OH-SEN-S-0145 | ODNR Wildlife Production Area 18 | 50 | Jackson Twp | 41.335649, -83.254806 | Jackson Twp = Seneca County; also appeared in Sandusky bbox |

**WPA cross-county resolution:**
- WPA 62 (70ac): Sandusky County (Pleasant Twp) — already OH-SAN-S-0149. NOT a Seneca gap.
- WPA 14 (40ac): Sandusky County (Scott Twp) — already OH-SAN-S-0147. NOT a Seneca gap.
- WPA 31 (75ac): Sandusky County (Green Creek Twp) — already OH-SAN-S-0153.
- WPA 47 (40ac): Sandusky County (Pleasant Twp) — already OH-SAN-S-0150.
- WPA 50 (48ac): Sandusky County (Scott Twp) — already OH-SAN-S-0146.

**Green Springs State Forest:** Township lookup (Ballville Twp) = Sandusky County primary. Already inserted as OH-SAN-S-0144. NOT a Seneca gap. MRQ note added to verify whether any Seneca-side parcels exist separately.

---

## 4. Paradiso Athletic Complex (S-0146)

82ac facility at 41.119141, -83.215513, Hopewell Township, Seneca County. PAD-US owner = "Other or Unknown State Land." Governance unverified — possibly Heidelberg University (T2) or Seneca County (T4). Added to MRQ for governance verification.

---

## 5. Supplemental T6 Parks (7 new sites, S-0147–S-0153)

| Site ID | Name | Acres | Municipality | GPS |
|---------|------|-------|--------------|-----|
| OH-SEN-S-0147 | Apple-Jack Park | 3 | Tiffin | 41.123863, -83.182079 |
| OH-SEN-S-0148 | Don Elchert Field | 5 | Fostoria | 41.155045, -83.406025 |
| OH-SEN-S-0149 | Fostoria Rail Park | 5 | Fostoria | 41.152985, -83.407406 |
| OH-SEN-S-0150 | Historical District Park | 0 | Fostoria | 41.158241, -83.405578 |
| OH-SEN-S-0151 | Legion Park | 11 | Tiffin | 41.108791, -83.186163 |
| OH-SEN-S-0152 | Risdon Square | 1 | Fostoria | 41.166102, -83.417746 |
| OH-SEN-S-0153 | Tiffin Baseball Field | 2 | Tiffin | 41.112897, -83.160840 |

S-0150 acreage = 0 in PAD-US (data gap).

---

## 6. Open Items

- Paradiso Athletic Complex (S-0146): governance and tier verification — MRQ
- Reformed Cemetery [2] (S-0086): shared GPS with S-0085 — MRQ
- Rock Creek Cemetery [2] (S-0134): shared GPS with S-0133 — MRQ
- OH-SEN-T-0001 entity type conflict (Trail vs OH-SAN-S-0005 Site) — resolve in Wyandot County run — MRQ
- Green Springs SF Seneca-side parcel check — MRQ
- WPA 62 / WPA 14 / WPA 31 / WPA 47 / WPA 50 confirmed Sandusky County — no Seneca action needed
- OH-SEN-T-0001 (Sandusky SSR) remains in held_entities (cross_county_held, Wyandot primary) — valid hold
- 5 Franklin County cemeteries: deleted from Seneca held, stage for Franklin County T8 when that county runs
- Acreage discrepancies (Foundation Park, Garlo Heritage, Meadowbrook, Zimmerman) — still open; verify against source documents
