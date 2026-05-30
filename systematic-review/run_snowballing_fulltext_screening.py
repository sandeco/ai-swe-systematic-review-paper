from __future__ import annotations

import csv
import json
from collections import Counter
from datetime import datetime
from pathlib import Path


BASE = Path(r"C:\SCIENTEX\_papers\ai-dev-frameworks-review\systematic-review")
RESULTS = BASE / "search-results.json"
EXTRACTS = BASE / "pdf-extracts"
SCREENING = BASE / "screening"
LOG = SCREENING / "full-text.log.csv"
SUMMARY = SCREENING / "exclusion-reasons.md"
ROUND_SUMMARY = BASE / "snowballing" / "round-1" / "fulltext-summary.md"
DISCOVERY = "snowballing-1"
RUN_LOCAL = datetime.now().strftime("%Y-%m-%d %H:%M")
RUN_ISO = datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")


DECISIONS = {
    "JulesWhite2023": (
        "include",
        "I1",
        "Texto completo apresenta metodo reutilizavel de prompt patterns para varias atividades de engenharia de software, incluindo requisitos, design, prototipacao, qualidade de codigo, deployment e testes.",
    ),
    "ChristophTreude2025": (
        "exclude",
        "missing I2/I3/I4",
        "Texto completo fornece taxonomia de interacoes desenvolvedor-IA, mas nao descreve artefatos persistentes, papeis, workflow executavel ou validacao operacional suficientes para extracao como framework de desenvolvimento.",
    ),
    "JundaHe2025": (
        "include",
        "I1",
        "Texto completo revisa sistemas multiagente baseados em LLM para engenharia de software, organiza aplicacoes por etapas do SDLC, discute frameworks LMA e inclui estudos de caso.",
    ),
    "JSauvola2024": (
        "include",
        "I1",
        "Texto completo propoe quatro cenarios para operacoes de desenvolvimento com IA generativa, modelando papeis, ferramentas, processos, transicoes e riscos operacionais.",
    ),
    "AyyappaSajja2024": (
        "exclude",
        "missing I1",
        "Texto completo discute impactos gerais da IA generativa em codigo, documentacao, manutencao e produtividade, mas nao apresenta framework, metodo, toolkit, plataforma, IDE, CLI ou kit operacional.",
    ),
    "MitulModi2024": (
        "include",
        "I1",
        "Texto completo apresenta analise sistematica e framework de adocao de GenAI em workflows de desenvolvimento, cobrindo geracao de codigo, testes, code review e analise preditiva.",
    ),
    "ShreyasPangavhane2024": (
        "exclude",
        "E2",
        "Texto completo descreve beneficios de ferramentas AI-augmented e assistentes de codigo, mas nao define workflow proprio, artefatos persistentes, papeis ou validacao propria.",
    ),
    "KRRaghi2024": (
        "include",
        "I1",
        "Texto completo apresenta abordagem multi-etapa para automacao do SDLC com LLMs e LangChain, cobrindo planejamento, requisitos, codigo, testes e deployment.",
    ),
    "DanielRusso2024": (
        "include",
        "I1",
        "Texto completo propoe e valida o Human-AI Collaboration and Adaptation Framework para adocao de IA generativa em engenharia de software, incluindo fatores de workflow e estrategias organizacionais.",
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
    marker = "## Passada 2b (snowballing rodada 1, full text)"
    if marker in lines:
        lines = lines[:lines.index(marker)]
    while lines and lines[-1] == "":
        lines.pop()

    descriptions = {
        "missing I1": "Fora do foco operacional: texto completo discute IA generativa em software, mas nao descreve framework, metodo, toolkit, plataforma, IDE, CLI ou kit operacional.",
        "missing I2/I3/I4": "Falta de estrutura minima: texto completo nao apresenta pelo menos dois entre artefatos persistentes, papeis, workflow, integracao ou validacao.",
        "E2": "Assistente generico ou conjunto de ferramentas: texto completo nao define workflow proprio, artefatos persistentes, papeis ou validacao propria.",
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
        f"**Total full text snowballing rodada 1**: {len(excluded)} excluidos de {len(rows)} analisados ({(len(excluded) / len(rows)) * 100:.1f}%).",
        "",
        "### Incluidos finais adicionais apos snowballing",
        "",
        "| Citation key | Ano | Titulo |",
        "|---|---:|---|",
    ])
    for row in included:
        lines.append(f"| {row['citation_key']} | {row['year']} | {row['title'].replace('|', '/')} |")
    SUMMARY.write_text("\n".join(lines) + "\n", encoding="utf-8")

    round_lines = [
        "# Full Text Screening Snowballing Round 1",
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
