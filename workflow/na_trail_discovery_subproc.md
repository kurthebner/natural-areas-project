# NATURAL AREAS PROJECT
# TRAIL DISCOVERY SUB‑PROCEDURE v4.0
(Authoritative Sub‑Procedure for Discovering Trails)

This module defines the authoritative, deterministic workflow for discovering
**Trails** across all discovery tiers within the v4.0
Raw → Resolution → Normalization → Entity Graph pipeline.

This document supersedes all v3.x Trail discovery logic.  
It introduces enumerative + recursive discovery, raw‑layer output, and
provenance‑driven extraction.

This module contains no controlled vocabularies.  
All vocabularies are defined in the **Trail Vocabulary Module v4.0**.

------------------------------------------------------------
# 1. PURPOSE

The Trail Discovery Sub‑Procedure v4.0 provides the authoritative workflow for:

- Identifying Trail candidates  
- Extracting raw, unnormalized metadata  
- Supporting enumerative and recursive discovery  
- Preventing misclassification across the six‑entity ontology  
- Recording tier and URL provenance  
- Emitting Raw Discovery Records v4.0  
- Emitting Discovery Metadata v4.0  
- Integrating cleanly with Trail Segment, Trail Network, and Access Point discovery  
- Feeding the Resolution Engine v4.0  

A **Trail** is:

- A named, identity‑bearing linear corridor  
- Documented in authoritative sources  
- Distinct from Trail Segments  
- Distinct from Trail Networks  
- Distinct from Sites and child Sites  
- Not an Access Point or amenity  
- Not a temporary or unnamed connector  

This module is authoritative for Trail discovery.

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

Each tier must surface Trail candidates when applicable.

------------------------------------------------------------
# 3. REQUIRED SOURCES

Each tier must check the following for Trail references:

- Official agency websites  
- Authoritative listing/index pages (e.g., `/trails/`, `/bikeways/`)  
- GIS systems and interactive trail maps  
- Trail brochures and downloadable maps  
- Park district trail pages  
- Statewide trail inventories  
- Federal trail inventories  
- Regional greenway or bikeway plans  
- Trail signage programs  
- Digitally documented trailhead kiosks  
- Planning documents (master plans, corridor plans)  
- Multi‑trail system documents (for individual trail extraction)  

All sources must be logged in **Discovery Metadata v4.0**.

------------------------------------------------------------
# 4. IDENTITY RULES FOR TRAIL CANDIDATES

A Trail candidate is valid only if:

1. It is explicitly documented as a **named linear corridor**.  
2. It has a **stable, identity‑bearing name**.  
3. It is **not merely a segment** of a larger Trail.  
4. It is **not a Trail Network** (umbrella over multiple Trails).  
5. It is **not a Site or child Site**.  
6. It is **not an Access Point or amenity**.  
7. It is **not a temporary or unnamed connector**.  

If any condition fails, the candidate must not be created.

------------------------------------------------------------
# 5. DISCOVERY WORKFLOW

The Trail Discovery Sub‑Procedure v4.0 participates in both:

- **Enumerative discovery** (via Tier Sub‑Procedures)  
- **Recursive discovery** (via URL propagation)  

This section defines the Trail‑specific extraction workflow.

------------------------------------------------------------
## 5.1 Step 1 — Identify Named Trails

Search all required sources for:

- Named trails  
- Named loops  
- Named linear corridors  
- Named bikeways or greenways  
- Named water trails  
- Named equestrian trails  
- Named multi‑use trails  

Record each appearance as a raw Trail candidate.

------------------------------------------------------------
## 5.2 Step 2 — Verify Identity‑Bearing Name

A Trail must have:

- A documented, stable name  
- Not a temporary project name  
- Not a marketing slogan  
- Not a generic label unless officially used  

If ambiguous, flag for review in metadata.

------------------------------------------------------------
## 5.3 Step 3 — Confirm Trail‑Level Identity

The candidate must:

