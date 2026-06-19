---
name: na-discovery
description: Executes tier-based discovery of natural areas entities across U.S. counties. Triggers on discover, find parks, catalog entities, tier discovery, or any mention of searching for natural areas in a location.
---

# Natural Areas Project — Discovery Skill v5.5

## Project Orientation Protocol (IMP-112)

**Mandatory first step in every session — new or resumed — before reading any module, touching any data, or beginning any tier work.**

1. **List the project root.** Run `ls` on the project root directory. This establishes the ground truth of what directories exist. It takes one command and prevents every file-location failure that follows from skipping it.

2. **Identify the authoritative module directories.** The canonical v5.x structure is:
   - `/discovery` — tier and entity discovery sub-procedures (v5.x)
   - `/schemas` — entity schemas (v5.x)
   - `/vocabularies` — controlled vocabularies (v5.x)
   - `/normalization` — normalization contracts (v5.x)
   - `/output` — TSV output specifications (v5.x)
   - `/processing` — pipeline and resolution modules (v5.x)
   - `/audit` — audit and logging modules (v5.x)

3. **Read the module manifest.** Read the highest-versioned `na_module_manifest_v5.*.md` at the project root. The manifest lists the current canonical filename — including version number — for every module. Use the manifest to determine which exact file to read. Do not use memory, the skill text, or a session summary to determine module filenames.

4. **Never read from non-authoritative locations.** Files in the following locations are not authoritative and must never be used as procedure or schema references:
   - `deprecated/` — superseded modules; retained for history only
   - `Natural Areas supplelmental files/` — legacy v4 reference material
   - Any path whose directory components include a version number lower than the current project version

5. **Target directories directly. Do not use broad Glob patterns.** Broad patterns (`**/*.md` across the full project tree) surface deprecated copies before authoritative ones and produce truncated result sets that hide correct files. The correct workflow is: read the manifest → get the exact filename → read that file from its canonical directory. This is never slower than a Glob and is always correct.

**This protocol applies equally to new sessions and resumed sessions.** A session summary or handoff that references a module by name is not a substitute for reading the module from disk at the correct path. Session summaries compress content and may contain stale version references. The manifest and the files in the authoritative directories are the only ground truth.

---

## Source Authority Hierarchy (IMP-078)

Protocol documents and sub-procedures are the **sole authoritative source** for what to do and how to do it. The following precedence order is absolute and cannot be overridden:

1. **Protocol modules and sub-procedures** — authoritative for all rules, procedures, and required steps
2. **The handoff document** — a progress tracker only; records where you are, not what the rules are
3. **Session memory, prior context, and summaries** — have no protocol authority; must never override modules

When any two of these conflict, the higher-authority source wins without exception. The handoff may say "Tier 5 complete" but if the sub-procedure's mandatory steps are not evidenced in the staging file, Tier 5 is not complete. Session memory may recall how a prior county handled something, but the module — not memory — governs.

This hierarchy applies to resumed sessions and new sessions equally.

---

## Resumed Session Protocol (IMP-074)

**Before touching any data or staging files in a resumed session:**

0. **Execute IMP-112 (Project Orientation Protocol) first.** List the project root, confirm the authoritative directory structure, and read the module manifest to establish current filenames. Do not proceed past this step on the basis of memory or session summaries alone.
1. Read **Discovery Orchestration Module §6** (authoritative tier order)
2. Verify that the current tier label in the handoff matches the canonical tier order in §6
3. If they disagree, the module wins without exception — correct the handoff before proceeding
4. At every tier transition, state explicitly: *"I am about to begin Tier N — [canonical name per §6]."* This makes compliance visible and auditable

The handoff's tier labels are confirmed against the module, never trusted independently. A handoff that says "T5 = City of Defiance" is wrong if §6 says Tier 5 = Township. Fix the label; do not proceed under the wrong tier number.

---

## Core Rules

