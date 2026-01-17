# NATURAL AREAS PROJECT — TRAIL SEGMENT DISCOVERY SUB‑PROCEDURE v1
Authoritative, versioned sub‑procedure for discovering Trail Segments in the statewide
Natural Areas & Trails system.

This module defines:
- The Trail Segment discovery workflow
- Required sources
- Identity rules for Trail Segment candidates
- Tier‑specific discovery expectations
- Output requirements
- Integration points

This module contains no controlled vocabularies.
All vocabularies are defined in the Trail Segment Vocabulary Module v1.

------------------------------------------------------------
# 1. PURPOSE
The Trail Segment Discovery Sub‑Procedure v1 provides the authoritative, deterministic
workflow for discovering Trail Segments across all eight discovery tiers.

A Trail Segment is:
- An operational portion of a Trail
- Documented in authoritative sources
- Distinct from the Trail itself
- Distinct from Access Points
- Distinct from Trail Networks

This sub‑procedure ensures:
- Consistent identification of Trail Segments
- Prevention of misclassification as Trails or Access Points
- Proper metadata capture
- Clean integration with Trail and Trail Network discovery

This module is authoritative for Trail Segment discovery.

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
- Trail signage programs (digitally documented)
- Multi‑trail system documents (for segment extraction)

All sources must be logged in Discovery Metadata.

------------------------------------------------------------
# 4. IDENTITY RULES FOR TRAIL SEGMENT CANDIDATES
A Trail Segment candidate is valid only if:

1. It is explicitly documented as a portion of a Trail.  
2. It has a stable identity within the parent Trail.  
3. It is not itself a Trail.  
4. It is not a Trail Network.  
5. It is not an Access Point.  
6. It is not a temporary or unnamed connector.  
7. It is not a Site or Sub‑Site.  

If any of these conditions fail, the candidate must not be created.

------------------------------------------------------------
# 5. DISCOVERY WORKFLOW

## 5.1 Step 1 — Identify Segment‑Level Documentation
Search all required sources for:
- Named segments
- Numbered segments
- GIS‑defined segments
- Operational segments (e.g., “North Section,” “Riverside Segment”)
- Segments with distinct surface types or statuses
- Segments with distinct management

Record each appearance as a raw candidate.

## 5.2 Step 2 — Verify Segment Identity
A Trail Segment must:
- Be part of a specific parent Trail
- Have a documented boundary or identity
- Not be a full Trail
- Not be a Trail Network

If ambiguous, flag for review.

## 5.3 Step 3 — Confirm Parent Trail
Each segment must have:
- Exactly one parent Trail
- A documented relationship to that Trail
- No inferred parentage

If the parent Trail is not yet discovered, create a placeholder Trail candidate.

## 5.4 Step 4 — Extract Required Metadata
For each candidate, extract:
- Segment name (or segment identifier)
- Parent Trail name
- Segment length (if documented)
- Surface type
- Status
- Counties traversed
- Managing agency (primary)
- Managing agencies (secondary)
- Description
- URL
- Map link
- Notes
- Source tier
- Source dataset
- Discovery confidence

## 5.5 Step 5 — Extract Geometry (If Available)
If GIS data is present:
- Extract segment geometry
- Do not simplify or infer geometry
- Preserve coordinate precision

## 5.6 Step 6 — Log Access Points (Non‑Authoritative)
Record any Access Points associated with the segment.
These become authoritative during Access Point discovery.

## 5.7 Step 7 — Emit Raw Candidate Record
Produce a Raw Candidate Trail Segment Record following the Trail Segment Schema Module v1.

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

## 6.3 Park District Tier
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

## 6.6 Land Trust & Conservancy Tier
May surface:
- Segment‑level breakdowns within preserves

## 6.7 Private & Organization‑Based Tier
May surface:
- Privately managed segment‑level trails
- Campus‑scale segment delineations

------------------------------------------------------------
# 7. CONSOLIDATION RULES
During consolidation:
- Merge identical segments only if they share the same parent Trail.
- Preserve all conflicting metadata.
- Do not merge segments with different documented names or identifiers.
- Align segments with their parent Trail during normalization.
- Maintain all source references.

------------------------------------------------------------
# 8. OUTPUT REQUIREMENTS
Each Trail Segment candidate must output:

- All fields required by the Trail Segment Schema Module v1
- Discovery Metadata
- Source references
- Non‑authoritative Access Point references
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
- Trail Segment Schema Module v1
- Trail Segment Vocabulary Module v1
- Trail Discovery Sub‑Procedure v1
- Trail Network Discovery Sub‑Procedure v1
- Access Point Discovery Sub‑Procedure v3.1
- Normalization and Resolution Modules
- TSV Output Specifications
- Audit & Logging Module v1.1

------------------------------------------------------------
# END OF TRAIL SEGMENT DISCOVERY SUB‑PROCEDURE v1