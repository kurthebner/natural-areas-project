# NATURAL AREAS PROJECT
# SITE NETWORK DISCOVERY SUB-PROCEDURE v5.0
(Authoritative Sub-Procedure for Discovering Site Networks)

This module defines the authoritative, deterministic workflow for discovering
**Site Networks** across all discovery tiers within the v5.0
Raw → Resolution → Normalization → Entity Graph pipeline.

This document supersedes all v4.x Site Network discovery logic.

------------------------------------------------------------
# CHANGES FROM v4.0

- **Philosophy clarified**: Discovery = Collection, Normalization = Decisions
- **Source mapping added**: Track which fields came from which URLs
- **Field changes**: Removed alternate_names, history; added ownership, member_count, member_site_ids
- **Governance terminology**: managing_agency_raw → governance_raw, secondary_managing_agencies_raw → partner_agencies_raw
- **Complete rewrite**: Enhanced practical guidance for discoverers
- All version references updated to v5.0

------------------------------------------------------------
# 1. PURPOSE

The Site Network Discovery Sub-Procedure v5.0 provides the authoritative workflow for:

- Identifying Site Network candidates
- Extracting raw, unnormalized metadata
- Supporting enumerative and recursive discovery
- Preventing misclassification across the six-entity ontology
- Recording tier and URL provenance with field-level source mapping
- Emitting Raw Discovery Records v5.0
- Emitting Discovery Metadata v5.0
- Integrating cleanly with Site, Trail Network, and Trail discovery
- Feeding the Resolution Engine v5.0

A **Site Network** is:

- A named, identity-bearing umbrella entity
- Composed of multiple Sites
- Documented in authoritative sources
- Distinct from its member Sites
- Not a marketing label or informal grouping
- Not a single Site with multiple child Sites

This module is authoritative for Site Network discovery.

------------------------------------------------------------
# 2. DISCOVERY PHILOSOPHY (v5.0)

## 2.1 Core Principle: Discovery = Collection, Normalization = Decisions

**Discovery Phase (YOU ARE HERE):**
- Collect everything you find
- Record exactly as found
- Don't normalize, standardize, or choose between values
- Don't deduplicate URLs
- Fast, mechanical extraction

**Normalization Phase (LATER):**
- Standardize vocabulary
- Choose canonical values
- Validate member site relationships
- Populate member_site_ids

## 2.2 When in Doubt: Collect It

If you're unsure whether to include something:
- Include it
- Record it in notes_raw if uncertain
- Let Resolution/Normalization decide

## 2.3 Multiple Sources = Multiple Records

If you find the same Site Network at multiple URLs:
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

Each tier must surface Site Network candidates when applicable.

------------------------------------------------------------
# 4. REQUIRED SOURCES

Each tier must check the following for Site Network references:

- Official agency websites
- Authoritative listing/index pages (e.g., `/heritage/`, `/corridors/`, `/parks/`)
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

All sources must be logged in **Discovery Metadata v5.0** and **source_map**.

------------------------------------------------------------
# 5. IDENTITY RULES FOR SITE NETWORK CANDIDATES

A Site Network candidate is valid only if:

1. It is explicitly documented as a **multi-site system**.
2. It has a **stable, identity-bearing name**.
3. It is composed of **two or more Sites**.
4. It is distinct from its member Sites.
5. It is not merely a marketing label or informal grouping.
6. It is not a Trail Network.
7. It is not a single Site with multiple child Sites.

If any condition fails, the candidate must not be created.

------------------------------------------------------------
# 6. SITE NETWORK VS. PARENT SITE: CRITICAL DISTINCTION

## 6.1 Site Network vs. Parent Site with Child Sites

**Site Network (umbrella over multiple sites):**
- ✅ "Wood County Park District" - manages multiple parks
- ✅ "Ohio State Park System" - manages multiple state parks
- ✅ "Cuyahoga Valley National Heritage Area" - encompasses multiple sites
- ✅ "Maumee River Scenic River Corridor" - includes multiple sites along corridor

**Parent Site with Child Sites (hierarchical containment):**
- ❌ "Heritage Village Historic Park" with "Blacksmith District" inside
  → One site with internal child sites, not a network

**Key difference:**
- Site Network = collection of separate sites that share identity/management
- Parent Site = one site containing internal identity-bearing areas

## 6.2 Key Questions

**Is it a Site Network or a Parent Site?**

Ask:
1. Does it manage multiple separate sites with their own names?
2. Is it described as a "system", "network", or collection of sites?
3. Are member sites geographically distributed (not all within one boundary)?

If YES to these → Site Network
If NO → May be Parent Site with child sites, or just one Site

