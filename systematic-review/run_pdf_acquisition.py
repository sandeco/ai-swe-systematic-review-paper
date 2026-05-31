from __future__ import annotations

import json
import os
import requests
import sys
import time
from datetime import datetime
from pathlib import Path

sys.path.insert(0, r"C:\SCIENTEX\.agents\skills\scientex\scripts")

from related_work.acquisition import try_acquire_open_access


BASE = Path(r"C:\SCIENTEX\_papers\ai-dev-frameworks-review\systematic-review")
RESULTS = BASE / "search-results.json"
OUT = BASE / "papers_to_review"
LOG = OUT / "_acquisition.log.json"
MANUAL = OUT / "_manual-fetch-required.md"
GENERATED_AT = datetime.now().strftime("%Y-%m-%d %H:%M")


def sanitize(value):
    if value is None:
        return ""
    text = str(value)
    return text.replace("\u2014", "-").replace("\u2013", "-")


def load_results():
    with RESULTS.open(encoding="utf-8-sig") as fh:
        return json.load(fh)


def existing_file(key: str):
    for ext in ("pdf", "html"):
        path = OUT / f"{key}.{ext}"
        if path.exists() and path.stat().st_size > 5000:
            return path
    return None


def acquire_arxiv_direct(entry, key: str):
    doi = entry.get("doi") or ""
    if not doi.lower().startswith("10.48550/arxiv."):
        return None
    arxiv_id = doi.split("arXiv.", 1)[-1] if "arXiv." in doi else doi.split("arxiv.", 1)[-1]
    arxiv_id = arxiv_id.strip()
    if not arxiv_id:
        return None
    url = f"https://arxiv.org/pdf/{arxiv_id}.pdf"
    dest = OUT / f"{key}.pdf"
    try:
        response = requests.get(url, timeout=60, stream=True, headers={"User-Agent": "SCIENTEX/0.1"})
        if not response.ok:
            return {
                "success": False,
                "method": "arxiv_direct_failed",
                "saved_path": None,
                "ext": None,
                "attempts": [{"step": "arxiv_direct", "ok": False, "note": f"HTTP {response.status_code}: {url}"}],
            }
        content_type = response.headers.get("content-type", "").lower()
        if "pdf" not in content_type and "octet-stream" not in content_type:
            return {
                "success": False,
                "method": "arxiv_direct_failed",
                "saved_path": None,
                "ext": None,
                "attempts": [{"step": "arxiv_direct", "ok": False, "note": f"not a PDF: {url}"}],
            }
        with dest.open("wb") as fh:
            for chunk in response.iter_content(8192):
                fh.write(chunk)
        if dest.stat().st_size < 5000:
            dest.unlink(missing_ok=True)
            return {
                "success": False,
                "method": "arxiv_direct_failed",
                "saved_path": None,
                "ext": None,
                "attempts": [{"step": "arxiv_direct", "ok": False, "note": f"too small: {url}"}],
            }
        return {
            "success": True,
            "method": "arxiv_direct",
            "saved_path": str(dest),
            "ext": "pdf",
            "attempts": [{"step": "arxiv_direct", "ok": True, "note": url}],
        }
    except Exception as exc:
        return {
            "success": False,
            "method": "arxiv_direct_failed",
            "saved_path": None,
            "ext": None,
            "attempts": [{"step": "arxiv_direct", "ok": False, "note": str(exc)}],
        }


def acquisition_record(entry, result):
    return {
        "citation_key": entry.get("citation_key"),
        "title": sanitize(entry.get("title")),
        "year": entry.get("year"),
        "venue": sanitize(entry.get("venue")),
        "doi": entry.get("doi"),
        "doi_url": entry.get("doi_url") or (f"https://doi.org/{entry.get('doi')}" if entry.get("doi") else None),
        "success": bool(result.get("success")),
        "method": result.get("method"),
        "saved_path": sanitize(result.get("saved_path")),
        "ext": result.get("ext"),
        "attempts": result.get("attempts") or [],
    }


