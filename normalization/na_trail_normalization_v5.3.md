# NATURAL AREAS PROJECT
# TRAIL NORMALIZATION CONTRACT v5.3
(Authoritative Field-Level Rules for Normalizing Resolved Trail Entities)

This module defines the entity-specific normalization rules applied by the
**Normalization Engine v5.x** to produce a fully normalized **Trail** entity
conforming to the **Trail Schema Module v5.x** and ready for insertion into
the **Entity Graph**.

This contract contains no controlled vocabularies.
All vocabularies are defined in the **Trail Vocabulary Module v5.2**.

This contract is authoritative for Trail normalization only.

------------------------------------------------------------
# CHANGES FROM v5.2 → v5.3

**IMP-100 — Trail vocabulary enforcement hardening.**

- **§5.3 Trail Use Type**: Added mandatory read gate for Trail Vocabulary §9.1
  mapping table. Replaced informal synonym list with enforcement language:
  null-and-log on unmappable values; REVIEW on compound values; empty string
  converted to null per §9.6.

- **§5.4 Trail Surface Type**: Added mandatory read gate for Trail Vocabulary
  §9.2 mapping table. Added enforcement language: null-and-log on unmappable
  values; REVIEW on compound values not resolvable as "Mixed"; empty string
  converted to null per §9.6.

- **§5.5 Trail Origin Type**: Added mandatory read gate for Trail Vocabulary
  §9.3 mapping table. Added enforcement language: null-and-log on unmappable
  values (including surface and governance descriptors such as "natural" or
  "wildlife area trail"); REVIEW on compound values; empty string converted
  to null per §9.6.

- **§5.10 Status**: Added mandatory read gate for Trail Vocabulary §9.4
  mapping table. Added "open"/"operational" → "Active" normalization rule
  explicitly. Added empty string → null rule.

- **§5.11 Difficulty**: Added mandatory read gate for Trail Vocabulary §9.5
  mapping table. Codified null-and-log for difficulty ranges ("Easy-Moderate",
  "varies", etc.) — single-value field; document range in Notes. Added empty
  string → null rule.

- **§5.21 Empty String Enforcement (new)**: All five vocabulary-controlled
  Trail fields (use_type, surface_type, origin_type, status, difficulty) treat
  empty string ("") as a data defect — convert to null and log. This applies
  at the end of the normalization pass across all vocabulary fields. See §5.21.

------------------------------------------------------------
# CHANGES FROM v5.1 → v5.2

- **IMP-054 — §5.20 Parent Site (`trail_parents`) population step added**: Trail
  normalization now includes a containment determination pass. After all Trail fields
  are normalized, the Normalization Engine evaluates whether the Trail is wholly
  contained within a single named Site (per Trail Schema Module v5.2 §5.4 containment
  criteria). If contained: insert a row into `trail_parents` (trail_id, parent_site_id)
  and ensure `identity_notes` contains "Contained within [Site Name] ([site_id])."
  If extra-limital: no `trail_parents` row is created; governance field documents site
  association. See §5.20 below.

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

The Trail Normalization Contract v5.3 defines:

- How a Resolved Trail is transformed into a Normalized Trail
- How each Trail Schema v5.x field is validated and normalized
- How Trail Use Type, Surface Type, Origin Type, Status, and Difficulty
  are normalized against the enforcement tables in Trail Vocabulary v5.2 §9.x
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

## 2.3 Vocabulary Modules
- **Trail Vocabulary Module v5.2** — Use Type, Surface Type, Origin Type,
  Status, Difficulty; §9.x enforcement mapping tables (IMP-100).
  **Read §9.x before normalizing any vocabulary-controlled field.**

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
3.  **Read Trail Vocabulary Module v5.2 §9.x** (enforcement mapping tables)
4.  Normalize Trail Name
5.  Normalize Alternate Names
6.  Normalize Trail Use Type (apply §9.1 mapping table)
7.  Normalize Trail Surface Type (apply §9.2 mapping table)
8.  Normalize Trail Origin Type (apply §9.3 mapping table)
9.  Normalize Total Length
10. Normalize Counties
11. Normalize Governance, Partner Agencies
12. Normalize Status (apply §9.4 mapping table)
13. Normalize Difficulty (apply §9.5 mapping table)
14. Normalize Accessibility
15. Normalize Description
16. Normalize Trail History
17. Normalize Identity Notes
18. Normalize Notes
19. Normalize URL
20. Normalize Maps (URL list)
21. Apply §5.21 empty string enforcement across all vocabulary fields
22. Run integrity anchor deduplication check (via Normalization Engine)
23. Validate against Trail Schema v5.x
24. Emit Normalized Trail + provenance

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

