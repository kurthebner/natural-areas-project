# NATURAL AREAS PROJECT
# COUNTY BASELINE MODULE v5.0
(Tier-0 Baseline — Non-Authoritative, Runs After All Other Tiers)

Authoritative definition of how user-authored county baseline spreadsheets are
interpreted, preserved, and integrated into the v5.0 Natural Areas pipeline.

This module contains no controlled vocabularies.
All vocabularies are defined in the respective Vocabulary Modules v5.0.

------------------------------------------------------------
# CHANGES FROM v4.0

- `role` and `access_level` removed from baseline field hints — fields deleted from Access Point schema
- `features_raw`, `difficulty_raw`, `accessibility_raw`, `maps_raw` added as recognized hint fields
- `township_raw` and `municipality_raw` explicitly excluded from baseline interpretation — GIS-derived only; baseline may not supply these
- **Discovery = Collection** principle reinforced — baseline rows are raw seeds, never normalized values
- All version references updated to v5.0

------------------------------------------------------------
# 1. PURPOSE

The County Baseline Module v5.0 defines:

- What a county baseline is
- How baseline spreadsheets are interpreted
- How baseline identity is preserved as **Tier-0 seeds**
- How baseline integrates with discovery and resolution in v5.0
- How baseline interacts with normalization and the Entity Graph
- How multi-county baseline entries are handled at the raw layer
- How baseline metadata is recorded and audited

This module ensures:

- Deterministic identity seeding (Tier-0 only)
- Zero invention
- Zero normalization
- Zero silent correction
- Full auditability
- Full compatibility with the v5.0 tiered pipeline

Baselines are **never authoritative** over agency or GIS sources.

------------------------------------------------------------
# 2. BASELINE ORIGIN AND NATURE

County baselines are **not county-authored datasets**.

They are:

- User-authored research artifacts
- Derived from a master spreadsheet created over time
- Later split into county-specific spreadsheets
- A mixture of copied rows and user-edited rows
- Evolving documents that reflect accumulated knowledge

Baselines are therefore:

- Semi-structured
- Incomplete
- Non-normalized
- Non-standardized
- Identity-bearing only

They are authoritative only for **"this entity probably exists here"**, not for
any specific field value.

------------------------------------------------------------
# 3. SCOPE OF BASELINE CONTENT

A county baseline may contain **any** of the six entity types:

- Site
- Access Point
- Trail
- Trail Segment
- Trail Network
- Site Network

In practice, baselines are:

- Mostly Sites
- Sometimes Access Points
- Occasionally Trails or Trail Segments
- Rarely Networks

No entity type is required. No entity type is prohibited.

------------------------------------------------------------
# 4. BASELINE STRUCTURE

Baselines are stored as spreadsheets with:

- One row per entity
- Arbitrary columns
- Arbitrary column order
- Arbitrary field names
- Arbitrary completeness

The only required field is:

- **Name** (identity-bearing seed)

All other fields are optional and may be:

- Blank
- Partial
- Inconsistent
- User-defined
- County-specific
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
- Features → hint
- Difficulty → hint
- Accessibility → hint
- Maps → hint
- Notes → hint

Baseline fields must never be:

- Normalized
- Corrected silently
- Reformatted
- Interpreted as authoritative

All normalization and schema enforcement occur later in the v5.0 pipeline.

### Fields that must not appear in baselines:

- `township` — must never be supplied via baseline; GIS-derived only
- `municipality` — must never be supplied via baseline; GIS-derived only

If a baseline row contains township or municipality values, those values must be:

- Preserved in raw metadata for provenance
- Never used to populate the township or municipality fields in the normalized record
- Logged as a baseline anomaly

------------------------------------------------------------
# 6. MULTI-COUNTY BASELINE RULES (RAW LAYER)

If a baseline entry spans multiple counties:

- Preserve the raw county list exactly as written
- Do not expand into multiple entries
- Do not alphabetize
- Do not normalize
- Do not infer missing counties

Later stages apply entity-specific rules:

- **Sites / Networks** → multi-county allowed
- **Access Points** → must resolve to a single primary county or be flagged
- **Trails / Trail Segments** → multi-county allowed

