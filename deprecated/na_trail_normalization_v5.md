# NATURAL AREAS PROJECT
# TRAIL NORMALIZATION CONTRACT v5.0
(Authoritative Field-Level Rules for Normalizing Resolved Trail Entities)

This module defines the entity-specific normalization rules applied by the
**Normalization Engine v5.0** to produce a fully normalized **Trail** entity
conforming to the **Trail Schema Module v5.0** and ready for insertion into the
**Entity Graph Schema v5.0**.

This contract contains no controlled vocabularies.
All vocabularies are defined in the **Trail Vocabulary Module v5.0**.

This contract is authoritative for Trail normalization only.

------------------------------------------------------------
# CHANGES FROM v4.0

- **`counties_traversed` → `counties`**: Renamed; alphabetized array
- **`primary_managing_agency` → `governance`**: Renamed
- **`secondary_managing_agencies` → `partner_agencies`**: Renamed
- **`map_url` → `maps`**: Rich array format (url / type / description objects)
- **`network_affiliation` and `Parent Trail Network` removed**: Network membership tracked via relationship tables
- **`difficulty` added**: Optional — record only from authoritative sources
- **`accessibility` added**: Optional free-text
- **`alternate_names` added**: Documented historical or variant names
- **`trail_history` added**: Separate field for origin and history narrative
- **No GPS, no address, no township/municipality**: Trails are multi-location entities — these fields do not apply
- **Derived Label**: Computed at TSV output time, NOT during normalization (changed from v4.0)
- Updated all version references to v5.0

------------------------------------------------------------
# 1. PURPOSE

The Trail Normalization Contract v5.0 defines:

- How a Resolved Trail is transformed into a Normalized Trail
- How each Trail Schema v5.0 field is validated and normalized
- How Trail Use Type, Surface Type, Origin Type, Status, and Difficulty are normalized
- How Alternate Names and Trail History are handled
- How the Maps rich array is validated
- How Accessibility free-text is normalized
- How normalization interacts with the **Normalization Engine v5.0**
- How provenance, conflicts, and uncertainties are recorded
- How normalized entities integrate with the **Entity Upsert Engine v5.0**

Normalization must:

- Never invent data
- Never infer governance, ownership, or identity
- Never silently correct malformed values
- Always log normalization decisions

Derived Label is not computed here.
It is computed only during TSV output.

------------------------------------------------------------
# 2. INPUTS

## 2.1 Resolved Entity Object
From **Resolution Engine v5.0**, including:

- resolved identity key
- resolved entity_type = "Trail"
- resolved county set
- resolved governance, partner_agencies
- resolved use type, surface type, origin type, status
- resolved conflicts and uncertainties

## 2.2 Raw Discovery Record v5.0
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
- notes_raw
- url_raw
- maps_raw (array of url/type/description objects)
- discovery_tier, discovered_in_tiers
- seeded_from_baseline, baseline_id
- discovery_metadata
- source_map

**Not applicable for Trails:**
- No gps_raw (trails are multi-location — no single GPS point)
- No address (trails have no single address)
- No township, municipality (multi-location entities)

## 2.3 Vocabulary Modules v5.0
- Trail Vocabulary Module v5.0 (Use Type, Surface Type, Origin Type, Status, Difficulty)

## 2.4 Schema Modules v5.0
- Trail Schema Module v5.0

------------------------------------------------------------
# 3. OUTPUTS

Normalization produces:

- A **Normalized Trail Object v5.0** conforming to the Trail Schema Module v5.0
- A **Normalization Provenance Record**
- A **Validation Result Object** (warnings, errors)
- A normalized entity ready for the **Entity Upsert Engine v5.0**

No new information may be invented.

------------------------------------------------------------
# 4. NORMALIZATION WORKFLOW (HIGH-LEVEL)

