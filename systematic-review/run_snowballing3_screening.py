from __future__ import annotations

import csv
import json
from collections import Counter
from pathlib import Path


BASE = Path(r"C:\SCIENTEX\_papers\ai-dev-frameworks-review\systematic-review")
RESULTS = BASE / "search-results.json"
SCREENING = BASE / "screening"
LOG = SCREENING / "title-abstract.log.csv"
SUMMARY = SCREENING / "exclusion-reasons.md"
ROUND_SUMMARY = BASE / "snowballing" / "round-3" / "screening-summary.md"
DISCOVERY = "snowballing-3"
RUN_LOCAL = "2026-05-28 13:44"
TIMESTAMP = "2026-05-28T13:44:00Z"


INCLUDE = {
    "ChenQian2023": (
        "I1",
        "Titulo e abstract descrevem ChatDev como framework de desenvolvimento de software com agentes especializados, chat chain, design, coding, testing e comunicacao multi-turn.",
    ),
    "SiruiHong2023": (
        "I1",
        "Titulo e abstract descrevem MetaGPT como framework multiagente colaborativo que codifica SOPs, papeis, workflows e verificacao de resultados intermediarios para engenharia de software.",
    ),
    "YuCheng2023": (
        "I1",
        "Titulo e abstract descrevem Prompt Sapper como metodologia de AI chain engineering e IDE no-code para construir servicos de IA reutilizaveis com principios e padroes de engenharia de software.",
    ),
    "AshaRajbhoj2024": (
        "I1",
        "Titulo e abstract apresentam abordagem sistematica de prompting baseada em meta-modelos para fases do SDLC, validada em desenvolvimento de aplicacao com ChatGPT.",
    ),
}


