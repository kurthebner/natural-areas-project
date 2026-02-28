# Natural Areas Project v5.0
# Skill Update Action Plan — Post Clinton County Session
# Date: 2026-02-28
# Source: clinton_county_skill_revision_notes_3.md (OBS-001 to OBS-031)
#         skill_revision_url_sources.md (11 URLs)
#         GIS lookup session learnings (Township/Municipality derivation)

---

## SKILL FILES TO UPDATE (in order)

### 1. na-processing-quality / SKILL.md
**Changes:**
- [ ] OBS-001/003: Add "Create raw discovery staging file" as step 3 of Bootstrap checklist
- [ ] OBS-009: Add "Create skill revision notes file" to Bootstrap checklist
- [ ] OBS-009: Add naming convention for skill revision notes file

**Bootstrap Checklist additions:**
```
3. Create raw discovery staging file: {county}_{state}_raw_discovery.yaml
4. Create skill revision notes file: {county}_{state}_skill_revision_notes.md
```

---

### 2. na-discovery-workflow / SKILL.md
**Changes:**
- [ ] OBS-001/002: Add note that raw records go to staging FILE not chat window
- [ ] OBS-002: Add chat window vs. file output guidance
- [ ] OBS-017: Add null-tier documentation requirement
- [ ] OBS-009: Reference skill revision notes maintenance
- [ ] Tier table: Correct tier numbering (currently District=3, County=4 — but OBS-010/015 say sub-procedure headers are internally inconsistent; need to audit the table here vs. the sub-procedures)
- [ ] Add: Check browser availability at session start (OBS-018)

**Current tier table in SKILL.md:**
| 3 | District | na_district_discovery_subproc_v5.md |
| 4 | County   | na_county_discovery_subproc_v5.md   |
Note: OBS-010 says the county sub-procedure HEADER says "Tier 4" but county is Tier 3 in the hierarchy. OBS-015 says district sub-procedure header says "Tier 3" but district is Tier 4. So the SKILL.md table itself has District and County SWAPPED relative to the OBS descriptions. Need to clarify which is authoritative.

---

### 3. na-normalization-output / SKILL.md
**Changes:**
- [ ] GIS session: Add GIS spatial lookup methodology detail
- [ ] GIS session: Add GPS error flag guidance (when GPS falls outside expected county)
- [ ] OBS-007: Add Map URL derivation for Sites (from maps_raw)
- [ ] Add: When GIS lookup returns no match, flag as GPS_ERROR and use textual source

**New section to add:**
```
## GIS Derivation — Township and Municipality
township and municipality are populated via TIGER spatial join after GPS is confirmed.
- Use Census TIGER County Subdivisions layer for township
- Use Census TIGER Incorporated Places layer for municipality
- If GPS falls outside the county boundary: flag as GPS_ERROR, derive from address/text source
- If site is multi-county: leave township blank, document in Notes
- GPS errors are common for multi-county sites; verify with address before flagging
```

---

### 4. na-schema-vocabulary / SKILL.md
**Changes:**
- [ ] OBS-007: Add maps_raw to Sites (currently only listed for Trails, Trail Segments, Trail Networks, Site Networks)

**Specific line to update:**
Current: "`maps_raw` added to Trails, Trail Segments, Trail Networks, Site Networks"
New:     "`maps_raw` added to Sites, Trails, Trail Segments, Trail Networks, Site Networks"

---

### 5. na-complete-system / SKILL.md
**Changes:**
- [ ] Minor: Add staging file and skill revision notes to Quick Start step 1
- [ ] Add na-database to Skill Routing table (new skill created this session)

---

## REFERENCE DOCUMENTS TO UPDATE
(These live in the references/ directories of each skill — we cannot edit them directly
since /mnt/skills is read-only. These need to be updated by user in the skill editor.)

### na_discovery_orchestration_v5.md
- OBS-001: Add staging file creation and append discipline
- OBS-002: Add chat vs. file output guidance
- OBS-003: Staging file creation at bootstrap
- OBS-009: Skill revision notes as standing instruction
- OBS-017: Null-tier record format definition

