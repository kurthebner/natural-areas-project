# NATURAL AREAS PROJECT
# TRAIL NETWORK DISCOVERY SUB-PROCEDURE v5.0
(Authoritative Sub-Procedure for Discovering Trail Networks)

This module defines the authoritative, deterministic workflow for discovering
**Trail Networks** across all discovery tiers within the v5.0
Raw → Resolution → Normalization → Entity Graph pipeline.

This document supersedes all v4.x Trail Network discovery logic.

------------------------------------------------------------
# CHANGES FROM v4.0

- **Philosophy clarified**: Discovery = Collection, Normalization = Decisions
- **Source mapping added**: Track which fields came from which URLs
- **Field changes**: Added status, ownership, total_length_miles, member_trail_count, member_trail_ids, maps array
- **Governance terminology**: managing_agency_raw → governance_raw, added partner_agencies_raw
- **Complete rewrite**: Enhanced practical guidance for discoverers
- All version references updated to v5.0

------------------------------------------------------------
# 1. PURPOSE

The Trail Network Discovery Sub-Procedure v5.0 provides the authoritative workflow for:

- Identifying Trail Network candidates
- Extracting raw, unnormalized metadata
- Supporting enumerative and recursive discovery
- Preventing misclassification across the six-entity ontology
- Recording tier and URL provenance with field-level source mapping
- Emitting Raw Discovery Records v5.0
- Emitting Discovery Metadata v5.0
- Integrating cleanly with Trail, Trail Segment, and Site Network discovery
- Feeding the Resolution Engine v5.0

A **Trail Network** is:

- A named, identity-bearing umbrella entity
- Composed of multiple Trails
- Documented in authoritative sources
- Distinct from its member Trails
- Not a marketing label or informal grouping
- Not a single Trail with multiple Segments

This module is authoritative for Trail Network discovery.

------------------------------------------------------------
# 2. DISCOVERY PHILOSOPHY (v5.0)

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

If you're unsure whether to include something:
- Include it
- Record it in notes_raw if uncertain
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

Each tier must surface Trail Network candidates when applicable.

------------------------------------------------------------
# 4. REQUIRED SOURCES

Each tier must check the following for Trail Network references:

- Official agency websites
- Authoritative listing/index pages (e.g., `/trails/`, `/systems/`)
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

All sources must be logged in **Discovery Metadata v5.0** and **source_map**.

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

## 6.1 When Is Something A Trail Network?

**Trail Network (umbrella over multiple trails):**
- ✅ "Ohio to Erie Trail" - composed of multiple named trails
- ✅ "Buckeye Trail" - one continuous named trail system
- ✅ "Cleveland Metroparks All-Purpose Trail System" - multiple trails within system
- ✅ "National Trails System" - umbrella over many National Scenic/Historic Trails

**Individual Trail (not a network):**
- ❌ "Slippery Elm Trail" with multiple segments - this is ONE trail, not a network
- ❌ "Towpath Trail" even if very long - one trail identity, not a network

## 6.2 Key Questions

**Is it a Trail or a Network?**

Ask:
1. Does it have member trails with their own names?
2. Is it described as a "system", "network", or collection of trails?
3. Do sources list multiple trails as part of this entity?

If YES to these → Trail Network
If NO → Individual Trail (may have segments)

## 6.3 Ambiguous Cases

**"Buckeye Trail" - Is it a Trail or Trail Network?**
- Depends on how it's documented
- If treated as single continuous trail → Trail
- If described as system of county sections → Could be either
- Check authoritative sources for how they classify it

**When in doubt:**
- Flag in notes_raw
- Let Resolution/Normalization decide based on authoritative sources
- If sources treat it as single trail → Trail
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
- Multi-trail recreation or mobility networks
- Trail system overview pages

Record each appearance as a raw Trail Network candidate.

## 7.2 Step 2 — Verify Identity-Bearing Name

A Trail Network must have:

- A documented, stable name
- Not a temporary project name
- Not a marketing slogan
- Not an informal grouping

