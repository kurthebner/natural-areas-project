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
- **Pipeline stages** (post-discovery): Resolution (Pass 1) → GPS Fill-Forward → GPS Acquisition → GPS Gate (Sites only) → Resolution (Pass 2, APs) → GPS Gate (APs only) → Normalization → TSV Output → Vocabulary Validation → TSV Integrity Check → Human Review → Database Upsert
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
- Use `na_session_log_template_v1.md` (project root) as the starting structure — copy it and fill in the county header before beginning Tier 1
- Tier Yield table: fill in each row as a tier completes (entity count + brief name list); record null results here
- Normalization Decisions section: one or two sentences per non-obvious call only — skip entities where every field was a clean vocabulary match
- Errors and Fixes section: any pipeline error, unexpected behavior, or deviation from standard procedure
- Record baseline seed confirmations and gaps here

**Handoff document**: `{county}_{state}_handoff.md`
- Updated at the end of each session
- This is the only record that survives context breaks — more important than chat summaries
- Required sections:
  - **Tiers Completed** — summary of each tier with entity counts
  - **Tiers Remaining** — what's left with known entry points
  - **Key Active Flags** — unresolved issues, governance questions, pending verifications
  - **Entities Discovered** — running table of all raw records (pending pipeline)
  - **Held Entities** — records blocked on external resolution
  - **Unresolved Baseline Seeds** — seeds not yet confirmed by an authoritative source
  - **Open Questions** — numbered list of unanswered identity, governance, or data questions
  - **Next Steps** — ordered action list for the next session
  - **Pre-Discovery Checklist** *(created at tier start, before searches begin)* — complete enumeration of known entities/municipalities for the upcoming tier, with known URLs, checked off as visited. The next session resumes directly from this list without reconstructing it.
  - **Captured Source Data** *(populated at fetch time, not at staging time)* — verbatim tables from authoritative sources (parks address lists, preserve inventories, etc.). GPS columns left blank at discovery; filled during map verification (IMP-031) or the GPS acquisition pass. Eliminates re-fetching when a session ends between discovery and staging.

## Step 3 — Confirm County Context

Before beginning Tier 1, establish:

- County name and state
- County seat
- Major municipalities (cities and villages)
- Known townships — **for Ohio counties, derive the canonical township list from `Townships_Officials2022-2023.xlsx`** (filter by County Name column; 1,307 active townships across 88 counties). This is the authoritative pre-discovery enumeration for Tier 5. Note any townships absent from the roster as defunct candidates (see IMP-005 / Township Discovery Subproc §3.1a).
- Known park districts or metropark affiliations
- Any known cross-county entities (trail networks, site networks, metropark systems)

Cross-county entities (e.g. Toledo Metroparks straddling Wood and Lucas counties) should be discovered and recorded with their full county list. They will be held pending member resolution from other county runs.

## Step 4 — Context Window Management

Context windows are finite and cumulative. Manage carefully:

- Write raw discovery records to the staging file immediately — do not accumulate them in chat
- Write source tables (parks lists with addresses, preserve inventories) to the handoff's **Captured Source Data** section at fetch time — do not defer to staging time
- Write the municipality/entity list to the handoff's **Pre-Discovery Checklist** before beginning any individual searches for a tier
- Keep chat summaries brief: name, tier, entity type, key flags only
- Read skill and reference files only when needed for the current task
- Update the handoff document before the session ends
- If context is running low, complete the current entity, write to staging file, update handoff (including Captured Source Data and Pre-Discovery Checklist), and stop

The staging file + handoff together are the durable record. Chat history is not.

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
- `na_discovery_protocol.md` — authoritative rules
- `na_discovery_orchestration.md` — execution order
- `na_county_baseline.md` — baseline module
- `README.md` — architecture overview

---
# END OF NA_BOOTSTRAP_SKILL