The baseline layer never enforces entity-specific county rules.

------------------------------------------------------------
# 7. BASELINE IDENTITY RULES

## 7.1 Baseline entries are Tier-0 identity seeds
Baseline defines an initial list of **candidate entities** for a county:
"This thing probably exists here."

## 7.2 Baseline never overrides authoritative discovery
If authoritative discovery finds a matching entity:
- Authoritative discovery wins
- Baseline identity becomes a supporting or conflicting claim
- All merges and conflicts are logged

## 7.3 Baseline does not determine entity type
Entity type is determined later by:
- Discovery
- Resolution
- Normalization Modules v5.0

## 7.4 Baseline does not determine parent/child relationships
Parent Site, Trail, Trail Segment, and network relationships are assigned later.

## 7.5 Baseline does not determine governance
Governance is resolved later from authoritative sources.

## 7.6 Baseline does not determine township or municipality
These are GIS-derived fields and must never be populated from baseline data.

------------------------------------------------------------
# 8. BASELINE INTEGRATION RULES (v5.0 PIPELINE)

In v5.0, the baseline operates as **Tier-0** and runs **after** all authoritative tiers.

## 8.1 Stage 1 — Load Baseline (Tier-0)
- Load all rows exactly as written
- Mark all entries `seeded_from_baseline = true`
- Assign a `baseline_id` per row
- Preserve all raw fields
- Preserve all raw formatting
- Preserve all raw county lists
- Do not normalize
- Do not expand
- Do not infer
- Do not populate township or municipality from baseline values

## 8.2 Stage 2 — Discovery (Tiers 1–8)
- Federal, State, District, County, Township, Municipal, Conservancy, Private tiers run first
- Discovery may add new entities
- Discovery is not constrained by baseline guesses

## 8.3 Stage 3 — Resolution (Authoritative + Baseline)
Resolution receives:
- Authoritative discovery entities (Tiers 1–8)
- Baseline entities (Tier-0)

Resolution may:
- Match baseline entries to discovered entities
- Treat unmatched baseline entries as low-confidence candidates
- Override baseline entity type
- Split baseline entries into child Sites if rules require

Baseline is always the **lowest-authority source**.

------------------------------------------------------------
# 9. BASELINE CONFLICT RULES

If baseline conflicts with discovery:
- Authoritative discovery + Resolution win
- Baseline identity is preserved as a conflicting claim
- Conflict is logged

If baseline conflicts with normalization:
- Normalization applies schema rules
- Baseline raw values are preserved in provenance
- Conflict is logged

If baseline conflicts with authoritative sources:
- Resolution determines the final identity and type
- Baseline is treated as a historical/user-authored claim
- All conflicts are logged

Baseline is **never** allowed to override authoritative agency or GIS data.

------------------------------------------------------------
# 10. BASELINE METADATA REQUIREMENTS

For each baseline entry, metadata must record:

- Source (baseline spreadsheet identifier)
- Original row number
- Raw field values
- Raw county list
- `seeded_from_baseline` flag
- `baseline_id`
- Any anomalies detected (including township/municipality value attempts)
- Any conflicts with discovery
- Any conflicts with normalization
- Any Resolution overrides

Metadata must be preserved in the Audit & Logging system.

------------------------------------------------------------
# 11. BASELINE OUTPUT

The baseline module produces:

- A county-scoped **Tier-0 identity seed list**
- Raw baseline metadata
- A unified baseline state for all six entities

This output is consumed by:

- Discovery Protocol Module v5.0 (as Tier-0 inputs)
- Resolution Engine v5.0
- Normalization Engine v5.0
- Audit & Logging Module v5.0

Baseline output is never used directly for normalized entities; it always flows
through Resolution and Normalization.

------------------------------------------------------------
# 12. MODULE DEPENDENCIES

This module depends on:

- All six Schema Modules v5.0
- All six Vocabulary Modules v5.0
- Discovery Protocol Module v5.0
- Resolution Engine v5.0
- Normalization Engine v5.0
- Entity Upsert Engine v5.0
- Audit & Logging Module v5.0
- Child Site Rules Module v5.0

------------------------------------------------------------
# END OF COUNTY BASELINE MODULE v5.0
