# NATURAL AREAS PROJECT
# SITE NETWORK DISCOVERY SUB-PROCEDURE v5.1
(Authoritative Sub-Procedure for Discovering Site Networks)

This module defines the authoritative, deterministic workflow for discovering
**Site Networks** across all discovery tiers within the v5.x
Raw → Resolution → GPS Acquisition → Normalization → Entity Graph pipeline.

This document supersedes all v5.0 and v4.x Site Network discovery logic.

------------------------------------------------------------
# CHANGES FROM v5.0 → v5.1

- **Field renames**:
  - notes_raw → identity_notes_raw (identity clarifications and flags)
  - url_all → urls_raw (all URLs including map URLs)
  - url_primary → url_primary_raw
  - map_url_raw removed — map URLs now included in urls_raw
- **Identity threshold clarified**: Explicit system-level identity required;
  err on inclusion for gray-area cases; SITE_NETWORK_UNCERTAIN flag added
- **Gray-area guidance added**: County/municipal park systems,
  land trust collections — when to include vs. exclude
- **Derived Label removed**: No longer collected or referenced
- **All cross-module references updated to v5.x**

------------------------------------------------------------
# CHANGES FROM v4.0 → v5.0

- Philosophy clarified: Discovery = Collection, Normalization = Decisions
- Source mapping added: Track which fields came from which URLs
- Field changes: Removed alternate_names, history; added ownership,
  member_count, member_site_ids
- Governance terminology: managing_agency_raw → governance_raw,
  secondary_managing_agencies_raw → partner_agencies_raw
- Complete rewrite: Enhanced practical guidance for discoverers

------------------------------------------------------------
# 1. PURPOSE

The Site Network Discovery Sub-Procedure v5.1 provides the authoritative
workflow for:

- Identifying Site Network candidates
- Applying the identity threshold (explicit system-level identity)
- Flagging gray-area candidates with SITE_NETWORK_UNCERTAIN
- Extracting raw, unnormalized metadata
- Supporting enumerative and recursive discovery
- Preventing misclassification across the six-entity ontology
- Recording tier and URL provenance with field-level source mapping
- Emitting Raw Discovery Records v5.x
- Emitting Discovery Metadata v5.x
- Feeding the Resolution Engine v5.x

A **Site Network** is:

- A named, identity-bearing umbrella entity
- Composed of multiple Sites
- Documented in authoritative sources
- Distinct from its member Sites
- Not a marketing label or informal grouping
- Not a single Site with multiple child Sites
- Not a governance body that merely manages multiple sites without
  system-level identity

This module is authoritative for Site Network discovery.

------------------------------------------------------------
# 2. DISCOVERY PHILOSOPHY (v5.x)

## 2.1 Core Principle: Discovery = Collection, Normalization = Decisions

**Discovery Phase (YOU ARE HERE):**
- Collect everything you find
- Record exactly as found
- Don't normalize, standardize, or choose between values
- Don't deduplicate URLs
- Flag uncertainty — don't resolve it

**Normalization Phase (LATER):**
- Standardize vocabulary
- Choose canonical values
- Validate member site relationships
- Populate member_site_ids

## 2.2 Err on Inclusion

If uncertain whether a candidate meets the Site Network identity threshold:
- Include it
- Set the SITE_NETWORK_UNCERTAIN flag in identity_notes_raw
- Record rationale
- Let Resolution/Normalization arbitrate

**Better to include a borderline candidate than miss a legitimate network.**

## 2.3 Multiple Sources = Multiple Records

If you find the same Site Network at multiple URLs:
- Emit SEPARATE discovery records
- Do NOT attempt to merge
- Resolution engine handles merging

------------------------------------------------------------
# 3. IDENTITY THRESHOLD

## 3.1 The Standard

A Site Network requires **explicit system-level identity** — the organization
or designation must present itself as a named system or network in authoritative
sources, not merely manage multiple sites.

**Evidence of system-level identity (any one sufficient):**
- A system name distinct from the managing organization's name
- A published system-wide map covering all member sites
- A membership, passport, or unified access program
- Explicit "X parks in the Y system" or "Y network of preserves" language
- A federal or state designation as a heritage area, corridor, or network
- A branded system identity separate from the operational agency

## 3.2 What Qualifies

**Clear Site Networks:**
- MWCD — Muskingum Watershed Conservancy District's 16 lakes system
  (explicitly branded as a unified reservoir system)
