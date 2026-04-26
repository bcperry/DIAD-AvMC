# Quickstart: DIAD AvMC Customization

**Phase 1 Output** | **Date**: 2026-04-26

## Prerequisites

- Python 3.11+ (for data generation)
- Power BI Desktop (current release, Windows)
- Git

## Step 1: Generate Synthetic Data

```bash
cd /home/blaine/git/DIAD-AMC
uv sync
uv run Instructor/scripts/generate_synthetic_data.py
```

This creates:
- `Instructor/Data/USSales/Sales.csv` (~4.2M rows)
- `Instructor/Data/InternationalSales/{Australia,Canada,Germany,Japan,Mexico,SouthKorea}.csv` (~3M rows total)

Verify output:
```bash
head -2 Instructor/Data/USSales/Sales.csv
# Expected: PlatformID,Date,InstallationCode,WorkOrders,EngineeringHours
#           1001,2023-06-15,35808,3,254.572500

wc -l Instructor/Data/USSales/Sales.csv
# Expected: ~4,200,000
```

## Step 2: Update Theme JSON

Replace `Instructor/Data/Theme/DIADTheme2.json` with the Army-branded palette
defined in `specs/001-diad-avmc-customization/contracts/csv-schemas.md` (Contract 3).

## Step 3: Replace Branding Assets

1. Place `AvMC_Logo.png` (~979×122px) in `Instructor/Data/`
2. Replace `Background.jpg` (1280×720px) in `Instructor/Data/`

## Step 4: Rebuild .pbix Solution Files

For each `.pbix` in `Instructor/Reports/`:

1. Open in Power BI Desktop
2. **Home → Transform Data** — update data source paths if needed
3. Verify all queries load without errors
4. Apply the new theme: **View → Themes → Browse for themes** → select `DIADTheme2.json`
5. Replace logo image in any report pages referencing `VanArsdel_Logo.png`
6. Replace background image references
7. Update visual titles (e.g., "Revenue" → "Engineering Hours", "Units Sold" → "Work Orders")
8. Save

Repeat for `Instructor/Trainer Material/Optional Demos/*.pbix`.

## Step 5: Update PowerPoint Deck

Open `Instructor/Trainer Material/Dashboard in a Day.pptx`:
1. Find/replace "VanArsdel" → "DEVCOM AvMC"
2. Replace scenario language per the research document
3. Update screenshots to match new .pbix files
4. Save

## Step 6: Validate

- [ ] All 8 .pbix files open without data errors
- [ ] Theme colors render correctly in all charts
- [ ] Logo appears correctly on report pages
- [ ] No residual "VanArsdel" references in any deliverable
- [ ] PowerPoint deck narration matches new scenario
- [ ] CSV row counts approximate original targets
