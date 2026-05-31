import csv
import difflib
import json
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import defaultdict
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SEARCH_RESULTS = ROOT / "search-results.json"
FULL_TEXT_LOG = ROOT / "screening" / "full-text.log.csv"
SNOWBALLING = ROOT / "snowballing"
USER_AGENT = "SCIENTEX systematic review snowballing (mailto:sanderson.macedo@ifg.edu.br)"
NOW_LOCAL = datetime.now().strftime("%Y-%m-%d %H:%M")
NOW_ISO = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
MAX_FORWARD_PER_SEED = 100
REQUEST_DELAY = 0.12


def http_json(url, timeout=35, retries=2):
    last_error = None
    for attempt in range(retries + 1):
        try:
            req = urllib.request.Request(
                url,
                headers={
                    "User-Agent": USER_AGENT,
                    "Accept": "application/json",
                },
            )
            with urllib.request.urlopen(req, timeout=timeout) as response:
                data = response.read()
            time.sleep(REQUEST_DELAY)
            return json.loads(data.decode("utf-8"))
        except Exception as exc:
            last_error = exc
            if isinstance(exc, urllib.error.HTTPError) and exc.code in {404, 410}:
                break
            time.sleep(0.8 * (attempt + 1))
    raise last_error


def normalize_doi(doi):
    if not doi:
        return ""
    doi = str(doi).strip()
    doi = re.sub(r"^https?://(dx\.)?doi\.org/", "", doi, flags=re.I)
    doi = re.sub(r"^doi:\s*", "", doi, flags=re.I)
    return doi.lower().rstrip(".")


def normalize_title(title):
    if not title:
        return ""
    title = re.sub(r"\s+", " ", str(title).lower()).strip()
    title = re.sub(r"[^a-z0-9 ]+", "", title)
    return title


def title_match(title, known_titles):
    candidate = normalize_title(title)
    if not candidate:
        return False
    for known in known_titles:
        if difflib.SequenceMatcher(None, candidate, known).ratio() >= 0.92:
            return True
    return False


def slugify_author(author):
    cleaned = re.sub(r"[^A-Za-z]+", "", author or "")
    return cleaned or "Anon"


def make_key(title, authors, year, existing):
    author = "Anon"
    if authors:
        first = authors[0]
        if isinstance(first, dict):
            author = first.get("family") or first.get("name") or first.get("display_name") or "Anon"
        else:
            author = str(first).split(",")[0]
    base = f"{slugify_author(author)}{year or 'ND'}"
    key = base
    suffix = 2
    while key in existing:
        key = f"{base}_{suffix}"
        suffix += 1
    existing.add(key)
    return key


def authors_from_openalex(work):
    authors = []
    for authorship in work.get("authorships") or []:
        author = authorship.get("author") or {}
        name = author.get("display_name")
        if name:
            authors.append(name)
    return authors


def abstract_from_openalex(work):
    inv = work.get("abstract_inverted_index")
    if not inv:
        return None
    positions = []
    for word, indexes in inv.items():
        for index in indexes:
            positions.append((index, word))
    return " ".join(word for _, word in sorted(positions))


def candidate_from_openalex(work, direction, source_key, source_doi):
    primary = work.get("primary_location") or {}
    source = primary.get("source") or {}
    doi = normalize_doi(work.get("doi"))
    return {
        "doi": doi or None,
        "title": work.get("title"),
        "authors": authors_from_openalex(work),
        "year": work.get("publication_year"),
        "venue": source.get("display_name"),
        "abstract": abstract_from_openalex(work),
        "citations": work.get("cited_by_count"),
        "open_access_pdf_url": ((work.get("open_access") or {}).get("oa_url")),
        "doi_url": f"https://doi.org/{doi}" if doi else None,
        "source": "openalex",
        "source_id": work.get("id"),
        "source_papers": [source_doi],
        "source_citation_keys": [source_key],
        "snowballing_direction": direction,
    }


def candidate_from_crossref(item, direction, source_key, source_doi):
    doi = normalize_doi(item.get("DOI"))
    authors = []
    for author in item.get("author") or []:
        given = author.get("given", "")
        family = author.get("family", "")
        name = " ".join(part for part in [given, family] if part).strip()
        if name:
            authors.append(name)
    year = None
    date_parts = (((item.get("published-print") or item.get("published-online") or item.get("issued") or {}).get("date-parts")) or [])
    if date_parts and date_parts[0]:
        year = date_parts[0][0]
    container = item.get("container-title") or []
    title = item.get("title") or []
    return {
        "doi": doi or None,
        "title": title[0] if title else None,
        "authors": authors,
        "year": year,
        "venue": container[0] if container else None,
        "abstract": item.get("abstract"),
        "citations": item.get("is-referenced-by-count"),
        "open_access_pdf_url": None,
        "doi_url": f"https://doi.org/{doi}" if doi else None,
        "source": "crossref",
        "source_papers": [source_doi],
        "source_citation_keys": [source_key],
        "snowballing_direction": direction,
    }


