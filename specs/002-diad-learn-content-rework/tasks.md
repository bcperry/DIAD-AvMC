# Tasks: DIAD Learn-Content Rework

**Input**: Design documents from `/specs/002-diad-learn-content-rework/`
**Prerequisites**: plan.md (required), research.md, data-model.md, contracts/csv-schemas.md

**Tests**: Not requested — no test tasks included.

**Organization**: Tasks are grouped by module (matching the original DIAD structure) so each module can be edited and reviewed independently. The file being edited is a single markdown file (`Instructor/diad-learn-content/dashboard-in-a-day.md`), but each module section is a logically independent unit of work.

## Verification Rule

**AFTER every task**: Re-read the edited section in full. Confirm that:
1. The **instructional flow** still makes sense — steps build on each other logically, screenshots/references still align with the surrounding context.
2. The **pedagogical intent** is preserved — the learner is still practicing the same Power BI skill (e.g., appending queries, creating relationships, writing DAX) even though the domain vocabulary changed.
3. No **orphaned references** remain — a renamed term in one sentence didn't leave a stale original term two sentences later.
4. The **tone and voice** stay consistent with the rest of the training material (second-person instructional, concise steps).

If a section reads awkwardly after a terminology swap, rewrite the surrounding sentence for natural flow rather than doing a mechanical find-replace.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different sections, no dependencies)
- **[Story]**: Which user story this task belongs to (US1–US5)
- Exact file paths and line ranges included in descriptions

## User Stories (derived from plan.md)

| Story | Title | Priority | Description |
|-------|-------|----------|-------------|
| US1 | Module 1 + Header Rework | P1 | Update title, intro scenario, course file instructions |
| US2 | Module 2 Rework (Data Import & Prep) | P1 | Heaviest edit — all data paths, column names, table names, scenario text |
| US3 | Module 3 Rework (Data Model & Viz) | P1 | Table/column references, DAX expressions, relationship instructions |
| US4 | Module 4 Rework (Hierarchies & DAX) | P2 | Hierarchy names, DAX measures, scenario narrative |
| US5 | Module 5 Rework (Viz & Reports) | P2 | Chart labels, slicer references, theme/branding instructions |

---

## Phase 1: Setup

**Purpose**: Prepare for the learn-content rework by documenting the complete replacement mapping

- [X] T001 Create a working reference comment block at the top of `Instructor/diad-learn-content/dashboard-in-a-day.md` (temporary, removed in Polish phase) listing all find→replace pairs derived from the plan.md Naming Convention Summary. This ensures consistent terminology across all module edits. Key mappings: VanArsdel→DEVCOM AvMC, Sales→RDWorkload, Product→Program, Manufacturer→Directorate, Geography→Lab, Revenue→LaborHours, Units→ResearchTasks, ProductID→ProgramID, Zip→LabCode, ZipCountry→LabCodeCountry, USSales→USEngineering, InternationalSales→InternationalPrograms, Sales.csv→RDWorkload.csv, Nigeria→South Korea, bi_dimensions.xlsx sheets (geo→lab, manufacturer→directorate, Product_Table→Product_Table preserved as Excel sheet name).

---

## Phase 2: Foundational — Header & Module 1 (Blocking)

**Purpose**: Update the document header and Module 1 (Introduction/Prerequisites) which sets the scenario context for all subsequent modules

**⚠️ CRITICAL**: The scenario introduction in Module 1 frames the entire document — must be done first

- [X] T002 [US1] Update document title and header (line 1) in `Instructor/diad-learn-content/dashboard-in-a-day.md` — change from generic "Dashboard in a Day" framing to include AvMC context. Update the source URL comment to note this is an AvMC-customized version of the original Microsoft Learn content.
- [X] T003 [US1] Rewrite the scenario introduction paragraph (around line 111) in `Instructor/diad-learn-content/dashboard-in-a-day.md` — replace "The company VanArsdel, Ltd. manufactures expensive retail products that can be used for fun and work. This company sells their products directly to consumers nationwide and in several other countries." with DEVCOM AvMC R&D engineering workload scenario: DEVCOM AvMC manages aviation and missile technology development across multiple R&D programs, tracking engineering labor hours and research tasks at labs nationwide and with allied partner nations.
- [X] T004 [US1] Update the "Unzip the course files" section (around lines 91–117) in `Instructor/diad-learn-content/dashboard-in-a-day.md` — replace `C:\DIAD` references with the AvMC course folder path. Update "Your `C:\DIAD\` directory should now have the folders **Data** and **Reports**" and the dataset description. Replace "CMO" role with appropriate AvMC role (e.g., "Chief Engineer" or "Technology Director"). Replace Nigeria data note with South Korea note.
- [X] T005 [US1] Update Module 2 introduction section (around lines 129–153) in `Instructor/diad-learn-content/dashboard-in-a-day.md` — replace "Import VanArsdel, Ltd. USA sales data" and competitor references with AvMC equivalents. Update the four bullet learning objectives to reference R&D workload data, programs, and lab locations instead of sales data.

