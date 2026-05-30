# Score, ai-swe-systematic-review-paper

> Análise de viabilidade do paper, para consumo pelo futuro agente `improve`.
> Paper: "From Prompt to Process: A Systematic Review of AI-Assisted Software Development Frameworks"
> Tipo: revisão sistemática de literatura (Kitchenham), bilíngue (pt-br + en), 37 estudos.
> Data da avaliação: 2026-05-30. Avaliador: venue-recommender / paper-critic (SCIENTEX).
> **Score atual (Q): 86 / 100.** (era 74; rodada scientex-improve de 2026-05-30, com follow-up de texto completo e busca suplementar) **Teto honesto desta rodada atingido (~86).** **Meta 90+ exige itens AUTOR: IRR humano real (kappa) e expansão real do corpus com re-extração dos 12 estudos da busca suplementar.**

Este arquivo é a fonte de verdade do score. O agente `improve` deve: (1) ler este arquivo, (2) executar itens do backlog em ordem de prioridade, (3) reescrever apenas o necessário sem quebrar fatos, citações, números, DOIs, figuras nem as regras do SCIENTEX, (4) reavaliar com a mesma rubrica, (5) atualizar a tabela de score e o change log ao final.

## 1. Rubrica de pontuação (como pontuar, adaptada para RSL)

| Dimensão | Peso | O que mede em uma revisão sistemática |
|---|---|---|
| Novidade vs literatura | 20 | gap claro e posicionamento contra surveys/RSLs existentes |
| Rigor do protocolo | 25 | protocolo, multibase, 2 passadas, snowballing, **confiabilidade entre avaliadores (IRR)**, **avaliação de qualidade / risco de viés**, saturação |
| Reprodutibilidade | 15 | protocolo público, matriz de extração, logs, scripts, DOIs, dados abertos |
| Clareza e completude | 15 | estrutura, figuras com caption, tabelas, fluxo PRISMA/Kitchenham, limitações |
| Magnitude da contribuição | 15 | profundidade da síntese, força da taxonomia, achados acionáveis |
| Generalização | 10 | nº de estudos, janela temporal, idiomas/bases, viés de publicação tratado |

Score = soma ponderada das notas por dimensão.

## 2. Score atual (decomposição)

| Dimensão | Peso | Nota (74) | Nota (85) | Justificativa (estado em 2026-05-30, pós scientex-improve) |
|---|---|---|---|---|
| Novidade | 20 | 16 | 17 | IMP-8: posicionamento quantitativo vs Hou et al. e He et al. com diferencial mensurável pela unidade de análise (framework operacional vs tarefa/componente). |
| Rigor | 25 | 16 | 21 | IMP-2 avaliação de qualidade por categoria aplicada aos 37 (tabela por faixa); IMP-3 overclaim suavizado; IMP-6 checklist Kitchenham; IMP-1 IRR reportado com honestidade (dupla-checagem por protocolo + infra de kappa). Para 24+: IRR humano real (AUTOR). |
| Reprodutibilidade | 15 | 13 | 14 | novos scripts reproduzíveis (qualidade, kappa, achados narrativos, saturação), coding sheets e checklist de relato, somados ao que já existia. |
| Clareza | 15 | 13 | 14 | IMP-6 checklist de relato + nova tabela de qualidade + figura de saturação; estrutura de relato mais completa e auditável. |
| Magnitude | 15 | 10 | 12 | IMP-4 FEITO (texto completo): 2a passada sobre pdf-extracts dos 25; achados reais por estudo e resultados empíricos concretos injetados na síntese (AutoDev 91,5% Pass@1; ASTRA 11-66%; SDD ate 50%; SKaruppuchamy 20x deploy; Watfa SEM n=328; Reversa 517 claims). Síntese deixa de depender da identidade pública. |
| Generalização | 10 | 6 | 8 | IMP-5 curva de saturação honesta + IMP-7 viés de publicação quantificado (26/37) + busca suplementar (arXiv+Crossref) como auditoria de completude: revelou 12 estudos no escopo não capturados (5 na janela, 7 pós-corte), reportados com honestidade. Não infla o número (corpus não re-extraído); expansão real fica AUTOR. |
| **Total** | **100** | **74** | **86** | deltas confirmados por re-crítica independente (paper-critic, ciclo 4); IMP-4 elevado de parcial a completo com evidência de texto completo verificável na síntese. Sem fabricação; sem regressão de forças. |

## 3. Forças a preservar (NÃO regredir)

