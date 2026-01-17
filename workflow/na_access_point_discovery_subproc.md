# NATURAL AREAS PROJECT — ACCESS POINT DISCOVERY SUB‑PROCEDURE v3.1
Authoritative, versioned sub‑procedure for discovering Access Points in the statewide
Natural Areas & Trails system.

This module defines:
- The Access Point discovery workflow
- Required sources
- Identity rules for Access Point candidates
- Tier‑specific discovery expectations
- Output requirements
- Integration points

This module contains no controlled vocabularies.
All vocabularies are defined in the Access Point Vocabulary Module v5.

------------------------------------------------------------
# 1. PURPOSE
The Access Point Discovery Sub‑Procedure v3.1 provides the authoritative, deterministic
workflow for discovering Access Points across all eight discovery tiers.

An Access Point is:
- A visitor‑facing navigational entry location
- Documented in authoritative sources
- Attached to an identity‑bearing parent entity (Site, Sub‑Site, Trail, Trail Segment)
- Classified using the Access Point Vocabulary Module v5

This sub‑procedure ensures:
- Consistent identification of Access Points
- Prevention of misclassification as Sites, Trails, or Features
- Proper metadata capture
- Clean integration with Site, Trail, and Trail Segment discovery

This module is authoritative for Access Point discovery.

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

Each tier must surface Access Point candidates when applicable.

------------------------------------------------------------
# 3. REQUIRED SOURCES
Each tier must check the following for Access Point references:

- Official agency maps
- GIS layers showing trailheads, parking, boat ramps, etc.
- Park district trail maps
- State and federal recreation maps
- Brochures and downloadable PDFs
- Trailhead kiosks (digitally documented)
- Planning documents (master plans, corridor plans)
- Stewardship or restoration plans
- Land trust preserve maps
- Municipal park maps
- County recreation maps
- Signage programs (digitally documented)

All sources must be logged in Discovery Metadata.

------------------------------------------------------------
# 4. IDENTITY RULES FOR ACCESS POINT CANDIDATES
An Access Point candidate is valid only if:

1. It is explicitly documented as a visitor‑facing entry location.  
2. It has a documented or inferable geographic point.  
3. It is not a Site, Sub‑Site, Trail, or Trail Segment.  
4. It is not a feature or amenity (e.g., shelter, overlook, playground).  
5. It is not a parking lot unless it functions as an entry point.  
6. It is not a road intersection unless documented as an entry point.  
7. It is not a temporary or unnamed connector.  
8. It attaches to exactly one identity‑bearing parent entity.  

If any of these conditions fail, the candidate must not be created.

------------------------------------------------------------
# 5. DISCOVERY WORKFLOW

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

Record each appearance as a raw candidate.

## 5.2 Step 2 — Verify Access Point Identity
An Access Point must:
- Be a visitor‑facing entry location
- Have a documented or inferable coordinate
- Not be an amenity or feature
- Not be a Site, Sub‑Site, Trail, or Trail Segment

If ambiguous, flag for review.

## 5.3 Step 3 — Assign Access Point Type
Assign a Type from the Access Point Vocabulary Module v5.
If unclear, leave blank and flag for review.

## 5.4 Step 4 — Confirm Parent Entity
Each Access Point must attach to exactly one parent:
- Site  
- Sub‑Site  
- Trail  
- Trail Segment  

Rules:
- Do not infer parentage unless the map explicitly shows the relationship.
- If the parent entity is not yet discovered, create a placeholder candidate.

## 5.5 Step 5 — Extract Required Metadata
For each candidate, extract:
- Access Point Name (if present)
- Access Point Type
- Parent Entity Name
- Parent Entity Type
- County
- GPS Coordinates
- Plus Code
- Description
- Status
- URL
- Notes
- Source tier
- Source dataset
- Discovery confidence

## 5.6 Step 6 — Extract Geometry (If Available)
If GIS data is present:
- Extract point geometry
- Do not infer or adjust coordinates
- Preserve coordinate precision

## 5.7 Step 7 — Emit Raw Candidate Record
Produce a Raw Candidate Access Point Record following the Access Point Schema Module v1.1.

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

## 6.3 Park District Tier
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

## 6.6 Land Trust & Conservancy Tier
Must surface:
- Preserve access points
- Trailheads within conservation areas

## 6.7 Private & Organization‑Based Tier
May surface:
- Privately managed access points
- Campus‑scale access nodes

------------------------------------------------------------
# 7. CONSOLIDATION RULES
During consolidation:
- Merge identical Access Points across tiers.
- Preserve all conflicting metadata.
- Do not merge Access Points with different coordinates.
- Align Access Points with their parent entities.
- Maintain all source references.

------------------------------------------------------------
# 8. OUTPUT REQUIREMENTS
Each Access Point candidate must output:

- All fields required by the Access Point Schema Module v1.1
- Discovery Metadata
- Source references
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
- Access Point Schema Module v1.1
- Access Point Vocabulary Module v5
- Site Discovery Sub‑Procedure v3.1
- Sub‑Site Discovery Sub‑Procedure v1
- Trail Discovery Sub‑Procedure v1
- Trail Segment Discovery Sub‑Procedure v1
- Normalization and Resolution Modules
- TSV Output Specifications
- Audit & Logging Module v1.1

------------------------------------------------------------
# END OF ACCESS POINT DISCOVERY SUB‑PROCEDURE v3.1