def candidate_from_s2(paper, direction, source_key, source_doi):
    doi = None
    for external_id_key, external_id_value in (paper.get("externalIds") or {}).items():
        if external_id_key.lower() == "doi":
            doi = normalize_doi(external_id_value)
    return {
        "doi": doi or None,
        "title": paper.get("title"),
        "authors": [a.get("name") for a in (paper.get("authors") or []) if a.get("name")],
        "year": paper.get("year"),
        "venue": paper.get("venue"),
        "abstract": paper.get("abstract"),
        "citations": paper.get("citationCount"),
        "open_access_pdf_url": ((paper.get("openAccessPdf") or {}).get("url")),
        "doi_url": f"https://doi.org/{doi}" if doi else None,
        "source": "semanticscholar",
        "source_papers": [source_doi],
        "source_citation_keys": [source_key],
        "snowballing_direction": direction,
    }


def openalex_work_by_doi(doi):
    encoded = urllib.parse.quote(normalize_doi(doi), safe="")
    return http_json(f"https://api.openalex.org/works/doi:{encoded}?mailto=sanderson.macedo@ifg.edu.br")


def hydrate_openalex_id(openalex_id):
    fields = "id,doi,title,publication_year,primary_location,authorships,abstract_inverted_index,cited_by_count,open_access"
    work_id = str(openalex_id).rstrip("/").split("/")[-1]
    return http_json(f"https://api.openalex.org/works/{work_id}?select={fields}&mailto=sanderson.macedo@ifg.edu.br")


def crossref_work_by_doi(doi):
    encoded = urllib.parse.quote(normalize_doi(doi), safe="")
    return http_json(f"https://api.crossref.org/works/{encoded}")["message"]


def s2_references(doi):
    encoded = urllib.parse.quote(f"DOI:{normalize_doi(doi)}", safe="")
    fields = "title,year,venue,abstract,authors,externalIds,citationCount,openAccessPdf"
    url = f"https://api.semanticscholar.org/graph/v1/paper/{encoded}/references?limit=100&fields={fields}"
    return http_json(url).get("data") or []


def s2_citations(doi):
    encoded = urllib.parse.quote(f"DOI:{normalize_doi(doi)}", safe="")
    fields = "title,year,venue,abstract,authors,externalIds,citationCount,openAccessPdf"
    url = f"https://api.semanticscholar.org/graph/v1/paper/{encoded}/citations?limit=100&fields={fields}"
    return http_json(url).get("data") or []


def extract_backward(seed):
    source_key = seed["citation_key"]
    source_doi = seed["doi"]
    raw = {"source": source_key, "source_doi": source_doi, "provider": None, "items": []}
    errors = []
    candidates = []
    try:
        work = openalex_work_by_doi(source_doi)
        raw["provider"] = "openalex"
        refs = work.get("referenced_works") or []
        for ref_id in refs:
            try:
                ref_work = hydrate_openalex_id(ref_id)
                raw["items"].append(ref_work)
                cand = candidate_from_openalex(ref_work, "backward", source_key, source_doi)
                if cand.get("title"):
                    candidates.append(cand)
            except Exception as exc:
                errors.append(f"openalex hydrate {ref_id}: {exc}")
        return candidates, raw, errors
    except Exception as exc:
        errors.append(f"openalex references failed: {exc}")
    try:
        item = crossref_work_by_doi(source_doi)
        raw["provider"] = "crossref"
        references = item.get("reference") or []
        raw["items"] = references
        for ref in references:
            ref_doi = normalize_doi(ref.get("DOI") or ref.get("doi"))
            if not ref_doi:
                continue
            try:
                ref_item = crossref_work_by_doi(ref_doi)
                cand = candidate_from_crossref(ref_item, "backward", source_key, source_doi)
                if cand.get("title"):
                    candidates.append(cand)
            except Exception as exc:
                errors.append(f"crossref hydrate {ref_doi}: {exc}")
        return candidates, raw, errors
    except Exception as exc:
        errors.append(f"crossref references failed: {exc}")
    try:
        refs = s2_references(source_doi)
        raw["provider"] = "semanticscholar"
        raw["items"] = refs
        for ref in refs:
            paper = ref.get("citedPaper") or {}
            cand = candidate_from_s2(paper, "backward", source_key, source_doi)
            if cand.get("title"):
                candidates.append(cand)
        return candidates, raw, errors
    except Exception as exc:
        errors.append(f"semanticscholar references failed: {exc}")
    return candidates, raw, errors


