# NATURAL AREAS PROJECT
# SITE NORMALIZATION CONTRACT v6.0
(Authoritative Field-Level Rules for Normalizing Resolved Site Entities)

This module defines the entity-specific normalization rules applied by the
Normalization Engine v6.0 to produce a fully normalized Site entity conforming
to the Site Schema Module v6.0 and ready for insertion into the Entity Graph.

This contract contains no controlled vocabularies.
All vocabularies are defined in the Site Vocabulary Module v6.0.

This contract is authoritative for Site normalization only.

This module supersedes Site Normalization Contract v5.11.

------------------------------------------------------------
# CHANGES FROM v5.11 → v6.0

- **Four new fields added** (IMP-011, IMP-012, IMP-013): Normalization rules added
  for habitat_type (§5.22), access_notes (§5.23), last_verified_date (§5.24), and
  field_verified (§5.25). Raw inputs and outputs updated accordingly.

- **IMP-014 — Notes provenance prohibition added to §5.19**: Notes field is
  customer-facing. Pipeline source references, IMP numbers, and process content
  must not appear. Strengthened language added alongside existing IMP-053/IMP-061
  content stripping rules.

- **IMP-015 — Description ecological/physical character priority added to §5.10**:
  When description content could serve either ecological/physical identity or
  administrative context, ecological/physical character takes priority. Administrative
  descriptions of governance or ownership structure are not valid description content.

- **All v5.11 rules carried forward**: IMP-063 (Category enforcement), IMP-064
  (Subtype enforcement), IMP-065 (Subtype inference), IMP-066 (Municipality GIS
  derivation), IMP-067 (GPS county check), IMP-069 (GPS gate), IMP-049/050/051/116
  (Features normalization sequence), IMP-052/059/060/061 (Description rules),
  IMP-053 (Notes metadata stripping), IMP-054 (CRP Parkland suffix), IMP-055
  (Municipality/Township blocklist).

------------------------------------------------------------
# 1. PURPOSE

The Site Normalization Contract v6.0 defines:

- How a Resolved Site is transformed into a Normalized Site
- How each Site Schema v6.0 field is validated and normalized
- How Category, Subtype, Designation, Status, and Features are normalized
- How organizational fields (ownership, governance, partner_agencies, coordination)
  are separated
- How the four new fields (habitat_type, access_notes, last_verified_date,
  field_verified) are normalized
- How parent-child relationships are validated
- How GPS, Plus Code, Location, and jurisdiction fields are handled
- How normalization interacts with the Normalization Engine v6.0
- How provenance, conflicts, and uncertainties are recorded
- How normalized entities integrate with the Entity Upsert Engine v6.x

Normalization must:

- Never invent data
- Never infer governance, ownership, partner agencies, or identity
- Never silently correct malformed values
- Always log normalization decisions

------------------------------------------------------------
# 2. INPUTS

## 2.1 Resolved Entity Object
From Resolution Engine v6.x, including:

- resolved identity key
- resolved entity_type = "Site"
- resolved parent_site_id (if any)
- resolved county set
- resolved governance, ownership, partner_agencies, coordination
- resolved category, subtype, designation, status
- resolved conflicts and uncertainties

## 2.2 Raw Discovery Record v6.0
Including:

