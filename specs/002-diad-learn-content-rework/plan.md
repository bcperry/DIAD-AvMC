# Implementation Plan: DIAD Learn-Content Rework

**Branch**: `002-diad-learn-content-rework` | **Date**: 2026-04-26 | **Spec**: N/A (requirements captured in constitution + research)
**Input**: Constitution + Research from `/specs/002-diad-learn-content-rework/`; completed data/branding from spec 001

## Summary

Rework the `Instructor/diad-learn-content/dashboard-in-a-day.md` to match the AvMC R&D engineering workload scenario established in spec 001. Replace all VanArsdel consumer-product references with DEVCOM AvMC terminology (Programs, Labs, Directorates, LaborHours, ResearchTasks) while preserving the original DIAD instructional flow module-by-module.

## Technical Context

**Language/Version**: Python 3.11+ (data generation scripts only) + Power BI Desktop (current release)  
**Primary Dependencies**: Faker (synthetic data), python-pptx (PPTX editing), pbi-tools / pbi-tools-core (PBIX extract/compile)  
**Storage**: CSV files + Excel (.xlsx) for Power BI data sources  
**Testing**: Manual validation (row counts, header checks, visual inspection of .pbix)  
**Target Platform**: Windows (Power BI Desktop requirement)  
**Project Type**: Content/data customization pipeline  
**Performance Goals**: N/A  
**Constraints**: All data must be synthetic (no CUI/FOUO/PII); preserve original DIAD lab structure  
**Scale/Scope**: ~4.2M US rows + ~3M international rows across 7 CSV files; 8 .pbix solution files; 1 markdown learn-content file

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Status | Notes |
|-----------|--------|-------|
| I. Audience-First Design | ✅ PASS | All entities use AvMC R&D terminology (Programs, Labs, Directorates, LaborHours, ResearchTasks) |
| II. Data Fidelity with Synthetic Safety | ✅ PASS | 100% synthetic; column count/types preserved from original DIAD schema |
| III. Preserve Pedagogical Structure | ✅ PASS | Same lab sequence (1–5 + Final); only cosmetic/narrative changes |
| IV. Visual & Brand Consistency | ✅ PASS | Army Gold/Green/Black palette; DEVCOM AvMC logo; unified theme JSON |
| V. Traceability of Changes | ✅ PASS | Token replacement table in rebuild script; research.md documents all mapping decisions |

## Project Structure

### Documentation (this feature)

```text
specs/002-diad-learn-content-rework/
├── plan.md              # This file
├── research.md          # Phase 0: schema mapping, entity research (carried from spec 001)
├── data-model.md        # Phase 1: entity definitions, star schema (carried from spec 001)
├── quickstart.md        # Phase 1: step-by-step guide
├── contracts/
│   └── csv-schemas.md   # Phase 1: CSV format contracts (carried from spec 001)
└── tasks.md             # Phase 2: implementation task breakdown
```

### Source Code (repository root)

```text
Instructor/
├── Data/
│   ├── USEngineering/
│   │   ├── RDWorkload.csv          # ~4.2M rows (ProgramID,Date,LabCode,ResearchTasks,LaborHours)
│   │   └── bi_dimensions.xlsx      # Program, Directorate, Lab dimension sheets
│   ├── InternationalPrograms/
│   │   ├── Australia.csv           # ~1.99M rows (+ Country column)
│   │   ├── Canada.csv              # ~46K rows
│   │   ├── Germany.csv             # ~138K rows
│   │   ├── Japan.csv               # ~527K rows
│   │   ├── Mexico.csv              # ~129K rows
│   │   └── SouthKorea.csv          # ~205K rows
│   ├── Theme/
│   │   └── DIADTheme2.json         # Army-branded 15-color palette
│   ├── AvMC_Logo.png               # DEVCOM AvMC logo (~979×122px)
│   └── Background.jpg              # Defense-themed background (1280×720)
├── diad-learn-content/
│   └── dashboard-in-a-day.md       # Reworked DIAD learn-content (this planning cycle)
├── scripts/
│   ├── generate_synthetic_data.py  # CSV fact data + dimensions
│   ├── rebuild_powerbi_sources.py  # extract/patch/compile pipeline for .pbix
│   ├── create_brand_assets.py      # Logo + background image generation
│   ├── merge_diad_content.py       # Scrape consolidation
│   └── scrape_diad_learn.py        # Original content scraper
├── Reports/                        # 6 .pbix solution files (Labs 1–5 + Final)
└── Trainer Material/
    └── Optional Demos/             # 2 additional .pbix files (RLS, Social)
```

**Structure Decision**: Flat Instructor/ layout matching original DIAD directory structure per Constitution Principle V (traceability).

## Naming Convention Summary

The actual generated data uses the following naming (Option C from implementation):

| Original DIAD | AvMC Version | Context |
|---------------|-------------|---------|
| Sales (table) | RDWorkload | Fact table |
| Product (table) | Program | Dimension: R&D programs |
| Manufacturer (table) | Directorate | Dimension: Army organizations |
| Geography (table) | Lab | Dimension: test/research facilities |
| ProductID | ProgramID | FK to Program dimension |
| Zip | LabCode | FK to Lab dimension (real zip codes) |
| Units | ResearchTasks | Count metric |
| Revenue | LaborHours | Continuous metric (hours) |
| USSales/ | USEngineering/ | Folder name |
| InternationalSales/ | InternationalPrograms/ | Folder name |
| Sales.csv | RDWorkload.csv | US fact file |
| VanArsdel | DEVCOM AvMC | "Our" organization |
| Top Competitors | Partner Organizations | Grouped comparison |

## Complexity Tracking

> No constitution violations requiring justification.

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| [e.g., 4th project] | [current need] | [why 3 projects insufficient] |
| [e.g., Repository pattern] | [specific problem] | [why direct DB access insufficient] |
