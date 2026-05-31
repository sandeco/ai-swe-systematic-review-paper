from __future__ import annotations

import json
from collections import Counter
from pathlib import Path


BASE = Path(r"C:\SCIENTEX\_papers\ai-dev-frameworks-review\systematic-review")
RESULTS = BASE / "search-results.json"
LOG = BASE / "papers_to_review" / "_acquisition.log.json"
OUT = BASE / "snowballing" / "round-3" / "acquisition-summary.md"
RUN_LOCAL = "2026-05-28 13:52"


def clean(value: object) -> str:
    if value is None:
        return ""
    return str(value).replace("\u2014", "-").replace("\u2013", "-").replace("|", "/")


def acquisition_status(record: dict) -> str:
    if not record.get("success"):
        return "manual_required"
    if record.get("method") == "already_present":
        return "already_present"
    return "downloaded"


def main() -> None:
    data = json.loads(RESULTS.read_text(encoding="utf-8-sig"))
    records = json.loads(LOG.read_text(encoding="utf-8-sig"))
    by_key = {record["citation_key"]: record for record in records}

    for entry in data:
        key = entry.get("citation_key")
        record = by_key.get(key)
        if not record:
            continue
        entry["acquisition"] = {
            "success": bool(record.get("success")),
            "method": record.get("method"),
            "saved_path": record.get("saved_path") or "",
            "ext": record.get("ext"),
            "timestamp": RUN_LOCAL,
            "status": acquisition_status(record),
        }

    RESULTS.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    snow = [
        entry for entry in data
        if (entry.get("systematic_review") or {}).get("discovery") == "snowballing-3"
        and (entry.get("screening_pass1") or {}).get("decision") == "include"
    ]
    counts = Counter((entry.get("acquisition") or {}).get("method") for entry in snow)
    acquired = [entry for entry in snow if (entry.get("acquisition") or {}).get("success")]
    manual = [entry for entry in snow if not (entry.get("acquisition") or {}).get("success")]

    lines = [
        "# Acquisition Snowballing Round 3",
        "",
        f"> Executado em: {RUN_LOCAL}",
        "> Escopo: `snowballing-3` incluidos apos screening por titulo e abstract",
        "",
        "## Resultado",
        "",
        f"- Candidatos para texto completo: {len(snow)}",
        f"- Baixados ou ja presentes: {len(acquired)}",
        f"- Para download manual: {len(manual)}",
        "",
        "## Metodo de aquisicao",
        "",
        "| Metodo | N |",
        "|---|---:|",
    ]
    for method, count in sorted(counts.items()):
        lines.append(f"| {method or 'unknown'} | {count} |")

    lines.extend([
        "",
        "## Baixados ou ja presentes",
        "",
        "| Citation key | Metodo | Arquivo |",
        "|---|---|---|",
    ])
    for entry in acquired:
        acq = entry.get("acquisition") or {}
        saved = Path(acq.get("saved_path") or "").name
        lines.append(f"| {entry.get('citation_key')} | {acq.get('method')} | {saved} |")

    lines.extend([
        "",
        "## Download manual necessario",
        "",
        "| Citation key | Ano | Titulo | DOI |",
        "|---|---:|---|---|",
    ])
    for entry in manual:
        doi = entry.get("doi") or ""
        doi_url = f"https://doi.org/{doi}" if doi else ""
        lines.append(f"| {entry.get('citation_key')} | {entry.get('year') or ''} | {clean(entry.get('title'))} | {doi_url} |")

    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(json.dumps({
        "scope": "snowballing-3",
        "total": len(snow),
        "downloaded_or_present": len(acquired),
        "manual_required": len(manual),
        "methods": dict(counts),
        "summary": str(OUT),
    }, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
