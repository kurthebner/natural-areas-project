# NATURAL AREAS PROJECT
# TRAIL NETWORK DISCOVERY SUB-PROCEDURE v5.2
(Authoritative Sub-Procedure for Discovering Trail Networks)

This module defines the authoritative, deterministic workflow for discovering
**Trail Networks** across all discovery tiers within the v5.x
Raw → Resolution → GPS Acquisition → Normalization → Entity Graph pipeline.

This document supersedes all v5.0, v5.1, and v4.x Trail Network discovery logic.

------------------------------------------------------------
# CHANGES FROM v5.1 → v5.2

- **IMP-046 — Multi-county Trail Network "held entity" creation pattern**: Added
  §17 Multi-County Trail Network Protocol documenting when to create the network
  record, how to document partial membership at first encounter, and how to update
  the network when subsequent county sessions process additional member trails.
  Pattern: create the network entity during the first county session that encounters
  it; populate `member_trail_names_raw` with only the trails documented so far and
  note explicitly in `identity_notes_raw` that the list is partial. The network TSV
  lives in the first county's spreadsheet folder. When subsequent counties are
  processed, they append entries to `trail_network_members` and update
  `member_trail_ids`; no new network TSV row is created.

------------------------------------------------------------
# CHANGES FROM v5.0 → v5.1

- **Field renames**:
  - notes_raw → identity_notes_raw (identity clarifications and flags)
  - url_all → urls_raw (all URLs)
  - url_primary → url_primary_raw
  - maps_raw remains but is now explicitly a plain URL list (was
    described as a rich array in v5.0 — type and description metadata
    no longer collected)
- **identity_notes_raw section added**: explicit extraction guidance
  for the renamed field and its normalized counterpart
- **maps_raw guidance updated**: simplified to URL-only collection;
  no type/description metadata; all map-type URLs collected together
- **All cross-module references updated to v5.x**

------------------------------------------------------------
# CHANGES FROM v4.0 → v5.0

- Philosophy clarified: Discovery = Collection, Normalization = Decisions
- Source mapping added: Track which fields came from which URLs
- Field changes: Added status, ownership, total_length_miles,
  member_trail_count, member_trail_ids, maps array
- Governance terminology: managing_agency_raw → governance_raw;
  added partner_agencies_raw
- Complete rewrite: Enhanced practical guidance for discoverers

------------------------------------------------------------
# 1. PURPOSE

The Trail Network Discovery Sub-Procedure v5.1 provides the authoritative
workflow for:

- Identifying Trail Network candidates
- Extracting raw, unnormalized metadata
- Supporting enumerative and recursive discovery
- Preventing misclassification across the six-entity ontology
- Recording tier and URL provenance with field-level source mapping
- Emitting Raw Discovery Records v5.x
- Emitting Discovery Metadata v5.x
- Integrating cleanly with Trail, Trail Segment, and Site Network
  discovery
- Feeding the Resolution Engine v5.x

A **Trail Network** is:

- A named, identity-bearing umbrella entity
- Composed of multiple Trails
- Documented in authoritative sources
- Distinct from its member Trails
- Not a marketing label or informal grouping
- Not a single Trail with multiple Segments

This module is authoritative for Trail Network discovery.

------------------------------------------------------------
# 2. DISCOVERY PHILOSOPHY (v5.x)

## 2.1 Core Principle: Discovery = Collection, Normalization = Decisions

**Discovery Phase (YOU ARE HERE):**
- Collect everything you find
- Record exactly as found
- Don't normalize, standardize, or choose between values
- Don't deduplicate URLs or map links
- Don't make vocabulary decisions
- Fast, mechanical extraction

**Normalization Phase (LATER):**
- Standardize vocabulary
- Deduplicate URLs and maps
- Choose canonical values
- Validate member trail relationships
- Populate member_trail_ids

## 2.2 When in Doubt: Collect It

If uncertain whether to include something:
- Include it
- Record uncertainty in identity_notes_raw
- Let Resolution/Normalization decide

## 2.3 Multiple Sources = Multiple Records

If you find the same Trail Network at multiple URLs:
- Emit SEPARATE discovery records
- Do NOT attempt to merge
- Resolution engine handles merging

------------------------------------------------------------
# 3. SCOPE

This sub-procedure applies to all discovery tiers:

1. Federal
2. State
3. District
4. County
5. Township
6. Municipal
7. Conservancy
8. Private
9. Tier-0 Baseline (non-authoritative; runs last)

------------------------------------------------------------
# 4. REQUIRED SOURCES

Each tier must check the following for Trail Network references:

