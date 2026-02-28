# NATURAL AREAS PROJECT
# SITE NORMALIZATION CONTRACT v5.0
(Authoritative Field-Level Rules for Normalizing Resolved Site Entities)

This module defines the entity-specific normalization rules applied by the
**Normalization Engine v5.0** to produce a fully normalized **Site** entity
conforming to the **Site Schema Module v5.0** and ready for insertion into the
**Entity Graph Schema v5.0**.

This contract contains no controlled vocabularies.
All vocabularies are defined in the **Site Vocabulary Module v5.0**.

This contract is authoritative for Site normalization only.

------------------------------------------------------------
# CHANGES FROM v4.0

- **`address` → `location`**: Universal geographic reference field — accepts full address OR general geographic description
- **`gps_primary` → `gps_lat` + `gps_lon`**: GPS parsing is handled by Normalization Engine v5.0; this contract validates the result
- **`municipality` and `township`**: Now GIS-derived by Normalization Engine v5.0 — this contract does NOT normalize from raw discovery values
- **`county_list` → `counties`**: Renamed; alphabetized array
- **`network_affiliation` removed**: No longer a field; network membership tracked via relationship tables
- **`url_all` → `urls`**: Array of additional URLs
- **`source_primary`, `source_all` removed**: Tracked in provenance tables only
- **`coordination` replaces `Coordination`**: Field name aligned with schema
- Updated all version references to v5.0

------------------------------------------------------------
# 1. PURPOSE

The Site Normalization Contract v5.0 defines:

- How a Resolved Site is transformed into a Normalized Site
- How each Site Schema v5.0 field is validated and normalized
- How Category, Subtype, Designation, Status, and Features are normalized
- How parent-child relationships are validated using the **Child Site Rules Module v5.0**
- How GPS, Plus Code, Location, and jurisdiction fields are handled
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
- resolved entity_type = "Site"
- resolved parent_site (if any)
- resolved county set
- resolved governance, ownership, coordination, category, subtype
- resolved conflicts and uncertainties

## 2.2 Raw Discovery Record v5.0
Including:

- name_raw
- counties_raw
- ownership_raw
- gps_raw (string "lat,lon" — parsed by Normalization Engine)
- location_raw (address or geographic description)
- url_primary, url_all_raw
- parent_site_raw
- notes_raw
- description_raw
- features_raw
- discovery_tier, discovered_in_tiers
- seeded_from_baseline, baseline_id
- discovery_metadata
- source_map

**Not in raw discovery (GIS-derived):**
- township — populated by Normalization Engine via GIS spatial lookup
- municipality — populated by Normalization Engine via GIS spatial lookup

## 2.3 Normalization Engine Outputs (Pre-Populated)
Before this contract runs, the Normalization Engine v5.0 has already:

- Parsed gps_raw → gps_lat, gps_lon (numeric)
- Computed plus_code from gps_lat / gps_lon
- Derived township via GIS spatial lookup
- Derived municipality via GIS spatial lookup

This contract validates those results but does not recompute them.

## 2.4 Vocabulary Modules v5.0
- Site Vocabulary Module v5.0 (Category, Subtype, Designation, Status, Features)

## 2.5 Schema Modules v5.0
- Site Schema Module v5.0
- Child Site Rules Module v5.0

------------------------------------------------------------
# 3. OUTPUTS

Normalization produces:

- A **Normalized Site Object v5.0** conforming to the Site Schema Module v5.0
- A **Normalization Provenance Record**
- A **Validation Result Object** (warnings, errors)
- A normalized entity ready for the **Entity Upsert Engine v5.0**

No new information may be invented.

------------------------------------------------------------
# 4. NORMALIZATION WORKFLOW (HIGH-LEVEL)

1. Receive Resolved Site from Normalization Engine v5.0
2. Validate identity and entity_type = "Site"
3. Normalize name
4. Normalize Category, Subtype, Designation, Status
5. Normalize Ownership, Governance, Coordination
6. Normalize Counties
7. Validate GPS (gps_lat / gps_lon) — pre-populated by engine
8. Validate Plus Code — pre-populated by engine
9. Validate Township, Municipality — pre-populated by GIS lookup
10. Normalize Location (address / geographic description)
11. Normalize Acres
12. Normalize Features
13. Normalize Description
14. Normalize Notes
15. Normalize URLs
16. Validate Parent Site relationship (Child Site Rules v5.0)
17. Run integrity anchor deduplication check (via Normalization Engine)
18. Validate against Site Schema v5.0
19. Emit Normalized Site + provenance

