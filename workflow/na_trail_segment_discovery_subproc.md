# NATURAL AREAS PROJECT
# TRAIL SEGMENT DISCOVERY SUB‑PROCEDURE v4.0
(Authoritative Sub‑Procedure for Discovering Trail Segments)

This module defines the authoritative, deterministic workflow for discovering
**Trail Segments** across all discovery tiers within the v4.0
Raw → Resolution → Normalization → Entity Graph pipeline.

This document supersedes all v3.x Trail Segment discovery logic.  
It introduces enumerative + recursive discovery, raw‑layer output, and
provenance‑driven extraction.

This module contains no controlled vocabularies.  
All vocabularies are defined in the **Trail Segment Vocabulary Module v4.0**.

------------------------------------------------------------
# 1. PURPOSE

The Trail Segment Discovery Sub‑Procedure v4.0 provides the authoritative workflow for:

- Identifying Trail Segment candidates  
- Extracting raw, unnormalized metadata  
- Supporting enumerative and recursive discovery  
- Preventing misclassification across the six‑entity ontology  
- Recording tier and URL provenance  
- Emitting Raw Discovery Records v4.0  
- Emitting Discovery Metadata v4.0  
- Integrating cleanly with Trail, Trail Network, and Access Point discovery  
- Feeding the Resolution Engine v4.0  

A **Trail Segment** is:

- An identity‑bearing operational portion of a Trail  
- Documented in authoritative sources  
- Distinct from the Trail itself  
- Distinct from Access Points  
- Distinct from Trail Networks  
- Not a Site or child Site  
- Not a temporary or unnamed connector  

This module is authoritative for Trail Segment discovery.

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

Each tier must surface Trail Segment candidates when applicable.

------------------------------------------------------------
# 3. REQUIRED SOURCES

Each tier must check the following for Trail Segment references:

- Official agency trail maps  
- GIS systems with segment‑level geometry  
- Trail brochures showing named or numbered segments  
- Park district trail pages with segment breakdowns  
- Statewide trail inventories with segment IDs  
- Federal trail inventories with segment IDs  
- Corridor plans showing segment delineation  
- Digitally documented trail signage  
- Multi‑trail system documents (for segment extraction)  

All sources must be logged in **Discovery Metadata v4.0**.

------------------------------------------------------------
# 4. IDENTITY RULES FOR TRAIL SEGMENT CANDIDATES

A Trail Segment candidate is valid only if:

1. It is explicitly documented as a **portion of a Trail**.  
2. It has a **stable identity** within the parent Trail.  
3. It is **not itself a Trail**.  
4. It is **not a Trail Network**.  
5. It is **not an Access Point**.  
6. It is **not a temporary or unnamed connector**.  
7. It is **not a Site or child Site**.  

If any condition fails, the candidate must not be created.

------------------------------------------------------------
# 5. DISCOVERY WORKFLOW

The Trail Segment Discovery Sub‑Procedure v4.0 participates in both:

- **Enumerative discovery** (via Tier Sub‑Procedures)  
- **Recursive discovery** (via URL propagation)  

This section defines the Trail Segment‑specific extraction workflow.

------------------------------------------------------------
## 5.1 Step 1 — Identify Segment‑Level Documentation

Search all required sources for:

- Named segments  
- Numbered segments  
- GIS‑defined segments  
- Operational segments (e.g., “North Section,” “Riverside Segment”)  
- Segments with distinct surface types or statuses  
- Segments with distinct management  

Record each appearance as a raw Trail Segment candidate.

------------------------------------------------------------
## 5.2 Step 2 — Verify Segment Identity

A Trail Segment must:

- Be part of a specific parent Trail  
- Have a documented boundary or identity  
- Not be a full Trail  
- Not be a Trail Network  

If ambiguous, flag for review in metadata.

------------------------------------------------------------
## 5.3 Step 3 — Confirm Parent Trail (Single‑Parent Rule)

Each Trail Segment must have:

- **Exactly one parent Trail**  
- A documented relationship to that Trail  
- No inferred parentage  

Rules:

- If multiple Trails share the same corridor, Discovery must create  
  **parallel segments**, one per parent Trail.  
- Shared‑treadway situations do **not** create multi‑parent segments.  
- If the parent Trail has not yet been discovered, create a  
  **placeholder Trail Raw Discovery Record**.

------------------------------------------------------------
## 5.4 Step 4 — Extract Required Metadata (Raw Fields)

Extract **all raw, unnormalized values** required for downstream processing:

### Identity & Classification
- `segment_name_raw` or `segment_identifier_raw`  
- `parent_trail_raw`  

### Descriptive
- `description_raw`  
- `notes_raw`  

### Spatial
- `length_raw`  
- `surface_type_raw`  
- `status_raw`  
- `counties_raw`  
- `gps_raw` (if available)  

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
## 5.5 Step 5 — Extract Geometry (If Available)

If GIS data is present:

- Extract segment geometry  
- Do not simplify or infer geometry  
- Preserve coordinate precision  

------------------------------------------------------------
## 5.6 Step 6 — Log Access Points (Non‑Authoritative)

Record any Access Points associated with the segment.  
These become authoritative during Access Point discovery.

------------------------------------------------------------
## 5.7 Step 7 — Emit Raw Discovery Record

Produce a Raw Discovery Record following:

- **Discovery Output Specification v4.0**  
- **Discovery Metadata Specification v4.0**  
- **Trail Segment Schema Module v4.0**  

------------------------------------------------------------
# 6. TIER‑SPECIFIC EXPECTATIONS

## 6.1 Federal Tier
May surface:

- Segment‑level geometry for National Scenic Trails  
- Segment IDs for National Historic Trails  

## 6.2 State Tier
Must surface:

- Segment‑level breakdowns for state‑managed trails  
- Statewide trail inventory segments  

## 6.3 District Tier
Must surface:

- All named or numbered segments  
- Operational segments (e.g., “North Loop Section”)  

## 6.4 County Tier
May surface:

- County‑managed trail segments  
- Bikeway segments  

## 6.5 Township & Municipal Tiers
May surface:

- Local trail segments  
- Local bikeway segments  

## 6.6 Conservancy Tier
May surface:

- Segment‑level breakdowns within preserves  

## 6.7 Private Tier
May surface:

- Privately managed segment‑level trails  
- Campus‑scale segment delineations  

------------------------------------------------------------
# 7. CONSOLIDATION (REMOVED IN v4.0)

Discovery v4.0 performs **no consolidation**.

All consolidation is performed by the **Resolution Engine v4.0**, which:

- Merges identical segments only if they share the same parent Trail  
- Preserves conflicts  
- Aligns segments with their parent Trail  
- Preserves provenance  

------------------------------------------------------------
# 8. OUTPUT REQUIREMENTS

Each Trail Segment candidate must output:

- All fields required by the **Trail Segment Schema Module v4.0**  
- **Discovery Metadata v4.0**  
- Raw Access Point references  
- Geometry (if available)  
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
- **Trail Segment Schema Module v4.0**  
- **Trail Segment Vocabulary Module v4.0**  
- **Trail Discovery Sub‑Procedure v4.0**  
- **Trail Network Discovery Sub‑Procedure v4.0**  
- **Access Point Discovery Sub‑Procedure v4.0**  
- **Resolution Engine v4.0**  
- **Normalization Engine v4.0**  
- **TSV Output Specifications v4.0**  
- **Audit & Logging Module v4.0**  

------------------------------------------------------------
# END OF TRAIL SEGMENT DISCOVERY SUB‑PROCEDURE v4.0