**Checkpoint**: Scenario context is established. All subsequent module edits can reference the AvMC framing.
**Verify**: Re-read the full header through Module 1. Confirm the intro scenario, course-file instructions, and learning objectives read naturally as a cohesive AvMC training narrative — not a patched VanArsdel doc.

---

## Phase 3: User Story 2 — Module 2 Data Import & Preparation (Priority: P1)

**Goal**: Rework Module 2 (the heaviest edit) to reference all new data paths, column names, table names, and folder structures

**Independent Test**: Read through Module 2 and verify zero references to Sales.csv, USSales, InternationalSales, ProductID, Zip (as column), Units, Revenue (as column), bi_dimensions, geo, manufacturer (as table name), Nigeria, or VanArsdel

### Implementation for User Story 2

- [X] T006 [US2] Update "Exercise - Load data from various sources" dataset description (around line 157) in `Instructor/diad-learn-content/dashboard-in-a-day.md` — replace "sales data from VanArsdel, Ltd. and other competitors...seven years of transaction data by day, product, and zip code for each manufacturer...seven countries" with AvMC R&D workload description: five years of engineering data by day, program, and lab code for each directorate across six partner nations.
- [X] T007 [US2] Update data path references (around lines 159–163) in `Instructor/diad-learn-content/dashboard-in-a-day.md` — replace `Data > USSales > Sales.csv` with `Data > USEngineering > RDWorkload.csv`. Replace `Data > InternationalSales` with `Data > InternationalPrograms`. Replace "Product, Geography, and Manufacturer information is in...bi_dimensions.xlsx in the **USSales** subfolder" with "Program, Lab, and Directorate information is in...bi_dimensions.xlsx in the **USEngineering** subfolder in the **Data** folder (**/Data/USEngineering/**)."
- [X] T008 [US2] Update Task 1: Get USA data (around lines 165–239) in `Instructor/diad-learn-content/dashboard-in-a-day.md` — replace all "USA sales data" with "US engineering data". Update folder navigation: "double-click **USEngineering** folder, and then select the **RDWorkload.csv** file". Update "Sales.csv dialog window" to "RDWorkload.csv dialog window". Replace "sales file" with "workload file". Update the Zip column data type note to reference **LabCode** column instead, keeping the same instruction about changing to Text type.
- [X] T009 [US2] Update Task 2: Load various sources (around lines 241–275) in `Instructor/diad-learn-content/dashboard-in-a-day.md` — replace "USSales" folder references with "USEngineering". Keep bi_dimensions.xlsx filename. Replace sheet references: "geo" stays as sheet name in Excel (the rename happens in Section 1), "manufacturer" stays as sheet name, "Product_Table" stays as sheet name. Update the three checkbox instructions and the "three sheets are added as queries" note to match.
- [X] T010 [US2] Update Task 3: Add other data (around lines 277–359) in `Instructor/diad-learn-content/dashboard-in-a-day.md` — replace "InternationalSales" folder references with "InternationalPrograms". Update "Select the **InternationalPrograms** folder". Update query name references throughout. Replace "Nigeria" with "South Korea" in the country list. Update "You'll be taken back to...with a new query named **InternationalPrograms**". Update all **InternationalSales** bold references to **InternationalPrograms**. Update the Zip→Text instruction to reference LabCode context.
- [X] T011 [US2] Update Section 1: Rename tables (around lines 367–395) in `Instructor/diad-learn-content/dashboard-in-a-day.md` — update the rename mapping table: Sales→RDWorkload, geo→Lab, manufacturer→Directorate, Product_Table→Program, InternationalSales→International Programs. Update "Transform Files from InternationalSales" to "Transform Files from InternationalPrograms".
- [X] T012 [US2] Update Section 2–5: Data cleaning (around lines 397–503) in `Instructor/diad-learn-content/dashboard-in-a-day.md` — in Section 2 (Fill empty values), update **Product** query references to **Program** query. In Section 3 (Split columns), update **Product** column references to **Program** column and **Product** query to **Program** query. In Section 4, rename Product.1→Program, Product.2→Segment (Segment stays). In Section 5, update Price column splitting to work with the same pattern — keep the MSRP/Currency exercise as-is since it teaches the Column From Examples technique (the dimension data still has this structure).
- [X] T013 [US2] Update Section 6: Remove unwanted rows (around lines 505–545) in `Instructor/diad-learn-content/dashboard-in-a-day.md` — replace **Geography** query references with **Lab** query. Replace **Manufacturer** query references with **Directorate** query. Update "Zip" column references to "LabCode".
- [X] T014 [US2] Update Section 7: Transpose data (around lines 547–559) in `Instructor/diad-learn-content/dashboard-in-a-day.md` — replace **Manufacturer** query/table references with **Directorate**. Replace "ManufacturerID, Manufacturer, and Logo" with "DirectorateID, Directorate, and Logo".
- [X] T015 [US2] Update Section 8: Append queries (around lines 561–677) in `Instructor/diad-learn-content/dashboard-in-a-day.md` — replace **Sales** query/table references with **RDWorkload**. Replace **International Sales** with **International Programs**. Update "Revenue" column references to "LaborHours". Update "Fixed decimal number" note to reference LaborHours as engineering hours. Replace the conditional column instructions: CountryName logic stays the same but references RDWorkload table. Update "International Sales" disable-load references. Update query dependencies description.

