# NATURAL AREAS PROJECT — SUB‑SITE DISCOVERY SUB‑PROCEDURE v1
Authoritative, versioned sub‑procedure for discovering Sub‑Sites in the statewide
Natural Areas & Trails system.

This module defines:
- The Sub‑Site discovery workflow
- Required sources
- Identity rules for Sub‑Site candidates
- Tier‑specific discovery expectations
- Output requirements
- Integration points

This module contains no controlled vocabularies.
All vocabularies are defined in the Sub‑Site Vocabulary Module v1.

------------------------------------------------------------
# 1. PURPOSE
The Sub‑Site Discovery Sub‑Procedure v1 provides the authoritative, deterministic
workflow for discovering Sub‑Sites across all eight discovery tiers.

A Sub‑Site is:
- An identity‑bearing internal unit within a Site
- Documented in authoritative sources
- Distinct from the parent Site
- Distinct from Trails, Trail Segments, Trail Networks, and Site Networks
- Not an amenity or feature

This sub‑procedure ensures:
- Consistent identification of Sub‑Sites
- Prevention of misclassification as Sites or Features
- Proper metadata capture
- Clean integration with Site discovery and normalization

This module is authoritative for Sub‑Site discovery.

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

Each tier must surface Sub‑Site candidates when applicable.

------------------------------------------------------------
# 3. REQUIRED SOURCES
Each tier must check the following for Sub‑Site references:

- Official Site maps
- Official Site brochures
- Park district facility maps
- State or federal unit maps
- Trailhead kiosks (digitally documented)
- GIS layers showing internal units
- Planning documents (master plans, management plans)
- Stewardship or restoration plans
- Historic district or cultural landscape documentation
- Campus‑scale or complex‑scale internal unit maps

All sources must be logged in Discovery Metadata.

------------------------------------------------------------
# 4. IDENTITY RULES FOR SUB‑SITE CANDIDATES
A Sub‑Site candidate is valid only if:

1. It is explicitly documented as an internal identity‑bearing unit.  
2. It has a stable name or designation.  
3. It is not a full Site.  
4. It is not a Trail, Trail Segment, Trail Network, or Site Network.  
5. It is not an Access Point.  
6. It is not an amenity or feature (e.g., playground, shelter, overlook).  
7. It is not a temporary or unnamed management zone.  
8. It has exactly one parent Site.  

If any of these conditions fail, the candidate must not be created.

------------------------------------------------------------
# 5. DISCOVERY WORKFLOW

## 5.1 Step 1 — Identify Internal Identity‑Bearing Units
Search all required sources for:
- Named natural areas within a larger Site
- Named preserves within a larger park
- Named historic areas within a larger district
- Named ecological units
- Named cultural landscape units
- Named recreation areas within a larger Site
- Named campuses or complexes within a larger Site

Record each appearance as a raw candidate.

## 5.2 Step 2 — Verify Identity‑Bearing Name
A Sub‑Site must have:
- A documented, stable name
- Not a temporary project name
- Not a marketing slogan
- Not a generic label (e.g., “North Area”) unless officially used

If ambiguous, flag for review.

## 5.3 Step 3 — Confirm Parent Site
Each Sub‑Site must:
- Have exactly one parent Site
- Be documented as part of that Site
- Not be inferred from context alone

If the parent Site is not yet discovered, create a placeholder Site candidate.

## 5.4 Step 4 — Extract Required Metadata
For each candidate, extract:
- Sub‑Site name
- Alternate names
- Sub‑Site type
- Description
- County (if documented)
- GPS coordinates (if documented)
- URL
- Map link
- Notes
- Source tier
- Source dataset
- Discovery confidence

## 5.5 Step 5 — Extract Geometry (If Available)
If GIS data is present:
- Extract Sub‑Site polygon or centroid
- Do not simplify or infer geometry
- Preserve coordinate precision

## 5.6 Step 6 — Log Internal Features (Non‑Authoritative)
Record any features associated with the Sub‑Site.
These become authoritative during Site normalization.

## 5.7 Step 7 — Emit Raw Candidate Record
Produce a Raw Candidate Sub‑Site Record following the Sub‑Site Schema Module v1.

------------------------------------------------------------
# 6. TIER‑SPECIFIC EXPECTATIONS

## 6.1 Federal Tier
May surface:
- Internal units within national wildlife refuges
- Internal units within national parks
- Historic districts within federal Sites

## 6.2 State Tier
Must surface:
- Named units within state parks
- Named units within state forests
- Named units within state wildlife areas

## 6.3 Park District Tier
Must surface:
- Named preserves within larger parks
- Named natural areas within district Sites
- Named recreation areas within larger Sites

## 6.4 County Tier
May surface:
- Named internal units within county parks

## 6.5 Township & Municipal Tiers
May surface:
- Named internal units within municipal parks
- Named historic areas within municipal Sites

## 6.6 Land Trust & Conservancy Tier
Must surface:
- Named preserves within larger conservation areas
- Named ecological units

## 6.7 Private & Organization‑Based Tier
May surface:
- Named internal units within campuses or complexes
- Named internal units within privately managed natural areas

------------------------------------------------------------
# 7. CONSOLIDATION RULES
During consolidation:
- Merge identical Sub‑Sites only if they share the same parent Site.
- Preserve all conflicting metadata.
- Do not merge Sub‑Sites with different documented names.
- Align Sub‑Sites with their parent Site during normalization.
- Maintain all source references.

------------------------------------------------------------
# 8. OUTPUT REQUIREMENTS
Each Sub‑Site candidate must output:

- All fields required by the Sub‑Site Schema Module v1
- Discovery Metadata
- Source references
- Non‑authoritative feature references
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
- Sub‑Site Schema Module v1
- Sub‑Site Vocabulary Module v1
- Site Discovery Sub‑Procedure v3.1
- Trail Discovery Sub‑Procedure v1
- Access Point Discovery Sub‑Procedure v3.1
- Normalization and Resolution Modules
- TSV Output Specifications
- Audit & Logging Module v1.1

------------------------------------------------------------
# END OF SUB‑SITE DISCOVERY SUB‑PROCEDURE v1