**FETCH BEATS SEARCH**: Always web_fetch official pages. Never rely on search snippets alone.
**VIEW MAPS DIRECTLY**: Open Google Maps and view the location. Do not search for map references.
**EXHAUSTIVE BEATS EFFICIENT**: Complete every tier 100% before advancing.
**DOCUMENT NEGATIVES**: Record "no entities found" with evidence. Never assume.
**STAGING FILE IS THE RECORD**: Append each entity immediately. Chat history is not a record.
**HANDOFF IS THE INTER-SESSION RECORD**: Any structured table from an authoritative source (parks list with addresses, preserve inventory, municipality list) must be written to the handoff's Captured Source Data section at fetch time. The staging YAML holds the entity records; the handoff holds the source data. Both are needed. A session that ends between discovery and staging loses all source data unless it was written to the handoff.

---

## Discovery Is Collection Only

During discovery, collect raw values exactly as found:
- No normalization of names, types, or categories
- No correction of spelling or formatting
- No inference of missing values
- No population of `township` or `municipality` — GIS-derived only
- No invention of GPS coordinates — only record what authoritative sources explicitly state
- No assessment of difficulty or accessibility — only record what sources state

---

## Eight-Tier Sequence

**Mandatory tier-transition checkpoint (IMP-075)**: Before beginning any tier, **read (or re-read) the authoritative sub-procedure for that tier**. This is not optional and cannot be substituted with session memory, handoff summaries, or prior context. The sub-procedure contains mandatory steps that are easy to miss from memory and costly to remediate. This applies to resumed sessions and new sessions equally.

Execute tiers in order. Complete all six entity types per tier before advancing.

| Tier | Governance Level | Sub-Procedure |
|------|-----------------|---------------|
| 1 | Federal & Tribal | `na_fed_tribal_discovery_subproc.md` |
| 2 | State | `na_state_discovery_subproc.md` |
| 3 | District (Metroparks, conservancy districts) | `na_district_discovery_subproc.md` ⚠️ **Read §3.0 first — Ohio Auditor pre-enumeration is the mandatory first step before any other source** |
| 4 | County | `na_county_discovery_subproc.md` — **for covered counties (DEL, FAI, FAY, FRA, HOC, KNO, LIC, LOG, MAD, MAR, MRW, PER, PIC, ROS, UNI): cross-reference `Parks_and_Open_Space_7241389496048841555.csv` to confirm county-managed entities are captured** |
| 5 | Township | `na_township_discovery_subproc.md` — **Ohio: enumerate townships from `Townships_Officials2022-2023.xlsx` before searches; use Website column for trustee/fiscal officer pages as primary discovery source** |
| 6 | Municipal (cities and villages) | `na_municipal_discovery_subproc.md` — **for covered counties: cross-reference `Parks_and_Open_Space_7241389496048841555.csv` (filter by Jurisdiction) to confirm municipal entities are captured before closing the tier** |
| 7 | Conservancy & Land Trust | `na_conservancy_discovery_subproc.md` |
| 8 | Private | `na_private_discovery_subproc.md` |

---

## Entity Type Sequence Within Each Tier

Discover in this order within each tier:
1. Sites
2. Trails
3. Trail Segments
4. Trail Networks
5. Site Networks
6. Access Points

This ordering ensures Sites and Trails exist before Access Points need to reference them as parents.

**Every entity type requires a documented result before the tier is complete** — either confirmed entities with records, or a confirmed null with evidence and sources checked. Silence is not a null. An undocumented entity type within a tier is a process failure, the same as an undocumented tier.

---

## Entity Discovery Sub-Procedures

Read each subproc to determine whether that entity type applies — not only after finding examples. The subproc defines the criteria for existence. Reading it is how you decide whether to create entities, not a reward for having already found some.

- `na_site_discovery_subproc.md`
- `na_trail_discovery_subproc.md`
- `na_trail_segment_discovery_subproc.md` — defines when named/operational segments exist; read §6 before concluding null
- `na_trail_network_discovery_subproc.md` — defines what makes a multi-trail network vs. a single long trail; read §6 before concluding null
- `na_site_network_discovery_subproc.md` — defines system-level identity threshold; err on inclusion for gray-area cases; read §3 before concluding null
- `na_access_point_discovery_subproc.md`
- `na_water_trail_discovery_subproc.md` — **read for any county with navigable waterways or ODNR/EPA scenic river designations, regardless of whether a paddling trail has been found**; defines Water Site vs. Trail entity typing, qualification threshold, Trail Segment triggers, and Access Point rules specific to water; read §2 before concluding null for Water Sites, §3 before concluding null for water Trails

