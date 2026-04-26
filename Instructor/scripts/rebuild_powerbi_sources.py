#!/usr/bin/env python3
from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import time
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[2]
REPORTS_DIR = ROOT_DIR / "Instructor" / "Reports"
OPTIONAL_DEMOS_DIR = ROOT_DIR / "Instructor" / "Trainer Material" / "Optional Demos"
DATA_DIR = ROOT_DIR / "Instructor" / "Data"
US_DATA_PATH = DATA_DIR / "USEngineering" / "RDWorkload.csv"
DIMENSIONS_PATH = DATA_DIR / "USEngineering" / "bi_dimensions.xlsx"
INTERNATIONAL_DIR = DATA_DIR / "InternationalPrograms"
THEME_PATH = DATA_DIR / "Theme" / "DIADTheme2.json"
LOGO_PATH = DATA_DIR / "AvMC_Logo.png"
BACKGROUND_PATH = DATA_DIR / "Background.jpg"
SOCIAL_TWITTER_PATH = DATA_DIR / "Social" / "Twitterdatav4.csv"

LOCALAPPDATA = Path(os.environ.get("LOCALAPPDATA", Path.home() / "AppData" / "Local"))
PBI_TOOLS = LOCALAPPDATA / "pbi-tools" / "pbi-tools.exe"
PBI_TOOLS_CORE = LOCALAPPDATA / "pbi-tools-core" / "pbi-tools.core.exe"
WORK_ROOT = LOCALAPPDATA / "pbi-tools" / "diad-avmc"

PBIX_FILES = [
    REPORTS_DIR / "Lab 1 solution.pbix",
    REPORTS_DIR / "Lab 2 solution.pbix",
    REPORTS_DIR / "Lab 3 solution.pbix",
    REPORTS_DIR / "Lab 4 solution.pbix",
    REPORTS_DIR / "Lab 5 solution.pbix",
    REPORTS_DIR / "DIAD Final Report.pbix",
    OPTIONAL_DEMOS_DIR / "DIAD Final Report with RLS.pbix",
    OPTIONAL_DEMOS_DIR / "Social.pbix",
]

TEXT_EXTENSIONS = {".tmdl", ".json", ".txt"}

