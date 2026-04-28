#!/usr/bin/env python3
from __future__ import annotations

import csv
import random
from datetime import date
from pathlib import Path

from faker import Faker


ROOT_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT_DIR / "Instructor" / "Data"
US_DATA_PATH = DATA_DIR / "USEngineering" / "RDWorkload.csv"
INTERNATIONAL_DIR = DATA_DIR / "InternationalPrograms"

START_DATE = date(2021, 1, 1)
END_DATE = date(2025, 12, 31)
RANDOM_SEED = 20260426

US_ROW_COUNT = 4_200_000
INTERNATIONAL_ROW_COUNTS = {
    "Australia": 1_992_000,
    "Japan": 527_000,
    "SouthKorea": 205_000,
    "Germany": 138_000,
    "Mexico": 129_000,
    "Canada": 46_000,
}

PROGRAMS = [
    {"id": 1001, "name": "FLRAA (V-280 Valor)", "category": "Future Vertical Lift", "weight": 1.75, "tasks": (5, 35), "hours": 96.0},
    {"id": 1002, "name": "FARA", "category": "Future Vertical Lift", "weight": 1.35, "tasks": (4, 28), "hours": 88.0},
    {"id": 1003, "name": "ITEP (T901 Engine)", "category": "Future Vertical Lift", "weight": 1.20, "tasks": (3, 24), "hours": 102.0},
    {"id": 1004, "name": "MOSA Avionics", "category": "Future Vertical Lift", "weight": 0.78, "tasks": (2, 18), "hours": 64.0},
    {"id": 1005, "name": "Black Hawk Aircrew Trainer", "category": "Modeling & Simulation", "weight": 0.66, "tasks": (2, 16), "hours": 52.0},
    {"id": 2001, "name": "PrSM (Precision Strike Missile)", "category": "Long Range Precision Fires", "weight": 1.05, "tasks": (2, 20), "hours": 71.0},
    {"id": 2002, "name": "HIMARS Modernization", "category": "Long Range Precision Fires", "weight": 0.92, "tasks": (2, 18), "hours": 57.0},
    {"id": 2003, "name": "Hypersonic Weapon Components", "category": "Long Range Precision Fires", "weight": 0.55, "tasks": (1, 10), "hours": 136.0},
    {"id": 2004, "name": "LRPF Next-Gen Propulsion", "category": "Long Range Precision Fires", "weight": 0.42, "tasks": (1, 9), "hours": 118.0},
    {"id": 2005, "name": "IFPC (Indirect Fire Protection)", "category": "Air & Missile Defense", "weight": 0.96, "tasks": (2, 16), "hours": 76.0},
    {"id": 2006, "name": "THAAD Modernization", "category": "Air & Missile Defense", "weight": 0.88, "tasks": (1, 14), "hours": 43.0},
    {"id": 2007, "name": "Patriot Next-Gen Radar", "category": "Air & Missile Defense", "weight": 0.46, "tasks": (1, 10), "hours": 31.0},
    {"id": 3001, "name": "Directed Energy Weapons", "category": "Emerging Technology", "weight": 0.38, "tasks": (1, 12), "hours": 67.0},
    {"id": 3002, "name": "Counter-UAS Systems", "category": "Emerging Technology", "weight": 0.34, "tasks": (1, 11), "hours": 39.0},
    # PEO Aviation (DirectorateID 1)
    {"id": 4001, "name": "FUAS (Future UAS)", "category": "Unmanned Systems", "weight": 0.72, "tasks": (2, 16), "hours": 58.0},
    {"id": 4002, "name": "Apache Guardian Upgrade", "category": "Unmanned Systems", "weight": 0.65, "tasks": (2, 14), "hours": 48.0},
    {"id": 4003, "name": "Chinook Block II", "category": "Unmanned Systems", "weight": 0.50, "tasks": (1, 12), "hours": 42.0},
    # RCCTO (DirectorateID 3)
    {"id": 5001, "name": "Rapid Prototyping Initiative", "category": "Rapid Capability", "weight": 0.45, "tasks": (1, 10), "hours": 72.0},
    {"id": 5002, "name": "Autonomous Resupply", "category": "Rapid Capability", "weight": 0.35, "tasks": (1, 8), "hours": 55.0},
    # Joint Program Offices (DirectorateID 6)
    {"id": 6001, "name": "Joint Air-Ground Missile", "category": "Joint Munitions", "weight": 0.58, "tasks": (1, 14), "hours": 63.0},
    {"id": 6002, "name": "Joint Multi-Role Helo", "category": "Joint Munitions", "weight": 0.48, "tasks": (1, 12), "hours": 50.0},
    {"id": 6003, "name": "Joint C-UAS Integration", "category": "Joint Munitions", "weight": 0.40, "tasks": (1, 10), "hours": 45.0},
    # Industry Partners (DirectorateID 8)
    {"id": 7001, "name": "Industry IRAD - Composites", "category": "Defense Industrial Base", "weight": 0.30, "tasks": (1, 8), "hours": 38.0},
    {"id": 7002, "name": "Industry IRAD - AI/ML", "category": "Defense Industrial Base", "weight": 0.28, "tasks": (1, 7), "hours": 35.0},
]

