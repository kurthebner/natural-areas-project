# Normalization Engine v5.5 — Wayne County, Ohio
**Date:** 2026-03-08  
**Input:** Resolution Pass 1 output — 79 resolved records  
**Output:** 73 normalized | 6 held | 0 rejected  
**Status: COMPLETE**

---

## Summary

| Outcome | Count |
|---------|-------|
| Normalized (ready for TSV output) | 73 |
| Held (incomplete or cross-county) | 6 |
| Rejected (fatal validation errors) | 0 |
| **Input total** | **79** |

---

## Normalizations Applied

**GPS validation:** All 79 records passed Ohio range check (lat 39.0–42.5°N, lon 80.0–85.0°W). All GPS values rounded to 6 decimal places.

**Plus Code computation:** All 73 normalized records received a 10-character Open Location Code (OLC). Wayne County codes fall in the `8MGV` / `8MGW` prefix range, consistent with northeastern Ohio.

**County normalization:** `county_primary` values "Wayne" and "Wayne County" both normalized to `Wayne` (stripped "County" suffix per spec).

**Flag N-001 — T3-002 Koehler's Pond:** Routing decision: **keep as Site.** Koehler's Pond is a named wetland destination within Barnes Preserve with an accessible observation deck and documented ecological interest. It is a destination feature, not an entry/exit point — `Site` (natural feature subtype) is correct. Parent: T3-001 Barnes Preserve.

**Flag N-002 — T5-002 Chippewa trails:** Routed to **held** (identity_uncertain). Source describes "several short hiking trails" with no named trails confirmed. Held pending field verification.

**Flag N-003 — T2-007 Killbuck Obs. Trail:** Routed to **held** (identity_uncertain). Trail existence inferred from multi-source descriptions but not confirmed by ODNR trail inventory. Held pending field verification.

---

## Held Entities

| Record ID | Name | Entity Type | Hold Reason |
|-----------|------|-------------|-------------|
| T2-004 | Killbuck Marsh Wildlife Area | Site | multi_county — Holmes County not yet processed |
| T2-007 | Killbuck Marsh Wildlife Obs. Trail | Trail | identity_uncertain — trail existence unconfirmed |
| T2-012 | Funk Bottoms Wildlife Area | Site | multi_county — Ashland County not yet processed |
| T5-002 | Chippewa Twp Nature Preserve trails | Trail | identity_uncertain — trail count/names unconfirmed |
| T7-002 | Sippo Valley Trail | Trail | multi_county — Stark County not yet processed |
| T7-004 | Holmes County Trail | Trail | multi_county — Holmes County not yet processed |

Multi-county held entities will be released when the partner county is processed. Identity-uncertain held entities will be released when field verification confirms trail existence and count.

---

## Normalized Records by Entity Type

| Entity Type | Count |
|-------------|-------|
| Site | 44 |
| Access Point | 17 |
| Trail | 11 |
| Trail Network | 1 |
| **Total** | **73** |

---

## Normalized Records by Tier

| Tier | Count | Notes |
|------|-------|-------|
| 2 (State) | 9 | Includes Brown's Lake Bog SNP, Johnson Woods SNP, Shreve Lake WA; Killbuck Marsh and Funk Bottoms held |
| 3 (District) | 4 | Barnes Preserve + Koehler's Pond + Casey's Trails + access point |
| 5 (Township) | 2 | Chippewa Twp Nature Preserve (site + access point); trail held |
| 6 (Municipal) | 44 | All municipal parks and trails across Wooster, Orrville, Rittman, and villages |
| 7 (Conservancy) | 9 | County Line Trail, Heartland Trail + access points; Sippo Valley and Holmes County held |
| 8 (Private) | 5 | Secrest Arboretum, Vulture's Knob + trails and access points |

---

## GPS Status in Normalized Output

| Status | Count |
|--------|-------|
| GPS-CONFIRMED (Maps listing or satellite) | 71 |
| GPS-APPROXIMATE (area coordinate or intersection geocode) | 2 |

GPS-APPROXIMATE records: T6-024 (E.J. Young Grand View Park, Rittman) and T6-025 (Washington Street Park, Rittman) — no Maps listing available; coordinates are intersection geocodes. These will pass to TSV output with appropriate flags.

---

## Governance Distribution (Normalized Records)

| Governing Body | Records |
|----------------|---------|
| Villages (various — Apple Creek, Burbank, Creston, Doylestown, Fredericksburg, Marshallville, Mt Eaton, Shreve, Smithville, West Salem) | 18 |
| City of Wooster | 13 |
| ODNR (State) | 9 |
| City of Rittman | 9 |
| Rails to Trails of Wayne County | 8 |
| Wayne County Park District | 4 |
| City of Orrville | 4 |
| Chippewa Township | 2 |
| OSU/OARDC | 2 |
| Friends of Vultures Knob / private | 2 |
| Holmes County Rails-to-Trails Coalition | 1 |

---

## Next Stage

**Stage 4: TSV Output** — generate six TSV files (sites, trails, trail_segments, trail_networks, site_networks, access_points) from the 73 normalized records.

Reference specs: `na_tsv_output_site_v5.2.md`, `na_tsv_output_trail_v5.1.md`, etc.
