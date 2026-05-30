from __future__ import annotations

import json
import re
from pathlib import Path

from bs4 import BeautifulSoup
from pypdf import PdfReader
from datetime import datetime


BASE = Path(r"C:\SCIENTEX\_papers\ai-dev-frameworks-review\systematic-review")
RESULTS = BASE / "search-results.json"
PAPERS = BASE / "papers_to_review"
OUT = BASE / "pdf-extracts"


def normalize_text(text: str) -> str:
    text = text.replace("\u2014", "-").replace("\u2013", "-")
    text = text.replace("\u2018", "'").replace("\u2019", "'")
    text = text.replace("\u201c", '"').replace("\u201d", '"')
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def extract_pdf(path: Path) -> tuple[str, int]:
    reader = PdfReader(str(path))
    pages = []
    for page in reader.pages:
        try:
            pages.append(page.extract_text() or "")
        except Exception:
            pages.append("")
    return normalize_text("\n\n".join(pages)), len(reader.pages)


def extract_html(path: Path) -> tuple[str, int]:
    soup = BeautifulSoup(path.read_text(encoding="utf-8", errors="ignore"), "html.parser")
    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()
    text = soup.get_text("\n")
    return normalize_text(text), 1


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    data = json.load(open(RESULTS, encoding="utf-8-sig"))
    included = [entry for entry in data if (entry.get("screening_pass1") or {}).get("decision") == "include"]
    index_lines = [
        "# Full Text Extraction Index",
        "",
        f"> Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "",
        "| Citation key | Source file | Pages | Characters | Status |",
        "|---|---|---:|---:|---|",
    ]
    for entry in included:
        key = entry.get("citation_key")
        source = None
        for ext in ("pdf", "html"):
            candidate = PAPERS / f"{key}.{ext}"
            if candidate.exists():
                source = candidate
                break
        if not source:
            index_lines.append(f"| {key} | missing | 0 | 0 | missing |")
            continue
        try:
            if source.suffix.lower() == ".pdf":
                text, pages = extract_pdf(source)
            else:
                text, pages = extract_html(source)
            out_path = OUT / f"{key}.md"
            content = [
                f"# {key}",
                "",
                f"- **Title**: {normalize_text(entry.get('title') or '')}",
                f"- **Year**: {entry.get('year') or ''}",
                f"- **DOI**: {entry.get('doi') or ''}",
                f"- **Source file**: `{source.name}`",
                f"- **Pages**: {pages}",
                "",
                "## Extracted text",
                "",
                text,
                "",
            ]
            out_path.write_text("\n".join(content), encoding="utf-8")
            index_lines.append(f"| {key} | {source.name} | {pages} | {len(text)} | ok |")
        except Exception as exc:
            index_lines.append(f"| {key} | {source.name} | 0 | 0 | error: {normalize_text(str(exc))} |")
    (OUT / "_index.md").write_text("\n".join(index_lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
