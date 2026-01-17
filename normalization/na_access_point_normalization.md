# NATURAL AREAS PROJECT — ACCESS POINT NORMALIZATION CONTRACT v3.1
Deterministic, field‑by‑field normalization contract governing how Access Point
Raw Candidate Records are interpreted, validated, corrected, and prepared for
TSV serialization under the v3.1 ontology.

This module contains no controlled vocabularies.  
All vocabularies are defined in the **Access Point Vocabulary Module v3.1**.

---

# 1. PURPOSE

This module defines:

- How raw Access Point **Raw Candidate Records** from Discovery are normalized  
- How each Access Point schema field is populated from `raw_candidate_record`  
- How Access Point Type, Role, Status, and Access Level are validated against
  the Access Point Vocabulary Module v3.1  
- How identity parents (Site or Trail Segment) are validated  
- How County, Township, and Municipality are validated  
- How GPS and Plus Code rules are applied  
- How URL and source rules are applied  
- How any Derived Label or display label is constructed (if required by TSV)  
- How normalization interacts with the Audit & Logging Module and Resolution  

This module is authoritative for **Access Point normalization** in v3.1.

---

# 2. SCOPE

This contract applies to:

- All Access Points discovered through the **Discovery Protocol Module v3.1**  
- All Access Points produced by the **Access Point Discovery Sub‑Procedure v3.1**  
- All Access Points seeded from the **County Baseline Module v1.1**  
- All Access Points manually provided by the user (when mapped into
  `raw_candidate_record` form)  
- All counties and all processing runs  

Normalization must be:

- Deterministic  
- Non‑destructive  
- Audit‑ready  
- Fully reversible from logs and metadata  

---

# 3. INPUTS AND OUTPUTS

## 3.1 Inputs

Normalization consumes:

1. **Raw Candidate Record** (from Discovery Output Specification v3.1)  
   - `raw_candidate_record.entity_type` must be `Access Point`  
   - Includes fields such as:
     - `name_raw`
     - `county`, `township`, `municipality`
     - `access_point_type_raw`
     - `role_raw`
     - `parent_sites`
     - `parent_trail_systems`
     - `ownership_raw`
     - `access_level_raw`
     - `gps_raw`
     - `address_raw`
     - `url_primary`, `url_all`
     - `source_datasets`, `source_maps`, `source_gis_layers`
     - `discovery_tier`, `discovered_in_tiers`
     - `seeded_from_baseline`, `baseline_id`
     - `notes_raw`

2. **Discovery Metadata Object**  
   - As defined in **Discovery Metadata Specification v1.0**  
   - Embedded in `raw_candidate_record.discovery_metadata`

3. **Normalized Site and Trail Segment entities**  
   - From **Site Normalization Contract v3.1**  
   - Used to validate identity parents

## 3.2 Outputs

Normalization produces:

- A **normalized Access Point entity** conforming to the
  **Access Point Schema Module v3.1**  
- A record ready for export via the
  **Access Point TSV Output Specification v3.1**  
- Full audit trail entries via the **Audit & Logging Module v1.1**

No new information may be invented during normalization.

---

# 4. NORMALIZATION WORKFLOW (HIGH‑LEVEL)

Access Point normalization proceeds through the following steps:

1. **Receive Raw Candidate Record**  
   - Confirm `entity_type = Access Point`.

2. **Validate Identity**  
   - Validate `name_raw` and `access_point_type_raw`.  
   - Confirm the candidate meets Access Point identity rules.

3. **Resolve and Validate Parent**  
   - Determine the single identity parent (Site or Trail Segment).  
   - Validate against normalized Site and Trail Segment entities.  
   - Surface ambiguous or conflicting parents to Resolution.

4. **Normalize Core Fields**  
   - Name  
   - Access Point Type  
   - Role (if present)  
   - Parent fields (Site or Trail Segment)  

5. **Normalize Jurisdiction Fields**  
   - County (required)  
   - Township (optional)  
   - Municipality (optional)

6. **Normalize Location Fields**  
   - GPS (if available and valid)  
   - Plus Code (if supported and derivable from GPS)  
   - Address (if available and valid)

7. **Normalize Access & Status Fields**  
   - Access Level (from `access_level_raw`)  
   - Status (if present in vocabularies)  

8. **Normalize URLs and Sources**  
   - Primary URL  
   - All URLs  
   - Source datasets, maps, and GIS layers  

9. **Normalize Notes**  
   - Access‑related notes  
   - Boundary and uncertainty notes (if mapped into schema)  

10. **Apply Formatting Rules**  
    - Whitespace, delimiters, and TSV‑safe formatting.

11. **Emit Normalized Access Point Entity**  
    - Conforming to Access Point Schema v3.1.  
    - Ready for TSV export.

If any critical step fails, the issue must be logged and surfaced to the
**Resolution Module v3.1**.

---

# 5. FIELD‑LEVEL NORMALIZATION RULES

