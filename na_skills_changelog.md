# Natural Areas Project — Skills Changelog

Changes to skill files (na-pipeline, na-discovery, na-bootstrap, na-entities, na-quality).
Most recent changes first within each skill.

---

## na-pipeline

### 2026-05-12 (IMP-108 / IMP-109)
- **IMP-109 — Module versioning and reference convention established**:
  Canonical rule: filenames and document headers carry version numbers;
  inter- and intra-module references use bare document title only (no
  version suffix), plus section as needed. Module manifest is the single
  authoritative source for current version numbers — update it when a
  module is versioned up; no other references need changing.
- **IMP-108 — Deversioning pass applied**: All cross-references in active
  modules scrubbed to bare titles. 7 stale duplicate versions moved to
  `deprecated/`. Skill SKILL.md files (`na-bootstrap`, `na-discovery`,
  `na-pipeline`) updated: 4 stale versioned references replaced with bare
  titles. **No behavioral changes** — read gates and module pointers unchanged;
  only the version suffix was removed from reference strings.

### 2026-05-12 (IMP-107)
- **IMP-107 — Global entity ID format migration**: All entity IDs in the DB
  migrated from bare `{COUNTY}-{TYPE}-{SEQ}` to `OH-{COUNTY}-{TYPE}-{SEQ}`.
  Multi-county entities (counties field >1 value) now use `OH-MC-{TYPE}-{SEQ}`.
  2,245 entities renamed; 6,294 cell updates across entity, FK, and provenance
  tables; 34 TSV files updated. 7 Category 2 true duplicates deleted
  (DEF-T-002, LUC-T-013, PAU-TR-002, WOD-TR-003, HEN_T_006, LUC-T-010,
  WIL-TR-003); 4 Category 1 sequence collisions renumbered.
  Cross-county resolution protocol updated to v5.2; module manifest updated
  to v5.18. **No skill file text changes required** — ID format is documented
  in `na_cross_county_resolution.md`; pipeline and discovery skills
  reference that module rather than encoding the format directly.

### 2026-05-10 (IMP-106)
- **IMP-106 — File Writing Rules**: Added `## File Writing Rules (IMP-106)`
  section to na-pipeline SKILL.md. Rule: never use bash heredocs for files
  longer than ~30 lines — use the `Write` tool for new files, `Edit` tool for
  targeted changes. IMP-079 YAML key-targeted appends remain the one legitimate
  bash file operation. Mandatory syntax verification gate after every script
  write: `python -m py_compile path && echo "OK"`. Failure mode documented:
  silent truncation, file appears written, last line is mid-expression.
  Also added: Human Review Gate (Stage 5.5) now enforced at code level in
  `na_pipeline_core.py` v1.1 — `ReviewRequired` exception raised unless
  `--confirm-review` flag passed. Pipeline exits with code 2 at gate without
  the flag; dry runs bypass gate automatically.
  **Manual update required**: na-pipeline SKILL.md in the skills folder is
  read-only from the sandbox. Rule text is in `na_processing_orchestration.md`
  §12 and should be copied into the skill file at next manual edit opportunity.

### 2026-05-07 (IMP-105)
- **IMP-105 — No skill file changes required.** Trail Network Vocabulary
  bumped to v5.3 (Equestrian Trail Network added); Site Network
  Normalization Contract bumped to v5.3 (org_type schema gap resolved).
  Read gates in na_trail_network_normalization_v5.2 and
  na_site_network_normalization_v5.3 updated internally; skill
  orchestration layer unchanged.

### 2026-05-07 (IMP-104)
- **IMP-104 — Cross-County Resolution Protocol**: Pipeline Startup section
  must now include a mandatory read of `processing/na_cross_county_resolution_v5.1.md`
  for any county run that includes multi-county entity candidates. Stage 1a
  (Resolution Pass 1) note added: Resolution Engine Phase 0 (MC candidate
  detection) runs before Phase 1 Grouping — read §7 of the cross-county
  protocol before running any resolution pass on a county with CROSS_COUNTY_CANDIDATE
  flags or known multi-county entities.

