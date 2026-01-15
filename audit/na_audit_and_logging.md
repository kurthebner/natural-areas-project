# NATURAL AREAS PROJECT — AUDIT & LOGGING MODULE v1
A deterministic framework for recording, storing, and surfacing all decisions, sources, conflicts, formatting transformations, and delimiter‑integrity checks made during the Natural Areas processing pipeline for **Sites** and **Access Points**.

This module contains no controlled vocabularies.  
All vocabularies are defined in the Site Vocabulary Module v1 and Access Point Vocabulary Module v1.

---

# 1. PURPOSE
This module defines:

- What Copilot must log during each processing run  
- How logs are structured  
- How conflicts and ambiguities are surfaced  
- How formatting and delimiter integrity are validated  
- How module versions are recorded  
- How audit trails ensure reproducibility and transparency  

This module ensures:

- Every decision is traceable  
- Every data source is documented  
- No silent corrections occur  
- No silent formatting drift occurs  
- All conflicts are visible to the user  
- All delimiter‑integrity issues are surfaced  
- The entire pipeline is reproducible at any time  

---

# 2. SCOPE OF LOGGING
Copilot must log all actions taken during:

- Baseline loading  
- Discovery (Sites + Access Points)  
- Resolution (Sites + Access Points)  
- Normalization (Sites + Access Points)  
- TSV output generation (Sites + Access Points)  
- TSV delimiter‑integrity validation (Sites + Access Points)  

Logging applies to:

- Every Site  
- Every Access Point  
- Every field  
- Every conflict  
- Every correction  
- Every unverifiable claim  
- Every formatting correction  
- Every delimiter‑integrity anomaly  

---

# 3. LOG STRUCTURE
Each processing run produces a structured log with the following sections.

---

## 3.1 Run Metadata
- County name  
- Timestamp (start and end)  
- Module versions used:  
  - Site Schema Module v1  
  - Access Point Schema Module v1  
  - Site Vocabulary Module v1  
  - Access Point Vocabulary Module v1  
  - County Baseline Module  
  - Discovery Protocol Module v1  
  - Resolution Module v1  
  - Site Normalization Contract v1  
  - Access Point Normalization Contract v1  
  - Site TSV Output Specification v1  
  - Access Point TSV Output Specification v1  
  - TSV Integrity Check Module  
  - Processing Orchestration Module v1  
  - Audit & Logging Module v1  

---

## 3.2 Source Log
For each Site and Access Point:

- All URLs consulted  
- All GIS layers consulted  
- All authoritative documents consulted  
- All secondary sources consulted  
- Notes on source reliability (if applicable)  

---

## 3.3 Conflict Log
For each conflict:

- Entity type (Site or Access Point)  
- Field name (e.g., Ownership, Acres, Category, Access Point Type)  
- Conflicting values  
- Sources of each conflicting value  
- Resolution applied (or flagged for user review)  
- Module responsible for resolution  

---

## 3.4 Correction Log
For each correction:

- Entity type  
- Field name  
- Original value  
- Corrected value  
- Reason for correction  
- Source supporting correction  
- Module responsible for correction  

---

## 3.5 Unverifiable Claims Log
For each unverifiable claim:

- Entity type  
- Field name  
- Claimed value  
- Source of claim  
- Reason unverifiable  
- Action taken (e.g., left blank, flagged)  

---

## 3.6 Exclusion Log
For each excluded entity:

- Name  
- Entity type (Site or Access Point)  
- Reason for exclusion  
- Module rule invoked  
- Source(s) supporting exclusion  

---

## 3.7 Multi‑Site Complex Log
For each split:

- Parent Site  
- Child Sites created  
- Reason for split  
- Rules invoked  

(Access Points are never split.)

---

## 3.8 Normalization Log
For each Site and Access Point:

- All fields normalized  
- Any fields left blank (with reason)  
- Any formatting corrections  
- Any controlled vocabulary assignments  
- Derived Label construction details  
  - Including fallback to Management when Ownership is blank (Sites)  
  - Including Access Point Type → Derived Label mapping (Access Points)  

---

## 3.9 Delimiter‑Integrity Log
For each TSV row:

### Sites
- Expected delimiter count: **24 tabs**  
- Actual delimiter count  
- Whether the row passed delimiter‑integrity validation  
- Any anomalies:  
  - Missing delimiters  
  - Extra delimiters  
  - Spaces between delimiters  
  - Collapsed blank fields  
  - Misaligned fields  

### Access Points
- Expected delimiter count: **9 tabs**  
- Actual delimiter count  
- Same anomaly checks as above  

### Corrective Action
- Whether the row was corrected  
- Whether the row was rejected  
- Whether the pipeline halted  

---

# 4. LOGGING RULES

## 4.1 No Silent Corrections
Every correction must appear in the Correction Log.

## 4.2 No Silent Exclusions
Every exclusion must appear in the Exclusion Log.

## 4.3 No Silent Assumptions
If a field cannot be verified, it must be logged as unverifiable.

## 4.4 No Invented Data
If data is missing, leave blank and log the absence.

## 4.5 All Sources Must Be Recorded
Even if a source yields no useful information.

## 4.6 All Conflicts Must Be Surfaced
Conflicts are never resolved silently.

## 4.7 All Module Versions Must Be Recorded
This ensures reproducibility across runs.

## 4.8 Blank Fields Must Be True Blanks
Blank fields must be represented as true empty values between delimiters  
(e.g., `\t\t` in TSV).  
No spaces, placeholders, or invisible characters.

## 4.9 Delimiter Count Must Be Validated
- Sites: exactly **24 tabs**  
- Access Points: exactly **9 tabs**  
Any deviation must be logged.

---

# 5. USER‑VISIBLE SURFACING
At the end of each run, Copilot must surface:

- Summary of conflicts requiring user review  
- Summary of unverifiable claims  
- Summary of exclusions  
- Summary of multi‑site splits  
- Summary of baseline anomalies  
- Summary of normalization failures  
- Summary of delimiter‑integrity anomalies  

These summaries must be concise but complete.

---

# 6. STORAGE & RETENTION

## 6.1 Logs are stored per county per run  
## 6.2 Logs must be retrievable for comparison across runs  
## 6.3 Logs must include module version numbers  
## 6.4 Logs must not overwrite previous logs unless explicitly instructed  

---

# 7. AUDIT TRAIL REQUIREMENTS
A valid audit trail must allow the user to:

- Reconstruct every decision  
- Trace every field to its source  
- Identify every conflict and how it was resolved  
- Verify that no invented data was introduced  
- Confirm that all modules were applied in the correct order  
- Confirm that all delimiter‑integrity checks passed  
- Confirm that both entity types were processed correctly  

---

# 8. PIPELINE INTEGRATION
This module is invoked automatically during:

- Stage 1 (Baseline Loading)  
- Stage 2 (Discovery)  
- Stage 3 (Resolution)  
- Stage 4 (Normalization)  
- Stage 5 (TSV Output)  
- Stage 6 (TSV Integrity Check)  

It produces the final output of Stage 7.

---

# 9. MODULE DEPENDENCIES
This module depends on:

- **Site Schema Module v1**  
- **Access Point Schema Module v1**  
- **Site Vocabulary Module v1**  
- **Access Point Vocabulary Module v1**  
- **Discovery Protocol v1**  
- **Resolution Module v1**  
- **Site Normalization Contract v1**  
- **Access Point Normalization Contract v1**  
- **Site TSV Output Specification v1**  
- **Access Point TSV Output Specification v1**  
- **TSV Integrity Check Module**  
- **Processing Orchestration Module v1**

---

# END OF AUDIT & LOGGING MODULE v1