**Checkpoint**: Module 2 fully reworked. All data import/prep instructions use AvMC terminology.
**Verify**: Re-read Module 2 end-to-end. Confirm each exercise still guides the learner through the same Power Query skills (import CSV, connect Excel, append queries, rename tables, change data types) with correct file paths, column names, and folder references. Ensure step-by-step instructions flow logically and no stale terms survive.

---

## Phase 4: User Story 3 — Module 3 Data Model & Visualization (Priority: P1)

**Goal**: Rework Module 3 to use AvMC table names, column names, and relationship references

**Independent Test**: Read Module 3 and verify all table/column references match the AvMC naming convention

### Implementation for User Story 3

- [X] T016 [P] [US3] Update Module 3 introduction and scenario (around lines 680–710) in `Instructor/diad-learn-content/dashboard-in-a-day.md` — replace "CMO for VanArsdel, Ltd." with appropriate AvMC role. Update task descriptions to reference R&D data model instead of sales model.
- [X] T017 [US3] Update Section 1: Data modeling (around lines 740–780) in `Instructor/diad-learn-content/dashboard-in-a-day.md` — replace **Sales** table references with **RDWorkload**. Replace **Product** with **Program**. Replace **Manufacturer** with **Directorate**. Update relationship descriptions: "RDWorkload and Program tables using the ProgramID column" and "Program and Directorate tables using the DirectorateID column".
- [X] T018 [US3] Update Section 2: Data exploration (around lines 782–810) in `Instructor/diad-learn-content/dashboard-in-a-day.md` — replace **Geography** field references with **Lab**. Replace **Revenue** field with **LaborHours**. Update "Sum of Revenue of each country" to "Sum of LaborHours by country". Update the relationship note.
- [X] T019 [US3] Update Section 1: Create missing relationships (around lines 812–870) in `Instructor/diad-learn-content/dashboard-in-a-day.md` — replace **Sales** and **Geography** table references with **RDWorkload** and **Lab**. Replace **Zip** column references with **LabCode**. Update DAX expressions: `ZipCountry = Sales[Zip] & "," & Sales[Country]` → `LabCodeCountry = RDWorkload[LabCode] & "," & RDWorkload[Country]`. Update Geography DAX: `ZipCountry = Geography[Zip] & "," & Geography[Country]` → `LabCodeCountry = Lab[LabCode] & "," & Lab[Country]`. Replace all **ZipCountry** references with **LabCodeCountry**. Update relationship drag-and-drop instructions to use new column/table names.
- [X] T020 [US3] Update Section 2: Data visualization (around lines 872–935) in `Instructor/diad-learn-content/dashboard-in-a-day.md` — replace **Revenue** with **LaborHours** in chart references. Replace **Manufacturer** table/column with **Directorate**. Update "top manufacturers by country" to "top directorates by country". Update Top N filter: drag **LaborHours** to "By value". Replace "VanArsdel, Ltd. has a higher percentage of sales" with "DEVCOM AvMC has a higher share of engineering effort".
- [X] T021 [US3] Update Group and bin data section (around lines 937–1035) in `Instructor/diad-learn-content/dashboard-in-a-day.md` — replace "CMO for VanArsdel, Ltd." with AvMC role. Replace "top five competitors by revenue" with "top five partner organizations by labor hours". Replace **Manufacturer** field/table/filter references with **Directorate**. Replace group member names: "Fabrikam, Inc."→"PEO Missiles & Space", "Nod Publishers"→"DEVCOM ARL", "Tailwind Traders"→"SMDC", "Wide World Importers"→"Industry Partners", "Top Competitors"→"Partner Organizations". Replace "VanArsdel, Ltd." group with "DEVCOM AvMC" group. Update "VanArsdel has nearly 50% share" to "DEVCOM AvMC has nearly 50% of effort share". Update Treemap and cross-highlighting references.
- [X] T022 [US3] Update visual level filters and time analysis (around lines 1037–1105) in `Instructor/diad-learn-content/dashboard-in-a-day.md` — replace **Manufacturer (groups)** with **Directorate (groups)** in page filter. Replace **Revenue** with **LaborHours** in chart references. Update "Sum of Revenue by Year" to "Sum of LaborHours by Year". Replace "VanArsdel, Ltd." slicer/filter selections with "DEVCOM AvMC". Update drill-down narrative: replace "fourth-quarter sales" with "fourth-quarter effort" and "2021 sales spike" with "2024 labor hours spike" (or appropriate year from the 2021–2025 range).
- [X] T023 [US3] Update Section 3: Slicers and card visual (around lines 1107–1190) in `Instructor/diad-learn-content/dashboard-in-a-day.md` — replace **Manufacturer** slicer references with **Directorate**. Replace "VanArsdel, Ltd." slicer selection with "DEVCOM AvMC". Replace **Revenue** card visual with **LaborHours** card. Update "Sum of Revenue" references to "Sum of LaborHours". Update decimal formatting note. Update field hiding instructions: hide LabCode, ProgramID, LabCodeCountry, DirectorateID instead of the original column names.
- [X] T024 [US3] Update Create a date table section (around lines 1140–1190) in `Instructor/diad-learn-content/dashboard-in-a-day.md` — update the CALENDAR DAX function: `Date = CALENDAR(DATE(2020,1,1), DATE(2026,12,31))` to match the AvMC data range. Replace **Sales** table references with **RDWorkload** in relationship creation. Update field-hiding list at end of section.

