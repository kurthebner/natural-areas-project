# NATURAL AREAS PROJECT — SITE NORMALIZATION CONTRACT v1
A deterministic, field‑by‑field normalization and validation protocol for transforming raw discovery outputs into the 25‑field Site dataset. This module ensures zero invention, zero drift, and full auditability.

This module contains no controlled vocabularies.  
All vocabularies are defined in the Site Vocabulary Module v1.

---

# 1. PURPOSE
This module defines:

- How raw Site discoveries are normalized  
- How each of the 25 Site fields is populated  
- How Category, Subtype, Designation, Status, Trail Role, Trail Segment Type, Trail Access Type, and Features are validated against the Site Vocabulary Module v1  
- How Parent Site and Parent Trail relationships are validated  
- How GPS, Plus Code, and URL rules are applied  
- How Derived Label is constructed  
- How normalization integrates with the Audit & Logging Module  

This module is authoritative for Site normalization.

---

# 2. INPUT TO THIS MODULE
The input is the raw candidate list produced by the Discovery Protocol, containing:

- Name  
- URL(s)  
- Source of discovery  
- Notes on discovery context  
- Any available GPS  
- Any available address  
- Any available acreage  
- Any available trail role  
- Any available designation  

No assumptions may be made beyond what is explicitly present or verifiable.

---

# 3. OUTPUT OF THIS MODULE
A fully normalized, audit‑ready dataset with all **25 fields** in the following order:

1. Name  
2. Category  
3. Subtype  
4. Designation  
5. Ownership  
6. Management  
7. Coordination  
8. Description  
9. Status  
10. Address  
11. Acres  
12. Location  
13. County  
14. GPS Coordinates  
15. Plus Code  
16. Trail Role  
17. Parent Trail Name  
18. Trail Segment Type  
19. Trail Access Type  
20. Trail Length (Miles)  
21. Features  
22. Notes  
23. URL  
24. Derived Label (computed, not stored)  
25. Parent Site  

The TSV Output Specification consumes this normalized structure.

---

# 4. FIELD‑BY‑FIELD NORMALIZATION RULES

---

## 4.1 Name
- Use the official published name.  
- If multiple names exist, choose the most authoritative.  
- Former names go in Description.  
- Never invent names.  

---

## 4.2 Category
- Must match a value from the **Site Vocabulary Module v1**.  
- Never infer Category from amenities or features.  
- If ambiguous, surface for Resolution.  

---

## 4.3 Subtype
- Optional.  
- If present, must match the Category‑dependent lists in the **Site Vocabulary Module v1**.  
- Must not describe habitat conditions or temporary states.  
- Leave blank if no subtype applies.  

---

## 4.4 Designation
- Must match a value from the **Site Vocabulary Module v1**.  
- Never infer designation.  
- If unverifiable, surface for review.  
- Semicolon‑delimit if multiple.  
- Leave blank if none.  

---

## 4.5 Ownership
- Use the legal owner as stated by authoritative sources.  
- Never infer ownership.  
- Leave blank if unknown.  

---

## 4.6 Management
- Use the operational manager(s).  
- Semicolon‑delimit if multiple.  
- If same as Ownership, repeat explicitly.  
- Leave blank if unknown.  

---

## 4.7 Coordination
- Only formal coordinating entities.  
- Leave blank if none.  

---

## 4.8 Description
- 1–3 sentences.  
- Must describe identity‑defining ecological or historical characteristics.  
- Include naming history and former names.  
- Must not include amenities or temporary conditions.  

---

## 4.9 Status
- Must match a value from the **Site Vocabulary Module v1**.  
- “Closed” = permanently closed as the entity described.  
- “Proposed” must be officially referenced.  

---

## 4.10 Address
- Use authoritative address if available.  
- If partial address is verifiable, include partial.  
- Leave blank if no address exists.  
- Never invent.  

---

## 4.11 Acres
- Numeric only.  
- Leave blank if unknown.  
- Never estimate.  

---

## 4.12 Location
- Municipality or township only.  
- Semicolon‑delimit if multiple.  
- Must not include county names.  
- If many jurisdictions, use jurisdiction of Address.  

---

## 4.13 County
- List all counties the site spans.  
- Alphabetical.  
- Semicolon‑delimited.  
- Omit the word “County.”  

---

## 4.14 GPS Coordinates
- One coordinate pair in decimal degrees.  
- Format: `lat,lon` (no space after comma).  
- Accept only authoritative coordinates.  
- Reject placeholders or unverifiable coordinates.  
- Leave blank if verification fails.  

