# Natural Areas Project — Improvements & Tests Backlog
# Created: 2026-05-02
# Update this file as items are completed or new ideas arise.

---

## PRIORITY 1 — Completeness & Validation

### PAD-US Completeness Gate
Add a named validation step to the quality module (na-quality skill and
na_audit_and_logging or a new module) that cross-checks a completed county
against the Protected Areas Database of the US (PAD-US).
- PAD-US is a free federal open dataset covering all governance tiers
- After pipeline closes a county, compare entity names/locations against
  PAD-US records within the county bounding box
- Flag anything in PAD-US with no match in the NAP database
- Document explicitly what PAD-US does NOT cover:
  - Tier 5 (townships): weakest coverage
  - Tier 6 (small municipal parks): weakest coverage
- For Tiers 5–6 gaps: Ohio Auditor parcel data (public ownership parcels
  with no matching entity) is the better cross-check — more work but more
  thorough
- Call this the "Completeness Gate" — run it before marking a county closed
- Prove the concept on Van Wert first, then codify into the quality module

### When to do comprehensiveness work
Decision: Shore it up NOW before going further — not after 88 counties.
Reason: If there's a systematic gap in the protocol (e.g., a source type
consistently missed in the township tier), fixing it retroactively across
a completed state is very expensive. One missed county is cheap; one missed
source type across all counties is not.

---

## PRIORITY 2 — Pipeline Infrastructure

### YAML Sanitizer / Validator
The raw discovery YAMLs have a parse defect: bare # characters inside
field values (e.g., "Pavilion #1" in features_raw) are interpreted by
the YAML parser as comments, breaking yaml.safe_load_all().
- Write a pre-processor that quotes or escapes those values
- Or write a custom loader that handles the defect gracefully
- Affects: any future use of raw discovery YAMLs as pipeline input
- Van Wert example: line 780 "Pavilion #1 (near Playground)" in features_raw

### na_generate_config.py — Config Scaffolding Tool
Given a raw discovery YAML, auto-generate the pipeline config JSON skeleton:
- Read the YAML header (county, state, run_id, prefix)
- Assign entity IDs from prefix (VNW-S-001, VNW-T-001, etc.)
- Lift name_raw into name field scaffold
- Leave all normalized fields blank for Claude to fill during Stage 2
- Output: {county}_{state}_pipeline_config.json ready for normalization
- Significantly reduces per-county scaffolding work

### Deprecate Old Per-County Pipeline Scripts
Van Wert now has both:
  - van_wert_oh_pipeline.py (old monolithic script, self-contained)
  - van_wert_oh_pipeline_config.json (new parameterized approach)
The old script is now redundant. For new counties, only the JSON config
approach should be used. Consider moving old scripts to deprecated/ or
adding a header comment marking them as superseded.

---

## PRIORITY 3 — Copilot Hybrid Workflow Test

### Test: Copilot for Discovery Tier Research
Copilot (Windows, with access to NAP module files) is a candidate for
the web-research-heavy parts of discovery, reducing Claude token usage.
- Test plan: run one complete tier (suggest Tier 2 — State, or Tier 3 —
  District) for a new county using Copilot for web lookup
- Claude handles: YAML writing, vocabulary enforcement, tier sequencing,
  normalization decisions
- Copilot handles: finding source URLs, pulling address lists, checking
  Ohio Auditor, reading park district websites
- Evaluate: Does Copilot reliably follow the protocol? Does it maintain
  session discipline? Is the handoff friction worth the token savings?
- Key question: Can Copilot load and follow the tier sub-procedure modules
  (e.g., na_municipal_discovery_subproc) without Claude?

---

## PRIORITY 4 — Module & Skill Maintenance

### Skill Files — Verify Install
The four updated skill files (na-pipeline, na-discovery, na-bootstrap,
na-quality) have been uploaded to the Claude Customize area.
- User confirms uploads are done
- Claude cannot verify installed versions directly (skills directory is
  a read-only snapshot from session start)
- Next session: check that END markers are present after each skill loads;
  absent marker = truncation = re-upload needed
- Working copies: na-*-SKILL-updated.md in project root
- Version history: na_skills_changelog.md

### na_processing_orchestration.md — Stage Numbering Audit
The processing orchestration module and the pipeline skill may have
diverged on stage numbers after the two-pass resolution restructure
(Stage 1a / Stage 1b split, GPS Gate as Stage 2c). Verify they agree.

---

## COMPLETED THIS SESSION (2026-05-02)

- [x] Added mandatory read gates to na-pipeline skill at each stage
- [x] Added Stage 5.5 Human Review Gate (halt before DB upsert)
- [x] Moved GPS protocols (IMP-081, IMP-083) to na_gps_acquisition module
- [x] Moved Canonical Feature Mapper to utilities/na_feature_mapper_reference.md
- [x] Added end markers (# END OF NA_*_SKILL) to all five skills
- [x] Fixed truncated content in na-entities and na-quality from deprecated sources
- [x] Removed CHANGES blocks from skill files; created na_skills_changelog.md
- [x] Updated na-bootstrap skill: mandatory module manifest read gate
- [x] Updated na-discovery skill: mandatory read instruction (not passive reference)
- [x] Updated na_module_manifest §11: skills as orchestration layers, architecture note
- [x] Updated na_module_manifest §2: added /utilities, fixed /skills filenames
- [x] Added na_module_manifest §14: utilities section, parameterized pipeline docs
- [x] Wrote utilities/na_run_county.py — county pipeline driver
- [x] Generated County_Spreadsheets/Van Wert/van_wert_oh_pipeline_config.json
- [x] Wrote utilities/na_pipeline_config_template.json — empty skeleton for new counties
- [x] Dry-run verified: na_run_county.py processes Van Wert config end-to-end cleanly
