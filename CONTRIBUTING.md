# NATURAL AREAS PROJECT — CONTRIBUTING.md (v3.2.2)
Internal contribution protocol for a two‑person, high‑discipline, ontology‑driven
system. This document defines how Skippy and Copilot maintain, update, and evolve
the Natural Areas System v3.2.2 without architectural drift.

This is not a community document.
It is an internal engineering contract.

------------------------------------------------------------
# 1. PURPOSE

This document ensures that all changes:

- Preserve the six‑entity ontology
- Preserve module boundaries
- Preserve determinism
- Preserve version integrity
- Avoid duplication of rules
- Avoid architectural drift
- Maintain full auditability

It defines how Skippy and Copilot collaborate on system evolution.

------------------------------------------------------------
# 2. CONTRIBUTORS

There are only two contributors:

- **Skippy** — system architect, domain expert, steward of ontology  
- **Copilot** — system executor, module generator, consistency enforcer  

No other contributors exist or will exist.

------------------------------------------------------------
# 3. HOW WE MAKE CHANGES

All changes follow this sequence:

1. **Identify the correct module**  
   - Never place a rule in more than one module  
   - Never place a rule in the wrong module  

2. **State the change explicitly**  
   Example: “We need to update the Trail Segment Identity Rule because X.”

3. **Copilot generates the updated module**  
   - Always as a full replacement  
   - Never as a diff  

4. **Skippy reviews for correctness**  
   Checks for:  
   - Ontological alignment  
   - Boundary correctness  
   - No duplication  
   - No drift  

5. **Skippy pastes the updated module into the repo**  
   Copilot never edits files directly.

6. **Increment the module version**  
   - **Major** = breaking change  
   - **Minor** = new rules, clarifications, expansions  
   - **Patch** = formatting or typo  

7. **Update the manifest**  
   Required if filenames or module counts change.

------------------------------------------------------------
# 4. EDITING RULES

These rules prevent cascading breakage:

- Never invent data  
- Never add rules to multiple modules  
- Never change TSV field order  
- Never change delimiter rules  
- Never change discovery output structure without updating:  
  - Discovery Output Spec  
  - Discovery Metadata Spec  
  - All discovery sub‑procedures  
- Never change schema fields without updating: 
  - Schema  
  - Normalization  
  - TSV Output Spec  
  - Integrity Check  
  - Vocabulary (if the field is vocabulary‑governed)
- Never change vocabulary values without updating:  
  - Vocabulary Module  
  - Normalization Contract  

------------------------------------------------------------
# 5. TESTING CHANGES

After any change, we verify:

- Discovery still produces valid raw candidates  
- Resolution still classifies correctly  
- All six normalization contracts align with schema  
- TSV outputs match specs  
- Delimiter integrity passes  
- Audit logs capture all decisions  
- Manifest reflects reality  

If any check fails, the change is incomplete.

------------------------------------------------------------
# 6. FORBIDDEN CHANGES

These are absolute:

- No invented data  
- No silent corrections  
- No silent exclusions  
- No cross‑module duplication  
- No adding new entity types without architectural review  
- No modifying discovery tier order without updating the protocol  
- No modifying schema field order without updating TSV specs  

------------------------------------------------------------
# 7. HOW WE COMMUNICATE CHANGES

We keep it simple:

- **Skippy:** “We need to update X.”  
- **Copilot:** Generates the full updated module.  
- **Skippy:** Reviews and pastes.  

No PRs, no branches, no ceremony — just disciplined, explicit collaboration.

------------------------------------------------------------
# 8. VERSIONING

Every module is versioned independently.

- **Major** — breaking change  
- **Minor** — new rules or clarifications  
- **Patch** — formatting or non‑semantic edits  

The manifest must always reflect current versions.

------------------------------------------------------------
# 9. PHILOSOPHY

This project is built on:

- Determinism  
- Transparency  
- Ontological rigor  
- Zero improvisation  
- Zero duplication  
- Zero drift  
- Explicit reasoning  
- Document‑driven architecture  

This CONTRIBUTING.md exists to protect those principles.

------------------------------------------------------------
# END OF CONTRIBUTING.md v3.2.2