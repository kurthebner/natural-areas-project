# NATURAL AREAS PROJECT — DISCOVERY PROTOCOL MODULE v1
A deterministic, statewide, multi‑source discovery workflow for identifying all candidate **Sites** and **Access Points** for the Natural Areas & Trails dataset.

This module governs *what is discovered* and *how it is surfaced*, not how it is normalized or serialized.

This module contains no controlled vocabularies.  
All vocabularies are defined in the Site Vocabulary Module v1 and Access Point Vocabulary Module v1.

---

# 1. PURPOSE
The Discovery Protocol defines:

- What qualifies as a discoverable **Site**  
- What qualifies as a discoverable **Access Point**  
- Which authoritative sources must be scanned  
- How candidates are extracted  
- How duplicates are handled  
- How ambiguous cases are surfaced  
- How discovery metadata is recorded  

This module ensures:

- Statewide consistency  
- Zero improvisation  
- Zero reliance on memory  
- Deterministic, repeatable sweeps  
- Full auditability  

Normalization rules live in the Site and Access Point Normalization Contracts.  
Ambiguous cases are resolved in the Resolution Module.

---

# 2. WHAT COUNTS AS A DISCOVERABLE ENTITY

Discovery surfaces **two entity types**:

- **Sites** (25‑field schema)  
- **Access Points** (10‑field schema)  

Discovery does **not** assign vocabularies or schema fields.  
It only identifies candidates.

---

# 2A. WHAT COUNTS AS A “SITE”
A candidate must be surfaced as a Site if it meets **any** of the following identity criteria.

## 2A.1 Ecological Identity
- Natural area  
- Nature preserve  
- Conservation area  
- Wetland, fen, prairie, bog, marsh, swamp  
- Riparian corridor  
- Forest (upland, floodplain, old‑growth, successional)  
- Wildlife area  
- Restoration area (if named or designated)  

## 2A.2 Governance Identity
- Municipal, township, county, or park district park  
- State or federal land with public access  
- Land trust or conservancy property  
- Privately owned but **designated** natural area  
- Tribal conservation land  

## 2A.3 Trail Infrastructure (as Sites)
- Trail systems  
- Trail corridors  
- Named trail segments  
- Linear parks  
- Greenways  

## 2A.4 Water‑Based Sites
- Water access sites  
- Reservoir properties  
- Named shoreline or riverfront units  

## 2A.5 Special Cases (Always Included)
- Cemeteries with natural areas  
- Stormwater greens with ecological identity  
- Multi‑site complexes (parks with internal natural areas)  
- Mitigation banks (if named or designated)  

---

# 2B. WHAT COUNTS AS AN “ACCESS POINT”
Discovery must surface an Access Point candidate when **any** of the following appear in authoritative sources:

- Trailhead  
- Parking area serving a Site  
- Boat ramp  
- Watercraft access point  
- Fishing access  
- River access  
- Roadside pull‑off  
- Pedestrian entrance  
- Vehicle entrance  
- Bicycle access  
- Snowmobile access  
- Cross‑country ski access  
- Equestrian access  
- Administrative access (if explicitly documented)  

Discovery **does not** assign Access Point Type.  
Normalization assigns it using the Access Point Vocabulary Module v1.

---

# 3. SOURCES COPILOT MUST CHECK (ORDER OF AUTHORITY)

## 3.1 County‑Level Sources
- County park district websites  
- County GIS viewers  
- County recreation/parks departments  
- County conservation districts  
- County planning commissions  
- County greenway/trail plans  
- County open space inventories  

## 3.2 Municipal Sources  
For **every** city, village, and incorporated town:

- Municipal websites  
- Parks & recreation departments  
- Municipal GIS viewers  
- Park maps, PDFs, brochures  
- Capital improvement plans  
- Trail master plans  

## 3.3 Township Sources  
For **every** township:

- Township websites  
- Township parks/facilities pages  
- Township zoning maps  
- Township recreation plans  

## 3.4 State Sources
- ODNR (parks, preserves, wildlife areas, forests, scenic rivers)  
- Ohio History Connection  
- Ohio Scenic Byways  
- Ohio Greenways  
- Statewide trail systems (Buckeye Trail, North Country Trail)  

