# Log da Busca Multi-base

> Paper: `ai-dev-frameworks-review`
> Etapa: 3, Busca multi-base + dedup
> Data: 2026-05-27 11:34
> Descritores: `systematic-review/descriptors.md`
> Saida canonica: `systematic-review/search-results.json`

## Consultas executadas

### Rodada principal

- **Query**: `agentic software engineering framework workflow specification validation AI agents software development`
- **Limite por fonte**: 40
- **Fontes solicitadas**: Crossref, OpenAlex, Semantic Scholar, arXiv, PubMed
- **Resultado bruto**: 80 registros unicos em `search-results.raw.json`
- **Observacoes**: Crossref e OpenAlex retornaram resultados. Semantic Scholar retornou HTTP 429. arXiv expirou por timeout. PubMed nao acrescentou registros relevantes nessa rodada.

### Rodada complementar

- **Query**: `agentic software engineering AI coding assistants spec-driven development`
- **Limite por fonte**: 20
- **Fontes solicitadas**: Semantic Scholar, arXiv
- **Resultado bruto**: 20 registros unicos em `search-results.s2-arxiv.json`
- **Observacoes**: Semantic Scholar retornou resultados. arXiv retornou HTTP 429.

## Consolidacao

- **Registros brutos antes de merge**: 100
- **Registros apos merge inicial por DOI/titulo**: 99
- **Registros apos filtro temporal 2018 a 2026**: 85
- **Registros apos deduplicacao adicional por titulo**: 84
- **Registros finais com DOI**: 80
- **Registros finais sem DOI**: 4

## Distribuicao por fonte principal

| Fonte | N |
|---|---:|
| Crossref | 33 |
| OpenAlex | 32 |
| Semantic Scholar | 19 |

## Limitacoes registradas

- A busca direta no arXiv nao retornou resultados por timeout ou HTTP 429. Alguns preprints arXiv ainda entraram via Semantic Scholar ou DOI `10.48550/arXiv.*`.
- A cobertura de IEEE, ACM, Scopus e Web of Science nesta rodada depende de metadados via Crossref, OpenAlex e Semantic Scholar, nao de acesso direto as bases pagas.
- O screening da Etapa 4 deve aplicar criterios I1 a I8 e E1 a E8 para remover falsos positivos, especialmente trabalhos sobre agentes ou IA fora do escopo de desenvolvimento de software.
- Metadados brutos foram preservados nos arquivos `.raw.json` e `.s2-arxiv.json`; o arquivo canonico remove payloads `raw` para evitar problemas de parser e manter somente campos normalizados.

## Seed dirigido posterior

- **Data**: 2026-05-27 15:08
- **Citation key**: Macedo2026
- **Titulo**: Reversa: A Reverse Documentation Engineering Framework for Converting Legacy Software into Operational Specifications for AI Agents
- **DOI**: https://doi.org/10.48550/arXiv.2605.18684
- **Motivo**: framework do escopo inicial e seed conhecido em `descriptors.md`; nao apareceu na busca automatica, entao foi adicionado para preservar cobertura do corpus.
- **Aquisicao**: PDF baixado diretamente de https://arxiv.org/pdf/2605.18684.pdf
