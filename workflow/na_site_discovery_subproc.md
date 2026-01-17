# NATURAL AREAS PROJECT — SITE DISCOVERY SUB‑PROCEDURE v3.1
Authoritative, versioned sub‑procedure for discovering Sites in the statewide
Natural Areas & Trails system.

This module defines:
- The Site discovery workflow
- Required sources
- Identity rules for Site candidates
- Tier‑specific discovery expectations
- Output requirements
- Integration points

This module contains no controlled vocabularies.
All vocabularies are defined in the Site Vocabulary Module v2.

------------------------------------------------------------
# 1. PURPOSE
The Site Discovery Sub‑Procedure v3.1 provides the authoritative, deterministic
workflow for discovering Sites across all eight discovery tiers.

A Site is:
- An identity‑bearing land unit
- Documented in authoritative sources
- Distinct from Sub‑Sites
- Distinct from Trails, Trail Segments, Trail Networks, and Site Networks
- Not an amenity or feature

This sub‑procedure ensures:
- Consistent identification of Sites
- Prevention of misclassification across the 7‑entity ontology
- Proper metadata capture
- Clean integration with Sub‑Site, Trail, and Access Point discovery

This module is authoritative for Site discovery.

------------------------------------------------------------
# 2. SCOPE
This sub‑procedure applies to all eight discovery tiers:

1. Federal  
2. State  
3. Park District  
4. County  
5. Township  
6. Municipal  
7. Land Trust & Conservancy  
8. Private & Organization‑Based  

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

All sources must be logged in Discovery Metadata.

------------------------------------------------------------
# 4. IDENTITY RULES FOR SITE CANDIDATES
A Site candidate is valid only if:

1. It is explicitly documented as an identity‑bearing land unit.  
2. It has a stable, identity‑bearing name.  
3. It is not a Sub‑Site (unless Parent Site is documented).  
4. It is not a Trail, Trail Segment, Trail Network, or Site Network.  
5. It is not an Access Point.  
6. It is not an amenity or feature (e.g., playground, shelter, overlook).  
7. It is not a temporary or unnamed management zone.  
8. It is not a parcel unless documented as a Site.  

If any of these conditions fail, the candidate must not be created.

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
- Not a generic label (e.g., “North Area”) unless officially used

If ambiguous, flag for review.

## 5.3 Step 3 — Confirm Site‑Level Identity
The candidate must:
- Represent a full identity‑bearing land unit
- Not be a Sub‑Site
- Not be a Trail or Trail Network
- Not be a Site Network
- Not be an amenity or feature

If unclear, flag for review.

## 5.4 Step 4 — Extract Required Metadata
For each candidate, extract:
- Name
- Category
- Subtype (if applicable)
- Designation
- Ownership
- Management
- Coordination
- Description
- Status
- Address
- Acres
- Location
- County
- GPS coordinates
- Plus Code
- Features
- Notes
- URL
- Source tier
- Source dataset
- Discovery confidence

## 5.5 Step 5 — Extract Geometry (If Available)
If GIS data is present:
- Extract Site polygon or centroid
- Do not simplify or infer geometry
- Preserve coordinate precision

## 5.6 Step 6 — Log Sub‑Sites (Non‑Authoritative)
Record any internal units referenced.
These become authoritative during Sub‑Site discovery.

## 5.7 Step 7 — Log Trails and Access Points (Non‑Authoritative)
Record any Trails or Access Points associated with the Site.
These become authoritative in their respective discovery tracks.

## 5.8 Step 8 — Emit Raw Candidate Record
Produce a Raw Candidate Site Record following the Site Schema Module v2.0.

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
# 7. CONSOLIDATION RULES
During consolidation:
- Merge identical Site names across tiers.
- Preserve all conflicting metadata.
- Do not merge Sites with different documented names.
- Align Sub‑Sites with their parent Sites.
- Align Trails and Access Points with Sites when documented.
- Maintain all source references.

------------------------------------------------------------
# 8. OUTPUT REQUIREMENTS
Each Site candidate must output:

- All fields required by the Site Schema Module v2.0
- Discovery Metadata
- Source references
- Non‑authoritative Sub‑Site references
- Non‑authoritative Trail and Access Point references
- Geometry (if available)
- Confidence and verification placeholders

Output must conform to:
- Discovery Metadata Specification v1.0
- TSV Output Specification v2.0
- Normalization Contract v2.0

------------------------------------------------------------
# 9. INTEGRATION POINTS
This module integrates with:
- Discovery Protocol Module v3.1
- Site Schema Module v2.0
- Site Vocabulary Module v2
- Sub‑Site Discovery Sub‑Procedure v1
- Trail Discovery Sub‑Procedure v1
- Access Point Discovery Sub‑Procedure v3.1
- Normalization and Resolution Modules
- TSV Output Specifications
- Audit & Logging Module v1.1

------------------------------------------------------------
# END OF SITE DISCOVERY SUB‑PROCEDURE v3.1