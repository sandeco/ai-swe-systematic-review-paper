# -*- coding: utf-8 -*-
"""Methodology figure (Kitchenham funnel), bilingual pt-br + en.
Counts match tex/sections/02_metodo_revisao.tex. Rules 12 (>=12pt) and 13 (96 DPI).
Output: figures/methodology_{pt,en}.{pdf,png,svg}
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

plt.rcParams["font.size"] = 12
PAPER = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
OUT = os.path.join(PAPER, "figures"); os.makedirs(OUT, exist_ok=True)
C_MAIN="#2C5F8A"; C_MAIN_F="#E8F0F7"; C_EXCL="#9A3B3B"; C_EXCL_F="#F6EBEB"
C_FINAL="#1F6B3B"; C_FINAL_F="#E6F2EA"; C_LANE="#F4F4F4"; C_LANE_EDGE="#D8D8D8"; TXT="#1A1A1A"

T = {
 "pt": {
  "lanes": ["Identificação","Seleção","Snowballing","Extração","Síntese","Relato"],
  "b1": "Busca multibase (arXiv, ACM, IEEE,\nCrossref, OpenAlex, Semantic Scholar)\n100 registros brutos",
  "b2": "85 candidatos\n(dedup + filtro 2018-2026 + 1 semente dirigida)",
  "b3": "Triagem por título e resumo\n28 incluídos",
  "b4": "Leitura de texto completo\n25 incluídos finais",
  "b5": "Snowballing backward + forward\n3 rodadas, 149 candidatos adicionais",
  "b6": "R1: 69 novos -> 6 incluídos\nR2: 50 novos -> 3 incluídos\nR3: 30 novos -> 3 incluídos\n(forward: 0 elegíveis)",
  "b7": "12 estudos novos incorporados",
  "b8": "Busca suplementar (arXiv + Crossref)\n+4 estudos peer-reviewed na janela",
  "b9": "Síntese temática híbrida\n6 temas x taxonomia de 6 dimensões",
  "b10": "Corpus final\n41 estudos (37 do protocolo + 4 suplementares)",
  "e1": "Excluídos na triagem\ntítulo/resumo: 57",
  "e2": "Excluídos em\ntexto completo: 3",
  "note": "Busca suplementar incorporou 4 estudos peer-reviewed dentro da janela (corpus: 41).\nDuas fontes sem texto completo na data de corte ficaram como pendência operacional.\nData de corte: 26 de maio de 2026.",
  "title": "Fluxo da revisão sistemática de literatura (protocolo Kitchenham)",
 },
 "en": {
  "lanes": ["Identification","Selection","Snowballing","Extraction","Synthesis","Reporting"],
  "b1": "Multi-database search (arXiv, ACM, IEEE,\nCrossref, OpenAlex, Semantic Scholar)\n100 raw records",
  "b2": "85 candidates\n(dedup + 2018-2026 filter + 1 directed seed)",
  "b3": "Title and abstract screening\n28 included",
  "b4": "Full-text reading\n25 final included",
  "b5": "Backward + forward snowballing\n3 rounds, 149 additional candidates",
  "b6": "R1: 69 new -> 6 included\nR2: 50 new -> 3 included\nR3: 30 new -> 3 included\n(forward: 0 eligible)",
  "b7": "12 new studies incorporated",
  "b8": "Supplementary search (arXiv + Crossref)\n+4 peer-reviewed studies in window",
  "b9": "Hybrid thematic synthesis\n6 themes x 6-dimension taxonomy",
  "b10": "Final corpus\n41 studies (37 from protocol + 4 supplementary)",
  "e1": "Excluded at title/abstract\nscreening: 57",
  "e2": "Excluded at\nfull text: 3",
  "note": "Supplementary search added 4 peer-reviewed studies within the window (corpus: 41).\nTwo sources lacked full text at the cutoff date and were kept as operational pending items.\nCutoff date: May 26, 2026.",
  "title": "Systematic literature review flow (Kitchenham protocol)",
 },
}

def render(lang):
    d = T[lang]
    fig, ax = plt.subplots(figsize=(12.6, 16.2))
    ax.set_xlim(0,100); ax.set_ylim(0,132); ax.axis("off")
    fig.patch.set_facecolor("white"); ax.set_facecolor("white")
    lanes = list(zip(d["lanes"], [(118,132),(78,118),(44,78),(30,44),(16,30),(2,16)]))
    LANE_X, LANE_W = 1.5, 97
    for name,(y0,y1) in lanes:
        ax.add_patch(FancyBboxPatch((LANE_X,y0),LANE_W,y1-y0,boxstyle="round,pad=0.2,rounding_size=1.2",
                     fc=C_LANE,ec=C_LANE_EDGE,lw=1.0,zorder=0))
        ax.text(LANE_X+1.8,(y0+y1)/2,name,rotation=90,va="center",ha="center",fontsize=13,fontweight="bold",color="#555555",zorder=1)
    CX,BW,BH=40,50,8.0; EX_X,EBW,EBH=80,38,7.5
    def box(cx,cy,w,h,text,fc,ec,fs=12,bold=False,z=3):
        ax.add_patch(FancyBboxPatch((cx-w/2,cy-h/2),w,h,boxstyle="round,pad=0.3,rounding_size=1.0",fc=fc,ec=ec,lw=1.6,zorder=z))
        ax.text(cx,cy,text,va="center",ha="center",fontsize=fs,color=TXT,zorder=z+1,fontweight=("bold" if bold else "normal"))
    def arrow(x0,y0,x1,y1,color=C_MAIN,lw=1.8,z=2):
        ax.add_patch(FancyArrowPatch((x0,y0),(x1,y1),arrowstyle="-|>",mutation_scale=16,color=color,lw=lw,zorder=z,shrinkA=2,shrinkB=2))
    box(CX,125,BW,BH,d["b1"],C_MAIN_F,C_MAIN); box(CX,110,BW,BH,d["b2"],C_MAIN_F,C_MAIN)
    box(CX,96,BW,BH,d["b3"],C_MAIN_F,C_MAIN); box(CX,82,BW,BH,d["b4"],C_MAIN_F,C_MAIN)
    box(CX,71,BW,BH,d["b5"],C_MAIN_F,C_MAIN); box(CX,57,BW,10.5,d["b6"],C_MAIN_F,C_MAIN)
    box(CX,46,BW,BH,d["b7"],C_MAIN_F,C_MAIN); box(CX,37,BW,BH,d["b8"],C_MAIN_F,C_MAIN)
    box(CX,23,BW,BH,d["b9"],C_MAIN_F,C_MAIN); box(CX,9,BW,9.0,d["b10"],C_FINAL_F,C_FINAL,fs=13,bold=True)
    for yb,yt in [(125-BH/2,110+BH/2),(110-BH/2,96+BH/2),(96-BH/2,82+BH/2),(82-BH/2,71+BH/2),
                  (71-BH/2,57+10.5/2),(57-10.5/2,46+BH/2),(46-BH/2,37+BH/2),(37-BH/2,23+BH/2),(23-BH/2,9+9.0/2)]:
        arrow(CX,yb,CX,yt)
    def excl(cy,text):
        box(EX_X,cy,EBW,EBH,text,C_EXCL_F,C_EXCL,fs=12); arrow(CX+BW/2,cy+0.2,EX_X-EBW/2,cy,color=C_EXCL,lw=1.4)
    excl(103,d["e1"]); excl(89,d["e2"])
    ax.text(CX,2.6,d["note"],va="center",ha="center",fontsize=12,color="#666666",style="italic",zorder=5)
    ax.text(50,130.8,d["title"],va="center",ha="center",fontsize=14,fontweight="bold",color=TXT)
    plt.subplots_adjust(left=0.01,right=0.99,top=0.99,bottom=0.01)
    for ext in ("pdf","png","svg"):
        fig.savefig(os.path.join(OUT,f"methodology_{lang}.{ext}"),dpi=96,facecolor="white",bbox_inches="tight")
    plt.close(fig); print("wrote methodology_"+lang)

for lang in ("pt","en"): render(lang)
print("done")