- Official agency websites
- Authoritative listing/index pages
- GIS systems and interactive trail maps
- Regional trail plans
- Greenway or bikeway master plans
- Statewide trail system documents
- National Trail System documentation
- Multi-trail corridor plans
- Partnership announcements
- Regional mobility or recreation initiatives
- Multi-trail branding or signage programs
- Trail system overview maps
- Network-level GPX/KML files

All sources must be logged in **Discovery Metadata v5.x** and
**source_map**.

------------------------------------------------------------
# 5. IDENTITY RULES FOR TRAIL NETWORK CANDIDATES

A Trail Network candidate is valid only if:

1. It is explicitly documented as a **multi-trail system**.
2. It has a **stable, identity-bearing name**.
3. It is composed of **two or more Trails**.
4. It is distinct from its member Trails.
5. It is not merely a marketing label or informal grouping.
6. It is not a Site Network.
7. It is not a single Trail with multiple Segments.

If any condition fails, the candidate must not be created.

------------------------------------------------------------
# 6. TRAIL NETWORK VS. TRAIL: CRITICAL DISTINCTION

## 6.1 When Is Something a Trail Network?

**Trail Network (umbrella over multiple trails):**
- ✅ Composed of multiple named trails with their own identities
- ✅ Described as a "system", "network", or collection of trails
- ✅ Sources list multiple trails as part of this entity

**Individual Trail (not a network):**
- ❌ A single named trail with multiple segments
- ❌ A trail that is very long or multi-county
- ❌ A trail described as a "trail" even if part of a system

**Key questions:**
1. Does it have member trails with their own names?
2. Is it described as a system or network?
3. Do sources list multiple trails as part of this entity?

If YES → Trail Network. If NO → Individual Trail.

## 6.2 Ambiguous Cases

When a named entity could be either a Trail or Trail Network:
- Flag in identity_notes_raw
- Let Resolution/Normalization decide
- If sources consistently treat it as single trail → Trail
- If sources treat it as multi-trail system → Trail Network

------------------------------------------------------------
# 7. DISCOVERY WORKFLOW

## 7.1 Step 1 — Identify Named Multi-Trail Systems

Search all required sources for:

- Regional trail networks
- Greenway systems
- Bikeway networks
- Multi-trail corridors
- Statewide trail systems
- National Trail System components
- County or municipal trail networks
- Multi-trail recreation or mobility networks

## 7.2 Step 2 — Verify Identity-Bearing Name

Must have a documented, stable name. Not a temporary project
name, marketing slogan, or informal grouping. Flag in
identity_notes_raw if ambiguous.

## 7.3 Step 3 — Confirm Multi-Trail Composition

Must include two or more Trails with documented membership.

**Do not infer membership:**
- Only record trails explicitly listed as members
- Don't guess which trails belong
- Normalization validates relationships

------------------------------------------------------------
# 8. FIELD-BY-FIELD EXTRACTION GUIDE

## 8.1 Core Identity Fields

### `network_name_raw` (REQUIRED)
Official published name exactly as written.

**Examples:**
- "Ohio to Erie Trail" ✅
- "Cleveland Metroparks All-Purpose Trail System" ✅

---

### `network_type_raw` (OPTIONAL)
Record exactly as source describes. Don't normalize vocabulary.

**Examples of source terms to capture:**
- "regional greenway system", "county trail network",
  "statewide trail system", "water trail network"

---

### `status_raw` (OPTIONAL)
Only if explicitly stated. "Partial" or "Partially Open" is
especially important for Trail Networks.

**Examples:**
- "under development" → record "under development"
- "partially complete" → record "partially complete"

## 8.2 Physical Characteristics

### `total_length_miles_raw` (OPTIONAL)
Total length of entire network as published.

**Examples:**
- "Ohio to Erie Trail spans 326 miles" → record "326"
- "System includes 45 miles of trails" → record "45"

**Never:**
- ❌ Calculate by adding member trail lengths
- ❌ Estimate from maps

---

### `member_trail_count_raw` (OPTIONAL)
Published count of member trails.

**Examples:**
- "System includes 12 trails" → record "12"

**Never:**
- ❌ Count trails yourself from a list
- ❌ Estimate

---

### `member_trail_names_raw` (OPTIONAL)
Names of member trails exactly as listed. Semicolon-delimited.

**Examples:**
- "Towpath Trail;Slippery Elm Trail;University Parks Trail"

**Record for normalization reference** — normalization resolves
names to trail_ids and populates member_trail_ids.

## 8.3 Governance Fields

### `governance_raw` (OPTIONAL)
Primary coordinating agency or organization.

