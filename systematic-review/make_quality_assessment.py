#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Avaliacao de qualidade / risco de vies dos estudos incluidos (IMP-2 do score.md).

Aplica um checklist de qualidade adaptado de Kitchenham (itens para estudos
primarios) e DARE/CASP, derivando cada item de sinais OBSERVAVEIS e rastreaveis
na matriz de extracao (extracted/extraction-matrix.csv). Nenhum valor e inventado:
cada item vem do campo `evidencia` (tipo de venue, avaliacao empirica, estudo de
caso, repositorio publico) e do campo `confianca` ja registrado na extracao.

Itens de qualidade (cada um binario, 0/1):
  QA1  Venue revisado por pares (journal ou conferencia indexada), nao preprint
       nem registro tecnico nao indexado.
  QA2  Avaliacao empirica reportada (experimento, medicao, estudo controlado).
  QA3  Validacao aplicada (estudo de caso, aplicacao em projeto real).
  QA4  Artefato publico para reprodutibilidade (repositorio publico).

Score de qualidade QA = QA1+QA2+QA3+QA4 (0 a 4). Faixa:
  ALTA   QA >= 3
  MEDIA  QA == 2
  BAIXA  QA <= 1

Saidas:
  extracted/quality-assessment.csv   (uma linha por estudo, itens + score + faixa)
  extracted/quality-summary.md       (distribuicoes para o texto do paper)
"""
import csv
import os

HERE = os.path.dirname(os.path.abspath(__file__))
MATRIX = os.path.join(HERE, "extracted", "extraction-matrix.csv")
OUT_CSV = os.path.join(HERE, "extracted", "quality-assessment.csv")
OUT_MD = os.path.join(HERE, "extracted", "quality-summary.md")

PREPRINT_MARK = "preprint arxiv"
TECH_RECORD_MARK = "paper ou registro tecnico"


def classify(ev: str):
    e = ev.lower()
    is_preprint = PREPRINT_MARK in e
    is_tech_record = TECH_RECORD_MARK in e
    qa1 = 0 if (is_preprint or is_tech_record) else 1  # peer-reviewed venue
    qa2 = 1 if "avaliacao empirica" in e else 0        # empirical evaluation
    qa3 = 1 if "estudo de caso" in e else 0            # case study / applied
    qa4 = 1 if "repositorio publico" in e else 0       # public artifact
    venue = "preprint" if is_preprint else ("registro tecnico" if is_tech_record else "revisado por pares")
    return qa1, qa2, qa3, qa4, venue


def tier(score: int) -> str:
    if score >= 3:
        return "ALTA"
    if score == 2:
        return "MEDIA"
    return "BAIXA"


def main():
    with open(MATRIX, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    out = []
    for r in rows:
        qa1, qa2, qa3, qa4, venue = classify(r["evidencia"])
        score = qa1 + qa2 + qa3 + qa4
        out.append({
            "citation_key": r["citation_key"],
            "year": r["year"],
            "venue_type": venue,
            "QA1_peer_reviewed": qa1,
            "QA2_empirical": qa2,
            "QA3_case_study": qa3,
            "QA4_public_repo": qa4,
            "QA_score": score,
            "QA_tier": tier(score),
            "confianca_extracao": r["confianca"],
        })

    with open(OUT_CSV, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(out[0].keys()))
        w.writeheader()
        w.writerows(out)

    n = len(out)
    by_tier = {"ALTA": 0, "MEDIA": 0, "BAIXA": 0}
    by_venue = {}
    item_counts = {"QA1_peer_reviewed": 0, "QA2_empirical": 0, "QA3_case_study": 0, "QA4_public_repo": 0}
    for o in out:
        by_tier[o["QA_tier"]] += 1
        by_venue[o["venue_type"]] = by_venue.get(o["venue_type"], 0) + 1
        for k in item_counts:
            item_counts[k] += o[k]

    lines = []
    lines.append("# Avaliacao de qualidade dos estudos incluidos\n")
    lines.append(f"> Gerado por make_quality_assessment.py sobre extraction-matrix.csv ({n} estudos).")
    lines.append("> Checklist adaptado de Kitchenham/DARE; cada item derivado de sinais observaveis na extracao.\n")
    lines.append("## Distribuicao por faixa de qualidade\n")
    lines.append("| Faixa | Criterio | Estudos | % |")
    lines.append("|---|---|---:|---:|")
    for t, crit in [("ALTA", "QA >= 3"), ("MEDIA", "QA == 2"), ("BAIXA", "QA <= 1")]:
        c = by_tier[t]
        lines.append(f"| {t} | {crit} | {c} | {100*c/n:.0f}% |")
    lines.append("")
    lines.append("## Distribuicao por tipo de venue\n")
    lines.append("| Tipo de venue | Estudos | % |")
    lines.append("|---|---:|---:|")
    for v in ("revisado por pares", "preprint", "registro tecnico"):
        c = by_venue.get(v, 0)
        lines.append(f"| {v} | {c} | {100*c/n:.0f}% |")
    lines.append("")
    lines.append("## Cobertura por item de qualidade\n")
    lines.append("| Item | Descricao | Estudos que atendem | % |")
    lines.append("|---|---|---:|---:|")
    labels = {
        "QA1_peer_reviewed": "Venue revisado por pares",
        "QA2_empirical": "Avaliacao empirica reportada",
        "QA3_case_study": "Validacao aplicada (estudo de caso)",
        "QA4_public_repo": "Artefato publico (repositorio)",
    }
    for k, lab in labels.items():
        c = item_counts[k]
        lines.append(f"| {k.split('_')[0]} | {lab} | {c} | {100*c/n:.0f}% |")
    lines.append("")
    lines.append("## Estudos de menor confianca (faixa BAIXA ou confianca media na extracao)\n")
    lines.append("| Estudo | Ano | Venue | QA | Faixa | Confianca extracao |")
    lines.append("|---|---|---|---:|---|---|")
    for o in out:
        if o["QA_tier"] == "BAIXA" or o["confianca_extracao"] == "media":
            lines.append(f"| {o['citation_key']} | {o['year']} | {o['venue_type']} | {o['QA_score']} | {o['QA_tier']} | {o['confianca_extracao']} |")
    lines.append("")

    with open(OUT_MD, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print("\n".join(lines))


if __name__ == "__main__":
    main()