---

## Per-Entity-Type Null Documentation

Trail Segments, Trail Networks, and Site Networks are the entity types most commonly left undocumented. They have lower base rates than Sites and Trails, which makes it tempting to skip them silently — but silent skipping produces a broken record with no evidence of having checked.

Before concluding null for any of the three, you must:
1. Read the relevant subproc's criteria section (§6 for segments and networks, §3 for site networks)
2. Check at least two sources for evidence of the entity type at the current tier
3. Record what was checked and why null was concluded

Required null format for these entity types:

```yaml
entity_type_result:
  tier: [number]
  governance_level: [name]
  entity_type: Trail Segment | Trail Network | Site Network
  result: null
  sources_checked:
    - [URL or source description]
    - [URL or source description]
  reasoning: [specific evidence for null — e.g., "Trail treated as single unit by manager; no named or GIS-defined segments in any source"]
```

This block can appear inline within the tier's staging notes or in the session log. What matters is that it exists and is specific — not just "none found."

---

## Raw Discovery Record — Key Fields (v5.2)

Every raw discovery record must include:

```yaml
entity_type:          # Site | Trail | Trail Segment | Trail Network | Site Network | Access Point
name_raw:             # exactly as found
counties_raw: []      # all counties, exactly as found
county_primary:       # county currently being processed
ownership_raw:        # exactly as found
governance_raw:       # exactly as found
partner_agencies_raw: # exactly as found
coordination_raw:     # exactly as found
gps_lat_raw:          # only if explicitly stated by authoritative source
gps_lon_raw:          # only if explicitly stated by authoritative source
location_raw:         # Sites and Access Points only
description_raw:      # Sites and Access Points only — narrative prose, verbatim from source
features_raw:         # Sites and Access Points only — amenity/facility LIST, verbatim from source
difficulty_raw:       # Trails and Trail Segments only
accessibility_raw:    # Trails and Trail Segments only
urls_raw: []          # ALL urls including maps, PDFs, GIS viewers
identity_notes_raw:   # identity clarifications, conflicts, uncertainty flags
township_raw:         # BLANK — GIS-derived only
municipality_raw:     # BLANK — GIS-derived only
discovery_tier:       # integer 1-8
seeded_from_baseline: # true | false
baseline_id:          # if baseline-seeded
```

Note: `gps_raw` is retired. Always use `gps_lat_raw` and `gps_lon_raw` as separate fields.
Note: `notes_raw` is retired. Use `identity_notes_raw`.
Note: `maps_raw` is retired. Map URLs go into `urls_raw`.

---

## Description vs. Features — Required Distinction

These two fields capture different things from the same source page and must never be conflated:

**`description_raw`** — Narrative prose about the Site. Complete sentences. Usually an "About," "Overview," or introductory paragraph on the park page or in a brochure.
- ✓ "Griggs Reservoir Park is a 393-acre greenway along the Scioto River offering fishing, hiking, and scenic views of the reservoir."
- ✓ "Established in 1975, this nature preserve protects one of central Ohio's last intact upland oak-hickory forests."
- ✗ "Picnic shelters, restrooms, fishing" ← that's features_raw, not description_raw

**`features_raw`** — List of amenities and physical features. NOT sentences. Usually icons, bullets, or a "Facilities" or "What's Here" section.
- ✓ "Picnic shelter, restrooms, fishing pond, playground, dog park off-leash area"
- ✓ "Parking; ADA accessible trails; Boat ramp; Restrooms; Covered shelter"
- ✗ "This park features a large playground and restrooms for visitor convenience." ← that's description_raw, not features_raw

**Key rule**: The Normalization Engine maps `features_raw` tokens to controlled vocabulary. Capture raw — do not attempt to normalize during discovery. Narrative sentences cannot be mapped to vocabulary; they belong in `description_raw`.

**Governance contamination rule**: `governance_raw` must contain only the managing organization's name. GIS park type labels (e.g., "Community Park," "Neighborhood Park") are NOT governance — never append them to `governance_raw`. Record them in `category_raw` or `identity_notes_raw`.

---

## First-Pass Capture Rule

