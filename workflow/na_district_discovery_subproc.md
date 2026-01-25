# NATURAL AREAS PROJECT
# DISTRICT‑LEVEL PUBLIC LANDHOLDERS DISCOVERY SUB‑PROCEDURE v4.0
(Tier 3 — Park Districts, Metro Parks, Joint Recreation Districts, Conservancy Districts, Watershed Districts, Special Districts)

This module defines the authoritative, deterministic Tier‑3 discovery rules for
district‑level public landholders within the v4.0 Raw → Resolution → Normalization →
Entity Graph pipeline.

This document supersedes all v3.x district‑tier discovery logic.

This module contains no controlled vocabularies.  
All vocabularies are defined in the appropriate v4.0 Vocabulary Modules.

------------------------------------------------------------
# 1. PURPOSE

The District‑Level Public Landholders Discovery Sub‑Procedure v4.0 defines how Tier 3 must:

- Identify all district‑managed Sites  
- Identify child Sites within district Sites  
- Identify Trails, Trail Segments, and Trail Networks managed by districts  
- Identify Site Networks managed by districts  
- Identify Access Points associated with district Sites and Trails  
- Distinguish district management from municipal, township, county, state, or federal co‑management  
- Identify conservancy district lands, watershed district lands, and flood‑control lands  
- Avoid false positives from similarly named places  
- Log uncertainty and boundary cases  
- Produce Raw Discovery Records v4.0  
- Produce Discovery Metadata v4.0  

This module is referenced only by:

- Discovery Protocol Module v4.0  
- Discovery Orchestration Module v4.0  
- Tier Sub‑Procedure Template v4.0  

------------------------------------------------------------
# 2. SCOPE

This sub‑procedure applies to all district‑level public landholders in Ohio.

## 2.1 Park & Recreation Districts
- County park districts  
- Metro parks systems  
- Joint recreation districts  

## 2.2 Conservancy & Watershed Districts
- Muskingum Watershed Conservancy District (MWCD)  
- Miami Conservancy District  
- Joint conservancy districts  
- Watershed districts  
- Flood‑control districts  

## 2.3 Special Districts
- Districts with statutory authority to own/manage natural areas  
- Districts managing lakes, reservoirs, or floodplain corridors  
- Districts with recreation or conservation mandates  

This tier governs discovery of:

- Sites  
- Child Sites  
- Trails  
- Trail Segments  
- Trail Networks  
- Site Networks  
- Access Points  

Tier 3 sits **below State** and **above County**.

------------------------------------------------------------
# 3. AUTHORITATIVE SOURCES (MANDATORY)

Tier 3 must enumerate and recursively explore the following authoritative sources.

## 3.1 Official District Websites
Required sources:
- Park or property lists → Sites  
- Facility lists → child Sites  
- Trail pages → Trails  
- Trail maps → Trails, Trail Segments  
- Access point listings → Access Points  
- District‑managed programs or networks → Site Networks, Trail Networks  

## 3.2 District GIS
Required sources:
- District boundaries → Sites  
- Internal units → child Sites  
- Trail geometry → Trails, Trail Segments  
- Access point layers → Access Points  

## 3.3 District Brochures & Maps
Required sources:
- Named parks → Sites  
- Named internal areas → child Sites  
- Named trails → Trails  
- Trailheads, parking, boat access → Access Points  

## 3.4 County Auditor / County GIS
Required sources:
- Parcels owned by the district → Sites  
- Parcels leased or co‑managed → Sites or child Sites  

## 3.5 Partner Agencies
Required sources:
- Co‑managed parks  
- Joint recreation districts  
- Shared trail systems  
- USACE partnerships (e.g., MWCD lakes)  

All sources must be logged in **Discovery Metadata v4.0**.

------------------------------------------------------------
# 4. DOMAIN RULES FOR DISTRICT‑LEVEL DISCOVERY

## 4.1 Multi‑County Districts
Districts may span multiple counties.

Rules:
- **Do NOT segment multi‑county Sites**  
- Record all counties in `counties_raw`  

## 4.2 Conservancy Districts
Examples: MWCD, Miami Conservancy District

Check for:
- Lakes and reservoirs → Sites  
- Recreation areas → Sites or child Sites  
- Shoreline access → Access Points  
- Flood‑control lands → Sites  
- Multi‑site lake systems → Site Networks  
- Multi‑trail lake corridors → Trail Networks  

## 4.3 Watershed & Flood‑Control Districts
Check for:
- Floodplain corridors → Sites  
- River access → Access Points  
- Multi‑county river systems → Site Networks  
- District‑managed trails → Trails  

## 4.4 Co‑Management
Districts may co‑manage Sites with:
- Municipalities  
- Townships  
- Counties  
- ODNR  
- USACE  

