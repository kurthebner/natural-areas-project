# NATURAL AREAS PROJECT
# SITE NETWORK DISCOVERY SUB‑PROCEDURE v4.0
(Authoritative Sub‑Procedure for Discovering Site Networks)

This module defines the authoritative, deterministic workflow for discovering
**Site Networks** across all discovery tiers within the v4.0  
Raw → Resolution → Normalization → Entity Graph pipeline.

This document supersedes all v3.x Site Network discovery logic.  
It introduces enumerative + recursive discovery, raw‑layer output, and
provenance‑driven extraction.

This module contains no controlled vocabularies.  
All vocabularies are defined in the **Site Network Vocabulary Module v4.0**.

------------------------------------------------------------
# 1. PURPOSE

The Site Network Discovery Sub‑Procedure v4.0 provides the authoritative workflow for:

- Identifying Site Network candidates  
- Extracting raw, unnormalized metadata  
- Supporting enumerative and recursive discovery  
- Preventing misclassification across the six‑entity ontology  
- Recording tier and URL provenance  
- Emitting Raw Discovery Records v4.0  
- Emitting Discovery Metadata v4.0  
- Integrating cleanly with Site, Trail Network, and Trail discovery  
- Feeding the Resolution Engine v4.0  

A **Site Network** is:

- A named, identity‑bearing umbrella entity  
- Composed of multiple Sites  
- Documented in authoritative sources  
- Distinct from its member Sites  
- Not a marketing label or informal grouping  
- Not a single Site with multiple child Sites  

This module is authoritative for Site Network discovery.

------------------------------------------------------------
# 2. SCOPE

This sub‑procedure applies to all discovery tiers:

1. Federal  
2. State  
3. District  
4. County  
5. Township  
6. Municipal  
7. Conservancy  
8. Private  
9. Tier‑0 Baseline (non‑authoritative; runs last)

Each tier must surface Site Network candidates when applicable.

------------------------------------------------------------
# 3. REQUIRED SOURCES

Each tier must check the following for Site Network references:

- Official agency websites  
- Authoritative listing/index pages (e.g., `/heritage/`, `/corridors/`)  
- GIS systems and interactive maps  
- Planning documents (master plans, corridor plans, heritage plans)  
- Stewardship or management plans  
- Federal and state designation documents  
- National Heritage Area documentation  
- Scenic River Corridor documentation  
- Historic District documentation  
- Watershed or ecological corridor plans  
- Partnership announcements  
- Multi‑site program pages  
- Regional conservation or heritage initiatives  

All sources must be logged in **Discovery Metadata v4.0**.

------------------------------------------------------------
# 4. IDENTITY RULES FOR SITE NETWORK CANDIDATES

A Site Network candidate is valid only if:

1. It is explicitly documented as a **multi‑site system**.  
2. It has a **stable, identity‑bearing name**.  
3. It is composed of **two or more Sites**.  
4. It is distinct from its member Sites.  
5. It is not merely a marketing label or informal grouping.  
6. It is not a Trail Network.  
7. It is not a single Site with multiple child Sites.  

If any condition fails, the candidate must not be created.

------------------------------------------------------------
# 5. DISCOVERY WORKFLOW

The Site Network Discovery Sub‑Procedure v4.0 participates in both:

- **Enumerative discovery** (via Tier Sub‑Procedures)  
- **Recursive discovery** (via URL propagation)  

This section defines the Site Network‑specific extraction workflow.

------------------------------------------------------------
## 5.1 Step 1 — Identify Named Multi‑Site Systems

Search all required sources for:

- Named corridors  
- Heritage areas  
- Historic districts  
- Scenic river systems  
- Watershed networks  
- Cultural landscape networks  
- Multi‑site conservation programs  
- Multi‑site recreation networks  

Record each appearance as a raw Site Network candidate.

------------------------------------------------------------
## 5.2 Step 2 — Verify Identity‑Bearing Name

A Site Network must have:

- A documented, stable name  
- Not a temporary project name  
- Not a marketing slogan  

If ambiguous, flag for review in metadata.

------------------------------------------------------------
## 5.3 Step 3 — Confirm Multi‑Site Composition