If ambiguous, flag for review in notes_raw.

## 7.3 Step 3 — Confirm Multi-Trail Composition

The candidate must include:

- Two or more Trails
- Documented membership
- Explicit geographic or thematic linkage

**Do not infer membership:**
- Only record trails explicitly listed as members
- Don't guess which trails belong
- Normalization will validate relationships

------------------------------------------------------------
# 8. FIELD-BY-FIELD EXTRACTION GUIDE

## 8.1 Core Identity Fields

### `network_name_raw` (REQUIRED)
**What to collect:**
- Official published name exactly as written
- Don't normalize capitalization
- Don't add or remove words

**Examples:**
- "Ohio to Erie Trail" ✅
- "Cleveland Metroparks All-Purpose Trail System" ✅
- "National Trails System" ✅

**What NOT to do:**
- ❌ Don't standardize: "Ohio-to-Erie Trail" when source says "Ohio to Erie Trail"
- ❌ Don't add descriptors not in official name

### `network_type_raw` (OPTIONAL)
**What to collect:**
- Regional Greenway, Statewide Trail System, National Trail System,
  County Trail System, Municipal Trail Network, Bikeway Network,
  Water Trail Network, Multi-Use Trail System

**Record exactly as source describes:**
- Source says "regional greenway system" → record "regional greenway system"
- Source says "county trail network" → record "county trail network"
- Don't normalize vocabulary

### `status_raw` (OPTIONAL) ✨ NEW IN v5.0
**What to collect:**
- Active, Planned, Partial, Inactive

**"Partial" is important for Trail Networks:**
- Some sections complete, others gaps or planned
- Common for long-distance or regional networks

**Only if explicitly stated:**
- Source says "under development" → record "under development"
- Source says "partially complete" → record "Partial"

## 8.2 Physical Characteristics

### `total_length_miles_raw` (OPTIONAL) ✨ NEW IN v5.0
**What to collect:**
- Total length of entire network (all member trails combined)
- Number only: "326", "1444", "87.5"

**Often published by network:**
- "Ohio to Erie Trail spans 326 miles" → record "326"
- "System includes 45 miles of trails" → record "45"

**What NOT to do:**
- ❌ Don't calculate by adding up member trail lengths
- ❌ Only record if network publishes total
- ❌ Don't estimate

### `member_trail_count_raw` (OPTIONAL) ✨ NEW IN v5.0
**What to collect:**
- Number of trails in the network
- Number only: "12", "47", "8"

**Examples:**
- "System includes 12 trails" → record "12"
- "Network composed of 8 major trails" → record "8"

**What NOT to do:**
- ❌ Don't count trails yourself from lists
- ❌ Only record if explicitly published
- If you see a list of trails, note count in description/notes, not here

### `member_trail_names_raw` (OPTIONAL) ✨ NEW IN v5.0
**What to collect:**
- Names of member trails
- Semicolon-delimited list
- Record exactly as listed

**Examples:**
- "Towpath Trail;Slippery Elm Trail;University Parks Trail"
- Record all member trails mentioned

**Important:**
- This is for discovery reference only
- Normalization populates member_trail_ids by resolving names to IDs
- Don't worry about exact matching - record as shown

## 8.3 Governance Fields

### `governance_raw` (OPTIONAL)
**What to collect:**
- Primary coordinating agency or organization
- "Ohio Department of Natural Resources", "Cleveland Metroparks",
  "Buckeye Trail Association", "Rails-to-Trails Conservancy"

**Record exactly as stated:**
- Source says "managed by Rails-to-Trails Conservancy"
  → record "Rails-to-Trails Conservancy"

### `partner_agencies_raw` (OPTIONAL) ✨ NEW IN v5.0
**What to collect:**
- Secondary managing agencies or partner organizations
- Important for multi-jurisdiction networks

**Semicolon-delimited:**
- "Cleveland Metroparks;Summit Metro Parks;Ohio & Erie Canal Association"

**Look for:**
- "In partnership with..."
- "Managed jointly by..."
- "Coordinated by... with support from..."