**Checkpoint**: Module 3 fully reworked with AvMC table names, relationships, and DAX.
**Verify**: Re-read Module 3 end-to-end. Confirm relationship-building steps still reference the correct table pairs and join columns. Verify every DAX expression is syntactically valid with the new names. Confirm chart/visual instructions still describe the right fields and expected outcomes.

---

## Phase 5: User Story 4 — Module 4 Hierarchies & DAX (Priority: P2)

**Goal**: Rework Module 4 to use AvMC hierarchy names, DAX measures, and scenario narrative

**Independent Test**: Verify all DAX expressions use LaborHours/ResearchTasks, hierarchy uses Program, and narrative references AvMC

### Implementation for User Story 4

- [X] T025 [P] [US4] Update Module 4 introduction and scenario (around lines 1194–1230) in `Instructor/diad-learn-content/dashboard-in-a-day.md` — replace "CMO for VanArsdel, Ltd." with AvMC role. Update example scenario to reference R&D analysis.
- [X] T026 [US4] Update hierarchy exercise (around lines 1232–1310) in `Instructor/diad-learn-content/dashboard-in-a-day.md` — replace **Geography** references with **Lab** table for Country/State drill-down. Replace "VanArsdel, Ltd." slicer selection with "DEVCOM AvMC". Update "Sum of Revenue by Country" to "Sum of LaborHours by Country". Replace **Product** table references with **Program** for hierarchy creation. Rename "Category Hierarchy" to "Category Hierarchy" (keep), then rename to "Program Hierarchy" instead of "Product Hierarchy". Update the hierarchy fields: Category, Segment, Program.
- [X] T027 [US4] Update matrix visual exercise (around lines 1312–1390) in `Instructor/diad-learn-content/dashboard-in-a-day.md` — replace **Revenue** with **LaborHours** in all matrix value references. Update "Sum of Revenue" to "Sum of LaborHours". Update "%GT Revenue" rename to "%GT LaborHours". Replace drill-down narrative about "Extreme" category and specific products with AvMC program category and specific programs (e.g., "Future Vertical Lift" category, "FLRAA (V-280 Valor)" program). Update "Maximus UE-04" and "Maximus UE-21" product references to appropriate program names.
- [X] T028 [US4] Update DAX measures exercise (around lines 1392–1434) in `Instructor/diad-learn-content/dashboard-in-a-day.md` — update PY Sales DAX: `PY Labor Hours = CALCULATE(SUM(RDWorkload[LaborHours]), SAMEPERIODLASTYEAR('Date'[Date]))`. Update % Growth DAX: `% Growth = DIVIDE(SUM(RDWorkload[LaborHours])-[PY Labor Hours],[PY Labor Hours])`. Replace all "PY Sales" references with "PY Labor Hours". Replace "Revenue" field references with "LaborHours". Update the narrative about "Maximus UE-04 has nearly 158% growth" with an appropriate AvMC program reference. Update formatting instructions (Currency → number format for LaborHours).