If any critical step fails → return error to Normalization Engine v5.0.

------------------------------------------------------------
# 5. FIELD-BY-FIELD NORMALIZATION RULES

## 5.1 Name

- Use `name_raw` with minimal whitespace cleanup only.
- If multiple authoritative names exist → Resolution Engine v5.0 chooses; use resolved name.
- Former names and alternate names → append to Description, not to Name.
- Never infer names from amenities, features, or nearby entities.
- Never derive names from Category, Subtype, or Designation.

**Provenance:** Log all name conflicts and any corrections applied.

---

## 5.2 Category

- Must match a controlled value from Site Vocabulary Module v5.0.
- One value only — choose the most specific that applies.
- Never infer from amenities, features, or trail presence.
- Never infer from governance or ownership alone.
- If ambiguous → leave blank and log uncertainty.

**Common errors to catch:**
- "Natural Area" assigned to a formally designated Nature Preserve → correct to "Nature Preserve"
- "Park" assigned based on name alone without source documentation → flag for review

---

## 5.3 Subtype

- Optional.
- Must match subtype list for the chosen Category from Site Vocabulary Module v5.0.
- Must not describe habitat conditions or temporary states.
- Must not be applied from the wrong Category's list.
- Leave blank if no subtype clearly applies.

---

## 5.4 Designation

- Must match vocabulary values from Site Vocabulary Module v5.0.
- Semicolon-delimit if multiple.
- Never infer from site character, name, or category alone.
- "None" used only when source explicitly confirms no formal designation.
- Leave blank if designation status is unknown or undocumented.

---

## 5.5 Status

- Must match vocabulary values from Site Vocabulary Module v5.0.
- "Closed" = permanently closed only.
- "Proposed" must be explicitly documented in authoritative sources.
- Never infer from imagery, social media, or lack of web presence.
- Temporary closures → Notes, not Status.
- Seasonal closures → use "Seasonal" status + note season details in Notes.

---

## 5.6 Ownership

- Must contain the **actual legal name** of the owning entity.
- Must not use generic categories (e.g., "State Government", "Municipal Agency", "Nonprofit").
- Must not encode management, governance, designation, or temporary conditions.
- Must not be inferred from signage alone.
- If ownership cannot be verified from authoritative sources → leave blank.

**Examples:**
- ✅ "Ohio Department of Natural Resources"
- ✅ "Wood County Park District"
- ✅ "Maumee Valley Land Trust"
- ❌ "State Agency" — too generic
- ❌ "Local Government" — too generic

**Provenance:** Log all ownership decisions.

---

## 5.7 Governance

- Must contain the **actual name(s)** of the operational managing organization(s).
- Semicolon-delimit if multiple managers are formally documented.
- Must not use generic categories (e.g., "County Agency", "Nonprofit Organization").
- Must not encode ownership, designation, or access rules.
- If governance is identical to ownership → repeat explicitly (do not leave blank).
- Leave blank if unverifiable.

**Examples:**
- ✅ "Wood County Park District"
- ✅ "Ohio Department of Natural Resources;Metroparks Toledo"
- ❌ "County Parks" — too generic

**Provenance:** Log all governance decisions.

---

## 5.8 Coordination

- Must contain the **actual names** of formally documented partner organizations.
- Must not use generic categories.
- Must not duplicate Ownership or Governance.
- Must not encode temporary volunteer activity or informal relationships.
- Leave blank if no documented coordination exists.

---

## 5.9 Description

- 1-3 sentences.
- Must describe identity-defining ecological, historical, cultural, or physical character.
- Include naming history and former names when documented.
- Must not include governance, ownership, amenities, or temporary conditions.
- Must not contradict controlled fields (Category, Designation, Status).
- Must not be copied verbatim from source — paraphrase or synthesize.