## 6.3 Both Can Exist

**Common scenario:** Organization has both

**Example:**
```
Site Network:
  name: "Wood County Park District"
  type: "County Park System"
  member_sites: [Carter Farm, Oaks Opening, Blue Creek, ...]
  
Individual Site (also):
  name: "Carter Historic Farm"
  parent: Wood County Park District (via network membership)
```

------------------------------------------------------------
# 7. DISCOVERY WORKFLOW

## 7.1 Step 1 — Identify Named Multi-Site Systems

Search all required sources for:

- Named corridors
- Heritage areas
- Historic districts
- Scenic river systems
- Watershed networks
- Cultural landscape networks
- Multi-site conservation programs
- Multi-site recreation networks
- Park district systems
- Municipal park systems
- Land trust preserve networks

Record each appearance as a raw Site Network candidate.

## 7.2 Step 2 — Verify Identity-Bearing Name

A Site Network must have:

- A documented, stable name
- Not a temporary project name
- Not a marketing slogan
- Not an informal grouping

If ambiguous, flag for review in notes_raw.

## 7.3 Step 3 — Confirm Multi-Site Composition

The candidate must include:

- Two or more Sites
- Documented membership
- Explicit geographic or thematic linkage

**Do not infer membership:**
- Only record sites explicitly listed as members
- Don't guess which sites belong
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
- "Wood County Park District" ✅
- "Ohio State Park System" ✅
- "Cuyahoga Valley National Heritage Area" ✅
- "Black Swamp Conservancy Preserve Network" ✅

**What NOT to do:**
- ❌ Don't standardize
- ❌ Don't add descriptors not in official name

### `network_type_raw` (OPTIONAL)
**What to collect:**
- National Heritage Area, Scenic River Corridor, Historic District,
  County Park System, Municipal Park System, State Park System,
  Land Trust Preserve Network, Conservation Network, Watershed Network

**Record exactly as source describes:**
- Source says "county park district" → record "county park district"
- Source says "heritage area" → record "heritage area"
- Don't normalize vocabulary

### `status_raw` (OPTIONAL)
**What to collect:**
- Active, Proposed, Planned

**Only if explicitly stated:**
- Source says "proposed heritage area" → record "proposed"

## 8.2 Physical Characteristics

### `member_count_raw` (OPTIONAL) ✨ NEW IN v5.0
**What to collect:**
- Number of sites in the network
- Number only: "21", "75", "8"

**Examples:**
- "Wood County Park District manages 21 parks" → record "21"
- "System includes 75 state parks" → record "75"

**What NOT to do:**
- ❌ Don't count sites yourself from lists
- ❌ Only record if explicitly published

### `member_site_names_raw` (OPTIONAL) ✨ NEW IN v5.0
**What to collect:**
- Names of member sites
- Semicolon-delimited list
- Record exactly as listed

**Examples:**
- "Carter Historic Farm;Oaks Opening;Blue Creek Conservation Area"
- Record all member sites mentioned

**Important:**
- This is for discovery reference only
- Normalization populates member_site_ids by resolving names to IDs
- Don't worry about exact matching - record as shown

## 8.3 Governance Fields

### `governance_raw` (OPTIONAL)
**What to collect:**
- Primary managing agency or organization
- "Wood County Park District", "Ohio Department of Natural Resources",
  "Black Swamp Conservancy", "National Park Service"

**Record exactly as stated:**
- Don't normalize or abbreviate

### `partner_agencies_raw` (OPTIONAL)
**What to collect:**
- Secondary managing agencies or partner organizations
- Important for multi-jurisdiction networks

**Semicolon-delimited:**
- "National Park Service;Ohio Department of Natural Resources;Local Historical Society"

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
- County-owned system: "Wood County"
- State system: "State of Ohio"
- Federal: "United States Department of Interior"
- Coordinating body (no ownership): leave blank

**Ownership vs Governance:**
- Ownership = who legally owns or established the network
- Governance = who manages/coordinates
- For heritage areas, governance often more relevant than ownership

## 8.4 Location Fields

### `counties_raw` (OPTIONAL)
**What to collect:**
- All counties the network encompasses
- Multiple counties: semicolon-delimited

**Examples:**
- "Wood" ✅
- "Cuyahoga;Summit;Portage" ✅

### `states_raw` (OPTIONAL)
**What to collect:**
- States encompassed (for multi-state networks only)
- Leave blank for Ohio-only networks
- Semicolon-delimited

**Examples:**
- "Ohio;Pennsylvania" ✅
- Single-state networks: leave blank

## 8.5 Descriptive Fields

### `description_raw` (OPTIONAL)
**What to collect:**
- 1-3 sentences describing the network's identity, scope, and purpose
- May include brief establishment history or origin context