LABS = [
    {"code": 35808, "name": "Redstone Arsenal (HQ/TDD/S3I)", "weight": 2.80},
    {"code": 94035, "name": "Moffett Field / NASA Ames", "weight": 1.45},
    {"code": 23604, "name": "JB Langley-Eustis (Aviation Dev)", "weight": 1.30},
    {"code": 78419, "name": "Corpus Christi (Sustainment Eng)", "weight": 1.10},
    {"code": 80913, "name": "Colorado Springs (S3I Software)", "weight": 0.92},
    {"code": 88002, "name": "White Sands Missile Range", "weight": 1.05},
    {"code": 85365, "name": "Yuma Proving Ground", "weight": 0.86},
    {"code": 21005, "name": "Aberdeen Proving Ground (DEVCOM HQ)", "weight": 0.74},
    {"code": 96857, "name": "Wheeler Army Airfield", "weight": 0.48},
    {"code": 35898, "name": "Redstone Test Center", "weight": 0.72},
    {"code": 32542, "name": "Eglin AFB (Joint Test)", "weight": 0.56},
    {"code": 87117, "name": "Kirtland AFB (Directed Energy)", "weight": 0.38},
]

FMS_CONFIG = {
    "Australia": {"program_ids": [1001, 1003, 2005, 4001, 6001], "facility_codes": [2600, 4700, 5000, 8107], "growth": 0.04},
    "Japan": {"program_ids": [2003, 2006, 2007, 6002], "facility_codes": [100, 197, 904, 901], "growth": 0.035},
    "SouthKorea": {"program_ids": [1001, 2005, 2006, 3002, 4002], "facility_codes": [412, 140, 406, 503], "growth": 0.09},
    "Germany": {"program_ids": [2005, 2007, 1003, 5001], "facility_codes": [67657, 91522, 92655, 53123], "growth": 0.025},
    "Mexico": {"program_ids": [1004, 1005, 7001], "facility_codes": [11520, 76220, 45659, 66600], "growth": 0.02},
    "Canada": {"program_ids": [1001, 3001, 6003], "facility_codes": [8050, 3155, 3590, 107], "growth": 0.018},
}

PROGRAM_BY_ID = {program["id"]: program for program in PROGRAMS}
CSV_DIALECT = "excel"
CSV_LINE_TERMINATOR = "\r\n"


def weighted_choice(items: list[dict[str, object]], weight_key: str) -> dict[str, object]:
    return random.choices(items, weights=[float(item[weight_key]) for item in items], k=1)[0]


