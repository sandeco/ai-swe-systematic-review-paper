# Log de Revisões do Paper-Critic

Registro do que já foi revisado e aprovado, para que rodadas futuras não re-critiquem seções estáveis nem reabram correções já aplicadas.

O paper-critic lê este arquivo no início de cada rodada. Não re-critique seções marcadas como `✅ APROVADO` nem itens listados como "Correção aplicada", a menos que o autor tenha modificado a seção desde a última revisão.

---

## Seções aprovadas

<!--
Formato:

| Seção | Data da aprovação | Observação |
|---|---|---|
| `\section{Metodologia}` | 2026-06-01 | Sem problemas fatais/graves restantes |
-->

(nenhuma seção aprovada ainda)

---

## Correções aplicadas

### Ciclo 1 (2026-05-30, autonomous-maestro). Veredito: REVISÃO MENOR.

- [2026-05-30] G1 (GRAVE, traceabilidade): distribuição por ano da Tabela 1 seguia synthesis.md (2024:9, 2026:12), mas a autoridade é a extraction-matrix.csv (2024:10, 2026:11). Correção aplicada: tabela e prosa ("doze" para "onze em 2026") agora batem com a matriz. synthesis.md miscontou; o paper segue a matriz (regra 5).
- [2026-05-30] G2 (GRAVE, traceabilidade): "Origem acadêmica/industrial 31/6" não traçava à matriz. Matriz: 19+8+6=33 acadêmico/técnico e 4 indústria. Correção aplicada: tabela agora diz "33 / 4".
- [2026-05-30] M1 (MENOR): roadmap da Introdução omitia Trabalhos Relacionados. Correção aplicada.
- [2026-05-30] M2 (MENOR): Método dizia "(RQ1 a RQ4) acrescidas de uma quinta"; a Introdução já apresenta as 5 RQs. Correção aplicada para "(RQ1 a RQ5)" com explicação de por que a matriz só marca RQ1-4 por estudo.

Confirmados OK no ciclo 1 (não re-criticar sem mudança): citações 40/40 com DOI; natureza 34/1/1/1; empírica 26; repo 22; arXiv 10; confiança média = 2 (Dam2025, JundaHe2025); hedging de overclaim na Discussão adequado; zero travessões; sem subseções numeradas; figuras [h!].

### Ciclo 2 (2026-05-30). Veredito: REVISÃO MENOR.

- [2026-05-30] D1 (MODERADO, fundamentação): Trabalhos Relacionados posicionava a revisão apenas contra duas surveys do corpus (He et al., Hassan et al.); faltava o anchor canônico de revisão de LLM em Engenharia de Software. Correção aplicada: adicionada Hou et al. 2024 (TOSEM, DOI 10.1145/3695988, verificada via CrossRef) ao refs.bib e citada na primeira vertente, reforçando o gap (revisões por tarefa/técnica vs frameworks operacionais por processo).
- Reverificação: 41/41 cite-keys == bib-keys; 0 órfãos; hou2024llmse com DOI confirmado; 0 travessões.

### Ciclo 3 (2026-05-30). Veredito: REVISÃO MENOR.

- [2026-05-30] L1 (MODERADO/GRAVE para SLR, completude): o paper sub-reportava limitações (apenas um parágrafo no Método), enquanto synthesis.md documenta cinco limitações substantivas. Correção aplicada: criada a seção dedicada "Limitações da Revisão" (06b_limitacoes.tex) com os cinco pontos (granularidade da extração de 1a passada; ausência de ponderação por qualidade; recorte de idioma/bases + viés de publicação; pendência operacional fora do corpus; limite de snowballing sem saturação plena). Parágrafo de limitações do Método aparado para evitar redundância e apontar para a nova seção.
- Reverificação: merged doc sem fatais reais (só falso-positivo do caminho da figura em /tmp); 0 travessões; sem subseções numeradas.

## Após 3 ciclos: sem issues FATAL/MAJOR residuais. Não é necessário aviso "REVISÃO HUMANA RECOMENDADA".

