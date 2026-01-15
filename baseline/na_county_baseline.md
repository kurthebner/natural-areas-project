# NATURAL AREAS PROJECT — COUNTY BASELINE MODULE v1
A structured, authoritative seed layer containing the initial known **Sites** for each of Ohio’s 88 counties.  
This module anchors discovery and ensures consistent statewide coverage.

This module contains no controlled vocabularies.  
All vocabularies are defined in the Site Vocabulary Module v1 and Access Point Vocabulary Module v1.

---

# 1. PURPOSE
This module defines:

- How county baseline data is stored  
- How Copilot loads and uses baseline lists  
- How baseline entries interact with discovery  
- How conflicts between baseline and discovered data are surfaced  
- How updates to county baselines are handled  

The County Baseline Module provides the initial “known Sites” for each county.  
Discovery expands this list; normalization structures it; resolution clarifies ambiguities.

**Access Points are never included in baselines.**  
They are discovered dynamically.

---

# 2. STRUCTURE OF COUNTY BASELINE DATA
Each county has its own section containing:

- County Name  
- Baseline Site List (one Site per line)  
- Optional notes for special cases  

Each baseline Site entry contains:

- **Name** (required)  
- **URL** (optional)  
- **Notes** (optional)  
- **Any known fields** (optional; discovery and normalization will refine)  

**Format (TSV‑like, human‑editable):**  
Name | URL | Notes

**Example (indented to remain inside this code block):**

    Sugarcreek MetroPark | https://www.metroparks.org/sugarcreek | baseline seed
    Possum Creek MetroPark | https://www.metroparks.org/possum-creek | baseline seed

**Important:**  
- Baseline lists contain **Sites only**.  
- Access Points are discovered later and never appear in baseline files.

---

# 3. HOW COPILOT USES BASELINE DATA

## 3.1 Baseline as Seed Layer
- All baseline Sites are automatically included in the candidate list.  
- Discovery adds additional Sites but never removes baseline entries.  
- If redundancy is found, it is surfaced for review and resolution.

## 3.2 Baseline Precedence
- Baseline names are treated as authoritative unless contradicted by official sources.  
- Baseline URLs are used unless discovery finds a more authoritative link.

## 3.3 Baseline Fields Are Not Final
- Discovery and normalization may refine or expand baseline fields.  
- Baseline data is treated as “minimum viable information.”

## 3.4 Baseline Does Not Override Schema
- If a baseline entry violates schema rules, normalization corrects it.  
- If a baseline entry conflicts with authoritative sources, the conflict is surfaced.

---

# 4. HOW DISCOVERY INTERACTS WITH BASELINE

## 4.1 Discovery Adds, Never Deletes
- Discovery may add new Sites not in the baseline.  
- Discovery never removes baseline entries, even if renamed or merged.  
- If Sites are renamed or merged, the conflict is surfaced for review.

## 4.2 Discovery May Update Baseline Fields
- If discovery finds authoritative data (e.g., GPS, ownership), it is added.  
- Baseline notes remain intact unless superseded by authoritative information.

## 4.3 Discovery Flags Conflicts
- If discovery contradicts baseline ownership, acreage, or designation, the conflict is surfaced for review and resolution.

## 4.4 Access Points Are Independent
- Access Points discovered during the sweep do **not** modify the baseline.  
- Access Points are stored and normalized separately.  
- Baseline never contains Access Points.

---

# 5. BASELINE UPDATE RULES

## 5.1 User‑Driven Updates
- Only the user may add or remove baseline entries.  
- Copilot may suggest additions but never modifies baseline without explicit confirmation.

## 5.2 Versioning
- Each county baseline section includes a version number.  
- Changes must be documented in a simple change log.

## 5.3 Renamed Sites
- If a Site is renamed, the baseline retains the original name in Notes.  
- The normalized record uses the authoritative name.

## 5.4 Merged or Split Sites
- If a baseline Site is split into multiple authoritative Sites, discovery adds the new ones.  
- The original baseline entry remains with a note.

---

# 6. SPECIAL CASES

## 6.1 Counties with Sparse Data
- Baseline may contain only 1–2 known Sites.  
- Discovery is expected to expand these significantly.

## 6.2 Counties with Large Park Districts
- Baseline may include only major Sites.  
- Discovery must enumerate all named Sites and sub‑units.

## 6.3 Counties with No Park District
- Baseline may rely heavily on state, municipal, and township sources.

## 6.4 Multi‑County Sites
- Baseline entries appear in each relevant county.  
- Normalization ensures the County field lists all counties.

## 6.5 Internal Parcels
- Baseline may include internal identity‑bearing units (e.g., named natural areas).  
- These must follow the Internal Parcel Rule in the Resolution Module.

---

# 7. COUNTY BASELINE TEMPLATE
Each county section follows this template:

### COUNTY: [County Name]  
Version: 1.0  
Last Updated: [Date]

(Indented table to keep it inside the code block)

    Name | URL | Notes
    --- | --- | ---
    [Site 1] | [URL] | baseline seed
    [Site 2] | [URL] | baseline seed
    [Site 3] | [URL] | baseline seed

**Notes:**  
- [Optional county‑level notes]

---

# 8. MODULE DEPENDENCIES
This module depends on:

- **Site Schema Module v1**  
- **Site Vocabulary Module v1**  
- **Discovery Protocol v1**  
- **Resolution Module v1**  
- **Site Normalization Contract v1**  
- **Processing Orchestration Module v1**  
- **Audit & Logging Module**

Access Points are handled entirely by their own modules and never appear in baseline.

---

# END OF COUNTY BASELINE MODULE v1