- Ohio Scenic River corridors — formally designated, explicitly multi-site
- National Heritage Areas — federally designated, named systems
- Land trust preserve networks — e.g., "Black Swamp Conservancy preserves"
  when explicitly listed and mapped as a unified network
- County or municipal park systems with unified branding, system maps, or
  passport programs distinct from the managing department's identity

**Clear exclusions (not Site Networks):**
- A parks and recreation department as governance body only
  (no system-level branding, no system name)
- ODNR as the managing agency for Ohio state parks (agency, not network)
- Any informal grouping or marketing label

## 3.3 The Gray Area — Err on Inclusion

**Uncertain cases — include and flag:**
- County park district that manages multiple parks but has minimal
  system-level branding
- Municipal parks department with a simple parks page listing all parks
  but no distinct system name or map
- Land trust with multiple named preserves but no explicit "network" framing

**Flag these with:**
```
identity_notes_raw: "SITE_NETWORK_UNCERTAIN — [description of uncertainty,
e.g., 'governance body with multiple parks but no distinct system name or
branding; verify system-level identity']"
```

------------------------------------------------------------
# 4. SCOPE

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

Each tier must surface Site Network candidates when applicable.

------------------------------------------------------------
# 5. REQUIRED SOURCES

Each tier must check the following for Site Network references:

- Official agency websites
- Authoritative listing/index pages (e.g., /heritage/, /corridors/, /parks/)
- GIS systems and interactive maps
- Planning documents (master plans, corridor plans, heritage plans)
- Stewardship or management plans
- Federal and state designation documents
- National Heritage Area documentation
- Scenic River Corridor documentation
- Historic District documentation
- Watershed or ecological corridor plans
- Partnership announcements
- Multi-site program pages
- Regional conservation or heritage initiatives
- Park district or land trust system pages

All sources must be logged in **Discovery Metadata v5.x** and **source_map**.

------------------------------------------------------------
# 6. SITE NETWORK VS. RELATED ENTITIES: CRITICAL DISTINCTIONS

## 6.1 Site Network vs. Parent Site with Child Sites

**Site Network (umbrella over multiple separate sites):**
- ✅ "Wood County Park District System" — manages multiple separate parks
- ✅ "Ohio & Erie Canalway" — encompasses multiple distinct sites
- ✅ "Maumee River Scenic River Corridor" — includes multiple sites along corridor

**Parent Site with Child Sites (hierarchical containment):**
- ❌ "Heritage Village Historic Park" with "Blacksmith District" inside
  → One site with internal child sites, not a network

**Key difference:**
- Site Network = collection of separate sites sharing identity/management
- Parent Site = one site containing internal identity-bearing areas

## 6.2 Site Network vs. Governance Body

**Site Network (system-level identity):**
- ✅ Has a system name or brand distinct from the managing department
- ✅ Has a system-wide map, passport program, or unified access program
- ✅ Explicitly presents itself as a network or system

**Governance body only (not a Site Network):**
- ❌ Parks department that manages multiple parks with no system branding
- ❌ Agency listed as governance on multiple Site records
- → Record as governance on member Sites, not as a Site Network entity

**When uncertain:** Include and flag SITE_NETWORK_UNCERTAIN.

## 6.3 Site Network vs. Trail Network

**Site Network:** Collection of Sites (land areas)
**Trail Network:** Collection of Trails (linear systems)

A greenway may be both — a Site Network (sites along the greenway) and a
Trail Network (the trail system). Discover both if both identities exist.

------------------------------------------------------------
# 7. DISCOVERY WORKFLOW

## 7.1 Step 1 — Identify Named Multi-Site Systems

Search all required sources for:

- Named corridors, heritage areas, historic districts
- Scenic river systems
- Watershed and ecological networks
- Cultural landscape networks
- Multi-site conservation programs
- Multi-site recreation networks
- Park district systems with system-level branding
- Municipal park systems with system-level branding
- Land trust preserve networks with system-level branding

Record each appearance as a raw Site Network candidate.

## 7.2 Step 2 — Apply Identity Threshold

For each candidate, ask:
1. Does it have a name distinct from the managing organization?
2. Does it present itself as a system or network in authoritative sources?
3. Is there a system map, passport program, or unified access program?
4. Is it a formal designation (NHA, scenic river, historic district)?

- Any YES → include as Site Network candidate
- All NO, but uncertain → include with SITE_NETWORK_UNCERTAIN flag
- Clear governance-body-only → exclude; record as governance on member Sites

