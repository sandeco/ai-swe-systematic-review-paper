# -*- coding: utf-8 -*-
"""Data figures for the systematic review, bilingual (pt-br + en).
All values trace to systematic-review/extracted/extraction-matrix.csv / synthesis.md.
SCIENTEX rules: 96 DPI (rule 13), min 12pt fonts (rule 12).
Output: figures/<name>_{pt,en}.{pdf,png} at the paper root.
"""
import os, csv
from collections import Counter
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.size"] = 12
plt.rcParams["axes.titlesize"] = 14
plt.rcParams["axes.labelsize"] = 13

PAPER = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
OUT = os.path.join(PAPER, "figures")
os.makedirs(OUT, exist_ok=True)
DPI = 96
BLUE = "#2C5F8A"; GREEN = "#1F6B3B"; RED = "#9A3B3B"; GREY = "#777777"

rows = list(csv.DictReader(open(os.path.join(PAPER, "systematic-review/extracted/extraction-matrix.csv"))))

def save(fig, name):
    for ext in ("pdf", "png"):
        fig.savefig(os.path.join(OUT, f"{name}.{ext}"), dpi=DPI, facecolor="white", bbox_inches="tight")
    plt.close(fig)
    print("wrote", name)

# ---------------- Figure: studies by year ----------------
years = Counter(r["year"] for r in rows)
yk = sorted(years)
yv = [years[y] for y in yk]
def fig_year(lang):
    t = {"pt": ("Estudos por ano de publicacao", "Ano", "Numero de estudos"),
         "en": ("Studies by publication year", "Year", "Number of studies")}[lang]
    fig, ax = plt.subplots(figsize=(7.2, 4.2))
    bars = ax.bar(yk, yv, color=BLUE, width=0.62)
    for b, v in zip(bars, yv):
        ax.text(b.get_x()+b.get_width()/2, v+0.15, str(v), ha="center", va="bottom", fontsize=12)
    ax.set_title(t[0]); ax.set_xlabel(t[1]); ax.set_ylabel(t[2])
    ax.set_ylim(0, max(yv)+1.6)
    ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)
    ax.tick_params(labelsize=12)
    save(fig, f"studies_by_year_{lang}")

# ---------------- Figure: evidence profile ----------------
n = len(rows)
emp = sum(1 for r in rows if "empiric" in r["evidencia"].lower() or "empír" in r["evidencia"].lower())
repo = sum(1 for r in rows if "repositorio" in r["evidencia"].lower() or "repositório" in r["evidencia"].lower())
arx = sum(1 for r in rows if "arxiv" in r["evidencia"].lower())
case = 5; survey = 2  # curatorial classification from synthesis
def fig_evidence(lang):
    if lang == "pt":
        labels = ["Avaliacao empirica", "Repositorio publico", "Preprint arXiv", "Estudo de caso", "Survey / revisao"]
        title = f"Perfil de evidencia do corpus (n = {n})"; xlab = "Numero de estudos"
    else:
        labels = ["Empirical evaluation", "Public repository", "arXiv preprint", "Case study", "Survey / review"]
        title = f"Evidence profile of the corpus (n = {n})"; xlab = "Number of studies"
    vals = [emp, repo, arx, case, survey]
    order = np.argsort(vals)
    labels = [labels[i] for i in order]; vals = [vals[i] for i in order]
    fig, ax = plt.subplots(figsize=(7.6, 4.2))
    bars = ax.barh(labels, vals, color=GREEN)
    for b, v in zip(bars, vals):
        ax.text(v+0.3, b.get_y()+b.get_height()/2, f"{v}", va="center", fontsize=12)
    ax.set_title(title); ax.set_xlabel(xlab); ax.set_xlim(0, n)
    ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)
    ax.tick_params(labelsize=12)
    save(fig, f"evidence_profile_{lang}")

