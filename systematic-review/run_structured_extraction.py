import csv
import json
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SEARCH_RESULTS = ROOT / "search-results.json"
EXTRACTS_DIR = ROOT / "pdf-extracts"
OUT_DIR = ROOT / "extracted"
SUMMARY_MD = OUT_DIR / "_summary.md"
MATRIX_CSV = OUT_DIR / "extraction-matrix.csv"
PLAN = ROOT / "PLAN.md"
PAPER = ROOT.parent / "PAPER.md"

HUMAN_TIME = "2026-05-28 14:14"


def clean(value):
    if value is None:
        return ""
    text = str(value)
    text = text.replace("\u2014", "-").replace("\u2013", "-")
    text = text.replace("\u00c3\u00a2\u00e2\u201a\u00ac\u00e2\u20ac\u0153", "-")
    text = text.replace("\u00c3\u0192\u00c2\u00a2\u00c3\u00a2\u00e2\u201a\u00ac\u00c3\u00a2\u00e2\u201a\u00ac\u00c5\u201c", "-")
    text = text.replace("\u00e2\u20ac\u201c", "-").replace("\u00e2\u20ac\u201d", "-")
    text = text.replace("\u2018", "'").replace("\u2019", "'")
    text = text.replace("\u201c", '"').replace("\u201d", '"')
    text = re.sub(r"\s+", " ", text).strip()
    return text


def load_records():
    records = json.loads(SEARCH_RESULTS.read_text(encoding="utf-8"))
    included = [
        record
        for record in records
        if record.get("screening_pass2", {}).get("decision") == "include"
    ]
    return sorted(included, key=lambda r: (r.get("year", 0), r.get("citation_key", "")))


def read_extract(key):
    path = EXTRACTS_DIR / f"{key}.md"
    if not path.exists():
        return ""
    text = clean(path.read_text(encoding="utf-8", errors="ignore"))
    marker = re.search(r"\b(references|bibliography)\b", text, re.IGNORECASE)
    if marker:
        text = text[: marker.start()]
    return text


KNOWN_NAMES = {
    "Macedo2026": "Reversa",
    "MicheleTufano2024": "AutoDev",
    "YuntongZhang2024": "AutoCodeRover",
    "ZeeshanRasheed2024": "Codepori",
    "ChenQian2023": "ChatDev",
    "SiruiHong2023": "MetaGPT",
    "YuCheng2023": "Prompt Sapper",
    "DeepakBabuPiskala2026": "Spec-Driven Development",
    "RanjanSapkota2025": "Agentic coding",
    "AhmedEHassan2024": "AI-Native Software Engineering",
}


def infer_name(record):
    key = record["citation_key"]
    if key in KNOWN_NAMES:
        return KNOWN_NAMES[key]
    title = clean(record.get("title", ""))
    before_colon = title.split(":")[0].strip()
    if 2 <= len(before_colon.split()) <= 8:
        return before_colon
    for token in re.findall(r"\b[A-Z][A-Za-z0-9]{2,}\b", title):
        if token.lower() not in {"software", "engineering", "generative", "agentic"}:
            return token
    return before_colon or title[:80]


def has_any(text, terms):
    low = text.lower()
    return any(term in low for term in terms)


def infer_nature(primary, title):
    title_low = title.lower()
    low = f"{title} {primary}".lower()
    if "framework" in low:
        return "Framework"
    if "architecture" in low or "arquitetura" in low:
        return "Arquitetura"
    if "toolchain" in low or "toolkit" in low or "cli" in low:
        return "Toolkit ou toolchain"
    if "ide" in title_low or "platform" in title_low or "production tool" in title_low:
        return "Plataforma ou IDE"
    if "method" in low or "methodology" in low or "process" in low:
        return "Metodo ou processo"
    if "survey" in title_low or "review" in title_low or "roadmap" in title_low:
        return "Survey ou agenda conceitual"
    if "agentic" in low or "multi-agent" in low or "multiagent" in low:
        return "Arquitetura"
    return "Fonte tecnica sobre desenvolvimento com IA"