TOKEN_REPLACEMENTS = [
    # VanArsdel URL must be replaced before the generic brand replacement
    ("https://raw.githubusercontent.com/CharlesSterling/DiadManu/master/Vanarsdel.png", ""),
    # Brand (handle both casing variants; regex below catches remaining)
    ("VanArsdel", "DEVCOM AvMC"),
    ("Vanarsdel", "DEVCOM AvMC"),
    # Folder/file renames (catch paths already baked into PBIX from earlier sessions)
    ("InternationalSales", "InternationalPrograms"),
    ("USSales", "USEngineering"),
    ("Sales.csv", "RDWorkload.csv"),
    # ── Competitor / manufacturer names → AvMC directorates ──
    ("Fabrikam, Inc.", "Technology Development (TDD)"),
    ("Tailwind Traders", "Systems Readiness (SRD)"),
    ("Nod Publishers", "Software & Simulation (S3I)"),
    ("Wide World Importers", "Cross-Functional Teams"),
    ("Top Competitors", "Peer Directorates"),
    ("DEVCOM AvMC, Ltd.", "DEVCOM AvMC"),
    # ── Table / entity renames (longest match first) ──
    ("Manufacturer Analysis", "Directorate Analysis"),
    ("ManufacturerID", "DirectorateID"),
    ("Manufacturer (groups)", "Directorate (groups)"),
    ("Selected Manufacturer", "Selected Directorate"),
    # Manufacturer standalone — MUST come after compound terms above
    ("Manufacturer", "Directorate"),
    # Product table → Program (keep Product Hierarchy → Program Hierarchy)
    ("Product Hierarchy", "Program Hierarchy"),
    ("Product_Table", "Product_Table"),  # preserve xlsx sheet ref
    ("table Product", "table Program"),
    ("Product[Product]", "Program[Program]"),
    ("\"Product\"", "\"Program\""),
    ("'Product'", "'Program'"),
    ("{Product,", "{Program,"),
    ("column Product", "column Program"),
    ("sourceColumn: Product", "sourceColumn: Program"),
    # Geography → Lab (table name)
    ("table Geography", "table Lab"),
    ("Geography[LabCode]", "Lab[LabCode]"),
    ("Geography[Country]", "Lab[Country]"),
    ('"Geography"', '"Lab"'),
    ("Geography/", "Lab/"),
    # Sales table → RDWorkload
    ("table Sales", "table RDWorkload"),
    ("Sales[LaborHours]", "RDWorkload[LaborHours]"),
    ("Sales[Sales]", "RDWorkload[Total Labor Hours]"),
    ("Sales.ProgramID", "RDWorkload.ProgramID"),
    ("Sales.LabCodeCountry", "RDWorkload.LabCodeCountry"),
    ("Sales.Date", "RDWorkload.Date"),
    ("'Sales'", "'RDWorkload'"),
    # Product table → Program in relationships/expressions
    ("Product.ProgramID", "Program.ProgramID"),
    ("Product.DirectorateID", "Program.DirectorateID"),
    ("Product.ManufacturerID", "Program.DirectorateID"),
    # Manufacturer table → Directorate in relationships/expressions
    ("Manufacturer.DirectorateID", "Directorate.DirectorateID"),
    ("Manufacturer.ManufacturerID", "Directorate.DirectorateID"),
    # Geography table → Lab in relationships/expressions
    ("Geography.LabCodeCountry", "Lab.LabCodeCountry"),
    ("Geography.LabCode", "Lab.LabCode"),
    # ── Measure renames ──
    ("DEVCOM AvMC Market Share", "DEVCOM AvMC Effort Share"),
    ("DEVCOM AvMC Sales", "DEVCOM AvMC Labor Hours"),
    ("PY Sales", "PY Labor Hours"),
    ("measure Sales", "measure 'Total Labor Hours'"),
    ("measure Bar", "measure 'Workload Bar'"),
    ("[PY Sales]", "[PY Labor Hours]"),
    ("[DEVCOM AvMC Sales]", "[DEVCOM AvMC Labor Hours]"),
    # Product/Platform → Program (original + intermediate Option A name)
    ("ProductID", "ProgramID"),
    ("PlatformID", "ProgramID"),
    # Geography → Lab (intermediate first since it's longer)
    ("InstallationCode", "LabCode"),
    ("Zip", "LabCode"),
    # Display names (longest match first)
    ("Units Sold", "Research Tasks"),
    ("Work Orders", "Research Tasks"),
    # Column names (intermediate first since it's longer)
    ("WorkOrders", "ResearchTasks"),
    ("Units", "ResearchTasks"),
    # Measure column
    ("EngineeringHours", "LaborHours"),
    ("Revenue", "LaborHours"),
    # Country
    ("Nigeria", "South Korea"),
    # Social data fix
    ("Table.PromoteHeaders(Twitterdatav4_Sheet,", "Table.PromoteHeaders(Source,"),
]

PATH_REPLACEMENTS = [
    (r"C:\DIAD\Data\USSales\Sales.csv", str(US_DATA_PATH)),
    (r"C:\DIAD\Data\USSales\bi_dimensions.xlsx", str(DIMENSIONS_PATH)),
    (r"C:\DIADData\USSales\bi_dimensions.xlsx", str(DIMENSIONS_PATH)),
    (r"C:\DIAD\Data\InternationalSales", str(INTERNATIONAL_DIR)),
    (r"C:\Users\chass\Documents\Twitterdatav4.csv", str(SOCIAL_TWITTER_PATH)),
    (r"C:\Users\chass\Documents\Twitterdatav5.xlsx", str(SOCIAL_TWITTER_PATH)),
]

