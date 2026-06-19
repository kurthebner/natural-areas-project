# [COUNTY NAME] [STATE ABBR] — Handoff Document (v6)
**RUN_ID:** `[county_state_yyyy_mm_dd]`  
**PREFIX:** `[OH-XXX]`  
**County:** [County Name], [State]  
**Session date:** [YYYY-MM-DD]  
**Status:** IN PROGRESS | DISCOVERY COMPLETE — PIPELINE READY | COUNTY COMPLETE

---

## Tiers Completed

| Tier | Status | Entities | Notes |
|------|--------|----------|-------|
| T1 Federal & Tribal | COMPLETE / DEFECT / PENDING | [N] Sites, [N] Trailthings, [N] SNs, [N] APs | |
| T2 State | | | |
| T3 District | | | |
| T4 County | | | |
| T5 Township | | | |
| T6 Municipal | | | |
| T7 Conservancy | | | |
| T8 Private | | | |
| T0 Baseline | | | |

---

## Tiers Remaining

- **T[N] [Name]**: [Entry points, known URLs, specific entities expected]
- **T[N] [Name]**: [Entry points]

---

## Key Active Flags

- [Flag or open question description — governance uncertainty, cross-county candidate, DEFECT tier, etc.]

---

## Known Multi-County Entities

*(Populated at bootstrap from DB query — see `na_cross_county_resolution_v6.0.md` §5)*

| Entity ID | Name | Type | Counties | Status |
|-----------|------|------|----------|--------|
| [OH-MC-TT-0001] | [Name] | Trailthing | [Counties] | KNOWN_MC — reference only |

---

## Entities Discovered

*(Running table — all raw records pending pipeline)*

| Tier | Entity ID | Name | Type | Notes |
|------|-----------|------|------|-------|
| T[N] | [OH-XXX-S-001] | [Name] | Site — [Category] | |
| T[N] | [OH-XXX-TT-001] | [Name] | Trailthing — [source_term] | |
| T[N] | [OH-XXX-AP-001] | [Name] | Access Point | |

---

## Held Entities

*(Entities blocked on external resolution — not yet in DB)*

| Entity ID | Name | Hold Reason | Resolution Path |
|-----------|------|-------------|-----------------|
| [OH-XXX-TT-001] | [Name] | cross_county_held | [Partner county] run |

---

## Unresolved Baseline Seeds

*(Baseline entries not yet confirmed by authoritative source)*

| Baseline ID | Name | Status | Notes |
|-------------|------|--------|-------|
| [SEED-001] | [Name] | PENDING | Not found in T1–T[N]; continue searching |

---

## Pre-Discovery Checklist

*(Populated before beginning a tier — complete enumeration of entities/municipalities to visit)*

**Current tier: T[N] [Name]**

- [ ] [Entity or municipality name] — [URL]
- [ ] [Entity or municipality name] — [URL]

---

## Captured Source Data

*(Verbatim tables from authoritative sources — fetched at time of discovery, not deferred)*

### [Source name] — T[N] [Date fetched]

| Name | Address / Location | Acres | URL |
|------|--------------------|-------|-----|
| [Name] | [Address] | [N] | [URL] |

---

## Open Questions

1. [Numbered question — identity, governance, cross-county, scope]
2. [Question]

---

## Next Steps

1. [Ordered action for next session — e.g., "Continue T5 townships starting with [Township]"]
2. [Action]
3. [Action]

---

*This handoff is a progress tracker only. For authoritative procedure detail, read the module files. When this handoff and a module conflict, the module wins.*