> Note: Field names below refer to the **Access Point Schema Module v3.1**.
> Where names differ, this contract governs the mapping from `raw_candidate_record`
> to schema fields.

---

## 5.1 Name

### Input
- `raw_candidate_record.name_raw`

### Rules

- Use the authoritative name as discovered, after trimming whitespace.  
- Do **not** normalize capitalization beyond minimal consistency rules defined
  in the Access Point Schema Module v3.1 (if any).  
- Do **not** translate, abbreviate, or expand names.  
- Do **not** construct names from amenities or inferred context.  
- If the raw name is clearly a constructed placeholder from Discovery
  (e.g., “Unnamed Access Point”), preserve it but flag
  `uncertainty.requires_review = true` in metadata.

### Prohibited

- Inventing new names.  
- Replacing a discovered name with a “nicer” or “cleaner” version.  

### Audit

- Log all name corrections (whitespace, encoding).  
- Log any cases where the name appears malformed or ambiguous.

---

## 5.2 Access Point Type

### Input
- `raw_candidate_record.access_point_type_raw`

### Rules

- Must be mapped to a value in the **Access Point Vocabulary Module v3.1**.  
- If `access_point_type_raw` exactly matches a controlled value, use it.  
- If it is a known synonym or variant, map to the canonical vocabulary value
  and log the correction.  
- If ambiguous or not mappable, leave the normalized type blank and set
  `uncertainty.requires_review = true`.

### Prohibited

- Inventing a type not present in the vocabulary.  
- Guessing type from amenities alone without textual or mapped support.

### Audit

- Log all mappings from raw to canonical type.  
- Log all unmappable or ambiguous types.

---

## 5.3 Role

### Input
- `raw_candidate_record.role_raw` (optional)

### Rules

- If present, map to the **Access Point Role** vocabulary (if defined) or
  preserve as raw if no vocabulary exists.  
- Allowed examples (if vocab exists): `Primary`, `Secondary`, `Connector`, `Unknown`.  
- If role is clearly malformed or contradictory, leave blank and flag
  `uncertainty.requires_review = true`.

### Audit

- Log all role mappings and omissions.

---

## 5.4 Parent Entity (Identity Parent)

### Inputs
- `raw_candidate_record.parent_sites`
- `raw_candidate_record.parent_trail_systems`
- Discovery Metadata `parents` section
- Normalized Site and Trail Segment entities

### Rules

- An Access Point must have **exactly one identity parent**:
  - A **Site**, or  
  - A **Trail Segment**  
- Identity parent must be a **normalized entity** that passes identity rules.  
- If multiple candidate parents exist:
  - Prefer the **Trail Segment** if the AP is clearly a trailhead for a specific segment.  
  - Otherwise, prefer the **Site** that best matches authoritative sources.  
  - If ambiguity remains, do not assign a parent and surface to Resolution.  
- Parent fields in the Access Point Schema must be populated according to
  the schema’s parent structure (e.g., `parent_site_id`, `parent_trail_segment_id`,
  or equivalent).

### Prohibited

- Assigning multiple identity parents.  
- Using Trail, Trail Network, or Site Network as identity parents
  (these belong in the **Access Point Association Module v3.1**).  
- Inferring parents from proximity alone without authoritative support.

### Audit

- Log all parent resolutions and conflicts.  
- Log all cases where no valid parent could be assigned.

---

## 5.5 Jurisdiction Fields (County, Township, Municipality)

### Inputs
- `raw_candidate_record.county`
- `raw_candidate_record.township`
- `raw_candidate_record.municipality`
- Discovery Metadata `boundary` section

### County Rules

- **County is required.**  
- Must match the official Ohio county list.  
- Must represent the county in which the Access Point physically resides.  
- Must not be inferred solely from the parent Site’s county.  
- If Discovery indicates multi‑county context, the Access Point must still be
  anchored to a single county for normalization; multi‑county logic is handled
  at the Site/Trail level and in metadata.

### Township & Municipality Rules

- Include if known and validated against authoritative sources.  
- Must not be invented or guessed from address alone without corroboration.  
- If both township and municipality are present, preserve both.

### Audit

- Log all jurisdiction sources.  
- Log unverifiable or conflicting jurisdiction claims.

---

## 5.6 Location Fields (GPS, Plus Code, Address)

### GPS

#### Input
- `raw_candidate_record.gps_raw`

#### Rules

- Accept only authoritative coordinates from GIS or official maps.  
- Reject placeholder coordinates (e.g., `0,0`, obvious centroids).  
- Reject reverse‑geocoded guesses.  
- If GPS cannot be verified, leave blank and flag uncertainty if appropriate.

### Plus Code (if supported by schema)

#### Rules

- Generate only from **accepted GPS**.  
- If GPS is blank or rejected, Plus Code must be blank.  
- No reverse‑geocoded or approximate Plus Codes.

### Address

#### Input
- `raw_candidate_record.address_raw`

#### Rules

- Preserve as discovered, with minimal formatting cleanup (whitespace, encoding).  
- Do not normalize to USPS format in this module.  
- Do not invent addresses.

