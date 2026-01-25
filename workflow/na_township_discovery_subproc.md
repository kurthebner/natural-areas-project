# NATURAL AREAS PROJECT  
# TOWNSHIP LANDS DISCOVERY SUB‑PROCEDURE v4.0  
(Ohio Townships, Township Websites, County‑Hosted Township Pages, Township Recreation Assets)

Tier 5 of the **Discovery Protocol Module v4.0**.

Townships in Ohio vary dramatically in capacity, documentation quality, and web presence.  
Some maintain full recreation pages; others have no website at all. Township parks may be
hidden on non‑indexed subpages, embedded PDFs, or county‑hosted pages.

This module defines the authoritative, deterministic Tier‑5 discovery rules for township‑owned
and township‑managed natural areas within the v4.0 Raw → Resolution → Normalization → Entity Graph pipeline.

This module contains no controlled vocabularies.  
All vocabularies are defined in the appropriate v4.0 Vocabulary Modules.

------------------------------------------------------------
# 1. PURPOSE

The Township Lands Discovery Sub‑Procedure v4.0 defines how Tier 5 must:

- Identify township‑owned or township‑managed **Sites**  
- Identify township‑managed **child Sites**  
- Identify township‑managed **Trails** and **Trail Segments**  
- Identify township‑managed **Trail Networks** (rare)  
- Identify township‑managed **Site Networks** (rare)  
- Identify township‑managed **Access Points**  
- Identify township recreation assets even when no recreation department exists  
- Identify township pages hosted by the county  
- Surface uncertainty and conflicts  
- Produce Raw Discovery Records v4.0  
- Produce Discovery Metadata v4.0  

This module is referenced only by:

- Discovery Protocol Module v4.0  
- Discovery Orchestration Module v4.0  
- Tier Sub‑Procedure Template v4.0  

------------------------------------------------------------
# 2. SCOPE

This sub‑procedure applies to:

- Township government websites  
- Township recreation pages (if any)  
- Township‑hosted or county‑hosted subpages  
- Township planning documents (rare)  
- Township GIS layers (rare)  
- Township meeting minutes (for land acquisitions)  
- Official township social media (conditional)  

It governs discovery of:

- Sites  
- Child Sites  
- Trails  
- Trail Segments  
- Trail Networks  
- Site Networks  
- Access Points  

Tier 5 sits **below County** and **above Municipal**.

------------------------------------------------------------
# 3. AUTHORITATIVE SOURCES (MANDATORY)

Tier 5 must enumerate and recursively explore the following authoritative sources.

## 3.1 Township Website (If Exists)
Scan for:
- Parks  
- Recreation  
- Facilities  
- Community  
- Open Space / Green Space  
- Playgrounds  
- Shelters  
- Picnic Areas  

Township websites often contain:
- Hidden subpages  
- Non‑indexed pages  
- PDF‑only listings  
- Outdated or partial information  

All must be scanned.

## 3.2 County‑Hosted Township Pages
If the county hosts township pages:
- Treat them as authoritative  
- Scan for parks, preserves, trails, facilities  
- Log the county as the source  

Discoveries remain **Tier 5** because the township is the governing entity.

## 3.3 Township Meeting Minutes
Scan for:
- Land purchases  
- Park dedications  
- Trail agreements  
- Conservation partnerships  
- Recreation facility improvements  

## 3.4 Township GIS (If Exists)
Check for:
- Township‑owned parcels  
- Recreation layers  

## 3.5 Township Social Media (Conditional)
Township social media is authoritative only if:
- Explicitly designated as official by the township, OR  
- Linked from the township website, OR  
- Linked from the county website  

If official:
- Scan for park announcements  
- Facility openings  
- Trail access information  

If not official → exclude.

All sources must be logged in **Discovery Metadata v4.0**.

------------------------------------------------------------
# 4. DOMAIN RULES FOR TOWNSHIP DISCOVERY

## 4.1 Township‑Owned vs Township‑Managed
A Site may be:
- Owned by the township  
- Managed by the township  
- Co‑managed with counties or park districts  

All must be surfaced if identity‑bearing.

## 4.2 Hidden or Non‑Indexed Pages
Township parks may appear on:
- Unlinked HTML pages  
- PDF brochures  
- Archived pages  

These must be included if authoritative.

## 4.3 Township Recreation Assets Without a Recreation Department
Even if no recreation department exists:
- Parks  
- Trails  
- Facilities  
- Natural areas  