1. Receive Resolved Trail from Normalization Engine v5.0
2. Validate identity and entity_type = "Trail"
3. Normalize Trail Name
4. Normalize Alternate Names
5. Normalize Trail Use Type, Surface Type, Origin Type
6. Normalize Total Length
7. Normalize Counties
8. Normalize Governance, Partner Agencies
9. Normalize Status
10. Normalize Difficulty
11. Normalize Accessibility
12. Normalize Description
13. Normalize Trail History
14. Normalize Notes
15. Normalize URL
16. Normalize Maps (rich array)
17. Run integrity anchor deduplication check (via Normalization Engine)
18. Validate against Trail Schema v5.0
19. Emit Normalized Trail + provenance

If any critical step fails → return error to Normalization Engine v5.0.

------------------------------------------------------------
# 5. FIELD-BY-FIELD NORMALIZATION RULES

## 5.1 Trail Name

- Use resolved name with minimal whitespace cleanup only.
- Must be the official published name.
- Must not include unofficial descriptors.
- If multiple authoritative names exist → Resolution Engine v5.0 chooses; use resolved name.
- Alternate or historical names → Alternate Names field, not Trail Name.
- Never infer names from segments, networks, or amenities.

**Provenance:** Log all name conflicts and corrections.

---

## 5.2 Alternate Names ✨ NEW IN v5.0

- Optional.
- Semicolon-delimited in TSV; array in JSON.
- Include only documented historical or variant names from authoritative sources.
- Examples: former names, abbreviations, regional nicknames used by managing agency.
- Must not include marketing names, slogans, or invented names.
- Must not repeat the Trail Name itself.
- Leave blank if no alternate names are documented.

---

## 5.3 Trail Use Type

- Must match a controlled value from Trail Vocabulary Module v5.0.
- Describes the primary intended use of the Trail as a whole.
- One value only — choose the most specific that applies.
- "Multi-Use" only when explicitly documented as such.
- Never infer from surface type, trail name, or amenities.
- If ambiguous → leave blank and log uncertainty.

**Common normalization mappings:**
- "multi-purpose" → "Multi-Use"
- "walking trail" → "Hiking"
- "bike path" → "Bicycling"
- "MTB trail" → "Mountain Bike"
- See Trail Vocabulary Module v5.0 Section 8 for full mapping table.

---

## 5.4 Trail Surface Type

- Must match a controlled value from Trail Vocabulary Module v5.0.
- Describes the predominant surface type of the Trail as a whole.
- One value only.
- Never infer from imagery alone.
- "Mixed" only when explicitly documented.
- Note: "Paved" covers both asphalt and concrete — do not use separate values.

**Common normalization mappings:**
- "asphalt" → "Paved"
- "crushed limestone" → "Crushed Stone"
- "dirt trail" → "Natural Surface"
- See Trail Vocabulary Module v5.0 Section 8 for full mapping table.

---

## 5.5 Trail Origin Type

- Must match a controlled value from Trail Vocabulary Module v5.0.
- Describes the historical or structural origin of the Trail.
- Must be explicitly documented — not inferred from alignment, age, or name.
- One value only.
- Leave blank if origin is undocumented.

**Common normalization mappings:**
- "rails-to-trails" → "Rail Trail"
- "towpath" → "Canal Towpath"
- "power line trail" → "Utility Corridor"
- See Trail Vocabulary Module v5.0 Section 8 for full mapping table.

---

## 5.6 Total Length (Miles)

- Numeric only — no units, no ranges, no approximation symbols.
- Represents the total length of the Trail as a whole.
- Never estimate.
- If sources conflict → use most authoritative source (managing agency preferred).
- Log conflicts in normalization provenance.
- Leave blank if unknown.

---

## 5.7 Counties ✨ RENAMED FROM v4.0 (was `counties_traversed`)

- Required.
- Must match official Ohio county names.
- Alphabetized.
- Semicolon-delimited.
- Omit the word "County" (e.g., "Wood County" → "Wood").
- A multi-county Trail is **one entity** — never segmented by county.
- All counties traversed must be represented.

