<#
.SYNOPSIS
    Build pipeline for DIAD AvMC customized Power BI templates.

.DESCRIPTION
    Regenerates synthetic CSV data, then extracts/patches/compiles all PBIX
    files into PBIT templates with AvMC R&D Engineering scenario branding.

    Steps:
      1. Generate synthetic CSV data (USEngineering + InternationalPrograms)
      2. Extract each source PBIX via pbi-tools Desktop
      3. Patch text/images (token, path, regex replacements)
      4. Compile patched projects to PBIT via pbi-tools Core
      5. Audit for stale terms

.PARAMETER SkipDataGen
    Skip CSV regeneration (use existing data files).

.PARAMETER Force
    Delete previously extracted projects and re-extract from PBIX.

.PARAMETER Reports
    One or more PBIX stem filters, or 'all' (default). Example: 'Lab 1','Lab 2'

.PARAMETER OutDir
    Output folder for compiled PBITs.  Defaults to a timestamped folder under
    $env:LOCALAPPDATA\pbi-tools\diad-avmc\compiled-<timestamp>.

.PARAMETER NoCompile
    Stop after patching — do not compile PBIT files.

.EXAMPLE
    .\build.ps1
    # Full rebuild: regenerate data, extract, patch, compile all 8 PBITs.

.EXAMPLE
    .\build.ps1 -SkipDataGen -Force
    # Re-extract and rebuild PBITs without regenerating CSVs.

.EXAMPLE
    .\build.ps1 -Reports 'Lab 1','Lab 2' -SkipDataGen
    # Rebuild only Lab 1 and Lab 2 solution PBITs.
#>
[CmdletBinding()]
param(
    [switch]$SkipDataGen,
    [switch]$Force,
    [switch]$NoCompile,
    [string[]]$Reports = @('all'),
    [string]$OutDir
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$RepoRoot = $PSScriptRoot
$ScriptsDir = Join-Path $RepoRoot 'Instructor' 'scripts'

# ── Resolve output directory ───────────────────────────────────────────
if (-not $OutDir) {
    $stamp = Get-Date -Format 'yyyyMMdd-HHmmss'
    $OutDir = Join-Path $env:LOCALAPPDATA 'pbi-tools' 'diad-avmc' "compiled-$stamp"
}

# ── Step 1: Generate synthetic data ───────────────────────────────────
if (-not $SkipDataGen) {
    Write-Host "`n=== Step 1: Generating synthetic CSV data ===" -ForegroundColor Cyan
    $genScript = Join-Path $ScriptsDir 'generate_synthetic_data.py'
    if (-not (Test-Path $genScript)) {
        Write-Error "Data generator not found: $genScript"
        exit 1
    }
    uv run python -m py_compile $genScript
    if ($LASTEXITCODE -ne 0) { Write-Error "Syntax error in $genScript"; exit 1 }
    uv run python $genScript
    if ($LASTEXITCODE -ne 0) { Write-Error "Data generation failed"; exit 1 }
    Write-Host "Data generation complete.`n" -ForegroundColor Green
} else {
    Write-Host "`n=== Step 1: Skipped data generation (--SkipDataGen) ===" -ForegroundColor Yellow
}

# ── Step 2-4: Extract, patch, compile PBITs ───────────────────────────
Write-Host "=== Step 2-4: Extract / Patch / Compile PBITs ===" -ForegroundColor Cyan

$rebuildScript = Join-Path $ScriptsDir 'rebuild_powerbi_sources.py'
if (-not (Test-Path $rebuildScript)) {
    Write-Error "Rebuild script not found: $rebuildScript"
    exit 1
}

uv run python -m py_compile $rebuildScript
if ($LASTEXITCODE -ne 0) { Write-Error "Syntax error in $rebuildScript"; exit 1 }

$rebuildArgs = @($Reports)
if ($Force)     { $rebuildArgs += '--force' }
if ($NoCompile) { $rebuildArgs += '--no-compile' }
$rebuildArgs += '--out-dir'
$rebuildArgs += $OutDir

uv run python $rebuildScript @rebuildArgs
if ($LASTEXITCODE -ne 0) { Write-Error "PBIT rebuild failed"; exit 1 }

if ($NoCompile) {
    Write-Host "`nPatching complete (--NoCompile: skipped PBIT compilation)." -ForegroundColor Yellow
    exit 0
}

# ── Step 5: Audit ─────────────────────────────────────────────────────
Write-Host "`n=== Step 5: Audit ===" -ForegroundColor Cyan

# 5a: Count compiled PBITs
$pbitFiles = @(Get-ChildItem $OutDir -Filter '*.pbit' -ErrorAction SilentlyContinue | Sort-Object Name)
Write-Host "Compiled PBITs: $($pbitFiles.Count)"
$pbitFiles | ForEach-Object { Write-Host "  $($_.Name)  ($([Math]::Round($_.Length/1KB)) KB)" }

$expectedCount = 8
if ($Reports -ne @('all')) {
    $expectedCount = $Reports.Count
}
if ($pbitFiles.Count -lt $expectedCount) {
    Write-Warning "Expected at least $expectedCount PBITs, got $($pbitFiles.Count)"
}

# 5b: Scan for stale terms in extracted projects
$extractRoot = Join-Path $env:LOCALAPPDATA 'pbi-tools' 'diad-avmc' 'extracted'
$stalePatterns = @(
    'PlatformID', 'InstallationCode', 'WorkOrders', 'EngineeringHours',
    'VanArsdel', 'Vanarsdel', 'VANarsdel',
    'USSales', 'InternationalSales', 'Sales.csv',
    'IsParameterQueryRequired=true',
    'Fabrikam', 'Tailwind Traders', 'Nod Publishers', 'Wide World Importers',
    'table Sales', 'table Product', 'table Manufacturer', 'table Geography',
    'PY Sales', 'Market Share'
)
$staleHits = @()
foreach ($pattern in $stalePatterns) {
    $hits = Get-ChildItem $extractRoot -Recurse -File -Include '*.tmdl','*.json' -ErrorAction SilentlyContinue |
        Select-String -Pattern $pattern -SimpleMatch -ErrorAction SilentlyContinue
    if ($hits) { $staleHits += $hits }
}

if ($staleHits.Count -gt 0) {
    Write-Warning "Found $($staleHits.Count) stale term occurrence(s):"
    $staleHits | Select-Object -First 25 | ForEach-Object {
        $rel = $_.Path.Substring($extractRoot.Length + 1)
        Write-Host "  $rel`:$($_.LineNumber) $($_.Line.Trim())" -ForegroundColor Red
    }
} else {
    Write-Host "No stale terms found." -ForegroundColor Green
}

# ── Summary ───────────────────────────────────────────────────────────
Write-Host "`n=== Build Complete ===" -ForegroundColor Green
Write-Host "Output: $OutDir"
Write-Host "PBITs:  $($pbitFiles.Count)"
