from __future__ import annotations

import csv
import json
import re
from collections import Counter
from datetime import datetime
from pathlib import Path


BASE = Path(r"C:\SCIENTEX\_papers\ai-dev-frameworks-review\systematic-review")
RESULTS = BASE / "search-results.json"
SCREENING = BASE / "screening"
LOG = SCREENING / "title-abstract.log.csv"
SUMMARY = SCREENING / "exclusion-reasons.md"
ROUND_SUMMARY = BASE / "snowballing" / "round-1" / "screening-summary.md"
DISCOVERY = "snowballing-1"
RUN_LOCAL = "2026-05-28 11:41"
TIMESTAMP = "2026-05-28T11:41:00Z"


INCLUDE = {
    "JulesWhite2023": (
        "I1",
        "Titulo e abstract descrevem um metodo reutilizavel de prompt patterns para varias atividades de engenharia de software, incluindo requisitos, refatoracao, qualidade de codigo e design.",
    ),
    "ChristophTreude2025": (
        "I1",
        "Titulo e abstract descrevem uma taxonomia de interacoes entre desenvolvedores e ferramentas de IA ao longo do ciclo de desenvolvimento de software.",
    ),
    "JundaHe2025": (
        "I1",
        "Titulo e abstract descrevem sistemas multiagente baseados em LLM para engenharia de software, com revisao por etapas do SDLC e estudos de caso.",
    ),
    "JSauvola2024": (
        "I1",
        "Titulo e abstract analisam desenvolvimento de software com IA generativa, ferramentas, processos e automacao ao longo do ciclo de desenvolvimento.",
    ),
    "AyyappaSajja2024": (
        "I1",
        "Titulo e abstract discutem integracao de IA generativa ao ciclo de vida de desenvolvimento de software, incluindo qualidade de codigo e manutencao.",
    ),
    "MitulModi2024": (
        "I1",
        "Titulo e abstract apresentam analise sistematica de praticas automatizadas de desenvolvimento com IA generativa em multiplas fases do ciclo de software.",
    ),
    "ShreyasPangavhane2024": (
        "I1",
        "Titulo e abstract descrevem ferramentas de desenvolvimento de software aumentadas por IA em varias fases, incluindo DevOps, testes, deteccao de problemas e geracao de codigo.",
    ),
    "KRRaghi2024": (
        "I1",
        "Titulo e abstract apresentam uma abordagem para automacao do SDLC com LLMs e LangChain, cobrindo planejamento, requisitos, codigo, testes e deployment.",
    ),
    "DanielRusso2024": (
        "I1",
        "Titulo e abstract apresentam um modelo teorico de adocao de IA generativa em engenharia de software, com foco em colaboracao humano-IA e adaptacao.",
    ),
}