def random_activity_date(country: str | None = None) -> date:
    year_weights = []
    for year in range(START_DATE.year, END_DATE.year + 1):
        years_since_start = year - START_DATE.year
        if country == "SouthKorea":
            year_weights.append(1.0 + (0.22 * years_since_start))
        elif country:
            year_weights.append(1.0 + (FMS_CONFIG[country]["growth"] * years_since_start))
        else:
            year_weights.append(1.0 + (0.04 * years_since_start))

    selected_year = random.choices(range(START_DATE.year, END_DATE.year + 1), weights=year_weights, k=1)[0]
    quarter_months = [
        (1, 2, 3),
        (4, 5, 6),
        (7, 8, 9),
        (10, 11, 12),
    ]
    selected_quarter = random.choices(quarter_months, weights=[1.18, 0.92, 1.14, 0.96], k=1)[0]
    selected_month = random.choice(selected_quarter)
    selected_day = random.randint(1, 28)
    return date(selected_year, selected_month, selected_day)


def correlated_tasks_and_hours(program: dict[str, object], international: bool = False) -> tuple[int, str]:
    min_tasks, max_tasks = program["tasks"]
    task_ceiling = min(int(max_tasks), 20 if international else 50)
    tasks = random.triangular(int(min_tasks), task_ceiling, int(min_tasks) + (task_ceiling - int(min_tasks)) * 0.42)
    task_count = max(1, int(round(tasks)))

    mean_hours = float(program["hours"])
    noise = random.uniform(0.82, 1.22)
    complexity = random.choice([0.88, 0.95, 1.00, 1.07, 1.18])
    labor_hours = task_count * mean_hours * noise * complexity
    lower_bound = 25.0 if international else 50.0
    upper_bound = 3000.0 if international else 5000.0
    labor_hours = min(max(labor_hours, lower_bound), upper_bound)
    return task_count, f"{labor_hours:.6f}"


def write_csv(path: Path, header: list[str], rows) -> int:
    path.parent.mkdir(parents=True, exist_ok=True)
    count = 0
    with path.open("w", encoding="utf-8", newline="") as output_file:
        writer = csv.writer(output_file, dialect=CSV_DIALECT, lineterminator=CSV_LINE_TERMINATOR)
        writer.writerow(header)
        for row in rows:
            writer.writerow(row)
            count += 1
    return count


def generate_us_rows():
    for _ in range(US_ROW_COUNT):
        program = weighted_choice(PROGRAMS, "weight")
        lab = weighted_choice(LABS, "weight")
        research_tasks, labor_hours = correlated_tasks_and_hours(program)
        yield [
            program["id"],
            random_activity_date().isoformat(),
            lab["code"],
            research_tasks,
            labor_hours,
        ]


def generate_international_rows(country: str):
    config = FMS_CONFIG[country]
    program_subset = [PROGRAM_BY_ID[program_id] for program_id in config["program_ids"]]
    for _ in range(INTERNATIONAL_ROW_COUNTS[country]):
        program = weighted_choice(program_subset, "weight")
        research_tasks, labor_hours = correlated_tasks_and_hours(program, international=True)
        yield [
            program["id"],
            random_activity_date(country).isoformat(),
            random.choice(config["facility_codes"]),
            research_tasks,
            labor_hours,
            "South Korea" if country == "SouthKorea" else country,
        ]


def generate_us_sales() -> int:
    return write_csv(
        US_DATA_PATH,
        ["ProgramID", "Date", "LabCode", "ResearchTasks", "LaborHours"],
        generate_us_rows(),
    )


def generate_international_sales() -> dict[str, int]:
    row_counts = {}
    old_nigeria_path = INTERNATIONAL_DIR / "Nigeria.csv"
    if old_nigeria_path.exists():
        old_nigeria_path.unlink()
    for country in INTERNATIONAL_ROW_COUNTS:
        row_counts[country] = write_csv(
            INTERNATIONAL_DIR / f"{country}.csv",
            ["ProgramID", "Date", "LabCode", "ResearchTasks", "LaborHours", "Country"],
            generate_international_rows(country),
        )
    return row_counts


# ── Dimension data for bi_dimensions.xlsx ──

