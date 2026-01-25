# NATURAL AREAS PROJECT
# SITE DISCOVERY SUB‑PROCEDURE v4.0
(Authoritative Sub‑Procedure for Discovering Sites and Child Sites)

This module defines the authoritative, deterministic workflow for discovering
**Sites** (including **child Sites**) across all discovery tiers within the
v4.0 Raw → Resolution → Normalization → Entity Graph pipeline.

This document supersedes all v3.x Site discovery logic.  
It introduces enumerative + recursive discovery, raw‑layer output, and
provenance‑driven extraction.

This module contains no controlled vocabularies.  
All vocabularies are defined in the **Site Vocabulary Module v4.0**.

------------------------------------------------------------
# 1. PURPOSE

The Site Discovery Sub‑Procedure v4.0 provides the authoritative workflow for:

- Identifying Site and child Site candidates  
- Extracting raw, unnormalized metadata  
- Supporting enumerative and recursive discovery  
- Preventing misclassification across the six‑entity ontology  
- Recording tier and URL provenance  
- Emitting Raw Discovery Records v4.0  
- Emitting Discovery Metadata v4.0  
- Integrating cleanly with Resolution Engine v4.0  

A **Site** is:

- A named, identity‑bearing land unit  
- Documented in authoritative sources  
- May be a top‑level Site or a child Site  
- Distinct from Trails, Trail Segments, Trail Networks, Site Networks, and Access Points  
- Not an amenity, feature, or temporary management zone  

A **child Site** is an internal identity‑bearing unit that meets the criteria in
the **Child Site Rules Module v4.0** and is represented as a **Site with a Parent Site**.

This module is authoritative for Site discovery.

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

Each tier must surface Site candidates when applicable.

------------------------------------------------------------
# 3. REQUIRED SOURCES

Each tier must check the following for Site references:

- Official agency websites  
- Authoritative listing/index pages (e.g., `/parks/`, `/properties/`)  
- GIS systems and parcel‑level data  
- Park district site lists  
- State and federal inventories  
- Planning and stewardship documents  
- County auditor parcel data  
- Brochures and downloadable maps  
- Historic district or cultural landscape documentation  
- Land trust preserve lists  
- Private organization site lists  
- Partnership announcements  

All sources must be logged in **Discovery Metadata v4.0**.

------------------------------------------------------------
# 4. IDENTITY RULES FOR SITE CANDIDATES

A Site candidate is valid only if:

1. It is explicitly documented as an identity‑bearing land unit.  
2. It has a stable, identity‑bearing name.  
3. It is not a Trail, Trail Segment, Trail Network, or Site Network.  
4. It is not an Access Point.  
5. It is not an amenity or feature (e.g., playground, overlook, shelter).  
6. It is not a temporary or unnamed management zone.  
7. It is not a parcel unless documented as a Site.  

A candidate may be a **child Site** if:

- It is an internal identity‑bearing unit within a larger Site, AND  
- It meets the criteria in the **Child Site Rules Module v4.0**.

If any required condition fails, the candidate must not be created.

------------------------------------------------------------
# 5. DISCOVERY WORKFLOW

The Site Discovery Sub‑Procedure v4.0 participates in both:

- **Enumerative discovery** (via Tier Sub‑Procedures)  
- **Recursive discovery** (via URL propagation)  

This section defines the Site‑specific extraction workflow.

------------------------------------------------------------
## 5.1 Step 1 — Identify Named Identity‑Bearing Land Units

Search all required sources for:

- Parks  
- Preserves  
- Natural areas  
- Wildlife areas  
- Forests  
- Conservation areas  
- Historic sites  
- Cemeteries  
- Campuses  
- Recreation areas  
- Cultural or heritage sites  
- Multi‑parcel conservation lands  

Record each appearance as a raw Site candidate.

------------------------------------------------------------
## 5.2 Step 2 — Verify Identity‑Bearing Name

A Site must have:

- A documented, stable name  
- Not a temporary project name  
- Not a marketing slogan  
- Not a generic label unless officially used  

If ambiguous, flag for review in metadata.

------------------------------------------------------------
## 5.3 Step 3 — Determine Whether the Candidate Is a Child Site

If the candidate appears to be an internal unit:

- Evaluate using the **Child Site Rules Module v4.0**  
- If valid → record Parent Site relationship (raw)  
- If not valid → treat as a feature or ignore  

