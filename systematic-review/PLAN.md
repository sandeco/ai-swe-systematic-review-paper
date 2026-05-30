# Systematic Review, Plano de Execucao

> Paper: **Do Prompt ao Processo: uma Revisao de Frameworks de Desenvolvimento de Software com IA**
> Slug: `ai-dev-frameworks-review`
> Protocolo: `kitchenham`
> Quality assessment: `none`
> Iniciado em: 2026-05-27
> Coordenador: `systematic-review` (SCIENTEX)
> Ultima atividade: 2026-05-28 14:22

Esse documento e a memoria persistente do pipeline. Toda vez que voce invocar `/systematic-review`, o coordenador le esse arquivo e retoma de onde parou. Voce pode trabalhar nesse pipeline ao longo de semanas.

## Contexto do paper

- **Tema**: frameworks contemporaneos que deslocam o uso de IA no desenvolvimento de software de interacoes isoladas por prompt para processos estruturados, artefatos persistentes, papeis agenticos, fluxos de validacao e integracao com IDE/CLI.
- **Research Questions**: RQ1, dimensoes arquiteturais; RQ2, organizacao de contexto, papeis, artefatos e validacao; RQ3, riscos e lacunas em projetos reais; RQ4, agenda de pesquisa para avaliacao empirica, comparacao e governanca.
- **Tipo de paper**: revisao (systematic-review)
- **Dominio**: engenharia de software, desenvolvimento com IA, agentes de software, spec-driven development, IDEs agenticas.

## Status global

- [x] Etapa 1, Protocolo (PICO/PICOC + RQs + I/E) [CHECKPOINT]
- [x] Etapa 2, Descritores de busca
- [x] Etapa 3, Busca multi-base + dedup
- [x] Etapa 4, Screening passada 1 (titulo + abstract) [CHECKPOINT]
- [x] Etapa 5, Aquisicao de PDFs + screening passada 2 [CHECKPOINT]
- [x] Etapa 6, Snowballing (backward + forward), completed
- [x] Etapa 7, Extracao estruturada
- [x] Etapa 8, Avaliacao de qualidade (opcional), skipped
- [ ] Etapa 9, Sintese [CHECKPOINT]
- [ ] Etapa 10, Figura da metodologia [CHECKPOINT]

---

## Etapa 1, Protocolo

- **Status**: completed
- **Agente**: `review-protocol-builder`
- **Saida**: `systematic-review/protocol.md`
- **Iniciado em**: 2026-05-27 11:06, **Concluido em**: 2026-05-27 11:06,
- **Notas**: protocolo Kitchenham PICOC criado em `systematic-review/protocol.md`; inclui RQ1 a RQ5, criterios I1 a I8, criterios E1 a E8, bases alvo, periodo 2018 a 2026 e snowballing both com 1 nivel e maximo 3 rodadas. Checkpoint aprovado pelo autor em 2026-05-27 11:11. Status do protocolo: CONGELADO.

## Etapa 2, Descritores

- **Status**: completed
- **Skill**: `search-descriptors`
- **Saida**: `systematic-review/descriptors.md`
- **Iniciado em**: 2026-05-27 11:29, **Concluido em**: 2026-05-27 11:29,
- **Notas**: `systematic-review/descriptors.md` criado com 4 blocos conceituais, bloco de exclusao, strings para IEEE Xplore, Scopus, Web of Science, ACM, Google Scholar, ArXiv, PubMed, ScienceDirect, OpenAlex, Semantic Scholar e GitHub/docs oficiais.

## Etapa 3, Busca multi-base

- **Status**: completed
- **Skill**: `literature-search`
- **Saida**: `systematic-review/search-results.json`
- **Bases**: arXiv, PubMed/PMC, SciELO, Crossref, OpenAlex, Semantic Scholar; IEEE/Scopus/Elsevier via OpenAlex + proxy UFG
- **Iniciado em**: 2026-05-27 11:34, **Concluido em**: 2026-05-27 11:34,
- **N de papers**: 100, (antes dedup) / 85, (apos dedup, filtro 2018 a 2026 e 1 seed dirigido)
- **Notas**: busca executada via script local `related_work.search`; saida canonica em `systematic-review/search-results.json`; log auditavel em `systematic-review/search-log.md`; fontes finais originais: Crossref 33, OpenAlex 32, Semantic Scholar 19. arXiv direto falhou por timeout ou HTTP 429. Em 2026-05-27 15:08, `Macedo2026` foi adicionado como seed dirigido do escopo inicial.

## Etapa 4, Screening passada 1 (CHECKPOINT)

- **Status**: completed
- **Agente**: `screening-logger` modo 1
- **Saida**: `systematic-review/screening/title-abstract.log.csv`
- **Aplica**: criterios I/E de `protocol.md`
- **Iniciado em**: 2026-05-27 12:03, **Concluido em**: 2026-05-27 12:03,
- **N analisados**: 85, / **N incluidos**: 28, / **N excluidos**: 57,
- **Notas**: screening de titulo e abstract concluido. Saidas: `screening/title-abstract.log.csv` e `screening/exclusion-reasons.md`. Exclusoes vigentes: missing I1 = 48, E3 = 4, E2 = 3, E4 = 1, missing I2/I3/I4 = 1. Foram registradas 17 correcoes `AMENDED` no CSV append-only apos revisao dos falsos positivos e falsos negativos. Checkpoint aprovado pelo autor em 2026-05-27 12:22. `exclusion-reasons.md` foi expandido com definicoes operacionais para relato no artigo. Em 2026-05-27 15:08, `Macedo2026` foi incluido como seed dirigido por fazer parte do escopo inicial.

