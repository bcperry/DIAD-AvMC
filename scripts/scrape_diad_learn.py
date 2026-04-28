"""Scrape the Dashboard in a Day learning path from Microsoft Learn into markdown files.

Usage: python scrape_diad_learn.py [output_dir]
Default output: ../diad-learn-content/
"""
import re
import sys
import time
from pathlib import Path
from urllib.request import urlopen, Request
from html.parser import HTMLParser


# All modules and their units in order
MODULES = [
    {
        "slug": "01-intro-power-bi",
        "title": "Introduction and prerequisites for Power BI",
        "units": [
            ("introduction", "Introduction to Power BI"),
            ("install-application", "Install the Power BI Desktop application"),
            ("tour", "Tour of Power BI Desktop"),
            ("unzip-files", "Unzip the course files"),
            ("check", "Check your knowledge"),
            ("summary", "Summary"),
        ],
        "base": "https://learn.microsoft.com/en-us/training/modules/intro-power-bi",
    },
    {
        "slug": "02-access-prepare-power-bi",
        "title": "Access and prepare data for Power BI Desktop",
        "units": [
            ("introduction", "Introduction"),
            ("exercise-load-data", "Exercise - Load data from various sources into Power BI"),
            ("exercise-perform-common-data-cleaning", "Exercise - Perform common data cleaning practices"),
            ("check", "Check your knowledge"),
            ("summary", "Summary"),
        ],
        "base": "https://learn.microsoft.com/en-us/training/modules/access-prepare-power-bi",
    },
    {
        "slug": "03-build-your-first-data-model",
        "title": "Build your first data model and explore the data by using Power BI",
        "units": [
            ("introduction", "Introduction"),
            ("exercise-create-model-explore", "Create model and explore the data"),
            ("exercise-create-relationships", "Create missing relationships and use data visualizations"),
            ("exercise-group-bin", "Group and bin data"),
            ("exercise-create-date-table", "Create a date table"),
            ("knowledge-check", "Check your knowledge"),
            ("summary", "Summary"),
        ],
        "base": "https://learn.microsoft.com/en-us/training/modules/build-your-first-data-model",
    },
    {
        "slug": "04-use-hierarchies-dax-first-data-model",
        "title": "Use hierarchies and DAX in your first data model",
        "units": [
            ("introduction", "Introduction"),
            ("exercise-hierarchy-data-model", "Use hierarchies in your data model"),
            ("exercise-build-matrix-visual", "Build a matrix visual"),
            ("exercise-build-dax-measure", "Build DAX measures"),
            ("knowledge-check", "Knowledge check"),
            ("summary", "Summary"),
        ],
        "base": "https://learn.microsoft.com/en-us/training/modules/use-hierarchies-dax-first-data-model",
    },
    {
        "slug": "05-data-visualization-reports-power-bi",
        "title": "Data visualization and reports in Power BI",
        "units": [
            ("introduction", "Introduction"),
            ("apply-conditional", "Apply conditional formatting"),
            ("exercise-add-logo", "Exercise - Add a logo to the manufacturer filter"),
            ("exercise-apply-custom", "Exercise - Apply a custom report theme"),
            ("check", "Check your knowledge"),
            ("summary", "Summary"),
        ],
        "base": "https://learn.microsoft.com/en-us/training/modules/data-visualization-reports-power-bi",
    },
    {
        "slug": "06-import-custom-visuals",
        "title": "Import custom visuals and add bookmarks to a report in Power BI",
        "units": [
            ("introduction", "Introduction"),
            ("exercise-import", "Exercise - Import custom visuals"),
            ("exercise-add-bookmarks", "Exercise - Add bookmarks to a report"),
            ("check", "Check your knowledge"),
            ("summary", "Summary"),
        ],
        "base": "https://learn.microsoft.com/en-us/training/modules/import-custom-visuals",
    },
    {
        "slug": "07-publish-access-reports",
        "title": "Publish and access reports in Power BI service",
        "units": [
            ("introduction", "Introduction"),
            ("exercise-create-mobile-report-view", "Exercise - Create a mobile report view"),
            ("exercise-publish-report", "Exercise - Publish a report to the Power BI service"),
            ("exercise-build-dashboard", "Exercise - Build a dashboard"),
            ("check", "Check your knowledge"),
            ("summary", "Summary"),
        ],
        "base": "https://learn.microsoft.com/en-us/training/modules/publish-access-reports",
    },
    {
        "slug": "08-interact-share-power-bi",
        "title": "Interact, share, and collaborate Power BI dashboards",
        "units": [
            ("introduction", "Introduction"),
            ("exercise-service-interaction-personalization", "Exercise - Power BI service interaction and personalization"),
            ("exercise-share-apps", "Exercise - Share your work with Power BI apps"),
            ("exercise-access-report-mobile", "Exercise - Access the report from your mobile device"),
            ("check", "Check your knowledge"),
            ("summary", "Summary"),
        ],
        "base": "https://learn.microsoft.com/en-us/training/modules/interact-share-power-bi",
    },
]