def extract_forward(seed):
    source_key = seed["citation_key"]
    source_doi = seed["doi"]
    raw = {"source": source_key, "source_doi": source_doi, "provider": None, "items": []}
    errors = []
    candidates = []
    try:
        work = openalex_work_by_doi(source_doi)
        cited_by_url = work.get("cited_by_api_url")
        if not cited_by_url:
            raw["provider"] = "openalex"
            return candidates, raw, errors
        url = f"{cited_by_url}&per-page=100&mailto=sanderson.macedo@ifg.edu.br"
        data = http_json(url)
        raw["provider"] = "openalex"
        raw["items"] = data.get("results") or []
        for cited in raw["items"][:MAX_FORWARD_PER_SEED]:
            cand = candidate_from_openalex(cited, "forward", source_key, source_doi)
            if cand.get("title"):
                candidates.append(cand)
        return candidates, raw, errors
    except Exception as exc:
        errors.append(f"openalex citations failed: {exc}")
    try:
        cites = s2_citations(source_doi)
        raw["provider"] = "semanticscholar"
        raw["items"] = cites
        for cite in cites:
            paper = cite.get("citingPaper") or {}
            cand = candidate_from_s2(paper, "forward", source_key, source_doi)
            if cand.get("title"):
                candidates.append(cand)
        return candidates, raw, errors
    except Exception as exc:
        errors.append(f"semanticscholar citations failed: {exc}")
    return candidates, raw, errors


def merge_candidate(bucket, cand):
    doi = normalize_doi(cand.get("doi"))
    title_key = normalize_title(cand.get("title"))
    key = doi or f"title:{title_key}:{cand.get('year') or ''}"
    if key not in bucket:
        bucket[key] = cand
        bucket[key]["source_papers"] = list(dict.fromkeys(cand.get("source_papers") or []))
        bucket[key]["source_citation_keys"] = list(dict.fromkeys(cand.get("source_citation_keys") or []))
        return
    existing = bucket[key]
    existing["source_papers"] = list(dict.fromkeys((existing.get("source_papers") or []) + (cand.get("source_papers") or [])))
    existing["source_citation_keys"] = list(dict.fromkeys((existing.get("source_citation_keys") or []) + (cand.get("source_citation_keys") or [])))
    if existing.get("snowballing_direction") != cand.get("snowballing_direction"):
        existing["snowballing_direction"] = "both"
    for field in ["abstract", "venue", "doi", "open_access_pdf_url"]:
        if not existing.get(field) and cand.get(field):
            existing[field] = cand[field]


def in_protocol_scope(cand):
    year = cand.get("year")
    try:
        year = int(year)
    except Exception:
        return False, "missing year"
    if year < 2018 or year > 2026:
        return False, "outside 2018-2026"
    title = normalize_title(cand.get("title"))
    abstract = normalize_title(cand.get("abstract") or "")
    text = f"{title} {abstract}"
    focus_terms = [
        "software engineering",
        "software development",
        "coding assistant",
        "code assistant",
        "agentic",
        "software agent",
        "requirements engineering",
        "software testing",
        "code generation",
        "program repair",
        "developer",
        "devops",
        "ide",
        "spec driven",
        "llm",
        "large language model",
    ]
    structure_terms = [
        "framework",
        "workflow",
        "method",
        "methodology",
        "architecture",
        "toolchain",
        "platform",
        "system",
        "agent",
        "agents",
        "process",
        "orchestration",
        "specification",
        "artifact",
        "governance",
        "validation",
        "testing",
    ]
    if not any(term in text for term in focus_terms):
        return False, "missing software engineering focus"
    if not any(term in text for term in structure_terms):
        return False, "missing framework or workflow signal"
    return True, "candidate needs screening"


