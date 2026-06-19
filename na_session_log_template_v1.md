# [COUNTY NAME] [STATE ABBR] — Session Log
**RUN_ID:** `[county_state_yyyy_mm_dd]`  
**PREFIX:** `[XXX]`  
**County:** [County Name], [State]  
**Run date:** [YYYY-MM-DD]  
**Status:** IN PROGRESS | PIPELINE COMPLETE | COUNTY COMPLETE

---

## Discovery — Tier Yield

| Tier | Source Type | Query / Source | Entities Found |
|------|-------------|----------------|----------------|
| T1 | OSM | Overpass: boundary=protected_area + leisure=park + etc. | [n] — [brief list or "none"] |
| T2 | State agency | [Agency name + URL] | [n] — [names or "none"] |
| T3 | District agency | [Agency name + URL] | [n] — [names or "none"] |
| T4 | County website | [County parks/rec URL] | [n] — [names or "none"] |
| T5 | Municipal | [City/village + URL] | [n] — [names or "none"] |
| T6 | Municipal (additional) | [City/village + URL] | [n] — [names or "none"] |
| T7 | Land trust / conservancy | [Org name + URL] | [n] — [names or "none"] |
| T8 | Private / other | [Source] | [n] — [names or "none"] |

**Total raw records:** [N]  
**Post-resolution:** [N] Sites, [N] Trails, [N] APs, [N] Trail Segments, [N] Trail Networks, [N] Site Networks

---

## Normalization Decisions

Document only non-obvious calls — vocabulary lookups, category debates, parent assignments, held records. One or two sentences per entry. Skip entities where every field was a straightforward vocabulary match.

- **[Entity ID] [Name]:** [Rationale. E.g., "Raw category 'rest area' mapped to Open Space / Urban Open Space per §7.x mapping table; ODOT ownership confirmed from agency site."]
- **[Entity ID] [Name]:** [Rationale.]
- **HELD — [Entity ID] [Name]:** [Hold reason and what would resolve it.]

---

## GPS Acquisition

**Nominatim:** [N] acquired, [N] failed  
**Fallbacks used:**

| Entity ID | Name | Coords | Confidence | Method |
|-----------|------|--------|------------|--------|
| [ID] | [Name] | [lat, lon] | HIGH/MED/LOW | [Nominatim / manual query / centroid] |

**No GPS / unresolved:** [list or "none"]

---

## Errors and Fixes

Document any pipeline error, unexpected behavior, or deviation from standard procedure. Include the error message, root cause, and fix. If none, write "None."

- **[Stage N — brief label]:** [Error message or description.] Root cause: [explanation]. Fix: [what changed.]

---

## Pipeline Stage Log

| Stage | Result | Notes |
|-------|--------|-------|
| Stage 1 — Resolution | [N records → N entities] | [conflicts, merges, or "clean"] |
| Stage 2 — Normalization | [N entities normalized, N held] | [vocab issues or "clean"] |
| Stage 3 — GPS Acquisition | [N/N acquired] | [fallback summary or "all Nominatim"] |
| Stage 4 — TSV Output | [6 files written] | [zero-entity files or "all populated"] |
| Stage 4.5 — Vocab Gate | PASS / FAIL | [violation count or "clean"] |
| Stage 5 — Integrity Check | PASS / warnings | [warning summary or "clean"] |
| Stage 6 — DB Upsert | [N sites, N trails, N APs upserted] | ["clean" or note conflicts] |

---

## Entity ID Assignments

| Entity ID | Name | Type |
|-----------|------|------|
| [PREFIX-S-001] | [Name] | Site — [Category] |
| [PREFIX-T-001] | [Name] | Trail — [Use Type] |
| [PREFIX-AP-001] | [Name] | Access Point — [AP Type] |

---

## Open Flags

Items that remain unresolved after pipeline completion. If none, write "None."

| Flag ID | Entity | Issue | Resolution Path |
|---------|--------|-------|-----------------|
| [IMP-xxx or local flag] | [Entity ID / Name] | [Description] | [What would close it] |

---

## Status

**[COUNTY COMPLETE / IN PROGRESS / BLOCKED]**  
[One sentence summary if not complete — what's left.]