REGEX_REPLACEMENTS = [
    # Catch any remaining case variants of VanArsdel (e.g. VANarsdel in filenames)
    (re.compile(r'(?i)vanarsdel'), 'DEVCOM_AvMC'),
    (re.compile(r'\{"LaborHours",\s*Currency\.Type\}'), '{"LaborHours", type number}'),
    (re.compile(r'\{"EngineeringHours",\s*Currency\.Type\}'), '{"LaborHours", type number}'),
    # Strip currency formatting from all labor-hours measures — use plain number
    (re.compile(r'formatString:\s*\\\$#,0\.00;\(\\\$#,0\.00\);\\\$#,0\.00'), "formatString: #,0.00"),
    (re.compile(r'formatString:\s*\\\$#,0\.###############;\(\\\$#,0\.###############\);\\\$#,0\.###############'), "formatString: #,0.00"),
    (re.compile(r'formatString:\s*\\\$#,0;\(\\\$#,0\);\\\$#,0'), "formatString: #,0.00"),
    (re.compile(r'"currencyCulture":\s*"en-US"'), '"isDecimal": true'),
    # Rename TMDL table files after patching (handled by patch_project, not text replacement)
    (re.compile(r'IsParameterQueryRequired=true'), 'IsParameterQueryRequired=false'),
    (re.compile(r'Columns=11'), 'Columns=12'),
    (re.compile(r'\{"", type text\}, \{"_1", type text\}'), '{"Column10", type text}, {"Column11", type text}, {"Column12", type text}'),
    (
        re.compile(
            r'Source = Excel\.Workbook\(File\.Contents\("[^"]*Twitterdatav4\.csv"\), null, true\),\s*\n'
            r'\s*Twitterdatav4_Sheet = Source\{\[Item="Twitterdatav4",Kind="Sheet"\]\}\[Data\],',
            re.MULTILINE,
        ),
        lambda _: f'Source = Csv.Document(File.Contents("{SOCIAL_TWITTER_PATH}"),[Delimiter=",", Columns=12, Encoding=65001, QuoteStyle=QuoteStyle.Csv]),',
    ),
]


def run(command: list[str]) -> None:
    print("+", " ".join(f'"{part}"' if " " in part else part for part in command))
    subprocess.run(command, check=True, cwd=ROOT_DIR)


def ensure_tools() -> None:
    missing = [str(path) for path in (PBI_TOOLS, PBI_TOOLS_CORE) if not path.exists()]
    if missing:
        raise SystemExit("Missing pbi-tools executable(s): " + ", ".join(missing))


def project_name(pbix_path: Path) -> str:
    return pbix_path.stem.replace(" ", "_")


def extract_project(pbix_path: Path, extract_dir: Path, force: bool) -> None:
    if force and extract_dir.exists():
        shutil.rmtree(extract_dir)
        # Windows: directory may linger briefly after rmtree
        for _ in range(20):
            if not extract_dir.exists():
                break
            time.sleep(0.1)
    if extract_dir.exists():
        return
    extract_dir.parent.mkdir(parents=True, exist_ok=True)
    run([
        str(PBI_TOOLS),
        "extract",
        str(pbix_path),
        "-extractFolder",
        str(extract_dir),
        "-modelSerialization",
        "Tmdl",
        "-mashupSerialization",
        "Expanded",
    ])


def patch_text(text: str) -> str:
    for old, new in PATH_REPLACEMENTS:
        text = text.replace(old, new)
    for old, new in TOKEN_REPLACEMENTS:
        text = text.replace(old, new)
    for pattern, replacement in REGEX_REPLACEMENTS:
        text = pattern.sub(replacement, text)
    return text


