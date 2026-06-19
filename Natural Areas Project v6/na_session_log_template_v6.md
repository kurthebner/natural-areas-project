# [COUNTY NAME] [STATE ABBR] — Session Log (v6)
**RUN_ID:** `[county_state_yyyy_mm_dd]`  
**PREFIX:** `[XXX]`  
**County:** [County Name], [State]  
**Run date:** [YYYY-MM-DD]  
**Status:** IN PROGRESS | PIPELINE COMPLETE | COUNTY COMPLETE

---

## Discovery — Tier Yield

| Tier | Source Type | Query / Source | Entities Found |
|------|-------------|----------------|----------------|
| T1 | Federal & Tribal | [Agency name + URL] | [n] — [brief list or "none"] |
| T2 | State | [Agency name + URL] | [n] — [names or "none"] |
| T3 | District | [Agency name + URL] | [n] — [names or "none"] |
| T4 | County | [County parks/rec URL] | [n] — [names or "none"] |
| T5 | Township | [Township roster + URLs] | [n] — [names or "none"] |
| T6 | Municipal | [City/village + URL] | [n] — [names or "none"] |
| T7 | Conservancy & Land Trust | [Org name + URL] | [n] — [names or "none"] |
| T8 | Private | [Source] | [n] — [names or "none"] |

**Total raw records:** [N]  
**Post-resolution:** [N] Sites, [N] Trailthings, [N] Site Networks, [N] APs

---

## Document Collection

Documents downloaded during discovery. Full log in `{county}_document_log.yaml`.

| Filename | Tier | Type | Description |
|----------|------|------|-------------|
| [date_tier_desc.pdf] | T[N] | PDF map | [brief description] |

---

## Normalization Decisions

Document only non-obvious calls. Skip entities where every field was a straightforward vocabulary match.

- **[Entity ID] [Name]:** [Rationale. E.g., "Raw category 'rest area' mapped to Open Space / Urban Open Space per §7.x mapping table."]
- **HELD — [Entity ID] [Name]:** [Hold reason and what would resolve it.]

---

## GPS Acquisition

**Nominatim:** [N] acquired, [N] failed  
**Browser (Claude in Chrome):** [N] acquired  
**Human assist:** [N] acquired  
**Fallbacks used:**

| Entity ID | Name | Coords | Confidence | Method |
|-----------|------|--------|------------|--------|
| [ID] | [Name] | [lat, lon] | HIGH/MED/LOW | [browser / Nominatim / human / fallback] |

**No GPS / unresolved:** [list or "none"]

---

## Errors and Fixes

Document any pipeline error, unexpected behavior, or deviation from standard procedure.

- **[Stage N — brief label]:** [Error description.] Root cause: [explanation]. Fix: [what changed.]

---

## Pipeline Stage Log

| Stage | Result | Notes |
|-------|--------|-------|
| Stage 3 — Resolution | [N records → N entities] | [conflicts, merges, or "clean"] |
| Stage 4a — GPS Fill-Forward | [N filled from DB] | ["none" or list] |
| Stage 4b — GPS Acquisition | [N/N Sites, N/N APs acquired] | [method summary] |
| Stage 4c — GPS Gate | [N held gps_missing] | ["none held" or list] |
| Stage 5 — Normalization | [N entities normalized, N held] | [vocab issues or "clean"] |
| Stage 6 — TSV Output | [4 files written] | [zero-entity files or "all populated"] |
| Stage 6.5 — Vocab Gate | PASS / FAIL | [violation count or "clean"] |
| Stage 7 — Integrity Check | PASS / warnings | [warning summary or "clean"] |
| Stage 7.5 — Human Review | CONFIRMED by [reviewer] | [date confirmed] |
| Stage 8 — DB Upsert | [N sites, N trailthings, N APs upserted] | ["clean" or note conflicts] |

---

## Entity ID Assignments

| Entity ID | Name | Type |
|-----------|------|------|
| [OH-PREFIX-S-001] | [Name] | Site — [Category] |
| [OH-PREFIX-TT-001] | [Name] | Trailthing — [source_term] |
| [OH-PREFIX-AP-001] | [Name] | Access Point — [AP Type] |

---

## Held Entities

| Entity ID | Name | Hold Reason | Resolution Path |
|-----------|------|-------------|-----------------|
| [ID] | [Name] | [hold_reason] | [what resolves it] |

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
