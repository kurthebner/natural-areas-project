# NATURAL AREAS PROJECT
# TRAIL NETWORK DISCOVERY SUB‑PROCEDURE v4.0
(Authoritative Sub‑Procedure for Discovering Trail Networks)

This module defines the authoritative, deterministic workflow for discovering
**Trail Networks** across all discovery tiers within the v4.0
Raw → Resolution → Normalization → Entity Graph pipeline.

This document supersedes all v3.x Trail Network discovery logic.  
It introduces enumerative + recursive discovery, raw‑layer output, and
provenance‑driven extraction.

This module contains no controlled vocabularies.  
All vocabularies are defined in the **Trail Network Vocabulary Module v4.0**.

------------------------------------------------------------
# 1. PURPOSE

The Trail Network Discovery Sub‑Procedure v4.0 provides the authoritative workflow for:

- Identifying Trail Network candidates  
- Extracting raw, unnormalized metadata  
- Supporting enumerative and recursive discovery  
- Preventing misclassification across the six‑entity ontology  
- Recording tier and URL provenance  
- Emitting Raw Discovery Records v4.0  
- Emitting Discovery Metadata v4.0  
- Integrating cleanly with Trail, Trail Segment, and Site Network discovery  
- Feeding the Resolution Engine v4.0  

A **Trail Network** is:

- A named, identity‑bearing umbrella entity  
- Composed of multiple Trails  
- Documented in authoritative sources  
- Distinct from its member Trails  
- Not a marketing label or informal grouping  
- Not a single Trail with multiple Segments  

This module is authoritative for Trail Network discovery.

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

Each tier must surface Trail Network candidates when applicable.

------------------------------------------------------------
# 3. REQUIRED SOURCES

Each tier must check the following for Trail Network references:

- Official agency websites  
- Authoritative listing/index pages (e.g., `/trails/`, `/systems/`)  
- GIS systems and interactive trail maps  
- Regional trail plans  
- Greenway or bikeway master plans  
- Statewide trail system documents  
- National Trail System documentation  
- Multi‑trail corridor plans  
- Partnership announcements  
- Regional mobility or recreation initiatives  
- Multi‑trail branding or signage programs  

All sources must be logged in **Discovery Metadata v4.0**.

------------------------------------------------------------
# 4. IDENTITY RULES FOR TRAIL NETWORK CANDIDATES

A Trail Network candidate is valid only if:

1. It is explicitly documented as a **multi‑trail system**.  
2. It has a **stable, identity‑bearing name**.  
3. It is composed of **two or more Trails**.  
4. It is distinct from its member Trails.  
5. It is not merely a marketing label or informal grouping.  
6. It is not a Site Network.  
7. It is not a single Trail with multiple Segments.  

If any condition fails, the candidate must not be created.

------------------------------------------------------------
# 5. DISCOVERY WORKFLOW

The Trail Network Discovery Sub‑Procedure v4.0 participates in both:

- **Enumerative discovery** (via Tier Sub‑Procedures)  
- **Recursive discovery** (via URL propagation)  

This section defines the Trail Network‑specific extraction workflow.

------------------------------------------------------------
## 5.1 Step 1 — Identify Named Multi‑Trail Systems

Search all required sources for:

- Regional trail networks  
- Greenway systems  
- Bikeway networks  
- Multi‑trail corridors  
- Statewide trail systems  
- National Trail System components  
- Multi‑trail recreation or mobility networks  

Record each appearance as a raw Trail Network candidate.

------------------------------------------------------------
## 5.2 Step 2 — Verify Identity‑Bearing Name

A Trail Network must have:

- A documented, stable name  
- Not a temporary project name  
- Not a marketing slogan  

If ambiguous, flag for review in metadata.

------------------------------------------------------------
## 5.3 Step 3 — Confirm Multi‑Trail Composition

The candidate must include:

- Two or more Trails  
- Documented membership  
- Explicit geographic or thematic linkage  

Do not infer membership.

------------------------------------------------------------
## 5.4 Step 4 — Extract Required Metadata (Raw Fields)

Extract **all raw, unnormalized values** required for downstream processing:

### Identity & Classification
- `network_name_raw`  
- `network_type_raw`  

### Descriptive
- `description_raw`  
- `notes_raw`  

### Spatial
- `counties_raw`  
- `states_raw` (if multi‑state)  

### Governance
- `managing_agency_raw`  

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
## 5.5 Step 5 — Log Member Trails (Non‑Authoritative)

Record all Trails referenced as members.  
Membership becomes authoritative during Resolution + Normalization.

------------------------------------------------------------
## 5.6 Step 6 — Emit Raw Discovery Record

Produce a Raw Discovery Record following:

- **Discovery Output Specification v4.0**  
- **Discovery Metadata Specification v4.0**  
- **Trail Network Schema Module v4.0**  

------------------------------------------------------------
# 6. TIER‑SPECIFIC EXPECTATIONS

## 6.1 Federal Tier
Must surface:

- National Scenic Trails  
- National Historic Trails  
- National Recreation Trail Networks  
- Multi‑state trail systems  

## 6.2 State Tier
Must surface:

- Statewide trail systems  
- State‑designated greenway networks  
- Multi‑county trail corridors  

## 6.3 District Tier
May surface:

- Regional greenway networks  
- Multi‑trail recreation systems  

## 6.4 County Tier
May surface:

- Countywide bikeway networks  
- Countywide greenway systems  

## 6.5 Township & Municipal Tiers
May surface:

- Local trail networks  
- Multi‑trail corridor initiatives  

## 6.6 Conservancy Tier
May surface:

- Multi‑trail conservation corridors  
- Regional trail initiatives  

## 6.7 Private Tier
May surface:

- Privately managed trail systems  
- Campus‑scale multi‑trail networks  

------------------------------------------------------------
# 7. CONSOLIDATION (REMOVED IN v4.0)

Discovery v4.0 performs **no consolidation**.

All consolidation is performed by the **Resolution Engine v4.0**, which:

- Merges identical Trail Networks across tiers  
- Preserves conflicts  
- Aligns member Trails with normalized Trail records  
- Preserves provenance  

------------------------------------------------------------
# 8. OUTPUT REQUIREMENTS

Each Trail Network candidate must output:

- All fields required by the **Trail Network Schema Module v4.0**  
- **Discovery Metadata v4.0**  
- Raw member Trail references  
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
- **Trail Network Schema Module v4.0**  
- **Trail Network Vocabulary Module v4.0**  
- **Trail Discovery Sub‑Procedure v4.0**  
- **Trail Segment Discovery Sub‑Procedure v4.0**  
- **Site Network Discovery Sub‑Procedure v4.0**  
- **Resolution Engine v4.0**  
- **Normalization Engine v4.0**  
- **TSV Output Specifications v4.0**  
- **Audit & Logging Module v4.0**  

------------------------------------------------------------
# END OF TRAIL NETWORK DISCOVERY SUB‑PROCEDURE v4.0