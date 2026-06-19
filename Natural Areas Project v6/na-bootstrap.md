---
name: na-bootstrap
description: Initializes a county discovery run for the Natural Areas Project v6. Triggers on county bootstrap, start county, initialize county, begin discovery, or upload of a county baseline file.
---

# Natural Areas Project — Bootstrap Skill v6.0

Initializes a county discovery session. Always run this skill first, before any discovery begins.

## Core Principle

**Discovery = Collection. Normalization = Decisions. Systematic beats smart.**

Never normalize, correct, or interpret field values during discovery. Never populate `township` or `municipality` — GIS-derived only. Never classify a Trailthing as trail, trail segment, or trail network — capture `source_term_raw` verbatim and stop there.

## System Architecture

- **Four entity types**: Site, Trailthing, Site Network, Access Point
- **Eight discovery tiers**: Federal → State → District → County → Township → Municipal → Conservancy → Private
- **Pipeline stages** (post-discovery): Resolution (single pass) → GPS Fill-Forward → GPS Acquisition → GPS Gate (Sites + APs) → Normalization → TSV Output → Vocabulary Validation → TSV Integrity Check → Human Review → Database Upsert
- **Entity type sequence within each tier**: Sites → Trailthings → Site Networks → Access Points

## Step 1 — Read the Baseline

The county baseline is a human-curated seed list of known entities. It is a prompt, not a data import.

- Read the baseline before beginning Tier 1
- Internalize what entities are expected — names, rough types, locations
- Do NOT treat baseline entries as raw discovery records
- Do NOT normalize or output baseline entries directly
- Use baseline seeds to recognize and confirm entities during tier discovery
- Trail-type baseline entries will seed as Trailthings — do not pre-classify them
- At the end of discovery, flag any baseline seeds never confirmed by an authoritative source as `unconfirmed_baseline_seed`

## Step 2 — Establish Session Files

Create the following files before beginning discovery:

**Staging file**: `{county}_{state}_raw_discovery.yaml`
- All raw discovery records go here
- Append each entity immediately upon discovery
- Never hold records only in chat — chat history is not a record

**Session log**: `{county}_{state}_session_log.md`
- Use `na_session_log_template_v6.md` (v6 project root) as the starting structure — copy it and fill in the county header before beginning Tier 1
- Tier Yield table: fill in each row as a tier completes (entity count + brief name list); record null results here
- Normalization Decisions section: one or two sentences per non-obvious call only
- Errors and Fixes section: any pipeline error, unexpected behavior, or deviation

**Handoff document**: `{county}_{state}_handoff.md`
- Use `na_handoff_template_v6.md` (v6 project root) as the starting structure
- Updated at the end of each session
- Required sections:
  - **Tiers Completed** — summary of each tier with entity counts
  - **Tiers Remaining** — what's left with known entry points
  - **Key Active Flags** — unresolved issues, governance questions, pending verifications
  - **Entities Discovered** — running table of all raw records (pending pipeline)
  - **Held Entities** — records blocked on external resolution
  - **Unresolved Baseline Seeds** — seeds not confirmed by an authoritative source
  - **Open Questions** — numbered list of unanswered identity, governance, or data questions
  - **Next Steps** — ordered action list for the next session
  - **Pre-Discovery Checklist** — complete enumeration of known entities/municipalities for the upcoming tier, with known URLs, checked off as visited
  - **Captured Source Data** — verbatim tables from authoritative sources at fetch time; GPS columns left blank at discovery

**Document log**: `{county}_document_log.yaml`
- Log every downloaded document (map, PDF, brochure, GPX/KML, GIS export) at time of download
- Format per `discovery/na_discovery_orchestration_v6.0.md` §4
- Filename convention: `{date}_{tier}_{short-descriptor}.{ext}`
- Save downloaded files to `source_documents/` folder

## Step 3 — Confirm County Context

Before beginning Tier 1, establish:

- County name and state
- County seat
- Major municipalities (cities and villages)
- Known townships — **for Ohio counties, derive the canonical township list from `Townships_Officials2022-2023.xlsx`** (filter by County Name; 1,307 active townships across 88 counties). Authoritative pre-discovery enumeration for Tier 5.
- Known park districts or metropark affiliations
- Any known cross-county entities

**Known Multi-County Entities DB check (IMP-104):** Before discovery begins, query the DB
for any existing entities whose `counties` field includes the target county. Run the
queries in `processing/na_cross_county_resolution_v6.0.md` §5. The session files must include
a "Known Multi-County Entities" section listing all MC entities and held entities from other
counties that reference the target county. When you encounter one of these during discovery,
use `KNOWN_MC:{id}` rather than `CROSS_COUNTY_CANDIDATE` in `identity_notes_raw`.