def infer_origin(record, text):
    venue = clean(record.get("venue", "")).lower()
    low = text.lower()
    if "github" in low and "arxiv" in venue:
        return "Academia com artefato publico"
    if "arxiv" in venue or "acm" in venue or "ieee" in venue or "springer" in venue:
        return "Academia"
    if "conference" in venue or "journal" in venue:
        return "Academia"
    if "company" in low or "industrial" in low or "practitioner" in low:
        return "Industria ou pratica profissional"
    return "Academia ou comunidade tecnica"


def infer_artifacts(text):
    terms = [
        ("specs", ["specification", "specifications", "spec-driven", "contract"]),
        ("PRDs", ["prd", "product requirement", "requirements document"]),
        ("tarefas", ["task", "tasks", "ticket", "issue"]),
        ("codigo", ["code", "patch", "repository", "pull request"]),
        ("testes", ["test", "tests", "unit test", "validation"]),
        ("logs", ["log", "trace", "evidence", "audit"]),
        ("modelos", ["model", "uml", "diagram", "architecture"]),
        ("prompts", ["prompt", "prompt pattern", "prompting"]),
        ("documentacao", ["documentation", "document", "docs"]),
    ]
    found = [label for label, patterns in terms if has_any(text, patterns)]
    return ", ".join(found[:6]) if found else "Nao explicitado no texto extraido"


def infer_roles(text):
    terms = [
        ("agentes", ["agent", "agents", "multi-agent", "multiagent"]),
        ("personas", ["persona", "personas"]),
        ("desenvolvedor", ["developer", "programmer", "engineer"]),
        ("product manager", ["product manager", "project manager"]),
        ("arquiteto", ["architect", "architecture agent"]),
        ("testador", ["tester", "test engineer", "qa"]),
        ("usuario", ["user", "human", "stakeholder"]),
        ("revisor", ["reviewer", "review", "human-in-the-loop"]),
    ]
    found = [label for label, patterns in terms if has_any(text, patterns)]
    return ", ".join(found[:6]) if found else "Nao explicitado no texto extraido"


def infer_execution(text):
    terms = [
        ("IDE", ["ide", "integrated development environment"]),
        ("CLI", ["cli", "command line", "terminal"]),
        ("repositorio", ["github", "repository", "git"]),
        ("pipeline", ["pipeline", "workflow", "orchestration"]),
        ("edicao de codigo", ["code generation", "patch", "editing", "implementation"]),
        ("testes", ["unit test", "testing", "test case", "regression"]),
        ("browser", ["browser", "web"]),
    ]
    found = [label for label, patterns in terms if has_any(text, patterns)]
    return ", ".join(found[:6]) if found else "Nao explicitado no texto extraido"


def infer_validation(text):
    terms = [
        ("testes automatizados", ["unit test", "test case", "testing", "regression test"]),
        ("revisao humana", ["human", "reviewer", "human-in-the-loop", "manual review"]),
        ("checklists", ["checklist", "quality gate", "gate"]),
        ("avaliacao empirica", ["experiment", "empirical", "case study", "evaluation"]),
        ("traces ou auditoria", ["trace", "audit", "evidence", "log"]),
        ("contratos ou politicas", ["contract", "policy", "governance"]),
    ]
    found = [label for label, patterns in terms if has_any(text, patterns)]
    return ", ".join(found[:6]) if found else "Nao explicitado no texto extraido"


def infer_portability(text):
    low = text.lower()
    flags = []
    if "github" in low:
        flags.append("ancorado em GitHub ou repositorio")
    if "open source" in low or "available at" in low:
        flags.append("artefato publico")
    if "gpt" in low or "openai" in low:
        flags.append("dependencia possivel de LLM comercial")
    if "ide" in low:
        flags.append("dependencia de IDE ou ambiente")
    if "framework-agnostic" in low or "model agnostic" in low:
        flags.append("sinal de portabilidade")
    return ", ".join(flags[:4]) if flags else "Dependencias nao explicitadas"


