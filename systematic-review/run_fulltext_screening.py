from __future__ import annotations

import csv
import json
from collections import Counter
from pathlib import Path


BASE = Path(r"C:\SCIENTEX\_papers\ai-dev-frameworks-review\systematic-review")
RESULTS = BASE / "search-results.json"
EXTRACTS = BASE / "pdf-extracts"
SCREENING = BASE / "screening"
LOG = SCREENING / "full-text.log.csv"
SUMMARY = SCREENING / "exclusion-reasons.md"
TIMESTAMP = "2026-05-27T17:59:00Z"


EXCLUDE = {
    "AkhilaHarinarayana2026": (
        "E7",
        "Texto completo tem apenas uma pagina de resumo de conferencia, sem detalhes tecnicos suficientes para extrair arquitetura, artefatos, papeis, validacao e riscos.",
    ),
    "AshifAnwar2025": (
        "missing I1",
        "Texto completo sintetiza praticas gerais e tendencias de IA no SDLC, mas nao descreve framework, metodo, toolkit, plataforma, IDE, CLI ou kit especifico.",
    ),
    "NitishRatanAppanasamy2025": (
        "missing I1",
        "Texto completo discute oportunidades e impactos gerais da colaboracao com IA, mas nao descreve um framework operacional de desenvolvimento com IA.",
    ),
}


def clean(value):
    if value is None:
        return ""
    text = str(value)
    return text.replace("\u2014", "-").replace("\u2013", "-")


def include_reason(key):
    return "Texto completo confirma fonte dentro do escopo: descreve framework, metodo, plataforma, arquitetura, workflow, artefatos, validacao ou evidencia diretamente relacionada ao desenvolvimento de software com IA."


def main() -> None:
    data = json.load(open(RESULTS, encoding="utf-8-sig"))
    included = [entry for entry in data if (entry.get("screening_pass1") or {}).get("decision") == "include"]
    rows = []

    for entry in included:
        key = entry.get("citation_key")
        extract = EXTRACTS / f"{key}.md"
        if not extract.exists():
            decision = "exclude"
            criterion = "E_no_fulltext"
            reason = "Texto completo indisponivel em papers_to_review ou pdf-extracts."
        elif key in EXCLUDE:
            decision = "exclude"
            criterion, reason = EXCLUDE[key]
        else:
            decision = "include"
            criterion = "I1"
            reason = include_reason(key)

        entry["screening_pass2"] = {
            "decision": decision,
            "criterion": criterion,
            "reason": reason,
            "reviewer": "screening-logger",
            "timestamp": TIMESTAMP,
        }
        rows.append({
            "citation_key": key,
            "title": clean(entry.get("title")),
            "year": entry.get("year") or "",
            "decision": decision,
            "criterion": criterion,
            "reason": reason,
            "reviewer": "screening-logger",
            "timestamp": TIMESTAMP,
        })

    write_header = not LOG.exists() or LOG.stat().st_size == 0
    with LOG.open("a", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=["citation_key", "title", "year", "decision", "criterion", "reason", "reviewer", "timestamp"])
        if write_header:
            writer.writeheader()
        writer.writerows(rows)

    json.dump(data, open(RESULTS, "w", encoding="utf-8"), indent=2, ensure_ascii=False)

    pass1_excluded = [entry for entry in data if (entry.get("screening_pass1") or {}).get("decision") == "exclude"]
    pass2_included = [entry for entry in data if (entry.get("screening_pass2") or {}).get("decision") == "include"]
    pass2_excluded = [entry for entry in data if (entry.get("screening_pass2") or {}).get("decision") == "exclude"]
    pass2_counts = Counter((entry.get("screening_pass2") or {}).get("criterion") for entry in pass2_excluded)

    lines = SUMMARY.read_text(encoding="utf-8-sig").splitlines() if SUMMARY.exists() else []
    # Keep everything up to the pass 2 section if this script is rerun.
    if "## Passada 2 (full text)" in lines:
        lines = lines[:lines.index("## Passada 2 (full text)")]
    while lines and lines[-1] == "":
        lines.pop()
    lines.extend([
        "",
        "## Passada 2 (full text)",
        "",
        "| Motivo de exclusao | Criterio | N excluidos |",
        "|---|---|---:|",
    ])
    descriptions = {
        "E7": "Texto completo insuficiente: resumo, artigo curto ou conteudo sem detalhes tecnicos suficientes para extracao estruturada.",
        "missing I1": "Fora do foco operacional: texto completo nao descreve framework, metodo, toolkit, plataforma, IDE, CLI ou kit de desenvolvimento de software com IA.",
        "E_no_fulltext": "Texto completo indisponivel.",
    }
    for criterion, n in sorted(pass2_counts.items()):
        lines.append(f"| {descriptions.get(criterion, criterion)} | {criterion} | {n} |")
    lines.extend([
        "",
        f"**Total passada 2**: {len(pass2_excluded)} excluidos de {len(included)} analisados ({(len(pass2_excluded) / len(included)) * 100:.1f}%).",
        "",
        "## Incluidos finais apos full text",
        "",
        "| Citation key | Ano | Titulo |",
        "|---|---:|---|",
    ])
    for entry in pass2_included:
        title = clean(entry.get("title")).replace("|", "/")
        lines.append(f"| {entry.get('citation_key')} | {entry.get('year') or ''} | {title} |")
    lines.extend([
        "",
        "## Resumo atualizado dos numeros para flow diagram",
        "",
        "- Identificados na busca: 100",
        "- Apos dedup, filtro temporal e seed dirigido: 85",
        f"- Excluidos passada 1: {len(pass1_excluded)}",
        f"- Restantes pos passada 1: {len(included)}",
        f"- Excluidos passada 2: {len(pass2_excluded)}",
        f"- Incluidos finais: {len(pass2_included)}",
    ])
    SUMMARY.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(json.dumps({
        "full_text_analyzed": len(included),
        "include": len(pass2_included),
        "exclude": len(pass2_excluded),
        "exclude_by_criterion": dict(pass2_counts),
    }, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
