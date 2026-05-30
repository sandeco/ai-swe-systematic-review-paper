# Improve plan, ai-swe-systematic-review-paper

> Gerado por SCIENTEX / scientex-improve em 2026-05-30.
> Fonte: `score.md`. Paper: `_papers/ai-swe-systematic-review-paper/PAPER.md`.
> Q atual: 74/100. Meta do autor: >90/100. Teto honesto desta rodada (so itens AUTO): ~86/100.

## 1. Diagnostico gap-to-90

Decomposicao por dimensao (Secao 2 do score.md):

| Dimensao | Peso | Nota atual | Teto AUTO honesto | O que destrava o resto |
|---|---|---|---|---|
| Novidade | 20 | 16 | 17 | nada a mais critico |
| Rigor | 25 | 16 | 21..22 | IRR humano de verdade (2o codificador) |
| Reprodutibilidade | 15 | 13 | 14 | nada a mais critico |
| Clareza | 15 | 13 | 14 | nada a mais critico |
| Magnitude | 15 | 10 | 12 | 2a passada completa bem-feita |
| Generalizacao | 10 | 6 | 8 | mais bases / mais idiomas (busca nova) |
| **Total** | **100** | **74** | **~86** | itens AUTOR da Secao 4 |

- Q atual: 74/100.
- Gap ate a meta (>90): 16 pontos. Gap ate a meta declarada no score.md (88): 14 pontos.
- Soma dos deltas executaveis sem recurso novo (itens AUTO, conservador): cerca de +12.
- Teto honesto so com itens AUTO: **~86/100** (bate com o teto 88-90 do score.md, que assume IRR humano real).
- A meta acima de 90 e alcancavel so com trabalho autonomo? **NAO.**
  - Faltam ~4 a 5 pontos que dependem dos itens AUTOR: principalmente um segundo codificador humano independente para o IRR (IRR de verdade, nao auto-concordancia de protocolo), e secundariamente ampliacao real de bases na busca.
  - Razao tecnica do limite no IRR: a triagem registrada teve um unico avaliador (`screening-logger`). Recalcular kappa entre a triagem original e uma segunda passada automatizada com a MESMA logica produz concordancia quase trivial e nao e IRR credivel. Por isso a parte AUTO do IMP-1 rende pouco (protocolo + script + planilha), e o ponto cheio fica com o autor.

## 2. Forcas a preservar (NAO regredir)

- Gap e enquadramento de Engenharia de Software (nao confundir com survey de arquitetura de agentes).
- Revisao sistematica PURA: so entram estudos com paper citavel/DOI (sem literatura cinzenta, sem paper companheiro).
- 40 citacoes, 100% com DOI verificado e link clicavel (campo `note` com `\href`), inclusive preprints arXiv.
- 5 figuras de dados reais (rastreaveis a extraction-matrix.csv), 96 DPI, fonte >= 12pt, variantes _pt/_en.
- Bilingue: `main.tex` (pt-br) + `main-en.tex` (en), mesmo `refs.bib`.
- Hedging honesto (nao superdimensiona desempenho), secao de Limitacoes explicita.
- Zero travessao; sem subsecoes numeradas; acentuacao pt-br correta.

## 3. Itens a executar (ordenados por delta/esforco e desbloqueio de venue)

| Ordem | Item | Dimensao | Delta | Esforco | Viab. | No caminho ate 90? | Acao concreta | Dado-fonte |
|---|---|---|---|---|---|---|---|---|
| 1 | IMP-2 | Rigor | +3 | medio | AUTO | sim (parcial) | Checklist de qualidade adaptado (peer-reviewed vs preprint, avaliacao empirica, estudo de caso, repo publico) aplicado aos 37 estudos; tabela de distribuicao por categoria; discutir impacto dos preprints e dos 2 de confianca media | extraction-matrix.csv (confianca, evidencia) |
| 2 | IMP-3 | Rigor/Clareza | +1 | baixo | AUTO | sim | Trocar "validada empiricamente" por "confrontada com a evidencia do corpus" no abstract, intro, taxonomia e resultados, nas DUAS linguas | texto (julgamento do autor) |
| 3 | IMP-6 | Clareza/Rigor | +2 | baixo-medio | AUTO | sim | Checklist de relato (PRISMA 2020 ou Kitchenham) como apendice, item a item, referenciado no texto; rotular a figura de fluxo como compativel | estrutura do paper |
| 4 | IMP-8 | Novidade | +1 | baixo | AUTO | sim | Na Related Work, contraste quantitativo de cobertura/escopo vs Hou et al. e He et al. (foco por processo vs por tarefa/tecnica) | refs.bib + synthesis.md |
| 5 | IMP-4 | Magnitude/Rigor | +2 | alto | AUTO | sim (parcial) | Campo narrativo de key_findings por estudo (hoje ~16/37 substantivas); reforcar sintese tematica com evidencia por estudo | extracted/*.md |
| 6 | IMP-5 | Generalizacao | +1 | medio | AUTO (parcial) | parcial | Curva de saturacao do snowballing (candidatos 69/50/30; incluidos 6/3/3) + argumento honesto do corte; figura 96 DPI | snowballing/round-*/summary.md |
| 7 | IMP-7 | Generalizacao | +1 | medio | AUTO (parcial) | parcial | Reforcar justificativa do recorte + paragrafo de vies de publicacao na ameaca a validade | search-log.md + protocol.md |
| 8 | IMP-1 | Rigor | +1 (de +5) | alto | AUTO parcial / AUTOR | parcial | AUTO: protocolo de dupla-triagem reproduzivel + script de Cohen kappa + planilha de codificacao, reportado com honestidade no Metodo. AUTOR: 2o codificador humano para o ponto cheio | screening/*.log.csv |

## 4. Itens que dependem de voce (recurso real)

| Item | Delta cheio restante | O que so o autor fecha | Infraestrutura que a skill entrega |
|---|---|---|---|
| IMP-1 | +3 a +4 (Rigor 21->24) | Um segundo codificador humano independente que re-triagem uma amostra para calcular IRR de verdade | Protocolo de dupla-triagem reproduzivel + script de Cohen kappa pronto + planilha de codificacao pre-preenchida com as decisoes originais |
| IMP-7 | +1 (Generalizacao 8->9) | Rodar busca em bases ainda nao consultadas / sem restricao EN-PT e triar o retorno | Strings de busca prontas (descriptors.md) + protocolo de inclusao/exclusao; a skill faz o reforco textual do recorte agora |
| IMP-5 (opcional) | parte do +2 | Rodadas extras de snowballing reais (precisa de rede/APIs, hoje sujeito a firewall do container) | Scripts run_snowballing*.py ja existem; a skill entrega a curva e o argumento de corte |

## 5. Resultado esperado

- Se executar tudo que e AUTO: Q estimado **~86/100** (teto honesto desta rodada; meta 88 do score.md fica a 2 pontos, meta >90 nao alcancada sem itens AUTOR).
- Se o autor fechar tambem os itens da Secao 4 (IRR humano real + busca ampliada): Q estimado **~90 a 91/100**.
- Itens que NAO serao tocados: todas as forcas da Secao 2 deste plano. Nenhum numero, kappa, distribuicao ou achado sera inventado; tudo rastreia a `systematic-review/`.

## 6. Confirmacao

Aguardando a escolha do autor (Etapa 3b). Nenhum arquivo do paper foi alterado ate aqui.
