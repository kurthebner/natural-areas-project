---
name: na-processing-quality
description: Orchestrates Natural Areas Project workflows, manages county baselines, and runs quality audits. Triggers on bootstrap, county setup, pipeline orchestration, quality checks, or baseline management.
---

# Natural Areas Processing & Quality Control v5.0

Workflow orchestration, entity resolution, audit logging, and baseline management.

## Bootstrap New County

When starting a new county project:

1. Research jurisdiction — list all municipalities, townships, districts
2. Load baseline module: `view references/na_county_baseline_v5.md`
3. Establish Tier-0 baseline (candidate entity seeds)
4. Initialize session ID: `COUNTY-STATE-YYYYMMDD-seq`
5. Create raw discovery staging file: `{county}_{state}_raw_discovery.yaml`
6. Create skill revision notes file: `{county}_{state}_skill_revision_notes.md`
7. Load audit module: `view references/na_audit_and_logging_v5.md`
8. Check browser availability (Claude in Chrome) — required for map verification
9. Begin discovery (see na-discovery-workflow skill)

**Bootstrap Checklist**:
```
County: [Name], [State]
Cities: [count]
Villages: [count]
Townships: [count]
Special Districts: [count]
Session ID: [COUNTY]-[STATE]-[YYYYMMDD]-[seq]
Staging file: {county}_{state}_raw_discovery.yaml — CREATED
Skill revision notes: {county}_{state}_skill_revision_notes.md — CREATED
Browser available: [yes / no — map verification requires yes]
```

## Full Pipeline Orchestration

For the complete end-to-end pipeline (all stages from discovery through output):

`view references/na_processing_v5.md`

## Resolution Engine

After all 8 discovery tiers complete, run resolution:

`view references/na_resolution_engine_v5.md`

Resolution detects conflicts and merges duplicates. It does not resolve conflicts — normalization resolves them.

## Resolution Rules (Entity-Type Decisions)

When entity type or category is ambiguous:

`view references/na_resolution_rules_v5.md`

Covers: entity-type rules, category edge cases (Boardwalk, Linear Park, Greenway, Buffer Zone, etc.), trail edge cases, Access Point edge cases, ecological edge cases, multi-county conflict rules.

## County Baseline (Tier-0)

The baseline loads after all 8 tiers and provides candidate seeds only. It is never authoritative over discovered data. `township` and `municipality` must never be supplied via baseline.

`view references/na_county_baseline_v5.md`

## Child Site Rules

When to assign `parent_site_id` vs. create separate Sites:

`view references/na_child_site_rules_v5.md`

## Audit & Logging

Every session requires an audit trail. Discovery Log and Normalization Log are strictly separate.

`view references/na_audit_and_logging_v5.md`

## Quality Targets

Discovery: 100% tier coverage, 95%+ entity coverage
Normalization: 100% required fields, 98%+ vocabulary compliance
Output: 100% TSV integrity

## Best Practices Reference

`view references/improved_discovery_methodology.md`

Key lessons: Weston Elementary Park case study, village discovery failures, fetch beats search, map verification requirement for villages under 1,000 population.

## Reference Files

- `references/na_processing_v5.md` — end-to-end pipeline (all 10 stages)
- `references/na_resolution_rules_v5.md` — entity-type and category edge case decisions
- `references/na_resolution_engine_v5.md` — entity resolution, merging, conflict detection
- `references/na_county_baseline_v5.md` — baseline rules and Tier-0 integration
- `references/na_child_site_rules_v5.md` — parent/child site assignment rules
- `references/na_audit_and_logging_v5.md` — audit framework and log schemas
- `references/improved_discovery_methodology.md` — best practices and lessons learned
