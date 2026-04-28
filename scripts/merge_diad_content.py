"""Merge per-unit markdown files into one clean file per module and update the index.

Reads from Instructor/diad-learn-content/<module>/*.md
Writes to Instructor/diad-learn-content/<module>.md  (one file per module)
Then removes the per-unit subdirectories.

Usage: python Instructor/scripts/merge_diad_content.py
"""
import re
import shutil
from pathlib import Path

CONTENT_DIR = Path(__file__).resolve().parent.parent / "diad-learn-content"

# Module metadata in order
MODULES = [
    {
        "dir": "01-intro-power-bi",
        "title": "Module 1: Introduction and Prerequisites for Power BI",
        "base_url": "https://learn.microsoft.com/en-us/training/modules/intro-power-bi",
        "units": [
            "introduction",
            "install-application",
            "tour",
            "unzip-files",
        ],
        # skip: check, summary (quiz/recap fluff)
    },
    {
        "dir": "02-access-prepare-power-bi",
        "title": "Module 2: Access and Prepare Data for Power BI Desktop",
        "base_url": "https://learn.microsoft.com/en-us/training/modules/access-prepare-power-bi",
        "units": [
            "introduction",
            "exercise-load-data",
            "exercise-perform-common-data-cleaning",
        ],
    },
    {
        "dir": "03-build-your-first-data-model",
        "title": "Module 3: Build Your First Data Model",
        "base_url": "https://learn.microsoft.com/en-us/training/modules/build-your-first-data-model",
        "units": [
            "introduction",
            "exercise-create-model-explore",
            "exercise-create-relationships",
            "exercise-group-bin",
            "exercise-create-date-table",
        ],
    },
    {
        "dir": "04-use-hierarchies-dax-first-data-model",
        "title": "Module 4: Use Hierarchies and DAX in Your First Data Model",
        "base_url": "https://learn.microsoft.com/en-us/training/modules/use-hierarchies-dax-first-data-model",
        "units": [
            "introduction",
            "exercise-hierarchy-data-model",
            "exercise-build-matrix-visual",
            "exercise-build-dax-measure",
        ],
    },
    {
        "dir": "05-data-visualization-reports-power-bi",
        "title": "Module 5: Data Visualization and Reports in Power BI",
        "base_url": "https://learn.microsoft.com/en-us/training/modules/data-visualization-reports-power-bi",
        "units": [
            "introduction",
            "apply-conditional",
            "exercise-add-logo",
            "exercise-apply-custom",
        ],
    },
    {
        "dir": "06-import-custom-visuals",
        "title": "Module 6: Import Custom Visuals and Add Bookmarks",
        "base_url": "https://learn.microsoft.com/en-us/training/modules/import-custom-visuals",
        "units": [
            "introduction",
            "exercise-import",
            "exercise-add-bookmarks",
        ],
    },
    {
        "dir": "07-publish-access-reports",
        "title": "Module 7: Publish and Access Reports in Power BI Service",
        "base_url": "https://learn.microsoft.com/en-us/training/modules/publish-access-reports",
        "units": [
            "introduction",
            "exercise-create-mobile-report-view",
            "exercise-publish-report",
            "exercise-build-dashboard",
        ],
    },
    {
        "dir": "08-interact-share-power-bi",
        "title": "Module 8: Interact, Share, and Collaborate Power BI Dashboards",
        "base_url": "https://learn.microsoft.com/en-us/training/modules/interact-share-power-bi",
        "units": [
            "introduction",
            "exercise-service-interaction-personalization",
            "exercise-share-apps",
            "exercise-access-report-mobile",
        ],
    },
]


