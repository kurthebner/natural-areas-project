# Natural Areas Project - Skills Package Overview

## Package Contents

This package contains **5 uploadable skills** for the Natural Areas Project v4.0:

### 1. Natural Areas Discovery Workflow Skill
**File:** `na-discovery-workflow.zip`  
**Modules:** 18 discovery modules + best practices  
**Purpose:** Systematic tier-based discovery of natural areas across jurisdictions  
**Use when:** Conducting natural areas discovery in a county or region

### 2. Natural Areas Schema & Vocabulary Skill
**File:** `na-schema-vocabulary.zip`  
**Modules:** 15 modules (9 schemas + 6 vocabularies)  
**Purpose:** Entity definitions and controlled vocabularies for the six-entity ontology  
**Use when:** Structuring data, validating schemas, checking vocabularies

### 3. Natural Areas Normalization & Output Skill
**File:** `na-normalization-output.zip`  
**Modules:** 15 modules (8 normalization + 7 output specs)  
**Purpose:** Data normalization and TSV output generation  
**Use when:** Cleaning data, generating exports, validating quality

### 4. Natural Areas Processing & Quality Control Skill
**File:** `na-processing-quality.zip`  
**Modules:** 9 modules (5 workflow + 2 quality + 2 reference)  
**Purpose:** Workflow orchestration, resolution, audit, and baseline management  
**Use when:** Orchestrating workflows, resolving conflicts, quality audits

### 5. Natural Areas Complete System (Mega-Skill)
**File:** `na-complete-system.zip`  
**Modules:** All 47 v4.0 modules + best practices  
**Purpose:** Complete end-to-end system for comprehensive projects  
**Use when:** Full county projects, training, complete system reference

---

## Skill Selection Guide

### For Focused Tasks
Use the **modular skills** (1-4) when working on specific phases:
- Just discovery → Use skill #1
- Just schema/vocab reference → Use skill #2
- Just normalization/output → Use skill #3
- Just orchestration/QA → Use skill #4

