# NATURAL AREAS PROJECT — COUNTY BASELINE MODULE v3.2.2
Authoritative definition of how user‑authored county baseline spreadsheets are
interpreted, preserved, and integrated into the Natural Areas processing pipeline.

This module contains no controlled vocabularies.  
All vocabularies are defined in the respective Vocabulary Modules v3.2.2.

------------------------------------------------------------
# 1. PURPOSE

The County Baseline Module v3.2.2 defines:

- What a county baseline *is*  
- How baseline spreadsheets are interpreted  
- How baseline identity is preserved  
- How baseline integrates with discovery and resolution  
- How baseline interacts with normalization  
- How multi‑county baseline entries are handled  
- How baseline metadata is recorded  

This module ensures:

- Deterministic identity seeding  
- Zero invention  
- Zero normalization  
- Zero silent correction  
- Full auditability  
- Full compatibility with the v3.2.2 pipeline  

------------------------------------------------------------
# 2. BASELINE ORIGIN AND NATURE

County baselines are **not county‑authored datasets**.

They are:

- User‑authored research artifacts  
- Derived from a single master spreadsheet created over time  
- Later split into county‑specific spreadsheets  
- A mixture of copied rows and user‑edited rows  
- Evolving documents that reflect accumulated knowledge  

Baselines are therefore:

- Semi‑structured  
- Incomplete  
- Non‑normalized  
- Non‑standardized  
- Identity‑bearing only  

They are authoritative only for **“this entity exists”**, not for any specific field value.

------------------------------------------------------------
# 3. SCOPE OF BASELINE CONTENT

A county baseline may contain **any** of the six entity types:

- Site  
- Access Point  
- Trail  
- Trail Segment  
- Trail Network (rare but allowed)  
- Site Network (rare but allowed)  

In practice, baselines are:

- **Mostly Sites**  
- **Sometimes Access Points**  
- **Occasionally Trails or Trail Segments**  
- **Rarely Networks**  

No entity type is required.  
No entity type is prohibited.

------------------------------------------------------------
# 4. BASELINE STRUCTURE

Baselines are stored as spreadsheets with:

- One row per entity  
- Arbitrary columns  
- Arbitrary column order  
- Arbitrary field names  
- Arbitrary completeness  

The only required field is:

- **Name** (identity‑bearing)

All other fields are optional and may be:

- Blank  
- Partial  
- Inconsistent  
- User‑defined  
- County‑specific  
- Historically accumulated  

Baseline spreadsheets are **not** required to match any schema.

------------------------------------------------------------
# 5. BASELINE FIELD INTERPRETATION

Baseline fields are treated as **hints**, not authoritative values.

Examples:

- Description → hint  
- Acres → hint  
- Address → hint  
- Management → hint  
- URL → hint  
- GPS → hint  
- Notes → hint  

Baseline fields must never be:

- Normalized  
- Corrected silently  
- Reformatted  
- Interpreted as authoritative  

Normalization happens later.

------------------------------------------------------------
# 6. MULTI‑COUNTY BASELINE RULES (UNIVERSAL)

If a baseline entry spans multiple counties:

- Preserve the raw county list exactly as written  
- Do not expand into multiple entries  
- Do not alphabetize  
- Do not normalize  
- Do not infer missing counties  

Normalization later converts raw lists into:

- **semicolon‑delimited, alphabetized lists**

------------------------------------------------------------
# 7. BASELINE IDENTITY RULES

## 7.1 Baseline entries are identity seeds
Baseline defines the initial list of “things that exist in this county.”

## 7.2 Baseline identity overrides discovery identity
If discovery finds a matching entity:
- Baseline identity wins  
- Discovery metadata is merged  

## 7.3 Baseline does not determine entity type
Entity type is determined later by:
- Discovery  
- Resolution  
- Normalization Contracts  

## 7.4 Baseline does not determine parent/child relationships
Parent Site and parent Trail relationships are assigned later.

## 7.5 Baseline does not determine governance
Governance is resolved later.

------------------------------------------------------------
# 8. BASELINE INTEGRATION RULES

During Stage 1 (Load Baseline):

- Load all rows exactly as written  
- Mark all entries `seeded_from_baseline = true`  
- Preserve all raw fields  
- Preserve all raw formatting  
- Preserve all raw county lists  
- Do not normalize  
- Do not expand  
- Do not infer  

During Stage 2 (Discovery):

- Discovery may add new entities  
- Discovery may not override baseline identity  

During Stage 3 (Resolution):

- Resolution may override baseline entity type  
- Resolution may split baseline entries into child Sites if rules require  

------------------------------------------------------------
# 9. BASELINE CONFLICT RULES

If baseline conflicts with discovery:

- Baseline identity wins  
- Discovery metadata is appended  
- Conflict is logged  

If baseline conflicts with normalization:

- Normalization applies formatting rules  
- Baseline identity is preserved  
- Conflict is logged  

If baseline conflicts with authoritative sources:

- Resolution determines the final identity  
- All conflicts are logged  

------------------------------------------------------------
# 10. BASELINE METADATA REQUIREMENTS

For each baseline entry, metadata must record:

- Source (baseline spreadsheet)  
- Original row number  
- Raw field values  
- Raw county list  
- Any anomalies detected  
- Any conflicts with discovery  
- Any conflicts with normalization  
- Any Resolution overrides  

------------------------------------------------------------
# 11. BASELINE OUTPUT

The baseline module produces:

- A county‑scoped identity list  
- Raw baseline metadata  
- A unified baseline state for all six entities  

This output is consumed by:

- Discovery Orchestration Module v3.2  
- Resolution Module v3.2.2  
- Normalization Contracts v3.2.2  
- Audit & Logging Module v3.2.2  

------------------------------------------------------------
# 12. MODULE DEPENDENCIES

This module depends on:

- All six Schema Modules v3.2.2  
- All six Vocabulary Modules v3.2.2  
- Discovery Protocol Module v3.2.2  
- Resolution Module v3.2.2  
- Processing Orchestration Module v3.2.2  
- Audit & Logging Module v3.2.2  
- Child Site Rules Module v3.2.2  

------------------------------------------------------------
# END OF COUNTY BASELINE MODULE v3.2.2