DIRECTORATES = [
    {"id": 1, "name": "PEO Aviation", "logo": "https://th.bing.com/th/id/OIP.fmOoH9INyIdty4eSL8ad9wAAAA?w=137&h=150&c=7&r=0&o=7&dpr=1.5&pid=1.7&rm=3"},
    {"id": 2, "name": "PEO Missiles & Space", "logo": "https://deshq.com/wp-content/uploads/2019/12/PEO-MS.png"},
    {"id": 3, "name": "RCCTO", "logo": "https://th.bing.com/th/id/R.dbda82b5ab4e227d9db4e7bbf8dad487?rik=hGLL8IlU7B9YmA&riu=http%3a%2f%2fww1.prweb.com%2fprfiles%2f2020%2f01%2f22%2f16820400%2f0.png&ehk=yfGlM2angUdFD4K6Y42P78jDj4ODZoHCb7G7x5Vb3TU%3d&risl=&pid=ImgRaw&r=0"},
    {"id": 4, "name": "SMDC", "logo": "https://www.clipartmax.com/png/middle/188-1887751_smdc-logo-united-states-army-space-and-missile-defense-command.png"},
    {"id": 5, "name": "DEVCOM ARL", "logo": "https://tse4.mm.bing.net/th/id/OIP.79Gt8Sm_XEAJwzhmiRn2swHaDy?rs=1&pid=ImgDetMain&o=7&rm=3"},
    {"id": 6, "name": "Joint Program Offices", "logo": "https://jpeoaa.army.mil/portals/94/Images/JPEOAA/logos/logo-pljs.png?ver=KMAvkkhYRC6_xrFNl8HPeQ%3D%3D"},
    {"id": 7, "name": "DEVCOM AvMC", "logo": "https://tse1.mm.bing.net/th/id/OIP.B0t95Wh3PilNsphpi0EXKwHaDy?rs=1&pid=ImgDetMain&o=7&rm=3"},
    {"id": 8, "name": "Industry Partners", "logo": "https://upload.wikimedia.org/wikipedia/commons/9/97/Emblem_of_the_Assistant_Secretary_of_Defense_for_Industrial_Base_Policy.png"},
]

PROGRAM_DIMENSIONS = [
    # (ProgramID, "ProgramName|Segment", Category, DirectorateID, TRLLevel)
    (1001, "FLRAA (V-280 Valor)|Systems Integration", "Future Vertical Lift", 7, "TRL 7"),
    (1002, "FARA|Aerodynamics", None, 7, "TRL 6"),
    (1003, "ITEP (T901 Engine)|Propulsion", None, 7, "TRL 7"),
    (1004, "MOSA Avionics|Avionics Software", None, 7, "TRL 5"),
    (1005, "Black Hawk Aircrew Trainer|Virtual Simulation", "Modeling & Simulation", 7, "TRL 8"),
    (2001, "PrSM (Precision Strike Missile)|Guidance & Nav", "Long Range Precision Fires", 7, "TRL 7"),
    (2002, "HIMARS Modernization|Launcher Systems", None, 7, "TRL 8"),
    (2003, "Hypersonic Weapon Components|Thermal Protection", None, 2, "TRL 4"),
    (2004, "LRPF Next-Gen Propulsion|Rocket Propulsion", None, 2, "TRL 5"),
    (2005, "IFPC (Indirect Fire Protection)|Sensors & Radar", "Air & Missile Defense", 4, "TRL 6"),
    (2006, "THAAD Modernization|Interceptor Systems", None, 4, "TRL 7"),
    (2007, "Patriot Next-Gen Radar|Signal Processing", None, 4, "TRL 6"),
    (3001, "Directed Energy Weapons|High Energy Laser", "Emerging Technology", 5, "TRL 4"),
    (3002, "Counter-UAS Systems|Detection & Track", None, 5, "TRL 5"),
    # PEO Aviation (DirectorateID 1)
    (4001, "FUAS (Future UAS)|Flight Controls", "Unmanned Systems", 1, "TRL 5"),
    (4002, "Apache Guardian Upgrade|Avionics Integration", None, 1, "TRL 7"),
    (4003, "Chinook Block II|Structural Analysis", None, 1, "TRL 6"),
    # RCCTO (DirectorateID 3)
    (5001, "Rapid Prototyping Initiative|Systems Engineering", "Rapid Capability", 3, "TRL 4"),
    (5002, "Autonomous Resupply|Autonomy Software", None, 3, "TRL 3"),
    # Joint Program Offices (DirectorateID 6)
    (6001, "Joint Air-Ground Missile|Seeker Technology", "Joint Munitions", 6, "TRL 6"),
    (6002, "Joint Multi-Role Helo|Rotor Dynamics", None, 6, "TRL 5"),
    (6003, "Joint C-UAS Integration|Sensor Fusion", None, 6, "TRL 4"),
    # Industry Partners (DirectorateID 8)
    (7001, "Industry IRAD - Composites|Advanced Materials", "Defense Industrial Base", 8, "TRL 3"),
    (7002, "Industry IRAD - AI/ML|Machine Learning", None, 8, "TRL 4"),
]

