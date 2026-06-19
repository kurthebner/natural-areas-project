# NATURAL AREAS PROJECT
# COUNTY BASELINE MODULE v6.0
(Tier-0 Baseline — Non-Authoritative, Runs After All Other Tiers)

Authoritative definition of how user-authored county baseline spreadsheets are
interpreted, preserved, and integrated into the v6.x Natural Areas pipeline.

This module supersedes County Baseline Module v5.1.

This module contains no controlled vocabularies.
All vocabularies are defined in the respective Vocabulary Modules v6.x.

------------------------------------------------------------
# CHANGES FROM v5.1 → v6.0

- **Entity types updated throughout**: Trail, Trail Segment, and Trail Network
  references replaced with Trailthing. §3 updated to reflect four entity types.

- **Trailthing seeding rule added** (§7.8): Baseline entries that describe
  trail-related entities always seed as Trailthings — the only trail-type entity
  in v6.x. `source_term` is populated from whatever term the baseline row uses
  to describe the entity. The discoverer does not classify further.

- **`unconfirmed_baseline_seed` hold reason documented** (§9): Baseline entries
  that cannot be confirmed as active managed natural areas during Tiers 1–8
  discovery are held with `hold_reason = "unconfirmed_baseline_seed"`. Qualifying
  criteria, required documentation, and resolution paths defined.

- **Pipeline integration updated** (§8): GPS Acquisition is now a single pass
  covering all entity types after resolution. Resolution Pass 2 eliminated.
  References updated to v6.x processing orchestration.

- **Module dependencies updated to v6.0.**

- **All v5.1 rules carried forward**: baseline origin and nature, structure,
  field interpretation, multi-county rules, identity rules, conflict rules,
  metadata requirements, baseline output.

------------------------------------------------------------
# 1. PURPOSE

The County Baseline Module v6.0 defines:

- What a county baseline is
- How baseline spreadsheets are interpreted
- How baseline identity is preserved as **Tier-0 seeds**
- How trail-type baseline entries seed as Trailthings
- How baseline integrates with discovery and resolution in v6.x
- How unconfirmed baseline seeds are held and resolved
- How baseline interacts with normalization and the database
- How multi-county baseline entries are handled at the raw layer
- How baseline metadata is recorded and audited

This module ensures:

- Deterministic identity seeding (Tier-0 only)
- Zero invention
- Zero normalization
- Zero silent correction
- Full auditability
- Full compatibility with the v6.x tiered pipeline

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

They are authoritative only for **"this entity probably exists here"**,
not for any specific field value.

------------------------------------------------------------
# 3. SCOPE OF BASELINE CONTENT

A county baseline may contain any of the four v6.x entity types:

- Site
- Trailthing (replaces Trail, Trail Segment, and Trail Network)
- Site Network
- Access Point

In practice, baselines are:

- Mostly Sites
- Sometimes Access Points
- Occasionally Trailthings
- Rarely Site Networks

No entity type is required. No entity type is prohibited.

**Trail-type entries**: Baseline rows describing trails, trail systems, trail
segments, greenways, water trails, or any other trail-related entity always
seed as Trailthings regardless of what term the baseline uses. See §7.8.

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
- Maps → hint (plain URL list; no type or description metadata)
- Identity Notes → hint
- Notes → hint

Baseline fields must never be:

- Normalized
- Corrected silently
- Reformatted
- Interpreted as authoritative

All normalization and schema enforcement occur later in the v6.x pipeline.

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

- **Sites / Site Networks** → multi-county allowed
- **Trailthings** → multi-county allowed
- **Access Points** → must resolve to a single primary county or be flagged

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
Entity type is determined later by discovery, resolution, and normalization —
with the exception of §7.8 (trail-type entries always seed as Trailthings).

## 7.4 Baseline does not determine parent/child relationships
Parent Site, Trailthing hierarchy, and network relationships are assigned later.

## 7.5 Baseline does not determine governance
Governance is resolved later from authoritative sources.

## 7.6 Baseline does not determine township or municipality
These are GIS-derived fields and must never be populated from baseline data.

## 7.7 Baseline does not determine source_term for Trailthings
`source_term` on a Trailthing record must reflect what an authoritative source
says about the entity — not what the baseline row calls it. The baseline may
seed a Trailthing candidate; the authoritative source provides `source_term`.
If no authoritative source is found during discovery, the baseline term is
preserved as a hint in raw metadata but `source_term` remains blank until
confirmed.

## 7.8 Trail-type baseline entries always seed as Trailthings
Any baseline row describing a trail, trail system, trail segment, greenway,
water trail, rail trail, blueway, or any other trail-related entity seeds as
a **Trailthing** — the only trail-type entity in the v6.x architecture.

- The baseline term (whatever word the row uses — "trail," "greenway,"
  "rail trail," "loop," "system") is preserved in raw metadata.
- `source_term` on the resulting Trailthing record is populated from the
  **authoritative source** found during discovery, not from the baseline row.
- The discoverer does not classify the Trailthing further during seeding.
- If discovery confirms the entity exists, the Trailthing record is fully
  populated per the Trailthing Discovery Sub-Procedure v6.x.
- If discovery cannot confirm the entity, the Trailthing seed is held with
  `hold_reason = "unconfirmed_baseline_seed"` (see §9).

------------------------------------------------------------
# 8. BASELINE INTEGRATION WITH THE v6.x PIPELINE