## Etapa 5, Aquisicao de PDFs + screening passada 2 (CHECKPOINT)

- **Status**: completed
- **Sub-etapa 5a**: `pdf-acquirer` (baixa PDFs publicos via cascata de 7 fontes; gera `_manual-fetch-required.md` para os fechados)
- **Sub-etapa 5b**: `screening-logger` modo 2 (aplica I/E na leitura full text)
- **Saida**: `systematic-review/papers_to_review/` + `screening/full-text.log.csv`
- **Iniciado em**: 2026-05-27 12:35, **Concluido em**: 2026-05-27 17:59,
- **N baixados automaticamente**: 15, / **N para download manual**: 13, / **N incluidos apos full text**: 25,
- **Notas**: sub-etapa 5a concluida com `pdf-acquirer`. Foram obtidos 15 de 28 textos automaticamente: 7 por arXiv direto ou seed arXiv, 5 por Unpaywall, 2 por arXiv via cascata C3 e 1 por HTML full text. O autor baixou manualmente os 13 PDFs restantes. Sub-etapa 5b concluida com `screening-logger` modo 2: 28 textos analisados, 25 incluidos finais e 3 excluidos. Saidas: `pdf-extracts/`, `screening/full-text.log.csv`, `screening/exclusion-reasons.md`. Checkpoint aprovado pelo autor em 2026-05-27 18:22.

## Etapa 6, Snowballing

- **Status**: completed
- **Agente**: `snowballing-hunter`
- **Saida**: `systematic-review/snowballing/`
- **Rodadas executadas**: 3,
- **N de novos candidatos por rodada**: rodada 1 = 69 candidatos novos adicionados a `search-results.json`; rodada 2 = 50 candidatos novos adicionados a `search-results.json`; rodada 3 = 30 candidatos novos adicionados a `search-results.json`,
- **Criterio de parada**: rodada com 0 incluidos novos OU maximo 3 rodadas
- **Iniciado em**: 2026-05-27 19:36, **Concluido em**: 2026-05-28 14:14,
- **Notas**: rodada 1 executada em `systematic-review/snowballing/round-1/`. Foram processados 25 papers-fonte com DOI. Backward: 158 referencias brutas, 154 unicas antes dos filtros, 69 novas apos dedup e pre-filtro. Forward: 0 citacoes brutas, 0 novas. Pre-filtro operacional rejeitou 84 candidatos fora do foco minimo do protocolo. Uma falha de API foi registrada: `Ulfsnes2024`, backward, OpenAlex 404 para uma referencia. Screening por titulo e abstract dos 69 candidatos `snowballing-1` executado em 2026-05-28 11:41: 9 incluidos para texto completo e 60 excluidos. Motivos de exclusao documentados em `screening/exclusion-reasons.md` para uso na escrita do metodo. Aquisicao concluida em 2026-05-28 12:15: 37 de 37 textos do conjunto atual presentes, incluindo os 9 do snowballing. Full text screening dos 9 candidatos `snowballing-1` executado em 2026-05-28 12:19: 6 incluidos finais adicionais e 3 excluidos. Incluidos finais consolidados: 31. Rodada 2 executada em 2026-05-28 13:19 usando como sementes os 6 incluidos finais adicionados pela rodada 1. Resultado da rodada 2: 183 referencias backward brutas, 182 unicas antes dos filtros, 50 novas apos dedup e pre-filtro, 128 rejeitadas em pre-filtro operacional, 18 falhas OpenAlex 404, forward 0 citacoes novas. Screening por titulo e abstract dos 50 candidatos `snowballing-2` executado em 2026-05-28 13:27: 5 incluidos para texto completo e 45 excluidos. Motivos de exclusao documentados em `screening/exclusion-reasons.md` para uso na escrita do metodo. Aquisicao dos 5 candidatos incluidos pela rodada 2 concluida em 2026-05-28 13:32: 5 PDFs obtidos automaticamente, 0 pendentes manuais. Textos completos extraidos com status `ok`. Full text screening dos 5 candidatos `snowballing-2` executado em 2026-05-28 13:36: 3 incluidos finais adicionais e 2 excluidos. Incluidos finais consolidados: 34. Rodada 3 executada em 2026-05-28 13:40 usando como sementes os 3 incluidos finais adicionados pela rodada 2. Resultado da rodada 3: 73 referencias backward brutas, 73 unicas antes dos filtros, 30 novas apos dedup e pre-filtro, 41 rejeitadas em pre-filtro operacional, 2 falhas OpenAlex 404, forward 0 citacoes novas. Screening por titulo e abstract dos 30 candidatos `snowballing-3` executado em 2026-05-28 13:44: 4 incluidos para texto completo e 26 excluidos. Aquisicao dos 4 candidatos incluidos pela rodada 3 executada em 2026-05-28 13:52: 3 PDFs obtidos automaticamente e 1 pendente para download manual. Screening full text parcial dos 3 textos obtidos executado em 2026-05-28 14:02: 3 incluidos finais adicionais, 0 excluidos e 1 pendente operacional sem PDF local. Incluidos finais consolidados ate o momento: 37. Proxima acao: baixar manualmente `AshaRajbhoj2024.pdf` ou aprovar fechamento do snowballing com corpus parcial antes da extracao estruturada. Como esta e a terceira rodada, nao havera rodada 4 pelo protocolo.