**Examples:**
- "System of 21 parks and preserves managed by Wood County Park District"
- "National Heritage Area encompassing 22,000 acres along the Cuyahoga River valley"

**What NOT to include:**
- ❌ Detailed individual site descriptions (those go in Site records)

### `notes_raw` (OPTIONAL)
**What to collect:**
- Clarifications, gaps in information, uncertainties
- Development status notes
- Special programs or initiatives

## 8.6 URL and Map Fields

### `url_primary` (OPTIONAL)
**What to collect:**
- Primary authoritative URL for the network
- Usually network's dedicated page or main agency page

**Examples:**
- https://wcparks.org/ ✅
- https://stateparks.com/ohio.html ✅

### `url_all` (OPTIONAL)
**What to collect:**
- ALL URLs where network is mentioned
- Don't deduplicate

### `map_url_raw` (OPTIONAL)
**What to collect:**
- Map URL showing the network
- System overview map, GIS viewer

**Note:** Site Networks use simple map_url (not rich array like Trail Networks)
- Typically just one overview map
- If multiple maps, semicolon-delimited

------------------------------------------------------------
# 9. MEMBER SITE TRACKING

## 9.1 During Discovery

**Record member site names in `member_site_names_raw`:**
- Semicolon-delimited list
- Record exactly as source lists them
- Don't worry about exact name matching

**Example:**
```
member_site_names_raw: "Carter Historic Farm;Oaks Opening;Blue Creek Conservation Area;Whitehouse Quarry"
member_count_raw: "4"
```

## 9.2 During Normalization

**Normalization Engine:**
- Resolves site names to site_ids
- Populates `member_site_ids` array
- Handles name variants and spelling differences
- Creates entries in `site_network_members` relationship table

**Result in database:**
```
member_site_ids: [site_123, site_456, site_789, site_012]
member_count: 4
```

## 9.3 Incomplete Member Lists

**Common scenario:** Network mentions some sites but not all

**Solution:**
- Record what you find
- Note in description/notes if list appears incomplete
- Later discoveries or sources will add missing members