**Only if explicitly documented:**
- Don't infer partnerships

### `ownership_raw` (OPTIONAL) ✨ NEW IN v5.0
**What to collect:**
- Legal owner of the network (if applicable)
- Often blank for coordinating bodies

**Examples:**
- County-owned network: "Wood County"
- Municipal system: "City of Cleveland"
- Coordinating body (no ownership): leave blank

**Ownership vs Governance:**
- Ownership = who legally owns
- Governance = who manages/coordinates
- For Trail Networks, governance often more relevant than ownership
- Many networks are coordinating bodies without land ownership

## 8.4 Location Fields

### `counties_raw` (OPTIONAL)
**What to collect:**
- All counties the network traverses
- Multiple counties: semicolon-delimited

**Examples:**
- "Wood;Lucas;Ottawa;Sandusky;Erie" ✅
- "Wood County;Lucas County" → record "Wood County;Lucas County"
  (normalization removes "County")

### `states_raw` (OPTIONAL)
**What to collect:**
- States traversed (for multi-state networks only)
- Leave blank for Ohio-only networks
- Semicolon-delimited

**Examples:**
- "Ohio;Pennsylvania;New York" ✅
- Single-state networks: leave blank

## 8.5 Descriptive Fields

### `description_raw` (OPTIONAL)
**What to collect:**
- 1-3 sentences describing the network's identity, scope, and purpose
- May include brief establishment history

**Examples:**
- "326-mile multi-use trail connecting Cleveland, Columbus, and Cincinnati"
- "System of 12 interconnected trails spanning three metro parks districts"

**What NOT to include:**
- ❌ Detailed member trail descriptions (those go in Trail records)
- ❌ Individual access point details

### `notes_raw` (OPTIONAL)
**What to collect:**
- Clarifications, gaps in information, uncertainties
- Development status notes
- Planned expansions

## 8.6 URL and Map Fields

### `url_primary` (OPTIONAL)
**What to collect:**
- Primary authoritative URL for the network
- Usually network's dedicated page

**Examples:**
- https://ohiotoerietrail.org/ ✅
- https://buckeyetrail.org/ ✅

### `url_all` (OPTIONAL)
**What to collect:**
- ALL URLs where network is mentioned
- Don't deduplicate

### `maps_raw` (OPTIONAL) ✨ NEW IN v5.0 - RICH ARRAY
**What to collect:**
- ALL map URLs for the network
- System overview maps, interactive viewers, GPX files, network maps

**Trail Networks are spatial - multiple map types expected:**
- System overview map: collect it
- Interactive GIS viewer: collect it
- Network-wide GPX file: collect it
- PDF map of entire system: collect it
- Segment maps: collect them

**Examples:**
- https://ohiotoerietrail.org/maps/system-map.pdf
- https://ohiotoerietrail.org/interactive-map
- https://ohiotoerietrail.org/gpx/complete-route.gpx

**Semicolon-delimited:**
- "https://network.org/map.pdf;https://network.org/viewer;https://network.org/gpx/route.gpx"

------------------------------------------------------------
# 9. MEMBER TRAIL TRACKING

## 9.1 During Discovery

**Record member trail names in `member_trail_names_raw`:**
- Semicolon-delimited list
- Record exactly as source lists them
- Don't worry about exact name matching

**Example:**
```
member_trail_names_raw: "Towpath Trail;Slippery Elm Trail;University Parks Trail;Wintergarden Trail"
member_trail_count_raw: "4"
```

## 9.2 During Normalization

**Normalization Engine:**
- Resolves trail names to trail_ids
- Populates `member_trail_ids` array
- Handles name variants and spelling differences
- Creates entries in `trail_network_members` relationship table

**Result in database:**
```
member_trail_ids: [trail_123, trail_456, trail_789, trail_012]
member_trail_count: 4
```

## 9.3 Incomplete Member Lists

**Common scenario:** Network mentions some trails but not all