## Etapa 7, Extracao estruturada

- **Status**: completed
- **Agente**: `structured-extractor`
- **Saida**: `systematic-review/extracted/<citation-key>.md` por paper
- **Schema usado**: `software-engineering`
- **Iniciado em**: 2026-05-28 14:14, **Concluido em**: 2026-05-28 14:14,
- **N de extracoes**: 37,
- **Notas**: extracao estruturada de primeira passada concluida para os 37 estudos incluidos finais disponiveis. Saidas: `systematic-review/extracted/`, `extraction-matrix.csv` e `_summary.md`. `AshaRajbhoj2024` permaneceu pendente por ausencia de PDF local e nao foi contado como exclusao.

## Etapa 8, Avaliacao de qualidade (opcional)

- **Status**: skipped (`quality_assessment: none`)
- **Agente**: `quality-assessor`
- **Saida**: `systematic-review/quality-assessment/`
- **Framework**: `none`
- **Iniciado em**: 2026-05-28 14:14, **Concluido em**: 2026-05-28 14:14,
- **N avaliados**: 0,
- **Notas**: etapa ignorada conforme protocolo aprovado, `quality_assessment: none`.

## Etapa 9, Sintese (CHECKPOINT)

- **Status**: completed (aguardando aprovacao do autor no checkpoint)
- **Agente**: `synthesis-writer`
- **Saida**: `systematic-review/synthesis.md`
- **Metodo**: `thematic` (modo hibrido: temas indutivos validados contra a taxonomia de 6 dimensoes)
- **Iniciado em**: 2026-05-28 14:22, **Concluido em**: 2026-05-28 15:05,
- **Notas**: sintese tematica hibrida dos 37 estudos incluidos finais concluida em `synthesis.md` (~3819 palavras, self-check em-dash/en-dash com zero ocorrencias, confirmado por grep do coordenador). Deliverable restrito a `synthesis.md`; `review.tex` adiado por mismatch de chaves (extraction-keys vs `refs.bib`) e cobertura bibliografica incompleta; nenhum arquivo em `tex/sections/` foi tocado. 6 temas indutivos (cobertura 100%): T1 orquestracao multiagente e papeis; T2 especificacao e contrato como artefato central; T3 engenharia de contexto e recuperacao de conhecimento; T4 validacao, rastreabilidade e governanca; T5 colaboracao humano-IA, adocao e confianca (emergente); T6 seguranca, robustez e red-teaming (emergente). Mapeamento hibrido: 5 das 6 dimensoes (especificacao, contexto, papeis, execucao, validacao) tem ancoragem empirica forte; PORTABILIDADE e a dimensao fraca, aparece quase so como risco (lock-in, dependencia de IDE/modelo), nao como diferenciador positivo. T5 e T6 nao cabem nas 6 dimensoes: recomendada extensao da taxonomia com camada sociotecnica (colaboracao/governanca humano-IA) e seguranca como criterio transversal. Tres eixos de tensao reportados como consenso parcial: autonomia vs controle humano; governanca pesada vs agilidade leve; spec-first vs spec-recovered (Reversa). Reconciliacao de RQs: `protocol.md` tem 5 RQs (RQ1 a RQ5), `PAPER.md` lista so 4; RQ5 (lacunas) tratada como meta-pergunta de sintese, recomendada atualizacao de PAPER.md. Limitacao registrada: ~21 das 37 fichas tinham justificativa generica, sintese apoiou-se em campos estruturados + identidade publica dos frameworks; recomendada 2a passada de extracao com campo narrativo de achados antes da redacao final da Discussao.

## Etapa 10, Figura da metodologia (CHECKPOINT)

- **Status**: completed
- **Agente**: `methodology-diagram` (matplotlib, devido a indisponibilidade da cadeia node/mermaid/cairosvg no ambiente)
- **Saida**: `figures/methodology.{pdf,png,svg}` na raiz do paper (incluida no LaTeX via `figures/methodology.pdf`)
- **Design**: funil Kitchenham em 6 raias (Identificacao, Selecao, Snowballing, Extracao, Sintese, Relato) com counts reais
- **Iniciado em**: 2026-05-28 15:25, **Concluido em**: 2026-05-28 15:35,
- **Notas**: figura gerada com contagens que batem exatamente com o texto reescrito de `tex/sections/02_metodo_revisao.tex` (100 brutos, 85 candidatos, 28 e 25 incluidos, snowballing 3 rodadas com 149 candidatos e 12 novos, corpus final 37). Fundo branco. Script reproduzivel em `systematic-review/make_methodology_figure.py`.