class ContentExtractor(HTMLParser):
    """Extract the main learning content from a Microsoft Learn training page."""

    def __init__(self):
        super().__init__()
        self._in_main = False
        self._depth = 0
        self._tag_stack = []
        self._text_parts = []
        self._current_tag = None
        self._skip_tags = {"script", "style", "nav", "footer", "header"}
        self._in_skip = 0
        # Track the unit-inner-content div
        self._in_content = False
        self._content_depth = 0

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        cls = attrs_dict.get("class", "")

        # Look for the unit content area
        if tag == "div" and "unit-inner-content" in cls:
            self._in_content = True
            self._content_depth = 0

        if self._in_content:
            self._content_depth += 1

        if tag in self._skip_tags:
            self._in_skip += 1

        if self._in_content and self._in_skip == 0:
            if tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
                level = int(tag[1])
                self._text_parts.append("\n" + "#" * level + " ")
            elif tag == "p":
                self._text_parts.append("\n\n")
            elif tag == "li":
                self._text_parts.append("\n- ")
            elif tag == "ol":
                self._text_parts.append("\n")
            elif tag == "br":
                self._text_parts.append("\n")
            elif tag == "img":
                alt = attrs_dict.get("alt", "")
                src = attrs_dict.get("src", "")
                if alt or src:
                    self._text_parts.append(f"\n\n![{alt}]({src})\n\n")
            elif tag == "code":
                self._text_parts.append("`")
            elif tag == "pre":
                self._text_parts.append("\n```\n")
            elif tag == "strong" or tag == "b":
                self._text_parts.append("**")
            elif tag == "em" or tag == "i":
                self._text_parts.append("*")
            elif tag == "a":
                href = attrs_dict.get("href", "")
                self._tag_stack.append(("a", href))
                self._text_parts.append("[")
            elif tag == "table":
                self._text_parts.append("\n\n")
            elif tag == "tr":
                self._text_parts.append("| ")
            elif tag == "th" or tag == "td":
                pass  # handled in data
            elif tag == "blockquote":
                self._text_parts.append("\n> ")

        self._current_tag = tag

    def handle_endtag(self, tag):
        if tag in self._skip_tags:
            self._in_skip = max(0, self._in_skip - 1)

        if self._in_content and self._in_skip == 0:
            if tag == "code":
                self._text_parts.append("`")
            elif tag == "pre":
                self._text_parts.append("\n```\n")
            elif tag == "strong" or tag == "b":
                self._text_parts.append("**")
            elif tag == "em" or tag == "i":
                self._text_parts.append("*")
            elif tag == "a":
                if self._tag_stack and self._tag_stack[-1][0] == "a":
                    href = self._tag_stack.pop()[1]
                    self._text_parts.append(f"]({href})")
            elif tag == "tr":
                self._text_parts.append(" |\n")
            elif tag == "th" or tag == "td":
                self._text_parts.append(" | ")
            elif tag == "p":
                self._text_parts.append("\n")

        if self._in_content:
            self._content_depth -= 1
            if self._content_depth <= 0:
                self._in_content = False

    def handle_data(self, data):
        if self._in_content and self._in_skip == 0:
            self._text_parts.append(data)

    def get_content(self):
        text = "".join(self._text_parts)
        # Clean up excessive whitespace
        text = re.sub(r"\n{3,}", "\n\n", text)
        text = re.sub(r"[ \t]+\n", "\n", text)
        return text.strip()


