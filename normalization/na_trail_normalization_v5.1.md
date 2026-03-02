# NATURAL AREAS PROJECT
# TRAIL NORMALIZATION CONTRACT v5.1
(Authoritative Field-Level Rules for Normalizing Resolved Trail Entities)

This module defines the entity-specific normalization rules applied by the
**Normalization Engine v5.x** to produce a fully normalized **Trail** entity
conforming to the **Trail Schema Module v5.x** and ready for insertion into
the **Entity Graph**.

This contract contains no controlled vocabularies.
All vocabularies are defined in the **Trail Vocabulary Module v5.x**.

This contract is authoritative for Trail normalization only.

------------------------------------------------------------
# CHANGES FROM v5.0 → v5.1

- **identity_notes added**: New normalized field surfaced from
  identity_notes_raw; distinct from notes; used for identity
  clarifications, trail vs. segment boundary questions, alternate name
  conflicts, and vocabulary type flags
- **maps simplified**: Rich array format (url/type/description objects)
  replaced by plain semicolon-delimited URL list; object validation
  steps removed; URL-only validation applies
- **Derived Label removed**: No longer computed or stored at any stage
- **Raw input field renames**:
  - notes_raw → identity_notes_raw (identity clarifications)
  - url_all → urls_raw (all URLs)
  - url_raw → url_primary_raw
  - maps_raw remains but is now a plain URL list, not an object array
- **Parent Trail Network removed**: Field dropped; network membership
  tracked exclusively via trail_network_members relationship table
- **Normalization workflow updated**: Steps revised for removed and
  added fields; maps object validation replaced with URL list validation
- **All cross-module references updated to v5.x**

------------------------------------------------------------
# CHANGES FROM v4.0 → v5.0

- `counties_traversed` → `counties` — renamed; alphabetized array
- `primary_managing_agency` → `governance` — renamed
- `secondary_managing_agencies` → `partner_agencies` — renamed
- `map_url` → `maps` — rich array (simplified to URL list in v5.1)
- `network_affiliation` and `Parent Trail Network` removed
- `difficulty` added — optional, authoritative sources only
- `accessibility` added — optional free-text
- `alternate_names` added
- `trail_history` added

------------------------------------------------------------
# 1. PURPOSE

The Trail Normalization Contract v5.1 defines:

- How a Resolved Trail is transformed into a Normalized Trail
- How each Trail Schema v5.x field is validated and normalized
- How Trail Use Type, Surface Type, Origin Type, Status, and Difficulty
  are normalized
- How Alternate Names and Trail History are handled
- How the Maps URL list is validated
- How Identity Notes are surfaced from identity_notes_raw
- How Accessibility free-text is normalized
- How normalization interacts with the Normalization Engine v5.x
- How provenance, conflicts, and uncertainties are recorded
- How normalized entities integrate with the Entity Upsert Engine v5.x

Normalization must:
- Never invent data
- Never infer governance, ownership, or identity
- Never silently correct malformed values
- Always log normalization decisions

------------------------------------------------------------
# 2. INPUTS

## 2.1 Resolved Entity Object
From Resolution Engine v5.x, including:

- resolved identity key
- resolved entity_type = "Trail"
- resolved county set
- resolved governance, partner_agencies
- resolved use type, surface type, origin type, status
- resolved conflicts and uncertainties

## 2.2 Raw Discovery Record v5.1
Including:

- name_raw
- alternate_names_raw
- trail_use_type_raw
- trail_surface_type_raw
- trail_origin_type_raw
- total_length_miles_raw
- counties_raw
- governance_raw
- partner_agencies_raw
- status_raw
- difficulty_raw
- accessibility_raw
- description_raw
- trail_history_raw
- identity_notes_raw
- url_primary_raw
- urls_raw (all URLs)
- maps_raw (semicolon-delimited URL list)
- discovery_tier, discovered_in_tiers
- seeded_from_baseline, baseline_id
- discovery_metadata
- source_map

**Removed from v5.0 raw inputs:**
- notes_raw — renamed to identity_notes_raw
- url_raw — renamed to url_primary_raw
- url_all — renamed to urls_raw
- maps_raw object array — replaced by URL list

**Not applicable for Trails:**
- No gps_lat_raw, gps_lon_raw (trails are multi-location entities)
- No address (trails have no single address)
- No township, municipality (multi-location entities)

