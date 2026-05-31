from __future__ import annotations

import csv
import json
import re
from collections import Counter
from pathlib import Path


BASE = Path(r"C:\SCIENTEX\_papers\ai-dev-frameworks-review\systematic-review")
RESULTS = BASE / "search-results.json"
SCREENING = BASE / "screening"
LOG = SCREENING / "title-abstract.log.csv"
SUMMARY = SCREENING / "exclusion-reasons.md"
ROUND_SUMMARY = BASE / "snowballing" / "round-2" / "screening-summary.md"
DISCOVERY = "snowballing-2"
RUN_LOCAL = "2026-05-28 13:27"
TIMESTAMP = "2026-05-28T13:27:00Z"


INCLUDE = {
    "YuntongZhang2024": (
        "I1",
        "Titulo e abstract descrevem AutoCodeRover como abordagem autonoma para resolver issues do GitHub, combinando LLMs, busca de codigo, manutencao e evolucao de software.",
    ),
    "ZeeshanRasheed2024": (
        "I1",
        "Titulo descreve Codepori como sistema de larga escala para desenvolvimento autonomo de software usando tecnologia multiagente; ausencia de abstract exige verificacao em texto completo.",
    ),
    "HuanZhang2024": (
        "I1",
        "Titulo e abstract descrevem PairCoder como framework de pair programming com agentes Navigator e Driver, planejamento, execucao de codigo, testes e refinamento por feedback.",
    ),
    "SaiZhang2025": (
        "I1",
        "Titulo e abstract descrevem AgileGen como desenvolvimento generativo baseado em agile e teamwork humano-IA, com requisitos, criterios de aceitacao, Gherkin e iteracao.",
    ),
    "pekzkaya2023": (
        "I1",
        "Titulo e abstract discutem processos de desenvolvimento de software aumentados por IA generativa, com foco explicito em evolucao do processo e automacao bem direcionada.",
    ),
}


