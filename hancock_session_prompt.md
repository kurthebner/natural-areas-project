# New Session Prompt — Hancock County, Ohio

## What You Are Doing

You are beginning a Natural Areas Project discovery run for **Hancock County, Ohio**. This is a fresh county — no prior session files exist and there are no Hancock entities in the database yet.

Your first action is to invoke the **na-bootstrap** skill, which will walk you through setting up the session files and preparing for Tier 1 discovery.

---

## Project Location

The workspace folder is:
`D:\users\user1\Documents\CP Projects\Natural Areas Project v5`

All session files (staging YAML, session log, handoff) go in this folder.
The database is at `NASqlite/natural_areas_v5.db`.

---

## Key Facts for This County

- **County:** Hancock County, Ohio
- **County seat:** Findlay
- **County abbreviation (for entity IDs):** `HAN`
- **Entity ID format:** `OH-HAN-{TYPE}-{SEQ}` (e.g., OH-HAN-S-0001)
  *(IMP-107: all Ohio entity IDs use OH- prefix; four-digit zero-padded sequence)*
- **No multi-county entities** currently in the DB touch Hancock County

---

## Baseline

A human-curated baseline spreadsheet exists at:
`County_Spreadsheets/Hancock/Hancock.xlsx`

It has two sheets:
- **Sheet1** — original seed list (~63 rows)
- **from Copilot** — expanded list (~136 rows) with more detail, descriptions, and some GPS coordinates

Read both sheets during bootstrap. The "from Copilot" sheet is the richer source. Treat all entries as seeds to be confirmed through discovery — not as import-ready records.

---

## Module Reference Convention (IMP-109)

When reading or citing project modules, references use **bare document titles without version numbers** — e.g., `na_resolution_engine.md`, not `na_resolution_engine_v5.5.md`. The **module manifest** (`na_module_manifest_v5.18.md`) is the authoritative source for current versioned filenames if you need to Read a specific file.

---

## Skills to Use

1. **na-bootstrap** — run first; sets up session files and county context
2. **na-discovery** — executes the eight discovery tiers
3. **na-pipeline** — post-discovery processing (only after all 8 tiers are complete)

---

## Current Project State

- 12+ Ohio counties completed and in the DB
- IMP-107 applied: all entity IDs are in `OH-{COUNTY}-{TYPE}-{SEQ}` format
- IMP-109 applied: all module cross-references use bare titles; the manifest lists versioned filenames
- The `Parks_and_Open_Space_7241389496048841555.csv` GIS layer covers Hancock County (it is in the 15-county regional set: DEL, FAI, FAY, FRA, HOC, KNO, LIC, LOG, MAD, MAR, MRW, PER, PIC, ROS, UNI — **Hancock is NOT in this set**, so the CSV cross-check does not apply for Tier 4 or Tier 6)

---

## Start Here

Invoke the **na-bootstrap** skill now to begin.
