import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SEARCH_RESULTS = ROOT / "search-results.json"
FULLTEXT_LOG = ROOT / "screening" / "full-text.log.csv"
EXCLUSION_REASONS = ROOT / "screening" / "exclusion-reasons.md"
SUMMARY = ROOT / "snowballing" / "round-3" / "fulltext-summary.md"
PAPER = ROOT.parent / "PAPER.md"
PLAN = ROOT / "PLAN.md"

TIMESTAMP = "2026-05-28T14:02:00Z"
HUMAN_TIME = "2026-05-28 14:02"
DISCOVERY = "snowballing-3"

INCLUDES = {
    "ChenQian2023": {
        "criterion": "I1",
        "reason": (
            "Texto completo apresenta ChatDev como framework de desenvolvimento de software "
            "com agentes especializados, chat chain, design, coding, testing, comunicacao "
            "multi-turn e mecanismo de communicative dehallucination."
        ),
    },
    "SiruiHong2023": {
        "criterion": "I1",
        "reason": (
            "Texto completo apresenta MetaGPT como framework multiagente que codifica SOPs, "
            "papeis e workflows de engenharia de software, produzindo PRDs, artefatos de "
            "design, especificacoes de interface e validacao por testes."
        ),
    },
    "YuCheng2023": {
        "criterion": "I1",
        "reason": (
            "Texto completo apresenta Prompt Sapper como metodologia e IDE para AI chain "
            "engineering, com requisitos, composicao de workers, papeis, prompts, design, "
            "implementacao, testing e gerenciamento de artefatos."
        ),
    },
}

PENDING = "AshaRajbhoj2024"


def load_results():
    return json.loads(SEARCH_RESULTS.read_text(encoding="utf-8"))