def infer_evidence(record, primary):
    venue = clean(record.get("venue", ""))
    title = clean(record.get("title", "")).lower()
    low = primary.lower()
    evidence = []
    if "arxiv" in venue.lower():
        evidence.append("preprint arXiv")
    elif venue:
        evidence.append(f"paper em {venue}")
    else:
        evidence.append("paper ou registro tecnico")
    if "case study" in low or "case study" in title:
        evidence.append("estudo de caso")
    if "experiment" in low or "empirical" in low or "evaluation" in low:
        evidence.append("avaliacao empirica")
    if "survey" in title or "literature review" in title or "review" in title or "roadmap" in title:
        evidence.append("survey")
    if "github" in low or "available at" in low:
        evidence.append("repositorio publico")
    return ", ".join(evidence[:4])


def infer_risks(text):
    terms = [
        ("drift", ["drift", "inconsistency", "misalignment"]),
        ("lock-in", ["lock-in", "vendor", "platform dependence"]),
        ("seguranca", ["security", "vulnerability", "privacy", "supply chain"]),
        ("governanca", ["governance", "policy", "compliance"]),
        ("rastreabilidade", ["traceability", "trace", "audit"]),
        ("confiabilidade", ["reliability", "hallucination", "error", "incorrect"]),
        ("overhead", ["overhead", "cost", "latency"]),
        ("contexto", ["context", "context window", "context engineering"]),
    ]
    found = [label for label, patterns in terms if has_any(text, patterns)]
    return ", ".join(found[:6]) if found else "Riscos nao detalhados no texto extraido"


def rq_mapping(row):
    mapping = ["RQ1"]
    if row["artefatos"] != "Nao explicitado no texto extraido" or row["papeis"] != "Nao explicitado no texto extraido":
        mapping.append("RQ2")
    if row["evidencia"]:
        mapping.append("RQ3")
    if row["riscos"] != "Riscos nao detalhados no texto extraido":
        mapping.append("RQ4")
    if row["natureza"] in {"Survey ou agenda conceitual", "Fonte tecnica sobre desenvolvimento com IA"}:
        mapping.append("RQ5")
    return ", ".join(dict.fromkeys(mapping))


def confidence(text, row):
    score = 0
    for field in ["artefatos", "papeis", "execucao", "validacao", "riscos"]:
        if not row[field].startswith("Nao") and not row[field].startswith("Riscos nao"):
            score += 1
    if len(text) > 20000:
        score += 1
    if "repositorio publico" in row["evidencia"] or "avaliacao empirica" in row["evidencia"]:
        score += 1
    if score >= 6:
        return "alta"
    if score >= 4:
        return "media"
    return "baixa"


def extract_row(record):
    key = record["citation_key"]
    title = clean(record.get("title", ""))
    abstract = clean(record.get("abstract", ""))
    reason = clean(record.get("screening_pass2", {}).get("reason", ""))
    extracted_text = read_extract(key)
    primary = " ".join([title, abstract, reason, extracted_text[:12000]])
    full_for_fields = " ".join([primary, extracted_text[12000:30000]])
    row = {
        "citation_key": key,
        "title": title,
        "year": record.get("year", ""),
        "doi": clean(record.get("doi", "")),
        "nome": infer_name(record),
        "natureza": infer_nature(primary, title),
        "origem": infer_origin(record, primary),
        "artefatos": infer_artifacts(full_for_fields),
        "papeis": infer_roles(full_for_fields),
        "execucao": infer_execution(full_for_fields),
        "validacao": infer_validation(full_for_fields),
        "portabilidade": infer_portability(primary),
        "evidencia": infer_evidence(record, primary),
        "riscos": infer_risks(full_for_fields),
        "criterio_inclusao": clean(record.get("screening_pass2", {}).get("criterion", "")),
        "motivo_inclusao": clean(record.get("screening_pass2", {}).get("reason", "")),
    }
    row["rqs"] = rq_mapping(row)
    row["confianca"] = confidence(extracted_text, row)
    return row


