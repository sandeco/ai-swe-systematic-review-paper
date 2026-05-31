# -*- coding: utf-8 -*-
"""Gera a figura da metodologia (funil Kitchenham) do paper ai-dev-frameworks-review.
Contagens batem exatamente com tex/sections/02_metodo_revisao.tex.
Saida: figures/methodology.{pdf,png,svg} na raiz do paper.
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from matplotlib.lines import Line2D

PAPER = r"C:\SCIENTEX\_papers\ai-dev-frameworks-review"
OUT = os.path.join(PAPER, "figures")
os.makedirs(OUT, exist_ok=True)

# Paleta sobria, fundo branco
C_MAIN = "#2C5F8A"   # caixas do fluxo principal
C_MAIN_F = "#E8F0F7"
C_EXCL = "#9A3B3B"   # caixas de exclusao
C_EXCL_F = "#F6EBEB"
C_FINAL = "#1F6B3B"  # corpus final
C_FINAL_F = "#E6F2EA"
C_LANE = "#F4F4F4"
C_LANE_EDGE = "#D8D8D8"
TXT = "#1A1A1A"

fig, ax = plt.subplots(figsize=(8.6, 11.0))
ax.set_xlim(0, 100)
ax.set_ylim(0, 132)
ax.axis("off")
fig.patch.set_facecolor("white")
ax.set_facecolor("white")

# ---- Raias (6 fases) ----
lanes = [
    ("Identificação", 118, 132),
    ("Seleção",        78, 118),
    ("Snowballing",    44,  78),
    ("Extração",       30,  44),
    ("Síntese",        16,  30),
    ("Relato",          2,  16),
]
LANE_X = 1.5
LANE_W = 97
for name, y0, y1 in lanes:
    ax.add_patch(FancyBboxPatch((LANE_X, y0), LANE_W, y1 - y0,
                 boxstyle="round,pad=0.2,rounding_size=1.2",
                 fc=C_LANE, ec=C_LANE_EDGE, lw=1.0, zorder=0))
    ax.text(LANE_X + 1.6, (y0 + y1) / 2, name, rotation=90, va="center", ha="center",
            fontsize=11, fontweight="bold", color="#555555", zorder=1)

CX = 40          # centro coluna do fluxo principal
BW, BH = 46, 7.5  # largura/altura caixa principal
EX_X = 78         # coluna de exclusoes
EBW, EBH = 36, 6.5

def box(cx, cy, w, h, text, fc, ec, fs=10.5, bold=False, z=3):
    ax.add_patch(FancyBboxPatch((cx - w/2, cy - h/2), w, h,
                 boxstyle="round,pad=0.3,rounding_size=1.0",
                 fc=fc, ec=ec, lw=1.6, zorder=z))
    ax.text(cx, cy, text, va="center", ha="center", fontsize=fs,
            color=TXT, zorder=z+1, fontweight=("bold" if bold else "normal"))

def arrow(x0, y0, x1, y1, color=C_MAIN, lw=1.8, z=2):
    ax.add_patch(FancyArrowPatch((x0, y0), (x1, y1),
                 arrowstyle="-|>", mutation_scale=16, color=color, lw=lw, zorder=z,
                 shrinkA=2, shrinkB=2))

# ---- Fluxo principal ----
# Identificacao
box(CX, 125, BW, BH,
    "Busca multibase (arXiv, ACM, IEEE,\nCrossref, OpenAlex, Semantic Scholar)\n100 registros brutos",
    C_MAIN_F, C_MAIN, fs=9.5)
# Selecao: 85 candidatos
box(CX, 110, BW, BH,
    "85 candidatos\n(dedup + filtro 2018-2026 + 1 seed dirigido)",
    C_MAIN_F, C_MAIN, fs=9.5)
box(CX, 96, BW, BH,
    "Triagem por título e resumo\n28 incluídos",
    C_MAIN_F, C_MAIN, fs=9.5)
box(CX, 82, BW, BH,
    "Leitura de texto completo\n25 incluídos finais",
    C_MAIN_F, C_MAIN, fs=9.5)
# Snowballing
box(CX, 71, BW, BH,
    "Snowballing backward + forward\n3 rodadas, 149 candidatos adicionais",
    C_MAIN_F, C_MAIN, fs=9.5)
box(CX, 57.5, BW, 9.5,
    "R1: 69 novos -> 6 incluídos\nR2: 50 novos -> 3 incluídos\nR3: 30 novos -> 3 incluídos\n(forward: 0 elegíveis)",
    C_MAIN_F, C_MAIN, fs=9.0)
box(CX, 47, BW, BH,
    "12 estudos novos incorporados",
    C_MAIN_F, C_MAIN, fs=9.5)
# Extracao
box(CX, 37, BW, BH,
    "Extração estruturada (10 campos)\n37 estudos",
    C_MAIN_F, C_MAIN, fs=9.5)
# Sintese
box(CX, 23, BW, BH,
    "Síntese temática híbrida\n6 temas x taxonomia de 6 dimensões",
    C_MAIN_F, C_MAIN, fs=9.5)
# Relato (corpus final)
box(CX, 9, BW, 8.5,
    "Corpus final\n37 estudos incluídos",
    C_FINAL_F, C_FINAL, fs=11, bold=True)

# ---- Setas do fluxo principal ----
seq_y = [125, 110, 96, 82, 71, 57.5, 47, 37, 23]
tops_bottoms = [
    (125-BH/2, 110+BH/2),
    (110-BH/2, 96+BH/2),
    (96-BH/2, 82+BH/2),
    (82-BH/2, 71+BH/2),
    (71-BH/2, 57.5+9.5/2),
    (57.5-9.5/2, 47+BH/2),
    (47-BH/2, 37+BH/2),
    (37-BH/2, 23+BH/2),
    (23-BH/2, 9+8.5/2),
]
for yb, yt in tops_bottoms:
    arrow(CX, yb, CX, yt)

# ---- Caixas de exclusao (laterais) ----
def excl(cy, text):
    box(EX_X, cy, EBW, EBH, text, C_EXCL_F, C_EXCL, fs=9.0)
    arrow(CX + BW/2, cy + 0.2, EX_X - EBW/2, cy, color=C_EXCL, lw=1.4)

excl(103, "Excluídos na triagem\ntítulo/resumo: 57")
excl(89, "Excluídos em\ntexto completo: 3")

# Nota da pendencia operacional
ax.text(CX, 3.0,
        "1 fonte aprovada na triagem da R3 ficou sem texto completo na data de corte\n(pendência operacional, não exclusão). Data de corte: 26 de maio de 2026.",
        va="center", ha="center", fontsize=7.6, color="#666666", style="italic", zorder=5)

# Titulo
ax.text(50, 130.8, "Fluxo da revisão de literatura multivocal (protocolo Kitchenham)",
        va="center", ha="center", fontsize=12.5, fontweight="bold", color=TXT)

plt.subplots_adjust(left=0.01, right=0.99, top=0.99, bottom=0.01)

for ext in ("pdf", "png", "svg"):
    p = os.path.join(OUT, f"methodology.{ext}")
    fig.savefig(p, dpi=300, facecolor="white", bbox_inches="tight")
    print("wrote", p)
print("done")