---

## 4.15 Plus Code
- Generated only from accepted GPS.  
- If GPS is blank, Plus Code is blank.  

---

## 4.16 Trail Role
- Must match a value from the **Site Vocabulary Module v1**.  
- Non‑trail sites = “None.”  
- Never infer from features.  

---

## 4.17 Parent Trail Name
- Required for segments and spurs.  
- Blank for standalone trails and non‑trail sites.  
- Must match the official name of the parent trail.  

---

## 4.18 Trail Segment Type
- Must match a value from the **Site Vocabulary Module v1**.  
- Use only when Trail Role = Trail Segment.  
- Use “None” when not applicable.  

---

## 4.19 Trail Access Type
- Must match a value from the **Site Vocabulary Module v1**.  
- Use only when the site functions as a trail access location.  
- Use “None” when not applicable.  

---

## 4.20 Trail Length (Miles)
- Numeric only.  
- Blank for non‑trail sites.  
- No estimates.  
- No units.  

---

## 4.21 Features
- Semicolon‑delimited list.  
- Must match values from the **Site Vocabulary Module v1**.  
- Features describe internal components, not identity‑bearing land units.  
- Named trails are never Features.  
- Unnamed trails use trail‑related Feature terms.  
- Minor connectors belong in Notes, not Features.  

---

## 4.22 Notes
- Optional free‑text field.  
- Must not include identity‑defining ecology.  
- Must not include internal features.  
- Use for temporary closures, access restrictions, historical notes, or clarifications.  

---

## 4.23 URL
- Full `https://` URLs only.  
- Semicolon‑delimit if multiple.  
- Must be authoritative.  

---

## 4.24 Derived Label
Derived Label is computed but not stored.

**Formula:**  
**Category + (Ownership if present else Management) + Designation**

Rules:
- If Ownership exists → use Ownership.  
- If Ownership is blank and Management exists → use Management.  
- If both are blank → Derived Label = Category.  
- If Designation exists → append Designation.  
- If both Ownership/Management and Designation exist → append both, comma‑separated.  

All Derived Label construction must be logged.

---

## 4.25 Parent Site
- Leave blank for top‑level sites.  
- Must match the official Name of the parent site.  
- A site may have only one parent.  
- Parent–child relationships must be explicit in authoritative sources.  

---

# 5. VALIDATION LOGIC
Normalization must validate:

- All vocabulary‑controlled fields  
- GPS format  
- Plus Code generation  
- Semicolon formatting  
- Field order  
- No invented data  
- Blank fields are true blanks  
- No delimiter characters inside fields  

If any field fails validation:
- Surface the issue  
- Do not silently correct  

---

# 6. DELIMITER‑INTEGRITY REQUIREMENTS
Normalization must ensure:

- Blank fields are true blanks  
- No spaces between delimiters  
- No trailing spaces  
- No collapsed delimiters  
- No missing or extra delimiters  

Any anomaly must be logged.

---

# 7. CONFLICT RESOLUTION RULES
### 7.1 Conflicting Names
- Use the most authoritative source.  
- Record alternates in Description.  

### 7.2 Conflicting Ownership
- Flag for Resolution; never infer.  

### 7.3 Conflicting Acreage
- Use the most authoritative source.  
- If conflict persists, flag for Resolution.  

### 7.4 Conflicting Trail Roles
- Use the most authoritative trail system source.  
- If unclear, flag for Resolution.  

---

# 8. MISSING DATA RULES
- If data is missing and cannot be verified, leave blank.  
- Never estimate.  
- Never infer ownership, designation, or acreage.  
- Never generate GPS without verification.  

---

# 9. AUDITABILITY REQUIREMENTS
Copilot must:

- Record all sources used  
- Record conflicts  
- Record unverifiable claims  
- Record normalization decisions  
- Record Derived Label construction  
- Record delimiter‑integrity validation  
- Never overwrite user‑provided data without surfacing the change  

---

# 10. MODULE DEPENDENCIES
This module depends on:

- **Site Vocabulary Module v1**  
- **Site Schema Module v1**  
- **TSV Output Specification (Sites) v1**  
- **Audit & Logging Module**  
- **Resolution Module**  
- **Discovery Protocol v2**  
- **Processing Orchestration Module**

---

# END OF SITE NORMALIZATION CONTRACT v1