**Checkpoint**: Module 4 fully reworked with AvMC hierarchies and DAX measures.
**Verify**: Re-read Module 4 end-to-end. Confirm hierarchy drill-down steps still work logically (Category → Segment → Program). Verify DAX measures (PY Labor Hours, % Growth) reference the correct columns and tables. Ensure the narrative about specific programs reads naturally.

---

## Phase 6: User Story 5 — Module 5 Visualization & Reports (Priority: P2)

**Goal**: Rework Module 5 to use AvMC visual labels, theme, and branding references

**Independent Test**: Verify all chart titles, slicer labels, and branding references use AvMC terminology

### Implementation for User Story 5

- [X] T029 [P] [US5] Update Module 5 introduction (around line 1434) in `Instructor/diad-learn-content/dashboard-in-a-day.md` — replace "Chief Marketing Officer of VanArsdel, Ltd." with AvMC role.
- [X] T030 [US5] Update conditional formatting exercise in `Instructor/diad-learn-content/dashboard-in-a-day.md` — replace **% Growth** and **Revenue** references with AvMC equivalents. Replace "VanArsdel, Ltd." slicer/filter references with "DEVCOM AvMC". Replace **Manufacturer** slicer styling with **Directorate** slicer. Update drill-down references to use **Lab** table (Country → State).
- [X] T031 [US5] Update logo exercise in `Instructor/diad-learn-content/dashboard-in-a-day.md` — replace **Manufacturer** slicer references with **Directorate**. Replace **Logo** field from **Directorate** table (same field name). Update "VanArsdel, Ltd." logo selection with "DEVCOM AvMC" logo. Replace **Revenue** with **LaborHours** in chart references. Update "Sum of Revenue by Year" visual changes.
- [X] T032 [US5] Update gauge visual and theme exercise in `Instructor/diad-learn-content/dashboard-in-a-day.md` — replace "Sum of Revenue" card with "Sum of LaborHours". Replace **PY Sales** target with **PY Labor Hours**. Update theme file path reference to `Data/Theme/DIADTheme2.json` (same path, but note it now contains Army-branded palette). Update "VanArsdel" references in theme instructions. Update color palette description to reference Army Gold/Green/Black.

**Checkpoint**: Module 5 fully reworked with AvMC branding and visualization references.
**Verify**: Re-read Module 5 end-to-end. Confirm conditional formatting, logo, gauge, and theme exercises still teach the intended Power BI skills. Verify branding references (Army palette, DEVCOM AvMC logo) are consistent and the theme JSON path is correct.

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Final validation and cleanup across the entire document