**Read Trail Vocabulary Module v5.2 §9.1 before applying this step.**

- Optional. Describes the primary intended use of the Trail as a whole.
- Single value only — compound values are never valid.
- "Multi-Use" only when explicitly documented as such.
- Never infer from surface type, trail name, or amenities.

**Normalization procedure:**

1. Check `trail_use_type_raw` against the §9.1 mapping table.
2. If the raw value maps to a controlled value → apply the mapping; log.
3. If the raw value is a compound (e.g., "Foot;Bike", "Hiking/Biking") →
   route to **REVIEW**; flag in `identity_notes`; leave field blank until
   resolved.
4. If the raw value is unmappable and not compound → **null-and-log**:
   leave blank, record the raw value and reason in `normalization_provenance`.
5. Empty string ("") → null; see §5.21.

**Common mappings (non-exhaustive — §9.1 is authoritative):**
- "foot" / "walking" / "walking trail" → "Hiking"
- "bike path" / "cycling" → "Bicycling"
- "MTB trail" / "mountain biking" → "Mountain Bike"
- "multi-purpose" / "multipurpose" → "Multi-Use"
- "equestrian" / "horse" → "Equestrian"

---

## 5.4 Trail Surface Type

**Read Trail Vocabulary Module v5.2 §9.2 before applying this step.**

- Optional. Describes the predominant surface type of the Trail as a whole.
- Single value only — compound values are never valid unless resolvable
  as "Mixed" with explicit source documentation.
- Never infer from imagery alone.
- "Paved" covers asphalt, concrete, and chip-and-seal.

**Normalization procedure:**

1. Check `trail_surface_type_raw` against the §9.2 mapping table.
2. If the raw value maps to a controlled value → apply the mapping; log.
3. If the raw value is a compound (e.g., "Gravel/Paved") → attempt to
   resolve as "Mixed" only if the source explicitly documents a mixed
   surface. If not explicitly documented → route to **REVIEW**; flag in
   `identity_notes`; leave field blank until resolved.
4. If the raw value is unmappable (e.g., a width descriptor such as
   "singletrack", a governance label, or an ambiguous term) →
   **null-and-log**: leave blank, record the raw value and reason in
   `normalization_provenance`.
5. Empty string ("") → null; see §5.21.

**Common mappings (non-exhaustive — §9.2 is authoritative):**
- "asphalt" / "paved asphalt" → "Paved"
- "concrete" → "Paved"
- "chip-and-seal" → "Paved"
- "crushed limestone" / "crushed stone" → "Crushed Stone"
- "dirt trail" / "natural" / "primitive" / "rustic" / "singletrack" → "Natural Surface"
- "grass" / "mowed grass" → "Turf/Grass"
- "boardwalk" / "wood" → "Boardwalk"
- "gravel" → "Gravel"

---

## 5.5 Trail Origin Type

**Read Trail Vocabulary Module v5.2 §9.3 before applying this step.**

- Optional. Must be explicitly documented — not inferred from alignment, age,
  corridor appearance, or name.
- Single value only — compound values are never valid.
- Leave blank if origin is undocumented.

**Normalization procedure:**