---

## 5.10 Location ✨ UPDATED FROM v4.0 (was `address`)

The `location` field is a **universal geographic reference** — it accepts:

**Option A — Full street address (preferred when available):**
- "18331 Carter Road, Bowling Green, OH 43402"
- "350 West Poe Road, Bowling Green, OH"

**Option B — General geographic description (when no street address exists):**
- "East shore of Metzger Marsh, north of State Route 2"
- "Mile marker 47 on State Route 6"
- "North end of Carter Road, south of the Portage River"

**Rules:**
- Never invent street numbers
- Do not USPS-normalize addresses
- Do not include county names
- Do not encode governance or access rules
- Leave blank if no authoritative or defensible location reference exists

---

## 5.11 Acres

- Numeric only — no units, no ranges, no approximation symbols.
- Never estimate.
- Never average conflicting acreage values — use most authoritative source.
- If sources conflict and cannot be resolved → log conflict, use highest-authority source.
- Leave blank if unknown.

---

## 5.12 Counties ✨ RENAMED FROM v4.0 (was `county_list`)

- Required.
- Must match official Ohio county names.
- Alphabetized.
- Semicolon-delimited.
- Omit the word "County" (e.g., "Wood County" → "Wood").
- Multi-county Sites produce one normalized entity — not one per county.

---

## 5.13 Municipality ✨ GIS-DERIVED IN v5.0

**DO NOT normalize from raw discovery values.**

- Populated by Normalization Engine v5.0 via GIS spatial lookup
- This contract validates that the field is either:
  - A recognized municipality name (city or village), or
  - Blank (site is outside any municipality boundary)
- Never copy `municipality_raw` from discovery records — that field is informational only

---

## 5.14 Township ✨ GIS-DERIVED IN v5.0

**DO NOT normalize from raw discovery values.**

- Populated by Normalization Engine v5.0 via GIS spatial lookup
- This contract validates that the field is either:
  - A recognized civil township name (without "Township" appended), or
  - Blank (GIS lookup failed or GPS unavailable)
- Never copy `township_raw` from discovery records — that field is informational only

---

## 5.15 GPS (gps_lat / gps_lon) ✨ UPDATED FROM v4.0

**GPS parsing is handled by the Normalization Engine v5.0.**
This contract validates the result:

- Both gps_lat and gps_lon must be present, or both must be blank
- gps_lat must be in range [-90, 90]
- gps_lon must be in range [-180, 180]
- Both must be numeric (float)
- Must represent an authoritative coordinate — no placeholders, no centroids, no inferred locations
- If validation fails → log error, blank both fields

---

## 5.16 Plus Code ✨ UPDATED FROM v4.0

**Plus Code computation is handled by the Normalization Engine v5.0.**
This contract validates:

- If gps_lat and gps_lon are present → plus_code must be present and well-formed
- If GPS is blank → plus_code must be blank
- Never manually enter a Plus Code

---

## 5.17 Features

- Semicolon-delimited flat list.
- Must match vocabulary values from Site Vocabulary Module v5.0.
- Metadata in parentheses is permitted: "restrooms (ADA accessible)", "picnic tables (6)"
- Features describe internal components only.
- Trails, Trail Segments, Access Points, and child Sites are **never** Features.
- Named trails → child Trail entity, not a Feature.
- Minor connectors → Notes, not Features.
- Do not add features not documented in authoritative sources.

---

## 5.18 Notes

- Optional free text.
- Use for: temporary closures, access restrictions, historical context, boundary notes, parcel IDs, citations, clarifications.
- Must not include identity-defining ecological, cultural, or historical character (that belongs in Description).
- Must not include internal features (those belong in Features).
- Must not contradict controlled fields.

---

## 5.19 URLs ✨ UPDATED FROM v4.0

**`url_primary`:**
- Full https:// URL to primary authoritative source.
- Single value only.
- Must be a stable, authoritative URL.

**`urls` (replaces `url_all`):**
- Array of additional URLs beyond url_primary.
- Semicolon-delimited in TSV output.
- May include non-official sources of documentation value.
- Remove duplicates.
- Full https:// URLs only.