**Example notes:**
- "Source lists 4 sites; district website mentions '21 parks in system'"
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
    "https://wcparks.org/": [
      "network_name", "governance", "description", "url_primary"
    ],
    "https://wcparks.org/parks/": [
      "member_count", "member_site_names"
    ],
    "https://wcparks.org/about/": [
      "ownership", "partner_agencies"
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

## 11.1 Don't Create Networks for Parent Sites
- ❌ Don't create network for site with multiple child sites
- ✅ Parent Site with child sites = use parent_site_id in Site schema

## 11.2 Don't Create Networks for Marketing Labels
- ❌ "Top 10 Parks in Wood County" (marketing list)
- ❌ "Beautiful Parks of Ohio" (informal grouping)
- ✅ Only create for documented, identity-bearing systems

## 11.3 Don't Normalize or Standardize
- ❌ Don't change capitalization
- ❌ Don't fix typos in network names
- ❌ Don't standardize terminology
- ✅ Record exactly as found

## 11.4 Don't Calculate or Estimate
- ❌ Don't count member sites yourself
- ❌ Don't estimate counties from maps
- ✅ Only record explicitly published values

## 11.5 Don't Infer Membership
- ❌ Don't guess which sites belong
- ❌ Don't add sites that seem like they should be members
- ✅ Only record explicitly documented members

## 11.6 Don't Merge or Detect Conflicts
- ❌ Don't merge records from multiple sources
- ❌ Don't try to detect if values conflict
- ✅ Emit separate records, Resolution handles merging

------------------------------------------------------------
# 12. SPECIAL CASES

## 12.1 Park District Systems

**Scenario:** "Wood County Park District"

**Is this a Site Network?**

**Yes - if it manages multiple separate parks:**
```
network_name_raw: "Wood County Park District"
network_type_raw: "County Park System"
governance_raw: "Wood County Park District"
ownership_raw: "Wood County"
member_site_names_raw: "Carter Historic Farm;Oaks Opening;Blue Creek Conservation Area;..."
member_count_raw: "21"
```

**Each park is also a Site:**
- "Carter Historic Farm" = Site (member of Wood County Park District network)
- "Oaks Opening" = Site (member of Wood County Park District network)

## 12.2 National Heritage Areas

**Scenario:** "Cuyahoga Valley National Heritage Area"

**How to document:**
```
network_name_raw: "Cuyahoga Valley National Heritage Area"
network_type_raw: "National Heritage Area"
governance_raw: "National Park Service"
partner_agencies_raw: "Cuyahoga Valley National Park;Ohio & Erie Canal Coalition"
counties_raw: "Cuyahoga;Summit"
member_site_names_raw: "Cuyahoga Valley National Park;Peninsula Depot;Hale Farm & Village;..."
```

**Each site within the heritage area is also a Site entity**

## 12.3 Historic Districts

**Scenario:** "Perrysburg Historic District"

**Is this a Site Network or a Site?**

**Ask:**
- Does it contain multiple separate sites with their own names?
  → Site Network
- Is it one bounded area treated as single entity?
  → Site

**Example - Site Network:**
```
network_name: "Perrysburg Historic District"
network_type: "Local Historic District"
member_sites: [Fort Meigs, Hood House, Bigelow-Chapman House, ...]
```

**Example - Single Site:**
```
name: "Perrysburg Downtown Historic District"
category: "Historic Site"
designation: "Local Historic District"
(No network - just one site)
```

## 12.4 Coordinating Bodies vs. Ownership Systems

**Coordinating Body (no land ownership):**
```
network_name: "Maumee River Scenic River Corridor"
network_type: "Scenic River Corridor"
governance: "Ohio Department of Natural Resources"
ownership: [BLANK] - corridor doesn't own land, just coordinates
member_sites: [Sites along river managed by various entities]
```

**Ownership System:**
```
network_name: "Wood County Park District"
network_type: "County Park System"
governance: "Wood County Park District"
ownership: "Wood County"
member_sites: [All parks owned by Wood County]
```

------------------------------------------------------------
# 13. TIER-SPECIFIC EXPECTATIONS

## 13.1 Federal Tier (Tier 1)
Must surface:
- National Heritage Areas
- National Scenic River Corridors
- Multi-state heritage or conservation networks

## 13.2 State Tier (Tier 2)
Must surface:
- State Scenic River Corridors
- Statewide heritage or conservation networks
- Multi-county ecological corridors
- State park systems (if treated as network)

## 13.3 District Tier (Tier 3)
Must surface:
- Park district systems
- Multi-park heritage or conservation initiatives

## 13.4 County Tier (Tier 4)
Must surface:
- County park systems
- Countywide historic districts
- Countywide conservation corridors
- Watershed-scale networks

## 13.5 Township & Municipal Tiers (Tiers 5-6)
Must surface:
- Municipal park systems
- Local historic districts
- Local cultural landscape networks

## 13.6 Conservancy Tier (Tier 7)
Must surface:
- Land trust preserve networks
- Multi-site conservation networks
- Ecological corridors
- Watershed networks

## 13.7 Private Tier (Tier 8)
May surface:
- Privately managed heritage or conservation networks
- Multi-site campus-scale networks

------------------------------------------------------------
# 14. OUTPUT REQUIREMENTS

Each Site Network candidate must output:

**Raw Discovery Record conforming to:**
- **Discovery Output Specification v5.0**
- **Site Network Schema Module v5.0**
- **Discovery Metadata Specification v5.0**

**Must include:**
- All extracted fields (raw, unnormalized)
- Complete source_map
- Member site names (if available)
- Member site count (if published)

**Must NOT include:**
- Normalized values
- Merged data from multiple sources
- Inferred member sites
- Calculated counts
- Resolved member_site_ids (normalization populates this)

------------------------------------------------------------
# 15. QUALITY CHECKLIST

Before emitting a discovery record, verify:

- ✅ network_name_raw recorded exactly as found
- ✅ Network is multi-site system (not single site with child sites)
- ✅ Network is not just marketing label or informal grouping
- ✅ All available fields extracted
- ✅ source_map populated with URL → fields mapping
- ✅ member_site_names_raw recorded if member sites listed
- ✅ member_count_raw recorded if published
- ✅ ownership recorded if meaningful (often blank for coordinating bodies)
- ✅ No normalization or standardization applied
- ✅ No calculated or estimated values
- ✅ No inferred member sites

------------------------------------------------------------
# 16. INTEGRATION POINTS

This module integrates with:

- **Discovery Protocol Module v5.0**
- **Tier Sub-Procedure Template v5.0**
- **Site Network Schema Module v5.0**
- **Site Network Vocabulary Module v5.0**
- **Site Discovery Sub-Procedure v5.0**
- **Trail Network Discovery Sub-Procedure v5.0**
- **Discovery Output Specification v5.0**
- **Discovery Metadata Specification v5.0**
- **Resolution Engine v5.0**
- **Normalization Engine v5.0**
- **TSV Output Specifications v5.0**
- **Audit & Logging Module v5.0**

------------------------------------------------------------
# END OF SITE NETWORK DISCOVERY SUB-PROCEDURE v5.0