When fetching a park page, extract ALL available fields in a single pass:
- `description_raw` (narrative paragraph, if present)
- `features_raw` (amenity list, if present)
- `location_raw`, `acres_raw`, `urls_raw`

Both fields are typically on the same page. **Do not return to a source already fetched to collect fields that were available on first visit.** A return visit for missed fields is a process failure. See `na_site_discovery_subproc.md` §7.3 for full guidance.

---

## Null Tier Results

When a tier yields zero entities across all types, record explicitly:

```yaml
tier_result:
  tier: [number]
  governance_level: [name]
  result: null
  entities_found: 0
  sources_checked: [list what was searched and fetched]
  notes: [what evidence supports the null result]
```

When a tier yields entities of some types but not others, document the null entity types separately using the per-entity-type null format above. Do not leave any entity type undocumented just because the tier itself was productive for Sites or Trails.

Never leave a tier undocumented. A null result with evidence is valid. An undocumented tier is not.

**DEFECT status (IMP-076)**: If a tier was worked but under the wrong protocol, with missing mandatory steps, or with work left incomplete, mark it **DEFECT** — not complete. In the staging file, add a comment block:

```yaml
tier_defect:
  tier: [number]
  deviation: [specific description of what protocol was bypassed or missed]
  remediation_required: [specific sub-procedure sections that must be re-run]
```

In the handoff, mark the tier as `PENDING` (not COMPLETE) with the exact remediation steps listed. Carrying a defective tier forward as "done" or "mostly done" is a protocol violation. The staging file comment and handoff status must make the remediation path unambiguous to a fresh session.

---

## Tier Close Verification — Physical File Check (IMP-080)

Before closing any tier, **physically verify** that every result block is present in the staging YAML file. Do not rely on session context, chat references, or memory.

**Required check before marking any tier complete:**
1. Read or grep the staging YAML file
2. Confirm every entity type that should have a result (entities or null evidence block) is actually present with the correct YAML structure
3. Specifically: null result blocks must have `entity_type_result:` and `result: null` fields actually in the file — not just described in chat

"I staged it above" is not a substitute for verifying the content exists on disk. The staging file is the record; chat history is not. A tier is not closeable until all documented results can be read back out of the YAML.

## Cross-County Candidate Flagging (IMP-104)

**Required check when closing any discovery tier.**

When closing any tier, scan all entities staged in that tier: if any entity's `counties_raw`
field lists more than one county, verify that `identity_notes_raw` contains either
`CROSS_COUNTY_CANDIDATE` or `KNOWN_MC:{existing_id}` before the tier is marked complete.

**When to flag `CROSS_COUNTY_CANDIDATE`:**
- Entity's counties_raw lists two or more counties
- No existing DB record has already been assigned an MC ID for this entity

**When to flag `KNOWN_MC:{id}` instead:**
- A prior county run already discovered this entity and assigned it a cross-county ID
- Use the existing ID: e.g., `KNOWN_MC:MC-T-0001`

**When NOT to flag** (read `processing/na_cross_county_resolution.md` §6 for full rules):
- Generic names at genuinely separate installations (e.g., two unrelated "Veterans Park" in adjacent counties)
- Single-county parks whose boundary briefly crosses a county line with no meaningful presence in the second county

Before closing any tier with multi-county entities, read **`processing/na_cross_county_resolution.md` §6**
for the full flagging rules and the collision detection procedure.

## Staging Append Safety — Key-Targeted Writes (IMP-079)

Staging YAML files have multiple top-level keys: `records:`, `tier_6_entity_type_results:`, `tier_null_results:`, and others. **Never append T7/T8 entities (or any records after T6 work is staged) by text position using the Edit tool.** Text-position-based appends place content under whichever key ends the file — which is frequently the wrong one.

**Required approach for all record appends after T6:**

```python
import yaml, pathlib
f = pathlib.Path("county_oh_raw_discovery.yaml")
data = yaml.safe_load(f.read_text())
# Verify target key before writing
print("Top-level keys:", list(data.keys()))
data.setdefault("records", [])
data["records"].append({ ... new record dict ... })
f.write_text(yaml.dump(data, allow_unicode=True, sort_keys=False))
```