------------------------------------------------------------
## 5.4 Step 4 — Confirm Site‑Level Identity

The candidate must:

- Represent a full identity‑bearing land unit  
- Not be a Trail or Trail Network  
- Not be a Site Network  
- Not be an amenity or feature  

If unclear, flag for review.

------------------------------------------------------------
## 5.5 Step 5 — Extract Required Metadata (Raw Fields)

Extract **all raw, unnormalized values** required for downstream processing:

### Identity & Classification
- `name_raw`  
- `category_raw`  
- `subtype_raw`  
- `designation_raw`  

### Governance
- `ownership_raw`  
- `management_raw`  
- `coordination_raw`  
- `network_affiliation_raw`  

### Descriptive
- `description_raw`  
- `notes_raw`  

### Spatial
- `address_raw`  
- `acres_raw`  
- `municipality_raw`  
- `township_raw`  
- `county_raw`  
- `gps_raw`  

### URLs
- `url_primary_raw`  
- `url_all_raw`  
- `map_url_raw`  

### Parent Site
- `parent_site_raw` (for child Sites)  

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

- Extract Site polygon or centroid  
- Do not simplify or infer geometry  
- Preserve coordinate precision  

------------------------------------------------------------
## 5.7 Step 7 — Log Internal Units (Non‑Authoritative)

Record any internal identity‑bearing units referenced.  
These become child Site candidates.

------------------------------------------------------------
## 5.8 Step 8 — Log Trails and Access Points (Non‑Authoritative)

Record any Trails or Access Points associated with the Site.  
These become authoritative in their respective discovery tracks.

------------------------------------------------------------
## 5.9 Step 9 — Emit Raw Discovery Record

Produce a Raw Discovery Record following:

- **Discovery Output Specification v4.0**  
- **Discovery Metadata Specification v4.0**  
- **Site Schema Module v4.0**  

------------------------------------------------------------
# 6. TIER‑SPECIFIC EXPECTATIONS

## 6.1 Federal Tier
Must surface:

- National parks  
- National wildlife refuges  
- National forests  
- National historic sites  
- Federally managed recreation areas  

## 6.2 State Tier
Must surface:

- State parks  
- State forests  
- State wildlife areas  
- State nature preserves  
- State historic sites  

## 6.3 District Tier
Must surface:

- All district‑managed parks  
- All district‑managed preserves  
- All district‑managed natural areas  

## 6.4 County Tier
May surface:

- County‑managed parks  
- County‑managed natural areas  

## 6.5 Township & Municipal Tiers
Must surface:

- Township parks  
- Municipal parks  
- Municipal natural areas  
- Municipal historic sites  

## 6.6 Conservancy Tier
Must surface:

- Preserves  
- Conservation areas  
- Natural areas under management  

## 6.7 Private Tier
May surface:

- Privately managed natural areas  
- Privately managed historic sites  
- Campus‑scale identity‑bearing land units  

------------------------------------------------------------
# 7. CONSOLIDATION (REMOVED IN v4.0)

Discovery v4.0 performs **no consolidation**.

All consolidation is performed by the **Resolution Engine v4.0**, which:

- Merges identical Sites across tiers  
- Preserves conflicts  
- Aligns Parent Site relationships  
- Aligns Trails and Access Points  
- Preserves provenance  

------------------------------------------------------------
# 8. OUTPUT REQUIREMENTS

Each Site candidate must output:

- All fields required by the **Site Schema Module v4.0**  
- **Discovery Metadata v4.0**  
- Source references  
- Non‑authoritative child Site references  
- Non‑authoritative Trail and Access Point references  
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
- **Site Schema Module v4.0**  
- **Site Vocabulary Module v4.0**  
- **Child Site Rules Module v4.0**  
- **Trail Discovery Sub‑Procedure v4.0**  
- **Trail Segment Discovery Sub‑Procedure v4.0**  
- **Access Point Discovery Sub‑Procedure v4.0**  
- **Site Network Discovery Sub‑Procedure v4.0**  
- **Resolution Engine v4.0**  
- **Normalization Engine v4.0**  
- **TSV Output Specifications v4.0**  
- **Audit & Logging Module v4.0**  

------------------------------------------------------------
# END OF SITE DISCOVERY SUB‑PROCEDURE v4.0