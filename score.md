# Score, ai-swe-systematic-review-paper

> Análise de viabilidade do paper, para consumo pelo futuro agente `improve`.
> Paper: "From Prompt to Process: A Systematic Review of AI-Assisted Software Development Frameworks"
> Tipo: revisão sistemática de literatura (Kitchenham), bilíngue (pt-br + en), 37 estudos.
> Data da avaliação: 2026-05-30. Avaliador: venue-recommender / paper-critic (SCIENTEX).
> **Score atual (Q): 74 / 100.** **Teto realista após backlog: 88 a 90 / 100.** **Meta: 88.**

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

| Dimensão | Peso | Nota atual | Justificativa (estado em 2026-05-30) |
|---|---|---|---|
| Novidade | 20 | 16 | gap claro (lente de SE sobre frameworks operacionais), posicionado vs Hou et al., He et al., Hassan et al. |
| Rigor | 25 | 16 | protocolo Kitchenham sólido (multibase, 2 passadas, 3 rodadas de snowballing, matriz). FALTA: IRR (kappa), avaliação de qualidade/risco de viés, análise de saturação. |
| Reprodutibilidade | 15 | 13 | protocolo, extraction-matrix.csv, logs de screening, scripts e DOIs públicos no repo. PDFs não redistribuídos (corpus por DOI). |
| Clareza | 15 | 13 | bilíngue, 5 figuras (96 DPI), 3 tabelas, seção de Limitações, figura de fluxo Kitchenham. FALTA: rotular o fluxo como PRISMA/Kitchenham checklist explícito. |
| Magnitude | 15 | 10 | taxonomia testada + 3 eixos de tensão + agenda. Síntese parcialmente apoiada na identidade pública dos frameworks (extração de 1a passada). |
| Generalização | 10 | 6 | 37 estudos, 2022-2026, EN/PT; viés de publicação provável; snowballing pode não ter saturado. |
| **Total** | **100** | **74** | bom artigo de RSL, acima da média, com lacunas metodológicas tratáveis. |

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

### IMP-1 (CRÍTICO) Confiabilidade entre avaliadores (IRR)
- Dimensão: Rigor. Delta esperado: +4 a +5. Esforço: alto (exige 2o avaliador ou protocolo de re-triagem).
- Ação: reaplicar a triagem (título/resumo e texto completo) por um segundo avaliador em uma amostra (ou no todo), calcular Cohen's kappa (ou Krippendorff), reportar o valor e como divergências foram resolvidas. Se 2o avaliador humano não for viável, documentar um protocolo de dupla-checagem reproduzível e reportar a concordância.
- Critério de aceite: kappa reportado no Método com interpretação; objeção nº 1 de revisores de RSL neutralizada.
- Fonte: systematic-review/screening/*.csv (logs de triagem).

### IMP-2 (CRÍTICO) Avaliação de qualidade / risco de viés
- Dimensão: Rigor. Delta esperado: +3 a +4. Esforço: médio.
- Ação: aplicar um checklist de qualidade adaptado (ex.: DARE/CASP ou itens de Kitchenham para estudos primários) aos 37 estudos; reportar a distribuição e discutir o impacto dos 10 preprints e dos 2 de confiança média. Não precisa excluir; basta ponderar/qualificar.
- Critério de aceite: subseção/parágrafo de avaliação de qualidade no Método ou Resultados, com tabela ou síntese por categoria.
- Fonte: extraction-matrix.csv (campo confianca, evidencia).

### IMP-3 (ALTO) Suavizar "validação empírica" da taxonomia
- Dimensão: Rigor / Clareza (reduz overclaim). Delta esperado: +1 (e remove risco de rejeição). Esforço: baixo.
- Ação: trocar "validada empiricamente" por "confrontada com a evidência do corpus" onde o mapeamento forte/média/fraca é julgado pelo autor; OU formalizar o mapeamento com protocolo de codificação + 2o codificador (aí "validação" se sustenta). Ajustar abstract, introdução, taxonomia e resultados nas DUAS línguas.
- Critério de aceite: termo "validação" só onde houver procedimento de codificação reportado.

### IMP-4 (ALTO) Segunda passada de extração com achados narrativos por estudo
- Dimensão: Magnitude (+2) e Rigor (+1). Esforço: alto.
- Ação: adicionar um campo narrativo de key_findings por estudo (hoje ~16 das 37 fichas têm justificativa substantiva; as demais são genéricas). Reforçar a síntese temática com evidência por estudo, reduzindo a dependência da identidade pública dos frameworks.
- Critério de aceite: cada tema citável a fichas com achado narrativo; Limitação de "granularidade da extração de 1a passada" reduzida ou removida.
- Fonte: systematic-review/extracted/*.md.

### IMP-5 (MÉDIO) Saturação do snowballing
- Dimensão: Generalização (+2). Esforço: médio a alto.
- Ação: rodar 1 a 2 rodadas adicionais de snowballing OU apresentar uma análise de saturação (curva de novos incluídos por rodada: 6, 3, 3) argumentando o ponto de corte. Hoje as últimas rodadas ainda adicionavam estudos.
- Critério de aceite: gráfico/curva de saturação OU rodadas extras com a decisão de parada justificada por dados.

### IMP-6 (MÉDIO) Conformidade de relato (PRISMA/Kitchenham checklist)
- Dimensão: Clareza (+1) e Rigor (+1). Esforço: baixo a médio.
- Ação: adicionar um checklist de relato (PRISMA 2020 ou Kitchenham reporting) como apêndice/material suplementar e rotular a figura de fluxo como compatível. Já existe a figura de funil; falta o checklist item a item.
- Critério de aceite: checklist preenchido referenciado no texto.

### IMP-7 (MÉDIO) Ampliar bases/idiomas ou justificar o recorte
- Dimensão: Generalização (+1). Esforço: médio.
- Ação: ou ampliar a busca (mais bases, sem restrição EN/PT) ou fortalecer a justificativa do recorte e discutir explicitamente o viés de publicação a favor de frameworks com resultado positivo.
- Critério de aceite: parágrafo de ameaça à validade externa reforçado com dados.

### IMP-8 (BAIXO) Posicionamento quantitativo vs surveys existentes
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