## 2.3 Vocabulary Modules v5.x
- Trail Vocabulary Module v5.x (Use Type, Surface Type, Origin Type,
  Status, Difficulty)

## 2.4 Schema Modules v5.x
- Trail Schema Module v5.x

------------------------------------------------------------
# 3. OUTPUTS

Normalization produces:

- A **Normalized Trail Object v5.1** conforming to the Trail Schema
  Module v5.x
- A **Normalization Provenance Record**
- A **Validation Result Object** (warnings, errors)
- A normalized entity ready for the **Entity Upsert Engine v5.x**

No new information may be invented.

------------------------------------------------------------
# 4. NORMALIZATION WORKFLOW (HIGH-LEVEL)

1.  Receive Resolved Trail from Normalization Engine v5.x
2.  Validate identity and entity_type = "Trail"
3.  Normalize Trail Name
4.  Normalize Alternate Names
5.  Normalize Trail Use Type
6.  Normalize Trail Surface Type
7.  Normalize Trail Origin Type
8.  Normalize Total Length
9.  Normalize Counties
10. Normalize Governance, Partner Agencies
11. Normalize Status
12. Normalize Difficulty
13. Normalize Accessibility
14. Normalize Description
15. Normalize Trail History
16. Normalize Identity Notes
17. Normalize Notes
18. Normalize URL
19. Normalize Maps (URL list)
20. Run integrity anchor deduplication check (via Normalization Engine)
21. Validate against Trail Schema v5.x
22. Emit Normalized Trail + provenance

If any critical step fails → return error to Normalization Engine v5.x.

------------------------------------------------------------
# 5. FIELD-BY-FIELD NORMALIZATION RULES

## 5.1 Trail Name

- Use resolved name with minimal whitespace cleanup only.
- Must be the official published name.
- Must not include unofficial descriptors.
- Alternate or historical names → Alternate Names field, not Trail Name.
- Never infer names from segments, networks, or amenities.

**Provenance:** Log all name conflicts and corrections.

---

## 5.2 Alternate Names

- Optional.
- Semicolon-delimited in TSV; array in JSON.
- Include only documented historical or variant names from authoritative
  sources.
- Must not include marketing names, slogans, or invented names.
- Must not repeat the Trail Name itself.
- Leave blank if no alternate names are documented.

---

## 5.3 Trail Use Type

- Must match a controlled value from Trail Vocabulary Module v5.x.
- Describes the primary intended use of the Trail as a whole.
- One value only.
- "Multi-Use" only when explicitly documented as such.
- Never infer from surface type, trail name, or amenities.
- If ambiguous → leave blank and flag in identity_notes.

**Common normalization mappings:**
- "multi-purpose" → "Multi-Use"
- "walking trail" → "Hiking"
- "bike path" → "Bicycling"
- "MTB trail" → "Mountain Bike"
- See Trail Vocabulary Module v5.x Section 9 for full mapping table.

---

## 5.4 Trail Surface Type

- Must match a controlled value from Trail Vocabulary Module v5.x.
- Describes the predominant surface type of the Trail as a whole.
- One value only.
- Never infer from imagery alone.
- "Mixed" only when explicitly documented.
- "Paved" covers both asphalt and concrete.

**Common normalization mappings:**
- "asphalt" → "Paved"
- "crushed limestone" → "Crushed Stone"
- "dirt trail" → "Natural Surface"
- See Trail Vocabulary Module v5.x Section 9 for full mapping table.

---

## 5.5 Trail Origin Type

- Must match a controlled value from Trail Vocabulary Module v5.x.
- Must be explicitly documented — not inferred from alignment, age,
  or name.
- One value only.
- Leave blank if origin is undocumented.

**Common normalization mappings:**
- "rails-to-trails" → "Rail Trail"
- "towpath" → "Canal Towpath"
- "power line trail" → "Utility Corridor"
- See Trail Vocabulary Module v5.x Section 9 for full mapping table.

---

## 5.6 Total Length (Miles)

- Numeric only — no units, no ranges, no approximation symbols.
- Represents the total length of the Trail as a whole.
- Never estimate.
- If sources conflict → use most authoritative source (managing agency
  preferred); log conflict.
