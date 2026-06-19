---
name: na-bootstrap
description: Initializes a county discovery run for the Natural Areas Project. Triggers on county bootstrap, start county, initialize county, begin discovery, or upload of a county baseline file.
---

# Natural Areas Project — Bootstrap Skill v5.2

Initializes a county discovery session. Always run this skill first, before any discovery begins.

## Core Principle

**Discovery = Collection. Normalization = Decisions. Systematic beats smart.**

Never normalize, correct, or interpret field values during discovery. Never populate `township` or `municipality` — GIS-derived only, never from web sources.

## System Architecture

- **Six entity types**: Site, Trail, Trail Segment, Trail Network, Site Network, Access Point
- **Eight discovery tiers**: Federal → State → District → County → Township → Municipal → Conservancy → Private
- **Five pipeline stages**: Bootstrap → Discovery → Resolution → Normalization/GPS → Output/Upsert
- **Entity type sequence within each tier**: Sites → Trails → Trail Segments → Trail Networks → Site Networks → Access Points

## Step 1 — Read the Baseline

The county baseline is a human-curated seed list of known entities. It is a prompt, not a data import.

- Read the baseline before beginning Tier 1
- Internalize what entities are expected — names, rough types, locations
- Do NOT treat baseline entries as raw discovery records
- Do NOT normalize or output baseline entries directly
- Use baseline seeds to recognize and confirm entities during tier discovery
- At the end of discovery, flag any baseline seeds that were never confirmed by an authoritative source

Baseline entries are verified through discovery, not imported as facts.

## Step 2 — Establish Session Files

Create the following files before beginning discovery:

**Staging file**: `{county}_{state}_raw_discovery.yaml`
- All raw discovery records go here
- Append each entity immediately upon discovery
- Never hold records only in chat — chat history is not a record

**Session log**: `{county}_{state}_session_log.md`
- Running log of tier progress, decisions, flags, and observations
- Record null tier results here
- Record baseline seed confirmations and gaps here

**Handoff document**: `{county}_{state}_handoff.md`
- Updated at the end of each session
- Contains: tiers completed, entities found, held entities, unresolved baseline seeds, open questions, next steps
- This is how discovery resumes across sessions

## Step 3 — Confirm County Context

Before beginning Tier 1, establish:

- County name and state
- County seat
- Major municipalities (cities and villages)
- Known townships
- Known park districts or metropark affiliations
- Any known cross-county entities (trail networks, site networks, metropark systems)

Cross-county entities (e.g. Toledo Metroparks straddling Wood and Lucas counties) should be discovered and recorded with their full county list. They will be held pending member resolution from other county runs.

## Step 4 — Context Window Management

Context windows are finite and cumulative. Manage carefully:

- Write raw discovery records to the staging file immediately — do not accumulate them in chat
- Keep chat summaries brief: name, tier, entity type, key flags only
- Read skill and reference files only when needed for the current task
- Update the handoff document before the session ends
- If context is running low, complete the current entity, write to staging file, update handoff, and stop

## Tier Ordering Rules

- Complete all six entity types for a tier before advancing to the next tier
- Entity type sequence within each tier: Sites first, then Trails, Trail Segments, Trail Networks, Site Networks, Access Points last
- This ordering ensures parent entities exist before children need them
- Never skip a tier — record null results explicitly if a tier yields nothing
- Never mark a tier complete without evidence

## Network Entity Special Handling

Network entities (Trail Networks, Site Networks) are discovered at their governance tier but finalized late:

- Discover the network entity and record it at the appropriate tier
- member_site_ids and member_trail_ids will be blank or partial — this is correct
- Networks with unresolved members are held, not rejected
- Cross-county networks (e.g. national trail networks, metropark systems) remain held until all relevant counties are processed
- Do not hold up tier completion waiting for member resolution

## Reference Documents

When needed during bootstrap:
- `na_discovery_protocol_v5.x.md` — authoritative rules
- `na_discovery_orchestration_v5.x.md` — execution order
- `na_county_baseline_v5.x.md` — baseline module
- `README_v5.x.md` — architecture overview
