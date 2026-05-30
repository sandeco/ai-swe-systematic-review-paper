#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kit de confiabilidade entre avaliadores (IRR) para a triagem (IMP-1 do score.md).

CONTEXTO HONESTO: a triagem registrada nos logs (screening/*.log.csv) foi conduzida
por um unico avaliador operacional (`screening-logger`) seguindo o protocolo. Este kit
NAO inventa um segundo avaliador nem fabrica um kappa. Ele faz duas coisas:

  1) `build_sheets()` gera planilhas de codificacao (coding sheets) com a decisao do
     avaliador 1 ja preenchida (a partir dos logs reais) e uma coluna `reviewer2_decision`
     EM BRANCO, para que um SEGUNDO CODIFICADOR HUMANO INDEPENDENTE re-triagem a amostra.
  2) `compute_kappa()` le uma planilha ja preenchida pelo segundo codificador e calcula
     o Cohen's kappa entre os dois avaliadores, com a interpretacao de Landis e Koch.

Assim o ponto cheio de IRR (kappa de dois humanos) fica disponivel para o autor fechar,
sem que a skill simule concordancia. Rode `build_sheets` agora; rode `compute_kappa`
depois que o segundo codificador preencher `reviewer2_decision`.

Uso:
  python3 irr_kit.py build          # gera as coding sheets em screening/irr/
  python3 irr_kit.py kappa <sheet>  # calcula kappa de uma planilha preenchida
"""
import csv
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SCR = os.path.join(HERE, "screening")
IRR = os.path.join(SCR, "irr")

PHASES = {
    "title-abstract": "title-abstract.log.csv",
    "full-text": "full-text.log.csv",
}


def build_sheets():
    os.makedirs(IRR, exist_ok=True)
    for phase, fname in PHASES.items():
        src = os.path.join(SCR, fname)
        if not os.path.exists(src):
            print(f"[skip] {src} nao encontrado")
            continue
        with open(src, encoding="utf-8") as f:
            rows = list(csv.DictReader(f))
        out = os.path.join(IRR, f"coding-sheet-{phase}.csv")
        with open(out, "w", encoding="utf-8", newline="") as f:
            w = csv.writer(f)
            w.writerow([
                "citation_key", "title", "year",
                "reviewer1_decision", "reviewer1_criterion",
                "reviewer2_decision", "reviewer2_criterion", "notes",
            ])
            for r in rows:
                w.writerow([
                    r.get("citation_key", ""), r.get("title", ""), r.get("year", ""),
                    r.get("decision", ""), r.get("criterion", ""),
                    "", "", "",  # reviewer 2 preenche
                ])
        print(f"[ok] {out} ({len(rows)} itens; reviewer2_decision em branco)")


def cohen_kappa(a, b):
    """Cohen's kappa para duas listas de rotulos pareadas."""
    assert len(a) == len(b) and a, "listas vazias ou de tamanhos diferentes"
    n = len(a)
    labels = sorted(set(a) | set(b))
    po = sum(1 for x, y in zip(a, b) if x == y) / n
    pe = 0.0
    for lab in labels:
        pa = sum(1 for x in a if x == lab) / n
        pb = sum(1 for y in b if y == lab) / n
        pe += pa * pb
    if pe == 1.0:
        return 1.0, po, pe
    return (po - pe) / (1 - pe), po, pe


def interpret(k):
    if k < 0:
        return "pobre (poor)"
    if k <= 0.20:
        return "leve (slight)"
    if k <= 0.40:
        return "razoavel (fair)"
    if k <= 0.60:
        return "moderada (moderate)"
    if k <= 0.80:
        return "substancial (substantial)"
    return "quase perfeita (almost perfect)"


def compute_kappa(sheet):
    with open(sheet, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    a, b = [], []
    for r in rows:
        d1 = (r.get("reviewer1_decision") or "").strip().lower()
        d2 = (r.get("reviewer2_decision") or "").strip().lower()
        if d1 and d2:
            a.append(d1)
            b.append(d2)
    if not a:
        print("Nenhum par avaliado: a coluna reviewer2_decision ainda esta vazia.")
        print("Preencha reviewer2_decision com include/exclude e rode de novo.")
        return
    k, po, pe = cohen_kappa(a, b)
    print(f"Pares avaliados: {len(a)}")
    print(f"Concordancia observada (Po): {po:.3f}")
    print(f"Concordancia esperada (Pe): {pe:.3f}")
    print(f"Cohen's kappa: {k:.3f}  ->  concordancia {interpret(k)} (Landis e Koch, 1977)")


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "build"
    if cmd == "build":
        build_sheets()
    elif cmd == "kappa" and len(sys.argv) > 2:
        compute_kappa(sys.argv[2])
    else:
        print(__doc__)
