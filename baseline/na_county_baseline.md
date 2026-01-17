# NATURAL AREAS PROJECT — COUNTY BASELINE MODULE v3.1
A structured, authoritative seed layer containing the initial known **identity‑bearing
records** for each of Ohio’s 88 counties. Baseline entries may represent **any**
entity type in the v3.1 ontology (Site, Sub‑Site, Access Point, Trail, Trail
Segment, Trail Network, Site Network), although in practice most baseline entries
resolve to Sites.

This module anchors discovery, ensures consistent statewide coverage, and provides
the initial identity set from which the v3.1 system expands.

This module contains no controlled vocabularies.
All vocabularies are defined in the respective Vocabulary Modules v3.1.

------------------------------------------------------------
# 1. PURPOSE

This module defines:

- How county baseline data is stored
- How Copilot loads and interprets baseline entries
- How baseline entries interact with the v3.1 discovery pipeline
- How entity type is determined for baseline entries
- How conflicts between baseline and discovered data are surfaced
- How updates to county baselines are handled
- How baseline integrates with normalization and resolution

The County Baseline Module provides the initial “known named things” for each
county. Discovery expands this list; resolution interprets it; normalization
assigns entity type; TSV output serializes it.

Baseline is **identity‑bearing**, not schema‑bearing.

------------------------------------------------------------
# 2. STRUCTURE OF COUNTY BASELINE DATA

Each county has its own spreadsheet containing:

- County Name
- A baseline list of identity‑bearing records (one per line)
- Optional notes for special cases

## 2.1 Baseline files are NOT standardized
Each county’s baseline file may use a different column order, including:

- Name | Notes | URL
- Name | URL | Notes
- Name | Type | Acres | Notes | URL
- Name | Other fields | Notes | URL
- Name | Location | Management | Notes
- Name | URL only
- Name only

The **only guaranteed invariant** is:

### **Column 1 = Name (identity anchor)**

All other fields are optional, unordered, and county‑specific.

## 2.2 Baseline entries may represent any entity type
Baseline rows may correspond to:

- Sites  
- Sub‑Sites  
- Access Points  
- Trails  
- Trail Segments  
- Trail Networks  
- Site Networks  

Entity type is **not** determined by baseline structure.  
Entity type is assigned later by **resolution + normalization**.

## 2.3 Baseline fields are treated as hints, not authoritative data
- Column order is not trusted  
- Field names are not trusted  
- Field semantics are not trusted  
- Only the **Name** column is authoritative  
- All other fields are treated as optional metadata to be interpreted later  

## 2.4 Baseline format (illustrative only)
Because formats vary, the module provides an *example*, not a rule:

    Name | Other fields | Notes | URL

This is not prescriptive.  
Normalization must handle any column order gracefully.

## 2.5 Baseline is identity‑bearing, not schema‑bearing
Baseline entries provide:

- A name  
- A hint that “this thing exists”  
- Optional metadata  

They do **not** provide:

- Entity type  
- Schema‑aligned fields  
- Relationships  
- County correctness  
- Controlled vocabulary values  
- Normalized structure  

All of that is determined later in the pipeline.

------------------------------------------------------------
# 3. HOW COPILOT USES BASELINE DATA

## 3.1 Baseline as Identity Seed Layer
- All baseline entries are automatically included in the candidate list.
- Discovery adds additional entities but never removes baseline entries.
- Redundancy is surfaced for review and resolution.

## 3.2 Baseline Precedence
- Baseline names are treated as identity anchors unless contradicted by authoritative sources.
- Baseline URLs are used unless discovery finds a more authoritative link.

## 3.3 Baseline Fields Are Not Final
- Discovery and normalization refine or expand baseline fields.
- Baseline data is treated as “minimum viable information.”

## 3.4 Baseline Does Not Override Schema
- If a baseline entry violates schema rules, normalization corrects it.
- Conflicts with authoritative sources are surfaced.
- Entity type is determined by normalization, not baseline.

------------------------------------------------------------
# 4. HOW DISCOVERY INTERACTS WITH BASELINE

## 4.1 Discovery Adds, Never Deletes
- Discovery may add new entities not in the baseline.
- Discovery never removes baseline entries, even if renamed or merged.
- Renames and merges are surfaced for review.

## 4.2 Discovery May Update Baseline Fields
- If discovery finds authoritative data (e.g., GPS, ownership, County), it is added.
- Baseline notes remain unless superseded by authoritative information.

## 4.3 Discovery Flags Conflicts
- Conflicts in ownership, acreage, designation, County, Category, or entity type are surfaced.

## 4.4 Baseline Is Entity‑Agnostic
- Baseline may contain:
  - Sites
  - Sub‑Sites
  - Access Points
  - Trails
  - Trail Segments
  - Trail Networks
  - Site Networks
- Normalization determines the correct entity type.

------------------------------------------------------------
# 5. BASELINE UPDATE RULES

## 5.1 User‑Driven Updates
- Only the user may add or remove baseline entries.
- Copilot may suggest additions but never modifies baseline without explicit confirmation.

## 5.2 Versioning
- Each county baseline section includes a version number.
- Changes must be documented in a simple change log.

## 5.3 Renamed Entities
- If a baseline entity is renamed, the baseline retains the original name in Notes.
- The normalized record uses the authoritative name.

## 5.4 Merged or Split Entities
- If a baseline entity is split into multiple authoritative entities, discovery adds the new ones.
- The original baseline entry remains with a note.

------------------------------------------------------------
# 6. SPECIAL CASES

## 6.1 Counties with Sparse Data
- Baseline may contain only 1–2 known entities.
- Discovery is expected to expand these significantly.

## 6.2 Counties with Large Park Districts
- Baseline may include only major Sites or Trailheads.
- Discovery must enumerate all named Sites, Sub‑Sites, Trails, and Access Points.

## 6.3 Counties with No Park District
- Baseline may rely heavily on state, municipal, and township sources.

## 6.4 Multi‑County Entities
- Baseline entries may appear in each relevant county, or only in the county
  baseline for the largest portion.
- Normalization ensures the **County** field lists all counties for Sites, Trails,
  and other multi‑county entities.

## 6.5 Internal Parcels
- Baseline may include internal identity‑bearing units (e.g., named natural areas).
- These must follow the Internal Parcel Rule in the Resolution Module v3.1.

------------------------------------------------------------
# 7. COUNTY BASELINE TEMPLATE

Each county section is a spreadsheet that roughly follows this template:

Name | Other fields | Notes | URL

Notes:

- Templates vary across counties.
- Most records are Sites, but many counties include Trailheads, Trails, or Segments.
- Entity type is not trusted; normalization determines the correct type.
- Many records do not have URLs.

------------------------------------------------------------
# 8. MODULE DEPENDENCIES

This module depends on:

- All seven Schema Modules v3.1
- All seven Vocabulary Modules v3.1
- All seven Normalization Contracts v3.1
- Discovery Protocol Module v3.1
- Resolution Module v3.1
- Processing / Orchestration Module v3.1
- Audit & Logging Module v3.1

------------------------------------------------------------
# END OF COUNTY BASELINE MODULE v3.1