The candidate must include:

- Two or more Sites  
- Documented membership  
- Explicit geographic or thematic linkage  

Do not infer membership.

------------------------------------------------------------
## 5.4 Step 4 — Extract Required Metadata (Raw Fields)

Extract **all raw, unnormalized values** required for downstream processing:

### Identity & Classification
- `network_name_raw`  
- `alternate_names_raw`  
- `network_type_raw`  

### Descriptive
- `description_raw`  
- `history_raw`  
- `notes_raw`  

### Spatial
- `counties_raw`  
- `states_raw` (if multi‑state)  

### Governance
- `managing_agency_raw`  
- `secondary_managing_agencies_raw`  

### URLs
- `url_primary_raw`  
- `url_all_raw`  
- `map_url_raw`  

### Source Tracking
- `source_datasets`  
- `source_maps`  
- `source_gis_layers`  

### Tier Tracking
- `source_tier`  
- `source_system`  
- `source_url`  
- `parent_url` (if propagated)  

### Baseline Tracking
- `seeded_from_baseline`  
- `baseline_id`  

All values must be raw and unnormalized.

------------------------------------------------------------
## 5.5 Step 5 — Log Member Sites (Non‑Authoritative)

Record all Sites referenced as members.  
Membership becomes authoritative during Resolution + Normalization.

------------------------------------------------------------
## 5.6 Step 6 — Emit Raw Discovery Record

Produce a Raw Discovery Record following:

- **Discovery Output Specification v4.0**  
- **Discovery Metadata Specification v4.0**  
- **Site Network Schema Module v4.0**  

------------------------------------------------------------
# 6. TIER‑SPECIFIC EXPECTATIONS

## 6.1 Federal Tier
Must surface:

- National Heritage Areas  
- National Scenic River Corridors  
- Multi‑state heritage or conservation networks  

## 6.2 State Tier
Must surface:

- State Scenic River Corridors  
- Statewide heritage or conservation networks  
- Multi‑county ecological corridors  

## 6.3 District Tier
May surface:

- Regional greenway networks  
- Multi‑park heritage or conservation initiatives  

## 6.4 County Tier
May surface:

- Countywide historic districts  
- Countywide conservation corridors  
- Watershed‑scale networks  

## 6.5 Township & Municipal Tiers
May surface:

- Local historic districts  
- Local cultural landscape networks  

## 6.6 Conservancy Tier
May surface:

- Multi‑site conservation networks  
- Ecological corridors  
- Watershed networks  

## 6.7 Private Tier
May surface:

- Privately managed heritage or conservation networks  
- Multi‑site campus‑scale networks  

------------------------------------------------------------
# 7. CONSOLIDATION (REMOVED IN v4.0)

Discovery v4.0 performs **no consolidation**.

All consolidation is performed by the **Resolution Engine v4.0**, which:

- Merges identical Site Networks across tiers  
- Preserves conflicts  
- Aligns member Sites with normalized Site records  
- Preserves provenance  

------------------------------------------------------------
# 8. OUTPUT REQUIREMENTS

Each Site Network candidate must output:

- All fields required by the **Site Network Schema Module v4.0**  
- **Discovery Metadata v4.0**  
- Raw member Site references  
- Raw values only (no normalization)  

Output must conform to:

- **Discovery Metadata Specification v4.0**  
- **Discovery Output Specification v4.0**  
- **Normalization Engine v4.0** (downstream)  

------------------------------------------------------------
# 9. INTEGRATION POINTS

This module integrates with:

- **Discovery Protocol Module v4.0**  
- **Tier Sub‑Procedure Template v4.0**  
- **Site Network Schema Module v4.0**  
- **Site Network Vocabulary Module v4.0**  
- **Site Discovery Sub‑Procedure v4.0**  
- **Trail Network Discovery Sub‑Procedure v4.0**  
- **Resolution Engine v4.0**  
- **Normalization Engine v4.0**  
- **TSV Output Specifications v4.0**  
- **Audit & Logging Module v4.0**  

------------------------------------------------------------
# END OF SITE NETWORK DISCOVERY SUB‑PROCEDURE v4.0