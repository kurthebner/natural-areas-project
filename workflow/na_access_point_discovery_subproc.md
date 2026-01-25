# NATURAL AREAS PROJECT
# ACCESS POINT DISCOVERY SUB‑PROCEDURE v4.0
(Authoritative Sub‑Procedure for Discovering Access Points)

This module defines the authoritative, deterministic workflow for discovering
**Access Points** across all discovery tiers within the v4.0
Raw → Resolution → Normalization → Entity Graph pipeline.

This document supersedes all v3.x Access Point discovery logic.
It introduces enumerative + recursive discovery, raw‑layer output, multi‑parent
Access Points, and provenance‑driven extraction.

This module contains no controlled vocabularies.
All vocabularies are defined in the **Access Point Vocabulary Module v4.0**.

------------------------------------------------------------
# 1. PURPOSE

The Access Point Discovery Sub‑Procedure v4.0 provides the authoritative workflow for:

- Identifying Access Point candidates  
- Extracting raw, unnormalized metadata  
- Supporting enumerative and recursive discovery  
- Preventing misclassification across the six‑entity ontology  
- Recording tier and URL provenance  
- Emitting Raw Discovery Records v4.0  
- Emitting Discovery Metadata v4.0  
- Integrating cleanly with Site, Trail, and Trail Segment discovery  
- Feeding the Resolution Engine v4.0  

An **Access Point** is:

- A visitor‑facing navigational entry location  
- Documented in authoritative sources  
- Attached to one or more identity‑bearing parent entities  
  (**Site, Trail, or Trail Segment**)  
- Classified using the Access Point Vocabulary Module v4.0  
- Not a feature, amenity, or non‑navigational point  

This module is authoritative for Access Point discovery.

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

Each tier must surface Access Point candidates when applicable.

------------------------------------------------------------
# 3. REQUIRED SOURCES

Each tier must check the following for Access Point references:

- Official agency maps  
- GIS layers showing trailheads, parking, boat ramps, etc.  
- Park district trail maps  
- State and federal recreation maps  
- Brochures and downloadable PDFs  
- Digitally documented trailhead kiosks  
- Planning documents (master plans, corridor plans)  
- Stewardship or restoration plans  
- Land trust preserve maps  
- Municipal park maps  
- County recreation maps  
- Digitally documented signage programs  

All sources must be logged in **Discovery Metadata v4.0**.

------------------------------------------------------------
# 4. IDENTITY RULES FOR ACCESS POINT CANDIDATES

A valid Access Point candidate must satisfy all of the following:

1. It is explicitly documented as a **visitor‑facing entry location**.  
2. It has a **documented geographic point** (coordinate, map marker, GIS point).  
   - Discovery must **not infer** coordinates.  
3. It is not a Site, child Site, Trail, or Trail Segment.  
4. It is not a feature or amenity (e.g., shelter, overlook, playground).  
5. It is not a parking lot unless it functions as an entry point.  
6. It is not a road intersection unless documented as an entry point.  
7. It is not a temporary or unnamed connector.  
8. It attaches to **one or more identity‑bearing parent entities**  
   (Site, Trail, Trail Segment).  
9. It must never attach to Site Networks or Trail Networks.  

If any condition fails, the candidate must not be created.

------------------------------------------------------------
# 5. DISCOVERY WORKFLOW

The Access Point Discovery Sub‑Procedure v4.0 participates in both:

- **Enumerative discovery** (via Tier Sub‑Procedures)  
- **Recursive discovery** (via URL propagation)  

This section defines the Access Point‑specific extraction workflow.

------------------------------------------------------------
## 5.1 Step 1 — Identify Access Point Candidates

Search all required sources for:

- Trailheads  
- Parking areas that serve as entry points  
- Boat ramps  
- Watercraft access points  
- Fishing access points  
- Equestrian access points  
- Bicycle access points  
- Pedestrian access points  
- Scenic overlook pull‑offs (if documented as entry)  
- Gateways or entrances  
- Named or mapped access nodes  

Record each appearance as a raw Access Point candidate.

------------------------------------------------------------
## 5.2 Step 2 — Verify Access Point Identity

An Access Point must:

- Be a visitor‑facing entry location  
- Have a documented geographic point  
- Not be an amenity or feature  
- Not be a Site, child Site, Trail, or Trail Segment  

If ambiguous, flag for review in metadata.