## na-bootstrap

### 2026-05-07 (IMP-104)
- **IMP-104 — Bootstrap pre-discovery DB check added**: Step 3 of the
  bootstrap procedure must now include a Known Multi-County Entities DB
  check before discovery begins. Read `processing/na_cross_county_resolution_v5.1.md`
  §5 for the required SQL queries and output format. The baseline document
  must include a "Known Multi-County Entities" section listing all MC entities
  and held entities from other counties that reference the target county.

## na-discovery

### 2026-05-07 (IMP-104)
- **IMP-104 — CROSS_COUNTY_CANDIDATE flagging requirement**: Tier transition
  checkpoint updated. When closing any discovery tier, if any entity's counties
  field lists more than one county, the discoverer must verify whether
  `CROSS_COUNTY_CANDIDATE` (or `KNOWN_MC:{id}`) has been set in
  `identity_notes_raw`. Read `processing/na_cross_county_resolution_v5.1.md`
  §6 for full flagging rules including when NOT to flag (generic names at
  separate installations, single-county parks that briefly cross a line).

## na-pipeline

### 2026-05-07 (IMP-102)
- **IMP-102 — No skill file changes required.** Trail Network and Site Network
  normalization contracts updated to v5.2 with mandatory vocabulary read gates;
  vocabulary files bumped to Trail Network Vocabulary v5.2 and Site Network
  Vocabulary v5.3. na-pipeline skill references normalization modules by
  unversioned name — read gates are enforced by the contracts themselves at
  runtime, not by the skill orchestration layer.

### 2026-05-07
- **IMP-101 — Pre-run DB integrity check**: Pipeline Startup section updated.
  Added mandatory `PRAGMA integrity_check` + `PRAGMA foreign_key_check` step
  before any pipeline writes. Hard stop on non-"ok" integrity_check result;
  FK violations are warnings. Also documents state field rule: `run_metadata.state`
  must be full state name ("Ohio"), never abbreviation ("OH").

### 2026-05-02
- Added Pipeline Startup mandatory read gate: `audit/na_audit_and_logging.md`
- Added Stage 1a mandatory read gates: `na_resolution_engine.md`, `na_resolution_rules.md`
- Added Stage 1b (Resolution Pass 2, Access Points only) as a distinct stage
- Added Stage 2b mandatory read gate: `discovery/na_gps_acquisition.md`
- Expanded Stage 3a mandatory reads from 3 vocabulary modules to all 6 (one per entity type) plus normalization contracts table and conditional `na_child_site_rules.md`
- Added Stage 4 mandatory read gates: TSV output spec for each entity type
- Added Stage 5.5 Human Review Gate — pipeline halts before DB upsert pending explicit human confirmation
- Moved Nominatim rural address fallback (IMP-081), county bounding box check (IMP-081), and large-county GPS timeout protocol (IMP-083) to `discovery/na_gps_acquisition.md` §5.7, §5.8, §9.4
- Moved Canonical Feature Mapper to `utilities/na_feature_mapper_reference.md`; replaced with pointer
- Added end marker: `# END OF NA_PIPELINE_SKILL`
- Stripped null bytes and trailing whitespace from file

### 2026-04-xx (prior session)
- Added Stage 1a / Stage 1b two-pass resolution structure
- Added GPS Gate (IMP-069) as Stage 2c
- Added Held-Entity Child Rule (IMP-086) to Stage 3
- Removed Derived Label from per-entity routing (Sites and APs)
- Corrected Stage 4.5 vocabulary section reference §7.5 → §5
- Added `trail_parents` to Stage 6 DDL relationship tables
- Added prerequisite note: all 8 discovery tiers must be complete before invoking
- Corrected description header: GPS moved to correct position after Resolution Pass 1
- Updated Pipeline Overview diagram: Stage 1a → Stage 2 → Stage 1b → Stage 3 sequence
- TSV output before DB upsert (was reversed)

---

## na-discovery

