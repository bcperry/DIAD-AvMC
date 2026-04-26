# Tasks: DIAD AvMC Customization

**Input**: Design documents from `/specs/001-diad-avmc-customization/`
**Prerequisites**: plan.md (required), research.md, data-model.md, contracts/csv-schemas.md, quickstart.md

**Tests**: Not requested — no test tasks included.

**Organization**: Tasks are grouped by user story (derived from plan.md deliverables). Each story can be validated independently.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (US1–US4)
- Exact file paths included in descriptions

## User Stories (derived from plan.md)

| Story | Title | Priority | Description |
|-------|-------|----------|-------------|
| US1 | Generate Synthetic Data | P1 | Python script producing 7 CSV files per contracts |
| US2 | Apply Army Branding | P1 | Theme JSON, logo, background image |
| US3 | Rebuild Power BI Solutions | P2 | 8 .pbix files against new data/branding |
| US4 | Update Trainer Materials | P3 | PowerPoint deck, PDF demo scripts |

---

## Phase 1: Setup

**Purpose**: Create project scaffolding for data generation tooling

- [X] T001 Create `Instructor/scripts/` directory, initialize a `pyproject.toml` at repo root with Python >=3.11 requirement and dependencies (Faker), then run `uv sync` to create the virtual environment. Initialize `Instructor/scripts/generate_synthetic_data.py` with imports (csv, random, datetime, os, pathlib, faker) and output path constants pointing to `Instructor/Data/`. Use `uv run` to execute scripts. Do NOT use pip.

---

## Phase 2: Foundational (Data Generation Script)

**Purpose**: Build the synthetic data generator that ALL downstream work depends on

**⚠️ CRITICAL**: No branding, .pbix, or trainer material work can begin until CSVs are generated

- [X] T002 Define Platform reference data (14 platforms from research.md R2 table: IDs 1001–1005 helicopters, 2001–2007 missiles, 3001–3002 UAS) as a list of dicts in `Instructor/scripts/generate_synthetic_data.py`. Include per-platform weight factors so high-volume platforms (Black Hawk, Apache, Chinook) generate more rows than niche systems (Little Bird, Shadow). Include a typical WorkOrders range and mean EngineeringHours per platform so helicopters trend higher hours than missiles.
- [X] T003 Define Installation reference data (12 installations from research.md R2 table with zip codes: 35808, 78419, 17201, 36362, 96859, 98433, 31314, 42223, 79916, 10996, 28307, 80913) in `Instructor/scripts/generate_synthetic_data.py`. Assign relative activity weights — Redstone Arsenal and Corpus Christi (depot-level) should dominate volume; field installations like Fort Campbell and Fort Stewart get moderate traffic; West Point gets minimal.
- [X] T004 Define FMS country configuration (6 countries with row targets from Contract 2: Australia ~1,992,000, Japan ~527,000, SouthKorea ~205,000, Germany ~138,000, Mexico ~129,000, Canada ~46,000) in `Instructor/scripts/generate_synthetic_data.py`. Map a subset of platforms to each country reflecting real FMS relationships (e.g., Australia gets Apache/Chinook/Javelin; Japan gets Apache/Patriot/THAAD; Canada gets Chinook only).
- [X] T005 Implement `generate_us_sales()` function producing ~4,200,000 rows per Contract 1 (columns: PlatformID, Date, InstallationCode, WorkOrders, EngineeringHours; date range 2021-01-01 to 2025-12-31; WorkOrders 1–50; EngineeringHours 50.00–5000.00 with 6 decimal places) in `Instructor/scripts/generate_synthetic_data.py`. Distribution requirements: (a) weight platform selection by platform activity factors, (b) weight installation selection by installation activity factors, (c) correlate EngineeringHours with WorkOrders (more orders → more hours, with some noise), (d) add slight year-over-year upward trend (~3–5% annual growth) to make time-series charts interesting, (e) add seasonal variation (higher activity in Q1/Q3 fiscal year), (f) use seeded random for reproducibility.
- [X] T006 Implement `generate_international_sales()` function producing 6 country CSV files per Contract 2 (same columns + Country; per-file row counts matching targets; date range 2021-01-01 to 2025-12-31) in `Instructor/scripts/generate_synthetic_data.py`. Distribution requirements: (a) each country only generates rows for its mapped platform subset from T004, (b) correlate EngineeringHours with WorkOrders as in T005, (c) vary volume patterns by country (e.g., Australia steady growth, SouthKorea ramp-up in later years reflecting newer FMS deals), (d) use seeded random for reproducibility.
- [X] T007 Implement CLI entry point with `__main__` block: call both generators, write CSVs with UTF-8 encoding and CRLF line endings, print summary of row counts per file in `Instructor/scripts/generate_synthetic_data.py`
- [X] T008 Run `uv run Instructor/scripts/generate_synthetic_data.py` and validate all 7 CSVs: verify headers match contracts, row counts within 5% of targets, decimal precision is 6 places, line endings are CRLF, files written to correct paths under `Instructor/Data/`. Do NOT use pip.

