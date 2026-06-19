---
name: na-discovery-workflow
description: Executes tier-based discovery of parks, trails, and natural areas across U.S. counties. Triggers on discover, catalog, find parks, county discovery, or mentions of natural areas in any location.
---

# Natural Areas Discovery Workflow v5.0

Executes tier-based discovery of parks, trails, and natural areas across any U.S. county.

## Core Principle

**Discovery = Collection. Normalization = Decisions.**

During discovery, collect raw data exactly as found. Do not normalize, correct, or interpret field values. Do not populate `township` or `municipality` — these are GIS-derived only.

## Before Starting Any Discovery

Read the best-practices reference first:

`view references/improved_discovery_methodology.md`

Then load the discovery protocol:

`view references/na_discovery_protocol_v5.md`

## 8-Tier Discovery Sequence

Execute tiers in order. Complete each tier 100% before advancing.

| Tier | Category | Sub-Procedure |
|------|----------|---------------|
| 1 | Federal & Tribal | `references/na_fed_tribal_discovery_subproc_v5.md` |
| 2 | State | `references/na_state_discovery_subproc_v5.md` |
| 3 | District | `references/na_district_discovery_subproc_v5.md` |
| 4 | County | `references/na_county_discovery_subproc_v5.md` |
| 5 | Township | `references/na_township_discovery_subproc_v5.md` |
| 6 | Municipal | `references/na_municipal_discovery_subproc_v5.md` |
| 7 | Conservancy | `references/na_conservancy_discovery_subproc_v5.md` |
| 8 | Private | `references/na_private_discovery_subproc_v5.md` |

## Entity Discovery Sub-Procedures

Read the relevant sub-procedure when discovering that entity type:

- `references/na_site_discovery_subproc_v5.md`
- `references/na_trail_discovery_subproc_v5.md`
- `references/na_trail_segment_discovery_subproc_v5.md`
- `references/na_trail_network_discovery_subproc_v5.md`
- `references/na_site_network_discovery_subproc_v5.md`
- `references/na_access_point_discovery_subproc_v5.md`

## Wrapper Modules

- `references/na_discovery_protocol_v5.md` — rules and entity definitions (read first)
- `references/na_discovery_orchestration_v5.md` — execution order and state management
- `references/na_discovery_metadata_spec_v5.md` — metadata structure
- `references/na_discovery_output_spec_v5.md` — output format requirements

## After All Tiers Complete

`view references/na_resolution_engine_v5.md`

## Critical Rules

**EXHAUSTIVE BEATS EFFICIENT**: Complete every tier 100% before moving to next.
**FETCH BEATS SEARCH**: Always use `web_fetch` on official pages. Never rely on search snippets alone.
**VIEW MAPS DIRECTLY**: Do not search for map references — open Google Maps and view the location.
**NEVER assume official pages are complete**: Cross-verify with maps. (See Weston Elementary case study.)
**DOCUMENT NEGATIVES**: Record "no parks found" with evidence. Never assume.
**township and municipality are blank during discovery**: GIS-derived only, never from web sources.

## Common Failures to Avoid

- Skipping small villages ("they probably don't have parks")
- Using search snippets instead of fetching full pages
- Searching FOR maps instead of VIEWING maps directly
- Marking "0 parks" for a village without map-based verification
- Populating township or municipality during discovery
