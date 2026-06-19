# Scioto County — Batch Resolution Log
**Date:** 2026-06-10
**Run ID:** `BATCH_SCI_2026-06-10`
**Source:** Quality review 2026-06-08; QR status: PARTIAL FAIL

---

## 1. Trail Parent Added (1 entry)

| Trail | Parent Site | Note |
|-------|-------------|------|
| OH-MC-T-0006 Shawnee Backpack Trail | OH-MC-S-0002 Shawnee State Forest | Missing per QR §5; trail traverses the state forest |

---

## 2. Supplemental T7 Sites (5 new sites, S-0048–S-0052)

### Glade Wetland (3 parcels, ~292ac total, GAP1)

| Site ID | Name | Acres | Township | GPS |
|---------|------|-------|----------|-----|
| OH-SC-S-0048 | Glade Wetland Fee (Parcel A) | 215 | Marion Twp | 39.014741, -82.803850 |
| OH-SC-S-0049 | Glade Wetland Fee (Parcel B) | 71 | Scioto Twp | 39.013633, -82.790176 |
| OH-SC-S-0050 | Glade Wetland | 6 | Scioto Twp | 39.015321, -82.790857 |

**S-0048 county flag:** Township lookup returned Marion Township. Scioto County has no Marion Township — this may be Pike County. Added to MRQ for county verification. The 71ac and 6ac parcels are confirmed Scioto Township, Scioto County.

### Other T7

| Site ID | Name | Acres | Township | GPS |
|---------|------|-------|----------|-----|
| OH-SC-S-0051 | Molly Lauman Girl Scout Camp | 19 | Morgan Twp | 38.927978, -83.063230 |
| OH-SC-S-0052 | Unknown NGO Park (Scioto County) | 5 | Valley Twp | 38.873883, -82.999668 |

S-0052 name unknown in PAD-US; added to MRQ for name/org verification.

---

## 3. Supplemental T6 Sites (3 new sites, S-0053–S-0055)

| Site ID | Name | Acres | Municipality/Township | GPS |
|---------|------|-------|-----------------------|-----|
| OH-SC-S-0053 | Branch Rickey Park | 0 | Portsmouth | 38.727074, -82.974337 |
| OH-SC-S-0054 | Village Square Park | 1 | New Boston | 38.748320, -82.942899 |
| OH-SC-S-0055 | Washington Township Park | 6 | Washington Twp | 38.762111, -83.029840 |

S-0053 acreage = 0 in PAD-US (data gap); small Portsmouth city park.
S-0055 was previously wrong-matched to Clay Township Park (QR §7a); inserted as distinct entity.

---

## 4. Bbox False Positives (Not Scioto Gaps)

- **Arc of Appalachia Biodiversity (317ac, Franklin Twp):** Franklin Township = Adams County, NOT Scioto. Added to MRQ.
- **Unknown Ball Park (3ac, Seal Twp):** Seal Township = Pike County, NOT Scioto. Added to MRQ.

---

## 5. Open Items

- Glade Wetland Fee Parcel A (S-0048): county verify — may be Pike County — MRQ
- Unknown NGO Park (S-0052): verify name and org — MRQ
- AP-0004 Burkes Point Boat Ramp: GOVERNANCE_UNCERTAIN, no parent — MRQ
- Shawnee State Park acreage (DB 1,095ac vs PAD-US 2,045ac) — MRQ
- Horseshoe Mound (S-0026) precision GPS — MRQ
- Arc of Appalachia Biodiversity (317ac): confirmed Adams County, not Scioto — MRQ for Adams run
- If Arc of Appalachia Biodiversity is confirmed Scioto: add to OH-SC-SN-0001 as 5th member
