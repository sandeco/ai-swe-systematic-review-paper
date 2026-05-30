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
ROUND_SUMMARY = BASE / "snowballing" / "round-2" / "fulltext-summary.md"
DISCOVERY = "snowballing-2"
RUN_LOCAL = "2026-05-28 13:36"
RUN_ISO = "2026-05-28T13:36:00Z"


DECISIONS = {
    "YuntongZhang2024": (
        "include",
        "I1",
        "Texto completo apresenta AutoCodeRover como framework de program improvement com agentes de recuperacao de contexto e geracao de patch, busca estrutural no codigo, uso opcional de testes e validacao de patches.",
    ),
    "ZeeshanRasheed2024": (
        "include",
        "I1",
        "Texto completo apresenta CodePori como sistema multiagente para desenvolvimento autonomo de software em larga escala, com agentes de gerencia, arquitetura, estrutura, desenvolvimento, verificacao e finalizacao.",
    ),
    "HuanZhang2024": (
        "exclude",
        "E3",
        "Texto completo apresenta PairCoder como framework agentico para code generation, mas o escopo permanece restrito a uma tarefa isolada de geracao de codigo avaliada em benchmarks, sem processo amplo de desenvolvimento.",
    ),
    "SaiZhang2025": (
        "include",
        "I1",
        "Texto completo apresenta AgileGen como framework agile de desenvolvimento generativo humano-IA, com criterios de aceitacao em Gherkin, artefatos de requisitos, decisao humana, memoria e iteracao ate validacao.",
    ),
    "pekzkaya2023": (
        "exclude",
        "E7",
        "Texto completo e um comentario editorial sobre processos de desenvolvimento aumentados por IA, sem especificar framework, metodo operacional, papeis, artefatos ou validacao extraiveis.",
    ),
}