In v6.x, the baseline operates as **Tier-0** and runs **after** all
authoritative tiers. For full stage definitions see
`processing/na_processing_orchestration_v6.x.md`.

## Load Baseline (Tier-0)
- Load all rows exactly as written
- Mark all entries `seeded_from_baseline = true`
- Assign a `baseline_id` per row
- Preserve all raw fields
- Preserve all raw formatting
- Preserve all raw county lists
- Seed trail-type rows as Trailthings (§7.8)
- Do not normalize
- Do not expand
- Do not infer
- Do not populate township or municipality from baseline values

## Discovery (Tiers 1–8) — runs before Tier-0
- Federal, State, District, County, Township, Municipal, Conservancy,
  and Private tiers run first
- Discovery may add new entities not present in the baseline
- Discovery is not constrained by baseline guesses
- Discovery attempts to confirm each baseline seed during the relevant tier

## Resolution (Authoritative + Baseline)
Resolution receives:
- Authoritative discovery entities (Tiers 1–8)
- Baseline entities (Tier-0)

Resolution may:
- Match baseline entries to discovered entities
- Treat unmatched baseline entries as low-confidence candidates
- Override baseline entity type (subject to §7.8 for trail-type entries)
- Split baseline entries into child Sites if rules require

Baseline is always the **lowest-authority source**.

Baseline entries that cannot be matched to any authoritative discovery entity
are held with `hold_reason = "unconfirmed_baseline_seed"` (see §9).

## GPS Acquisition
GPS Acquisition runs as a single pass after Resolution, covering all entity
types — including those seeded from baseline. Baseline GPS hints feed into
GPS Acquisition as candidate coordinates subject to the same acquisition and
validation rules as all other entities.

## Normalization
Baseline raw values flow into normalization as hints. Normalization applies
schema rules; baseline raw values are preserved in provenance.

------------------------------------------------------------
# 9. UNCONFIRMED BASELINE SEEDS

## 9.1 Definition
An unconfirmed baseline seed is a Tier-0 entry that could not be confirmed
as an active, managed natural area through Tiers 1–8 discovery. The entity
may or may not exist — the baseline asserts it probably does, but no
authoritative source during discovery corroborated that assertion.

## 9.2 Hold Behavior
Unconfirmed baseline seeds are routed to `held_entities` with:
- `hold_reason = "unconfirmed_baseline_seed"`
- `hold_detail`: a plain-language explanation of what was attempted during
  discovery and why confirmation failed

They are **not** upserted to the main entity tables. They are **not** included
in TSV output. They remain in `held_entities` until resolved.

## 9.3 Required Documentation
When an entry is held as `unconfirmed_baseline_seed`, the `hold_detail` field
must contain:
1. Which tiers were searched for this entity
2. What sources were checked
3. Why the entity could not be confirmed (not found, conflicting information,
   source no longer exists, etc.)

Example:
`"Baseline seed 'Sycamore Prairie' (Ottawa County). Searched T1–T8. Not found
in ODNR, county auditor, township websites, or conservancy sources. No
authoritative source documents a managed natural area by this name in Ottawa
County. Determined 2026-05-31."`

## 9.4 Resolution Paths

| Condition | Resolution |
|---|---|
| Authoritative source confirms entity is active and publicly accessible | Remove from `held_entities`; proceed through full pipeline |
| Entity confirmed non-existent, inaccessible, or no longer managed | Remove from `held_entities` with disposition note in `hold_detail`; do not upsert |
| Entity existence uncertain pending field verification | Retain in `held_entities`; add to field visit planning queue |

## 9.5 Not a Substitute for Discovery
`unconfirmed_baseline_seed` is set only after a genuine discovery attempt
during the relevant tier(s). It must not be set preemptively or used to
defer discovery work. If a tier has not yet been worked for the county, the
baseline seed status is simply "pending" — not held.

------------------------------------------------------------
# 10. BASELINE CONFLICT RULES

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
# 11. BASELINE METADATA REQUIREMENTS

For each baseline entry, metadata must record:

- Source (baseline spreadsheet identifier)
- Original row number
- Raw field values
- Raw county list
- `seeded_from_baseline` flag
- `baseline_id`
- Entity type assigned at seeding (including Trailthing for trail-type rows)
- Any anomalies detected (including township/municipality value attempts)
- Any conflicts with discovery
- Any conflicts with normalization
- Any Resolution overrides
- Hold reason and hold detail if held as `unconfirmed_baseline_seed`

Metadata must be preserved in the Audit & Logging system.

------------------------------------------------------------
# 12. BASELINE OUTPUT

The baseline module produces:

- A county-scoped **Tier-0 identity seed list**
- Raw baseline metadata
- A unified baseline state for all four v6.x entity types

This output is consumed by:

- Discovery Protocol Module v6.x (as Tier-0 inputs)
- Resolution Engine v6.x
- Normalization Engine v6.x
- Audit & Logging Module v6.x

Baseline output is never used directly for normalized entities; it always
flows through Resolution and Normalization.

------------------------------------------------------------
# 13. MODULE DEPENDENCIES

This module depends on:

- Site Schema Module v6.0
- Trailthing Schema Module v6.0
- Site Network Schema Module v6.0
- Access Point Schema Module v6.0
- Discovery Protocol Module v6.0
- Resolution Engine v6.0
- Normalization Engine v6.0
- GPS Acquisition Module v6.0
- Child Site Rules Module v6.0
- Audit & Logging Module v6.0

------------------------------------------------------------
# END OF COUNTY BASELINE MODULE v6.0