**Checkpoint**: All 7 CSV files exist and match contract specifications. Downstream work can begin.

---

## Phase 3: User Story 1 — Apply Army Branding (Priority: P1)

**Goal**: Replace all VanArsdel branding assets with DEVCOM AvMC Army-themed equivalents

**Independent Test**: Open DIADTheme2.json and verify 15 Army colors; confirm logo and background exist at correct dimensions

### Implementation for User Story 1

- [X] T009 [P] [US1] Replace contents of `Instructor/Data/Theme/DIADTheme2.json` with the 15-color Army palette from Contract 3 (name: "DEVCOM AvMC Theme", lead colors: #C1A875 Gold, #4B5320 Green, #2D2926 Black)
- [X] T010 [P] [US1] Create `Instructor/Data/AvMC_Logo.png` with `uv run Instructor/scripts/create_brand_assets.py` — DEVCOM AvMC text-based logo placeholder, ~979×122px RGBA PNG, using Army Gold (#C1A875) text on transparent background per Contract 4
- [X] T011 [P] [US1] Replace `Instructor/Data/Background.jpg` with `uv run Instructor/scripts/create_brand_assets.py` — defense/engineering-themed background image, 1280×720px JPEG, dark tones compatible with light-colored chart overlays per Contract 4

**Checkpoint**: Theme JSON updated, logo created, background replaced. Ready for .pbix rebuilds.

---

## Phase 4: User Story 2 — Rebuild Power BI Solutions (Priority: P2)

**Goal**: Reconnect all .pbix solution files to new CSV data, apply Army theme, swap branding assets, rename measures/columns

**Independent Test**: Open each .pbix in Power BI Desktop — all queries load without errors, visuals render with Army colors, no "VanArsdel" text visible

**Dependencies**: Requires Phase 2 (CSVs exist) and US1 (branding assets exist)

### Implementation for User Story 2

- [ ] T012 [P] [US2] Rebuild `Instructor/Reports/Lab 1 solution.pbix` — open in Power BI Desktop, update data source to new Sales.csv, rename ProductID→PlatformID / Zip→InstallationCode / Units→WorkOrders / Revenue→EngineeringHours in Power Query, apply DIADTheme2.json theme, replace VanArsdel logo with AvMC_Logo.png, update visual titles
- [ ] T013 [P] [US2] Rebuild `Instructor/Reports/Lab 2 solution.pbix` — reconnect US + International data sources, verify folder-based import picks up SouthKorea.csv (renamed from Nigeria.csv), rename columns in Power Query, apply theme, swap branding assets, update visual titles
- [ ] T014 [P] [US2] Rebuild `Instructor/Reports/Lab 3 solution.pbix` — reconnect data sources, rename columns, update all DAX measures (replace Revenue references with EngineeringHours, Units with WorkOrders), apply theme, swap branding assets
- [ ] T015 [P] [US2] Rebuild `Instructor/Reports/Lab 4 solution.pbix` — reconnect data sources, rename columns, apply theme, replace logo/background images on all report pages, update chart titles and KPI labels
- [ ] T016 [P] [US2] Rebuild `Instructor/Reports/Lab 5 solution.pbix` — reconnect data sources, rename columns, apply theme, swap branding, update any workspace/app name references in the report
- [ ] T017 [P] [US2] Rebuild `Instructor/Reports/DIAD Final Report.pbix` — reconnect all data sources, rename columns, update all DAX measures, apply theme, replace logo/background on all pages, update executive summary titles and KPIs
- [ ] T018 [P] [US2] Rebuild `Instructor/Trainer Material/Optional Demos/DIAD Final Report with RLS.pbix` — reconnect data sources, rename columns, apply theme, swap branding, verify Row-Level Security roles still function with new column names
- [ ] T019 [US2] Review `Instructor/Trainer Material/Optional Demos/Social.pbix` for VanArsdel references — light rebrand if references found, otherwise keep as-is

**Checkpoint**: All 8 .pbix files open cleanly, display Army-branded visuals, and show no VanArsdel references.

---

## Phase 5: User Story 3 — Update Trainer Materials (Priority: P3)

**Goal**: Update the PowerPoint deck and PDF demo scripts to reflect the AvMC defense scenario

**Independent Test**: Open .pptx and search for "VanArsdel" — zero results; scenario language references AvMC platforms and sustainment

**Dependencies**: Requires US2 complete (updated .pbix screenshots needed for PowerPoint)

### Implementation for User Story 3

- [ ] T020 [US3] Update `Instructor/Trainer Material/Dashboard in a Day.pptx` using python-pptx — find/replace "VanArsdel" → "DEVCOM AvMC" across all slides, replace scenario narrative (consumer products → defense platform sustainment), swap company logo images, update data field references (Revenue → Engineering Hours, Units → Work Orders, Product → Platform, Zip → Installation)
- [ ] T021 [P] [US3] Update `Instructor/Trainer Material/DIAD Demo Script - PowerBI Desktop.pdf` — replace VanArsdel scenario language with AvMC defense narrative, update column/measure name references throughout
- [ ] T022 [P] [US3] Update `Instructor/Trainer Material/Optional Demos/Optional DIAD Demo Script - PowerBI Desktop.pdf` — replace VanArsdel references with AvMC equivalents
- [ ] T023 [P] [US3] Update `Instructor/Trainer Material/Optional Demos/Optional DIAD Demo Script - Power BI Service.pdf` — replace VanArsdel references with AvMC equivalents
- [ ] T024 [P] [US3] Update `Instructor/Trainer Material/Optional Demos/Optional DIAD Demo Script - Copilot in Power BI.pdf` — replace VanArsdel references with AvMC equivalents
- [ ] T025 [P] [US3] Update `Instructor/Trainer Material/DIAD Change Log.pdf` — add entry documenting AvMC customization (date, scope of changes, version)
- [ ] T026 [US3] Keep `Instructor/Trainer Material/Teams for Power BI Demo.pdf` as-is — tool-generic content, no VanArsdel references expected (verify and confirm)

**Checkpoint**: All trainer materials reference AvMC scenario. No VanArsdel text in any deliverable.

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Final validation and cleanup across all deliverables

- [ ] T027 Search all deliverables for residual "VanArsdel" text — grep across CSV headers, JSON, .pptx (via python-pptx), and any text-extractable files; fix any remaining references
- [ ] T028 Validate CSV row counts match contract targets (US Sales ~4.2M, Australia ~1.99M, Japan ~527K, SouthKorea ~205K, Germany ~138K, Mexico ~129K, Canada ~46K)
- [ ] T029 Run end-to-end validation per `specs/001-diad-avmc-customization/quickstart.md` checklist: all 8 .pbix open without errors, theme renders correctly, logo displays, PowerPoint narration matches scenario
- [ ] T030 Remove `Instructor/Data/VanArsdel_Logo.png` (replaced by `Instructor/Data/AvMC_Logo.png`)

---

## Dependencies & Execution Order

### Phase Dependencies

```
Phase 1: Setup ──────────────────────────────────────────► (no deps)
Phase 2: Foundational (Data Gen) ───────────────────────► depends on Phase 1
Phase 3: US1 Branding ─────────────────────────────────► can start after Phase 1 (parallel with Phase 2)
Phase 4: US2 Power BI Rebuilds ────────────────────────► depends on Phase 2 AND Phase 3
Phase 5: US3 Trainer Materials ────────────────────────► depends on Phase 4 (needs .pbix screenshots)
Phase 6: Polish ───────────────────────────────────────► depends on all above
```

### User Story Dependencies

- **US1 (P1 — Branding)**: Can start after Phase 1 Setup — independent of data generation
- **US2 (P2 — .pbix Rebuilds)**: Requires BOTH Foundational (CSVs) AND US1 (branding assets)
- **US3 (P3 — Trainer Materials)**: Requires US2 (updated .pbix files for screenshots)

### Within Each User Story

- All US1 branding tasks (T009–T011) can run in parallel — different files
- All US2 .pbix tasks (T012–T018) can run in parallel — different files
- US3 PowerPoint (T020) should complete first; PDF updates (T021–T026) can run in parallel

### Parallel Opportunities

```
PARALLEL GROUP A (after Phase 1):
  ├── Phase 2: T002 → T003 → T004 → T005 → T006 → T007 → T008
  └── Phase 3: T009 ║ T010 ║ T011

PARALLEL GROUP B (after Phase 2 + Phase 3):
  └── Phase 4: T012 ║ T013 ║ T014 ║ T015 ║ T016 ║ T017 ║ T018 → T019

PARALLEL GROUP C (after Phase 4):
  └── Phase 5: T020 → (T021 ║ T022 ║ T023 ║ T024 ║ T025 ║ T026)
```

---

## Parallel Example: Data Generation (Phase 2)

```bash
# Sequential — single file development:
Task T002: Define Platform reference data in generate_synthetic_data.py
Task T003: Define Installation reference data in generate_synthetic_data.py
Task T004: Define FMS country config in generate_synthetic_data.py
Task T005: Implement US Sales generator in generate_synthetic_data.py
Task T006: Implement International generator in generate_synthetic_data.py
Task T007: Add CLI entry point in generate_synthetic_data.py
Task T008: Run and validate outputs
```

## Parallel Example: Power BI Rebuilds (Phase 4)

```bash
# All .pbix files can be rebuilt in parallel (different files):
Task T012: Lab 1 solution.pbix
Task T013: Lab 2 solution.pbix
Task T014: Lab 3 solution.pbix
Task T015: Lab 4 solution.pbix
Task T016: Lab 5 solution.pbix
Task T017: DIAD Final Report.pbix
Task T018: DIAD Final Report with RLS.pbix
```

---

## Implementation Strategy

### MVP First (Data + Branding + Lab 1 only)

1. Complete Phase 1: Setup (T001)
2. Complete Phase 2: Foundational — generate all CSVs (T002–T008)
3. Complete Phase 3: Branding assets (T009–T011)
4. Rebuild Lab 1 only (T012) as proof-of-concept
5. **STOP and VALIDATE**: Verify Lab 1 loads with new data and Army branding
6. Proceed with remaining .pbix files

### Incremental Delivery

1. Setup + Data Generation → CSVs validated ✓
2. Branding → Theme + logo + background ready ✓
3. Power BI Rebuilds → All 8 .pbix files validated ✓
4. Trainer Materials → PowerPoint + PDFs updated ✓
5. Polish → Final sweep, cleanup, full validation ✓

### Single-Developer Execution Order

For a solo workflow (most likely scenario):

1. T001 → T002–T008 (build and validate data generator with uv)
2. T009–T011 (create branding assets in parallel)
3. T012 (rebuild Lab 1 as proof-of-concept, validate pattern)
4. T013–T018, T019 (apply same pattern to remaining .pbix files)
5. T020–T026 (update trainer materials)
6. T027–T030 (final validation and cleanup)

---

## Notes

- **PDF editing**: PDF files (T021–T026) may require manual editing or recreation if source .docx files are unavailable. Consider converting to a text-editable format first.
- **.pbix files**: Binary format — must be edited interactively in Power BI Desktop. Tasks describe what to change; execution is manual.
- **python-pptx**: Can automate text replacement in .pptx but may struggle with embedded images. Plan for manual image swaps in PowerPoint.
- **Row counts**: Generator should use seeded random for reproducibility. Exact counts will vary; target ±5% of contract values.
- Commit after each phase completion.