EXCLUDE_OVERRIDES = {
    "PrestonGSmith2020": (
        "missing I1",
        "Titulo e abstract tratam gerenciamento de riscos em projetos e produtos, sem desenvolvimento de software com IA como unidade de analise.",
    ),
    "JunjieChen2020": (
        "missing I1",
        "Titulo e abstract apresentam survey de compiler testing, sem camada de IA para desenvolvimento de software.",
    ),
    "SamarAlSaqqa2020": (
        "missing I1",
        "Titulo e abstract revisam metodologias ageis tradicionais, sem framework de desenvolvimento de software com IA.",
    ),
    "YasamanBahri2024": (
        "E8",
        "Titulo e abstract tratam leis de escala em redes neurais, sem analise substantiva de desenvolvimento de software com IA.",
    ),
    "NasifImtiaz2021": (
        "missing I1",
        "Titulo e abstract comparam ferramentas de software composition analysis para vulnerabilidades, sem camada de IA para desenvolvimento de software.",
    ),
    "LinaMarkauskait2022": (
        "E8",
        "Titulo e abstract tratam capacidades de aprendizagem humana em mundo com IA, fora do dominio de engenharia de software.",
    ),
    "Anon2022": (
        "E7",
        "Registro corresponde a anais de conferencia, sem estudo ou detalhes tecnicos extraiveis como fonte primaria individual.",
    ),
    "Anon2022_2": (
        "E7",
        "Registro corresponde a anais de conferencia, sem estudo ou detalhes tecnicos extraiveis como fonte primaria individual.",
    ),
    "NoahShinn2023": (
        "E8",
        "Titulo e abstract descrevem Reflexion como framework geral de agentes de linguagem, sem foco substantivo em desenvolvimento de software.",
    ),
    "GuohaoLi2023": (
        "E8",
        "Titulo e abstract descrevem CAMEL como framework geral de agentes comunicativos, sem foco substantivo em desenvolvimento de software.",
    ),
    "JRHorton2023": (
        "E8",
        "Titulo e abstract tratam LLMs como agentes simulados em economia, fora do dominio de engenharia de software.",
    ),
    "JiaweiLiu2023": (
        "E1",
        "Titulo e abstract descrevem EvalPlus como benchmark para avaliar corretude de codigo gerado por LLMs, sem camada de processo ou framework de desenvolvimento.",
    ),
    "JundaHe2023": (
        "missing I1",
        "Titulo e abstract tratam representacao de posts do Stack Overflow, sem framework de desenvolvimento de software com IA.",
    ),
    "ZhenpengChen2024": (
        "E3",
        "Titulo e abstract apresentam survey de fairness testing de software de ML, uma area de teste especifica sem framework amplo de desenvolvimento com IA.",
    ),
    "MichaelCFu2023": (
        "E3",
        "Titulo e abstract focam deteccao, classificacao e reparo de vulnerabilidades com ChatGPT, conjunto de tarefas especificas sem processo amplo.",
    ),
    "ChunqiuStevenXia2024": (
        "E3",
        "Titulo e abstract descrevem fuzzing universal com LLMs, uma tarefa de teste especifica sem framework amplo de desenvolvimento.",
    ),
    "MaryamTaeb2024": (
        "E3",
        "Titulo e abstract descrevem workflow de teste de acessibilidade a partir de linguagem natural, restrito a uma tarefa de testing.",
    ),
    "JuyeonYoon2024": (
        "E3",
        "Titulo e abstract descrevem agente autonomo para teste de GUI Android, restrito a uma tarefa de testing.",
    ),
    "Anon2024": (
        "E7",
        "Registro corresponde a anais de conferencia e nao possui abstract ou detalhes tecnicos suficientes para extracao.",
    ),
    "ZhensuSun2024": (
        "E3",
        "Titulo e abstract focam gramatica de linguagem de programacao orientada a geracao eficiente por IA, sem processo amplo de desenvolvimento.",
    ),
    "HanbinWang2024": (
        "E3",
        "Titulo e abstract descrevem sistema de reparo interativo de codigo com papeis e feedback de compilador, mas restrito a geracao, traducao e reparo de codigo.",
    ),
    "VasiliosMavroudis2024": (
        "E8",
        "Titulo e abstract analisam LangChain para desenvolvimento de aplicacoes LLM em geral, sem tratar frameworks de desenvolvimento de software com IA como unidade de analise.",
    ),
    "XinZhou2024": (
        "E3",
        "Titulo e abstract apresentam revisao sobre LLMs para deteccao e reparo de vulnerabilidades, tarefa especifica de seguranca de software.",
    ),
    "SungminKang2024": (
        "E3",
        "Titulo e abstract descrevem debugging e reparo automatizado com LLMs, restritos a uma tarefa especifica de manutencao.",
    ),
    "VivankSharma2019": (
        "missing I1",
        "Titulo e abstract tratam predicao de falhas em sistema IoT monitorado, sem desenvolvimento de software com IA.",
    ),
    "RajivKohli2018": (
        "missing I1",
        "Titulo e abstract revisam inovacao digital em sistemas de informacao, sem framework de desenvolvimento de software com IA.",
    ),
    "KlaasJanStol2018": (
        "missing I1",
        "Titulo e abstract apresentam metodologia de pesquisa em engenharia de software, sem desenvolvimento de software com IA.",
    ),
    "DanielRusso2018": (
        "missing I1",
        "Titulo e abstract tratam qualidade de sistemas de informacao, arquitetura e processo, sem camada de IA para desenvolvimento de software.",
    ),
    "AriHoltzman2019": (
        "E8",
        "Titulo e abstract tratam degeneracao em geracao neural de texto, sem analise substantiva de desenvolvimento de software com IA.",
    ),
    "MaiSkjttLinneberg2019": (
        "missing I1",
        "Titulo e abstract tratam codificacao de dados qualitativos, sem desenvolvimento de software com IA.",
    ),
    "GalitShmueli2019": (
        "missing I1",
        "Titulo e abstract tratam avaliacao preditiva em PLS-SEM, sem desenvolvimento de software com IA.",
    ),
    "JaredKaplan2020": (
        "E8",
        "Titulo e abstract tratam leis de escala ou intervencoes agenticas em IA de modo geral, sem desenvolvimento de software com IA como unidade de analise.",
    ),
    "StineGrodal2020": (
        "missing I1",
        "Titulo e abstract tratam rigor em analise qualitativa e teoria organizacional, sem desenvolvimento de software com IA.",
    ),
    "DanielRusso2021": (
        "missing I1",
        "Titulo e abstract tratam PLS-SEM para pesquisa em engenharia de software, sem desenvolvimento de software com IA.",
    ),
    "DanielRusso2021_2": (
        "missing I1",
        "Titulo e abstract tratam modelo de sucesso agile tradicional, sem camada de IA para desenvolvimento de software.",
    ),
    "EmmanuelSeniorTenakwah2021": (
        "missing I1",
        "Titulo e abstract tratam retencao de empregados e turnover, fora do dominio de desenvolvimento de software com IA.",
    ),
    "PriyanVaithilingam2022": (
        "E2",
        "Titulo e abstract avaliam usabilidade de Copilot como ferramenta de geracao de codigo, sem workflow proprio, artefatos persistentes ou papeis.",
    ),
    "HusseinMozannar2022": (
        "E2",
        "Titulo e abstract modelam comportamento de usuarios em Copilot e CodeWhisperer, sem framework proprio de desenvolvimento com IA.",
    ),
    "RuijiaCheng2022": (
        "E2",
        "Titulo e abstract estudam confianca em ferramentas de geracao de codigo por IA, sem workflow proprio, artefatos persistentes ou papeis.",
    ),
    "AntonioMastropaolo2023": (
        "E2",
        "Titulo e abstract avaliam robustez de GitHub Copilot como ferramenta de geracao de codigo, sem framework de processo proprio.",
    ),
    "BeiqiZhang2023": (
        "E2",
        "Titulo e abstract estudam praticas e desafios de uso do GitHub Copilot, sem framework proprio de desenvolvimento com IA.",
    ),
    "BeiqiZhang2023_2": (
        "E5",
        "Registro duplica o estudo `BeiqiZhang2023` sobre praticas e desafios de uso do GitHub Copilot; ambos permanecem fora do escopo por E2.",
    ),
    "RuotongWang2023": (
        "E2",
        "Titulo e abstract estudam confianca em ferramentas de geracao de codigo por IA, sem workflow proprio, artefatos persistentes ou papeis.",
    ),
    "GarridoMerchn2023": (
        "E8",
        "Titulo e abstract apresentam survey amplo de IA generativa e LLMs, sem foco substantivo em desenvolvimento de software com IA.",
    ),
    "YanjieGao2023": (
        "missing I1",
        "Titulo e abstract analisam problemas de qualidade em plataforma de deep learning, sem framework de desenvolvimento de software com IA.",
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
        "&nbsp;": " ",
        "&amp;": "&",
        "&lt;": "<",
        "&gt;": ">",
        "<scp>": "",
        "</scp>": "",
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
        "debugging",
        "repair",
        "vulnerability",
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
    marker = "## Passada 1c (snowballing rodada 2, titulo + abstract)"
    if marker in prior_summary:
        prior_summary = prior_summary[:prior_summary.index(marker)]
    while prior_summary and prior_summary[-1] == "":
        prior_summary.pop()

    descriptions = {
        "missing I1": "Fora do foco tematico principal: titulo e abstract nao indicam desenvolvimento de software com IA como unidade de analise.",
        "missing I2/I3/I4": "Falta de estrutura minima de framework: titulo e abstract mencionam IA em software, mas nao mostram metodo, workflow, artefatos, papeis ou validacao.",
        "E1": "Benchmark ou modelo sem camada de processo: a fonte avalia modelos, APIs ou benchmarks de codigo sem workflow de desenvolvimento.",
        "E2": "Assistente generico ou estudo de uso: a fonte descreve assistente de codigo sem workflow proprio, artefatos persistentes, papeis ou validacao propria.",
        "E3": "Tarefa isolada de engenharia de software: a fonte trata uma tarefa pontual sem propor framework ou processo amplo.",
        "E5": "Duplicata: a fonte duplica outra entrada mais adequada ou ja registrada.",
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
        f"**Total snowballing rodada 2**: {len(excluded)} excluidos de {len(all_rows)} analisados ({(len(excluded) / len(all_rows)) * 100:.1f}%).",
        "",
        "### Incluidos para aquisicao de texto completo apos snowballing rodada 2",
        "",
        "| Citation key | Ano | Titulo |",
        "|---|---:|---|",
    ])
    for row in included:
        prior_summary.append(f"| {row['citation_key']} | {row['year']} | {row['title'].replace('|', '/')} |")
    SUMMARY.write_text("\n".join(prior_summary) + "\n", encoding="utf-8")

    round_lines = [
        "# Screening Snowballing Round 2",
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