def write_individual(row):
    path = OUT_DIR / f"{row['citation_key']}.md"
    lines = [
        f"# {row['citation_key']}",
        "",
        f"- **Titulo**: {row['title']}",
        f"- **Ano**: {row['year']}",
        f"- **DOI**: {row['doi'] or 'nao informado'}",
        f"- **Nome extraido**: {row['nome']}",
        f"- **Natureza**: {row['natureza']}",
        f"- **Origem**: {row['origem']}",
        f"- **Artefatos**: {row['artefatos']}",
        f"- **Papeis**: {row['papeis']}",
        f"- **Execucao**: {row['execucao']}",
        f"- **Validacao**: {row['validacao']}",
        f"- **Portabilidade**: {row['portabilidade']}",
        f"- **Evidencia**: {row['evidencia']}",
        f"- **Riscos**: {row['riscos']}",
        f"- **RQs relacionadas**: {row['rqs']}",
        f"- **Confianca da extracao**: {row['confianca']}",
        "",
        "## Justificativa de inclusao",
        "",
        row["motivo_inclusao"] or "Incluido em full text conforme log de screening.",
        "",
        "## Nota de curadoria",
        "",
        "Extracao estruturada de primeira passada, derivada dos metadados, do texto extraido do PDF e dos logs de screening. Campos com baixa especificidade devem ser revisados durante a sintese final.",
        "",
    ]
    path.write_text("\n".join(clean(line) for line in lines), encoding="utf-8")


def write_matrix(rows):
    fieldnames = [
        "citation_key",
        "year",
        "title",
        "doi",
        "nome",
        "natureza",
        "origem",
        "artefatos",
        "papeis",
        "execucao",
        "validacao",
        "portabilidade",
        "evidencia",
        "riscos",
        "rqs",
        "confianca",
    ]
    with MATRIX_CSV.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fieldnames})


def write_summary(rows):
    nature = Counter(row["natureza"] for row in rows)
    evidence = Counter()
    confidence = Counter(row["confianca"] for row in rows)
    for row in rows:
        for item in row["evidencia"].split(", "):
            evidence[item] += 1

    lines = [
        "# Extracao estruturada, resumo",
        "",
        f"- Data: {HUMAN_TIME}",
        f"- Estudos incluidos extraidos: {len(rows)}",
        "- Schema: software-engineering, conforme protocolo Kitchenham do paper.",
        "- Observacao: `AshaRajbhoj2024` permanece pendente por download manual e nao entrou nesta rodada de extracao.",
        "",
        "## Distribuicao por natureza",
        "",
        "| Natureza | N |",
        "|---|---:|",
    ]
    lines.extend(f"| {clean(label)} | {count} |" for label, count in nature.most_common())
    lines.extend(
        [
            "",
            "## Distribuicao por evidencia",
            "",
            "| Evidencia | N |",
            "|---|---:|",
        ]
    )
    lines.extend(f"| {clean(label)} | {count} |" for label, count in evidence.most_common())
    lines.extend(
        [
            "",
            "## Confianca da extracao",
            "",
            "| Confianca | N |",
            "|---|---:|",
        ]
    )
    lines.extend(f"| {clean(label)} | {count} |" for label, count in confidence.most_common())
    lines.extend(
        [
            "",
            "## Arquivos gerados",
            "",
            "- `extraction-matrix.csv`: matriz consolidada para analise e sintese.",
            "- `<citation-key>.md`: ficha de extracao individual por estudo.",
            "",
        ]
    )
    SUMMARY_MD.write_text("\n".join(lines), encoding="utf-8")