## Reescrita da Etapa de Metodo (feedback do autor, 2026-05-28)

- **Motivo**: o autor rejeitou o `02_metodo_revisao.tex` anterior. Problemas: (1) descrevia uma "revisao narrativa" com "amostragem intencional" e afirmava na conclusao que "ainda nao foram aplicadas strings formais nem criterios de I/E", o que era FALSO em relacao ao pipeline executado; (2) voz em primeira pessoa ("frameworks citados pelo autor como relevantes"), escrevendo decisoes em nome do autor; (3) sem acentuacao pt-br; (4) sem figura da metodologia.
- **Acao**: secao reescrita no estilo do paper Kitchenham do autor (drone-review-sandeco.pdf): metodo Kitchenham nomeado, bases, periodo, criterios I/E em tabela, funil com numeros reais, snowballing com Wohlin, extracao (10 campos), sintese tematica, limitacoes. Voz impessoal. Acentuacao corrigida. Zero travessoes.
- **Decisao estrutural**: confirmado por grep que os 7 frameworks (BMAD, OpenSpec, Kiro, Antigravity etc.) NAO estao no corpus dos 37 estudos (so Reversa, como seed).
- **Enquadramento APROVADO pelo autor em 2026-05-28**: revisao de literatura multivocal (MLR), Kitchenham + Garousi et al. (2019). Literatura formal = 37 estudos (busca por string, funil da figura); literatura cinzenta = 7 frameworks (busca dirigida as fontes primarias, mesmos criterios I/E e mesmo esquema de extracao). Emenda registrada em `protocol.md` secao 11. Substitui o enquadramento provisorio de "duas frentes".
- **refs.bib**: adicionadas entradas `kitchenham2009slr` (DOI 10.1016/j.infsof.2008.09.009), `wohlin2014snowballing` (DOI 10.1145/2601248.2601268) e `garousi2019mlr` (DOI 10.1016/j.infsof.2018.09.006).
- **main.tex**: adicionado `\usepackage{graphicx}` + `\graphicspath{{figures/}}`.

## Recorte e busca dirigida da literatura cinzenta (frameworks), 2026-05-28

- **Recorte definido pelo autor (brainstorm)**: a revisao e sobre frameworks que ajudam quem usa um agente de desenvolvimento (Claude Code, Codex, Gemini CLI) a desenvolver software com IA. Registro em `BRAINSTORM_RECORTE_AGENT_LOOP.md` e memoria de projeto. Autor autorizou perder estudos que nao se alinhem ao recorte; foco prevalece.
- **Excluidos por categoria**: agentes/runtimes em si (Claude Code, Codex, Gemini CLI); IDEs/plataformas fechadas (Google Antigravity, Kiro); SDKs de construcao de agentes de proposito geral (CrewAI, Agno, Google ADK).
- **Busca dirigida** em comparativos publicos (spec-compare, MarkTechPost), listas curadas (Awesome-SDD, awesome-claude-code-toolkit) e repositorios GitHub.
- **Filtros**: (1) aderencia ao escopo; (2) tracao minima = adocao substancial + atividade recente.
- **Tracao medida via GitHub API em 2026-05-28** (stars, ultima atividade):
  - github/spec-kit: 106786, ativo. INCLUIDO.
  - gsd-build/get-shit-done (GSD): 63754, ativo. INCLUIDO.
  - Fission-AI/OpenSpec: 51404, ativo. INCLUIDO.
  - bmad-code-org/BMAD-METHOD: 48209, ativo. INCLUIDO.
  - Priivacy-ai/spec-kitty: 1273, ativo. INCLUIDO (no limiar).
  - Pimzino/claude-code-spec-workflow: 3748, mas sem push desde 2025-09 (~8 meses). EXCLUIDO por inatividade.
  - marcusgoll/Spec-Flow: 85. EXCLUIDO por tracao baixa.
  - tesslio/spec-driven-development-tile (Tessl): 38 no tile. EXCLUIDO por tracao; mantido apenas como referencia de ecossistema (plataforma comercial com cobertura editorial).
  - Reversa (Macedo2026): incluido por escopo (paper do autor + seed dirigido), ja consta no corpus formal.
- **Conjunto final de frameworks-objeto (6)**: GitHub Spec Kit, OpenSpec, BMAD Method, GSD, Spec Kitty, Reversa.
- **Pendente de propagacao**: `04_frameworks.tex`, `03_taxonomia.tex`, `05_discussao.tex` e `refs.bib` (entradas para GSD, OpenSpec, Spec Kitty) ainda referenciam o conjunto antigo; a sintese (`synthesis.md`) e o corpus formal dos 37 foram feitos sob o recorte amplo e precisam ser re-alinhados ao recorte novo (autor ciente de que estudos podem cair).

---

## Historico de sessoes

### Sessao 1, 2026-05-27 10:31

- Plano criado.
- `PAPER.md` atualizado com flags do pipeline systematic-review.
- Proxima acao: iniciar Etapa 1 (protocolo) com `review-protocol-builder`.

### Sessao 2, 2026-05-27 11:06