**Entity Sequence Numbering Gaps (IMP-117):** Sequence numbers may have gaps across county
runs. Gaps do not indicate data loss — they arise from provisional IDs superseded during
resolution, entities merged into existing records, or sequence numbers withdrawn during QA.
Do not infer missing entities from gaps.

## Step 4 — Context Window Management

- Write raw discovery records to the staging file immediately — do not accumulate in chat
- Write source tables to the handoff's Captured Source Data section at fetch time
- Write downloaded documents to `source_documents/` and log them in the document log immediately
- Write the municipality/entity list to the handoff's Pre-Discovery Checklist before beginning a tier's individual searches
- Keep chat summaries brief: name, tier, entity type, key flags only
- Update the handoff document before the session ends
- If context is running low: complete the current entity, write to staging file, update handoff, log any pending documents, and stop

The staging file + handoff + document log together are the durable record. Chat history is not.

## Tier Ordering Rules

- Complete all four entity types for a tier before advancing to the next tier
- Entity type sequence within each tier: Sites first, then Trailthings, Site Networks, Access Points last
- This ordering ensures parent entities exist before children need them
- Never skip a tier — record null results explicitly if a tier yields nothing
- Never mark a tier complete without evidence

## Network Entity Special Handling

Site Networks are discovered at their governance tier but finalized late:
- Discover the network entity and record it at the appropriate tier
- `member_site_ids` will be blank or partial at discovery — this is correct
- Create SITE_NETWORK_PROVISIONAL at first member site encounter; update as additional members are found
- Networks with unresolved members are held, not rejected
- Cross-county networks remain held until all relevant counties are processed
- Do not hold up tier completion waiting for member resolution

**Every tier requires an explicit Site Network result** — either a record or a documented null. Silence is not a null. If no Site Networks qualify at a tier, stage a null-evidence block before closing that entity type.

### Threshold Rules (summary — read Site Network Discovery Sub-Procedure v6.0 §3 for full rules)

The four threshold rules determine when a Site Network record is created. Rules are checked in order:

| Rule | Org Type | Threshold |
|---|---|---|
| Rule 1 | Formal designation (NHA, Scenic Corridor, Heritage Corridor, etc.) | Always — regardless of member site count |
| Rule 2 | Conservation or land-holding org (Land Trust, County Authority, State Agency, Federal Agency, Nonprofit Conservancy, Regional Authority) | 2+ member Sites |
| Rule 3 | Municipal Department | 3+ in-scope member Sites |
| Rule 4 | Other | 3+ member Sites with documented rationale |

**SITE_NETWORK_PROVISIONAL**: Create a provisional record when the first member Site is cataloged for an organization expected to meet threshold. Do not wait until threshold is confirmed — create early, remove flag when threshold is met.

```
identity_notes_raw: "SITE_NETWORK_PROVISIONAL — [org name] first member site
cataloged [date]; [N] additional member sites expected. Threshold: Rule [N] —
[applicable rule summary]."
```

**SITE_NETWORK_UNCERTAIN**: Use only for genuine ambiguity about `org_type` or `network_type` — not as a substitute for PROVISIONAL. See Site Network Discovery Sub-Procedure v6.0 §3.7.

### Tier Expectations for Site Networks

- **Tiers 1–2 (Federal, State)**: NHAs, scenic corridors, state program portfolios, federal program portfolios
- **Tier 3 (District)**: Park district systems, conservancy district portfolios
- **Tier 4 (County)**: County park systems (if multi-site and above threshold)
- **Tier 5 (Township)**: Rare — township-managed multi-site systems only
- **Tier 6 (Municipal)**: Municipal recreation systems (3+ in-scope sites)
- **Tier 7 (Conservancy)**: Land trust portfolios, nonprofit conservation portfolios
- **Tier 8 (Private)**: Private multi-site systems (rare)

Trailthings that are members of Site Networks: record `parent_site_network_raw` only when the authoritative source explicitly frames that relationship.

## eBird Hotspot ID Capture

For every Site discovered, check whether an eBird hotspot exists for it. The eBird
hotspot ID (`L` + digits, e.g. `L123456`) links this database to eBird sighting
records and should be captured at discovery time while the site is already open.

**How to check**: On [ebird.org/explore](https://ebird.org/explore), search by site
name or use the map. If a hotspot exists at the location, the URL will contain the
L-code (e.g. `ebird.org/hotspot/L123456`). Record it in `ebird_hotspot_id` on the
raw discovery record.

Record blank if no hotspot is found — do not create or infer one.

## Reference Documents

When needed during bootstrap:
- `na_discovery_protocol_v6.0.md` — authoritative rules
- `na_discovery_orchestration_v6.0.md` — execution order and document collection system
- `na_county_baseline_v6.0.md` — baseline module
- `na_cross_county_resolution_v6.0.md` §5 — MC entity DB queries

---
# END OF NA_BOOTSTRAP_SKILL