## 7.3 Step 3 — Confirm Multi-Site Composition

The candidate must include:
- Two or more Sites
- Documented membership (explicit or inferable from system framing)
- Explicit geographic or thematic linkage

**Do not infer membership:**
- Only record sites explicitly listed as members
- Don't guess which sites belong
- Normalization will validate relationships

------------------------------------------------------------
# 8. FIELD-BY-FIELD EXTRACTION GUIDE

## 8.1 Core Identity Fields

### `network_name_raw` (REQUIRED)
Record the official published name exactly as written.
- Don't normalize capitalization
- Don't add or remove words

**Examples:**
- "Wood County Park District System" ✅
- "Ohio & Erie Canalway National Heritage Area" ✅
- "Black Swamp Conservancy Preserve Network" ✅

### `network_type_raw` (OPTIONAL)
Record exactly as the source describes:
- "county park district", "heritage area", "scenic river corridor",
  "preserve network", "conservation corridor"
- Don't normalize vocabulary during discovery

### `status_raw` (OPTIONAL)
Only if explicitly stated:
- "proposed", "active", "in formation"

## 8.2 Membership Fields

### `member_count_raw` (OPTIONAL)
The officially published count of member sites only — do not count yourself.
- "21 parks", "16 lakes", "8 preserves" → record "21", "16", "8"

### `member_site_names_raw` (OPTIONAL)
Names of member sites, semicolon-delimited, exactly as listed in source.
- "Carter Historic Farm;Oaks Opening;Blue Creek Conservation Area"
- Normalization resolves names to IDs — record as shown

## 8.3 Governance Fields

### `governance_raw` (OPTIONAL)
Primary managing agency or organization, exactly as stated.
- "Wood County Park District", "ODNR", "National Park Service"

### `partner_agencies_raw` (OPTIONAL)
Secondary managing agencies or partners, semicolon-delimited.
Only if explicitly documented — do not infer partnerships.

### `ownership_raw` (OPTIONAL)
Legal owner of the network if applicable. Often blank for coordinating bodies.
- "Wood County", "State of Ohio", "United States Department of Interior"
- Leave blank for NHAs, scenic corridors, and other designating bodies

## 8.4 Location Fields

### `counties_raw` (OPTIONAL)
All counties the network encompasses, semicolon-delimited.
- "Wood", "Cuyahoga;Summit;Portage"

### `states_raw` (OPTIONAL)
States encompassed for multi-state networks only.
Leave blank for Ohio-only networks.

## 8.5 Descriptive Fields

### `description_raw` (OPTIONAL)
1-3 sentences describing the network's identity, scope, and purpose.
- "System of 21 parks and preserves managed by Wood County Park District"
- Do not include individual site descriptions

### `identity_notes_raw` (OPTIONAL)
Identity clarifications, disambiguation notes, uncertainty flags.

**Use for:**
- SITE_NETWORK_UNCERTAIN flag with rationale
- Alternate or historical names
- Vocabulary type uncertainty (e.g., "may be Trail Network or Site Network")
- Disambiguation from similar-named entities
- Governance-body-vs-network uncertainty

**SITE_NETWORK_UNCERTAIN format:**
```
SITE_NETWORK_UNCERTAIN — [description of uncertainty]
```

**Examples:**
```
identity_notes_raw: "SITE_NETWORK_UNCERTAIN — parks department manages
multiple parks but no distinct system name or branding found; verify
system-level identity"

identity_notes_raw: "Also known as 'Wood County Parks' in informal sources;
official name confirmed as 'Wood County Park District System'"

identity_notes_raw: "Greenway system — may qualify as both Site Network
(sites along greenway) and Trail Network (trail system); flagged for
dual discovery"
```

## 8.6 URL Fields

### `url_primary_raw` (OPTIONAL)
Primary authoritative URL for the network's main or dedicated page.
- https://wcparks.org/ ✅
- https://ohiodnr.gov/go-and-do/plan-a-visit/find-a-property ✅

### `urls_raw` (OPTIONAL)
ALL URLs where network information is found, semicolon-delimited.
Includes:
- All content pages (about, parks list, history, programs)
- Map URLs (system overview maps, GIS viewers, PDF maps)
- Do not deduplicate — Resolution handles deduplication

**Note:** There is no separate map_url_raw field. All map URLs go into
urls_raw along with other URLs.

------------------------------------------------------------
# 9. MEMBER SITE TRACKING