- [X] T033 Remove the temporary reference comment block added in T001 from `Instructor/diad-learn-content/dashboard-in-a-day.md`
- [X] T034 Run a full-document search for residual original DIAD terms in `Instructor/diad-learn-content/dashboard-in-a-day.md` — grep for: VanArsdel, Revenue (as column/measure name not generic word), Units (as column name), Sales.csv, USSales, InternationalSales, ProductID, Zip (as column), Geography (as table), Manufacturer (as table), Nigeria, C:\DIAD, "sales data", "CMO". Fix any remaining references.
- [X] T035 Verify all DAX expressions in `Instructor/diad-learn-content/dashboard-in-a-day.md` are syntactically correct — check that table/column references in DAX match the AvMC naming (e.g., `RDWorkload[LaborHours]` not `Sales[Revenue]`, `Lab[LabCode]` not `Geography[Zip]`).
- [X] T036 Review Modules 6–8 (if present) in `Instructor/diad-learn-content/dashboard-in-a-day.md` for any VanArsdel, Revenue, Sales, Manufacturer, Geography, or Product references that need updating. These modules (Custom Visuals/Bookmarks, Power BI Service, Sharing) are more tool-generic but may contain scattered scenario references.
- [X] T037 Run quickstart.md validation step 7 checklist against the completed `Instructor/diad-learn-content/dashboard-in-a-day.md` — confirm no residual VanArsdel text, all DAX uses AvMC column names, and module structure is preserved.

---

## Dependencies & Execution Order

### Phase Dependencies

```
Phase 1: Setup ──────────────────────────────────────────► (no deps)
Phase 2: Foundational (Header + Module 1) ──────────────► depends on Phase 1
Phase 3: US2 Module 2 (Data Import & Prep) ─────────────► depends on Phase 2 (scenario context set)
Phase 4: US3 Module 3 (Data Model & Viz) ──────────────► depends on Phase 2
Phase 5: US4 Module 4 (Hierarchies & DAX) ──────────────► depends on Phase 2
Phase 6: US5 Module 5 (Viz & Reports) ─────────────────► depends on Phase 2
Phase 7: Polish ────────────────────────────────────────► depends on all above
```

### User Story Dependencies

- **US1 (P1 — Header/Module 1)**: Foundational — sets scenario context for all modules
- **US2 (P1 — Module 2)**: Can start after US1; heaviest edit
- **US3 (P1 — Module 3)**: Can start after US1; independent of US2
- **US4 (P2 — Module 4)**: Can start after US1; independent of US2/US3
- **US5 (P2 — Module 5)**: Can start after US1; independent of US2/US3/US4

### Parallel Opportunities

```
SEQUENTIAL (must go first):
  Phase 1: T001
  Phase 2: T002 → T003 → T004 → T005

PARALLEL GROUP A (after Phase 2):
  ├── Phase 3 (US2): T006 → T007 → T008 → T009 → T010 → T011 → T012 → T013 → T014 → T015
  ├── Phase 4 (US3): T016 ║ T017 → T018 → T019 → T020 → T021 → T022 → T023 → T024
  ├── Phase 5 (US4): T025 ║ T026 → T027 → T028
  └── Phase 6 (US5): T029 ║ T030 → T031 → T032

SEQUENTIAL (after all above):
  Phase 7: T033 → T034 → T035 → T036 → T037
```

Note: Within each module, tasks are sequential because they edit adjacent sections of the same file. Across modules, tasks CAN run in parallel if using separate working copies, but in practice a single-file edit workflow means they'll be sequential.

---

## Implementation Strategy

### MVP First (Module 1 + Module 2 only)

1. Complete Phase 1: Setup (T001)
2. Complete Phase 2: Header & Module 1 (T002–T005)
3. Complete Phase 3: Module 2 (T006–T015)
4. Run T034 validation on just Modules 1–2

This delivers the highest-impact rework first — Module 2 has the most data references.

### Incremental Delivery

After MVP, add modules in priority order:
- Module 3 (T016–T024) — second heaviest edit
- Module 4 (T025–T028) — DAX measures
- Module 5 (T029–T032) — branding/theme
- Polish (T033–T037) — final sweep
