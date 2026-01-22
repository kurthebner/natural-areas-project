# NATURAL AREAS PROJECT — PRIVATE & ORGANIZATION‑BASED DISCOVERY SUB‑PROCEDURE v3.2.2  
(Private Nature Preserves, Camps, Retreat Centers, Scout Camps, Church Camps, Fraternal Lands, HOA Open Space, Corporate Lands)

Tier 8 of the **Discovery Protocol Module v3.2.2**.

Private and organization‑based lands are highly variable, inconsistently documented,  
and often partially accessible. Some are fully public; some are seasonally public;  
some are identity‑bearing but private; some have no public role. Tier 8 provides  
the final sweep to ensure statewide completeness.

This module defines the **authoritative, deterministic workflow** for Tier 8  
discovery across all six ontology entity types.

------------------------------------------------------------
# 1. PURPOSE

This sub‑procedure defines how the system must:

- Identify private or organization‑based **Sites**  
- Identify **child Sites** within private holdings  
- Identify private **Trails** and **Trail Segments**  
- Identify private **Trail Networks** (rare)  
- Identify private **Site Networks** (rare)  
- Identify private **Access Points** when public or limited access exists  
- Distinguish public, limited, and private access  
- Identify identity‑bearing private natural areas  
- Identify private preserves owned by nonprofits or foundations  
- Log uncertainty and boundary cases  
- Produce Raw Candidate Records and Discovery Metadata v3.2.2  

This module is referenced only by the Discovery Protocol Module v3.2.2.

------------------------------------------------------------
# 2. SCOPE

This sub‑procedure applies to:

- Private nature preserves  
- Private campgrounds  
- Church camps  
- Scout camps  
- Fraternal organization lands  
- HOA open space  
- Corporate campuses with natural areas  
- Private hunting/fishing clubs  
- Private retreat centers  
- Private trail systems  
- Private foundations with land holdings  

It governs discovery of:

- **Sites**  
- **Child Sites**  
- **Trails**  
- **Trail Segments**  
- **Trail Networks**  
- **Site Networks**  
- **Access Points**  

This tier sits **below Land Trusts & Conservancies** and is the final discovery tier.

------------------------------------------------------------
# 3. REQUIRED SOURCES (ALL MANDATORY)

## 3.1 Official Websites
Scan for:
- Nature Preserve  
- Camp  
- Retreat Center  
- Outdoor Center  
- Hiking Trails  
- Natural Area  
- Open Space  
- Wildlife Area  

Scan all:
- Facility pages  
- Program pages  
- Maps  
- PDF brochures  

## 3.2 County Auditor / GIS (Parcel Verification)
Private holdings often appear as:
- Private preserves  
- Private campgrounds  
- Private recreation areas  
- HOA open space  
- Corporate natural areas  

GIS is required for:
- County boundary confirmation  
- Ownership confirmation  
- Access point verification  
- Parcel extent verification  

## 3.3 Statewide & Regional Directories
Check:
- Ohio campground directories  
- Ohio tourism directories  
- Regional recreation guides  
- Scout council property lists  
- Church camp directories  
- Fraternal organization property lists  

## 3.4 Organizational Partners
Private lands may appear in:
- Land trust partnership announcements  
- County planning documents  
- Regional trail plans  
- Watershed group projects  

## 3.5 Social Media (Conditional)
Private organization social media is **authoritative only if**:
- Explicitly designated as official  
- Linked from the organization’s website  
- Linked from a county or municipal website  

If official:
- Scan for park/trail announcements  
- Scan for access information  

If not official → **exclude**.

------------------------------------------------------------
# 4. PRIVATE LAND DISCOVERY CONDITIONS

A private or organization‑based Site must be surfaced if:

### ✔ Identity‑bearing (named, mapped, or designated)  
### ✔ Public or limited public access (seasonal, fee‑based, reservation‑only, program‑only)  
### ✔ Appears in authoritative directories  
### ✔ Appears in county GIS as a recreation or natural area  
### ✔ Is a private preserve owned by a nonprofit or foundation  
### ✔ Is a private trail system with public access  
### ✔ Is a private campground with natural area components  
### ✔ Is a private retreat center with trails or natural areas  

### ❌ Exclude:
- Private lands with no public access and no identity‑bearing role  
- HOA open space with no public access  
- Corporate campuses with no public access  
- Private hunting clubs with no public access  
- Private farms with no recreation role  
- Private residences  

## 4.9 Limited‑Access Sites
If access is:
- Seasonal  
- Fee‑based  
- Reservation‑only  
- Program‑only  

→ **Include**, but record access limitations in Notes.

## 4.10 Multi‑County Sites
- **Record all counties exactly as discovered in `counties_raw`**  
- **Do NOT segment multi‑county Sites**  
- Normalization alphabetizes and semicolon‑delimits the county list  

------------------------------------------------------------
# 5. CHILD SITE DISCOVERY RULES

Surface a **child Site** when:
- A named internal unit exists within a private Site  
- A named natural area, recreation area, or facility is documented  
- A named lake area, trail area, or program area is identity‑bearing  