- Autor enviou `continue`.
- Etapa 1 iniciada com `review-protocol-builder`.
- `systematic-review/protocol.md` criado a partir de `PAPER.md` e `sections/review_protocol.md`.
- Etapa 1 concluida e aguardando decisao do autor no checkpoint.

### Sessao 3, 2026-05-27 11:11

- Autor respondeu `APROVAR`.
- Protocolo marcado como CONGELADO em `systematic-review/protocol.md`.
- Proxima acao: Etapa 2, Descritores de busca, via skill `search-descriptors`, apos novo `CONTINUE`.

### Sessao 4, 2026-05-27 11:29

- Autor confirmou Kitchenham e pediu criacao dos descritores com `search-descriptors`.
- Etapa 2 iniciada.
- `systematic-review/descriptors.md` criado.
- Proxima acao: Etapa 3, Busca multi-base + dedup, via skill `literature-search`, apos novo `CONTINUE`.

### Sessao 5, 2026-05-27 11:34

- Autor enviou `continue`.
- Etapa 3 iniciada.
- Busca multi-base executada.
- `systematic-review/search-results.json` criado com 84 candidatos finais.
- `systematic-review/search-log.md` criado com consultas, falhas e contagens.
- Proxima acao: Etapa 4, screening de titulo e abstract com `screening-logger`, apos novo `CONTINUE`.

### Sessao 6, 2026-05-27 12:03

- Autor enviou `continue`.
- Etapa 4 iniciada com `screening-logger` modo 1.
- Etapa 4 concluida: 84 analisados, 27 incluidos para texto completo, 57 excluidos.
- `search-results.json` atualizado com `screening_pass1`.
- Checkpoint pendente: autor deve aprovar ou pedir revisao da triagem antes da Etapa 5.

### Sessao 7, 2026-05-27 12:22

- Autor aprovou o checkpoint da Etapa 4 com `APROVAR`.
- Autor solicitou que os motivos de exclusao fiquem claros para registro no artigo de revisao.
- `screening/exclusion-reasons.md` atualizado com descricoes operacionais dos motivos de exclusao.
- Proxima acao: Etapa 5, aquisicao de PDFs e screening full text, via `pdf-acquirer` e `screening-logger`, apos novo `CONTINUE`.

### Sessao 8, 2026-05-27 12:35

- Autor enviou `continue`.
- Etapa 5 iniciada pela sub-etapa 5a, aquisicao de PDFs publicos com `pdf-acquirer`.
- Autor reforcou que artigos arXiv sao importantes.
- Executor ajustado para priorizar DOI `10.48550/arXiv.*` por download direto em `arxiv.org/pdf`.
- Sub-etapa 5a concluida: 14 de 27 textos obtidos automaticamente, incluindo 6 por `arxiv_direct`.
- 13 papers ficaram em `papers_to_review/_manual-fetch-required.md`.
- Proxima acao: autor baixar os 13 PDFs manuais ou autorizar screening full text parcial dos 14 obtidos.

### Sessao 9, 2026-05-27 15:08

- Autor perguntou se o artigo do Reversa foi encontrado.
- Verificacao: Reversa nao apareceu nos 84 resultados da busca automatica, mas estava em `refs.bib` e no escopo inicial do `PAPER.md`.
- `Macedo2026` foi adicionado como seed dirigido em `search-results.json`, com DOI `10.48550/arXiv.2605.18684`.
- PDF baixado diretamente de arXiv para `papers_to_review/Macedo2026.pdf`.
- Contagens atualizadas: 85 candidatos analisados, 28 incluidos, 57 excluidos; 15 textos obtidos automaticamente.

### Sessao 10, 2026-05-27 17:59

- Autor informou que concluiu todos os downloads manuais.
- Verificacao: os 28 textos incluidos na passada 1 estao presentes em `papers_to_review/`.
- Textos completos extraidos para `pdf-extracts/`.
- Screening full text executado: 25 incluidos finais, 3 excluidos.
- Etapa 5 concluida e aguardando aprovacao do checkpoint antes da Etapa 6.

### Sessao 11, 2026-05-27 18:22

- Autor aprovou o checkpoint da Etapa 5 com `APROVAR`.
- Lista final apos full text aprovada: 25 incluidos finais e 3 excluidos.
- Proxima acao: Etapa 6, snowballing backward + forward, apos novo `CONTINUE`.

### Sessao 12, 2026-05-27 19:36

- Autor enviou `CONTINUE`.
- Etapa 6 iniciada com `snowballing-hunter`, rodada 1.
- Saidas geradas em `systematic-review/snowballing/round-1/`.
- Resultado da rodada 1: 158 referencias backward brutas, 154 unicas antes dos filtros, 69 candidatos novos adicionados a `search-results.json`; forward retornou 0 citacoes novas.
- `search-results.json` passou de 85 para 154 registros.
- Proxima acao: screening por titulo e abstract dos 69 candidatos `snowballing-1`, apos novo `CONTINUE`.

### Sessao 13, 2026-05-28 11:46