def main():
    with SEARCH_RESULTS.open("r", encoding="utf-8") as f:
        entries = json.load(f)

    by_key = {entry.get("citation_key"): entry for entry in entries}
    known_dois = {normalize_doi(entry.get("doi")) for entry in entries if normalize_doi(entry.get("doi"))}
    known_titles = {normalize_title(entry.get("title")) for entry in entries if normalize_title(entry.get("title"))}
    existing_keys = {entry.get("citation_key") for entry in entries if entry.get("citation_key")}

    included = []
    with FULL_TEXT_LOG.open("r", encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f):
            if row.get("decision") == "include":
                entry = by_key.get(row.get("citation_key"), {})
                doi = normalize_doi(entry.get("doi"))
                included.append({
                    "citation_key": row.get("citation_key"),
                    "title": row.get("title") or entry.get("title"),
                    "doi": doi,
                })

    SNOWBALLING.mkdir(exist_ok=True)
    existing_rounds = []
    for child in SNOWBALLING.glob("round-*"):
        if child.is_dir():
            match = re.search(r"round-(\d+)$", child.name)
            if match:
                existing_rounds.append(int(match.group(1)))
    round_num = max(existing_rounds, default=0) + 1
    if existing_rounds:
        latest = SNOWBALLING / f"round-{max(existing_rounds)}"
        failures_log = latest / "failures.log"
        new_candidates = latest / "new-candidates.json"
        try:
            failed_with_no_candidates = (
                failures_log.exists()
                and failures_log.read_text(encoding="utf-8").strip()
                and new_candidates.exists()
                and len(json.loads(new_candidates.read_text(encoding="utf-8"))) == 0
            )
        except Exception:
            failed_with_no_candidates = False
        if failed_with_no_candidates:
            round_num = max(existing_rounds)
    if round_num > 3:
        raise SystemExit("Maximum snowballing rounds already reached")

    if round_num > 1:
        previous_discovery = f"snowballing-{round_num - 1}"
        included = [
            item for item in included
            if (by_key.get(item["citation_key"], {}).get("systematic_review") or {}).get("discovery") == previous_discovery
            and (by_key.get(item["citation_key"], {}).get("screening_pass2") or {}).get("decision") == "include"
        ]

    round_dir = SNOWBALLING / f"round-{round_num}"
    backward_dir = round_dir / "backward"
    forward_dir = round_dir / "forward"
    backward_dir.mkdir(parents=True, exist_ok=True)
    forward_dir.mkdir(parents=True, exist_ok=True)

    no_doi = []
    seeds = []
    for item in included:
        if item["doi"]:
            seeds.append(item)
        else:
            no_doi.append(item)
    with (SNOWBALLING / "no-doi.log").open("a", encoding="utf-8") as f:
        for item in no_doi:
            f.write(f"{NOW_ISO},{item['citation_key']},{item['title']}\n")

    failures = []
    backward_bucket = {}
    forward_bucket = {}
    per_seed = defaultdict(lambda: {"backward_raw": 0, "forward_raw": 0, "backward_new": 0, "forward_new": 0})

    for seed in seeds:
        backward_candidates, backward_raw, backward_errors = extract_backward(seed)
        (backward_dir / f"{seed['citation_key']}.json").write_text(
            json.dumps(backward_raw, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        per_seed[seed["citation_key"]]["backward_raw"] = len(backward_candidates)
        for err in backward_errors:
            failures.append(f"{seed['citation_key']},backward,{err}")
        for cand in backward_candidates:
            merge_candidate(backward_bucket, cand)

        forward_candidates, forward_raw, forward_errors = extract_forward(seed)
        (forward_dir / f"{seed['citation_key']}.json").write_text(
            json.dumps(forward_raw, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        per_seed[seed["citation_key"]]["forward_raw"] = len(forward_candidates)
        for err in forward_errors:
            failures.append(f"{seed['citation_key']},forward,{err}")
        for cand in forward_candidates:
            merge_candidate(forward_bucket, cand)

    all_candidates = []
    rejected_scope = []
    for direction, bucket in [("backward", backward_bucket), ("forward", forward_bucket)]:
        for cand in bucket.values():
            cand["snowballing_direction"] = cand.get("snowballing_direction") or direction
            doi = normalize_doi(cand.get("doi"))
            if doi and doi in known_dois:
                continue
            if not doi and title_match(cand.get("title"), known_titles):
                continue
            keep, reason = in_protocol_scope(cand)
            if not keep:
                cand["rejected_pre_screening_reason"] = reason
                rejected_scope.append(cand)
                continue
            all_candidates.append(cand)

    deduped = {}
    for cand in all_candidates:
        merge_candidate(deduped, cand)

    added = []
    for cand in deduped.values():
        key = make_key(cand.get("title"), cand.get("authors") or [], cand.get("year"), existing_keys)
        cand["citation_key"] = key
        cand["systematic_review"] = {
            "retrieved_at": NOW_LOCAL,
            "stage": "identification",
            "discovery": f"snowballing-{round_num}",
            "query_family": "snowballing",
            "year_in_protocol_range": True,
        }
        cand["screening_pass1"] = {
            "decision": "pending",
            "criterion": "",
            "reason": "Novo candidato identificado por snowballing; requer triagem por titulo e abstract.",
            "reviewer": "snowballing-hunter",
            "timestamp": NOW_ISO,
        }
        cand["added_at"] = NOW_ISO
        entries.append(cand)
        added.append(cand)
        doi = normalize_doi(cand.get("doi"))
        if doi:
            known_dois.add(doi)
        if cand.get("title"):
            known_titles.add(normalize_title(cand.get("title")))
        for source_key in cand.get("source_citation_keys") or []:
            if cand.get("snowballing_direction") in {"backward", "both"}:
                per_seed[source_key]["backward_new"] += 1
            if cand.get("snowballing_direction") in {"forward", "both"}:
                per_seed[source_key]["forward_new"] += 1

    (round_dir / "backward.json").write_text(
        json.dumps(list(backward_bucket.values()), ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    (round_dir / "forward.json").write_text(
        json.dumps(list(forward_bucket.values()), ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    (round_dir / "new-candidates.json").write_text(
        json.dumps(added, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    (round_dir / "rejected-pre-screening.json").write_text(
        json.dumps(rejected_scope, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    (round_dir / "failures.log").write_text("\n".join(failures) + ("\n" if failures else ""), encoding="utf-8")
    SEARCH_RESULTS.write_text(json.dumps(entries, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    backward_raw_total = sum(row["backward_raw"] for row in per_seed.values())
    forward_raw_total = sum(row["forward_raw"] for row in per_seed.values())
    backward_added = sum(1 for cand in added if cand.get("snowballing_direction") in {"backward", "both"})
    forward_added = sum(1 for cand in added if cand.get("snowballing_direction") in {"forward", "both"})

    lines = [
        f"# Snowballing Round {round_num}",
        "",
        f"> Executado em: {NOW_LOCAL}",
        f"> Papers-fonte: {len(seeds)} incluidos com DOI",
        "> Direcao: both",
        "",
        "## Resultados",
        "",
        f"- Backward: {backward_raw_total} referencias brutas, {len(backward_bucket)} unicas antes dos filtros, {backward_added} novas apos dedup e pre-filtro.",
        f"- Forward: {forward_raw_total} citacoes brutas, {len(forward_bucket)} unicas antes dos filtros, {forward_added} novas apos dedup e pre-filtro.",
        f"- Total novos candidatos adicionados a `search-results.json`: {len(added)}",
        f"- Rejeitados em pre-filtro operacional antes do screening: {len(rejected_scope)}",
        f"- Falhas registradas em APIs: {len(failures)}",
        "",
        "## Por paper-fonte",
        "",
        "| Citation key | Backward brutos | Backward novos | Forward brutos | Forward novos | Total novos |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for seed in seeds:
        stats = per_seed[seed["citation_key"]]
        total_new = stats["backward_new"] + stats["forward_new"]
        lines.append(
            f"| {seed['citation_key']} | {stats['backward_raw']} | {stats['backward_new']} | "
            f"{stats['forward_raw']} | {stats['forward_new']} | {total_new} |"
        )
    lines.extend([
        "",
        "## Proximo passo",
        "",
        (
            f"Como a rodada adicionou candidatos novos, o coordenador deve rodar `screening-logger` sobre os registros com "
            f"`systematic_review.discovery = snowballing-{round_num}` antes de decidir nova rodada."
            if added
            else "Como a rodada nao adicionou candidatos novos, o coordenador pode considerar o snowballing saturado e seguir para a Etapa 7."
        ),
    ])
    (round_dir / "summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(json.dumps({
        "round": round_num,
        "seeds_with_doi": len(seeds),
        "seeds_without_doi": len(no_doi),
        "backward_raw": backward_raw_total,
        "forward_raw": forward_raw_total,
        "backward_unique": len(backward_bucket),
        "forward_unique": len(forward_bucket),
        "added": len(added),
        "rejected_pre_screening": len(rejected_scope),
        "failures": len(failures),
        "summary": str(round_dir / "summary.md"),
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