**Solution:**
- Record what you find
- Note in description/notes if list appears incomplete
- Later discoveries or sources will add missing members

**Example notes:**
- "Source lists 4 trails; network website mentions 'over 15 trails in system'"
- "Partial member list; complete inventory not available"

------------------------------------------------------------
# 10. PROVENANCE TRACKING (v5.0)

## 10.1 Source Mapping (REQUIRED) ✨ NEW IN v5.0

**For each discovery record, maintain source_map:**

Track which fields came from which URLs.

**Format:**
```json
{
  "source_map": {
    "https://ohiotoerietrail.org/": [
      "network_name", "description", "governance", "url_primary"
    ],
    "https://ohiotoerietrail.org/about/": [
      "total_length_miles", "member_trail_count", "member_trail_names", "partner_agencies"
    ],
    "https://ohiotoerietrail.org/maps/": [
      "maps", "counties"
    ]
  }
}
```

**Guidelines:**
- Group fields by the URL they came from
- URL-level granularity is sufficient

## 10.2 Multiple Sources = Multiple Records

**If you encounter the same network at multiple URLs:**

- Emit SEPARATE discovery records
- Each with its own source_map
- Do NOT attempt to merge
- Resolution engine will handle merging

------------------------------------------------------------
# 11. WHAT NOT TO DO (CRITICAL)

## 11.1 Don't Create Networks for Single Trails
- ❌ Don't create network for trail with multiple segments
- ✅ Single trail = Trail entity, not Trail Network

## 11.2 Don't Create Networks for Marketing Labels
- ❌ "Scenic Trails of Wood County" (informal grouping)
- ❌ "Best Trails in Ohio" (marketing list)
- ✅ Only create for documented, identity-bearing systems

## 11.3 Don't Normalize or Standardize
- ❌ Don't change capitalization
- ❌ Don't fix typos in network names
- ❌ Don't standardize terminology
- ✅ Record exactly as found

## 11.4 Don't Calculate or Estimate
- ❌ Don't calculate total length from member trails
- ❌ Don't count member trails yourself
- ❌ Don't estimate counties from maps
- ✅ Only record explicitly published values

## 11.5 Don't Infer Membership
- ❌ Don't guess which trails belong
- ❌ Don't add trails that seem like they should be members
- ✅ Only record explicitly documented members

## 11.6 Don't Merge or Detect Conflicts
- ❌ Don't merge records from multiple sources
- ❌ Don't try to detect if values conflict
- ✅ Emit separate records, Resolution handles merging

------------------------------------------------------------
# 12. SPECIAL CASES

## 12.1 National Trails System

**Scenario:** National Trails System is umbrella over National Scenic Trails,
National Historic Trails, National Recreation Trails

**How to document:**
```
network_name_raw: "National Trails System"
network_type_raw: "National Trail System"
governance_raw: "National Park Service"
member_trail_names_raw: "North Country National Scenic Trail;Appalachian National Scenic Trail;..."
member_trail_count_raw: "30" (if published)
```

**Each National Scenic Trail is ALSO a Trail entity:**
- "North Country National Scenic Trail" = Trail (not network)
- "National Trails System" = Trail Network (contains many trails)

## 12.2 Nested Systems

**Question:** Can a Trail Network contain other Trail Networks?

**Answer:** No, in v5.0 ontology.
- Trail Networks contain Trails only
- No nested network structures
- Keeps architecture clean

**Example:**
- "National Trails System" contains "North Country National Scenic Trail"
- "North Country NST" is a Trail, not a network
- Even though NCT is very long and crosses many states

## 12.3 County/Municipal Systems

**Scenario:** "Wood County Park District Trail System"

**Is this a Trail Network or Site Network?**

**Ask:**
- Does it contain multiple named trails? → Trail Network
- Is it an umbrella over multiple parks/sites? → Site Network
- Both? → Create both entities (they serve different purposes)

