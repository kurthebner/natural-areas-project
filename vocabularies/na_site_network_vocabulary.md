# NATURAL AREAS PROJECT — SITE NETWORK VOCABULARY MODULE v3.2.2
Authoritative, versioned, single‑source‑of‑truth controlled vocabularies  
for all Site Network–level fields in the statewide Natural Areas & Trails system.

This module contains:
- All controlled vocabularies used in the Site Network Schema v3.2.2  
- Definitions and rules for each vocabulary  
- Clarifications for ambiguous or overlapping values  

All Site Network–related modules must reference this module for vocabulary authority.

------------------------------------------------------------
# 1. NETWORK TYPE VOCABULARY (Controlled)

## Allowed Values
National Heritage Area  
Local Historic District  
Scenic River Corridor  
Conservation Corridor  
Cultural Landscape Network  
Watershed Network  
Greenway Network  
Ecological Corridor  
Heritage Corridor  
Historic Corridor  
Multi‑Site Recreation Network  
Multi‑Site Conservation Network  
Other (explicitly named only)

## Rules & Clarifications
- Describes the **identity‑bearing classification** of the Site Network.  
- Must not encode governance, ownership, or management.  
- Must not encode temporary conditions or project phases.  
- Must not be inferred; must be documented in authoritative sources.  
- “National Heritage Area” applies only to federally designated NHAs.  
- “Local Historic District” applies only to formally designated districts.  
- “Scenic River Corridor” applies only to documented scenic river systems.  
- “Greenway Network” applies to planned or documented greenway systems.  
- “Other” may be used only when an authoritative source provides a named network type not covered above.  
- Must not duplicate or conflict with the **Parent Site Network** or **Network Affiliation** fields in Site records.

------------------------------------------------------------
# 2. VOCABULARY RULES
- All values must be used exactly as written.  
- No synonyms, abbreviations, or invented terms.  
- If a Site Network does not clearly match a value, leave the field blank and flag for review.  
- New values may be added only through a versioned update to this module.  

------------------------------------------------------------
# 3. MODULE DEPENDENCIES
This module depends on:

- **Site Network Schema Module v3.2.2**  
  (for structural rules and field definitions)

All other modules (Discovery, Normalization, TSV Output, Resolution, Orchestration)  
must reference this vocabulary.

------------------------------------------------------------
# END OF SITE NETWORK VOCABULARY MODULE v3.2.2