- name_raw
- counties_raw
- ownership_raw
- governance_raw
- partner_agencies_raw (optional; may be absent)
- coordination_raw
- gps_lat_raw
- gps_lon_raw
- location_raw
- url_primary_raw
- urls_raw
- parent_site_raw
- identity_notes_raw
- description_raw
- features_raw
- habitat_type_raw *(new in v6.0)*
- access_notes_raw *(new in v6.0)*
- last_verified_date *(new in v6.0 — populated at discovery with today's date)*
- field_verified *(new in v6.0 — always false at discovery)*
- ebird_hotspot_id *(new in v6.0 — optional; Sites only)*
- discovery_metadata

Not in raw discovery (GIS-derived):
- municipality
- township

## 2.3 Normalization Engine Pre-Populated Fields
Before this contract runs, the Normalization Engine v6.0 has already:

- Validated gps_lat and gps_lon from gps_lat_raw / gps_lon_raw
- Computed plus_code
- Derived township via GIS spatial lookup
- Derived municipality via GIS spatial lookup

## 2.4 Vocabulary Modules v6.0
- Category, Subtype, Designation, Status, Features
- Habitat Type: open vocabulary — no vocabulary module governs this field

## 2.5 Schema Modules v6.0
- Site Schema Module v6.0
- Child Site Rules per Site Discovery Sub-Procedure v6.0

------------------------------------------------------------
# 3. OUTPUTS

Normalization produces:

- A Normalized Site Object v6.0 conforming to the Site Schema Module v6.0
- A Normalization Provenance Record
- A Validation Result Object (warnings, errors)
- A normalized entity ready for the Entity Upsert Engine v6.x

No new information may be invented.

------------------------------------------------------------
# 4. NORMALIZATION WORKFLOW (HIGH-LEVEL)

1.  Receive Resolved Site
2.  Validate identity and entity_type = "Site"
3.  Normalize Name
4.  Normalize Category — vocabulary enforcement (§5.2)
4a. Apply cultural institution name-pattern check (§5.2)
5.  Normalize Subtype — vocabulary enforcement (§5.3)
5a. Apply deterministic subtype inference if blank (§5.3a)
6.  Normalize Designation, Status
7.  Normalize organizational fields:
    ownership → governance → partner_agencies → coordination
8.  Normalize Counties
9.  Validate GPS (gps_lat / gps_lon)
10. Validate Plus Code
11. Derive Township, Municipality from GPS via GIS lookup (§5.14, §5.15)
12. **GPS Gate** — hold if GPS null and no gps_unresolvable flag (§5.17a)
12a. **GPS County Check** — flag county mismatch for manual review (§5.17b)
13. Normalize Location
14. Normalize Acres
15. Normalize Features (four-step sequence + unmapped token log)
16. Normalize Description (redundancy stripping + formula detection)
17. Normalize Habitat Type (§5.22)
18. Normalize Access Notes (§5.23)
19. Normalize Notes (metadata stripping + provenance prohibition)
20. Normalize URLs
21. Normalize Last Verified Date (§5.24)
22. Normalize Field Verified (§5.25)
23. Validate Parent Site relationship
24. Run identity anchor deduplication check
25. Validate against Site Schema v6.0
26. Emit Normalized Site + provenance

------------------------------------------------------------
# 5. FIELD-BY-FIELD NORMALIZATION RULES

## 5.1 Name
- Use resolved name or name_raw with minimal whitespace cleanup.
- Never infer from amenities or nearby entities.
- Alternate names → Description or Notes.
- **Columbus CRP "Parkland" suffix normalization**: If name_raw ends with the word
  "Parkland" (case-insensitive, whole-word match), replace trailing "Parkland" with
  "Park" to produce the normalized name. Raw name preserved in name_raw.

## 5.2 Category (IMP-063)

**Vocabulary enforcement**: Every `category` value must match one of the allowed
values in Site Vocabulary Module v6.0 §2.1. Apply in this order:

1. **Case normalization**: convert to title case, trim whitespace.
2. **Exact match check**: if the value matches an allowed value exactly → accept.
3. **Mapping table**: if no exact match, apply Site Vocabulary Module v6.0 §7.1
   mapping table.
   - Unambiguous mappings → apply and log.
   - Context-dependent mappings → flag for **REVIEW**; do not auto-resolve.
4. **No match, no mapping**: → **FATAL REJECT**.
   Log: `"Category '[value]' has no vocabulary mapping. Entity held for manual
   category assignment."`
5. **Blank category**: allowed only when source documents provide no classification.
   Log as WARNING.

**Cultural institution name-pattern check (IMP-068)**: After category is set,
compare the normalized site name against Site Vocabulary Module v6.0 §7.2 pattern
table. If category is "Recreation Facility" but name matches a cultural institution
pattern → flag as **CATEGORY MISMATCH** review item. Do NOT auto-correct.

## 5.3 Subtype (IMP-064)

**Vocabulary enforcement**: Every non-blank `subtype` value must appear in the
category-specific list in Site Vocabulary Module v6.0 §3.2. Apply in this order:

1. **Category-specific list check**: if the subtype appears in the list for the
   entity's category → accept.
2. **Mapping table**: if not in the category list, apply Site Vocabulary Module
   v6.0 §7.3 mapping table.
   - Ecological descriptors misplaced in Nature Preserve subtype → null the
     `subtype` field; append ecological character to `description` if not present.
   - Features vocabulary terms misplaced in Recreation Facility subtype → null
     `subtype`; ensure Features vocabulary equivalent appears in `features`.
   - Other mapped values → apply and log.
   - Unmappable values → **null** the subtype (do not reject; log WARNING).
3. **Wrong-category subtype**: valid value but wrong category → flag for **REVIEW**.

## 5.3a Deterministic Subtype Inference (IMP-065)

Applied **after** §5.3 vocabulary enforcement, **only when `subtype` is still blank**.
Apply inference rules from Site Vocabulary Module v6.0 §7.4. Record inference in
normalization provenance as `subtype_source = "name_inference"` or
`"description_inference"`. If no rule matches → leave `subtype` blank.

## 5.4 Designation
- Must match vocabulary.
- Semicolon-delimited.
- Never infer from name or category.

## 5.5 Status
- Must match vocabulary.
- "Closed" = permanently closed.
- "Proposed" must be explicitly documented.

## 5.6 Ownership
- Must contain the exact legal name of the owning entity.
- Must not use generic categories.
- Must not encode governance or partner roles.
- Leave blank if unverifiable.

## 5.7 Governance
- Must contain exact names of managing organizations.
- Semicolon-delimited if multiple.
- Must not encode ownership or partner roles.
- If governance = ownership → repeat explicitly.

## 5.8 Partner Agencies
- Formal, documented co-operator organizations.
- Must use exact organization names.
- Must not duplicate Ownership or Governance.
- Must not include informal volunteer groups.
- Must be supported by authoritative documentation.
- Leave blank if no formal partners exist.

## 5.9 Coordination
- Community-based, volunteer, advisory, or informal partners.
- Must not duplicate Ownership, Governance, or Partner Agencies.
- Must not use generic categories.
- Leave blank if no documented coordination exists.

## 5.10 Description

**Priority (IMP-015)**: Description must capture ecological, physical, or cultural
character of the site — not administrative or governance structure. When
description_raw contains both ecological/physical content and administrative content
(who manages it, what programs it hosts, what designation it holds), extract and
retain the ecological/physical content and discard the administrative.

- 1–3 sentences.
- Identity-defining ecological, physical, historical, or cultural character.
- Must not include governance, ownership, or amenities.
- Must not contradict controlled fields.

**REDUNDANCY DETECTION AND STRIPPING (IMP-052)**: Before writing to `description`,
apply the following stripping pass to `description_raw`:

1. Detect prohibited openers (case-insensitive):
   - `A [N]-acre [category word] ...` — strip the entire opener clause
   - `Located in [place] ...` — strip if nothing substantive follows
   - `[Site name] is a [category] ...` — strip if remainder is only location/governance
   - `A [N]-acre [category] located in [place] ...` — strip the entire combined opener

2. After stripping the opener, evaluate the remainder:
   - Contains identity-defining content (ecology, history, physical character,
     named natural features, cultural significance) → write to `description`
   - Only location, governance, acreage, or category restatement remains → blank
     `description`

3. If `description_raw` consists entirely of prohibited opener patterns with no
   substantive remainder, write blank to `description`. A blank description is the
   correct normalization outcome when the source offers no distinctive identity content.

**FORMULA DESCRIPTION DETECTION (IMP-059)**: REJECT and blank on these patterns:
- `"[digits]-acre [type] in the [name] community."` — CRP database formula
- `"[Name] is a [X]-acre [type] in the [name] community."` — CRP full formula
- `"[type] in the [name] community."` — CRP formula fragment
- `"[Name] has [X] acres of parkland."` — acreage restatement only
- `"The site is part of the [governance entity] natural areas network."` — governance self-reference
- `"of [type] in the [name] community."` — CRP fragment

For formula descriptions that also contain non-formula sentences (trail access,
named natural features, historical notes) → strip only the formula sentence; retain
remainder if ≥ 20 characters.

**ACQUISITION/ESTABLISHMENT YEAR HANDLING**: If `description_raw` begins with
`"Acquired in [YYYY]"` or `"Established in [YYYY]"`, extract the date note and
append to `notes` as `"Acquired in [YYYY]."` or `"Established in [YYYY]."`.
Strip the acquisition clause from description; evaluate remainder per IMP-052.

**ACREAGE IN DESCRIPTION WARNING**: If description contains an acreage figure that
differs from the `acres` field by more than 10%, log WARNING. Do not reject; do not
use description acreage to update the acres field.

Fields that must never appear in `description`: governance, ownership, acreage
(unless contextually embedded in identity content), hours, permits, amenity lists,
administrative community or district names with no geographic bearing on the site.

## 5.11 Location
- Full address OR general geographic description.
- Never invent street numbers.
- Must not include county names.
- Must not encode governance or access rules.

## 5.12 Acres
- Numeric only.
- Never estimate or average.
- Use most authoritative source.
- **Source documentation (IMP-060)**: When `acres` is populated, record the source
  in normalization provenance. Do not use acreage from `description_raw` to populate
  this field. If the only available acreage is from description text → leave `acres`
  blank and log.

## 5.13 Counties
- Required.
- Alphabetized.
- Semicolon-delimited.
- Must omit the word "County."
- Multi-county Sites remain single entities.

## 5.14 Municipality (GIS-derived, IMP-066)

Must be derived from GPS coordinates using
`na_township_lookup.OhioTownshipLookup.get_both(lat, lon)`. This method returns a
`(township_name, municipality_name)` tuple:

- `township_name` is None and `municipality_name` is not None → GPS point falls
  within an incorporated city or village. Populate `municipality = municipality_name`.
  Leave `township` blank.
- `township_name` is not None → GPS point falls within an unincorporated civil
  township. Populate `township = "[township_name] Township"`. Leave `municipality`
  blank.
- GPS null → leave both `municipality` and `township` blank.
- GIS lookup fails → leave blank; log WARNING.

Never populated from discovery fields, source text, or address parsing.

**REJECT with FATAL error if municipality contains:**
- Any governance vocabulary value, agency abbreviation, or management entity name
- Any value ending in "Township" or "Twp"
- Bare type labels: "Township", "County", "District", "Division", "Authority",
  "Commission", "Reservation", "Preserve", "Area", "Wildlife", "Nature"
- Any value matching Ownership or Governance fields of the same entity

**Cross-field contamination check:** if municipality == township for the same entity
→ REJECT both.

## 5.15 Township (GIS-derived)
- Must be GIS-derived from GPS coordinates via spatial lookup. Never populated from
  discovery fields, source text, or any other pipeline stage.
- Valid form: "[Name] Township".
- Leave blank if GPS is null, GPS falls outside Ohio, or GIS lookup fails.

**REJECT with FATAL error if township contains:**
- Any governance vocabulary value or agency abbreviation
- A bare type label without a name: "Township", "Twp", "County"
- Any value matching the Municipality field of the same entity

**Normalization:** if township raw value is "[Name] Twp" → expand to
"[Name] Township".

## 5.16 GPS (gps_lat / gps_lon)
- Both present or both blank.
- Must be numeric.
- Must be authoritative.
- If invalid → blank both fields.

## 5.17 Plus Code
- Must be present if GPS present.
- Must be blank if GPS blank.
- Never manually entered.

## 5.17a GPS Gate — Pre-Output Hold (IMP-069)

No Site entity may proceed to TSV Output or Database Upsert unless one of the
following is true:

**A. GPS is confirmed**: both `gps_lat` and `gps_lon` are non-null, valid numerics.

**B. GPS is explicitly flagged unresolvable**: `gps_unresolvable = true`, accompanied
by a `notes` entry explaining why GPS cannot be obtained.

**If neither condition is met**: route entity to `held_entities` with
`hold_reason = "gps_missing"`. Entity will be released when GPS is acquired.

## 5.17b GPS County Check — County Mismatch Flag (IMP-067)

Runs after §5.17a, only when GPS is confirmed (gps_confidence HIGH or MED).

Cross-check the entity's `counties` field against the county derived from a
point-in-polygon lookup on GPS coordinates using TIGER COUSUB COUNTYFP data.

**On mismatch:**
- Route entity to `manual_review_queue` with `flag = "county_mismatch"`.
- Entity **continues through the pipeline** with its current `counties` value unchanged.

**Do not run when** `gps_confidence` is LOW or NONE, or when GPS is null.

## 5.18 Features

**FEATURES NORMALIZATION SEQUENCE (IMP-049, IMP-050, IMP-051, IMP-116):**

Apply in this order to each token in `features_raw`:

**Step 1 — Activity detection (IMP-049)**: Map pure activity terms to physical
infrastructure vocabulary terms where documented, or drop. See Site Normalization
Contract v5.11 §5.18 Step 1 for full activity mapping table (carries forward
unchanged).

**Step 2 — Operational content stripping (IMP-050)**: Strip tokens or annotations
representing hours, parking, policies, permit requirements, seasonal closures, events,
or facility sub-detail. Physical feature terms that carry operational annotations are
retained with the annotation stripped.

**Step 3 — Named entity detection (IMP-051)**: Drop tokens that name a specific
Trail, Access Point, or child Site entity. Generic infrastructure references pass
through.

**Step 4 — Vocabulary mapping**: Map remaining tokens to vocabulary terms per Site
Vocabulary Module v6.0 §6.2. Alphabetize; semicolon-delimit.

**Step 5 — Unmapped token logging (IMP-116)**: For every token dropped in Step 4
(no vocabulary match, not eliminated by Steps 1–3), write a provenance record:
`action: "unmapped_token_dropped"`. These accumulate as vocabulary expansion
candidates surfaced at Stage 5 TSV Integrity Check.

## 5.19 Notes

**Core principle (IMP-061)**: The `notes` field is a content field — the primary
home for substantive contextual information. When in doubt, retain the note.

**CUSTOMER-FACING SCOPE (IMP-014)**: Notes is a customer-facing field. Pipeline
source references, IMP numbers, session identifiers, and process-related content
must not appear. Strip these during normalization; do not carry them into output.

- Free text; semicolon-delimited when listing multiple distinct notes.
- Must not contradict controlled fields.
- Use for: source citations, GPS approximation warnings with location context,
  address conflicts, identity ambiguities, external system cross-references,
  acquisition and establishment history, operational restrictions, cross-entity
  relationships.

**PIPELINE METADATA CLEANSING (IMP-053)**: Strip only narrow, meaningless
machine-generated scaffolding artifacts — not substantive content.

Strip the following patterns (case-insensitive):
- Session references: `Session N:`, `Session N.`, `Session N` (trailing),
  `Manually assigned Session N`
- Bare IMP references: `(IMP-NNN)`, `(IMP-NNN: description)`, `; IMP-NNN` —
  strip only when the IMP reference is the entire note or an isolated
  parenthetical; do not strip when IMP context is woven into explanatory text
- OBJECTID annotations: `(OBJECTID NNN)`, `OBJECTID NNN,`
- Bare GPS placeholders: `GPS pending verification.` — strip ONLY this exact
  placeholder; do not strip GPS approximation notes with substantive location
  context
- Discovery run labels: `Cataloged during [County] County run.`
- Pipeline staging notes: `staged in [file] YAML`, `staged not pipelined`
- Browser retry annotations: `([date] browser retry)`, `(browser JS extraction, [date])`

**Preserve the following** (substantive content, never pipeline scaffolding):
- `Source: [source].` lines
- GPS approximation notes with location detail
- External system identifiers (MORPC ParkID, ODNR ID, etc.)
- Operational notes: hours, closures, permit requirements, contact information
- Identity notes written in plain prose
- Cross-entity references
- Acquisition and establishment history
- Funding and grant notes
- Verification flags
- **Alternate names** (IMP-029): `ALT NAME: '[name]' — [source context]` — any name used
  by an authoritative source that differs from the canonical `name` field. Always preserve;
  never discard known alternate names.

After stripping, clean up residual punctuation artifacts. If stripping would leave
nothing → write NULL.

## 5.20 URLs

`url_primary`:
- Single authoritative URL; full https://; stable and authoritative.

`urls`:
- Semicolon-delimited list of additional URLs from `urls_raw`.
- Remove duplicates. Full https:// URLs only.

## 5.21 Parent Site
- Blank for top-level Sites.
- Must reference a valid parent_site_id.
- Must not be inferred from signage or layout.

## 5.22 Habitat Type (IMP-011) *(new in v6.0)*

**Open vocabulary — no controlled value mapping.** This is a free-text field
capturing the ecological character of the site.

**Normalization rules:**

- Pass through `habitat_type_raw` with minimal cleanup: trim whitespace, normalize
  line endings, clean up leading/trailing punctuation.
- Never map to a controlled vocabulary.
- Never infer habitat type from features, description, or site name.
- Never populate from non-authoritative sources (i.e., only populate if explicitly
  stated in the source).
- Leave blank if no habitat type description was captured at discovery.
- Must not duplicate `description`. If `habitat_type_raw` is identical to or a
  substring of `description_raw`, log WARNING and blank `habitat_type` — the
  description field is the correct home for that content.

**Examples of valid habitat_type values:**
- "Oak savanna and open woodland"
- "Wet prairie, sedge meadow, and marsh"
- "Forested ravine with intermittent stream"

**Invalid patterns (blank and log):**
- Category or designation labels ("Nature Preserve", "ODNR Wildlife Area") — these
  belong in `category` or `designation`
- Amenity or feature lists ("Trails, picnic areas") — these belong in `features`
- Governance content ("Managed by ODNR") — this belongs in `governance`

**Provenance:** Record whether `habitat_type` was populated from `habitat_type_raw`
or left blank, and reason.

## 5.23 Access Notes (IMP-012) *(new in v6.0)*

**Free-text field** capturing seasonal access conditions, public access caveats,
permit requirements, or access restrictions that affect visitor planning.

**Normalization rules:**

- Pass through `access_notes_raw` with minimal cleanup: trim whitespace, normalize
  line endings, clean up leading/trailing punctuation.
- Never infer access conditions from governance, designation, or category alone.
- Leave blank if no access conditions were documented at discovery.
- Must not duplicate `notes`. If `access_notes_raw` content belongs in `notes`
  (operational details, contact information, closures) and not in `access_notes`
  (public access caveats specific to visiting the site), log WARNING and route to
  `notes` instead.

**Valid access_notes content:**
- Seasonal access: "Open April–October; closed to visitors during hunting season"
- Permit requirements: "Day-use permit required; available at trailhead kiosk"
- Access restrictions: "No public access to western parcel; trail access only on
  marked footpaths"
- Public access status: "Hunt club easement; public access by written permission only"

**Invalid patterns (blank and log, or route to notes):**
- Hours of operation alone ("Open 8am–dusk") — this is operational; route to notes
- Contact information — route to notes
- Facility announcements — route to notes

**Relationship to Status field**: Access Notes does not replace the Status field.
If the site has a status-vocabulary-mapped condition (Active, Closed, Restricted,
Abandoned), that belongs in `status`. Access Notes captures nuanced access detail
that Status vocabulary cannot express.

**Provenance:** Record whether `access_notes` was populated from `access_notes_raw`
or left blank, and reason.

## 5.24 Last Verified Date (IMP-013) *(new in v6.0)*

**DATE field** — the date the site record was last verified against a source.

**Normalization rules:**

- Accept `last_verified_date` from raw discovery record (populated with today's date
  at discovery time).
- Validate format: must be ISO 8601 DATE format (YYYY-MM-DD).
- If present and valid → pass through unchanged.
- If format is invalid (e.g., MM/DD/YYYY, plain year) → attempt to parse and
  reformat to YYYY-MM-DD; log WARNING if reformatted.
- If absent or null → log WARNING; leave blank.

**Never infer or generate a date not present in the raw record.** The pipeline does
not set or modify this field except to validate format.

## 5.25 Field Verified (IMP-013) *(new in v6.0)*

**Boolean field** — whether the site record has been field-verified.

**Normalization rules:**

- Accept `field_verified` from raw discovery record (always `false` at discovery).
- Validate: must be boolean `true` or `false`.
- If present and valid → pass through unchanged.
- If value is string "false" or "False" → convert to boolean `false`; log.
- If value is string "true" or "True" → convert to boolean `true`; log.
- If absent or null → default to `false`; log WARNING.
- If any value other than true/false variants → null-and-log; flag for REVIEW.

**At discovery time, this field is always false.** A `true` value indicates
post-discovery field verification has occurred and must be documented in `notes`.

## 5.26 eBird Hotspot ID (IMP-021) *(new in v6.0)*

**Text field** — the eBird hotspot identifier for this site, if one exists.

**Normalization rules:**

- Accept `ebird_hotspot_id` from raw discovery record.
- Pass through verbatim — no mapping, no vocabulary enforcement, no transformation.
- Validate format: if populated, must match the pattern `L` followed by one or more
  digits (e.g., `L123456`). If format does not match → null-and-log; flag for REVIEW.
- If absent or null → leave blank. Blank is correct and expected for most sites.

**Never infer, generate, or look up an eBird hotspot ID during normalization.**
This field is populated only when explicitly captured at discovery time.

------------------------------------------------------------
# 6. IDENTITY ANCHOR VALIDATION

Top-level Sites:
- entity_type + name + counties

Child Sites:
- entity_type + name + counties + parent_site_id

Normalization must verify:
- All anchor fields present
- Counties valid and alphabetized
- Parent Site ID valid if present

------------------------------------------------------------
# 7. VALIDATION LOGIC

Normalization must validate:

- **Category vocabulary enforcement** (§5.2, IMP-063): FATAL REJECT on unmappable
  values; REVIEW flag on context-dependent mappings
- **Cultural institution name-pattern check** (§5.2, IMP-068): CATEGORY MISMATCH
  flag if Recreation Facility + cultural institution name pattern
- **Subtype vocabulary enforcement** (§5.3, IMP-064): null on unmappable; REVIEW
  flag on wrong-category subtypes
- **Subtype inference** (§5.3a, IMP-065): applied after §5.3, only when subtype blank
- Organizational field separation: ownership vs governance vs partner_agencies vs
  coordination
- GPS pairing and numeric format
- **GPS Gate** (§5.17a, IMP-069): HOLD in held_entities if GPS null and no
  gps_unresolvable flag
- **GPS County Check** (§5.17b, IMP-067): WARNING + manual_review_queue flag if
  GPS places entity outside documented counties
- Plus Code derivation
- **GIS municipality/township derivation** (§5.14, IMP-066): `get_both()` called
  after GPS validation
- Acres numeric
- Semicolon formatting
- **Habitat type** (§5.22): open vocabulary; no vocabulary enforcement; warn on
  duplicate of description
- **Access notes** (§5.23): free-text; warn on content that belongs in notes instead
- **Last verified date** (§5.24): DATE format validation; warn if absent
- **Field verified** (§5.25): boolean validation; default false if absent
- No invented data
- No placeholders
- No delimiter characters inside fields
- Parent Site validity
- Identity anchor completeness
- Municipality blocklist check (§5.14): REJECT if governance name, type label, or
  township value present in municipality field
- Township blocklist check (§5.15): REJECT if governance name or bare type label present
- Cross-field contamination check: REJECT if municipality == township for same entity

------------------------------------------------------------
# 8. DELIMITER INTEGRITY REQUIREMENTS

- Blank fields must be true blanks (null, not empty string).
- No trailing spaces.
- No collapsed semicolons.
- No missing delimiters in multi-value fields.

------------------------------------------------------------
# 9. CONFLICT HANDLING

- Conflicting names → use most authoritative; log alternates.
- Conflicting ownership → flag; never infer.
- Conflicting acreage → use highest-authority source; log conflict.
- Conflicting category → leave blank; log conflict.

------------------------------------------------------------
# 10. MISSING DATA RULES

- Leave blank if unverifiable.
- Never estimate acres.
- Never infer ownership, governance, partner agencies, or designation.
- Never generate GPS without authoritative source.
- Never copy municipality or township from discovery.
- If GPS is blank, municipality and township must also be blank.
- If GIS lookup fails, leave municipality and township blank.
- `habitat_type` and `access_notes` are left blank when not documented — do not
  infer from category, designation, or governance.
- `last_verified_date` is left blank when absent — do not generate a date.
- `field_verified` defaults to false when absent — do not assume verified.

------------------------------------------------------------
# 11. AUDITABILITY REQUIREMENTS

Normalization must record in `normalization_provenance`:

- All sources consulted
- All vocabulary mappings applied
- All null-and-log decisions
- All REVIEW and REJECT flags
- All blank-field decisions and reasons
- All GPS parsing results
- All GIS derivations
- All features normalization steps (activity mappings, operational strips, named
  entity drops, vocabulary mappings, unmapped token log)
- All description stripping decisions (IMP-052, IMP-059)
- All notes metadata stripping decisions (IMP-053)
- All habitat_type, access_notes, last_verified_date, field_verified outcomes
- All delimiter corrections
- Identity anchor validation result
- Deduplication check result

------------------------------------------------------------
# 12. MODULE DEPENDENCIES

This contract depends on:

- Site Vocabulary Module v6.0
- Site Schema Module v6.0
- Site Discovery Sub-Procedure v6.0 (child site rules)
- Resolution Engine v6.x
- Normalization Engine v6.0
- Entity Graph Schema v6.x
- Audit & Logging Module v6.x

------------------------------------------------------------
# END OF SITE NORMALIZATION CONTRACT v6.0