---

## 5.8 Governance ✨ RENAMED FROM v4.0 (was `primary_managing_agency`)

- Must contain the **actual name(s)** of the operational managing organization(s).
- Semicolon-delimit if multiple managers are formally documented.
- Must not use generic categories (e.g., "County Agency", "Nonprofit").
- Must not encode ownership, designation, or access rules.
- If governance is identical to ownership → repeat explicitly.
- Leave blank if unverifiable.

**Examples:**
- ✅ "Ohio Department of Natural Resources"
- ✅ "Wood County Park District;Metroparks Toledo"
- ❌ "County Parks" — too generic

---

## 5.9 Partner Agencies ✨ RENAMED FROM v4.0 (was `secondary_managing_agencies`)

- Must contain the **actual names** of formally documented partner organizations.
- Semicolon-delimit if multiple.
- Must not use generic categories.
- Must not duplicate Governance.
- Must not encode temporary volunteer activity or informal relationships.
- Leave blank if no documented partner agencies exist.

---

## 5.10 Status

- Must match a controlled value from Trail Vocabulary Module v5.0.
- Describes the Trail as a whole — not individual segments.
- "Closed" = permanently closed only.
- "Proposed" must be explicitly documented.
- Never infer from imagery or social media.
- Temporary closures → Notes.
- "Gap" applies when a missing portion is the defining characteristic of the trail's current state.

---

## 5.11 Difficulty ✨ NEW IN v5.0

- Must match a controlled value from Trail Vocabulary Module v5.0.
- Optional — leave blank if not documented by authoritative source.
- Describes difficulty of the Trail as a whole.
- **CRITICAL:** Only populate from explicit authoritative source ratings.
  - ❌ Do not assess difficulty yourself
  - ❌ Do not infer from length, elevation, or surface type
  - ✅ Only record when managing agency or authoritative source explicitly rates it
- When trail-level and segment-level difficulty differ → trail-level reflects the overall characterization from the source, not an average.

**Common normalization mappings:**
- "beginner" → "Easy"
- "intermediate" → "Moderate"
- "hard" / "advanced" / "challenging" → "Difficult" (verify context)
- "expert only" / "black diamond" → "Expert"

---

## 5.12 Accessibility ✨ NEW IN v5.0

- Free-text — no controlled vocabulary.
- Optional — leave blank if no accessibility information is documented.
- Record the accessibility description as documented by the authoritative source.
- Paraphrase if needed — do not reproduce verbatim from copyrighted sources.
- Must not be inferred from surface type alone.
- Must not include personal assessments.

**Examples of valid values:**
- "ADA accessible from Main Street trailhead; paved surface, grades under 5%"
- "Wheelchair accessible for first 0.5 miles from north trailhead"
- "Not ADA compliant; natural surface with variable grades"

---

## 5.13 Description

- 1-3 sentences.
- Must describe identity-defining characteristics: ecological, cultural, historical, or physical character of the Trail.
- Include naming history and alternate names when relevant.
- Must not include governance, ownership, amenities, or temporary conditions.
- Must not contradict controlled fields.
- Must not be copied verbatim from source — paraphrase or synthesize.

---

## 5.14 Trail History ✨ NEW IN v5.0

- Optional free-text.
- Captures the historical origin, corridor history, and significant milestones of the Trail.
- Particularly important for Rail Trails, Canal Towpaths, and Historic Routes.
- Must not duplicate Description.
- Must not include current operational details (those go in Notes).
- Must be documented — not invented.

**Examples of appropriate content:**
- Former railroad corridor history, abandonment date, conversion timeline
- Canal system history and conversion to trail use
- Historic designation background
- Significant expansions or route changes

---

## 5.15 Notes

- Optional free text.
- Use for: temporary closures, access restrictions, parking notes, trailhead details, gap locations, construction updates.
- Must not include identity-defining characteristics (those belong in Description).
- Must not include historical origin narrative (that belongs in Trail History).
- Must not contradict controlled fields.