def patch_project(extract_dir: Path) -> int:
    changed = 0
    for path in extract_dir.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in TEXT_EXTENSIONS:
            continue
        text = path.read_text(encoding="utf-8-sig")
        patched = patch_text(text)
        if patched != text:
            path.write_text(patched, encoding="utf-8", newline="")
            changed += 1

    # ── Rename TMDL table files to match patched table names ──
    tmdl_renames = {
        "Sales.tmdl": "RDWorkload.tmdl",
        "Product.tmdl": "Program.tmdl",
        "Manufacturer.tmdl": "Directorate.tmdl",
        "Geography.tmdl": "Lab.tmdl",
    }
    tables_dir = extract_dir / "Model" / "tables"
    if tables_dir.exists():
        for old_name, new_name in tmdl_renames.items():
            old_path = tables_dir / old_name
            new_path = tables_dir / new_name
            if old_path.exists() and not new_path.exists():
                old_path.rename(new_path)
                changed += 1

    # ── Rename report section folders ──
    section_renames = {
        "000_Market Share": "000_Effort Share",
        "001_By Manufacturer": "001_By Directorate",
    }
    sections_dir = extract_dir / "Report" / "sections"
    if sections_dir.exists():
        for old_name, new_name in section_renames.items():
            old_path = sections_dir / old_name
            new_path = sections_dir / new_name
            if old_path.exists() and not new_path.exists():
                old_path.rename(new_path)
                changed += 1

    # ── Rename bookmark folders ──
    bookmark_renames = {
        "AUS Sales Spike in 2018": "AUS Spike in 2018",
        "JAP Sales Steady": "JPN Steady",
        "USA Sales Increasing": "USA Increasing",
        "Product 04 - Spike": "Program 04 - Spike",
        "Product 20 - not so much": "Program 20 - not so much",
        "Product 21 also Spike": "Program 21 also Spike",
    }
    bookmarks_dir = extract_dir / "Report" / "bookmarks"
    if bookmarks_dir.exists():
        for old_name, new_name in bookmark_renames.items():
            old_path = bookmarks_dir / old_name
            new_path = bookmarks_dir / new_name
            if old_path.exists() and not new_path.exists():
                old_path.rename(new_path)
                changed += 1

    theme_dir = extract_dir / "StaticResources" / "SharedResources" / "BaseThemes"
    if THEME_PATH.exists() and theme_dir.exists():
        theme_text = THEME_PATH.read_text(encoding="utf-8-sig")
        for theme_file in theme_dir.glob("*.json"):
            if theme_file.read_text(encoding="utf-8-sig") != theme_text:
                theme_file.write_text(theme_text, encoding="utf-8", newline="")
                changed += 1

    resources_dir = extract_dir / "StaticResources" / "RegisteredResources"
    if resources_dir.exists():
        if LOGO_PATH.exists():
            logo_bytes = LOGO_PATH.read_bytes()
            for image_file in resources_dir.glob("*.png"):
                normalized = image_file.name.lower().replace("_", "")
                if "vanarsdel" in normalized:
                    if image_file.read_bytes() != logo_bytes:
                        image_file.write_bytes(logo_bytes)
                        changed += 1
                    # Rename file to match updated text references
                    new_name = re.sub(r'(?i)vanarsdel', 'DEVCOM_AvMC', image_file.name)
                    if new_name != image_file.name:
                        image_file.rename(image_file.with_name(new_name))
                        changed += 1
        if BACKGROUND_PATH.exists():
            background_bytes = BACKGROUND_PATH.read_bytes()
            for image_file in resources_dir.glob("*.jpg"):
                if "background" in image_file.name.lower():
                    if image_file.read_bytes() != background_bytes:
                        image_file.write_bytes(background_bytes)
                        changed += 1
    return changed


def compile_project(extract_dir: Path, out_dir: Path) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    run([str(PBI_TOOLS_CORE), "compile", str(extract_dir), str(out_dir), "PBIT", "true"])
    output = out_dir / f"{extract_dir.name}.pbit"
    if not output.exists():
        candidates = sorted(out_dir.glob("*.pbit"), key=lambda item: item.stat().st_mtime, reverse=True)
        if not candidates:
            raise FileNotFoundError(f"No PBIT output created in {out_dir}")
        output = candidates[0]
    return output


def selected_pbix(names: list[str]) -> list[Path]:
    existing = [path for path in PBIX_FILES if path.exists()]
    if not names or names == ["all"]:
        return existing
    lookup = {path.stem.lower(): path for path in existing}
    selected = []
    for name in names:
        key = name.lower().removesuffix(".pbix")
        matches = [path for stem, path in lookup.items() if key in stem]
        if not matches:
            raise SystemExit(f"No PBIX matched '{name}'")
        selected.extend(matches)
    return list(dict.fromkeys(selected))


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract, patch, and compile DIAD PBIX files for the AvMC scenario.")
    parser.add_argument("reports", nargs="*", default=["all"], help="PBIX stem filters, or 'all'.")
    parser.add_argument("--force", action="store_true", help="Delete existing extracted projects before extracting.")
    parser.add_argument("--no-compile", action="store_true", help="Patch extracted projects without compiling PBIT files.")
    parser.add_argument("--out-dir", type=Path, default=WORK_ROOT / "compiled", help="Folder for compiled PBIT output.")
    args = parser.parse_args()

    ensure_tools()
    output_root = args.out_dir
    patched_projects = []

    for pbix_path in selected_pbix(args.reports):
        name = project_name(pbix_path)
        extract_dir = WORK_ROOT / "extracted" / name
        print(f"\n== {pbix_path.relative_to(ROOT_DIR)} ==")
        extract_project(pbix_path, extract_dir, args.force)
        changed = patch_project(extract_dir)
        print(f"Patched {changed} text/resource file(s) in {extract_dir}")
        patched_projects.append(extract_dir)
        if not args.no_compile:
            pbit_path = compile_project(extract_dir, output_root)
            print(f"Compiled: {pbit_path}")

    print("\nPatched projects:")
    for project in patched_projects:
        print(f"- {project}")
    if not args.no_compile:
        print(f"\nCompiled PBIT output folder: {output_root}")


if __name__ == "__main__":
    main()