def write_manual(manual_records, no_doi_records):
    lines = [
        "# Papers que precisam de download manual",
        "",
        f"> Gerado em: {GENERATED_AT}",
        f"> Total: {len(manual_records) + len(no_doi_records)} papers",
        "> Razao da nao automacao: paper fechado ou DOI ausente",
        "",
        "A cascata tentou Unpaywall, Semantic Scholar OA, preprint servers, OpenAlex OA, Crossref link, HTML fetch direto e Zenodo. Nenhuma encontrou versao publica para os itens listados como closed.",
        "",
        "## Como baixar",
        "",
        "1. Abra o link DOI abaixo.",
        "2. Se houver acesso institucional, baixe o PDF diretamente.",
        "3. Salve o PDF em `_papers/ai-dev-frameworks-review/systematic-review/papers_to_review/<citation_key>.pdf`.",
        "4. Use exatamente o `citation_key` como nome do arquivo.",
        "5. Depois digite `CONTINUE` para seguir para screening full text.",
        "",
        "## Lista",
        "",
        "| # | Citation key | Titulo | Ano | Venue | DOI | Razao |",
        "|---:|---|---|---:|---|---|---|",
    ]
    for idx, rec in enumerate(manual_records, 1):
        doi = rec.get("doi")
        doi_url = f"https://doi.org/{doi}" if doi else ""
        title = sanitize(rec.get("title")).replace("|", "/")
        venue = sanitize(rec.get("venue")).replace("|", "/")
        lines.append(
            f"| {idx} | {rec.get('citation_key')} | {title} | {rec.get('year') or ''} | {venue} | {doi_url} | closed |"
        )

    lines += [
        "",
        "## Papers sem DOI",
        "",
        "| Citation key | Titulo | Ano | Notas |",
        "|---|---|---:|---|",
    ]
    for rec in no_doi_records:
        title = sanitize(rec.get("title")).replace("|", "/")
        lines.append(f"| {rec.get('citation_key')} | {title} | {rec.get('year') or ''} | DOI ausente em search-results.json |")

    MANUAL.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    entries = [e for e in load_results() if (e.get("screening_pass1") or {}).get("decision") == "include"]
    records = []
    manual_records = []
    no_doi_records = []

    for index, entry in enumerate(entries, 1):
        key = entry.get("citation_key")
        doi = entry.get("doi")
        title = entry.get("title")
        present = existing_file(key)
        if present:
            result = {
                "success": True,
                "method": "already_present",
                "saved_path": str(present),
                "ext": present.suffix.lstrip("."),
                "attempts": [{"step": "already_present", "ok": True, "note": str(present)}],
            }
        elif not doi:
            result = {
                "success": False,
                "method": "no_doi",
                "saved_path": None,
                "ext": None,
                "attempts": [{"step": "no_doi", "ok": False, "note": "no DOI to query"}],
            }
        else:
            arxiv_result = acquire_arxiv_direct(entry, key)
            if arxiv_result and arxiv_result.get("success"):
                result = arxiv_result
            else:
                result = try_acquire_open_access(entry, OUT, key)
                if arxiv_result:
                    result.setdefault("attempts", [])
                    result["attempts"] = arxiv_result.get("attempts", []) + result["attempts"]

        rec = acquisition_record(entry, result)
        records.append(rec)
        if not rec["success"]:
            if not doi:
                no_doi_records.append(rec)
            else:
                manual_records.append(rec)
        print(f"[{index}/{len(entries)}] {key}: {rec['method']}")
        time.sleep(1)

    LOG.write_text(json.dumps(records, indent=2, ensure_ascii=False), encoding="utf-8")
    write_manual(manual_records, no_doi_records)
    print(json.dumps({
        "total": len(entries),
        "acquired": sum(1 for r in records if r["success"]),
        "manual": len(manual_records),
        "no_doi": len(no_doi_records),
        "out": str(OUT),
    }, indent=2))


if __name__ == "__main__":
    main()
