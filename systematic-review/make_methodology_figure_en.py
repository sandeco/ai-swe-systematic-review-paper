# -*- coding: utf-8 -*-
"""Methodology figure (Kitchenham funnel), English labels.
Counts match tex/sections/02_metodo_revisao.tex exactly.
Compliant with SCIENTEX rules 12 (min 12pt) and 13 (96 DPI).
Output: figures/methodology.{pdf,png,svg} at the paper root.
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

plt.rcParams["font.size"] = 12  # rule 12 floor

PAPER = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
OUT = os.path.join(PAPER, "figures")
os.makedirs(OUT, exist_ok=True)

C_MAIN = "#2C5F8A"; C_MAIN_F = "#E8F0F7"
C_EXCL = "#9A3B3B"; C_EXCL_F = "#F6EBEB"
C_FINAL = "#1F6B3B"; C_FINAL_F = "#E6F2EA"
C_LANE = "#F4F4F4"; C_LANE_EDGE = "#D8D8D8"
TXT = "#1A1A1A"

# Larger canvas so 12pt text fits the dense funnel boxes (rule 12).
fig, ax = plt.subplots(figsize=(12.6, 16.2))
ax.set_xlim(0, 100)
ax.set_ylim(0, 132)
ax.axis("off")
fig.patch.set_facecolor("white")
ax.set_facecolor("white")

lanes = [
    ("Identification", 118, 132),
    ("Selection",       78, 118),
    ("Snowballing",     44,  78),
    ("Extraction",      30,  44),
    ("Synthesis",       16,  30),
    ("Reporting",        2,  16),
]
LANE_X = 1.5; LANE_W = 97
for name, y0, y1 in lanes:
    ax.add_patch(FancyBboxPatch((LANE_X, y0), LANE_W, y1 - y0,
                 boxstyle="round,pad=0.2,rounding_size=1.2",
                 fc=C_LANE, ec=C_LANE_EDGE, lw=1.0, zorder=0))
    ax.text(LANE_X + 1.8, (y0 + y1) / 2, name, rotation=90, va="center", ha="center",
            fontsize=13, fontweight="bold", color="#555555", zorder=1)

CX = 40; BW, BH = 50, 8.0
EX_X = 80; EBW, EBH = 38, 7.5

def box(cx, cy, w, h, text, fc, ec, fs=12, bold=False, z=3):
    ax.add_patch(FancyBboxPatch((cx - w/2, cy - h/2), w, h,
                 boxstyle="round,pad=0.3,rounding_size=1.0",
                 fc=fc, ec=ec, lw=1.6, zorder=z))
    ax.text(cx, cy, text, va="center", ha="center", fontsize=fs,
            color=TXT, zorder=z+1, fontweight=("bold" if bold else "normal"))

def arrow(x0, y0, x1, y1, color=C_MAIN, lw=1.8, z=2):
    ax.add_patch(FancyArrowPatch((x0, y0), (x1, y1),
                 arrowstyle="-|>", mutation_scale=16, color=color, lw=lw, zorder=z,
                 shrinkA=2, shrinkB=2))

box(CX, 125, BW, BH,
    "Multi-database search (arXiv, ACM, IEEE,\nCrossref, OpenAlex, Semantic Scholar)\n100 raw records", C_MAIN_F, C_MAIN, fs=12)
box(CX, 110, BW, BH,
    "85 candidates\n(dedup + 2018-2026 filter + 1 directed seed)", C_MAIN_F, C_MAIN, fs=12)
box(CX, 96, BW, BH,
    "Title and abstract screening\n28 included", C_MAIN_F, C_MAIN, fs=12)
box(CX, 82, BW, BH,
    "Full-text reading\n25 final included", C_MAIN_F, C_MAIN, fs=12)
box(CX, 71, BW, BH,
    "Backward + forward snowballing\n3 rounds, 149 additional candidates", C_MAIN_F, C_MAIN, fs=12)
box(CX, 57, BW, 10.5,
    "R1: 69 new -> 6 included\nR2: 50 new -> 3 included\nR3: 30 new -> 3 included\n(forward: 0 eligible)", C_MAIN_F, C_MAIN, fs=12)
box(CX, 46, BW, BH,
    "12 new studies incorporated", C_MAIN_F, C_MAIN, fs=12)
box(CX, 37, BW, BH,
    "Structured extraction (10 fields)\n37 studies", C_MAIN_F, C_MAIN, fs=12)
box(CX, 23, BW, BH,
    "Hybrid thematic synthesis\n6 themes x 6-dimension taxonomy", C_MAIN_F, C_MAIN, fs=12)
box(CX, 9, BW, 9.0,
    "Final corpus\n37 included studies", C_FINAL_F, C_FINAL, fs=13, bold=True)

tops_bottoms = [
    (125-BH/2, 110+BH/2), (110-BH/2, 96+BH/2), (96-BH/2, 82+BH/2),
    (82-BH/2, 71+BH/2), (71-BH/2, 57+10.5/2), (57-10.5/2, 46+BH/2),
    (46-BH/2, 37+BH/2), (37-BH/2, 23+BH/2), (23-BH/2, 9+9.0/2),
]
for yb, yt in tops_bottoms:
    arrow(CX, yb, CX, yt)

def excl(cy, text):
    box(EX_X, cy, EBW, EBH, text, C_EXCL_F, C_EXCL, fs=12)
    arrow(CX + BW/2, cy + 0.2, EX_X - EBW/2, cy, color=C_EXCL, lw=1.4)

excl(103, "Excluded at title/abstract\nscreening: 57")
excl(89, "Excluded at\nfull text: 3")

ax.text(CX, 2.6,
        "1 source approved at R3 screening lacked full text at the cutoff date\n(operational pending item, not an exclusion). Cutoff date: May 26, 2026.",
        va="center", ha="center", fontsize=12, color="#666666", style="italic", zorder=5)

ax.text(50, 130.8, "Multivocal literature review flow (Kitchenham protocol)",
        va="center", ha="center", fontsize=14, fontweight="bold", color=TXT)

plt.subplots_adjust(left=0.01, right=0.99, top=0.99, bottom=0.01)

for ext in ("pdf", "png", "svg"):
    p = os.path.join(OUT, f"methodology.{ext}")
    fig.savefig(p, dpi=96, facecolor="white", bbox_inches="tight")  # rule 13: 96 DPI
    print("wrote", p)
print("done")