**Example - Both:**
```
Site Network:
  name: "Wood County Park District"
  type: "County Park System"
  member_sites: [Carter Farm, Oaks Opening, ...]

Trail Network:
  name: "Wood County Park District Trail System"
  type: "County Trail System"
  member_trails: [Slippery Elm Trail, Oak Openings Trail, ...]
```

## 12.4 Partial vs. Planned Networks

**"Partial" status:**
- Some trails complete and active
- Other sections are gaps or planned
- Network exists but incomplete

**Example:**
```
network_name: "Great Ohio Lake to River Greenway"
status: "Partial"
description: "85-mile planned greenway; 23 miles currently open"
```

**"Planned" status:**
- Entire network is planned
- No sections yet open
- Network documented but not yet built

------------------------------------------------------------
# 13. TIER-SPECIFIC EXPECTATIONS

## 13.1 Federal Tier (Tier 1)
Must surface:
- National Scenic Trails
- National Historic Trails
- National Recreation Trail Networks
- Multi-state trail systems

## 13.2 State Tier (Tier 2)
Must surface:
- Statewide trail systems
- State-designated greenway networks
- Multi-county trail corridors

## 13.3 District Tier (Tier 3)
May surface:
- Regional greenway networks
- Multi-trail recreation systems
- District-level trail systems

## 13.4 County Tier (Tier 4)
May surface:
- Countywide bikeway networks
- Countywide greenway systems
- County trail systems

## 13.5 Township & Municipal Tiers (Tiers 5-6)
May surface:
- Local trail networks
- Multi-trail corridor initiatives
- Municipal trail systems

## 13.6 Conservancy Tier (Tier 7)
May surface:
- Multi-trail conservation corridors
- Regional trail initiatives

## 13.7 Private Tier (Tier 8)
May surface:
- Privately managed trail systems
- Campus-scale multi-trail networks

------------------------------------------------------------
# 14. OUTPUT REQUIREMENTS

Each Trail Network candidate must output:

**Raw Discovery Record conforming to:**
- **Discovery Output Specification v5.0**
- **Trail Network Schema Module v5.0**
- **Discovery Metadata Specification v5.0**

**Must include:**
- All extracted fields (raw, unnormalized)
- Complete source_map
- Member trail names (if available)
- Member trail count (if published)
- Total length (if published)

**Must NOT include:**
- Normalized values
- Merged data from multiple sources
- Inferred member trails
- Calculated totals
- Resolved member_trail_ids (normalization populates this)

------------------------------------------------------------
# 15. QUALITY CHECKLIST

Before emitting a discovery record, verify:

- ✅ network_name_raw recorded exactly as found
- ✅ Network is multi-trail system (not single trail with segments)
- ✅ Network is not just marketing label or informal grouping
- ✅ All available fields extracted
- ✅ source_map populated with URL → fields mapping
- ✅ member_trail_names_raw recorded if member trails listed
- ✅ member_trail_count_raw recorded if published
- ✅ total_length_miles_raw recorded if published
- ✅ status recorded if documented (especially "Partial" or "Planned")
- ✅ ownership recorded if meaningful (often blank for coordinating bodies)
- ✅ maps collected - multiple map URLs if available
- ✅ No normalization or standardization applied
- ✅ No calculated or estimated values
- ✅ No inferred member trails

------------------------------------------------------------
# 16. INTEGRATION POINTS

This module integrates with:

- **Discovery Protocol Module v5.0**
- **Tier Sub-Procedure Template v5.0**
- **Trail Network Schema Module v5.0**
- **Trail Network Vocabulary Module v5.0**
- **Trail Discovery Sub-Procedure v5.0**
- **Trail Segment Discovery Sub-Procedure v5.0**
- **Site Network Discovery Sub-Procedure v5.0**
- **Discovery Output Specification v5.0**
- **Discovery Metadata Specification v5.0**
- **Resolution Engine v5.0**
- **Normalization Engine v5.0**
- **TSV Output Specifications v5.0**
- **Audit & Logging Module v5.0**

------------------------------------------------------------
# END OF TRAIL NETWORK DISCOVERY SUB-PROCEDURE v5.0
