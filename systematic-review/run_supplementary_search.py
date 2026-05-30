#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Busca suplementar (IMP-7 do score.md): roda uma rodada adicional de busca em rotas
de acesso que a busca original consultou de forma parcial (arXiv API direta e Crossref),
com os mesmos descritores do protocolo, e DEDUPLICA contra tudo que ja foi visto
(search-results.json + extraction-matrix.csv + logs de screening). O objetivo e auditar
a COMPLETUDE do corpus: quantos candidatos novos, de fato fora do que ja foi triado,
ainda apareceriam. Nao fabrica estudo: so reporta o que as APIs retornam.

Saidas:
  snowballing/supplementary/raw-arxiv.json, raw-crossref.json
  snowballing/supplementary/new-candidates.json   (apos dedup)
  snowballing/supplementary/summary.md
"""
import json, os, re, time, urllib.request, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "snowballing", "supplementary")
os.makedirs(OUT, exist_ok=True)

QUERY_TERMS = [
    "AI-assisted software development framework",
    "agentic software engineering framework",
    "spec-driven development LLM",
    "multi-agent software development lifecycle",
    "LLM agent software engineering process",
]
YEAR_MIN = 2018

def norm_title(t):
    return re.sub(r"[^a-z0-9]", "", (t or "").lower())

def load_seen():
    seen_doi, seen_title = set(), set()
    sr = json.load(open(os.path.join(HERE, "search-results.json")))
    for r in sr:
        if r.get("doi"): seen_doi.add(r["doi"].lower())
        if r.get("title"): seen_title.add(norm_title(r["title"]))
    import csv
    with open(os.path.join(HERE, "extracted", "extraction-matrix.csv")) as f:
        for r in csv.DictReader(f):
            if r.get("doi"): seen_doi.add(r["doi"].lower())
            if r.get("title"): seen_title.add(norm_title(r["title"]))
    for fn in ("title-abstract.log.csv", "full-text.log.csv"):
        p = os.path.join(HERE, "screening", fn)
        if os.path.exists(p):
            with open(p) as f:
                for r in csv.DictReader(f):
                    if r.get("title"): seen_title.add(norm_title(r["title"]))
    return seen_doi, seen_title

def fetch_arxiv(term, maxr=30):
    q = urllib.parse.quote(f'all:{term}')
    url = f"http://export.arxiv.org/api/query?search_query={q}&start=0&max_results={maxr}&sortBy=submittedDate&sortOrder=descending"
    try:
        raw = urllib.request.urlopen(url, timeout=20).read().decode("utf-8", "replace")
    except Exception as e:
        print("  arxiv fail", term, e); return []
    out = []
    for entry in re.findall(r"<entry>(.*?)</entry>", raw, re.S):
        title = re.search(r"<title>(.*?)</title>", entry, re.S)
        ttl = re.sub(r"\s+", " ", title.group(1)).strip() if title else ""
        doi = re.search(r"<arxiv:doi[^>]*>(.*?)</arxiv:doi>", entry)
        idm = re.search(r"<id>(.*?)</id>", entry)
        year = re.search(r"<published>(\d{4})", entry)
        out.append({"title": ttl, "doi": (doi.group(1) if doi else ""),
                    "url": idm.group(1) if idm else "", "year": int(year.group(1)) if year else None,
                    "source": "arxiv-supplementary"})
    return out

def fetch_crossref(term, maxr=40):
    q = urllib.parse.quote(term)
    url = f"https://api.crossref.org/works?query={q}&rows={maxr}&filter=from-pub-date:2018-01-01"
    try:
        data = json.load(urllib.request.urlopen(url, timeout=25))
    except Exception as e:
        print("  crossref fail", term, e); return []
    out = []
    for it in data.get("message", {}).get("items", []):
        ttl = (it.get("title") or [""])[0]
        yr = None
        for k in ("published-print", "published-online", "issued"):
            if it.get(k, {}).get("date-parts"): yr = it[k]["date-parts"][0][0]; break
        out.append({"title": ttl, "doi": (it.get("DOI") or "").lower(),
                    "url": it.get("URL", ""), "year": yr,
                    "venue": (it.get("container-title") or [""])[0], "source": "crossref-supplementary"})
    return out

def main():
    seen_doi, seen_title = load_seen()
    print(f"seen: {len(seen_doi)} DOIs, {len(seen_title)} titulos")
    arxiv, crossref = [], []
    for t in QUERY_TERMS:
        print("arxiv:", t); arxiv += fetch_arxiv(t); time.sleep(3)
        print("crossref:", t); crossref += fetch_crossref(t); time.sleep(1)
    json.dump(arxiv, open(os.path.join(OUT, "raw-arxiv.json"), "w"), indent=1)
    json.dump(crossref, open(os.path.join(OUT, "raw-crossref.json"), "w"), indent=1)

    allc = arxiv + crossref
    new, dup_doi, dup_title, seen_local = [], 0, 0, set()
    for r in allc:
        nt = norm_title(r["title"])
        if not nt or len(nt) < 10: continue
        if r.get("year") and r["year"] < YEAR_MIN: continue
        if r.get("doi") and r["doi"] in seen_doi: dup_doi += 1; continue
        if nt in seen_title: dup_title += 1; continue
        if nt in seen_local: continue
        seen_local.add(nt); new.append(r)
    json.dump(new, open(os.path.join(OUT, "new-candidates.json"), "w"), indent=1)

    lines = ["# Busca suplementar (IMP-7) - auditoria de completude\n",
             f"> Bases: arXiv API direta + Crossref. Descritores do protocolo. Janela {YEAR_MIN}-2026.",
             f"> Brutos: {len(arxiv)} arXiv + {len(crossref)} Crossref = {len(allc)}.",
             f"> Duplicatas ja vistas: {dup_doi} por DOI, {dup_title} por titulo.",
             f"> Candidatos novos apos dedup: {len(new)}.\n",
             "## Candidatos novos (para triagem manual contra I/E)\n"]
    for r in new[:60]:
        lines.append(f"- [{r.get('year')}] {r['title']}  (doi: {r.get('doi') or 'n/a'}, {r['source']})")
    open(os.path.join(OUT, "summary.md"), "w").write("\n".join(lines))
    print(f"\nBrutos {len(allc)}; dup DOI {dup_doi}; dup titulo {dup_title}; NOVOS {len(new)}")

if __name__ == "__main__":
    main()