**Examples:**
- "Buckeye Trail Association"
- "Rails-to-Trails Conservancy"
- "Ohio Department of Natural Resources"

---

### `partner_agencies_raw` (OPTIONAL)
Secondary managing agencies or partner organizations. Semicolon-
delimited. Only if explicitly documented.

**Look for:** "in partnership with...", "co-managed by..."

---

### `ownership_raw` (OPTIONAL)
Legal owner of the network if applicable. Often blank for
coordinating bodies.

**Ownership vs. Governance:**
- Ownership = who legally owns the corridor or land
- Governance = who manages or coordinates
- Many networks are coordinating bodies — blank ownership is
  correct and common

## 8.4 Location Fields

### `counties_raw` (OPTIONAL)
All counties the network traverses. Semicolon-delimited.

**Example:** "Wood;Lucas;Ottawa;Sandusky;Erie"

---

### `states_raw` (OPTIONAL)
States traversed. For multi-state networks only. Leave blank for
Ohio-only networks. Semicolon-delimited.

**Example:** "Ohio;Pennsylvania;New York"

## 8.5 Identity Notes Field

### `identity_notes_raw` (OPTIONAL)
Free-text field for identity clarifications and uncertainty flags.

**Use for:**
- Network vs. trail boundary questions:
  "Source alternately calls this a 'trail' and a 'trail system'
  — unclear if Trail or Trail Network; flag for review"
- Name conflicts:
  "Source uses 'Ohio to Erie Trail' and 'OTE Trail' — cannot
  determine which is official"
- Membership uncertainty:
  "Source lists 'approximately 12 trails' without naming them
  — partial membership list only"
- Vocabulary type flags:
  "Source calls this a 'trail corridor' — unclear if Trail or
  Trail Network"

**What NOT to put here:**
- ❌ Operational details → notes_raw  (renamed to identity_notes_raw —
  use a separate notes_raw field)
- ❌ Member trail names → member_trail_names_raw
- ❌ Map URLs → maps_raw

**Note on field naming:** At discovery stage, identity clarifications
go in `identity_notes_raw`. Operational notes (gap documentation,
planning status, partial completion) go in `notes_raw`. Both are
separate discovery fields.

## 8.6 Notes Field

### `notes_raw` (OPTIONAL)
Operational details, development status, gap information,
partial completion notes.

**Must not include:**
- ❌ Identity clarifications → identity_notes_raw
- ❌ Member trail names → member_trail_names_raw

## 8.7 URL and Map Fields

### `url_primary_raw` (OPTIONAL)
Most authoritative URL for the network — usually the network's
dedicated homepage.

**Examples:**
- https://ohiotoerietrail.org/ ✅
- https://buckeyetrail.org/ ✅

---

### `urls_raw` (OPTIONAL)
ALL URLs where the network is mentioned. Semicolon-delimited.
Don't deduplicate.

---

### `maps_raw` (OPTIONAL)
ALL map URLs for the network — system overview maps, interactive
viewers, GPX files, PDF strip maps, network maps. Semicolon-
delimited plain URL list. No type labels or descriptions.

**Trail Networks are spatial — multiple map types expected:**
- System overview PDF → collect it
- Interactive GIS viewer → collect it
- Network-wide GPX file → collect it
- PDF strip maps by county → collect all

**Format — URLs only, semicolon-delimited:**
```
https://ohiotoerietrail.org/maps/system-map.pdf;https://ohiotoerietrail.org/interactive-map;https://ohiotoerietrail.org/gpx/complete-route.gpx
```

**Don't deduplicate** — Resolution handles deduplication.

## 8.8 Descriptive Fields

### `description_raw` (OPTIONAL)
1-3 sentences describing the network's identity, scope, and
purpose. May include brief establishment history.

**Focus on network-level identity:**
- "326-mile multi-use trail connecting Cleveland, Columbus,
  and Cincinnati"
- "System of 12 interconnected trails spanning three metro
  parks districts"

**Must not include:**
- ❌ Detailed member trail descriptions
- ❌ Access point details

------------------------------------------------------------
# 9. MEMBER TRAIL TRACKING

## 9.1 During Discovery

Record member trail names in `member_trail_names_raw` — exactly
as listed in source, semicolon-delimited. Don't attempt to match
to existing Trail entities.

**Example:**
```
member_trail_names_raw: "Towpath Trail;Slippery Elm Trail;University Parks Trail;Wintergarden Trail"
member_trail_count_raw: "4"
```

## 9.2 During Normalization

Normalization Engine:
- Resolves trail names to trail_ids
- Populates `member_trail_ids` array
- Creates entries in `trail_network_members` relationship table
- Handles name variants and spelling differences

