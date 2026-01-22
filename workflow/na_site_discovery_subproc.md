# NATURAL AREAS PROJECT — SITE DISCOVERY SUB‑PROCEDURE v3.2.2
Authoritative, versioned sub‑procedure for discovering Sites (including child
Sites) in the statewide Natural Areas & Trails system.

This module defines:

- The Site discovery workflow  
- Required sources  
- Identity rules for Site and child Site candidates  
- Tier‑specific discovery expectations  
- Output requirements  
- Integration points  

This module contains no controlled vocabularies.  
All vocabularies are defined in the **Site Vocabulary Module v3.2.2**.

------------------------------------------------------------
# 1. PURPOSE

The Site Discovery Sub‑Procedure v3.2.2 provides the authoritative, deterministic
workflow for discovering Sites across all eight discovery tiers.

A Site is:

- A named, identity‑bearing land unit  
- Documented in authoritative sources  
- May be a top‑level Site or a child Site  
- Distinct from Trails, Trail Segments, Trail Networks, Site Networks, and Access Points  
- Not an amenity or feature  

Child Sites are internal identity‑bearing units that meet the criteria in the
**Child Site Rules Module v3.2.2** and are represented as **Sites with Parent Site**.

This sub‑procedure ensures:

- Consistent identification of Sites and child Sites  
- Prevention of misclassification across the six‑entity ontology  
- Proper metadata capture  
- Clean integration with Trail, Trail Segment, Site Network, and Access Point discovery  

This module is authoritative for Site discovery.

------------------------------------------------------------
# 2. SCOPE

This sub‑procedure applies to all eight discovery tiers:

1. Federal  
2. State  
3. District  
4. County  
5. Township  
6. Municipal  
7. Conservancy  
8. Private  

Each tier must surface Site candidates when applicable.

------------------------------------------------------------
# 3. REQUIRED SOURCES

Each tier must check the following for Site references:

- Official agency websites  
- GIS systems and parcel‑level data  
- Park district site lists  
- State and federal site inventories  
- Planning documents (master plans, management plans)  
- Stewardship or restoration plans  
- County auditor parcel data  
- Brochures and downloadable maps  
- Historic district or cultural landscape documentation  
- Land trust preserve lists  
- Private organization site lists  
- Partnership announcements  

All sources must be logged in **Discovery Metadata v3.2.2**.

------------------------------------------------------------
# 4. IDENTITY RULES FOR SITE CANDIDATES

A Site candidate is valid only if:

1. It is explicitly documented as an identity‑bearing land unit.  
2. It has a stable, identity‑bearing name.  
3. It is not a Trail, Trail Segment, Trail Network, or Site Network.  
4. It is not an Access Point.  
5. It is not an amenity or feature (e.g., playground, shelter, overlook).  
6. It is not a temporary or unnamed management zone.  
7. It is not a parcel unless documented as a Site.  

A candidate may be a **child Site** if:

- It is an internal identity‑bearing unit within a larger Site, AND  
- It meets the criteria in the **Child Site Rules Module v3.2.2**.  

If any required condition fails, the candidate must not be created.

------------------------------------------------------------
# 5. DISCOVERY WORKFLOW

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

Record each appearance as a raw candidate.

## 5.2 Step 2 — Verify Identity‑Bearing Name

A Site must have:

- A documented, stable name  
- Not a temporary project name  
- Not a marketing slogan  
- Not a generic label unless officially used  

If ambiguous, flag for review.

## 5.3 Step 3 — Determine Whether the Candidate Is a Child Site

If the candidate appears to be an internal unit:

- Evaluate using the **Child Site Rules Module v3.2.2**  
- If valid → record Parent Site relationship  
- If not valid → treat as a feature or ignore  

## 5.4 Step 4 — Confirm Site‑Level Identity

The candidate must:

- Represent a full identity‑bearing land unit  
- Not be a Trail or Trail Network  
- Not be a Site Network  
- Not be an amenity or feature  

If unclear, flag for review.