- Leave blank if unknown.

---

## 5.7 Counties

- Required.
- Must match official Ohio county names.
- Alphabetized.
- Semicolon-delimited.
- Omit the word "County."
- A multi-county Trail is **one entity** — never segmented by county.
- All counties traversed must be represented.

---

## 5.8 Governance

- Must contain the **actual name(s)** of the operational managing
  organization(s).
- Semicolon-delimit if multiple co-managers with equal authority.
- Must not use generic categories.
- Must not encode ownership, designation, or access rules.
- Leave blank if unverifiable.

**Examples:**
- ✅ "Ohio Department of Natural Resources"
- ✅ "Wood County Park District;Metroparks Toledo"
- ❌ "County Parks" — too generic

---

## 5.9 Partner Agencies

- Must contain the **actual names** of formally documented partner
  organizations.
- Semicolon-delimit if multiple.
- Must not use generic categories.
- Must not duplicate Governance.
- Must not encode temporary volunteer activity or informal
  relationships.
- Leave blank if no documented partner agencies exist.

---

## 5.10 Status

- Must match a controlled value from Trail Vocabulary Module v5.x.
- Describes the Trail as a whole — not individual segments.
- "Closed" = permanently closed only.
- "Planned" must be explicitly documented.
- Never infer from imagery or social media.
- Temporary closures → Notes.
- "Gap" applies when a missing portion is the defining characteristic
  of the trail's current state.

---

## 5.11 Difficulty

- Must match a controlled value from Trail Vocabulary Module v5.x.
- Optional — leave blank if not documented by authoritative source.
- **CRITICAL:** Only populate from explicit authoritative source
  ratings — never assess yourself, never infer.
- When trail-level and segment-level difficulty differ → trail-level
  reflects the overall characterization from the source.

**Common normalization mappings:**
- "beginner" → "Easy"
- "intermediate" → "Moderate"
- "hard" / "advanced" / "challenging" → "Difficult" (verify context)
- "expert only" / "black diamond" → "Expert"

---

## 5.12 Accessibility

- Free-text — no controlled vocabulary.
- Optional — leave blank if no accessibility information is documented.
- Record the accessibility description as documented by the
  authoritative source.
- Must not be inferred from surface type alone.
- Must not include personal assessments.

---

## 5.13 Description

- 1-3 sentences.
- Must describe identity-defining characteristics: ecological, cultural,
  historical, or physical character of the Trail.
- Must not include governance, ownership, amenities, or temporary
  conditions.
- Must not contradict controlled fields.
- Must not be copied verbatim from source — paraphrase or synthesize.

---

## 5.14 Trail History

- Optional free-text.
- Captures historical origin, corridor history, and significant
  milestones.
- Particularly important for Rail Trails, Canal Towpaths, and Historic
  Routes.
- Must not duplicate Description.
- Must not include current operational details (those go in Notes).
- Must be documented — not invented.

---

## 5.15 Identity Notes

Surfaced from `identity_notes_raw` at discovery stage.