def clean_content(raw: str) -> str:
    """Strip UI chrome, feedback sections, and navigation boilerplate from scraped markdown."""

    # Remove the source header we added
    text = re.sub(r"^\*Source:.*?\*\s*$", "", raw, flags=re.MULTILINE)
    text = re.sub(r"^---\s*$", "", text, flags=re.MULTILINE, count=1)

    # ---- Line-based cleanup to avoid catastrophic backtracking ----
    JUNK_PATTERNS = {
        "Read in English", "Achievements", "Add to plan", "Ask Learn",
        "Completed", "Was this page helpful?", "Yes", "No",
        "Need help with this topic?",
        "Want to try using Ask Learn to clarify or guide you through this topic?",
        "Suggest a fix?",
    }

    lines = text.split("\n")
    cleaned = []
    skip_rest = False
    seen_h1 = set()

    for line in lines:
        stripped = line.strip()

        # Once we hit Feedback or Next unit, skip everything after
        if stripped.startswith("## Feedback") or stripped.startswith("## Next unit:") or stripped.startswith("## Module incomplete:"):
            skip_rest = True
            continue
        if skip_rest:
            continue

        # Skip junk lines
        if stripped in JUNK_PATTERNS:
            continue
        if stripped == "Add":
            continue

        # Skip lines that are only whitespace/tabs with maybe a dash
        if not stripped or (len(stripped) <= 2 and stripped in ("-", "")):
            cleaned.append("")
            continue

        # Skip "- N minutes" chrome
        if re.match(r"^-\s*\d+\s*minutes?$", stripped):
            continue

        # Skip all top-level # headings — the merge function adds ## headings
        if stripped.startswith("# ") and not stripped.startswith("## "):
            continue

        cleaned.append(line)

    text = "\n".join(cleaned)

    # Clean HTML entities
    text = text.replace("&gt;", ">").replace("&lt;", "<").replace("&amp;", "&")

    # Normalize multiple blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip()


def merge_module(mod: dict) -> str:
    """Read all unit files for a module, clean them, and merge into one markdown string."""
    mod_dir = CONTENT_DIR / mod["dir"]
    parts = []

    # Module header
    parts.append(f"# {mod['title']}")
    parts.append(f"\n*Source: [{mod['base_url']}]({mod['base_url']})*\n")

    for unit_slug in mod["units"]:
        unit_file = mod_dir / f"{unit_slug}.md"
        if not unit_file.exists():
            print(f"  WARNING: Missing {unit_file}")
            continue

        raw = unit_file.read_text(encoding="utf-8")

        # Extract the original title from the first "# " line
        title_match = re.search(r"^# (.+)$", raw, re.MULTILINE)
        title = title_match.group(1) if title_match else unit_slug.replace("-", " ").title()

        cleaned = clean_content(raw)

        if not cleaned or len(cleaned) < 50:
            print(f"  SKIPPED (empty after cleanup): {unit_slug}")
            continue

        parts.append(f"\n---\n\n## {title}\n")
        parts.append(cleaned)

    return "\n".join(parts) + "\n"


def main():
    print(f"Content dir: {CONTENT_DIR}")
    index_lines = [
        "# Dashboard in a Day - Online Workshop\n\n",
        "*Source: https://learn.microsoft.com/en-us/training/paths/dashboard-in-a-day/*\n\n",
    ]

    for mod in MODULES:
        print(f"\nProcessing: {mod['title']}")
        merged = merge_module(mod)

        out_file = CONTENT_DIR / f"{mod['dir']}.md"
        out_file.write_text(merged, encoding="utf-8")
        char_count = len(merged)
        print(f"  -> Wrote {out_file.name} ({char_count:,} chars)")

        index_lines.append(f"- [{mod['title']}]({mod['dir']}.md)\n")

        # Remove the subdirectory
        mod_dir = CONTENT_DIR / mod["dir"]
        if mod_dir.is_dir():
            shutil.rmtree(mod_dir)
            print(f"  -> Removed {mod['dir']}/")

    # Write new index
    index_path = CONTENT_DIR / "README.md"
    index_path.write_text("".join(index_lines), encoding="utf-8")
    print(f"\nIndex updated: {index_path}")
    print("Done!")


if __name__ == "__main__":
    main()