LAB_DIMENSIONS = [
    # (LabCode, City, State, Region, District, Country)
    ("35808", "Redstone Arsenal, AL", "AL", "South", "District #01", "USA"),
    ("94035", "Moffett Field, CA", "CA", "West", "District #02", "USA"),
    ("23604", "JB Langley-Eustis, VA", "VA", "East", "District #03", "USA"),
    ("78419", "Corpus Christi, TX", "TX", "South", "District #04", "USA"),
    ("80913", "Colorado Springs, CO", "CO", "West", "District #05", "USA"),
    ("88002", "White Sands, NM", "NM", "West", "District #06", "USA"),
    ("85365", "Yuma Proving Ground, AZ", "AZ", "West", "District #07", "USA"),
    ("21005", "Aberdeen, MD", "MD", "East", "District #08", "USA"),
    ("96857", "Wheeler AAF, HI", "HI", "West", "District #09", "USA"),
    ("35898", "Redstone Test Center, AL", "AL", "South", "District #01", "USA"),
    ("32542", "Eglin AFB, FL", "FL", "South", "District #10", "USA"),
    ("87117", "Kirtland AFB, NM", "NM", "West", "District #06", "USA"),
]

# International facility codes → lab entries
_FMS_FACILITIES = {
    "Australia": [
        ("2600", "Edinburgh, SA", "SA", "Pacific", "APAC District", "Australia"),
        ("4700", "Townsville, QLD", "QLD", "Pacific", "APAC District", "Australia"),
        ("5000", "Adelaide, SA", "SA", "Pacific", "APAC District", "Australia"),
        ("8107", "Darwin, NT", "NT", "Pacific", "APAC District", "Australia"),
    ],
    "Japan": [
        ("100", "Ichigaya, Tokyo", "TK", "Pacific", "Japan District", "Japan"),
        ("197", "Sagamihara, Kanagawa", "KN", "Pacific", "Japan District", "Japan"),
        ("904", "Kadena, Okinawa", "OK", "Pacific", "Japan District", "Japan"),
        ("901", "Naha, Okinawa", "OK", "Pacific", "Japan District", "Japan"),
    ],
    "SouthKorea": [
        ("412", "Daejeon", "DJ", "Pacific", "Korea District", "South Korea"),
        ("140", "Seoul", "SE", "Pacific", "Korea District", "South Korea"),
        ("406", "Cheonan", "CN", "Pacific", "Korea District", "South Korea"),
        ("503", "Changwon", "GN", "Pacific", "Korea District", "South Korea"),
    ],
    "Germany": [
        ("67657", "Kaiserslautern", "RP", "Europe", "Germany District", "Germany"),
        ("91522", "Ansbach", "BY", "Europe", "Germany District", "Germany"),
        ("92655", "Grafenwoehr", "BY", "Europe", "Germany District", "Germany"),
        ("53123", "Bonn", "NW", "Europe", "Germany District", "Germany"),
    ],
    "Mexico": [
        ("11520", "Mexico City", "CDMX", "Americas", "Mexico District", "Mexico"),
        ("76220", "Queretaro", "QRO", "Americas", "Mexico District", "Mexico"),
        ("45659", "Guadalajara", "JAL", "Americas", "Mexico District", "Mexico"),
        ("66600", "Monterrey", "NL", "Americas", "Mexico District", "Mexico"),
    ],
    "Canada": [
        ("8050", "Ottawa, ON", "ON", "Americas", "Canada District", "Canada"),
        ("3155", "Valcartier, QC", "QC", "Americas", "Canada District", "Canada"),
        ("3590", "Suffield, AB", "AB", "Americas", "Canada District", "Canada"),
        ("107", "Halifax, NS", "NS", "Americas", "Canada District", "Canada"),
    ],
}