# ---------------- Figure: theme x dimension heatmap ----------------
# strong=3, medium=2, weak=1, absent=0 (from synthesis hybrid mapping)
M = np.array([
    [2,2,3,3,2,1],
    [3,2,1,2,3,1],
    [1,3,1,2,1,1],
    [2,1,1,2,3,1],
    [1,1,1,1,1,0],
    [1,1,1,2,2,0],
])
def fig_heat(lang):
    if lang == "pt":
        themes = ["T1 Orquestracao", "T2 Especificacao", "T3 Contexto", "T4 Validacao", "T5 Colab. humano-IA", "T6 Seguranca"]
        dims = ["Especif.", "Contexto", "Papeis", "Execucao", "Validacao", "Portab."]
        title = "Mapeamento tema x dimensao da taxonomia"
        legend = {3:"forte", 2:"media", 1:"fraca", 0:"ausente"}
    else:
        themes = ["T1 Orchestration", "T2 Specification", "T3 Context", "T4 Validation", "T5 Human-AI collab.", "T6 Security"]
        dims = ["Spec.", "Context", "Roles", "Exec.", "Valid.", "Portab."]
        title = "Theme x taxonomy-dimension mapping"
        legend = {3:"strong", 2:"medium", 1:"weak", 0:"absent"}
    from matplotlib.colors import ListedColormap
    cmap = ListedColormap(["#F2F2F2", "#CFE0EE", "#7FA8CC", "#2C5F8A"])
    fig, ax = plt.subplots(figsize=(8.4, 6.0))
    ax.imshow(M, cmap=cmap, vmin=0, vmax=3, aspect="auto")
    ax.set_xticks(range(len(dims))); ax.set_xticklabels(dims, fontsize=12)
    ax.set_yticks(range(len(themes))); ax.set_yticklabels(themes, fontsize=12)
    ax.set_title(title, fontsize=14)
    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            val = M[i, j]
            ax.text(j, i, legend[val], ha="center", va="center", fontsize=12,
                    color="white" if val == 3 else "#1A1A1A")
    ax.set_xticks(np.arange(-.5, len(dims), 1), minor=True)
    ax.set_yticks(np.arange(-.5, len(themes), 1), minor=True)
    ax.grid(which="minor", color="white", linewidth=2)
    ax.tick_params(which="minor", length=0)
    save(fig, f"theme_dimension_{lang}")

# ---------------- Figure: risk frequency ----------------
rc = Counter()
for r in rows:
    for tok in [t.strip().lower() for t in r["riscos"].split(",") if t.strip()]:
        rc[tok] += 1
# canonical order by frequency for the main risks
risk_keys = ["contexto", "confiabilidade", "overhead", "seguranca", "governanca", "rastreabilidade", "drift"]
labels_map = {
    "pt": {"contexto":"Contexto", "governanca":"Governanca", "confiabilidade":"Confiabilidade",
           "overhead":"Custo de coordenacao", "seguranca":"Seguranca", "drift":"Drift spec-codigo",
           "rastreabilidade":"Rastreabilidade"},
    "en": {"contexto":"Context", "governanca":"Governance", "confiabilidade":"Reliability",
           "overhead":"Coordination cost", "seguranca":"Security", "drift":"Spec-code drift",
           "rastreabilidade":"Traceability"},
}
def fig_risk(lang):
    title = ("Frequencia dos riscos no corpus (n = 37 estudos)" if lang=="pt"
             else "Risk frequency across the corpus (n = 37 studies)")
    xlab = "Numero de estudos" if lang=="pt" else "Number of studies"
    keys = sorted(risk_keys, key=lambda k: rc[k])
    labels = [labels_map[lang][k] for k in keys]
    vals = [rc[k] for k in keys]
    colors = [RED if k=="seguranca" else BLUE for k in keys]
    fig, ax = plt.subplots(figsize=(7.8, 4.6))
    bars = ax.barh(labels, vals, color=colors)
    for b, v in zip(bars, vals):
        ax.text(v+0.3, b.get_y()+b.get_height()/2, str(v), va="center", fontsize=12)
    ax.set_title(title); ax.set_xlabel(xlab); ax.set_xlim(0, 40)
    ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)
    ax.tick_params(labelsize=12)
    save(fig, f"risk_frequency_{lang}")

for lang in ("pt", "en"):
    fig_year(lang); fig_evidence(lang); fig_heat(lang); fig_risk(lang)
print("ALL DONE; risk counts:", dict(rc))