## 9.3 Incomplete Member Lists

When source mentions some trails but not all:
- Record what you find
- Note incompleteness in identity_notes_raw:
  "Source lists 4 trails; network website mentions 'over 15
  trails in system' — partial member list only"
- Later discoveries or sources will add missing members

------------------------------------------------------------
# 10. PROVENANCE TRACKING (v5.x)

## 10.1 Source Mapping (REQUIRED)

For each discovery record, maintain source_map tracking which
fields came from which URLs.

**Format:**
```json
{
  "source_map": {
    "https://ohiotoerietrail.org/": [
      "network_name", "description", "governance", "url_primary_raw"
    ],
    "https://ohiotoerietrail.org/about/": [
      "total_length_miles", "member_trail_count", "member_trail_names",
      "partner_agencies"
    ],
    "https://ohiotoerietrail.org/maps/": [
      "maps_raw", "counties"
    ]
  }
}
```

## 10.2 Multiple Sources = Multiple Records

If you encounter the same network at multiple URLs:
- Emit SEPARATE discovery records
- Each with its own source_map
- Do NOT attempt to merge
- Resolution engine handles merging

------------------------------------------------------------
# 11. WHAT NOT TO DO (CRITICAL)

- ❌ Don't create networks for single trails (even very long ones)
- ❌ Don't create networks for marketing labels or informal
  groupings
- ❌ Don't normalize or standardize field values
- ❌ Don't deduplicate URLs or map links
- ❌ Don't calculate total length from member trails
- ❌ Don't count member trails yourself from lists
- ❌ Don't infer membership from geography or trail names
- ❌ Don't merge records from multiple sources
- ❌ Don't add type/description metadata to maps_raw entries —
  URLs only

------------------------------------------------------------
# 12. SPECIAL CASES

## 12.1 National Trail System

"National Trails System" is a Trail Network (umbrella over
National Scenic Trails, Historic Trails, Recreation Trails).
Each National Scenic Trail (e.g., North Country NST) is itself
a Trail entity — very long, but a Trail, not a network.

## 12.2 Nested Systems

Trail Networks in v5.x contain Trails only — no nested network
structures. "National Trails System" contains "North Country
National Scenic Trail" as a Trail entity, not as a sub-network.

## 12.3 County/Municipal Systems — Trail Network vs. Site Network

**Ask:**
- Does it contain multiple named trails? → Trail Network
- Is it an umbrella over multiple parks/sites? → Site Network
- Both? → Create both entities (they serve different purposes)

**Example — both entities may exist:**
```
Site Network:
  name: "Wood County Park District"
  type: "County Park System"
  member_sites: [Carter Farm, Oak Openings, ...]

Trail Network:
  name: "Wood County Park District Trail System"
  type: "County Trail Network"
  member_trails: [Slippery Elm Trail, ...]
```

## 12.4 Partially Open Networks

Document both the network and its partial status:

```
network_name_raw: "Great Ohio Lake to River Greenway"
status_raw: "partial"
description_raw: "85-mile planned greenway; 23 miles currently open"
notes_raw: "Some sections complete and active; remainder planned"
```

------------------------------------------------------------
# 13. TIER-SPECIFIC EXPECTATIONS

## Federal Tier (Tier 1)
Must surface:
- National Scenic Trails as Trail entities
- National Trails System as Trail Network
- Multi-state trail systems

## State Tier (Tier 2)
Must surface:
- Statewide trail systems
- State-designated greenway networks
- Multi-county trail corridors

## District Tier (Tier 3)
May surface:
- Regional greenway networks
- Multi-trail recreation systems
- District-level trail networks

## County Tier (Tier 4)
May surface:
- Countywide bikeway networks
- County trail systems

## Township & Municipal Tiers (Tiers 5–6)
May surface:
- Municipal trail networks
- Multi-trail corridor initiatives

## Conservancy Tier (Tier 7)
May surface:
- Multi-trail conservation corridors
- Regional trail initiatives

## Private Tier (Tier 8)
May surface:
- Privately managed trail systems
- Campus-scale multi-trail networks

------------------------------------------------------------
# 14. OUTPUT REQUIREMENTS

Each Trail Network candidate must output:

**Raw Discovery Record conforming to:**
- **Discovery Output Specification v5.x**
- **Trail Network Schema Module v5.x**
- **Discovery Metadata Specification v5.x**

**Must include:**
- All extracted fields (raw, unnormalized)
- Complete source_map
- Member trail names (if available) in member_trail_names_raw
- Member trail count (if published)
- Total length (if published)
- identity_notes_raw with any network/trail boundary questions,
  membership uncertainty, or name conflicts