## 9.1 During Discovery
Record member site names in `member_site_names_raw`:
- Semicolon-delimited list
- Record exactly as source lists them
- Record count in `member_count_raw` if explicitly published

**Example:**
```
member_site_names_raw: "Carter Historic Farm;Oaks Opening;Blue Creek
Conservation Area;Whitehouse Quarry"
member_count_raw: "4"
```

## 9.2 During Normalization
Normalization Engine:
- Resolves site names to site_ids
- Populates `member_site_ids` array
- Handles name variants and spelling differences
- Creates entries in `site_network_members` relationship table

## 9.3 Incomplete Member Lists
Common scenario: network mentions some sites but not all.

- Record what you find
- Note in identity_notes_raw or description_raw if list appears incomplete
- Later discoveries will add missing members

**Example:**
```
identity_notes_raw: "Source lists 4 sites; district website mentions
'21 parks in system' — member list incomplete"
```

------------------------------------------------------------
# 10. PROVENANCE TRACKING (v5.x)

## 10.1 Source Mapping (REQUIRED)

For each discovery record, maintain source_map tracking which fields
came from which URLs.

**Format:**
```json
{
  "source_map": {
    "https://wcparks.org/": [
      "network_name", "governance", "description", "url_primary_raw"
    ],
    "https://wcparks.org/parks/": [
      "member_count", "member_site_names"
    ],
    "https://wcparks.org/maps/system-map.pdf": [
      "urls_raw"
    ]
  }
}
```

## 10.2 Multiple Sources = Multiple Records

If you encounter the same network at multiple URLs:
- Emit SEPARATE discovery records
- Each with its own source_map
- Do NOT attempt to merge
- Resolution engine will handle merging

------------------------------------------------------------
# 11. WHAT NOT TO DO (CRITICAL)

- ❌ Don't create networks for parent Sites with child Sites
- ❌ Don't create networks for governance bodies with no system identity
- ❌ Don't create networks for marketing labels or informal groupings
- ❌ Don't normalize or standardize field values during discovery
- ❌ Don't count member sites yourself — only record published counts
- ❌ Don't infer membership from proximity or shared governance
- ❌ Don't merge records from multiple sources
- ❌ Don't use a separate map_url_raw field — map URLs go in urls_raw

---

When uncertain: **include the candidate and flag it**, don't exclude it.

------------------------------------------------------------
# 12. SPECIAL CASES

## 12.1 County and Municipal Park Systems

**Include as Site Network when:**
- Explicit system name distinct from the managing department
- Published system-wide map covering all member parks
- Passport, membership, or unified access program
- "X parks in the Y system" language

**Exclude (governance body only) when:**
- No system name, just a department listing its parks
- Parks are listed on a department website with no system-level framing

**When uncertain:** Include and flag SITE_NETWORK_UNCERTAIN.

**Example — include:**
```
network_name_raw: "Wood County Park System"  ← distinct system name
governance_raw: "Wood County Park District"
member_count_raw: "21"
identity_notes_raw: "System has dedicated system map and park passport
program; qualifies as Site Network"
```

**Example — exclude:**
```
[No Site Network record created]
[Each park → individual Site entity]
[governance on each Site: "Bowling Green Parks & Recreation"]
identity_notes on Sites: "No system-level branding found for city parks
collection; governance body only"
```

## 12.2 National Heritage Areas

```
network_name_raw: "Ohio & Erie Canalway National Heritage Area"
network_type_raw: "National Heritage Area"
governance_raw: "National Park Service"
partner_agencies_raw: "Ohio & Erie Canalway Coalition;Ohio History Connection"
counties_raw: "Cuyahoga;Mahoning;Stark;Summit;Tuscarawas"
member_site_names_raw: "Cuyahoga Valley National Park;Canal Visitor Center;..."
```

## 12.3 Scenic River Corridors

```
network_name_raw: "Little Miami Scenic River Corridor"
network_type_raw: "Scenic River Corridor"
governance_raw: "Ohio Department of Natural Resources"
counties_raw: "Clermont;Greene;Hamilton;Warren"
identity_notes_raw: "State-designated scenic river; corridor encompasses
multiple access sites and natural areas along river"
```

## 12.4 Land Trust Preserve Networks

**Include as Site Network when:**
- Land trust explicitly presents preserves as a unified network or system
- Network has a name, map, or collective identity

**Flag when:**
- Land trust manages multiple preserves listed on a properties page
  but without explicit network framing

