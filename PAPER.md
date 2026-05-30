# PAPER: Revisao Sistematica de Frameworks de Desenvolvimento de Software com IA (corpus de 37 estudos)

> Este paper nasceu da divisao do antigo `ai-dev-frameworks-review` em dois recortes
> (2026-05-29). Este e o **recorte anterior / amplo**: a revisao sistematica formal
> (Kitchenham) do corpus de 37 estudos academicos e de literatura cinzenta sobre
> desenvolvimento de software com IA. O recorte novo, focado nos frameworks de apoio a
> agentes de desenvolvimento (BMAD, Reversa, Spec Kit, OpenSpec, GSD, Spec Kitty), virou
> o paper irmao `_papers/dev-agent-frameworks-review-paper`. O workspace original foi
> arquivado em `_papers/_archive/ai-dev-frameworks-review`.

## Meta

- **Autores**: Sanderson Oliveira de Macedo, Federal Institute of Goias (`sanderson.macedo@ifg.edu.br`)
- **Venue-alvo**: arXiv (preprint). Categoria principal provavel: `cs.SE`; cross-list possivel: `cs.AI`.
- **Status**: CONCLUIDO E PRONTO PARA PUBLICAR (modo autonomo, 2026-05-30). Texto escrito da sintese, validado (latex + 40/40 citacoes com DOI), 3 ciclos de critic (REVISAO MENOR, 0 issue residual), TRADUZIDO PARA INGLES e HUMANIZADO (voz Ng/Rajpurkar). Figura da metodologia regenerada em ingles a 96 DPI / fontes >=12pt. Ver `AUTONOMOUS_RUN.md` e `critic/review_log.md`.
- **Idioma de escrita**: BILINGUE. `main.tex` (pt-br, secoes em `tex/sections/`) e `main-en.tex` (ingles, secoes em `tex/sections-en/`), mesmo `refs.bib`.
- **Figuras (5, dados reais, 96 DPI, >=12pt, variantes _pt/_en)**: methodology (funil Kitchenham), studies_by_year, evidence_profile, theme_dimension (mapa de calor), risk_frequency. Geradas por `systematic-review/make_methodology_bilingual.py` e `make_data_figures.py`.
- **DOI**: 100% das 41 entradas do refs.bib tem `doi` verificado E `note` com `\href` clicavel (visivel mesmo com bibstyle `plain`, inclusive nos @misc/preprints).
- **Correcao de dado (2026-05-30)**: ranking de risco corrigido (seguranca e 4o, nao 2o): contexto 33 > confiabilidade 31 > custo de coordenacao 25 > seguranca 24 > governanca 16; texto ajustado em ambas as versoes (a figura risk_frequency expos a discrepancia).

## Humanizer (voz autoral, ingles)

- Alvo de estilo: perfil Ng/Rajpurkar (corpus `reference_authors/`): ingles cientifico direto, conciso, empirico; "We present/propose"; numeros concretos cedo; conectivos sobrios.
- Antes->depois (burstiness do paper): media 24,6->23,8 palavras/frase; frases longas (>30w) 30%->27%; n de frases 209->216 (mais frases curtas). Desvio ~11 (variacao saudavel, acima do piso 8).
- Palavras-fetiche / conectivos-cl;iche ("moreover", "furthermore", "leverage", "robust", "comprehensive", "delve", "landscape", "plays a crucial role"...): ZERO ocorrencias no texto final.
- Tecnicas aplicadas: variar ritmo (quebra de run-ons 45-60w via ponto), cortar paralelismo simetrico, voz autoral em 1a pessoa do plural, citacoes integradas.
- Contrato de preservacao: todos os \cite (41), numeros e fatos intactos; zero travessao; sem subsecao numerada. Nenhum claim fortalecido/enfraquecido.
- **paper_type**: `systematic-review`
- **protocol**: `kitchenham` (RSL pura; APENAS estudos com paper citavel/DOI. Enquadramento multivocal/literatura cinzenta REMOVIDO a pedido do autor em 2026-05-30 para maximizar rigor; ref. Garousi removida; figura da metodologia retitulada para "revisao sistematica de literatura").
- **quality_assessment**: `none`
- **synthesis_method**: `thematic` (modo hibrido)
- **target_pages**: `12-20`
- **Corpus final**: 37 estudos incluidos finais (`AshaRajbhoj2024` pendente operacional, fora da extracao).

## Recorte (objeto deste paper)

Revisao sistematica da literatura sobre frameworks, metodos e sistemas de desenvolvimento
de software com IA que deslocam a unidade de trabalho do prompt isolado para processos
estruturados com artefatos persistentes, papeis agenticos, execucao integrada e validacao.
O objeto e o **corpus de literatura** (37 estudos: ChatDev, MetaGPT, AutoCodeRover, SDD,
AgileGen, ASTRA, etc.), nao um conjunto fixo de produtos. A selecao dirigida dos frameworks
de apoio (BMAD, Spec Kit, OpenSpec, GSD, Spec Kitty, Reversa) foi separada para o paper irmao.

## Perguntas de pesquisa (autoridade: `systematic-review/protocol.md`)