---

## 5.16 URL

- Full https:// URL to primary authoritative source.
- Single value.
- Must be stable and authoritative.
- Remove tracking parameters.
- Leave blank if no authoritative URL exists.

---

## 5.17 Maps ✨ NEW IN v5.0 (replaces `map_url`)

The `maps` field is a **rich array** — each element is an object with:
- `url` (required) — full https:// URL
- `type` (required) — one of: PDF, Interactive, Static Image, GIS Layer, Other
- `description` (optional) — brief description of what the map shows

**Normalization rules:**
- Validate each element: url must be well-formed https://; type must match allowed values
- Remove elements with malformed URLs — log as warning
- Remove elements with missing type — log as warning
- `description` may be blank — that is valid
- Preserve order from resolution — do not sort
- Semicolon-delimited in TSV output (urls only); full array in JSON

**Examples of valid elements:**
- `{ url: "https://wcparks.org/slippery-elm-map.pdf", type: "PDF", description: "Official trail map" }`
- `{ url: "https://www.traillink.com/trail/slippery-elm-trail/", type: "Interactive", description: "" }`

**Invalid elements (log and remove):**
- Missing url
- Non-https url
- Type not in allowed values

---

## 5.18 Network Affiliation / Parent Trail Network ✨ REMOVED IN v5.0

- `network_affiliation` and `parent_trail_network` are no longer fields in the Trail schema.
- Network membership is tracked via the `trail_to_network` relationship table.
- If these values are present in resolved records from older discovery runs → silently drop.
- Do not migrate these values to any other field.

------------------------------------------------------------
# 6. MULTI-COUNTY NORMALIZATION RULES

- A Trail spanning multiple counties produces **one normalized entity**.
- `counties` must include all counties traversed, alphabetized, semicolon-delimited.
- Never segment multi-county Trails.
- No township or municipality fields for Trails — these are not applicable to multi-location entities.

------------------------------------------------------------
# 7. IDENTITY ANCHOR VALIDATION

The integrity anchor for Trails is:
`entity_type` + `name` + `counties`

This contract must verify:
- All anchor fields are present and non-blank
- `counties` is a valid, alphabetized list

The Normalization Engine v5.0 runs the deduplication check after this validation.

------------------------------------------------------------
# 8. VALIDATION LOGIC

Normalization must validate:

- All vocabulary-controlled fields map to valid values
- Total Length: numeric only, no units
- Counties: alphabetized, semicolon-delimited, "County" stripped
- Maps array: each element has valid url and type
- Alternate Names: semicolon-delimited, no duplicates, no repeat of Trail Name
- Semicolon formatting: trimmed, no empty segments
- Field types match schema
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
- Log conflict in normalization provenance.

### 10.2 Conflicting Length
- Use the most authoritative source (managing agency preferred).
- If conflict persists → log, use highest-authority value, flag for review.

### 10.3 Conflicting Use Type, Surface Type, or Origin Type
- Use authoritative trail system sources.
- If unclear → leave blank, flag uncertainty.

### 10.4 Conflicting Difficulty
- If sources disagree on difficulty → leave blank, log conflict.
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
- Maps array validation results (valid/invalid elements)
- Difficulty source (which URL provided the rating)
- All delimiter-integrity corrections
- Identity anchor validation result
- Deduplication check result

Never overwrite previously logged normalization decisions.

------------------------------------------------------------
# 13. MODULE DEPENDENCIES

This contract depends on:

- Trail Vocabulary Module v5.0
- Trail Schema Module v5.0
- Discovery Output Specification v5.0
- Resolution Engine v5.0
- Normalization Engine v5.0
- Entity Graph Schema v5.0
- Audit & Logging Module v5.0

------------------------------------------------------------
# END OF TRAIL NORMALIZATION CONTRACT v5.0