EXCLUDE_OVERRIDES = {
    "HamzaChniter2018": (
        "missing I1",
        "Titulo e abstract descrevem arquitetura multiagente para sistemas distribuidos de tempo real, mas nao desenvolvimento de software com IA como unidade de analise.",
    ),
    "KashumiMadampe2021": (
        "missing I1",
        "Titulo e abstract tratam mudancas de requisitos em contextos ageis, sem camada de IA para desenvolvimento de software.",
    ),
    "CarlosMolinaJimnez2018": (
        "missing I1",
        "Titulo e abstract tratam arquiteturas hibridas para smart contracts, sem desenvolvimento de software com IA como unidade de analise.",
    ),
    "StephenSYau2020": (
        "missing I1",
        "Titulo e abstract tratam coordenacao confiavel com blockchain em desenvolvimento colaborativo, sem camada de IA.",
    ),
    "SelinaDemi2021": (
        "missing I1",
        "Titulo e abstract tratam aplicacoes de blockchain em engenharia de software, sem desenvolvimento de software com IA.",
    ),
    "NgocHuyTruong2018": (
        "missing I1",
        "Titulo e abstract tratam necessidades de desenvolvedores em testes de usabilidade, sem camada de IA para desenvolvimento de software.",
    ),
    "TomMens2019": (
        "missing I1",
        "Titulo e abstract tratam aspectos sociais do desenvolvimento de software, sem desenvolvimento de software com IA.",
    ),
    "AndrNMeyer2019": (
        "missing I1",
        "Titulo e abstract tratam rotina e produtividade de desenvolvedores, sem camada de IA para desenvolvimento de software.",
    ),
    "JohanERavn2022": (
        "missing I1",
        "Titulo e abstract tratam autonomia de times e transformacao digital, sem desenvolvimento de software com IA como unidade de analise.",
    ),
    "MartheBerntzen2023": (
        "missing I1",
        "Titulo e abstract tratam mecanismos de coordenacao em agile em larga escala, sem camada de IA.",
    ),
    "AnastasiiaTkalich2023": (
        "missing I1",
        "Titulo e abstract tratam pair programming em trabalho hibrido, sem camada de IA para desenvolvimento de software.",
    ),
    "DanieleDeBari2024": (
        "E3",
        "Titulo e abstract focam avaliacao de LLMs em modelagem UML, uma tarefa especifica sem framework amplo de desenvolvimento.",
    ),
    "EriksKlotins2019": (
        "missing I1",
        "Titulo e abstract tratam metas e praticas de engenharia de software em startups, sem camada de IA.",
    ),
    "EriksKlotins2021": (
        "missing I1",
        "Titulo e abstract nao indicam desenvolvimento de software com IA como unidade de analise.",
    ),
    "KevinZheyuanCui2024": (
        "E2",
        "Titulo e abstract tratam efeitos de produtividade do GitHub Copilot, sem framework ou workflow proprio de desenvolvimento com IA.",
    ),
    "RashinaHoda2021": (
        "missing I1",
        "Titulo e abstract tratam grounded theory para engenharia de software, sem camada de IA.",
    ),
    "DavinderKaur2022": (
        "E8",
        "Titulo e abstract tratam IA confiavel em geral, sem analise substantiva de desenvolvimento de software com IA.",
    ),
    "FangHou2022": (
        "missing I1",
        "Titulo e abstract tratam confianca no ecossistema de software, sem camada de IA para desenvolvimento de software.",
    ),
    "DayeNam2024": (
        "E2",
        "Titulo e abstract descrevem plugin conversacional para compreensao de codigo com LLM, sem workflow ou artefatos persistentes proprios.",
    ),
    "ChristopherSTimperley2021": (
        "missing I1",
        "Titulo e abstract tratam compartilhamento de artefatos em pesquisa de engenharia de software, sem camada de IA.",
    ),
    "AlexeySvyatkovskiy2019": (
        "E2",
        "Titulo e abstract descrevem um assistente de code completion integrado a IDE, sem workflow proprio, artefatos persistentes, papeis ou validacao de processo.",
    ),
    "ChristianBird2022": (
        "E2",
        "Titulo e abstract tratam de GitHub Copilot como assistente de codigo e estudo de uso, sem framework ou processo operacional proprio.",
    ),
    "StevenRoss2023": (
        "E2",
        "Titulo e abstract descrevem uma interface conversacional para programadores, mas nao um framework de desenvolvimento com artefatos, papeis ou workflow proprio.",
    ),
    "JiaoSun2022": (
        "E3",
        "Titulo e abstract tratam de explicabilidade de IA generativa em cenarios especificos de codigo, sem propor framework de desenvolvimento ou processo amplo.",
    ),
    "JunjieWang2024": (
        "E3",
        "Titulo e abstract focam uma unica classe de tarefa de engenharia de software, testes com LLMs, sem framework amplo de desenvolvimento com IA.",
    ),
    "AlessioFerrari2024": (
        "E3",
        "Titulo e abstract focam geracao de modelos UML a partir de requisitos, uma tarefa isolada sem framework amplo de desenvolvimento com IA.",
    ),
    "FidaZubair2024": (
        "E3",
        "Titulo e abstract focam program repair com LLMs, uma tarefa isolada de engenharia de software sem processo amplo.",
    ),
    "HaonanLi2024": (
        "E3",
        "Titulo e abstract descrevem um framework para bug detection com analise estatica e LLMs, mas restrito a uma tarefa isolada.",
    ),
    "ShuaicaiRen2024": (
        "E3",
        "Titulo e abstract focam elicitacao de requisitos com LLMs e prompts, uma tarefa especifica sem framework amplo de desenvolvimento.",
    ),
    "JunaedYounusKhan2022": (
        "E3",
        "Titulo e abstract focam geracao automatica de documentacao de codigo, uma tarefa isolada de engenharia de software.",
    ),
    "AlokMathur2023": (
        "E3",
        "Titulo e abstract focam geracao automatica de casos de teste, uma tarefa isolada de engenharia de software.",
    ),
    "MohammedLatifSiddiq2024": (
        "E3",
        "Titulo e abstract focam geracao de testes JUnit com LLMs, uma tarefa isolada de engenharia de software.",
    ),
    "HammondPearce2025": (
        "E3",
        "Titulo e abstract focam seguranca de contribuicoes de codigo geradas pelo Copilot, sem framework amplo de desenvolvimento com IA.",
    ),
    "Huang2025_2": (
        "E7",
        "Registro sem abstract ou detalhes tecnicos suficientes para justificar inclusao no screening por titulo e abstract.",
    ),
    "RobertKYin2018": (
        "E8",
        "Fonte metodologica geral de estudo de caso, sem analise substantiva de frameworks de desenvolvimento de software com IA.",
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
        "\u00e2\u20ac\u201d": "-",
        "\u00e2\u20ac\u201c": "-",
        "\u00c3\u00a2\u00e2\u201a\u00ac\"": "-",
        "\u00c3\u00a2\u00e2\u201a\u00ac": "-",
        "\u00e2\u20ac": "-",
        "\u00e2\u20ac\u2122": "'",
        "\u00c3\u00a2\u00e2\u201a\u00ac\u00e2\u201e\u00a2": "'",
        "\u00e2\u20ac\u0153": '"',
        "\u00e2\u20ac\u009d": '"',
        "\u00c3\u00a2\u00e2\u201a\u00ac\u00c5\u201c": '"',
        "\u00c3\u00a2\u00e2\u201a\u00ac\u00c2\u009d": '"',
        "\u00e2\u20ac\u02dc": "'",
        "\u00c3\u00a7": "c",
        "\u00c3\u00a3": "a",
        "\u00c3\u00a9": "e",
        "\u00c3\u00a1": "a",
        "\u00c3\u00b3": "o",
        "\u00c3\u00ba": "u",
        "\u00c3\u00ad": "i",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return re.sub(r"\s+", " ", text).strip()


def normalized_text(entry: dict) -> str:
    return clean(f"{entry.get('title') or ''} {entry.get('abstract') or ''}").lower()


def default_exclusion(entry: dict) -> tuple[str, str]:
    text = normalized_text(entry)
    if not clean(entry.get("abstract")):
        return (
            "E7",
            "Registro sem abstract ou detalhes tecnicos suficientes para justificar inclusao no screening por titulo e abstract.",
        )
    ai_terms = [
        "artificial intelligence",
        "generative ai",
        "large language model",
        "chatgpt",
        "copilot",
        "codex",
        "agentic",
        "machine learning",
        "neural",
        "gpt",
    ]
    se_terms = [
        "software",
        "developer",
        "code",
        "program",
        "requirements",
        "testing",
        "devops",
        "uml",
    ]
    has_ai = any(term in text for term in ai_terms) or bool(re.search(r"\b(ai|llm|llms)\b", text))
    if not has_ai:
        return (
            "missing I1",
            "Titulo e abstract nao indicam desenvolvimento de software com IA como unidade de analise.",
        )
    if not any(term in text for term in se_terms):
        return (
            "E8",
            "Titulo e abstract tratam IA ou agentes em outro dominio, sem analise substantiva de desenvolvimento de software com IA.",
        )
    return (
        "missing I2/I3/I4",
        "Titulo e abstract mencionam IA em engenharia de software, mas nao mostram estrutura minima de framework, metodo, workflow, artefatos, papeis ou validacao.",
    )


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
        elif key in EXCLUDE_OVERRIDES:
            decision = "exclude"
            criterion, reason = EXCLUDE_OVERRIDES[key]
        else:
            decision = "exclude"
            criterion, reason = default_exclusion(entry)

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
    marker = "## Passada 1b (snowballing rodada 1, titulo + abstract)"
    if marker in prior_summary:
        prior_summary = prior_summary[:prior_summary.index(marker)]
    while prior_summary and prior_summary[-1] == "":
        prior_summary.pop()

    descriptions = {
        "missing I1": "Fora do foco tematico principal: titulo e abstract nao indicam desenvolvimento de software com IA como unidade de analise.",
        "missing I2/I3/I4": "Falta de estrutura minima de framework: titulo e abstract mencionam IA em software, mas nao mostram metodo, workflow, artefatos, papeis ou validacao.",
        "E2": "Assistente generico ou estudo de uso: a fonte descreve assistente de codigo sem workflow proprio, artefatos persistentes, papeis ou validacao propria.",
        "E3": "Tarefa isolada de engenharia de software: a fonte trata uma tarefa pontual sem propor framework ou processo amplo.",
        "E7": "Conteudo insuficientemente detalhado: registro sem abstract ou com informacao tecnica insuficiente para triagem positiva.",
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
        f"**Total snowballing rodada 1**: {len(excluded)} excluidos de {len(all_rows)} analisados ({(len(excluded) / len(all_rows)) * 100:.1f}%).",
        "",
        "### Incluidos para aquisicao de texto completo apos snowballing",
        "",
        "| Citation key | Ano | Titulo |",
        "|---|---:|---|",
    ])
    for row in included:
        prior_summary.append(f"| {row['citation_key']} | {row['year']} | {row['title'].replace('|', '/')} |")
    SUMMARY.write_text("\n".join(prior_summary) + "\n", encoding="utf-8")

    round_lines = [
        "# Screening Snowballing Round 1",
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
    }, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