### 2026-05-07 (IMP-103)
- **IMP-103 — Water Trail Discovery Sub-Procedure added**: New module
  `na_water_trail_discovery_subproc.md` added to /discovery.
  Consolidates water trail entity typing, qualification threshold,
  GPS rules, Access Point rules, Trail Segment segmentation triggers,
  and multi-county handling from IMP-008, IMP-009, IMP-019, IMP-044.
- **na-discovery skill updated**: `na_water_trail_discovery_subproc.md`
  added to Entity Discovery Sub-Procedures list with mandatory read
  note — read §2 before concluding null for Water Sites, §3 before
  concluding null for water Trails, for any county with navigable
  waterways or scenic river designations.
- **Hazard Portage address handling refined**: §6.4 now distinguishes
  between Watercraft Access Points (address strongly expected; flag
  AP_ADDRESS_MISSING if not found) and Hazard Portages (address sought
  but not required; blank is correct for remote/river-access-only
  portages; AP_ADDRESS_UNVERIFIED flag for uncertain cases). Anti-patterns
  table and §9.3 field mapping updated to match.

### 2026-05-05
- **IMP-096 — Ohio Township Officials roster as Tier 5 authority**: Bootstrap Step 3
  updated to reference `Townships_Officials2022-2023.xlsx` as the pre-discovery
  enumeration source for Tier 5 county township lists and trustee/fiscal officer
  website URLs.
- **IMP-097 — Parks & Open Space GIS layer cross-reference**: Tier 4–6 discovery note
  added directing cross-reference against `Parks_and_Open_Space_7241389496048841555.csv`
  for the 15 covered central Ohio counties (DEL, FAI, FAY, FRA, HOC, KNO, LIC, LOG,
  MAD, MAR, MRW, PER, PIC, ROS, UNI) during discovery.

### 2026-05-02
- Removed CHANGES block from skill file (moved here)
- Replaced passive `Reference:` line at handoff with mandatory read instruction for `na_processing_orchestration.md`
- Added end marker: `# END OF NA_DISCOVERY_SKILL`

### 2026-04-xx (prior session) — v5.4 → v5.5
- **IMP-078 — Source Authority Hierarchy**: Added section declaring precedence order: protocol modules and sub-procedures > handoff document > session memory/summaries
- **IMP-074 — Resumed Session Protocol**: Added section requiring orchestration module §6 verification as first action in any resumed session
- **IMP-075 — Mandatory Sub-Procedure Read**: Added mandatory sub-procedure read requirement to tier transition checkpoint
- **IMP-076 — DEFECT Flagging**: Added DEFECT status requirement to Null Tier Results section
- **IMP-077 — Mandatory Step Completion Gate**: Added to Tier Close Verification section
- **IMP-072 — Ohio Auditor Pre-Enumeration**: Added note to Tier 3 requiring Ohio Auditor search before any other source
- Restored ~85 lines of truncated content (IMP-080, IMP-079, baseline seed tracking, municipal tier rules, cross-county entities, GPS during discovery, handoff instructions)
- Added explicit handoff section: verification steps, handoff status, inputs the pipeline skill expects

---

## na-bootstrap

### 2026-05-02
- Added end marker: `# END OF NA_BOOTSTRAP_SKILL`

### 2026-04-xx (prior session)
- Updated pipeline stage summary: "Five pipeline stages" → full 8-stage post-discovery sequence including GPS Gate and two Resolution passes

---

## na-entities

### 2026-05-02
- Added end marker: `# END OF NA_ENTITIES_SKILL`

### 2026-04-xx (prior session)
- Updated Derived Label note: removed from all entity types; no entity type computes or stores a Derived Label

---

## na-quality

### 2026-05-05
- **IMP-097 — Parks & Open Space Completeness Gate added**: New §"Parks & Open Space
  Completeness Gate (IMP-097)" section added. Covers: 15-county coverage scope,
  CSV data source and fields, filter rules (Status=Public; exclude Sub_Type=NOS),
  fuzzy name matching procedure (token-set ratio ≥ 80), `parks_os_unmatched` flag,
  three resolution outcomes. Runs after PAD-US gate.
- **IMP-099 — CEMETERY