This failure mode is subtle — the append succeeds (no error), but the record is silently routed under the wrong key and won't be picked up by the pipeline. A Python restructuring pass is required to repair it. Always target `records:` by key name, not by file position.

## Baseline Seed Tracking

As you discover entities, check them against baseline seeds:
- When a discovered entity matches a baseline seed, record `seeded_from_baseline: true` and the `baseline_id`
- Mark the seed as confirmed in the session log
- At tier completion, note which seeds remain unconfirmed
- Unconfirmed seeds at the end of all tiers are flagged for review — not automatically included in output

## Municipal Tier — Critical Rules

The municipal tier (Tier 6) is the most common source of missed entities:

- Never skip a village because it seems too small
- Never mark a village as 0 parks without map-based verification
- Always view Google Maps directly for each municipality — do not search for map references
- Official municipal websites are often incomplete or outdated — verify independently with maps
- If browser tools are unavailable, mark the municipality as PENDING/UNVERIFIED — never mark complete without verification

## Cross-County Entities

Entities spanning multiple counties (trail networks, site networks, metropark systems):
- Record all counties in `counties_raw`
- Discover and record the entity fully at its governance tier
- Member IDs will be blank or partial — this is correct and expected
- Do not hold up tier completion waiting for member resolution
- The pipeline will hold these entities pending cross-county resolution

## GPS During Discovery

**Primary rule**: Only record GPS if an authoritative source (official website, ODNR, USGS, etc.) explicitly provides coordinates. Never invent or infer GPS.

**Map verification exception (IMP-031)**: During mandatory map verification passes, when you open a Google Maps entity detail card to confirm an entity's identity, capture the GPS coordinates from the page URL at the same time. The URL format `@LAT,LON,ZOOMz` contains decimal coordinates.

- Record these in `gps_lat_raw` / `gps_lon_raw`
- Note in `identity_notes_raw`: `"GPS from Google Maps detail card during map verification — treat as approximate until GPS acquisition pass confirmation"`
- Also write to the handoff's Captured Source Data table

This converts the map verification pass into a partial GPS acquisition pass. For most Tier 6 entities, this eliminates the need for a dedicated GPS return pass, since the detail card is opened anyway to confirm address/phone/identity.

**Blank GPS is still correct** when map verification did not open a detail card. The GPS Acquisition Module handles remaining missing coordinates downstream.

## Supplemental Authorities — Ohio (IMP-096, IMP-097)

These files are project-root references available for all Ohio county runs. They do not replace tier sub-procedures — they supplement them at specific steps.

### `Townships_Officials2022-2023.xlsx` — Ohio Township Roster (IMP-096)

- **Scope**: All 88 Ohio counties, 1,307 active townships
- **Use in bootstrap**: Filter by County Name to enumerate the canonical township list before Tier 5 begins (see Bootstrap Step 3)
- **Use in Tier 5**: The Website column provides trustee/fiscal officer URLs — these are the primary discovery sources for township-managed parks and open spaces. Use them before generic web searches.
- **Defunct detection**: A township absent from this roster is a defunct candidate — follow the four-step confirmation procedure in Township Discovery Subproc §3.1a (IMP-005) before closing as defunct.

### `Parks_and_Open_Space_7241389496048841555.csv` — 15-County Regional GIS Layer (IMP-097)

- **Scope**: DEL, FAI, FAY, FRA, HOC, KNO, LIC, LOG, MAD, MAR, MRW, PER, PIC, ROS, UNI — updated July 2025
- **Fields**: Type, Name, Jurisdiction, County, Sub_Type, Status, Acres, Source
- **Use in Tier 4 (County)**: Filter by County to get a county-managed entity roster. Cross-reference against discovered sites before closing the tier.
- **Use in Tier 6 (Municipal)**: Filter by Jurisdiction (matches city/village names). Use as a completeness check — any entry not matched to a discovered entity requires investigation.
- **Limitations**: No GPS coordinates in this file. Does not replace web-based discovery; use as a cross-check after primary discovery is complete. Sub_Type vocabulary differs from NAP vocabulary — do not map Sub_Type values directly to NAP category or subtype fields.
- **Quality gate**: This file is also used post-pipeline as a completeness gate in na-quality (see Parks & Open Space Completeness Gate section).

---

## After All Tiers Complete

Before d