def fetch_page(url: str) -> str:
    """Fetch a URL and return the HTML content."""
    req = Request(url, headers={"User-Agent": "Mozilla/5.0 (DIAD scraper)"})
    with urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8", errors="replace")


def html_to_markdown(html: str) -> str:
    """Extract main content from HTML and convert to markdown."""
    parser = ContentExtractor()
    parser.feed(html)
    return parser.get_content()


def fallback_extract(html: str) -> str:
    """Simpler fallback: strip all tags, keep text."""
    # Find the main content area
    match = re.search(r'class="unit-inner-content"[^>]*>(.*?)</div>\s*</div>\s*<div[^>]*class="unit-', html, re.DOTALL)
    if not match:
        # Try broader match
        match = re.search(r'<main[^>]*>(.*?)</main>', html, re.DOTALL)
    if not match:
        return ""

    content = match.group(1)
    # Strip tags but keep structure
    content = re.sub(r'<h([1-6])[^>]*>', lambda m: '\n' + '#' * int(m.group(1)) + ' ', content)
    content = re.sub(r'</h[1-6]>', '\n', content)
    content = re.sub(r'<p[^>]*>', '\n\n', content)
    content = re.sub(r'</p>', '\n', content)
    content = re.sub(r'<li[^>]*>', '\n- ', content)
    content = re.sub(r'<img[^>]*alt="([^"]*)"[^>]*src="([^"]*)"[^>]*/?\s*>', r'\n\n![\1](\2)\n\n', content)
    content = re.sub(r'<code[^>]*>', '`', content)
    content = re.sub(r'</code>', '`', content)
    content = re.sub(r'<strong[^>]*>', '**', content)
    content = re.sub(r'</strong>', '**', content)
    content = re.sub(r'<em[^>]*>', '*', content)
    content = re.sub(r'</em>', '*', content)
    content = re.sub(r'<[^>]+>', '', content)
    content = re.sub(r'\n{3,}', '\n\n', content)
    return content.strip()


def main():
    output_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).parent.parent / "diad-learn-content"
    output_dir.mkdir(parents=True, exist_ok=True)

    # Create index file
    index_lines = ["# Dashboard in a Day - Online Workshop\n\n"]
    index_lines.append("Source: https://learn.microsoft.com/en-us/training/paths/dashboard-in-a-day/\n\n")

    total_units = sum(len(m["units"]) for m in MODULES)
    fetched = 0

    for mod in MODULES:
        mod_dir = output_dir / mod["slug"]
        mod_dir.mkdir(parents=True, exist_ok=True)

        index_lines.append(f"## {mod['title']}\n\n")

        for unit_slug, unit_title in mod["units"]:
            fetched += 1
            url = f"{mod['base']}/{unit_slug}"
            filename = f"{unit_slug}.md"
            filepath = mod_dir / filename

            print(f"[{fetched}/{total_units}] Fetching: {unit_title} ...")
            sys.stdout.flush()

            try:
                html = fetch_page(url)
                content = html_to_markdown(html)

                if len(content) < 100:
                    content = fallback_extract(html)

                # Add header
                md = f"# {unit_title}\n\n"
                md += f"*Source: [{url}]({url})*\n\n"
                md += f"---\n\n"
                md += content
                md += "\n"

                filepath.write_text(md, encoding="utf-8")
                index_lines.append(f"- [{unit_title}]({mod['slug']}/{filename})\n")

                print(f"  -> Saved {filepath.name} ({len(content):,} chars)")

            except Exception as e:
                print(f"  ** ERROR: {e}")
                index_lines.append(f"- [{unit_title}]({mod['slug']}/{filename}) *(fetch failed)*\n")

            # Be polite
            time.sleep(0.5)

        index_lines.append("\n")

    # Write index
    index_path = output_dir / "README.md"
    index_path.write_text("".join(index_lines), encoding="utf-8")
    print(f"\nDone! Index written to {index_path}")
    print(f"Content saved to {output_dir}")


if __name__ == "__main__":
    main()