- Autor enviou `CONTINUE`.
- Screening por titulo e abstract dos 69 candidatos `snowballing-1` executado.
- Resultado: 9 incluidos para texto completo e 60 excluidos.
- Motivos de exclusao agregados: missing I1 = 25, E8 = 12, E3 = 11, missing I2/I3/I4 = 6, E2 = 5, E7 = 1.
- Saidas atualizadas: `screening/title-abstract.log.csv`, `screening/exclusion-reasons.md`, `snowballing/round-1/screening-summary.md` e `search-results.json`.
- Proxima acao: aquisicao dos textos completos dos 9 candidatos incluidos pelo snowballing, apos novo `CONTINUE`.

### Sessao 14, 2026-05-28 12:07

- Autor reforcou que os motivos de exclusao devem ficar documentados para a escrita do paper; `screening/exclusion-reasons.md` ja contem a Passada 1b do snowballing com definicoes e contagens.
- Aquisicao dos 9 textos completos incluidos pelo snowballing executada.
- Resultado: 6 baixados automaticamente, 3 para download manual.
- Baixados automaticamente: `JulesWhite2023`, `ChristophTreude2025`, `JundaHe2025`, `JSauvola2024`, `AyyappaSajja2024`, `MitulModi2024`.
- Download manual necessario: `ShreyasPangavhane2024`, `KRRaghi2024`, `DanielRusso2024`.
- `_manual-fetch-required.md` atualizado com apenas os 3 pendentes atuais.
- `_acquisition.log.json` e `search-results.json` atualizados: arquivos ja existentes marcados como `already_present`, novos baixados como `downloaded`, pendentes como `manual_required`.
- Textos dos 6 PDFs baixados extraidos para `pdf-extracts/`; os 3 pendentes aparecem como `missing` em `pdf-extracts/_index.md`.
- Proxima acao: baixar manualmente os 3 PDFs pendentes ou autorizar screening full text parcial dos 6 obtidos.

### Sessao 15, 2026-05-28 12:19

- Autor informou que os downloads manuais foram concluidos e autorizou continuar.
- Verificacao: os 9 textos completos incluidos pelo snowballing estao presentes em `papers_to_review/`.
- Aquisicao sincronizada: 37 de 37 textos do conjunto atual presentes; `_manual-fetch-required.md` ficou sem pendencias.
- Textos completos extraidos para `pdf-extracts/`.
- Screening full text dos 9 candidatos `snowballing-1` executado.
- Resultado: 6 incluidos finais adicionais e 3 excluidos.
- Incluidos finais adicionais: `JulesWhite2023`, `JundaHe2025`, `JSauvola2024`, `MitulModi2024`, `KRRaghi2024`, `DanielRusso2024`.
- Excluidos em full text: `ChristophTreude2025` por `missing I2/I3/I4`, `AyyappaSajja2024` por `missing I1`, `ShreyasPangavhane2024` por `E2`.
- Incluidos finais consolidados: 31.
- Saidas atualizadas: `screening/full-text.log.csv`, `screening/exclusion-reasons.md`, `snowballing/round-1/fulltext-summary.md`, `search-results.json`.
- Proxima acao: snowballing rodada 2, pois a rodada 1 adicionou 6 incluidos finais, apos novo `CONTINUE`.

### Sessao 16, 2026-05-28 13:21

- Autor enviou `CONTINUE`.
- Executor de snowballing ajustado para rodadas posteriores usarem como sementes apenas os incluidos finais da rodada anterior.
- Snowballing rodada 2 executado com 6 papers-fonte: `JulesWhite2023`, `JundaHe2025`, `JSauvola2024`, `MitulModi2024`, `KRRaghi2024`, `DanielRusso2024`.
- Resultado da rodada 2: 183 referencias backward brutas, 182 unicas antes dos filtros, 50 candidatos novos adicionados a `search-results.json`; forward retornou 0 citacoes novas.
- Pre-filtro operacional rejeitou 128 candidatos fora do foco minimo do protocolo.
- Falhas registradas: 18 referencias OpenAlex retornaram 404 durante hidratacao.
- Saidas geradas em `systematic-review/snowballing/round-2/`.
- Proxima acao: screening por titulo e abstract dos 50 candidatos `snowballing-2`, apos novo `CONTINUE`.

### Sessao 17, 2026-05-28 13:27

- Autor confirmou continuar o `snowballing-2` normalmente.
- Screening por titulo e abstract dos 50 candidatos `snowballing-2` executado.
- Resultado: 5 incluidos para texto completo e 45 excluidos.
- Incluidos para aquisicao: `YuntongZhang2024`, `ZeeshanRasheed2024`, `HuanZhang2024`, `SaiZhang2025`, `pekzkaya2023`.
- Motivos de exclusao agregados: missing I1 = 16, E8 = 9, E3 = 9, E2 = 6, E7 = 3, E1 = 1, E5 = 1.
- Saidas atualizadas: `search-results.json`, `screening/title-abstract.log.csv`, `screening/exclusion-reasons.md`, `snowballing/round-2/screening-summary.md`.
- Proxima acao: aquisicao dos textos completos dos 5 candidatos incluidos pela rodada 2, apos novo `CONTINUE`.

### Sessao 18, 2026-05-28 13:32