| ID | Pergunta | Status |
|---|---|---|
| RQ1 | Quais dimensoes arquiteturais distinguem esses frameworks? | respondida na sintese |
| RQ2 | Como organizam contexto, papeis, artefatos, execucao e validacao? | respondida na sintese |
| RQ3 | Que tipos de evidencia sustentam as alegacoes? | respondida na sintese |
| RQ4 | Quais riscos e limitacoes sao reportados ou inferiveis? | respondida na sintese |
| RQ5 | Que lacunas de pesquisa permanecem? | respondida na secao de lacunas da sintese |

Nota: o `PAPER.md` antigo listava so 4 RQs; a autoridade e o `protocol.md` com 5 RQs. Alinhar ao escrever.

## Contribuicoes planejadas

1. Taxonomia de seis dimensoes (especificacao, contexto, papeis, execucao, validacao, portabilidade), validada empiricamente contra o corpus.
2. Sintese tematica de seis temas indutivos (cobertura 100% dos 37 estudos).
3. Discussao de riscos praticos e tres eixos de tensao (autonomia vs controle; governanca pesada vs agil; spec-first vs spec-recovered).
4. Agenda de pesquisa orientada a processo (RQ5).

## Ativos herdados nesta pasta

- `systematic-review/`: pipeline completo (protocolo, descritores, busca, screening, snowballing 3 rodadas, extracao, **`synthesis.md`**), scripts e corpus de PDFs em `papers_to_review/`.
- `figures/methodology.{pdf,png,svg}`: figura do funil Kitchenham (numeros reais).
- `tex/sections/02_metodo_revisao.tex`: secao de metodo ja reescrita no estilo Kitchenham (herdada, pronta).
- `tex/sections/03_taxonomia.tex`: taxonomia (compartilhada com o paper irmao). REESCREVER para este recorte: trocar os exemplos centrados nos 7 frameworks pela validacao empirica contra o corpus, usando a tabela tema x dimensao de `synthesis.md`.
- `tex/sections/03_trabalhos_relacionados.tex`: trabalhos relacionados (surveys). REVISAR para focar no posicionamento da revisao formal.
- `sections/review_protocol.md`: protocolo inicial (historico, superado por `systematic-review/protocol.md`).
- `refs.bib`: bibliografia compartilhada; PODAR entradas nao usadas por este paper.

## Secoes (status)

| Secao | Arquivo | Status |
|---|---|---|
| Resumo | `tex/sections/00_resumo.tex` | ESCRITO (pt-br) |
| Introducao | `tex/sections/01_introducao.tex` | ESCRITO (5 RQs, enquadramento de revisao de literatura) |
| Metodo de Revisao | `tex/sections/02_metodo_revisao.tex` | PRONTO (grey-lit reconciliado: aponta para o paper irmao) |
| Trabalhos Relacionados | `tex/sections/03_trabalhos_relacionados.tex` | REESCRITO (posicionamento da revisao formal, citacoes do corpus) |
| Taxonomia | `tex/sections/03_taxonomia.tex` | REESCRITO (6 dimensoes ancoradas no corpus; sem subsecoes) |
| Resultados / Sintese | `tex/sections/04_resultados_sintese.tex` | ESCRITO (6 temas + 3 tabelas; nucleo do paper) |
| Discussao | `tex/sections/05_discussao.tex` | ESCRITO (cross-cutting + 3 eixos de tensao) |
| Agenda de Pesquisa | `tex/sections/06_agenda_pesquisa.tex` | ESCRITO (RQ5, 6 lacunas) |
| Conclusao | `tex/sections/07_conclusao.tex` | ESCRITO |

## Submissao

- Recomendacao gerada em 2026-05-30: ver `venue-recommendation-2026-05-30.md`.
- Q (qualidade) validado: 74/100. Perfil: balanceado. Restricoes: internacional em ingles, sem APC.
- Tier 1 (aspirational): ACM Computing Surveys, IEEE TSE (baixa probabilidade; provavel APC no CSUR).
- Tier 2 (realistic, ALVO PRINCIPAL): Information and Software Technology (IST, melhor encaixe, sem APC pela assinatura) -> Journal of Systems and Software / Empirical Software Engineering -> Automated Software Engineering.
- Tier 3 (safe, sem APC): e-Informatica Software Engineering Journal (OA gratuito).
- Plano sequencial (nunca paralelo): IST -> (JSS ou EMSE) -> AUSE -> EISEJ. Manter preprint no arXiv.
- Pendencias antes de submeter (criticas para venues de RSL): adicionar confiabilidade entre avaliadores (kappa); incluir avaliacao de qualidade/risco de vies; suavizar "validacao empirica" da taxonomia para "confronto com a evidencia".

## Proximos passos

1. Converter `systematic-review/synthesis.md` nas secoes de Resultados/Sintese, Discussao e Agenda.
2. Escrever Resumo e Introducao com o enquadramento de revisao sistematica de literatura.
3. Reescrever a Taxonomia como validacao empirica (tabela tema x dimensao da sintese).
4. Podar `refs.bib` para as citacoes deste recorte.
5. Recuperar `AshaRajbhoj2024.pdf` se for fechar o corpus em 38, ou manter a pendencia documentada.

## Regras do projeto

- PROIBIDO travessao (em-dash U+2014 / en-dash U+2013) em qualquer texto gerado.
- Nao fabricar citacoes nem dados; todo numero rastreia a CSV/JSON do pipeline.
- Decisoes de pesquisa sao do autor; usar checkpoints.