DIMENSIONS_PATH = DATA_DIR / "USEngineering" / "bi_dimensions.xlsx"


def rebuild_dimensions() -> None:
    """Rebuild bi_dimensions.xlsx with Option C dimension data."""
    from openpyxl import Workbook
    from openpyxl.worksheet.table import Table, TableStyleInfo

    wb = Workbook()

    # ── product sheet (Excel Table named Product_Table) ──
    ws_prod = wb.active
    ws_prod.title = "product"
    ws_prod.append(["Product Details", None, None, None, None])
    ws_prod.append(["ProgramID", "Product", "Category", "DirectorateID", "TechnologyReadinessLevel"])
    for row in PROGRAM_DIMENSIONS:
        ws_prod.append(list(row))

    # Create named Excel Table over data range (row 2 = header, rows 3-16 = data)
    data_end_row = 2 + len(PROGRAM_DIMENSIONS)
    tab = Table(displayName="Product_Table", ref=f"A2:E{data_end_row}")
    tab.tableStyleInfo = TableStyleInfo(name="TableStyleMedium2", showFirstColumn=False,
                                        showLastColumn=False, showRowStripes=True)
    ws_prod.add_table(tab)

    # ── directorate sheet (transposed layout) ──
    ws_mfr = wb.create_sheet("directorate")
    num_dirs = len(DIRECTORATES)
    # Row 1: generic column headers
    ws_mfr.append(["Column1"] + [f"Column{i+2}" for i in range(num_dirs)])
    # Row 2: DirectorateID row
    ws_mfr.append(["DirectorateID"] + [d["id"] for d in DIRECTORATES])
    # Row 3: Directorate name row
    ws_mfr.append(["Directorate"] + [d["name"] for d in DIRECTORATES])
    # Row 4: Logo row
    ws_mfr.append(["Logo"] + [d["logo"] for d in DIRECTORATES])
    # Rows 5-7: intentional blank rows (students learn to delete these)
    for _ in range(3):
        ws_mfr.append([None] * (num_dirs + 1))

    # ── geo sheet (with header rows matching original layout) ──
    ws_geo = wb.create_sheet("geo")
    ws_geo.append(["Source:", "DEVCOM AvMC Lab Locations", None, None, None, None])
    ws_geo.append(["Last Updated:", "2026-01-01", None, None, None, None])
    ws_geo.append([None] * 6)
    ws_geo.append(["LabCode", "City", "State", "Region", "District", "Country"])

    # US lab rows
    for lab_row in LAB_DIMENSIONS:
        ws_geo.append(list(lab_row))

    # International facility rows
    for country_labs in _FMS_FACILITIES.values():
        for lab_row in country_labs:
            ws_geo.append(list(lab_row))

    DIMENSIONS_PATH.parent.mkdir(parents=True, exist_ok=True)
    wb.save(DIMENSIONS_PATH)
    print(f"Rebuilt {DIMENSIONS_PATH}")


def main() -> None:
    random.seed(RANDOM_SEED)
    Faker.seed(RANDOM_SEED)
    Faker()

    print("Generating DEVCOM AvMC synthetic CSV data...")
    us_count = generate_us_sales()
    print(f"USEngineering/RDWorkload.csv: {us_count:,} rows")

    international_counts = generate_international_sales()
    for country, row_count in international_counts.items():
        print(f"InternationalPrograms/{country}.csv: {row_count:,} rows")

    rebuild_dimensions()


if __name__ == "__main__":
    main()