### For Complete Projects
Use the **mega-skill** (#5) when you need:
- End-to-end county discovery
- Complete pipeline from discovery to output
- Full system documentation
- Training and teaching
- Maximum capability in one skill

---

## Natural Areas Project v4.0 Overview

### Six-Entity Ontology
1. **Site** - Parks, preserves, forests, wildlife areas
2. **Trail** - Named trails within or across sites
3. **Trail Segment** - Distinct sections of trails
4. **Trail Network** - Collections of related trails
5. **Site Network** - Collections of related sites
6. **Access Point** - Parking areas, trailheads, entrances

### Eight-Tier Discovery System
1. State facilities (parks, forests, wildlife areas)
2. Federal facilities (national parks/forests/refuges)
3. County park districts
4. Regional park districts
5. Township parks
6. Municipal parks (all cities and villages)
7. Conservancy preserves (land trusts, TNC, Audubon)
8. Private preserves (universities, foundations)

### Four-Stage Processing Pipeline
```
Discovery → Resolution → Normalization → Entity Graph/Output
```

### Core Methodology Principles
1. **SYSTEMATIC BEATS SMART** - Check every entity, no assumptions
2. **FETCH BEATS SEARCH** - Get actual pages, don't trust snippets
3. **DOCUMENT BEATS REMEMBER** - Record everything with full provenance

---

## Installation Instructions

### Upload to Claude

1. **For Claude.ai users (Pro/Team/Enterprise):**
   - Go to Settings → Capabilities → Skills
   - Click "Upload Skill"
   - Select one of the .zip files
   - Enable the skill after upload

2. **For Claude Code users:**
   - Skills are automatically available in beta
   - Place .zip files in your skills directory
   - Skills will be loaded when relevant

3. **For API users:**
   - Extract the .zip file
   - Reference the SKILL.md and reference modules in your API calls
   - Skills available via code execution tool

### Choosing Which Skills to Upload

**Recommended Approach:**

**Option A - Modular (Recommended for most users):**
Upload skills 1-4 individually. This gives you:
- Lighter-weight skills that load faster
- Focused capabilities for specific tasks
- Better performance
- Can use multiple skills together when needed

**Option B - Complete System:**
Upload skill #5 only. This gives you:
- Everything in one place
- Best for comprehensive projects
- Complete system reference
- Training and teaching

**Option C - Hybrid:**
Upload the mega-skill (#5) plus one or two focused skills you'll use most.

---

## Module Architecture

### Total Modules: 47 active v4.0 modules

**Schema & Structure (15):**
- Entity schemas (9)
- Controlled vocabularies (6)

**Discovery (18):**
- Core protocol (4)
- Jurisdictional sub-procedures (8)
- Entity-specific sub-procedures (6)

**Processing (15):**
- Normalization rules (8)
- TSV output specifications (7)

**Workflow & Quality (9):**
- Workflow orchestration (5)
- Audit and baseline (2)
- Manifest and architecture (2)

**Best Practices (1):**
- Improved Discovery Methodology

---

## Quality Standards

All skills implement v4.0 quality standards:

**Discovery:**
- 95%+ geographic coverage
- 100% source documentation
- Systematic methodology

**Data Quality:**
- 100% required field completeness
- 98%+ format validation
- 98%+ vocabulary compliance
- 99%+ referential integrity

**Output:**
- 100% TSV integrity
- Complete cross-file consistency
- Full metadata preservation

---

## Use Case Examples

### County Discovery Project
**Recommended:** Mega-skill (#5) or Discovery (#1) + Schema (#2) + Normalization (#3)
- Bootstrap county project
- Execute 8-tier discovery
- Normalize and validate data
- Generate TSV outputs

### Schema Reference
**Recommended:** Schema & Vocabulary skill (#2)
- Check entity field requirements
- Validate against controlled vocabularies
- Understand entity relationships

### Data Cleaning
**Recommended:** Normalization & Output skill (#3)
- Normalize raw discovery data
- Apply vocabulary mappings
- Generate clean TSV files

### Quality Audit
**Recommended:** Processing & Quality skill (#4)
- Run quality validation
- Generate audit reports
- Establish baselines

---

## Version Information

**Version:** 4.0  
**Release Date:** February 2026  
**Status:** Production-ready  
**Compatibility:** Claude with computer use capabilities  

### Changes from v3.x
- Six-entity ontology (Sites, Trails, Segments, Networks, Access Points)
- Deprecated: Sub-Sites (now use Parent_Site_ID)
- Deprecated: Access Point Association
- New: Complete four-stage pipeline architecture
- Enhanced: Discovery methodology with lessons learned
- New: Comprehensive audit and quality control

---

## Support and Documentation

### Each Skill Includes
- SKILL.md - Main skill file with metadata and instructions
- README.md - Overview and quick reference
- references/ - Complete module documentation organized by type

### Best Practices
- Read the Improved Discovery Methodology for systematic approach
- Start with baseline research before discovery
- Use web_fetch (not just web_search) for official pages
- Document everything with full provenance
- Validate quality at each pipeline stage

### Quality Philosophy
**Completeness over Speed**
- Spending adequate time for 95%+ coverage is better than quick incomplete results
- Systematic methodology prevents missing entities
- Full documentation enables auditability

---

## File Sizes

Approximate sizes of skill ZIP files:

1. na-discovery-workflow.zip: ~500 KB
2. na-schema-vocabulary.zip: ~400 KB
3. na-normalization-output.zip: ~450 KB
4. na-processing-quality.zip: ~350 KB
5. na-complete-system.zip: ~1.2 MB

All files are well within Claude's skill size limits.

---

## Contact and Attribution

**Project:** Natural Areas Project  
**Scope:** Statewide natural areas cataloging for Ohio and beyond  
**Methodology:** Evidence-based, continuously improving  
**Version Control:** All modules versioned independently  

**Created:** February 2026  
**For:** Systematic, comprehensive natural areas discovery and data management  

---

## Quick Start

### To Begin Using These Skills

1. **Choose your approach** (modular vs. mega-skill)
2. **Upload skill(s)** to Claude via Settings → Capabilities
3. **Enable the skill(s)** after upload
4. **Test with a simple request:**
   - "What fields does a Site entity require?" (tests Schema skill)
   - "How do I discover parks in a county?" (tests Discovery skill)
   - "Set up discovery for [County Name]" (tests Complete System)

5. **Start your project:**
   - For county discovery: "Bootstrap Natural Areas Project for [County], [State]"
   - For data work: "Normalize this natural areas data"
   - For reference: "Show me the Trail schema"

---

## Skills Composability

The modular skills (1-4) are designed to work together. Claude can automatically use multiple skills in combination when needed.

Example combined usage:
- Discovery skill finds raw data
- Schema skill validates structure
- Normalization skill cleans data
- Processing skill orchestrates workflow

Or use the mega-skill (#5) which includes everything integrated.

---

**Package Complete - Ready for Upload**

Choose your skills, upload to Claude, and begin systematic natural areas discovery!