- Represent a full linear corridor  
- Not be a single segment  
- Not be a cluster of segments  
- Not be a Trail Network  

If unclear, flag for review.

------------------------------------------------------------
## 5.4 Step 4 — Extract Required Metadata (Raw Fields)

Extract **all raw, unnormalized values** required for downstream processing:

### Identity & Classification
- `name_raw`  
- `alternate_names_raw`  
- `trail_type_raw`  
- `designation_raw`  

### Descriptive
- `description_raw`  
- `notes_raw`  

### Spatial
- `length_raw`  
- `counties_raw`  
- `gps_raw` (if available)  

### Governance
- `managing_agency_raw`  
- `status_raw`  

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
## 5.5 Step 5 — Log Trail Segments (Non‑Authoritative)

Record any documented segments as **raw references only**.  
Segment creation occurs in the **Trail Segment Discovery Sub‑Procedure v4.0**.

------------------------------------------------------------
## 5.6 Step 6 — Log Trail Network Membership (Non‑Authoritative)

Record any Trail Networks the Trail is part of.  
Membership becomes authoritative during Resolution + Normalization.

------------------------------------------------------------
## 5.7 Step 7 — Log Access Point References (Non‑Authoritative)

If sources show Access Points attached to the Trail:

- Record them as raw references only  
- Do not create Access Points here  
- Access Point creation occurs in the **Access Point Discovery Sub‑Procedure v4.0**  

------------------------------------------------------------
## 5.8 Step 8 — Emit Raw Discovery Record

Produce a Raw Discovery Record following:

- **Discovery Output Specification v4.0**  
- **Discovery Metadata Specification v4.0**  
- **Trail Schema Module v4.0**  

------------------------------------------------------------
# 6. TIER‑SPECIFIC EXPECTATIONS

## 6.1 Federal Tier
Must surface:

- National Scenic Trails  
- National Historic Trails  
- National Recreation Trails  
- Federally documented water trails  

## 6.2 State Tier
Must surface:

- State‑designated trails  
- Statewide trail corridors  
- State water trails  
- State greenway or bikeway systems (individual trails)  

## 6.3 District Tier
Must surface:

- All named trails within district boundaries  
- All named loops  
- All named multi‑use trails  

## 6.4 County Tier
May surface:

- Countywide bikeways  
- Countywide greenways  
- County‑managed trail corridors  

## 6.5 Township & Municipal Tiers
May surface:

- Local named trails  
- Local greenways  
- Local bikeways  

## 6.6 Conservancy Tier
May surface:

- Named trails within preserves  
- Named loops  
- Named access corridors  

## 6.7 Private Tier
May surface:

- Privately managed named trails  
- Campus‑scale trail systems (individual trails)  

------------------------------------------------------------
# 7. CONSOLIDATION (REMOVED IN v4.0)

Discovery v4.0 performs **no consolidation**.

All consolidation is performed by the **Resolution Engine v4.0**, which:

- Merges identical Trails across tiers  
- Preserves conflicts  
- Aligns Trail Segments with parent Trails  
- Aligns Trails with Trail Networks  
- Preserves provenance  

------------------------------------------------------------
# 8. OUTPUT REQUIREMENTS

Each Trail candidate must output:

- All fields required by the **Trail Schema Module v4.0**  
- **Discovery Metadata v4.0**  
- Raw segment references  
- Raw network membership references  
- Raw Access Point references  
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
- **Trail Schema Module v4.0**  
- **Trail Vocabulary Module v4.0**  
- **Trail Segment Discovery Sub‑Procedure v4.0**  
- **Trail Network Discovery Sub‑Procedure v4.0**  
- **Access Point Discovery Sub‑Procedure v4.0**  
- **Site Network Discovery Sub‑Procedure v4.0**  
- **Resolution Engine v4.0**  
- **Normalization Engine v4.0**  
- **TSV Output Specifications v4.0**  
- **Audit & Logging Module v4.0**  

------------------------------------------------------------
# END OF TRAIL DISCOVERY SUB‑PROCEDURE v4.0