def clean(value: object) -> str:
    if value is None:
        return ""
    text = str(value)
    replacements = {
        "\u2014": "-",
        "\u2013": "-",
        "\u2018": "'",
        "\u2019": "'",
        "\u201c": '"',
        "\u201d": '"',
        "\u00a0": " ",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return " ".join(text.split())


def main() -> None:
    data = json.loads(RESULTS.read_text(encoding="utf-8-sig"))
    targets = [
        entry for entry in data
        if (entry.get("systematic_review") or {}).get("discovery") == DISCOVERY
        and (entry.get("screening_pass1") or {}).get("decision") == "include"
    ]

    rows = []
    for entry in targets:
        key = entry.get("citation_key")
        extract = EXTRACTS / f"{key}.md"
        if not extract.exists():
            decision = "exclude"
            criterion = "E_no_fulltext"
            reason = "Texto completo indisponivel em papers_to_review ou pdf-extracts."
        else:
            decision, criterion, reason = DECISIONS[key]

        entry["screening_pass2"] = {
            "decision": decision,
            "criterion": criterion,
            "reason": reason,
            "reviewer": "screening-logger",
            "timestamp": RUN_ISO,
            "screening_scope": DISCOVERY,
        }
        rows.append({
            "citation_key": key,
            "title": clean(entry.get("title")),
            "year": entry.get("year") or "",
            "decision": decision,
            "criterion": criterion,
            "reason": reason,
            "reviewer": "screening-logger",
            "timestamp": RUN_ISO,
        })

    with LOG.open("a", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(
            fh,
            fieldnames=["citation_key", "title", "year", "decision", "criterion", "reason", "reviewer", "timestamp"],
        )
        writer.writerows(rows)

    RESULTS.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    included = [row for row in rows if row["decision"] == "include"]
    excluded = [row for row in rows if row["decision"] == "exclude"]
    counts = Counter(row["criterion"] for row in excluded)

    lines = SUMMARY.read_text(encoding="utf-8-sig").splitlines() if SUMMARY.exists() else []
    marker = "## Passada 2c (snowballing rodada 2, full text)"
    if marker in lines:
        lines = lines[:lines.index(marker)]
    while lines and lines[-1] == "":
        lines.pop()

    descriptions = {
        "E3": "Tarefa isolada de engenharia de software: texto completo descreve um framework ou tecnica restrita a uma tarefa pontual, sem processo amplo de desenvolvimento.",
        "E7": "Conteudo insuficientemente operacional: texto completo e comentario, editorial ou ensaio sem detalhes tecnicos suficientes para extracao como framework.",
        "E_no_fulltext": "Texto completo indisponivel.",
    }

    lines.extend([
        "",
        marker,
        "",
        "| Motivo de exclusao | Criterio | N excluidos |",
        "|---|---|---:|",
    ])
    for criterion, count in sorted(counts.items()):
        lines.append(f"| {descriptions.get(criterion, criterion)} | {criterion} | {count} |")
    lines.extend([
        "",
        f"**Total full text snowballing rodada 2**: {len(excluded)} excluidos de {len(rows)} analisados ({(len(excluded) / len(rows)) * 100:.1f}%).",
        "",
        "### Incluidos finais adicionais apos snowballing rodada 2",
        "",
        "| Citation key | Ano | Titulo |",
        "|---|---:|---|",
    ])
    for row in included:
        lines.append(f"| {row['citation_key']} | {row['year']} | {row['title'].replace('|', '/')} |")
    lines.extend([
        "",
        "## Resumo consolidado apos snowballing rodada 2",
        "",
        "- Identificados na busca inicial: 100",
        "- Apos dedup, filtro temporal e seed dirigido: 85",
        "- Incluidos finais apos busca inicial e full text: 25",
        "- Candidatos novos adicionados por snowballing rodada 1: 69",
        "- Excluidos na triagem titulo e abstract do snowballing rodada 1: 60",
        "- Textos completos analisados no snowballing rodada 1: 9",
        "- Excluidos no full text do snowballing rodada 1: 3",
        "- Incluidos finais adicionais por snowballing rodada 1: 6",
        "- Candidatos novos adicionados por snowballing rodada 2: 50",
        "- Excluidos na triagem titulo e abstract do snowballing rodada 2: 45",
        "- Textos completos analisados no snowballing rodada 2: 5",
        "- Excluidos no full text do snowballing rodada 2: 2",
        "- Incluidos finais adicionais por snowballing rodada 2: 3",
        "- Incluidos finais consolidados: 34",
    ])
    SUMMARY.write_text("\n".join(lines) + "\n", encoding="utf-8")

    round_lines = [
        "# Full Text Screening Snowballing Round 2",
        "",
        f"> Executado em: {RUN_LOCAL}",
        f"> Escopo: `{DISCOVERY}`",
        "",
        "## Resultado",
        "",
        f"- Textos completos analisados: {len(rows)}",
        f"- Incluidos finais adicionais: {len(included)}",
        f"- Excluidos em full text: {len(excluded)}",
        "",
        "## Excluidos por criterio",
        "",
        "| Criterio | N |",
        "|---|---:|",
    ]
    for criterion, count in sorted(counts.items()):
        round_lines.append(f"| {criterion} | {count} |")
    round_lines.extend([
        "",
        "## Incluidos finais adicionais",
        "",
        "| Citation key | Ano | Titulo |",
        "|---|---:|---|",
    ])
    for row in included:
        round_lines.append(f"| {row['citation_key']} | {row['year']} | {row['title'].replace('|', '/')} |")
    round_lines.extend([
        "",
        "## Excluidos",
        "",
        "| Citation key | Criterio | Motivo |",
        "|---|---|---|",
    ])
    for row in excluded:
        round_lines.append(f"| {row['citation_key']} | {row['criterion']} | {row['reason'].replace('|', '/')} |")
    ROUND_SUMMARY.write_text("\n".join(round_lines) + "\n", encoding="utf-8")

    print(json.dumps({
        "scope": DISCOVERY,
        "analyzed": len(rows),
        "include": len(included),
        "exclude": len(excluded),
        "exclude_by_criterion": dict(counts),
        "summary": str(ROUND_SUMMARY),
    }, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