```
network_name_raw: "Black Swamp Conservancy Preserve Network"
network_type_raw: "Multi-Site Conservation Network"
governance_raw: "Black Swamp Conservancy"
counties_raw: "Henry;Lucas;Wood"
identity_notes_raw: "BSC website presents preserves as unified network
with system map; qualifies as Site Network"
```

## 12.5 MWCD Reservoir System

```
network_name_raw: "Muskingum Watershed Conservancy District Lakes"
network_type_raw: "Multi-Site Recreation Network"
governance_raw: "Muskingum Watershed Conservancy District"
member_count_raw: "16"
counties_raw: "Coshocton;Guernsey;Holmes;Licking;Morgan;Muskingum;..."
identity_notes_raw: "16 reservoirs managed as unified system; MWCD
explicitly brands as system with unified recreation access"
```

------------------------------------------------------------
# 13. TIER-SPECIFIC EXPECTATIONS

## Federal Tier (Tier 1)
Must surface:
- National Heritage Areas
- National Scenic River Corridors
- Multi-state heritage or conservation networks

## State Tier (Tier 2)
Must surface:
- State Scenic River Corridors
- Statewide heritage or conservation networks
- MWCD and other multi-county conservancy systems
- Multi-county ecological corridors

## District Tier (Tier 3)
Must surface:
- Park district systems with system-level branding
- Multi-park heritage or conservation initiatives

## County Tier (Tier 4)
Must surface:
- County park systems with system-level branding (flag uncertain)
- Countywide historic districts
- Countywide conservation corridors
- Watershed-scale networks

## Township & Municipal Tiers (Tiers 5-6)
Must surface:
- Municipal park systems with system-level branding (flag uncertain)
- Local historic districts
- Local cultural landscape networks

## Conservancy Tier (Tier 7)
Must surface:
- Land trust preserve networks with system-level branding
- Multi-site conservation networks
- Ecological corridors
- Watershed networks

## Private Tier (Tier 8)
May surface:
- Privately managed heritage or conservation networks
- Multi-site campus-scale networks

------------------------------------------------------------
# 14. OUTPUT REQUIREMENTS

Each Site Network candidate must output:

**Raw Discovery Record conforming to:**
- **Discovery Output Specification v5.x**
- **Site Network Schema Module v5.x**
- **Discovery Metadata Specification v5.x**

**Must include:**
- All extracted fields (raw, unnormalized)
- Complete source_map
- identity_notes_raw with SITE_NETWORK_UNCERTAIN flag if applicable
- Member site names (if available)
- Member site count (if published)
- All URLs including map URLs in urls_raw

**Must NOT include:**
- Normalized values
- Merged data from multiple sources
- Inferred member sites
- Calculated counts
- Resolved member_site_ids (normalization populates this)
- Separate map_url_raw field (map URLs go in urls_raw)

------------------------------------------------------------
# 15. QUALITY CHECKLIST

Before emitting a discovery record, verify:

- ✅ network_name_raw recorded exactly as found
- ✅ Identity threshold checked — system-level identity or SITE_NETWORK_UNCERTAIN flag set
- ✅ Network is multi-site (not single site with child sites)
- ✅ Network is not purely a governance body (or flagged if uncertain)
- ✅ All available fields extracted
- ✅ source_map populated with URL → fields mapping
- ✅ member_site_names_raw recorded if member sites listed
- ✅ member_count_raw recorded if published (not self-counted)
- ✅ identity_notes_raw used for disambiguation, flags, alternate names
- ✅ Map URLs included in urls_raw (not in a separate map_url_raw field)
- ✅ No normalization or standardization applied
- ✅ No calculated or estimated values
- ✅ No inferred member sites

------------------------------------------------------------
# 16. INTEGRATION POINTS

This module integrates with:

- **Discovery Protocol Module v5.x**
- **Site Network Schema Module v5.x**
- **Site Network Vocabulary Module v5.x**
- **Site Discovery Sub-Procedure v5.x**
- **Trail Network Discovery Sub-Procedure v5.x**
- **Discovery Output Specification v5.x**
- **Discovery Metadata Specification v5.x**
- **Resolution Engine v5.x**
- **Normalization Engine v5.x**
- **Site Network TSV Output Specification v5.x**
- **Audit & Logging Module v5.x**

------------------------------------------------------------
# END OF SITE NETWORK DISCOVERY SUB-PROCEDURE v5.1