- maps_raw as plain URL list

**Must NOT include:**
- Normalized values
- Merged data from multiple sources
- Inferred member trails
- Calculated totals
- Resolved member_trail_ids (normalization populates this)
- Type/description metadata in maps_raw

------------------------------------------------------------
# 15. QUALITY CHECKLIST

Before emitting a discovery record, verify:

- ✅ network_name_raw recorded exactly as found
- ✅ Network is multi-trail system (not single trail with segments)
- ✅ Network is not marketing label or informal grouping
- ✅ All available fields extracted
- ✅ source_map populated with URL → fields mapping
- ✅ member_trail_names_raw recorded if member trails listed
- ✅ member_trail_count_raw recorded if published
- ✅ total_length_miles_raw recorded if published
- ✅ status recorded if documented (especially "Partial" or
  "Planned")
- ✅ ownership_raw recorded if applicable (often blank)
- ✅ identity_notes_raw used for any network/trail boundary
  questions, membership uncertainty, name conflicts
- ✅ maps_raw entries are plain URLs — no embedded metadata
- ✅ No normalization or standardization applied
- ✅ No calculated or estimated values
- ✅ No inferred member trails

------------------------------------------------------------
# 16. INTEGRATION POINTS

This module integrates with:

- **Discovery Protocol Module v5.x**
- **Trail Network Schema Module v5.x**
- **Trail Network Vocabulary Module v5.x**
- **Trail Discovery Sub-Procedure v5.x**
- **Trail Segment Discovery Sub-Procedure v5.x**
- **Site Network Discovery Sub-Procedure v5.x**
- **Discovery Output Specification v5.x**
- **Discovery Metadata Specification v5.x**
- **Resolution Engine v5.x**
- **Normalization Engine v5.x**
- **Trail Network TSV Output Specification v5.x**
- **Audit & Logging Module v5.x**

------------------------------------------------------------
# 17. MULTI-COUNTY TRAIL NETWORK PROTOCOL (IMP-046)

Trail Networks whose member trails span multiple counties require special handling
because member trails are discovered county-by-county over multiple sessions.

## 17.1 When to Create the Network Record

Create the Trail Network entity record during the **first county session** that
encounters the network. Do not defer network creation until all counties have been
processed — the network entity must exist in the Entity Graph before member trail
`trail_network_members` rows can reference it.

## 17.2 Partial Membership Documentation

When creating a multi-county Trail Network during the first county session:

- Populate `member_trail_names_raw` with only the trails documented in the current county session.
- Record the explicit note in `identity_notes_raw`:
  `PARTIAL MEMBERSHIP: Only [County] County member trails documented as of [date]. Additional member trails expected from [County2], [County3] county sessions.`
- Set `member_trail_count_raw` to the count of members documented so far, not the total network membership.
- Set `total_length_miles_raw` to the length documentable from available sources, noting if partial.

## 17.3 TSV File Location

The Trail Network TSV row is created and lives in the **first county's** spreadsheet folder.
It is NOT duplicated in subsequent county spreadsheet folders — subsequent county sessions
update the existing record, not create new ones.

## 17.4 Subsequent County Sessions

When a subsequent county session discovers additional member trails for an already-created Trail Network:

- Do NOT create a new Trail Network entity record.
- Locate the existing network entity in the Entity Graph by name.
- For each new member trail: add an entry to `trail_network_members` (network_id, trail_id).
- Update `member_trail_ids` on the network entity to include the new trail IDs.
- Update `member_trail_count` to the new total.
- Update `total_length_miles` if the new member trails add documented length.
- Update `identity_notes` to reflect updated membership status (remove "PARTIAL MEMBERSHIP"
  flag when all expected county sessions have been processed).

## 17.5 Network TSV Update

Because the network TSV lives in the first county's folder, subsequent county session
updates to the network entity must be reflected by re-exporting the network's TSV row.
Document the update in the session log for the subsequent county.

## 17.6 Example (Central Ohio Blueways)

Central Ohio Blueways (FR-TN-0003) was created during the Franklin County session
(2026-03-25). At creation, `member_trail_names_raw` included only the Franklin County
water trail members (Olentangy River, Scioto River, Alum Creek, Big Darby, Big Walnut
water trails). Delaware and Pickaway County member trails were noted as pending in
`identity_notes_raw`. The network TSV lives in the Franklin County spreadsheet folder.
When Delaware County is processed, its water trail member entries are added to
`trail_network_members` and `member_trail_ids` is updated on the existing FR-TN-0003 record.

------------------------------------------------------------
# END OF TRAIL NETWORK DISCOVERY SUB-PROCEDURE v5.2