## 3.5 Federal Sources
- National Park Service  
- U.S. Fish & Wildlife Service  
- U.S. Forest Service  
- U.S. Army Corps of Engineers  
- National Scenic Trails  
- National Heritage Areas  

## 3.6 Land Trusts & Conservancies
- Local land trusts  
- Regional conservancies  
- National organizations with local holdings (e.g., TNC)  

## 3.7 Supplemental Sources (Discovery Only)
- County auditor parcel maps (for unnamed natural areas)  
- Trail apps (secondary confirmation only)  
- Google Maps (secondary confirmation only)  
- Local tourism boards  
- Private organizations with likely holdings (e.g., camps, fraternal lands)  

No unofficial or user‑generated sources may be used as primary evidence.

---

# 4. DISCOVERY WORKFLOW (DETERMINISTIC)

## 4.1 Load County Baseline
- Load the county’s starter list (County Baseline Module).  
- Mark each baseline site as “seeded.”  
- Begin searching for additions.

## 4.2 Perform the Authority Sweep
For each source category (county → municipal → township → state → federal → land trust):

1. Extract all named Sites  
2. Extract all mapped Sites  
3. Extract all Access Points  
4. Extract natural areas within larger parks  
5. Extract linear parks and greenways  
6. Extract water access sites  
7. Extract cemeteries with natural areas  
8. Extract stormwater greens with ecological identity  
9. Extract unnamed natural areas visible in GIS  

## 4.3 Deduplicate (Discovery‑Level)
- Match by name  
- Match by location  
- Match by GPS  
- Match by parcel identity  
- Preserve all conflicting information  

Deduplication is **non‑destructive**.  
Normalization performs final deduplication.

## 4.4 Do Not Classify
Discovery must **not** assign:

- Category  
- Subtype  
- Designation  
- Status  
- Features  
- Trail Role  
- Trail Segment Type  
- Trail Access Type  
- Parent Site  
- Derived Label  

These belong to normalization.

## 4.5 Flag Ambiguous Cases
Discovery must surface a candidate when:

- A name appears but the type is unclear  
- A site appears on one map but not another  
- A trail segment appears unnamed  
- A feature might be a Site or Access Point  
- A water access appears but is unlabeled  

Ambiguity must never suppress discovery.  
Ambiguity is resolved in the Resolution Module.

---

# 5. INCLUSION RULES (MANDATORY)
A candidate **must** be included if:

- It has ecological identity  
- It is a park of any governance level  
- It is a trail system, segment, or access point  
- It is a water access site  
- It is a cemetery with natural area  
- It is a greenway or linear park  
- It is a stormwater green with ecological identity  
- It is a land trust property  
- It is a private natural area with public access  
- It is a private or public natural area with **formal designation** even without public access  

---

# 6. EXCLUSION RULES (MANDATORY)
A candidate **must** be excluded if:

- It is purely a sports facility  
- It is a school athletic complex  
- It is a private business (e.g., golf course)  
- It is a temporary event space  
- It is purely indoor  
- It is a standalone building  
- It is a stormwater basin with no ecological identity  
- It is a private residence with no designation  

---

# 7. DISCOVERY OUTPUT STRUCTURE
Each raw candidate must include:

- Name (as discovered)  
- URL(s)  
- Source type (county, municipal, township, state, federal, land trust)  
- Notes on discovery context  
- Any available GPS  
- Any available address  
- Any available acreage  
- Any available trail role  
- Any available designation  
- Any access‑related information (for Access Points)  

This raw list is passed to the Site or Access Point Normalization Contract.

---

# 8. AUDITABILITY REQUIREMENTS
Copilot must:

- Record the source of each discovery  
- Record the URL or GIS layer used  
- Record any conflicts  
- Never invent data  
- Never infer ownership or designation  
- Never assume access  
- Preserve all discovery metadata  

---

# 9. MODULE DEPENDENCIES
This module depends on:

- **Site Schema Module v1**  
- **Access Point Schema Module v1**  
- **Site Vocabulary Module v1**  
- **Access Point Vocabulary Module v1**  
- **Site Normalization Contract v1**  
- **Access Point Normalization Contract v1**  
- **Resolution Module v1**  
- **Processing Orchestration Module v1**  
- **Audit & Logging Module**

---

# END OF DISCOVERY PROTOCOL MODULE v1