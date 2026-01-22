# NATURAL AREAS PROJECT — TRAIL DISCOVERY SUB‑PROCEDURE v3.2.2
Authoritative, versioned sub‑procedure for discovering **Trails** in the statewide
Natural Areas & Trails system.

This module defines:
- The Trail discovery workflow  
- Required sources  
- Identity rules for Trail candidates  
- Tier‑specific expectations  
- Output requirements  
- Integration points  

This module contains no controlled vocabularies.  
All vocabularies are defined in the **Trail Vocabulary Module v3.2.2**.

------------------------------------------------------------
# 1. PURPOSE

The Trail Discovery Sub‑Procedure v3.2.2 provides the authoritative, deterministic
workflow for discovering **Trails** across all eight discovery tiers.

A Trail is:
- A **named, identity‑bearing linear corridor**  
- Documented in authoritative sources  
- Distinct from its Trail Segments  
- Distinct from Trail Networks  
- Distinct from Sites and child Sites  
- Not an Access Point or amenity  

This sub‑procedure ensures:
- Consistent identification of Trails  
- Prevention of misclassification as Sites, Trail Segments, or Trail Networks  
- Proper metadata capture  
- Clean integration with Trail Segment, Trail Network, and Access Point discovery  

This module is authoritative for Trail discovery.

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

Each tier must surface Trail candidates when applicable.

------------------------------------------------------------
# 3. REQUIRED SOURCES

Each tier must check the following for Trail references:

- Official agency websites  
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

All sources must be logged in **Discovery Metadata v3.2.2**.

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

## 5.1 Step 1 — Identify Named Trails
Search all required sources for:
- Named trails  
- Named loops  
- Named linear corridors  
- Named bikeways or greenways  
- Named water trails  
- Named equestrian trails  
- Named multi‑use trails  

Record each appearance as a **Raw Candidate Record**.

## 5.2 Step 2 — Verify Identity‑Bearing Name
A Trail must have:
- A documented, stable name  
- Not a temporary project name  
- Not a marketing slogan  
- Not a generic label unless officially used  

If ambiguous, flag for review in metadata.

## 5.3 Step 3 — Confirm Trail‑Level Identity
The candidate must:
- Represent a full linear corridor  
- Not be a single segment  
- Not be a cluster of segments  
- Not be a Trail Network  

If unclear, flag for review.

## 5.4 Step 4 — Extract Raw Metadata
Extract only **raw, unnormalized** values:
- name_raw  
- alternate_names_raw  
- trail_type_raw  
- length_raw (if documented)  
- counties_raw  
- managing_agency_raw  
- status_raw  
- description_raw  
- url_primary_raw  
- url_all_raw  
- source_datasets  
- source_maps  
- source_gis_layers  
- notes_raw  

No normalization is permitted.

## 5.5 Step 5 — Log Trail Segments (Non‑Authoritative)
Record any documented segments as **raw references only**.  
Segment creation occurs in the **Trail Segment Discovery Sub‑Procedure v3.2.2**.

## 5.6 Step 6 — Log Trail Network Membership (Non‑Authoritative)
Record any Trail Networks the Trail is part of.  
Membership becomes authoritative during normalization.

## 5.7 Step 7 — Log Access Point References (Non‑Authoritative)
If sources show Access Points attached to the Trail:
- Record them as **raw references only**  
- Do not create Access Points here  
- Access Point creation occurs in the **Access Point Discovery Sub‑Procedure v3.2.2**  

## 5.8 Step 8 — Emit Raw Candidate Record
Produce a Raw Candidate Trail Record conforming to the  
**Discovery Output Specification v3.2.2**.

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

## 6.3 Park District Tier
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

## 6.6 Land Trust & Conservancy Tier
May surface:
- Named trails within preserves  
- Named loops  
- Named access corridors  

## 6.7 Private & Organization‑Based Tier
May surface:
- Privately managed named trails  
- Campus‑scale trail systems (individual trails)  

------------------------------------------------------------
# 7. CONSOLIDATION RULES

During consolidation:
- Merge identical Trail names across tiers.  
- Preserve all conflicting metadata.  
- Do not merge Trails with different documented names.  
- Align Trail Segments with their parent Trails.  
- Align Trails with Trail Networks when documented.  
- Maintain all source references.  
- Apply **Resolution Module v3.2.2** for ambiguous cases.  

------------------------------------------------------------
# 8. OUTPUT REQUIREMENTS

Each Trail candidate must output:

- A **Raw Candidate Record** (unnormalized)  
- Raw values only  
- Complete **Discovery Metadata v3.2.2**  
- Raw segment references  
- Raw network membership references  
- Raw Access Point references (if documented)  
- No normalized fields  
- No Derived Label  
- No TSV rows (unless developer preview is explicitly requested)  

Output must conform to:
- **Discovery Metadata Specification v3.2.2**  
- **Discovery Output Specification v3.2.2**  
- **Resolution Module v3.2.2**  

------------------------------------------------------------
# 9. INTEGRATION POINTS

This module integrates with:
- **Discovery Protocol Module v3.2.2**  
- **Trail Schema Module v3.2.2**  
- **Trail Vocabulary Module v3.2.2**  
- **Trail Segment Discovery Sub‑Procedure v3.2.2**  
- **Trail Network Discovery Sub‑Procedure v3.2.2**  
- **Access Point Discovery Sub‑Procedure v3.2.2**  
- **Site Network Discovery Sub‑Procedure v3.2.2**  
- **Resolution Module v3.2.2**  
- **Normalization Contracts v3.2.2**  
- **TSV Output Specifications v3.2.2**  
- **Audit & Logging Module v3.2.2**  

------------------------------------------------------------
# END OF TRAIL DISCOVERY SUB‑PROCEDURE v3.2.2