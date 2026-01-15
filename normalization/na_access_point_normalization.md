# NATURAL AREAS PROJECT — ACCESS POINT NORMALIZATION CONTRACT v1
A deterministic, field‑by‑field normalization contract governing how Access Point records are interpreted, validated, corrected, and prepared for TSV serialization. This module ensures zero invention, zero drift, and full auditability.

This module contains no controlled vocabularies.  
All vocabularies are defined in the Access Point Vocabulary Module v1.

---

# 1. PURPOSE
This module defines:

- How raw Access Point discoveries are normalized  
- How each of the 10 Access Point fields is populated  
- How Access Point Type and Status are validated against the Access Point Vocabulary Module v1  
- How Parent Site relationships are validated  
- How GPS, Plus Code, and URL rules are applied  
- How Derived Label is constructed  
- How normalization interacts with the Audit & Logging Module  

This module is authoritative for Access Point normalization.

---

# 2. SCOPE
This contract applies to:

- All Access Points discovered through the Discovery Protocol  
- All Access Points manually provided by the user  
- All Access Points derived from authoritative sources  
- All counties and all processing runs  

Normalization must be deterministic and audit‑ready.

---

# 3. NORMALIZATION WORKFLOW (HIGH‑LEVEL)
Access Point normalization proceeds through the following steps:

1. Receive raw Access Point candidate  
2. Validate identity  
3. Validate Parent Site  
4. Normalize each field according to this contract  
5. Validate Access Point Type and Status using the Access Point Vocabulary Module v1  
6. Apply GPS and Plus Code rules  
7. Apply URL rules  
8. Construct Derived Label  
9. Validate formatting rules  
10. Emit normalized 10‑field record  

If any step fails, the issue must be logged and surfaced.

---

# 4. FIELD‑BY‑FIELD NORMALIZATION RULES

---

## 4.1 Access Point Name (Field 1)

### Acceptable sources
- Official park district maps  
- ODNR maps  
- Municipal or county GIS  
- On‑site signage (if documented)  
- Authoritative PDFs or brochures  

### Rules
- Use authoritative names exactly as published.  
- If unnamed but clearly identifiable, construct:  
  **Parent Site + " — " + Access Point Type**  
- Never invent names.  
- Never infer names from amenities.  
- Never use internal feature names.

### Audit requirements
- Log all sources consulted.  
- Log any constructed names.  
- Log any conflicts.

---

## 4.2 Access Point Type (Field 2)

### Rules
- Must match a value from the **Access Point Vocabulary Module v1**.  
- No synonyms or variants.  
- “Other” allowed only when explicitly named by authoritative sources.  
- If ambiguous, surface for Resolution.  
- Never infer type from amenities alone.

### Audit requirements
- Log all type conflicts.  
- Log any vocabulary corrections.

---

## 4.3 Parent Site (Field 3)

### Rules
- Must match the **exact Name** of a normalized Site.  
- No abbreviations or synonyms.  
- If multiple possible parents exist, surface for Resolution.  
- If parent cannot be determined, Access Point cannot be created.

### Audit requirements
- Log all parent conflicts.  
- Log unverifiable parent relationships.

---

## 4.4 GPS Coordinates (Field 4)

### Acceptable sources
- Official GIS  
- ODNR maps  
- County GIS  
- Municipal GIS  
- Authoritative recreation maps  

### Rules
- Accept only authoritative coordinates.  
- Verify using Name + Parent Site + Road Name.  
- Reject placeholder coordinates (0,0 or centroid defaults).  
- Reject reverse‑geocoded guesses.  
- If GPS cannot be verified, leave blank.

### Audit requirements
- Log accepted coordinates.  
- Log rejected coordinates.  
- Log unverifiable coordinates.

---

## 4.5 Plus Code (Field 5)

### Rules
- Generate only from accepted GPS.  
- If GPS is blank, Plus Code must be blank.  
- No reverse‑geocoded Plus Codes.

### Audit requirements
- Log Plus Code generation.  
- Log any rejected Plus Codes.

---

## 4.6 Road Name (Field 6)

### Acceptable sources
- GIS road layers  
- Official park maps  
- ODNR maps  
- County engineer maps  

### Rules
- Must be an authoritative road name.  
- No invented or inferred road names.  
- If road name cannot be verified, leave blank.

### Audit requirements
- Log all road name sources.  
- Log unverifiable road names.

---

## 4.7 Access Notes (Field 7)

### Allowed content
- Access conditions  
- Parking details  
- Gate hours  
- Seasonal closures  
- Trail signage  
- Water level considerations  

### Prohibited content
- Features vocabulary terms  
- Amenities  
- Ecological descriptions  
- Governance history  
- Trail logic fields  

### Audit requirements
- Log any removed or corrected content.

---

## 4.8 URL (Field 8)

### Rules
- Full `https://` URLs only.  
- Semicolon‑delimited if multiple.  
- No placeholders.  
- No partial URLs.  
- No inferred URLs.

### Audit requirements
- Log all URL corrections.  
- Log unverifiable URLs.

---

## 4.9 Status (Field 9)

### Rules
- Must match a value from the **Access Point Vocabulary Module v1**.  
- Use authoritative status if provided.  
- If ambiguous, leave blank.  
- Never infer status from imagery alone.

### Audit requirements
- Log all status conflicts.  
- Log unverifiable status claims.

---

## 4.10 Derived Label (Field 10)

### Formula
**Access Point Type + " Access Point"**

### Rules
- No parentheses.  
- No punctuation.  
- No additional descriptors.  
- Must match Access Point Type exactly.  
- Not stored in the normalized dataset.

### Audit requirements
- Log Derived Label construction.

---

# 5. FORMATTING RULES
- No leading or trailing spaces.  
- No internal tabs or newlines.  
- Blank fields must be true blanks.  
- All fields must pass TSV Output Specification validation.  
- No invented data.  
- No placeholders.

---

# 6. ERROR CONDITIONS
Normalization must halt and surface an error if:

- Parent Site cannot be validated  
- Access Point Type is not in the vocabulary  
- Status is not in the vocabulary  
- GPS is malformed  
- URL is malformed  
- Derived Label cannot be constructed  
- Field order is incorrect  

All errors must be logged.

---

# 7. MODULE DEPENDENCIES
This module depends on:

- **Access Point Vocabulary Module v1**  
- **Access Point Schema Module v1**  
- **TSV Output Specification (Access Points) v1**  
- **Audit & Logging Module**  
- **Resolution Module**  
- **Discovery Protocol v2**  
- **Processing Orchestration Module**

---

# END OF ACCESS POINT NORMALIZATION CONTRACT v1