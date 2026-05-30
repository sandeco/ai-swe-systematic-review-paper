# -*- coding: utf-8 -*-
"""Saturation figure for the snowballing rounds (IMP-5), bilingual (pt-br + en).

Values trace to systematic-review/snowballing/round-{1,2,3}/summary.md and to the
Method section: initial search included 25 studies (2 passes); the three snowballing
rounds screened 69, 50 and 30 new candidates and included 6, 3 and 3 new studies,
consolidating the corpus at 37. The figure shows decelerating new inclusions per round.

SCIENTEX rules: 96 DPI (rule 13), min 12pt fonts (rule 12), [h!] when inserted.
Output: figures/snowball_saturation_{pt,en}.{pdf,png} at the paper root.
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams["font.size"] = 12
plt.rcParams["axes.titlesize"] = 14
plt.rcParams["axes.labelsize"] = 13

PAPER = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
OUT = os.path.join(PAPER, "figures")
os.makedirs(OUT, exist_ok=True)
DPI = 96
BLUE = "#2C5F8A"; GREEN = "#1F6B3B"; GREY = "#777777"

# Real data (round 0 = initial database search after 2 screening passes).
rounds = [0, 1, 2, 3]
candidates = [85, 69, 50, 30]   # screened candidates per stage (85 = initial pool)
included = [25, 6, 3, 3]        # new studies included per stage
cumulative = [25, 31, 34, 37]   # running corpus size


def fig_saturation(lang):
    if lang == "pt":
        xlabels = ["Busca\ninicial", "Snowball\nrodada 1", "Snowball\nrodada 2", "Snowball\nrodada 3"]
        title = "Saturação do snowballing: novos estudos incluídos por rodada"
        ylab_l = "Novos estudos incluídos"
        ylab_r = "Corpus acumulado"
        leg_inc = "Novos incluídos na rodada"
        leg_cum = "Corpus acumulado"
    else:
        xlabels = ["Initial\nsearch", "Snowball\nround 1", "Snowball\nround 2", "Snowball\nround 3"]
        title = "Snowballing saturation: new studies included per round"
        ylab_l = "New studies included"
        ylab_r = "Cumulative corpus"
        leg_inc = "New inclusions in round"
        leg_cum = "Cumulative corpus"

    x = list(range(len(rounds)))
    fig, ax = plt.subplots(figsize=(7.8, 4.6))
    bars = ax.bar(x, included, color=BLUE, width=0.55, label=leg_inc)
    for b, v in zip(bars, included):
        ax.text(b.get_x() + b.get_width() / 2, v + 0.4, str(v), ha="center", va="bottom", fontsize=12)
    ax.set_ylabel(ylab_l)
    ax.set_ylim(0, max(included) + 4)
    ax.set_xticks(x)
    ax.set_xticklabels(xlabels, fontsize=12)
    ax.set_title(title)
    ax.spines["top"].set_visible(False)
    ax.tick_params(labelsize=12)

    ax2 = ax.twinx()
    ax2.plot(x, cumulative, color=GREEN, marker="o", linewidth=2, label=leg_cum)
    for xi, v in zip(x, cumulative):
        ax2.text(xi, v + 0.6, str(v), ha="center", va="bottom", fontsize=12, color=GREEN)
    ax2.set_ylabel(ylab_r, color=GREEN)
    ax2.set_ylim(0, 44)
    ax2.tick_params(axis="y", labelcolor=GREEN, labelsize=12)
    ax2.spines["top"].set_visible(False)

    lines_l, labels_l = ax.get_legend_handles_labels()
    lines_r, labels_r = ax2.get_legend_handles_labels()
    ax.legend(lines_l + lines_r, labels_l + labels_r, loc="upper right", fontsize=12, frameon=False)

    for ext in ("pdf", "png"):
        fig.savefig(os.path.join(OUT, f"snowball_saturation_{lang}.{ext}"), dpi=DPI, facecolor="white", bbox_inches="tight")
    plt.close(fig)
    print("wrote", f"snowball_saturation_{lang}")


for lang in ("pt", "en"):
    fig_saturation(lang)
print("ALL DONE")
