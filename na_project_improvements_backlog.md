# Natural Areas Project — Improvements & Tests Backlog
# Updated: 2026-05-07
# All Priority 1–4 items from the original 2026-05-02 backlog are complete.
# This file now tracks newly identified open items.

---

## OPEN ITEMS

### Copilot Hybrid Workflow Evaluation (IMP-092 — open)
Test whether Copilot can handle web-research-heavy discovery tier work
while Claude handles YAML writing and vocabulary enforcement.
- Test plan: one complete tier (Tier 2 or Tier 3) for a new county
- Evaluate: protocol adherence, session discipline, handoff friction
- Status: open — requires a manual test run

---

## COMPLETED (2026-05-07)

- [x] IMP-104: Cross-county resolution protocol — new module `na_cross_county_resolution_v5.1.md`;
  MC ID scheme (MC-T-0001, MC-TN-0001, etc.); three scenarios (Held/Collision/Known);
  bootstrap DB check; discovery CROSS_COUNTY_CANDIDATE flagging; Resolution Engine Phase 0;
  DB migration: MC-T-0001 (Maumee River Water Trail, 4 records merged), MC-T-0002
  (Wabash Cannonball Trail, 3 records merged); 7 deprecated IDs; held_entities cleaned
- [x] IMP-103: Water trail discovery sub-procedure — new consolidated module
  (na_water_trail_discovery_subproc.md); entity typing, qualification
  threshold, Trail Segment triggers, economy-of-scale GPS workflow, AP rules
- [x] IMP-102: Trail Network and Site Network normalization hardening —
  enforcement-grade vocabulary mapping tables (na_trail_network_vocabulary v5.2,
  na_trail_network_normalization v5.2, na_site_network_vocabulary v5.3,
  na_site_network_normalization v5.2, live DB remediation 6 records)
- [x] IMP-100: Trail and AP normalization hardening — enforcement-grade
  vocabulary mapping tables (na_trail_vocabulary v5.2, na_trail_normalization
  v5.3, na_access_point_normalization v5.2, live DB remediation)
- [x] IMP-101: Pre-run DB integrity check (PRAGMA integrity_check +
  foreign_key_check in na_run_county.py); run_metadata.state normalization
  guard; live DB fix (4 "OH" → "Ohio")
- [x] Skills changelog backfilled for IMP-088, IMP-096, IMP-097, IMP-099

## COMPLETED (2026-05-04 / 2026-05-05)

- [x] IMP-088: PAD-US Completeness Gate
- [x] IMP-089: YAML sanitizer (na_yaml_preprocess.py)
- [x] IMP-090: na_generate_config.py scaffolding tool
- [x] IMP-091: Monolithic county pipeline scripts deprecated
- [x] IMP-093: Stage numbering audit — na_processing_orchestration v5.5
- [x] IMP-094: Parameterized pipeline model (na_run_county.py + JSON config)
- [x] IMP-095: Skill file architecture overhaul
- [x] IMP-096: Ohio Township Officials roster as Tier 5 authority
- [x] IMP-097: Parks & Open Space GIS layer completeness gate
- [x] IMP-098: MORPC centroids relocated to Franklin County folder
- [x] IMP-099: Cemeteries and golf courses formally in scope — all tiers