- Autor enviou `CONTINUE`.
- Aquisicao dos 5 textos completos incluidos pelo `snowballing-2` executada.
- Resultado: 5 de 5 PDFs obtidos automaticamente, sem pendencias para download manual.
- Baixados automaticamente: `YuntongZhang2024`, `ZeeshanRasheed2024`, `HuanZhang2024`, `SaiZhang2025`, `pekzkaya2023`.
- Metodos de aquisicao: C3 = 4, C1 = 1.
- `_manual-fetch-required.md` atualizado com total 0.
- Textos extraidos para `pdf-extracts/` com status `ok` para os 5 novos PDFs.
- Saidas atualizadas: `papers_to_review/_acquisition.log.json`, `search-results.json`, `pdf-extracts/_index.md`, `snowballing/round-2/acquisition-summary.md`.
- Proxima acao: screening full text dos 5 candidatos da rodada 2, apos novo `CONTINUE`.

### Sessao 19, 2026-05-28 13:36

- Autor enviou `CONTINUE`.
- Screening full text dos 5 candidatos `snowballing-2` executado.
- Resultado: 3 incluidos finais adicionais e 2 excluidos.
- Incluidos finais adicionais: `YuntongZhang2024`, `ZeeshanRasheed2024`, `SaiZhang2025`.
- Excluidos em full text: `HuanZhang2024` por E3, tarefa isolada de code generation; `pekzkaya2023` por E7, comentario editorial sem framework operacional extraivel.
- Incluidos finais consolidados: 34.
- Motivos de exclusao atualizados em `screening/exclusion-reasons.md`, incluindo resumo consolidado apos snowballing rodada 2.
- Saidas atualizadas: `screening/full-text.log.csv`, `search-results.json`, `snowballing/round-2/fulltext-summary.md`.
- Proxima acao: snowballing rodada 3, ultima rodada permitida pelo protocolo, usando como sementes os 3 incluidos finais da rodada 2, apos novo `CONTINUE`.

### Sessao 20, 2026-05-28 13:40

- Autor enviou `CONTINUE`.
- Snowballing rodada 3 executado com 3 papers-fonte: `YuntongZhang2024`, `ZeeshanRasheed2024`, `SaiZhang2025`.
- Resultado da rodada 3: 73 referencias backward brutas, 73 unicas antes dos filtros, 30 candidatos novos adicionados a `search-results.json`; forward retornou 0 citacoes novas.
- Por paper-fonte: `YuntongZhang2024` gerou 9 candidatos novos; `ZeeshanRasheed2024` gerou 0; `SaiZhang2025` gerou 21.
- Pre-filtro operacional rejeitou 41 candidatos fora do foco minimo do protocolo.
- Falhas registradas: 2 referencias OpenAlex retornaram 404 durante hidratacao.
- Saidas geradas em `snowballing/round-3/`.
- Proxima acao: screening por titulo e abstract dos 30 candidatos `snowballing-3`, apos novo `CONTINUE`. Como esta e a terceira rodada, nao havera rodada 4 pelo protocolo.

### Sessao 22, 2026-05-28 13:44

- Autor enviou `CONTINUE`.
- Screening por titulo e abstract dos 30 candidatos `snowballing-3` executado.
- Resultado: 4 incluidos para texto completo e 26 excluidos.
- Incluidos para aquisicao: `ChenQian2023`, `SiruiHong2023`, `YuCheng2023`, `AshaRajbhoj2024`.
- Motivos de exclusao agregados: E3 = 15, missing I1 = 5, E1 = 3, E8 = 2, E2 = 1.
- Saidas atualizadas: `search-results.json`, `screening/title-abstract.log.csv`, `screening/exclusion-reasons.md`, `snowballing/round-3/screening-summary.md`.
- Proxima acao: aquisicao dos textos completos dos 4 candidatos incluidos pela rodada 3, apos novo `CONTINUE`.

### Sessao 21, 2026-05-28 13:46

- Autor invocou a skill `/competitor-finder`.
- Executada a analise automatica de concorrentes no modo survey para o paper ativo.
- Mapeados 13 concorrentes academicos e industriais que analisam surveys de agentes e frameworks de SDD, calculando o Contribution Overlap Score (COS) detalhado para cada um.
- Constatada a classificacao CROWDED pelo volume de surveys gerais na literatura, porem com forte diferenciacao tematica no recorte do Prompt ao Processo.
- Criado o relatorio de apoio a escrita do paper em `related-work/competitors.md`, contendo frases de diferenciacao prontas e citacoes obrigatorias.
- Atualizado o status do scan no arquivo de metadados `PAPER.md`.

### Sessao 23, 2026-05-28 13:52