1. Check `trail_origin_type_raw` against the §9.3 mapping table.
2. If the raw value maps to a controlled value → apply the mapping; log.
3. If the raw value is a surface or governance descriptor rather than an
   origin descriptor (e.g., "natural", "wildlife area trail", "county park
   trail") → **null-and-log**: these are not valid origin types; record the
   raw value and reason in `normalization_provenance`.
4. If the raw value is a compound or ambiguous → route to **REVIEW**; flag
   in `identity_notes`.
5. If the raw value is unmappable → **null-and-log**.
6. Empty string ("") → null; see §5.21.

**Common mappings (non-exhaustive — §9.3 is authoritative):**
- "rails-to-trails" / "rail trail" / "rail-trail" → "Rail Trail"
- "towpath" / "canal towpath" / "ohio & erie canal" → "Canal Towpath"
- "power line" / "utility corridor" → "Utility Corridor"
- "purpose-built" / "village-built" / "state-built" → "Purpose-Built"
- "historic route" / "heritage trail" → "Historic Route"
- "water trail" / "paddle trail" → "Water Trail"
- "natural" → null-and-log (surface character, not origin)
- "wildlife area trail" → null-and-log (governance context, not origin)

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

**Read Trail Vocabulary Module v5.2 §9.4 before applying this step.**

- Optional. Describes the operational state of the Trail as a whole — not
  individual segments.
- Single value only.
- "Closed" = permanently closed only.
- "Planned" must be explicitly documented.
- "Gap" applies when a missing portion is the defining characteristic
  of the trail's current state.
- Never infer from imagery or social media.
- Temporary closures → Notes, not Status.

**Normalization procedure:**

1. Check `status_raw` against the §9.4 mapping table.
2. If the raw value maps to a controlled value → apply the mapping; log.
   - "open" / "operational" → "Active"
   - "planned" / "proposed" → "Planned"
   - "closed" → "Closed"
   - "gap" / "incomplete" → "Gap"
3. If the raw value is compound (e.g., "open/partial") → route to
   **REVIEW**; flag in `identity_notes`; leave field blank until resolved.
4. If the raw value is unmappable → **null-and-log**.
5. Empty string ("") → null; see §5.21.

---

## 5.11 Difficulty

**Read Trail Vocabulary Module v5.2 §9.5 before applying this step.**

- Optional — leave blank if not documented by an authoritative source.
- **CRITICAL:** Only populate from explicit authoritative source
  ratings — never assess yourself, never infer from surface type or
  length.
- Single value only — difficulty ranges are never valid.
- When trail-level and segment-level difficulty differ → trail-level
  reflects the overall characterization from the source.

**Normalization procedure:**

1. Check `difficulty_raw` against the §9.5 mapping table.
2. If the raw value maps to a controlled value → apply the mapping; log
   the source URL in `normalization_provenance`.
3. If the raw value is a range or variable descriptor (e.g.,
   "Easy-Moderate", "Easy to Moderate", "Easy to Difficult", "varies",
   "variable") → **null-and-log**: single-value field; document the range
   in Notes for informational purposes.
4. If the raw value is unmappable → **null-and-log**.
5. Empty string ("") → null; see §5.21.

**Common mappings (non-exhaustive — §9.5 is authoritative):**
- "beginner" / "easy" → "Easy"
- "moderate" / "intermediate" → "Moderate"
- "difficult" / "hard" / "advanced" / "challenging" → "Difficult"
- "expert" / "expert only" / "black diamond" → "Expert"
- "varies" / "variable" / "Easy-Moderate" / "Easy to Difficult" → null-and-log

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
- REVIEW flags from normalization (compound values pending resolution)
- Notes added during Resolution or Normalization passes

**Rules:**
- Must not duplicate Notes content
- Must not contain operational or contextual notes (those go in Notes)
- Preserve uncertainty flags — do not resolve silently

---

## 5.16 Notes

- Optional free text.
- Use for: temporary closures, access restrictions, parking notes,
  trailhead details, gap locations, construction updates, difficulty range
  documentation (when null-and-log was applied to difficulty_raw).
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

---

## 5.20 Parent Site — `trail_parents` Population (IMP-054)

After all Trail fields are normalized, apply the containment determination pass:

**Step 1 — Evaluate containment** using the three criteria from Trail Schema Module v5.2 §5.4:
1. The Trail is geographically wholly within one Site's boundary.
2. The Trail's governance aligns with that Site.
3. The Trail's access and legal existence depend on the Site.

**Step 2a — Contained Trail**: If all three criteria hold:
- Insert a row into the `trail_parents` table: `(trail_id, parent_site_id)`.
- Ensure `identity_notes` contains the statement: `Contained within [Site Name] ([site_id]).`
  If `identity_notes` already has the statement, skip. If not, append it.
- Log the containment determination in normalization provenance.

**Step 2b — Extra-limital Trail**: If any containment criterion fails:
- Do not create a `trail_parents` row.
- Governance field documents site associations as free text.
- Do not add "Contained within" to `identity_notes`.
- If the Trail passes through multiple named Sites, each site relationship may be noted
  in `identity_notes` as prose (e.g., "Passes through Battelle Darby Creek Metro Park and
  Prairie Oaks Metro Park") but no formal containment relationship is asserted.

**Source for parent_site_id**: The parent site must be a valid `site_id` in the Entity Graph.
If the containing Site has not yet been upserted, hold the Trail as a Held Entity until the
Site is available, then release and insert the `trail_parents` row on release.

**Error condition**: If a Trail's `identity_notes_raw` contains "Parent site: [Name]" from
discovery but the named Site does not exist in the Entity Graph, flag as a manual review item.

---

## 5.21 Empty String Enforcement (IMP-100)

**Run this step after normalizing all vocabulary-controlled fields and before
the integrity anchor validation step.**

Empty string (`""`) is not a valid blank in any vocabulary-controlled Trail field.
It is a data defect produced when a raw value was present but normalization did not
assign a controlled value. It must not persist into the normalized entity.

**Applies to all five controlled fields:**
- `use_type`
- `surface_type`
- `origin_type`
- `status`
- `difficulty`

**Rule:** For each controlled field, if the value is an empty string after the
field-level normalization step:
1. Convert to null (true blank).
2. Log in `normalization_provenance`: `{field}: empty string converted to null`.
3. Do not route to REVIEW — empty string is a mechanical defect, not an ambiguous
   value. (If the original `_raw` field contained a meaningful value that could not
   be mapped, the null-and-log at the field level already captured it.)

This rule applies regardless of whether the empty string originated from the raw
record, from a failed mapping attempt, or from any intermediate processing step.

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

- All vocabulary-controlled fields map to valid values (per Trail Vocabulary v5.2)
- No vocabulary-controlled field contains an empty string (§5.21)
- Total Length: numeric only, no units
- Counties: alphabetized, semicolon-delimited, "County" stripped
- Maps: each entry is a well-formed https:// URL; no embedded metadata
- Alternate Names: semicolon-delimited, no duplicates, no repeat of
  Trail Name
- Semicolon formatting: trimmed, no empty segments
- No invented data
- Blank fields are true blanks (null, not empty string)
- No delimiter characters inside field values

If any field fails validation:
- Surface as warning or error (per severity)
- Do not silently correct
- Log in normalization provenance

------------------------------------------------------------
# 9. DELIMITER INTEGRITY REQUIREMENTS

Normalization must ensure:

- Blank fields are true blanks (null, not empty string)
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
- If unclear → leave blank (null), flag in identity_notes.

### 10.4 Conflicting Difficulty
- If sources disagree → leave blank (null), log conflict.
- Never average or choose arbitrarily.

### 10.5 Conflicting Status
- Use most recent authoritative documentation.
- Log conflict.

------------------------------------------------------------
# 11. MISSING DATA RULES

- If data is missing and cannot be verified → leave blank (null).
- Never estimate length.
- Never infer use type, surface type, or origin type.
- Never infer difficulty.
- Never infer governance from ownership or vice versa.

------------------------------------------------------------
# 12. AUDITABILITY REQUIREMENTS

Normalization must record in `normalization_provenance`:

- All sources consulted
- All vocabulary mappings applied (field, raw value, mapped value, mapping rule)
- All null-and-log decisions (field, raw value, reason)
- All REVIEW flags issued (field, raw value, reason)
- All empty string → null conversions (§5.21)
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

- **Trail Vocabulary Module v5.2** (§9.x enforcement mapping tables — IMP-100)
- Trail Schema Module v5.x
- Discovery Output Specification v5.x
- Resolution Engine v5.x
- Normalization Engine v5.x
- Entity Upsert Engine v5.x
- Audit & Logging Module v5.x

------------------------------------------------------------
# END OF TRAIL NORMALIZATION CONTRACT v5.3
