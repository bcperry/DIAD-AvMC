# Quickstart: DIAD AvMC Customization

**Phase 1 Output** | **Date**: 2026-04-26 | **Updated**: 2026-04-26

## Prerequisites

- Python 3.11+ with `uv` package manager
- Power BI Desktop (current release, Windows)
- pbi-tools + pbi-tools-core (in `%LOCALAPPDATA%`)
- Git

## Step 1: Generate Synthetic Data

```powershell
cd C:\Users\blaineperry\git\DIAD-AvMC
uv sync
uv run Instructor/scripts/generate_synthetic_data.py
```

This creates:
- `Instructor/Data/USEngineering/RDWorkload.csv` (~4.2M rows)
- `Instructor/Data/InternationalPrograms/{Australia,Canada,Germany,Japan,Mexico,SouthKorea}.csv` (~3M rows total)

Verify output:
```powershell
Get-Content "Instructor/Data/USEngineering/RDWorkload.csv" -TotalCount 3
# Expected: ProgramID,Date,LabCode,ResearchTasks,LaborHours
#           1003,2021-10-06,35808,13,1455.820813

(Get-Content "Instructor/Data/USEngineering/RDWorkload.csv" | Measure-Object -Line).Lines
# Expected: ~4,200,000
```

## Step 2: Generate Brand Assets

```powershell
uv run Instructor/scripts/create_brand_assets.py
```

Creates:
- `Instructor/Data/AvMC_Logo.png` (~979×122px, Army Gold on transparent)
- `Instructor/Data/Background.jpg` (1280×720px, defense-themed dark background)

## Step 3: Theme JSON

Already updated at `Instructor/Data/Theme/DIADTheme2.json` with Army-branded 15-color palette (see Contract 3 in csv-schemas.md).

## Step 4: Rebuild .pbix Solution Files

```powershell
.\build.ps1 -SkipDataGen -Force
# Or for full rebuild including data gen:
.\build.ps1 -Force
```

This runs `rebuild_powerbi_sources.py` which:
1. Extracts each .pbix via pbi-tools into TMDL + Mashup format
2. Patches all text files (token replacements, path replacements, regex replacements)
3. Renames TMDL table files (Sales→RDWorkload, Product→Program, etc.)
4. Swaps theme JSON, logo, and background in StaticResources
5. Compiles patched projects to .pbit files

## Step 5: Update Learn Content Markdown

Edit `Instructor/diad-learn-content/dashboard-in-a-day.md`:
1. Replace VanArsdel scenario narrative with DEVCOM AvMC R&D engineering workload
2. Update all data references (column names, table names, folder paths, file names)
3. Update DAX expressions (`LaborHours` not `Revenue`, `ResearchTasks` not `Units`)
4. Preserve identical instructional flow (Modules 1–5)

## Step 6: Update PowerPoint Deck (if present)

```powershell
uv run Instructor/scripts/merge_diad_content.py  # or python-pptx based updater
```

## Step 7: Validate

- [ ] All 7 CSV files exist with correct headers and approximate row counts
- [ ] `bi_dimensions.xlsx` contains Program, Directorate, Lab sheets
- [ ] Theme JSON has 15 Army colors with name "DEVCOM AvMC Theme"
- [ ] Logo and background images exist at correct dimensions
- [ ] All .pbit files compile without errors (via build.ps1)
- [ ] No residual "VanArsdel" references in any deliverable
- [ ] `dashboard-in-a-day.md` uses AvMC terminology throughout
- [ ] DAX expressions reference `LaborHours`, `ResearchTasks`, `PY Labor Hours`