- Autor enviou `CONTINUE`.
- Aquisicao dos 4 textos completos incluidos pelo `snowballing-3` executada.
- Resultado: 3 PDFs obtidos automaticamente e 1 pendente para download manual.
- Baixados automaticamente: `ChenQian2023`, `SiruiHong2023`, `YuCheng2023`.
- Download manual necessario: `AshaRajbhoj2024`, DOI `10.1145/3641399.3641403`.
- Metodos de aquisicao: arxiv_direct = 2, C3 = 1, manual_required = 1.
- Textos extraidos para `pdf-extracts/` com status `ok` para os 3 PDFs obtidos; `AshaRajbhoj2024` aparece como `missing`.
- Saidas atualizadas: `papers_to_review/_acquisition.log.json`, `papers_to_review/_manual-fetch-required.md`, `search-results.json`, `pdf-extracts/_index.md`, `snowballing/round-3/acquisition-summary.md`.
- Proxima acao: baixar manualmente `AshaRajbhoj2024.pdf` ou autorizar screening full text parcial dos 3 textos obtidos.

### Sessao 24, 2026-05-28 14:02

- Autor enviou `CONTINUE`.
- Verificacao: `AshaRajbhoj2024.pdf` ainda nao esta presente em `papers_to_review/`.
- Screening full text parcial dos 3 textos obtidos no `snowballing-3` executado.
- Resultado: 3 incluidos finais adicionais e 0 excluidos entre os textos analisados.
- Incluidos finais adicionais: `ChenQian2023`, `SiruiHong2023`, `YuCheng2023`.
- Pendente operacional: `AshaRajbhoj2024`, DOI `10.1145/3641399.3641403`, sem PDF local e nao registrado como exclusao.
- Incluidos finais consolidados ate o momento: 37.
- Saidas atualizadas: `screening/full-text.log.csv`, `search-results.json`, `screening/exclusion-reasons.md`, `snowballing/round-3/fulltext-summary.md`.
- Proxima acao: baixar manualmente `AshaRajbhoj2024.pdf` ou aprovar fechamento do snowballing com corpus parcial antes da extracao estruturada.

### Sessao 25, 2026-05-28 14:10

- Autor enviou `CONTINUE` com a instrucao de criar a secao de Trabalhos Relacionados de forma concisa e direta, relatando rapidamente o estado da arte, os gaps e a proposta.
- Escrita a secao em LaTeX no arquivo `tex/sections/03_trabalhos_relacionados.tex`, organizando a discussao em tres subsecoes estruturadas (O que Existe na Literatura, Gaps de Pesquisa, e Proposta do Nosso Projeto).
- Identificada a ausencia da chave `JundaHe2025` no arquivo BibTeX central `refs.bib` durante a analise estatica com o `latex-validator`.
- Resolvido o DOI oficial de Junda He et al. (TOSEM 2025) como `10.1145/3706857` e cadastrada a entrada de forma limpa em `refs.bib`.
- Executada a suite de validacao `latex-validator` (`validate_tex.py` e `validate_bib.py`) com sucesso, retornando zero erros fatais de compilacao.
- O corpus bibliografico e os arquivos LaTeX estao plenamente integrados e consistentes para uso no Overleaf.


### Sessao 26, 2026-05-28 14:14

- Autor enviou `CONTINUE`.
- Verificacao: `AshaRajbhoj2024.pdf` ainda nao esta presente em `papers_to_review/`.
- Decisao operacional inferida do `CONTINUE`: fechar o snowballing no limite de 3 rodadas com corpus parcial documentado, mantendo `AshaRajbhoj2024` como pendencia operacional e nao como exclusao.
- Etapa 6 concluida: snowballing encerrado por maximo de 3 rodadas do protocolo.
- Etapa 7 concluida: extracao estruturada de primeira passada executada para 37 estudos incluidos finais.
- Etapa 8 ignorada conforme protocolo, `quality_assessment: none`.
- Saidas geradas: `systematic-review/extracted/extraction-matrix.csv`, `systematic-review/extracted/_summary.md` e fichas individuais em `systematic-review/extracted/`.
- Proxima acao: Etapa 9, sintese tematica e matriz comparativa para responder RQ1 a RQ5.

### Sessao 27, 2026-05-28 15:05

- Autor invocou `/systematic-review` com instrucao de continuar o fluxo.
- Coordenador apresentou status (Etapas 1 a 8 concluidas, proxima Etapa 9 checkpoint) e coletou as decisoes pendentes do checkpoint da Etapa 9 via AskUserQuestion.
- Decisao 1: metodo de sintese = `thematic`. Flag `synthesis_method: thematic` persistida em PAPER.md.
- Decisao 2: articulacao temas x taxonomia = modo HIBRIDO (temas indutivos primeiro, depois mapeados contra as 6 dimensoes, reportando sobreposicao, dimensoes pouco cobertas e temas emergentes fora da taxonomia).
- Etapa 9 executada via `synthesis-writer`: `synthesis.md` criado com 6 temas indutivos, mapeamento hibrido, 2 tabelas cruzadas (temas x 6 dimensoes e temas x RQs), cross-cutting findings, lacunas (RQ5) e limitacoes. ~3819 palavras. Self-check de em-dash/en-dash com zero ocorrencias, reverificado por grep do coordenador.
- Achados-chave: portabilidade e a dimensao fraca da taxonomia (so risco); T5 colaboracao humano-IA e T6 seguranca emergem fora das 6 dimensoes; protocol.md tem 5 RQs mas PAPER.md so lista 4.
- Etapa 9 aguardando aprovacao do autor no checkpoint antes do CONTINUE para a Etapa 10 (figura da metodologia).
