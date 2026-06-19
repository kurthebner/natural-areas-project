---
name: na-discovery
description: Executes tier-based discovery of natural areas entities across U.S. counties. Triggers on discover, find parks, catalog entities, tier discovery, or any mention of searching for natural areas in a location.
---

# Natural Areas Project — Discovery Skill v5.5

## CHANGES FROM v5.4 → v5.5

- **IMP-021 — Explicit trail use/surface fields**: Added `trail_use_type_raw` and `trail_surface_type_raw` to the Raw Discovery Record key fields. Both are Preferred for Trail and Trail Segment entities. Embedding use/surface info in `accessibility_raw` as a combined string is an anti-pattern; explicit fields are required when the source states them.
- **IMP-022 — Category field standardization**: Added category field canonicalization rule. `category_raw` is the single authorized field name for site/entity category. `park_type_raw` and `site_type_raw` are deprecated and must not appear in new staging records.
- **IMP-024 — YAML staging: colon quoting**: Added YAML staging format rule requiring all field values containing a colon to be quoted. Unquoted colons in YAML values cause parse errors.
- **IMP-025 — YAML staging: record separators**: Added YAML staging format rule requiring `---` document separators between every discovery record in a staging file.

## CHANGES FROM v5.3 → v5.4

- **IMP-027 — Features staging prohibition**: Added explicit rule that the normalized `features` field must never be written during discovery. Only `features_raw` belongs in staging records. Placeholder strings (e.g., "GIS-documented; amenities require individual verification") are prohibited in `features_raw`.
- **IMP-028 — MORPC import governance contamination**: Added MORPC-specific import field-mapping note to the governance contamination rule. GIS park type metadata from MORPC or any GIS layer must go to `category_raw` or be discarded — never appended to `governance_raw`.
- Updated tier sub-procedure references to current versions.
- Updated entity sub-procedure references to current versions.

Executes systematic discovery across all eight tiers for all six entity types.

## Core Rules

**FETCH BEATS SEARCH**: Always web_fetch official pages. Never rely on search snippets alone.
**VIEW MAPS DIRECTLY**: Open Google Maps and view the location. Do not search for map references.
**EXHAUSTIVE BEATS EFFICIENT**: Complete every tier 100% before advancing.
**DOCUMENT NEGATIVES**: Record "no entities found" with evidence. Never assume.
**STAGING FILE IS THE RECORD**: Append each entity immediately. Chat history is not a record.

## Discovery Is Collection Only

During discovery, collect raw values exactly as found:
- No normalization of names, types, or categories
- No correction of spelling or formatting
- No inference of missing values
- No population of `township` or `municipality` — GIS-derived only
- No invention of GPS coordinates — only record what authoritative sources explicitly state
- No assessment of difficulty or accessibility — only record what sources state

## Eight-Tier Sequence

Execute in order. Complete all six entity types per tier before advancing.

| Tier | Governance Level | Sub-Procedure |
|------|-----------------|---------------|
| 1 | Federal & Tribal | `na_fed_tribal_discovery_subproc_v5.x.md` |
| 2 | State | `na_state_discovery_subproc_v5.x.md` |
| 3 | District (Metroparks, conservancy districts) | `na_district_discovery_subproc_v5.x.md` |
| 4 | County | `na_county_discovery_subproc_v5.x.md` |
| 5 | Township | `na_township_discovery_subproc_v5.x.md` |
| 6 | Municipal (cities and villages) | `na_municipal_discovery_subproc_v5.x.md` |
| 7 | Conservancy & Land Trust | `na_conservancy_discovery_subproc_v5.x.md` |
| 8 | Private | `na_private_discovery_subproc_v5.x.md` |

## Entity Type Sequence Within Each Tier

Discover in this order within each tier:
1. Sites
2. Trails
3. Trail Segments
4. Trail Networks
5. Site Networks
6. Access Points

This ordering ensures Sites and Trails exist before Access Points need to reference them as parents.

## Entity Discovery Sub-Procedures

Read when discovering that entity type:
- `na_site_discovery_subproc_v5.x.md`
- `na_trail_discovery_subproc_v5.x.md`
- `na_trail_segment_discovery_subproc_v5.x.md`
- `na_trail_network_discovery_subproc_v5.x.md`
- `na_site_network_discovery_subproc_v5.x.md`
- `na_access_point_discovery_subproc_v5.x.md`

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
trail_use_type_raw:   # Trails and Trail Segments — PREFERRED; capture explicitly when source states it
trail_surface_type_raw: # Trails and Trail Segments — PREFERRED; capture explicitly when source states it
difficulty_raw:       # Trails and Trail Segments only
accessibility_raw:    # Trails and Trail Segments only — ADA/accessibility statements; NOT use or surface type
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
Note: `park_type_raw` and `site_type_raw` are retired. Use `category_raw`. See below.

