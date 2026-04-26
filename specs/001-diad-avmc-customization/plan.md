# Implementation Plan: DIAD AvMC Customization

**Branch**: `001-diad-avmc-customization` | **Date**: 2026-04-26 | **Spec**: N/A (derived from constitution + outline)
**Input**: Constitution v1.0.0 + rough outline from initial conversation

## Summary

Customize the Microsoft "Dashboard in a Day" (DIAD) training content for the
U.S. Army DEVCOM Aviation & Missile Center (AvMC) audience. Replace the
fictional VanArsdel consumer-products scenario with a defense engineering
scenario (aviation/missile platform sustainment), swap branding assets, generate
synthetic domain-relevant datasets, and rebuild all Power BI solution files
while preserving the original lab sequence and pedagogical structure.

## Technical Context

**Language/Version**: Python 3.11+ (data generation scripts only)
**Primary Dependencies**: Power BI Desktop (current release), python-pptx (PPTX editing), Faker/random (synthetic data generation)
**Storage**: CSV flat files (matching original DIAD schema)
**Testing**: Manual validation — open each .pbix, verify visuals load without errors
**Target Platform**: Windows (Power BI Desktop), Power BI Service (cloud)
**Project Type**: Content/training-material customization (not a software application)
**Performance Goals**: Synthetic CSVs must load in Power BI Desktop within ~60 seconds (comparable to originals)
**Constraints**: All content unclassified/NIPRNet-safe; no CUI, FOUO, PII, or real program data
**Scale/Scope**: 8 .pbix files, 1 .pptx, 7 CSV data files, 2 image assets, 1 theme JSON, 5 PDF scripts

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| # | Principle | Status | Notes |
|---|-----------|--------|-------|
| I | Audience-First Design | ✅ PASS | Scenario reframed for AvMC engineers/PMs; defense domain language throughout |
| II | Data Fidelity with Synthetic Safety | ✅ PASS | All data will be generated synthetically; schema contract preserved from originals |
| III | Preserve Pedagogical Structure | ✅ PASS | Labs 1–5, Final Report, optional demos all retained; no new Power BI concepts added |
| IV | Visual & Brand Consistency | ✅ PASS | Army color palette, AvMC logo, defense-themed background planned |
| V | Traceability of Changes | ✅ PASS | Change log deliverable included; directory layout mirrors original DIAD |

**Gate result: PASS** — no violations; proceeding to Phase 0.

## Project Structure

### Documentation (this feature)

```text
specs/001-diad-avmc-customization/
├── plan.md              # This file
├── research.md          # Phase 0: domain research, color codes, schema mapping
├── data-model.md        # Phase 1: synthetic data schema definitions
├── quickstart.md        # Phase 1: how to rebuild .pbix files from new data
├── contracts/           # Phase 1: CSV schema contracts
└── tasks.md             # Phase 2: ordered implementation tasks
```

### Content (repository root — mirrors original DIAD layout)

```text
Instructor/
├── Data/
│   ├── Background.jpg              # REPLACE: defense-themed background
│   ├── VanArsdel_Logo.png          # REPLACE: DEVCOM AvMC logo → AvMC_Logo.png
│   ├── playAxis.*.pbiviz           # KEEP as-is
│   ├── Theme/
│   │   └── DIADTheme2.json         # UPDATE: Army-branded color palette
│   ├── USSales/
│   │   └── Sales.csv               # REPLACE: synthetic platform sustainment data
│   └── InternationalSales/
│       ├── Australia.csv            # REPLACE: allied nation FMS support data
│       ├── Canada.csv               # REPLACE
│       ├── Germany.csv              # REPLACE
│       ├── Japan.csv                # REPLACE
│       ├── Mexico.csv               # REPLACE
│       └── SouthKorea.csv           # REPLACE
├── Reports/
│   ├── Lab 1 solution.pbix          # REBUILD against new data
│   ├── Lab 2 solution.pbix          # REBUILD
│   ├── Lab 3 solution.pbix          # REBUILD
│   ├── Lab 4 solution.pbix          # REBUILD
│   ├── Lab 5 solution.pbix          # REBUILD
│   └── DIAD Final Report.pbix       # REBUILD
├── Trainer Material/
│   ├── Dashboard in a Day.pptx      # UPDATE: re-theme slides, swap scenario language
│   ├── DIAD Demo Script - PowerBI Desktop.pdf  # UPDATE: defense scenario narration
│   ├── DIAD Change Log.pdf          # UPDATE: add AvMC customization entries
│   ├── Teams for Power BI Demo.pdf  # KEEP as-is (tool-generic)
│   └── Optional Demos/
│       ├── DIAD Final Report with RLS.pbix     # REBUILD
│       ├── Social.pbix                          # KEEP or light rebrand
│       ├── Optional DIAD Demo Script - *.pdf    # UPDATE if VanArsdel refs found
│       └── ...
└── scripts/                          # NEW: data generation scripts
    └── generate_synthetic_data.py    # Python script to produce all CSVs
```

**Structure Decision**: Mirror the existing `Instructor/` directory layout exactly
(per Constitution Principle V: Traceability). Add one new `scripts/` directory
for the data generation tooling.

## Complexity Tracking

> No constitution violations — table not needed.