def save_results(records):
    SEARCH_RESULTS.write_text(
        json.dumps(records, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def by_key(records, key):
    for record in records:
        if record.get("citation_key") == key:
            return record
    raise KeyError(key)


def append_fulltext_log(records):
    existing = set()
    if FULLTEXT_LOG.exists():
        with FULLTEXT_LOG.open("r", encoding="utf-8", newline="") as handle:
            reader = csv.DictReader(handle)
            for row in reader:
                existing.add((row["citation_key"], row["timestamp"]))

    with FULLTEXT_LOG.open("a", encoding="utf-8", newline="") as handle:
        fieldnames = [
            "citation_key",
            "title",
            "year",
            "decision",
            "criterion",
            "reason",
            "reviewer",
            "timestamp",
        ]
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        for key, decision in INCLUDES.items():
            if (key, TIMESTAMP) in existing:
                continue
            record = by_key(records, key)
            writer.writerow(
                {
                    "citation_key": key,
                    "title": record.get("title", ""),
                    "year": record.get("year", ""),
                    "decision": "include",
                    "criterion": decision["criterion"],
                    "reason": decision["reason"],
                    "reviewer": "screening-logger",
                    "timestamp": TIMESTAMP,
                }
            )


def update_screening(records):
    for key, decision in INCLUDES.items():
        record = by_key(records, key)
        record["screening_pass2"] = {
            "decision": "include",
            "criterion": decision["criterion"],
            "reason": decision["reason"],
            "reviewer": "screening-logger",
            "timestamp": TIMESTAMP,
            "screening_scope": DISCOVERY,
        }

    # Keep the missing PDF as pending. It is not a full-text exclusion.
    pending = by_key(records, PENDING)
    pending.pop("screening_pass2", None)


def included_count(records):
    return sum(
        1
        for record in records
        if record.get("screening_pass2", {}).get("decision") == "include"
    )


def write_round_summary(records, final_included):
    rows = []
    for key in INCLUDES:
        record = by_key(records, key)
        rows.append(f"| {key} | {record.get('year', '')} | {record.get('title', '')} |")

    SUMMARY.write_text(
        "\n".join(
            [
                "# Snowballing rodada 3, screening full text parcial",
                "",
                f"- Data: {HUMAN_TIME}",
                "- Escopo: candidatos incluidos na triagem de titulo e abstract da rodada 3.",
                "- Textos completos esperados: 4",
                "- Textos completos analisados: 3",
                "- Incluidos finais adicionais: 3",
                "- Excluidos em full text: 0",
                "- Pendentes por download manual: 1",
                f"- Incluidos finais consolidados ate o momento: {final_included}",
                "",
                "## Incluidos finais adicionais",
                "",
                "| Citation key | Ano | Titulo |",
                "|---|---:|---|",
                *rows,
                "",
                "## Pendente manual",
                "",
                "| Citation key | DOI | Status |",
                "|---|---|---|",
                "| AshaRajbhoj2024 | 10.1145/3641399.3641403 | Aguardando download manual do PDF |",
                "",
                "Observacao metodologica: a ausencia temporaria do PDF nao foi registrada como exclusao. "
                "O estudo permanece pendente para decisao posterior ou para fechamento documentado "
                "do corpus parcial.",
                "",
            ]
        ),
        encoding="utf-8",
    )


def append_exclusion_reasons(records, final_included):
    text = EXCLUSION_REASONS.read_text(encoding="utf-8")
    marker = "## Passada 2d (snowballing rodada 3, full text parcial)"
    if marker in text:
        return

    rows = []
    for key in INCLUDES:
        record = by_key(records, key)
        rows.append(f"| {key} | {record.get('year', '')} | {record.get('title', '')} |")

    section = "\n".join(
        [
            "",
            marker,
            "",
            "Nao houve exclusoes entre os textos completos analisados nesta passada parcial.",
            "`AshaRajbhoj2024` permanece pendente por download manual e nao foi contado como excluido.",
            "",
            "| Motivo de exclusao | Criterio | N excluidos |",
            "|---|---|---:|",
            "| Nenhuma exclusao nos textos analisados | n/a | 0 |",
            "",
            "**Total full text snowballing rodada 3 parcial**: 0 excluidos de 3 analisados (0.0%).",
            "",
            "### Incluidos finais adicionais apos snowballing rodada 3",
            "",
            "| Citation key | Ano | Titulo |",
            "|---|---:|---|",
            *rows,
            "",
            "### Pendente por download manual",
            "",
            "| Citation key | Ano | Titulo | Motivo operacional |",
            "|---|---:|---|---|",
            "| AshaRajbhoj2024 | 2024 | Accelerating Software Development Using Generative AI: ChatGPT Case Study | PDF nao disponivel automaticamente; aguarda download manual. |",
            "",
            "## Resumo consolidado apos snowballing rodada 3 parcial",
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
            "- Candidatos novos adicionados por snowballing rodada 3: 30",
            "- Excluidos na triagem titulo e abstract do snowballing rodada 3: 26",
            "- Textos completos analisados no snowballing rodada 3 ate o momento: 3",
            "- Excluidos no full text do snowballing rodada 3 ate o momento: 0",
            "- Pendentes por download manual no snowballing rodada 3: 1",
            "- Incluidos finais adicionais por snowballing rodada 3 ate o momento: 3",
            f"- Incluidos finais consolidados: {final_included}",
            "",
        ]
    )
    EXCLUSION_REASONS.write_text(text.rstrip() + "\n" + section, encoding="utf-8")


def update_paper(final_included):
    text = PAPER.read_text(encoding="utf-8")
    marker = "### 2026-05-28 14:02"
    if marker in text:
        return
    addition = f"""

### 2026-05-28 14:02

- Autor enviou `CONTINUE`.
- Screening full text parcial dos 3 textos obtidos no `snowballing-3` executado.
- Resultado: 3 incluidos finais adicionais e 0 excluidos entre os textos analisados.
- Incluidos finais adicionais: `ChenQian2023`, `SiruiHong2023`, `YuCheng2023`.
- Pendente operacional: `AshaRajbhoj2024`, DOI `10.1145/3641399.3641403`, ainda sem PDF local. Nao foi registrado como exclusao.
- Incluidos finais consolidados ate o momento: {final_included}.
- Saidas atualizadas: `systematic-review/screening/full-text.log.csv`, `systematic-review/search-results.json`, `systematic-review/screening/exclusion-reasons.md` e `systematic-review/snowballing/round-3/fulltext-summary.md`.
- Proxima etapa pendente: baixar manualmente `AshaRajbhoj2024.pdf` ou aprovar fechamento do snowballing com corpus parcial antes da extracao estruturada.
"""
    PAPER.write_text(text.rstrip() + addition, encoding="utf-8")


def update_plan(final_included):
    text = PLAN.read_text(encoding="utf-8")
    text = text.replace(
        "> Ultima atividade: 2026-05-28 13:52",
        "> Ultima atividade: 2026-05-28 14:02",
    )
    text = text.replace(
        "Aquisicao dos 4 candidatos incluidos pela rodada 3 executada em 2026-05-28 13:52: 3 PDFs obtidos automaticamente e 1 pendente para download manual. Proxima acao: baixar manualmente `AshaRajbhoj2024.pdf` ou autorizar screening full text parcial dos 3 textos obtidos. Como esta e a terceira rodada, nao havera rodada 4 pelo protocolo.",
        f"Aquisicao dos 4 candidatos incluidos pela rodada 3 executada em 2026-05-28 13:52: 3 PDFs obtidos automaticamente e 1 pendente para download manual. Screening full text parcial dos 3 textos obtidos executado em 2026-05-28 14:02: 3 incluidos finais adicionais, 0 excluidos e 1 pendente operacional sem PDF local. Incluidos finais consolidados ate o momento: {final_included}. Proxima acao: baixar manualmente `AshaRajbhoj2024.pdf` ou aprovar fechamento do snowballing com corpus parcial antes da extracao estruturada. Como esta e a terceira rodada, nao havera rodada 4 pelo protocolo.",
    )
    marker = "### Sessao 24, 2026-05-28 14:02"
    if marker not in text:
        addition = f"""

### Sessao 24, 2026-05-28 14:02

- Autor enviou `CONTINUE`.
- Verificacao: `AshaRajbhoj2024.pdf` ainda nao esta presente em `papers_to_review/`.
- Screening full text parcial dos 3 textos obtidos no `snowballing-3` executado.
- Resultado: 3 incluidos finais adicionais e 0 excluidos entre os textos analisados.
- Incluidos finais adicionais: `ChenQian2023`, `SiruiHong2023`, `YuCheng2023`.
- Pendente operacional: `AshaRajbhoj2024`, DOI `10.1145/3641399.3641403`, sem PDF local e nao registrado como exclusao.
- Incluidos finais consolidados ate o momento: {final_included}.
- Saidas atualizadas: `screening/full-text.log.csv`, `search-results.json`, `screening/exclusion-reasons.md`, `snowballing/round-3/fulltext-summary.md`.
- Proxima acao: baixar manualmente `AshaRajbhoj2024.pdf` ou aprovar fechamento do snowballing com corpus parcial antes da extracao estruturada.
"""
        text = text.rstrip() + addition
    PLAN.write_text(text, encoding="utf-8")


def main():
    records = load_results()
    update_screening(records)
    save_results(records)
    append_fulltext_log(records)
    final_included = included_count(records)
    write_round_summary(records, final_included)
    append_exclusion_reasons(records, final_included)
    update_paper(final_included)
    update_plan(final_included)
    print(f"updated={len(INCLUDES)} final_included={final_included} pending={PENDING}")


if __name__ == "__main__":
    main()