## Category Field Canonicalization (IMP-022)

`category_raw` is the single authorized field name for entity category across all entity types and all tiers. Do not use `park_type_raw`, `site_type_raw`, or any other variant.

- `category_raw: "Nature Preserve"` ✓
- `park_type_raw: "Nature Preserve"` ✗ — deprecated, will cause extraction failure
- `site_type_raw: "Nature Preserve"` ✗ — deprecated, will cause extraction failure

If an older staging file or session log uses these deprecated field names, flag it for repair before pipeline processing.

## YAML Staging Format Rules

### Colon Quoting (IMP-024)

Any field value that contains a colon **must** be enclosed in quotes. Unquoted colons are interpreted as YAML key-value separators and will cause parse errors.

```yaml
# CORRECT
governance_raw: "City of Dublin"
identity_notes_raw: "Source: MORPC Parks layer; verified 2026-03"

# WRONG — unquoted colon causes parse error
governance_raw: City of Dublin; GIS park type: Community Park
```

This applies to every field in every staging record, regardless of tier or entity type.

### Record Separators (IMP-025)

Every discovery record in a staging file **must** be preceded by a `---` document separator. Omitting separators between records causes YAML block-end parse errors when multiple records are concatenated in a single file.

```yaml
---
entity_type: Site
name_raw: "Griggs Reservoir Park"
...

---
entity_type: Site
name_raw: "Antrim Park"
...
```

Always begin a new `---` separator when appending a new entity to an existing staging file, even when adding to a tier that already has records. Never rely on indentation alone to delimit records.

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

**Staging field prohibition (IMP-027)**: During discovery, write ONLY to `features_raw` — never to `features`. The normalized `features` field is populated exclusively by the Normalization Engine from controlled vocabulary tokens. Writing to `features` directly during staging bypasses normalization and will produce schema violations.

Additionally, `features_raw` must contain real amenity list items from the source — never placeholder text such as "GIS-documented; amenities require individual verification." If the source does not provide an explicit amenity list, leave `features_raw` blank and note the gap in `identity_notes_raw`.

**Governance contamination rule**: `governance_raw` must contain only the managing organization's name. GIS park type labels (e.g., "Community Park," "Neighborhood Park") are NOT governance — never append them to `governance_raw`. Record them in `category_raw` or `identity_notes_raw`.

**MORPC import field mapping (IMP-028)**: When importing from the MORPC Parks & Open Space layer (or any GIS source that provides both managing organization and park type):
- `governance_raw`: organization name only — e.g., `City of Dublin` ✓
- `category_raw`: GIS park type label — e.g., `Community Park` ✓
- `governance_raw`: combined string — e.g., `City of Dublin; GIS park type: Community Park` ✗

GIS park type is a category hint. It must never be appended to `governance_raw` under any circumstances, including batch import scripts.

## First-Pass Capture Rule

When fetching a park page, extract ALL available fields in a single pass:
- `description_raw` (narrative paragraph, if present)
- `features_raw` (amenity list, if present)
- `location_raw`, `acres_raw`, `urls_raw`

Both fields are typically on the same page. **Do not return to a source already fetched to collect fields that were available on first visit.** A return visit for missed fields is a process failure. See `na_site_discovery_subproc_v5.x.md` §7.3 for full guidance.

## Null Tier Results

When a tier yields zero entities, record explicitly:

```yaml
tier_result:
  tier: [number]
  governance_level: [name]
  result: null
  entities_found: 0
  sources_checked: [list what was searched and fetched]
  notes: [what evidence supports the null result]
```

Never leave a tier undocumented. A null result with evidence is valid. An undocumented tier is not.

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

- Only record GPS if an authoritative source explicitly provides coordinates
- Never derive GPS from maps, proximity, or inference during discovery
- Never record GPS from Google Maps pin locations unless the authoritative source confirms those coordinates
- Blank GPS is correct and expected — GPS Acquisition Module handles missing coordinates downstream

## After All Tiers Complete

1. Confirm all baseline seeds are confirmed or flagged
2. Confirm all tiers have results (including null results with evidence)
3. Update the handoff document
4. Pass staging file to Resolution via na-pipeline skill