**Removed in v5.0:** `source_primary`, `source_all` — these are tracked in provenance tables, not in the entity record.

---

## 5.20 Parent Site

- Leave blank for top-level Sites.
- Must reference a normalized parent Site ID (not a name string).
- A Site may have only one parent.
- Parent-child relationships must be explicit in authoritative sources.
- Must not be inferred from signage, geography, or layout.
- Must follow **Child Site Rules Module v5.0**.
- Parent Site must exist in Entity Graph before child is upserted.

---

## 5.21 Network Affiliation ✨ REMOVED IN v5.0

- `network_affiliation` is no longer a field in the Site schema.
- Network membership is tracked via the `site_to_network` relationship table.
- If network affiliation values are present in resolved records from older discovery runs → silently drop.
- Do not migrate network affiliation values to any other field.

------------------------------------------------------------
# 6. IDENTITY ANCHOR VALIDATION

The integrity anchor for Sites is:

**Top-level Sites:** `entity_type` + `name` + `counties`
**Child Sites:** `entity_type` + `name` + `counties` + `parent_site_id`

This contract must verify:
- All anchor fields are present and non-blank
- `counties` is a valid, alphabetized list
- `parent_site_id` (if present) references a valid entity

The Normalization Engine v5.0 runs the deduplication check after this validation.

------------------------------------------------------------
# 7. VALIDATION LOGIC

Normalization must validate:

- All vocabulary-controlled fields map to valid values
- GPS: both gps_lat and gps_lon present, or both blank; values in valid range
- Plus Code: present if GPS present, blank if GPS blank
- Acres: numeric only, no units
- Semicolon formatting: trimmed, no empty segments, alphabetized where required
- Field types match schema
- No invented data
- Blank fields are true blanks (no placeholders, no "N/A", no "Unknown")
- No delimiter characters inside field values
- Parent Site validity (if populated)
- Identity anchor completeness

If any field fails validation:
- Surface the issue as warning or error (per severity)
- Do not silently correct
- Log in normalization provenance

------------------------------------------------------------
# 8. DELIMITER INTEGRITY REQUIREMENTS

Normalization must ensure:

- Blank fields are true blanks
- No spaces between semicolons and values
- No trailing spaces or newlines within fields
- No collapsed delimiters (consecutive semicolons)
- No missing delimiters in multi-value fields

All anomalies must be logged.

------------------------------------------------------------
# 9. CONFLICT HANDLING

### 9.1 Conflicting Names
- Use the most authoritative source.
- Record alternates in Description or Notes.
- Log conflict in normalization provenance.

### 9.2 Conflicting Ownership
- Flag as conflict — never infer or choose without authoritative support.
- Log and surface for review.

### 9.3 Conflicting Acreage
- Use the most authoritative source (ODNR, county auditor, etc.).
- If conflict persists → log, use highest-authority value, flag for review.

### 9.4 Conflicting Category
- Flag as conflict.
- Leave blank rather than guess.
- Log and surface for review.

------------------------------------------------------------
# 10. MISSING DATA RULES

- If data is missing and cannot be verified → leave blank.
- Never estimate acres.
- Never infer ownership, designation, or category.
- Never generate GPS without authoritative source.
- Never copy municipality or township from discovery records.
- Never add features not in authoritative sources.

------------------------------------------------------------
# 11. AUDITABILITY REQUIREMENTS

Normalization must record in `normalization_provenance`:

- All sources consulted
- All vocabulary mappings applied
- All conflicts detected and how handled
- All fields left blank and why
- All GPS parsing results
- All GIS derivation results (township, municipality)
- All delimiter-integrity corrections
- Identity anchor validation result
- Deduplication check result

Never overwrite previously logged normalization decisions.

------------------------------------------------------------
# 12. MODULE DEPENDENCIES

This contract depends on:

- Site Vocabulary Module v5.0
- Site Schema Module v5.0
- Child Site Rules Module v5.0
- Discovery Output Specification v5.0
- Resolution Engine v5.0
- Normalization Engine v5.0
- Entity Graph Schema v5.0
- Audit & Logging Module v5.0

------------------------------------------------------------
# END OF SITE NORMALIZATION CONTRACT v5.0
