# Windows Handoff: DIAD AvMC Customization

Date: 2026-04-26
Branch: `001-diad-avmc-customization`

## Goal

Customize Microsoft's Dashboard in a Day training content for a DEVCOM AvMC audience. The original fictional VanArsdel consumer-products scenario is being replaced with a defense engineering / aviation and missile sustainment scenario while preserving the original DIAD lab flow.

## Key Decisions

- Use Army / DEVCOM AvMC framing: platform sustainment, engineering hours, work orders, installations, and FMS partner support.
- Preserve the original DIAD CSV shapes so Power BI labs require minimal structural changes.
- Replace Nigeria with South Korea for international/FMS data.
- Use `uv` as the Python package manager. Do not use `pip` under any circumstances.
- All synthetic data must remain public, fictional, NIPRNet-safe, and free of CUI, FOUO, PII, or real program data.

## Important Specs

- Plan: `specs/001-diad-avmc-customization/plan.md`
- Research: `specs/001-diad-avmc-customization/research.md`
- Data model: `specs/001-diad-avmc-customization/data-model.md`
- CSV contracts: `specs/001-diad-avmc-customization/contracts/csv-schemas.md`
- Quickstart: `specs/001-diad-avmc-customization/quickstart.md`
- Task list: `specs/001-diad-avmc-customization/tasks.md`

## Completed Work

Tasks T001 through T011 are complete in `tasks.md`.

Implemented:

- `pyproject.toml` and `uv.lock` for uv-managed Python dependencies.
- `.gitignore` with Python, local environment, log, OS, and editor ignores.
- `Instructor/scripts/generate_synthetic_data.py` for synthetic CSV generation.
- `Instructor/scripts/create_brand_assets.py` for logo/background generation.
- `Instructor/Data/Theme/DIADTheme2.json` with a DEVCOM AvMC / Army color palette.
- `Instructor/Data/AvMC_Logo.png` at 979 x 122 RGBA.
- `Instructor/Data/Background.jpg` at 1280 x 720 RGB.
- New synthetic CSVs under `Instructor/Data/`.

Generated CSVs:

- `Instructor/Data/USSales/Sales.csv`: 4,200,000 data rows plus header.
- `Instructor/Data/InternationalSales/Australia.csv`: 1,992,000 data rows plus header.
- `Instructor/Data/InternationalSales/Japan.csv`: 527,000 data rows plus header.
- `Instructor/Data/InternationalSales/SouthKorea.csv`: 205,000 data rows plus header.
- `Instructor/Data/InternationalSales/Germany.csv`: 138,000 data rows plus header.
- `Instructor/Data/InternationalSales/Mexico.csv`: 129,000 data rows plus header.
- `Instructor/Data/InternationalSales/Canada.csv`: 46,000 data rows plus header.

Removed/replaced:

- `Instructor/Data/InternationalSales/Nigeria.csv` was removed by the generator.
- South Korea is represented as filename `SouthKorea.csv` and CSV `Country` value `South Korea`.

## Data Shape

US CSV header:

```text
PlatformID,Date,InstallationCode,WorkOrders,EngineeringHours
```

International CSV header:

```text
PlatformID,Date,InstallationCode,WorkOrders,EngineeringHours,Country
```

The generator uses weighted and correlated synthetic data:

- Black Hawk, Apache, and Chinook have higher volume.
- Redstone Arsenal and Corpus Christi Army Depot dominate domestic activity.
- WorkOrders and EngineeringHours are correlated.
- Dates span 2021-01-01 through 2025-12-31.
- Data includes year-over-year growth and seasonal variation.
- South Korea ramps up more strongly in later years.
- Random generation is seeded for reproducibility.

## Commands To Use On Windows

From the repo root:

```powershell
uv sync
uv run python -m py_compile Instructor/scripts/generate_synthetic_data.py Instructor/scripts/create_brand_assets.py
uv run Instructor/scripts/generate_synthetic_data.py
uv run Instructor/scripts/create_brand_assets.py
```

Do not use `pip`.

## Validation Already Run

The Linux-side implementation validated:

- `uv sync` completed successfully.
- Both Python scripts compile with `uv run python -m py_compile ...`.
- Theme JSON parses with `uv run python -m json.tool Instructor/Data/Theme/DIADTheme2.json`.
- CSV headers match the contracts.
- CSV line endings are CRLF.
- Sampled `EngineeringHours` values have exactly 6 decimal places.
- `SouthKorea.csv` exists and `Nigeria.csv` is absent.
- Logo/background dimensions match the contracts.

## Next Phase On Windows: Power BI Desktop

Continue at T012 in `specs/001-diad-avmc-customization/tasks.md`.

Use `Instructor/Reports/Lab 1 solution.pbix` as the proof-of-concept rebuild first. In Power BI Desktop:

1. Open `Instructor/Reports/Lab 1 solution.pbix`.
2. Update data source paths to the generated CSVs if Power BI prompts for them.
3. In Power Query, rename/re-map fields:
   - `ProductID` -> `PlatformID`
   - `Zip` -> `InstallationCode`
   - `Units` -> `WorkOrders`
   - `Revenue` -> `EngineeringHours`
4. Apply `Instructor/Data/Theme/DIADTheme2.json` as the report theme.
5. Replace VanArsdel logo references with `Instructor/Data/AvMC_Logo.png`.
6. Replace or refresh report background references with `Instructor/Data/Background.jpg`.
7. Update visual titles and measure labels:
   - Revenue -> Engineering Hours
   - Units Sold / Units -> Work Orders
   - Product -> Platform
   - Zip -> Installation
8. Save and verify the report opens cleanly.

After Lab 1 works, apply the same pattern to:

- `Instructor/Reports/Lab 2 solution.pbix`
- `Instructor/Reports/Lab 3 solution.pbix`
- `Instructor/Reports/Lab 4 solution.pbix`
- `Instructor/Reports/Lab 5 solution.pbix`
- `Instructor/Reports/DIAD Final Report.pbix`
- `Instructor/Trainer Material/Optional Demos/DIAD Final Report with RLS.pbix`
- `Instructor/Trainer Material/Optional Demos/Social.pbix` if it contains VanArsdel references

## Trainer Material Phase

After `.pbix` rebuilds are done, continue at T020:

- Update `Instructor/Trainer Material/Dashboard in a Day.pptx`.
- Replace VanArsdel scenario language with DEVCOM AvMC language.
- Update field references: Revenue, Units, Product, Zip.
- Replace screenshots after the Power BI reports are rebuilt.
- Update PDF demo scripts if editable source files are available; otherwise recreate/export PDFs from updated sources.

## Current Task Status

Completed:

- T001-T011: setup, synthetic data generation, validation, theme, logo, and background.

Not completed:

- T012-T019: Power BI `.pbix` rebuilds.
- T020-T026: trainer material updates.
- T027-T030: final sweep, validation, and cleanup.

## Notes

- The `.pbix` files are binary Power BI artifacts and should be edited in Power BI Desktop on Windows.
- Keep the original lab sequence intact.
- Mark each task complete in `specs/001-diad-avmc-customization/tasks.md` as work finishes.
- The optional Spec Kit commit hook is `/speckit.git.commit` if you want to commit progress between phases.