### na_state_discovery_subproc_v5.md (Tier 2)
- OBS-006: Multi-county uncertainty handling
- URL-01: Add ODNR Find-a-Property as §3.0
- URL-02: Add Hunting Area Maps to §3.3
- URL-03: Add Fishing Lake Maps to §3.3
- URL-04: Add River & Stream Fishing Maps to §3.3
- URL-06: Add ODNR Historic Places to §4.1
- URL-07: Add New Deal Era Sites to §4.1
- URL-08: Add ODOT Rest Areas to §4.2
- URL-09: Add new §4.5 Ohio Turnpike (OTIC)
- URL-09: Add ohioturnpike.org to §5.3 recursion allowlist
- URL-11: Add Cardinal Collection to §3.1 as supplemental

### na_fed_tribal_discovery_subproc_v5.md (Tier 1)
- OBS-004: USACE co-managed land note (flag downstream ODNR entities)
- OBS-005: NRHP archaeological sites on private land guidance

### na_county_discovery_subproc_v5.md (Tier 3 or 4 — verify numbering)
- OBS-010: Fix header tier number
- OBS-011: County parks district → Site Network (not standalone Site)
- OBS-012: Cross-county address handling
- OBS-013: Minimal-data sites (GPS-only, no other info)
- OBS-014: Planned vs. built infrastructure
- OBS-028: Add NRHP bridge/structure search step
- OBS-029: Fetch full county parks directory (not just park district site)

### na_district_discovery_subproc_v5.md (Tier 4 or 3 — verify numbering)
- OBS-015: Fix header tier number
- OBS-016: Government conservancy district vs. nonprofit conservancy

### na_municipal_discovery_subproc_v5.md (Tier 6)
- OBS-018: Browser-unavailable branch (flag as PENDING, not zero)
- OBS-019: Empty parks page fallback (Google Maps + Tripadvisor + parcel search)
- OBS-020: Check parks board site separate from city government site
- OBS-021: Map verification mandatory — reinforce rationale
- OBS-022: Scan for access points during map verification pass
- OBS-023: Add grant record search step (county foundation, LWCF, Ohio PARD)

### na_township_discovery_subproc_v5.md (Tier 5 or 6 — verify)
- (No specific OBS targeted here beyond tier numbering audit)

### na_conservancy_discovery_subproc_v5.md (Tier 7)
- OBS-024: Trail coalition ≠ trail owner disambiguation step
- OBS-025: Grant-confirmed preserve absent from current website — status flag
- URL-10: Add ONAPA as cross-check source

### na_private_discovery_subproc_v5.md (Tier 8)
- OBS-026: County lists mix tiers — always verify governance independently
- OBS-027: Boundary overlap flag protocol
- OBS-030: Add hunting preserve and agritourism search queries
- OBS-031: Check NRHP database for features within Tier 8 parcels
- URL-extra: Add ODNR Hunting Preserves registry

### na_resolution_rules_v5.md
- OBS-005: NRHP archaeological sites on private land — entity type definition
- OBS-008: Child site identification — discovery phase vs. normalization phase

### na_discovery_output_spec_v5.md
- OBS-007: Extend maps_raw to Sites
- OBS-017: Define null-tier record format

### na_child_site_rules_v5.md
- OBS-008: Clarify discovery vs. normalization phase for child site identification
- OBS-031: NRHP features within private parcels → child site record

---

## WHAT WE CAN DO NOW vs. LATER

**Now** (SKILL.md files — we can edit these):
- na-processing-quality SKILL.md (4 changes)
- na-discovery-workflow SKILL.md (5 changes)
- na-normalization-output SKILL.md (3 changes)
- na-schema-vocabulary SKILL.md (1 change)
- na-complete-system SKILL.md (2 changes)

**Later** (reference .md files — read-only, user must edit in skill editor):
- 11 reference documents with 40+ targeted changes
- Recommend producing updated full text for each reference doc

---

## PRIORITY ORDER FOR SKILL.MD EDITS

1. na-processing-quality (bootstrap fixes — affects every future county)
2. na-discovery-workflow (staging file + chat guidance — affects every session)
3. na-schema-vocabulary (maps_raw for Sites — affects normalization correctness)
4. na-normalization-output (GIS derivation methodology)
5. na-complete-system (minor updates)