Record all co‑management in metadata.

------------------------------------------------------------
# 5. ENUMERATIVE + RECURSIVE DISCOVERY RULES

Tier 3 must use both enumerative and recursive discovery.

## 5.1 Enumerative Discovery (Listing Pages)
Tier 3 must enumerate:
- All district property listings  
- All district trail listings  
- All district facility listings  
- All district‑managed program listings  
- All district GIS datasets  

## 5.2 Recursive Discovery (URL Propagation)
Tier 3 must recursively follow:
- Internal links within district domains  
- Internal links within partner agency domains (if relevant)  

Recursion must stop when:
- The domain is not on the allowlist  
- The page is not relevant to Sites, Trails, or Access Points  
- The page is administrative or non‑recreational  

## 5.3 Recursion Allowlist
- *.metroparks.*  
- *.parkdistrict.*  
- *.parks.*  
- *.conservancy.*  
- *.watershed.*  
- *.mwcd.*  
- *.usace.army.mil (for partnerships only)*  

------------------------------------------------------------
# 6. ENTITY CREATION RULES (TIER‑SPECIFIC)

### 6.1 Site Creation
Create a **Site** when:
- District‑owned or district‑managed  
- Identity‑bearing (named, mapped, or designated)  
- Public access or recreation infrastructure exists  
- It influences Access Point logic  

Exclude:
- Administrative offices  
- Maintenance yards  
- Non‑public parcels with no identity  

### 6.2 Child Site Creation
Create a **child Site** when:
- A named internal unit exists within a district Site  
- It meets the **Child Site Rules Module v4.0**  

### 6.3 Trail Creation
Create a **Trail** when:
- A named trail appears in district datasets or maps  

### 6.4 Trail Segment Creation
Create a **Trail Segment** when:
- Segment‑level geometry or identifiers exist  

### 6.5 Trail Network Creation
Create a **Trail Network** when:
- A district‑managed multi‑trail system exists  
- A multi‑lake or multi‑river corridor trail system exists  

### 6.6 Site Network Creation
Create a **Site Network** when:
- A district‑managed multi‑site system exists  
- A multi‑lake or multi‑river system is documented  

### 6.7 Access Point Creation
Create an **Access Point** when:
- A visitor‑facing entry location is documented  

------------------------------------------------------------
# 7. TIER‑SPECIFIC EXPECTATIONS

Tier 3 **must** surface:
- All district‑managed Sites  
- All identity‑bearing child Sites  
- All district‑managed Trails  
- All district‑managed Trail Segments  
- All district‑managed Access Points  
- All conservancy district Sites (e.g., MWCD lakes, recreation areas)  
- All watershed/flood‑control district Sites  

Tier 3 **may** surface:
- District‑managed Trail Networks  
- District‑managed Site Networks  
- District‑managed easements  
- Flood‑control corridors  
- Multi‑lake or multi‑river systems  

------------------------------------------------------------
# 8. METADATA REQUIREMENTS

Each discovered entity must include:

- Full **Discovery Metadata v4.0**  
- All raw source references  
- All counties (raw)  
- All conflicts and uncertainties  
- All parent relationships (for child Sites and Access Points)  
- All geometry (if available)  

All values must be raw and unnormalized.

------------------------------------------------------------
# 9. OUTPUT REQUIREMENTS

Each district‑level entity must output a **Raw Discovery Record** conforming to:

- **Discovery Output Specification v4.0**  
- **Discovery Metadata Specification v4.0**  
- The appropriate Schema Module v4.0  
- The appropriate Vocabulary Module v4.0  

No normalized fields may appear in Tier 3 output.

------------------------------------------------------------
# 10. INTEGRATION POINTS

This module integrates with:

- Discovery Protocol Module v4.0  
- Discovery Orchestration Module v4.0  
- Tier Sub‑Procedure Template v4.0  
- All Entity Discovery Sub‑Procedures v4.0  
- Child Site Rules Module v4.0  
- Discovery Metadata Specification v4.0  
- Discovery Output Specification v4.0  
- Resolution Engine v4.0  
- Normalization Engine v4.0  
- TSV Output Specifications v4.0  
- Audit & Logging Module v4.0  
- County Baseline Module v4.0  

------------------------------------------------------------
# 11. VERSIONING

- This module is **District‑Level Public Landholders Discovery Sub‑Procedure v4.0**.  
- Updates to district governance or datasets may result in v4.1, v4.2, etc.  
- Any change to tier order or workflow must be made in the Discovery Protocol Module v4.0.

------------------------------------------------------------
# END OF DISTRICT‑LEVEL PUBLIC LANDHOLDERS DISCOVERY SUB‑PROCEDURE v4.0