**Use for:**
- Trail vs. trail segment boundary questions
- Alternate name conflicts
- Network membership uncertainty
- Disambiguation notes (e.g., why this is a Trail vs. a Trail Network)
- Vocabulary type flags (e.g., "source calls this 'pathway' — may be
  Hiking or Multi-Use; flagged for review")
- Notes added during Resolution or Normalization passes

**Rules:**
- Must not duplicate Notes content
- Must not contain operational or contextual notes (those go in Notes)
- Preserve uncertainty flags — do not resolve silently

---

## 5.16 Notes

- Optional free text.
- Use for: temporary closures, access restrictions, parking notes,
  trailhead details, gap locations, construction updates.
- Must not include identity-defining characteristics (those belong in
  Description or Identity Notes).
- Must not include historical origin narrative (that belongs in Trail
  History).
- Must not contradict controlled fields.

---

## 5.17 URL

- Full https:// URL to primary authoritative source.
- Single value.
- Must be stable and authoritative.
- Remove tracking parameters.
- Leave blank if no authoritative URL exists.

---

## 5.18 Maps

- Semicolon-delimited list of URLs to trail map resources.
- Includes: PDF maps, GPX files, KML files, interactive map viewers,
  GIS layers, elevation profiles.
- Each URL must be well-formed https://.
- Remove malformed URLs — log as warning.
- Remove duplicates.
- Distinct from URL — maps are navigation and geometry resources;
  URL is the trail's web presence.
- Leave blank if none.

**Validation rules:**
- Each entry must be a well-formed https:// URL
- No embedded metadata (type, description) — URLs only
- No empty segments (no consecutive semicolons)

---

## 5.19 Network Affiliation / Parent Trail Network — REMOVED IN v5.0

- `network_affiliation` and `parent_trail_network` are no longer fields
  in the Trail schema.
- Network membership tracked exclusively via `trail_network_members`
  relationship table.
- If present in older resolved records → silently drop.

------------------------------------------------------------
# 6. MULTI-COUNTY NORMALIZATION RULES

- A Trail spanning multiple counties produces **one normalized entity**.
- `counties` must include all counties traversed, alphabetized,
  semicolon-delimited.
- Never segment multi-county Trails.
- No township or municipality fields for Trails.

------------------------------------------------------------
# 7. IDENTITY ANCHOR VALIDATION

The integrity anchor for Trails is:
`entity_type` + `name` + `counties`

This contract must verify:
- All anchor fields are present and non-blank
- `counties` is a valid, alphabetized list

The Normalization Engine v5.x runs the deduplication check after this
validation.

------------------------------------------------------------
# 8. VALIDATION LOGIC

Normalization must validate:

- All vocabulary-controlled fields map to valid values
- Total Length: numeric only, no units
- Counties: alphabetized, semicolon-delimited, "County" stripped
- Maps: each entry is a well-formed https:// URL; no embedded metadata
- Alternate Names: semicolon-delimited, no duplicates, no repeat of
  Trail Name
- Semicolon formatting: trimmed, no empty segments
- No invented data
- Blank fields are true blanks
- No delimiter characters inside field values

If any field fails validation:
- Surface as warning or error (per severity)
- Do not silently correct
- Log in normalization provenance

------------------------------------------------------------
# 9. DELIMITER INTEGRITY REQUIREMENTS

Normalization must ensure:

- Blank fields are true blanks
- No spaces between semicolons and values
- No trailing spaces or newlines within fields
- No collapsed delimiters (consecutive semicolons)
- No missing delimiters in multi-value fields

All anomalies must be logged.

------------------------------------------------------------
# 10. CONFLICT HANDLING

### 10.1 Conflicting Names
- Use the most authoritative source.
- Record alternates in Alternate Names field.
- Log conflict.

### 10.2 Conflicting Length
- Use the most authoritative source (managing agency preferred).
- Log conflict; flag for review if unresolvable.

### 10.3 Conflicting Use Type, Surface Type, or Origin Type
- Use authoritative trail system sources.
- If unclear → leave blank, flag in identity_notes.

### 10.4 Conflicting Difficulty
- If sources disagree → leave blank, log conflict.
- Never average or choose arbitrarily.

### 10.5 Conflicting Status
- Use most recent authoritative documentation.
- Log conflict.

------------------------------------------------------------
# 11. MISSING DATA RULES

- If data is missing and cannot be verified → leave blank.
- Never estimate length.
- Never infer use type, surface type, or origin type.
- Never infer difficulty.
- Never infer governance from ownership or vice versa.

------------------------------------------------------------
# 12. AUDITABILITY REQUIREMENTS

Normalization must record in `normalization_provenance`:

- All sources consulted
- All vocabulary mappings applied
- All conflicts detected and how handled
- All fields left blank and why
- Maps URL validation results (valid/invalid URLs, duplicates removed)
- Difficulty source (which URL provided the rating)
- Identity Notes content surfaced from identity_notes_raw
- All delimiter-integrity corrections
- Identity anchor validation result
- Deduplication check result

Never overwrite previously logged normalization decisions.

------------------------------------------------------------
# 13. MODULE DEPENDENCIES

This contract depends on:

- Trail Vocabulary Module v5.x
- Trail Schema Module v5.x
- Discovery Output Specification v5.x
- Resolution Engine v5.x
- Normalization Engine v5.x
- Entity Upsert Engine v5.x
- Audit & Logging Module v5.x

------------------------------------------------------------
# END OF TRAIL NORMALIZATION CONTRACT v5.1