- Gap e enquadramento de Engenharia de Software (não confundir com survey de arquitetura de agentes).
- Revisão sistemática PURA: só entram estudos com paper citável/DOI (sem literatura cinzenta, sem paper companheiro).
- 40 citações, 100% com DOI verificado e link clicável (campo `note` com `\href`), inclusive preprints arXiv.
- 5 figuras de dados reais (rastreáveis à extraction-matrix.csv), 96 DPI, fonte >= 12pt, variantes _pt/_en.
- Bilíngue: `main.tex` (pt-br) + `main-en.tex` (en), mesmo `refs.bib`.
- Hedging honesto (não superdimensiona desempenho), seção de Limitações explícita.
- Zero travessão; sem subseções numeradas; acentuação pt-br correta.

## 4. Backlog de melhoria (priorizado)

Cada item: dimensão alvo, delta esperado, esforço, ação concreta, critério de aceite, fonte de dados.
Prioridade = maior delta por esforço, e desbloqueio de venues top de RSL.

### IMP-1 (CRÍTICO) Confiabilidade entre avaliadores (IRR) [PARCIAL 2026-05-30: infra entregue (irr_kit.py, coding sheets, irr-protocol.md) + reporte honesto no Método; ponto cheio PENDENTE-AUTOR: 2o codificador humano para o kappa]
- Dimensão: Rigor. Delta esperado: +4 a +5. Esforço: alto (exige 2o avaliador ou protocolo de re-triagem).
- Ação: reaplicar a triagem (título/resumo e texto completo) por um segundo avaliador em uma amostra (ou no todo), calcular Cohen's kappa (ou Krippendorff), reportar o valor e como divergências foram resolvidas. Se 2o avaliador humano não for viável, documentar um protocolo de dupla-checagem reproduzível e reportar a concordância.
- Critério de aceite: kappa reportado no Método com interpretação; objeção nº 1 de revisores de RSL neutralizada.
- Fonte: systematic-review/screening/*.csv (logs de triagem).

### IMP-2 (CRÍTICO) Avaliação de qualidade / risco de viés [FEITO 2026-05-30: checklist de 4 itens aplicado aos 37; Tabela tab:qualidade (alta 11, média 17, baixa 9); make_quality_assessment.py + quality-assessment.csv]
- Dimensão: Rigor. Delta esperado: +3 a +4. Esforço: médio.
- Ação: aplicar um checklist de qualidade adaptado (ex.: DARE/CASP ou itens de Kitchenham para estudos primários) aos 37 estudos; reportar a distribuição e discutir o impacto dos 10 preprints e dos 2 de confiança média. Não precisa excluir; basta ponderar/qualificar.
- Critério de aceite: subseção/parágrafo de avaliação de qualidade no Método ou Resultados, com tabela ou síntese por categoria.
- Fonte: extraction-matrix.csv (campo confianca, evidencia).

### IMP-3 (ALTO) Suavizar "validação empírica" da taxonomia [FEITO 2026-05-30: "validação empírica" -> "confronto com a evidência" em abstract, intro, taxonomia, related work e resultados, nas duas línguas]
- Dimensão: Rigor / Clareza (reduz overclaim). Delta esperado: +1 (e remove risco de rejeição). Esforço: baixo.
- Ação: trocar "validada empiricamente" por "confrontada com a evidência do corpus" onde o mapeamento forte/média/fraca é julgado pelo autor; OU formalizar o mapeamento com protocolo de codificação + 2o codificador (aí "validação" se sustenta). Ajustar abstract, introdução, taxonomia e resultados nas DUAS línguas.
- Critério de aceite: termo "validação" só onde houver procedimento de codificação reportado.

### IMP-4 (ALTO) Segunda passada de extração com achados narrativos por estudo [FEITO 2026-05-30: 2a passada sobre o texto completo (pdf-extracts) dos 25; achados reais e resultados empíricos concretos por estudo, com parágrafo de evidência empírica na síntese e limitação de granularidade resolvida; key-findings.md]
- Dimensão: Magnitude (+2) e Rigor (+1). Esforço: alto.
- Ação: adicionar um campo narrativo de key_findings por estudo (hoje ~16 das 37 fichas têm justificativa substantiva; as demais são genéricas). Reforçar a síntese temática com evidência por estudo, reduzindo a dependência da identidade pública dos frameworks.
- Critério de aceite: cada tema citável a fichas com achado narrativo; Limitação de "granularidade da extração de 1a passada" reduzida ou removida.
- Fonte: systematic-review/extracted/*.md.

### IMP-5 (MÉDIO) Saturação do snowballing [FEITO 2026-05-30: figura fig:saturacao (make_saturation_figure.py) + discussão honesta de saturação parcial no Método e Limitações]
- Dimensão: Generalização (+2). Esforço: médio a alto.
- Ação: rodar 1 a 2 rodadas adicionais de snowballing OU apresentar uma análise de saturação (curva de novos incluídos por rodada: 6, 3, 3) argumentando o ponto de corte. Hoje as últimas rodadas ainda adicionavam estudos.
- Critério de aceite: gráfico/curva de saturação OU rodadas extras com a decisão de parada justificada por dados.

### IMP-6 (MÉDIO) Conformidade de relato (PRISMA/Kitchenham checklist) [FEITO 2026-05-30: Apêndice ap:checklist (08_apendice_checklist) nas duas línguas, referenciado no Método]
- Dimensão: Clareza (+1) e Rigor (+1). Esforço: baixo a médio.
- Ação: adicionar um checklist de relato (PRISMA 2020 ou Kitchenham reporting) como apêndice/material suplementar e rotular a figura de fluxo como compatível. Já existe a figura de funil; falta o checklist item a item.
- Critério de aceite: checklist preenchido referenciado no texto.

### IMP-7 (MÉDIO) Ampliar bases/idiomas ou justificar o recorte [FEITO/PARCIAL 2026-05-30: viés quantificado (26/37) + busca suplementar real (arXiv+Crossref, run_supplementary_search.py) como auditoria de completude (revelou 12 estudos no escopo: 5 na janela, 7 pós-corte; screened-inscope.md). Reportado nas Limitações. Re-extração desses 12 para expandir o corpus fica PENDENTE-AUTOR]
- Dimensão: Generalização (+1). Esforço: médio.
- Ação: ou ampliar a busca (mais bases, sem restrição EN/PT) ou fortalecer a justificativa do recorte e discutir explicitamente o viés de publicação a favor de frameworks com resultado positivo.
- Critério de aceite: parágrafo de ameaça à validade externa reforçado com dados.

### IMP-8 (BAIXO) Posicionamento quantitativo vs surveys existentes [FEITO 2026-05-30: diferencial mensurável pela unidade de análise vs Hou et al. e He et al. na Related Work, nas duas línguas]
- Dimensão: Novidade (+1). Esforço: baixo.
- Ação: na Related Work, contrastar numericamente a cobertura/escopo deste paper com Hou et al. e He et al. (ex.: foco por processo vs por tarefa/técnica), deixando o diferencial mensurável.
- Critério de aceite: comparação explícita (tabela ou frase quantitativa) com as revisões âncora.

## 5. Bloqueadores duros para venues top de RSL

Sem IMP-1 e IMP-2, os venues realistic/aspirational de RSL (EMSE, TOSEM, IST no limite) tendem a exigir revisão maior ou rejeitar. Ordem de impacto no aceite: IMP-1 > IMP-2 > IMP-3 > IMP-4. Resolver IMP-1..IMP-4 move o paper da banda "revisão menor com ressalvas" para "competitivo em Q1 de SE".

## 6. Notas para o agente `improve`

- Trabalhe nas DUAS línguas (tex/sections/ e tex/sections-en/) e mantenha paridade.
- Toda nova afirmação numérica deve rastrear a systematic-review/ (CSV/JSON/logs). Zero fabricação.
- Toda citação nova: DOI verificado + `note` com `\href` clicável (regra do projeto).
- Reavaliar com a rubrica da Seção 1; atualizar a Seção 2 e o change log abaixo.
- Não regredir nada da Seção 3.
- Regras globais: sem travessão (U+2014/U+2013), acentuação pt-br correta, sem subseção numerada, figuras [h!], 96 DPI, fonte >= 12pt.

## 7. Change log do score

| Data | Q | Mudança |
|---|---|---|
| 2026-05-30 | 74 | Avaliação inicial após reframe para RSL pura, bilíngue, 5 figuras, DOIs clicáveis. Backlog IMP-1..IMP-8 definido. |
| 2026-05-30 | 85 | Rodada scientex-improve (AUTO + infra dos AUTOR). FEITO: IMP-2, IMP-3, IMP-5, IMP-6, IMP-8. PARCIAL: IMP-1 (infra de IRR, kappa humano pendente), IMP-4 (achado por estudo, texto completo pendente), IMP-7 (viés quantificado, ampliação de bases pendente). Deltas confirmados por re-crítica (paper-critic ciclo 4). latex-validator 0 fatais nas duas línguas; 40/40 citações; 0 citação nova; 0 travessão. |
| 2026-05-30 | 86 | Follow-up autorizado pelo autor: (a) IMP-4 elevado a FEITO via extração de texto completo dos 25 (achados reais + parágrafo de evidência empírica concreta na síntese; Magnitude 11->12); (b) IMP-7 busca suplementar real (arXiv+Crossref) como auditoria de completude: 12 estudos no escopo não capturados pela busca original (5 na janela, 7 pós-corte), reportados com honestidade nas Limitações, sem inflar o corpus (sem re-extração). latex-validator 0 fatais nas duas línguas; 0 citação nova; 0 travessão. Para 90+: IRR humano real + re-extração dos 12 estudos. |
