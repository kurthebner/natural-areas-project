# NATURAL AREAS PROJECT — SITE NETWORK VOCABULARY MODULE v1
Authoritative, versioned controlled vocabularies for Site Networks in the statewide
Natural Areas & Trails system.

This module defines:
- The controlled vocabulary for Site Network fields
- Field‑level rules for vocabulary usage
- Dependencies on the Site Network Schema Module v1

This module contains only controlled vocabularies.
All structural rules are defined in the Site Network Schema Module v1.

------------------------------------------------------------
# 1. PURPOSE
The Site Network Vocabulary Module v1 provides the authoritative, statewide‑consistent
controlled vocabularies required by the Site Network Schema Module v1.

This module:
- Ensures consistent classification of Site Networks
- Prevents ambiguous or invented network types
- Supports normalization, discovery, resolution, and TSV output
- Establishes a single source of truth for Site Network terminology

This module is authoritative for all Site Network vocabulary.

------------------------------------------------------------
# 2. VOCABULARY FIELDS
This module defines controlled vocabularies for:

1. Network Type

No other Site Network fields use controlled vocabularies.

------------------------------------------------------------
# 3. NETWORK TYPE (AUTHORITATIVE LIST)
Network Type describes the classification of the Site Network.
Values must be used exactly as written.

Allowed values:

- National Heritage Area
- Local Historic District
- Scenic River Corridor
- Conservation Corridor
- Cultural Landscape Network
- Watershed Network
- Greenway Network
- Ecological Corridor
- Heritage Corridor
- Historic Corridor
- Multi‑Site Recreation Network
- Multi‑Site Conservation Network

Rules:
- Must not encode governance, ownership, or temporary conditions.
- Must not be inferred; must be documented in authoritative sources.
- Additional values may be added in future versions as needed.

------------------------------------------------------------
# 4. VOCABULARY RULES
- All values must be used exactly as written.
- No synonyms, abbreviations, or invented terms.
- If a Site Network does not clearly match a value, leave the field blank and flag for review.
- New values may be added only through a versioned update to this module.

------------------------------------------------------------
# 5. MODULE DEPENDENCIES
This module depends on:

- Site Network Schema Module v1  
  (for structural rules and field definitions)

All other modules (Discovery, Normalization, TSV Output, Resolution, Orchestration)
must reference this vocabulary.

------------------------------------------------------------
# END OF SITE NETWORK VOCABULARY MODULE v1