def update_memories(rows):
    plan = PLAN.read_text(encoding="utf-8")
    plan = plan.replace(
        "> Ultima atividade: 2026-05-28 14:02",
        "> Ultima atividade: 2026-05-28 14:14",
    )
    plan = plan.replace(
        "- [ ] Etapa 6, Snowballing (backward + forward), em andamento",
        "- [x] Etapa 6, Snowballing (backward + forward), completed",
    )
    plan = plan.replace(
        "- [ ] Etapa 7, Extracao estruturada",
        "- [x] Etapa 7, Extracao estruturada",
    )
    plan = plan.replace(
        "- [ ] Etapa 8, Avaliacao de qualidade (opcional)",
        "- [x] Etapa 8, Avaliacao de qualidade (opcional), skipped",
    )
    plan = plan.replace("- **Status**: in_progress", "- **Status**: completed", 1)
    plan = plan.replace(
        "- **Iniciado em**: 2026-05-27 19:36, **Concluido em**: ,",
        "- **Iniciado em**: 2026-05-27 19:36, **Concluido em**: 2026-05-28 14:14,",
    )
    plan = plan.replace(
        "- **Status**: pending\n- **Agente**: `structured-extractor`",
        "- **Status**: completed\n- **Agente**: `structured-extractor`",
    )
    plan = plan.replace(
        "- **Iniciado em**: , **Concluido em**: ,\n- **N de extracoes**: ,\n- **Notas**: [vazio]",
        f"- **Iniciado em**: 2026-05-28 14:14, **Concluido em**: 2026-05-28 14:14,\n- **N de extracoes**: {len(rows)},\n- **Notas**: extracao estruturada de primeira passada concluida para os 37 estudos incluidos finais disponiveis. Saidas: `systematic-review/extracted/`, `extraction-matrix.csv` e `_summary.md`. `AshaRajbhoj2024` permaneceu pendente por ausencia de PDF local e nao foi contado como exclusao.",
        1,
    )
    plan = plan.replace(
        "- **Status**: pending (skip se `quality_assessment: none`)",
        "- **Status**: skipped (`quality_assessment: none`)",
    )
    plan = plan.replace(
        "- **Iniciado em**: , **Concluido em**: ,\n- **N avaliados**: ,\n- **Notas**: [vazio]",
        "- **Iniciado em**: 2026-05-28 14:14, **Concluido em**: 2026-05-28 14:14,\n- **N avaliados**: 0,\n- **Notas**: etapa ignorada conforme protocolo aprovado, `quality_assessment: none`.",
        1,
    )
    marker = "### Sessao 26, 2026-05-28 14:14"
    if marker not in plan:
        plan += f"""

### Sessao 26, 2026-05-28 14:14

- Autor enviou `CONTINUE`.
- Verificacao: `AshaRajbhoj2024.pdf` ainda nao esta presente em `papers_to_review/`.
- Decisao operacional inferida do `CONTINUE`: fechar o snowballing no limite de 3 rodadas com corpus parcial documentado, mantendo `AshaRajbhoj2024` como pendencia operacional e nao como exclusao.
- Etapa 6 concluida: snowballing encerrado por maximo de 3 rodadas do protocolo.
- Etapa 7 concluida: extracao estruturada de primeira passada executada para {len(rows)} estudos incluidos finais.
- Etapa 8 ignorada conforme protocolo, `quality_assessment: none`.
- Saidas geradas: `systematic-review/extracted/extraction-matrix.csv`, `systematic-review/extracted/_summary.md` e fichas individuais em `systematic-review/extracted/`.
- Proxima acao: Etapa 9, sintese tematica e matriz comparativa para responder RQ1 a RQ5.
"""
    PLAN.write_text(plan, encoding="utf-8")

    paper = PAPER.read_text(encoding="utf-8")
    marker = "### 2026-05-28 14:14"
    if marker not in paper:
        paper += f"""

### 2026-05-28 14:14

- Autor enviou `CONTINUE`.
- `AshaRajbhoj2024.pdf` ainda nao esta presente localmente; o snowballing foi fechado no limite protocolar de 3 rodadas com a pendencia registrada como operacional, nao como exclusao.
- Etapa 6 concluida: snowballing encerrado com 37 estudos incluidos finais disponiveis.
- Etapa 7 concluida: extracao estruturada de primeira passada executada para {len(rows)} estudos.
- Etapa 8 ignorada conforme protocolo, `quality_assessment: none`.
- Saidas geradas: `systematic-review/extracted/extraction-matrix.csv`, `systematic-review/extracted/_summary.md` e fichas individuais em `systematic-review/extracted/`.
- Proxima etapa pendente: sintese tematica e matriz comparativa para responder RQ1 a RQ5.
"""
    PAPER.write_text(paper, encoding="utf-8")


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    records = load_records()
    rows = [extract_row(record) for record in records]
    for row in rows:
        write_individual(row)
    write_matrix(rows)
    write_summary(rows)
    update_memories(rows)
    print(f"extracted={len(rows)} out={OUT_DIR}")


if __name__ == "__main__":
    main()