must still be surfaced if identity‑bearing.

## 4.4 County‑Hosted Township Pages
These are authoritative for township discovery but remain **Tier 5**.

------------------------------------------------------------
# 5. ENUMERATIVE + RECURSIVE DISCOVERY RULES

Tier 5 must use both enumerative and recursive discovery.

## 5.1 Enumerative Discovery (Listing Pages)
Tier 5 must enumerate:
- All township park listings  
- All township recreation pages  
- All township facility listings  
- All township PDFs  
- All county‑hosted township pages  

## 5.2 Recursive Discovery (URL Propagation)
Tier 5 must recursively follow:
- Internal links within township domains  
- Internal links within county‑hosted township pages  
- Internal links within township‑linked social media (if official)  

Recursion must stop when:
- The domain is not on the allowlist  
- The page is not relevant to Sites, Trails, or Access Points  
- The page is administrative or non‑recreational  

## 5.3 Recursion Allowlist
- *.township.*  
- *.townshipoh.gov  
- *.oh.gov (township subdomains)  
- *.countyoh.gov (county‑hosted township pages)  
- *.co.*.us (legacy township domains)  
- *.facebook.com/* (only if official)  

------------------------------------------------------------
# 6. ENTITY CREATION RULES (TIER‑SPECIFIC)

### 6.1 Site Creation
Create a **Site** when:
- Township‑owned or township‑managed  
- Identity‑bearing (named, mapped, or designated)  
- Public access or recreation infrastructure exists  
- It influences Access Point logic  

Exclude:
- Township halls  
- Administrative buildings  
- Cemeteries (unless designated natural areas)  
- Maintenance yards  

### 6.2 Child Site Creation
Create a **child Site** when:
- A named internal unit exists within a township Site  
- A recreation area, facility, or natural area is identity‑bearing  
- A playground, shelter area, or lake area is formally named  

Do not surface:
- Amenities without identity  
- Temporary zones  
- Unnamed management areas  

### 6.3 Trail Creation
Surface a **Trail** when:
- A named trail appears on township or county‑hosted pages  
- A named trail appears in meeting minutes  
- A named trail appears in township GIS (rare)  

### 6.4 Trail Segment Creation
Surface **Trail Segments** when:
- Segment‑level geometry exists in township or county GIS  
- Segment identifiers appear in maps or plans  

### 6.5 Trail Network Creation
Surface a **Trail Network** when:
- A township‑managed multi‑trail system exists  
- A greenway corridor spans multiple Trails  

Rare but must be captured.

### 6.6 Site Network Creation
Surface a **Site Network** when:
- A township‑managed multi‑site system exists  
- A conservation or greenway network is formally documented  

Very rare but must be captured.

### 6.7 Access Point Creation
Surface an **Access Point** when:
- It appears on township pages  
- It appears on county‑hosted township pages  
- It appears in township meeting minutes  
- It appears in township GIS (rare)  

Access Points must include raw values only:
- Name or descriptive label  
- Access Point Type (raw)  
- Township  
- County list (raw)  
- Parent entity (Site, child Site, Trail, Trail Segment)  
- Source(s)  
- Notes  

------------------------------------------------------------
# 7. TIER‑SPECIFIC EXPECTATIONS

Tier 5 **must** surface:
- All township‑owned or township‑managed Sites  
- All identity‑bearing child Sites  
- All township‑managed Trails  
- All township‑managed Trail Segments  
- All township‑managed Access Points  
- All parks, preserves, and trails listed on county‑hosted township pages  

Tier 5 **may** surface:
- Township‑managed Trail Networks  
- Township‑managed Site Networks  
- Township‑managed easements  
- Planned parks and trail corridors (if identity‑bearing)  

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

Each township entity must output a **Raw Discovery Record** conforming to:

- **Discovery Output Specification v4.0**  
- **Discovery Metadata Specification v4.0**  
- The appropriate Schema Module v4.0  
- The appropriate Vocabulary Module v4.0  

No normalized fields may appear in Tier 5 output.

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

- This module is **Township Lands Discovery Sub‑Procedure v4.0**.  
- Updates to township governance practices or statewide township directories may result in v4.1, v4.2, etc.  
- Any change to tier order or workflow must be made in the Discovery Protocol Module v4.0.

------------------------------------------------------------
# END OF TOWNSHIP LANDS DISCOVERY SUB‑PROCEDURE v4.0