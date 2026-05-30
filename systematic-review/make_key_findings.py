#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Segunda passada de extracao: consolida um achado narrativo (key finding) por estudo
a partir das fichas de extracao (extracted/*.md), reduzindo a dependencia da identidade
publica dos frameworks (IMP-4 do score.md).

NAO fabrica achados: cada linha narrativa e montada a partir do campo "Justificativa de
inclusao" da ficha e dos campos estruturados (Natureza, Artefatos, Papeis, Execucao,
Validacao, Riscos). Quando a justificativa e generica, a linha sinaliza isso, em vez de
inventar conteudo.

Saidas:
  extracted/key-findings.md   (uma entrada por estudo, com o achado narrativo)
  extracted/key-findings.csv  (citation_key, achado, fonte=justificativa/estruturado)
"""
import csv
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
EXTRACTED = os.path.join(HERE, "extracted")
MATRIX = os.path.join(EXTRACTED, "extraction-matrix.csv")
OUT_MD = os.path.join(EXTRACTED, "key-findings.md")
OUT_CSV = os.path.join(EXTRACTED, "key-findings.csv")

# Template generico de justificativa de 1a passada (sem conteudo especifico do estudo).
GENERIC_MARKERS = [
    "confirma fonte dentro do escopo",
    "descreve framework, metodo, plataforma, arquitetura, workflow",
]


def read_field(text, label):
    m = re.search(rf"- \*\*{re.escape(label)}\*\*:\s*(.+)", text)
    return m.group(1).strip() if m else ""


def read_section(text, header):
    m = re.search(rf"## {re.escape(header)}\s*\n+(.+?)(?:\n## |\Z)", text, re.S)
    return m.group(1).strip() if m else ""


def is_generic(just):
    j = just.lower()
    return any(g in j for g in GENERIC_MARKERS)


def main():
    with open(MATRIX, encoding="utf-8") as f:
        keys = [r["citation_key"] for r in csv.DictReader(f)]

    rows = []
    for k in keys:
        path = os.path.join(EXTRACTED, f"{k}.md")
        if not os.path.exists(path):
            rows.append({"citation_key": k, "achado": "(ficha ausente)", "fonte": "ausente"})
            continue
        text = open(path, encoding="utf-8").read()
        just = read_section(text, "Justificativa de inclusao")
        nome = read_field(text, "Nome extraido")
        natureza = read_field(text, "Natureza")
        if just and not is_generic(just):
            achado = just
            fonte = "justificativa"
        else:
            # fallback estruturado, sem inventar: descreve o que a ficha registra
            partes = []
            for lab in ("Papeis", "Execucao", "Validacao", "Artefatos", "Riscos"):
                v = read_field(text, lab)
                if v:
                    partes.append(f"{lab.lower()}: {v}")
            achado = f"{nome or k} ({natureza or 'estudo'}); " + "; ".join(partes[:4]) + " [achado consolidado dos campos estruturados; justificativa de 1a passada generica]"
            fonte = "estruturado"
        rows.append({"citation_key": k, "achado": achado, "fonte": fonte})

    with open(OUT_CSV, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["citation_key", "achado", "fonte"])
        w.writeheader()
        w.writerows(rows)

    n_just = sum(1 for r in rows if r["fonte"] == "justificativa")
    n_struct = sum(1 for r in rows if r["fonte"] == "estruturado")
    lines = ["# Achados narrativos por estudo (segunda passada)\n",
             f"> Gerado por make_key_findings.py sobre extracted/*.md ({len(rows)} estudos).",
             f"> {n_just} com achado da justificativa substantiva; {n_struct} consolidados dos campos estruturados.\n"]
    for r in rows:
        lines.append(f"- **{r['citation_key']}** ({r['fonte']}): {r['achado']}")
    with open(OUT_MD, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"{len(rows)} estudos; justificativa={n_just}, estruturado={n_struct}")


if __name__ == "__main__":
    main()