### Ciclo 4 (2026-05-30, scientex-improve, re-crítica focada). Veredito: REVISÃO MENOR.

Confirmação dos deltas do backlog do score.md (item a item):
- IMP-2 (avaliação de qualidade): FECHADO. Método descreve checklist de 4 itens (QA1-QA4) por categoria de fonte; Resultados traz Tabela tab:qualidade (alta 11/30%, média 17/46%, baixa 9/24%). Honesto e conservador (deriva de sinais da extração). Resíduo (instrumento de risco de viés por texto completo) declarado na Limitação. Creditável.
- IMP-1 (IRR): PARCIAL-HONESTO. O paper NÃO reivindica kappa de dois humanos; reporta dupla-checagem por protocolo e entrega infra (coding sheets, irr_kit.py, irr-protocol.md). Objeção nº1 de revisor de RSL suavizada, não plenamente neutralizada (sem valor de kappa ainda). Ponto cheio fica AUTOR.
- IMP-3 (overclaim): FECHADO. "validação empírica" -> "confronto com a evidência" em abstract, intro, taxonomia, related work e resultados; codificação pelo autor explicitada. Sem novo overclaim.
- IMP-4 (2a passada narrativa): PARCIAL. Achado narrativo consolidado por estudo (12 substantivos + 25 estruturados, sinalizados); extração de texto completo dos 25 restantes fica como futuro (declarado).
- IMP-5 (saturação): FECHADO. Figura fig:saturacao + discussão honesta de "saturação parcial".
- IMP-7 (viés de publicação): FECHADO. Quantificado (26/37, 70%).
- IMP-6 (checklist Kitchenham): FECHADO. Apêndice ap:checklist nas duas línguas.
- IMP-8 (posicionamento quantitativo): FECHADO. Diferencial mensurável pela unidade de análise vs Hou et al. e He et al., sem fabricar contagens dos surveys.

Sem regressão das forças: gap de SE preservado; RSL pura preservada; 40/40 DOIs intactos; hedging honesto reforçado, não enfraquecido. Paridade pt/en mantida. 0 travessões; 0 fatais de LaTeX; 40/40 cite-keys.

### Ciclo 5 (2026-05-31, scientex-improve, pós-expansão 37->41). Veredito: REVISÃO MENOR.

Expansão do corpus de 37 para 41 (4 estudos peer-reviewed de 2025 via busca suplementar: Tawosi2025/ALMAS, Erten2025/Scrum-AI, Zabardast2025/3-Layer NFR, Chen2025/AutoReview; extração a nível de resumo, confiança média).
- Consistência numérica: PASSA. Verdade-fonte da matriz (n=41): framework 37, empírica 28, repo 22, preprint 10, caso 6, confiança média 6, 2025:15, segurança 26. Todas as contagens no texto (abstract, método, resultados, tabelas, discussão, conclusão, limitações, figuras) batem nas duas línguas. Os "37/25/12" residuais são referências legítimas ao fluxo do protocolo (corpus do protocolo = 37; 25 incluídos pós-2-passadas; 12 do snowballing).
- Integração: 4 novos citados em temas (T1 Tawosi2025+Erten2025; T4 Zabardast2025; T6 Chen2025), na matriz (41 linhas), no refs.bib com DOI verificado (44 entradas, 44 cite-keys, 0 órfãs).
- Honestidade preservada: extração a nível de resumo declarada no Método e Limitações; recall audit reportado (12 achados: 4 incorporados, 1 pendente, 7 pós-corte); funil e figura de saturação atualizados; sem inflar além dos dados.
- Sem regressão: gap de SE, RSL pura, 44 DOIs, hedging honesto, 0 travessão, sem subseção numerada. latex-validator 0 fatais pt+en.

## Após 5 ciclos: sem issues FATAL/MAJOR residuais. Corpus 41. Pendência AUTOR para 90+: IRR humano real (kappa) e expansão completa (7 pós-corte + mais bases).