EXCLUDE = {
    "AlexandruMarginean2019": (
        "E3",
        "Titulo e abstract descrevem reparo automatizado de falhas em escala, mas restrito a fault fixing sem framework amplo de desenvolvimento com IA.",
    ),
    "XiangGao2019": (
        "E3",
        "Titulo e abstract focam reparo de programas para evitar crashes, uma tarefa isolada de program repair sem processo amplo de desenvolvimento com IA.",
    ),
    "AnilKoyuncu2019": (
        "E3",
        "Titulo e abstract descrevem pipeline de program repair guiado por bug reports, restrito a reparo de defeitos sem framework amplo de desenvolvimento com IA.",
    ),
    "QihaoZhu2021": (
        "E3",
        "Titulo e abstract focam decoder neural para program repair, uma tecnica de reparo isolada sem framework amplo de desenvolvimento.",
    ),
    "YujiaLi2022": (
        "E1",
        "Titulo e abstract descrevem AlphaCode como sistema de geracao de codigo para competicoes, sem workflow de desenvolvimento de software ou artefatos persistentes.",
    ),
    "MichaelCFu2022": (
        "E3",
        "Titulo e abstract focam reparo automatizado de vulnerabilidades, uma tarefa especifica de seguranca de software.",
    ),
    "ManishMotwani2023": (
        "E3",
        "Titulo e abstract focam program repair usando bug reports e testes, uma tarefa especifica de manutencao.",
    ),
    "ZhiyuFan2023": (
        "E3",
        "Titulo e abstract focam reparo de programas gerados por LLMs, uma tarefa especifica para melhorar codigo gerado.",
    ),
    "WeishiWang2023": (
        "E3",
        "Titulo e abstract descrevem patch generation para automatic program repair, restrito a uma tarefa de reparo.",
    ),
    "PengchengYin2018": (
        "E3",
        "Titulo e abstract tratam parsing semantico e code generation, uma tecnica de geracao de codigo sem processo amplo de desenvolvimento.",
    ),
    "GaetaninoPaolone2020": (
        "missing I1",
        "Titulo e abstract descrevem geracao automatica de codigo por MDA e UML, sem camada de IA para desenvolvimento de software.",
    ),
    "FrankFXu2022": (
        "E2",
        "Titulo e abstract avaliam plugin de code generation em IDE, sem workflow proprio, artefatos persistentes, papeis ou validacao de processo.",
    ),
    "YueWang2021": (
        "E1",
        "Titulo e abstract apresentam modelo pre-treinado para code understanding e generation, sem camada de processo ou framework de desenvolvimento.",
    ),
    "PhillipALaplante2022": (
        "missing I1",
        "Titulo e abstract tratam engenharia de requisitos para software e sistemas em geral, sem desenvolvimento de software com IA.",
    ),
    "KowndinyaBoyalakuntla2022": (
        "missing I1",
        "Titulo e abstract descrevem linguagem de modelagem e gerador de codigo para apps moveis, sem camada de IA.",
    ),
    "SijieShen2022": (
        "E3",
        "Titulo e abstract focam incorporacao de conhecimento de dominio em code generation, uma tarefa isolada.",
    ),
    "XinWang2022": (
        "E3",
        "Titulo e abstract focam aprendizagem multitarefa para neural code generation, uma tarefa isolada.",
    ),
    "ZiyanZhao2023": (
        "E3",
        "Titulo e abstract focam geracao automatica de requisitos a partir de keywords, uma tarefa isolada de engenharia de requisitos.",
    ),
    "YejinBang2023": (
        "E8",
        "Titulo e abstract avaliam ChatGPT em tarefas gerais de NLP, raciocinio, alucinacao e interatividade, fora do foco de desenvolvimento de software com IA.",
    ),
    "IrfanUllah2022": (
        "missing I1",
        "Titulo e abstract descrevem gerador de codigo baseado em templates e class diagram, sem camada de IA.",
    ),
    "RahulkrishnaYandrapally2023": (
        "E3",
        "Titulo e abstract focam geracao de testes e especificacao de API a partir de UI tests, uma tarefa especifica de testing.",
    ),
    "KnutHRolland2023": (
        "missing I1",
        "Titulo e abstract problematizam agile em larga escala, sem camada de IA para desenvolvimento de software.",
    ),
    "JoonSungPark2023": (
        "E8",
        "Titulo e abstract descrevem agentes generativos para simular comportamento humano em sandbox, sem foco substantivo em desenvolvimento de software.",
    ),
    "XiaoxueRen2023": (
        "E3",
        "Titulo e abstract descrevem AI chaining para exception handling em code generation, restrito a uma tarefa de geracao de codigo.",
    ),
    "YueLiu2024": (
        "E3",
        "Titulo e abstract caracterizam e mitigam problemas de qualidade em codigo gerado por ChatGPT, uma tarefa especifica de code generation.",
    ),
    "JianxunWang2023": (
        "E1",
        "Titulo e abstract revisam code generation com LLMs e avaliacao de codigo gerado, sem camada de processo ou framework de desenvolvimento.",
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
    ]

    rows = []
    all_rows = []
    for entry in targets:
        key = entry.get("citation_key")
        if key in INCLUDE:
            decision = "include"
            criterion, reason = INCLUDE[key]
        else:
            decision = "exclude"
            criterion, reason = EXCLUDE[key]

        previous = entry.get("screening_pass1") or {}
        changed = previous.get("decision") != decision or previous.get("criterion") != criterion or previous.get("reason") != reason
        entry["screening_pass1"] = {
            "decision": decision,
            "criterion": criterion,
            "reason": reason,
            "reviewer": "screening-logger",
            "timestamp": TIMESTAMP,
            "screening_scope": DISCOVERY,
        }
        current_row = {
            "citation_key": key,
            "title": clean(entry.get("title")),
            "year": entry.get("year") or "",
            "decision": decision,
            "criterion": criterion,
            "reason": reason,
            "reviewer": "screening-logger",
            "timestamp": TIMESTAMP,
        }
        all_rows.append(current_row)
        if changed:
            audit_row = dict(current_row)
            if previous.get("decision") != "pending":
                audit_row["criterion"] = f"AMENDED:{criterion}"
                audit_row["reason"] = f"Decision amended to {decision} by {criterion}. {reason}"
            rows.append(audit_row)

    with LOG.open("a", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(
            fh,
            fieldnames=["citation_key", "title", "year", "decision", "criterion", "reason", "reviewer", "timestamp"],
        )
        writer.writerows(rows)

    RESULTS.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    included = [row for row in all_rows if row["decision"] == "include"]
    excluded = [row for row in all_rows if row["decision"] == "exclude"]
    counts = Counter(row["criterion"] for row in excluded)

    prior_summary = SUMMARY.read_text(encoding="utf-8-sig").splitlines() if SUMMARY.exists() else []
    marker = "## Passada 1d (snowballing rodada 3, titulo + abstract)"
    if marker in prior_summary:
        prior_summary = prior_summary[:prior_summary.index(marker)]
    while prior_summary and prior_summary[-1] == "":
        prior_summary.pop()

    descriptions = {
        "missing I1": "Fora do foco tematico principal: titulo e abstract nao indicam desenvolvimento de software com IA como unidade de analise.",
        "E1": "Benchmark, modelo ou survey tecnico sem camada de processo: a fonte avalia modelos, APIs ou code generation sem workflow de desenvolvimento.",
        "E2": "Assistente generico ou estudo de uso: a fonte descreve assistente de codigo sem workflow proprio, artefatos persistentes, papeis ou validacao propria.",
        "E3": "Tarefa isolada de engenharia de software: a fonte trata uma tarefa pontual sem propor framework ou processo amplo.",
        "E8": "Mencao tangencial ou outro dominio: a fonte nao analisa substantivamente frameworks de desenvolvimento de software com IA.",
    }

    prior_summary.extend([
        "",
        marker,
        "",
        "| Motivo de exclusao | Criterio | N excluidos |",
        "|---|---|---:|",
    ])
    for criterion, count in sorted(counts.items()):
        prior_summary.append(f"| {descriptions.get(criterion, criterion)} | {criterion} | {count} |")
    prior_summary.extend([
        "",
        f"**Total snowballing rodada 3**: {len(excluded)} excluidos de {len(all_rows)} analisados ({(len(excluded) / len(all_rows)) * 100:.1f}%).",
        "",
        "### Incluidos para aquisicao de texto completo apos snowballing rodada 3",
        "",
        "| Citation key | Ano | Titulo |",
        "|---|---:|---|",
    ])
    for row in included:
        prior_summary.append(f"| {row['citation_key']} | {row['year']} | {row['title'].replace('|', '/')} |")
    SUMMARY.write_text("\n".join(prior_summary) + "\n", encoding="utf-8")

    round_lines = [
        "# Screening Snowballing Round 3",
        "",
        f"> Executado em: {RUN_LOCAL}",
        f"> Escopo: `{DISCOVERY}`",
        "",
        "## Resultado",
        "",
        f"- Candidatos analisados: {len(all_rows)}",
        f"- Incluidos para texto completo: {len(included)}",
        f"- Excluidos: {len(excluded)}",
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
        "## Incluidos",
        "",
        "| Citation key | Ano | Titulo |",
        "|---|---:|---|",
    ])
    for row in included:
        round_lines.append(f"| {row['citation_key']} | {row['year']} | {row['title'].replace('|', '/')} |")
    ROUND_SUMMARY.write_text("\n".join(round_lines) + "\n", encoding="utf-8")

    print(json.dumps({
        "scope": DISCOVERY,
        "analyzed": len(all_rows),
        "include": len(included),
        "exclude": len(excluded),
        "exclude_by_criterion": dict(counts),
        "summary": str(ROUND_SUMMARY),
    }, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