## 5.5 Step 5 — Extract Required Metadata (Raw Fields)

Extract **all raw, unnormalized values** required for normalization:

### Identity & Classification
- **name_raw**  
- **category_raw**  
- **subtype_raw**  
- **designation_raw**  

### Governance
- **ownership_raw**  
- **management_raw**  
- **coordination_raw**  
- **network_affiliation_raw**  

### Descriptive
- **description_raw**  
- **notes_raw**  

### Spatial
- **address_raw**  
- **acres_raw**  
- **municipality_raw**  
- **township_raw**  
- **county_raw**  
- **gps_raw**  

### URLs
- **url_primary_raw**  
- **url_all_raw**  
- **map_url_raw** (if available)  

### Parent Site
- **parent_site_raw** (for child Sites)  

### Source Tracking
- **source_datasets**  
- **source_maps**  
- **source_gis_layers**  

### Tier Tracking
- **discovery_tier**  
- **discovered_in_tiers**  

### Baseline Tracking
- **seeded_from_baseline**  
- **baseline_id**  

All values must be raw and unnormalized.

## 5.6 Step 6 — Extract Geometry (If Available)

If GIS data is present:

- Extract Site polygon or centroid  
- Do not simplify or infer geometry  
- Preserve coordinate precision  

## 5.7 Step 7 — Log Internal Units (Non‑Authoritative)

Record any internal identity‑bearing units referenced.  
These become child Site candidates.

## 5.8 Step 8 — Log Trails and Access Points (Non‑Authoritative)

Record any Trails or Access Points associated with the Site.  
These become authoritative in their respective discovery tracks.

## 5.9 Step 9 — Emit Raw Candidate Record

Produce a Raw Candidate Site Record following:

- **Discovery Output Specification v3.2.2**  
- **Discovery Metadata Specification v3.2.2**  
- **Site Schema Module v3.2.2**  

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

## 6.3 Park District Tier

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

## 6.6 Land Trust & Conservancy Tier

Must surface:

- All preserves  
- All conservation areas  
- All natural areas under management  

## 6.7 Private & Organization‑Based Tier

May surface:

- Privately managed natural areas  
- Privately managed historic sites  
- Campus‑scale identity‑bearing land units  

------------------------------------------------------------
# 7. CONSOLIDATION RULES (LOGICAL)

During consolidation:

- Merge identical Site names across tiers  
- Preserve all conflicting metadata  
- Do not merge Sites with different documented names  
- Preserve Parent Site relationships for child Sites  
- Align Trails and Access Points with Sites when documented  
- Maintain all source references  

Execution of consolidation is defined in the **Discovery Orchestration Module v3.2.2**.

------------------------------------------------------------
# 8. OUTPUT REQUIREMENTS

Each Site candidate must output:

- All fields required by the **Site Schema Module v3.2.2**  
- **Discovery Metadata v3.2.2**  
- Source references  
- Non‑authoritative child Site references  
- Non‑authoritative Trail and Access Point references  
- Geometry (if available)  
- Raw values only (no normalization)  

Output must conform to:

- **Discovery Metadata Specification v3.2.2**  
- **Discovery Output Specification v3.2.2**  
- **Normalization Contract v3.2.2**  

------------------------------------------------------------
# 9. INTEGRATION POINTS

This module integrates with:

- **Discovery Protocol Module v3.2.2**  
- **Site Schema Module v3.2.2**  
- **Site Vocabulary Module v3.2.2**  
- **Child Site Rules Module v3.2.2**  
- **Trail Discovery Sub‑Procedure v3.2.2**  
- **Trail Segment Discovery Sub‑Procedure v3.2.2**  
- **Access Point Discovery Sub‑Procedure v3.2.2**  
- **Site Network Discovery Sub‑Procedure v3.2.2**  
- **Normalization and Resolution Modules v3.2.2**  
- **TSV Output Specifications v3.2.2**  
- **Audit & Logging Module v3.2.2**  

------------------------------------------------------------
# END OF SITE DISCOVERY SUB‑PROCEDURE v3.2.2