------------------------------------------------------------
## 5.3 Step 3 — Assign Access Point Type

Assign a type from the **Access Point Vocabulary Module v4.0**.

If unclear, leave blank and flag for review.

------------------------------------------------------------
## 5.4 Step 4 — Confirm Parent Entities (Multi‑Parent Rule)

Each Access Point may attach to **one or more** of the following:

- Site  
- Trail  
- Trail Segment  

Rules:

- Parentage must reflect what the source explicitly shows.  
- Do not infer parentage unless the map or source clearly indicates it.  
- If multiple parents are documented, **preserve all of them**.  
- If a parent entity has not yet been discovered, create a  
  **placeholder Raw Discovery Record** with:  
  - correct entity_type  
  - minimal raw values  
  - no invented fields  
  - metadata flag `placeholder_parent = true`  
- Site Networks and Trail Networks must **not** be treated as parents.  
- Access Points may temporarily have zero parents until placeholders resolve.

------------------------------------------------------------
## 5.5 Step 5 — Extract Required Metadata (Raw Fields)

Extract **all raw, unnormalized values** required for downstream processing:

### Identity & Classification
- `access_point_name_raw` (if present)  
- `access_point_type_raw`  

### Parentage
- `parent_sites_raw`  
- `parent_trails_raw`  
- `parent_trail_segments_raw`  

### Spatial
- `coordinates_raw` or `latitude_raw` / `longitude_raw`  
- `plus_code_raw` (if present)  
- `counties_raw`  
  - Must preserve the raw county list exactly as discovered  
  - Must follow the **universal multi‑county rule v4.0**  

### Descriptive
- `status_raw`  
- `description_raw`  
- `notes_raw`  

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
## 5.6 Step 6 — Extract Geometry (If Available)

If GIS data is present:

- Extract point geometry  
- Do not infer or adjust coordinates  
- Preserve coordinate precision  

------------------------------------------------------------
## 5.7 Step 7 — Emit Raw Discovery Record

Produce a Raw Discovery Record following:

- **Discovery Output Specification v4.0**  
- **Discovery Metadata Specification v4.0**  
- **Access Point Schema Module v4.0**  

------------------------------------------------------------
# 6. TIER‑SPECIFIC EXPECTATIONS

## 6.1 Federal Tier
Must surface:

- Trailheads for National Scenic Trails  
- Access points for National Parks and Refuges  
- Boat ramps and water access points  

## 6.2 State Tier
Must surface:

- Trailheads for state parks, forests, and wildlife areas  
- Boat ramps and fishing access points  
- Statewide trail system access points  

## 6.3 District Tier
Must surface:

- All district‑managed trailheads  
- All district‑managed parking‑based access points  
- All district‑managed water access points  

## 6.4 County Tier
May surface:

- County‑managed trailheads  
- County‑managed access points  

## 6.5 Township & Municipal Tiers
May surface:

- Local trailheads  
- Local park access points  

## 6.6 Conservancy Tier
Must surface:

- Preserve access points  
- Trailheads within conservation areas  

## 6.7 Private Tier
May surface:

- Privately managed access points  
- Campus‑scale access nodes  

------------------------------------------------------------
# 7. CONSOLIDATION (REMOVED IN v4.0)

Discovery v4.0 performs **no consolidation**.

All consolidation is performed by the **Resolution Engine v4.0**, which:

- Merges identical Access Points across tiers  
- Preserves conflicts  
- Aligns Access Points with all discovered parent entities  
- Preserves provenance  

------------------------------------------------------------
# 8. OUTPUT REQUIREMENTS

Each Access Point candidate must output:

- All fields required by the **Access Point Schema Module v4.0**  
- **Discovery Metadata v4.0**  
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
- **Access Point Schema Module v4.0**  
- **Access Point Vocabulary Module v4.0**  
- **Site Discovery Sub‑Procedure v4.0**  
- **Trail Discovery Sub‑Procedure v4.0**  
- **Trail Segment Discovery Sub‑Procedure v4.0**  
- **Resolution Engine v4.0**  
- **Normalization Engine v4.0**  
- **TSV Output Specifications v4.0**  
- **Audit & Logging Module v4.0**  
- **Entity Graph Schema v4.0**  
- **Entity Upsert Engine v4.0**  

------------------------------------------------------------
# END OF ACCESS POINT DISCOVERY SUB‑PROCEDURE v4.0