Do **not** surface:
- Amenities without identity  
- Temporary zones  
- Unnamed management areas  

------------------------------------------------------------
# 6. PRIVATE TRAIL SYSTEM DISCOVERY RULES

A private trail system becomes a **Trail** or **Trail Network** if:
- It is named  
- It is mapped  
- It has public or limited public access  
- It is identity‑bearing  

### Multi‑County Trails
- **Record all counties in metadata**  
- **Do NOT segment the trail**  

------------------------------------------------------------
# 7. TRAIL SEGMENT DISCOVERY RULES

Surface **Trail Segments** when:
- Segment‑level geometry exists in county GIS  
- Segment identifiers appear in maps or brochures  

------------------------------------------------------------
# 8. SITE NETWORK DISCOVERY RULES

Surface a **Site Network** when:
- A private organization manages a multi‑site system  
- A corridor‑scale or campus‑scale network is documented  

Rare but must be captured.

------------------------------------------------------------
# 9. ACCESS POINT DISCOVERY RULES

Private Access Points must be surfaced when:
- They appear on official maps  
- They appear in brochures  
- They appear in county GIS  
- They appear in directories  
- They appear in partnership announcements  

Access Points must include raw values only:
- Name or descriptive label  
- Access Point Type (raw)  
- County list (raw)  
- Parent entity (Site, child Site, Trail, Trail Segment)  
- Access level (raw)  
- Source(s)  
- Notes (including access limitations)  

These are passed to the **Access Point Discovery Sub‑Procedure v3.2.2**.

------------------------------------------------------------
# 10. ACCESS LEVEL CLASSIFICATION (RAW)

Discovery must record **raw access level**, not normalized values:

- Public  
- Limited Public  
- Fee‑Based  
- Seasonal  
- Reservation‑Only  
- Program‑Only  
- Private (No Access)  

Normalization assigns final values.

------------------------------------------------------------
# 11. COUNTY‑ANCHORED VERIFICATION (MANDATORY)

## 11.1 Confirm County Boundaries
- Verify the feature lies within the county  
- **Record all counties in metadata**  
- **Do NOT segment multi‑county features**  

## 11.2 Confirm Ownership
Record raw ownership type:
- Private individual  
- Private organization  
- Nonprofit  
- Foundation  
- Fraternal organization  
- Church  
- Scout council  
- HOA  
- Corporate entity  

## 11.3 Confirm Access Points
Identify:
- Trailheads  
- Parking areas  
- Boat launches  
- Scenic overlooks  
- Camp entrances  
- Program‑only entrances  

## 11.4 Naming
Use the **organization’s published name** as authoritative.

------------------------------------------------------------
# 12. LOGGING REQUIREMENTS

Each discovered entity must include:
- Full **Discovery Metadata v3.2.2**  
- Organization name (raw)  
- Entity name (raw)  
- County list (`counties_raw`)  
- Entity type (raw)  
- Ownership type (raw)  
- Access level (raw)  
- Source dataset  
- URL or reference  
- Notes on access limitations  
- Discovery Tier: **8**  
- Uncertainty or conflicts  

All values must be raw and unnormalized.

------------------------------------------------------------
# 13. OUTPUT REQUIREMENTS

Each private or organization‑based entity must output a **Raw Candidate Record** conforming to:

- **Discovery Output Specification v3.2.2**  
- **Discovery Metadata Specification v3.2.2**  
- The appropriate Schema Module v3.2.2  
- The appropriate Vocabulary Module v3.2.2  

No normalized fields may appear in Tier 8 output.

------------------------------------------------------------
# 14. INTEGRATION POINTS

This module integrates with:
- **Discovery Protocol Module v3.2.2**  
- **Discovery Orchestration Module v3.2.2**  
- **Site Discovery Sub‑Procedure v3.2.2**  
- **Trail Discovery Sub‑Procedure v3.2.2**  
- **Trail Segment Discovery Sub‑Procedure v3.2.2**  
- **Trail Network Discovery Sub‑Procedure v3.2.2**  
- **Site Network Discovery Sub‑Procedure v3.2.2**  
- **Access Point Discovery Sub‑Procedure v3.2.2**  
- **Child Site Rules Module v3.2.2**  
- **Discovery Metadata Specification v3.2.2**  
- **Discovery Output Specification v3.2.2**  
- **Normalization Contracts v3.2.2**  
- **Resolution Module v3.2.2**  
- **TSV Output Specifications v3.2.2**  
- **Audit & Logging Module v3.2.2**  
- **County Baseline Module v3.2.2**  

No other module may reference this sub‑procedure directly.

------------------------------------------------------------
# 15. VERSIONING

- This module is **Private & Organization‑Based Discovery Sub‑Procedure v3.2.2**.  
- Updates to private recreation directories or organizational practices may result in v3.3, v3.4, etc.  
- Any change to tier order or workflow must be made in the  
  **Discovery Protocol Module v3.2.2**.

------------------------------------------------------------
# END OF PRIVATE & ORGANIZATION‑BASED DISCOVERY SUB‑PROCEDURE v3.2.2