### Audit

- Log accepted and rejected GPS values.  
- Log Plus Code generation.  
- Log unverifiable or conflicting location data.

---

## 5.7 Access Level and Status

### Access Level

#### Input
- `raw_candidate_record.access_level_raw`

#### Rules

- Map to the **Access Level** vocabulary in the Access Point Vocabulary Module v3.1.  
- Examples: `Public`, `Limited Public`, `Fee‑Based`, `Seasonal`,
  `Reservation‑Only`, `Program‑Only`, `Private (No Access)`.  
- If unmappable, preserve raw value in notes or a raw field (if schema supports)
  and leave normalized access level blank; flag for review.

### Status

#### Input
- If a Status field exists in the Access Point Schema and/or vocabularies.

#### Rules

- Must match a value from the Status vocabulary (if defined).  
- Use authoritative status if provided.  
- If ambiguous, leave blank and flag uncertainty.

### Audit

- Log all access level and status mappings.  
- Log unverifiable or conflicting claims.

---

## 5.8 URLs and Sources

### Inputs
- `raw_candidate_record.url_primary`
- `raw_candidate_record.url_all`
- `raw_candidate_record.source_datasets`
- `raw_candidate_record.source_maps`
- `raw_candidate_record.source_gis_layers`
- Discovery Metadata `sources` section

### URL Rules

- `url_primary` must be the most authoritative URL, if any.  
- All URLs must be full `https://` URLs.  
- No placeholders or partial URLs.  
- Multiple URLs may be preserved in a list or semicolon‑delimited string,
  depending on schema/TSV requirements.

### Source Rules

- All datasets, maps, and GIS layers used must be preserved.  
- No source may be discarded.  
- Names must match those used in Discovery Metadata where possible.

### Audit

- Log URL corrections and removals.  
- Log all source lists as part of metadata.

---

## 5.9 Notes

### Input
- `raw_candidate_record.notes_raw`
- Discovery Metadata `notes.general`, `uncertainty.notes`, etc.

### Rules

- Preserve access‑related notes (conditions, signage, seasonal closures, etc.).  
- Do not move identity‑defining information into notes if it belongs in
  structured fields.  
- Do not inject editorial commentary.  
- Notes may be concatenated from multiple raw sources, with clear delimiters
  if needed.

### Audit

- Log any redactions or structural moves of note content.

---

## 5.10 Derived Label (If Required)

If the Access Point Schema or TSV Output Specification v3.1 requires a
**Derived Label** or display label:

### Example Formula

- `Access Point Type + " Access Point"`  
  (e.g., `Trailhead Access Point`, `Parking Access Point`)

### Rules

- Must be derived solely from normalized fields.  
- Must not be stored as a primary identity field.  
- Must not introduce new semantics beyond type + label.

### Audit

- Log the derivation rule used.

---

# 6. FORMATTING RULES

- No leading or trailing spaces in any field.  
- No internal tabs or newlines in TSV‑bound fields.  
- Blank fields must be true blanks, not placeholders.  
- All fields must pass **TSV Output Specification (Access Points) v3.1**
  validation.  
- No invented data.  
- No placeholder values such as `N/A`, `Unknown`, or `TBD` unless explicitly
  allowed by vocabularies.

---

# 7. ERROR CONDITIONS

Normalization must halt for the affected record and surface an error to the
**Resolution Module v3.1** if:

- Identity parent (Site or Trail Segment) cannot be validated  
- Access Point Type cannot be mapped to the vocabulary  
- County is missing or invalid  
- GPS is malformed (if present)  
- URL is malformed (if present)  
- Required schema fields cannot be populated from raw data  

All errors must be:

- Logged via the **Audit & Logging Module v1.1**  
- Linked to the original `raw_candidate_record` and metadata  
- Marked for Resolution review

---

# 8. MODULE DEPENDENCIES

This module depends on:

- **Access Point Vocabulary Module v3.1**  
- **Access Point Schema Module v3.1**  
- **Access Point TSV Output Specification v3.1**  
- **Discovery Output Specification v3.1**  
- **Discovery Metadata Specification v1.0**  
- **Discovery Protocol Module v3.1**  
- **Access Point Discovery Sub‑Procedure v3.1**  
- **Site Normalization Contract v3.1**  
- **Trail Segment Normalization (within Trail Segment Schema/logic) v3.1**  
- **Access Point Association Module v3.1**  
- **Audit & Logging Module v1.1**  
- **Resolution Module v3.1**  
- **Processing / Orchestration Module v3.1**

---

# 9. VERSIONING

- This module is **Access Point Normalization Contract v3.1**.  
- Any change to normalization logic, required fields, or dependencies requires
  v3.2, v3.3, etc.  
- Any change to ontology or discovery workflow must be made first in the
  **Discovery Protocol Module v3.1+**, then reflected here.

---

# END OF ACCESS POINT NORMALIZATION CONTRACT v3.1