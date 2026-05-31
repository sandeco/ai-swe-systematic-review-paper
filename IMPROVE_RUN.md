# Improve run, ai-swe-systematic-review-paper

## Rodada 1, 2026-05-30
- Q antes: 74/100. Meta do autor: >90. Teto honesto desta rodada: ~86/100.
- Escopo escolhido: "AUTO + preparar a infraestrutura dos itens AUTOR".

### Itens executados (FEITO)
- IMP-2 (Rigor, +3): avaliação de qualidade por categoria aplicada aos 37 estudos. Arquivos: systematic-review/make_quality_assessment.py, extracted/quality-assessment.csv, extracted/quality-summary.md; tex/sections{,-en}/02_metodo_revisao.tex, 04_resultados_sintese.tex (Tabela tab:qualidade). Dado-fonte: extraction-matrix.csv (confianca, evidencia). Confirmado por paper-critic: sim. Delta creditado: +3.
- IMP-3 (Rigor/Clareza, +1): overclaim suavizado nas duas línguas (00_resumo, 01_introducao, 03_taxonomia, 03_trabalhos_relacionados, 04_resultados_sintese). Confirmado: sim. Delta: +1.
- IMP-5 (Generalização, +1): curva de saturação. Arquivos: systematic-review/make_saturation_figure.py, figures/snowball_saturation_{pt,en}.{pdf,png}; 02_metodo (fig:saturacao) + 06b_limitacoes. Dado-fonte: snowballing/round-*/summary.md (69/50/30; 6/3/3). Confirmado: sim. Delta: +1.
- IMP-6 (Clareza/Rigor, +1+0.5): checklist de relato Kitchenham. Arquivos: tex/sections{,-en}/08_apendice_checklist.tex, main{,-en}.tex (include), 02_metodo (ref ap:checklist). Confirmado: sim.
- IMP-8 (Novidade, +1): posicionamento quantitativo vs Hou et al. e He et al. (03_trabalhos_relacionados, duas línguas). Confirmado: sim. Delta: +1.

### Itens parciais (PARCIAL; ponto cheio AUTOR)
- IMP-1 (Rigor, +1 de +5): infra de IRR entregue (systematic-review/irr_kit.py, screening/irr/coding-sheet-*.csv, irr-protocol.md) + reporte honesto no Método (dupla-checagem por protocolo). PENDENTE-AUTOR: 2o codificador humano independente para calcular o Cohen kappa real. Confirmado por paper-critic: parcial.
- IMP-4 (Magnitude, +1 de +2): achado narrativo consolidado por estudo (make_key_findings.py -> extracted/key-findings.{md,csv}); 12 substantivos + 25 estruturados. Limitação 1 atualizada. PENDENTE: extração de texto completo, campo a campo, dos 25 restantes. Confirmado: parcial.
- IMP-7 (Generalização, +1): viés de publicação quantificado (26/37) e recorte reforçado (06b_limitacoes, duas línguas). PENDENTE-AUTOR: ampliar busca para bases adicionais / remover restrição de idioma.

### Itens AUTOR pendentes (para cruzar 90)
- IMP-1: precisa de 2o codificador humano. Infra entregue: protocolo + script de kappa + coding sheets pré-preenchidas. Renderia Rigor 21 -> 24 (+3).
- IMP-7 (ampliação real de bases): renderia Generalização 8 -> 9 (+1).
- IMP-4 (texto completo dos 25): renderia Magnitude 11 -> 12/13 (+1 a +2).

### Gates
- latex-validator: APROVADO (pt e en): 0 fatais, 0 refs indefinidas, 40/40 cite-keys, 0 órfãos. Bib: 18 avisos cosméticos pré-existentes (campo volume).
- citation-validator: 0 citação nova introduzida (reuso de chaves já com DOI verificado). Nada a validar.
- Travessão U+2014/U+2013: 0 ocorrências nos arquivos tocados.
- Acentuação pt-br: revisada no texto e nos rótulos das figuras (figuras de dados regeneradas com acento; saturação acentuada).
- Forças (Seção 3 do score.md): nenhuma regrediu (gap de SE, RSL pura, 40 DOIs, hedging honesto, bilíngue, zero travessão, sem subseção).
- Figuras novas: snowball_saturation a 96 DPI, fonte >=12pt, [h!], variantes _pt/_en.

- Q depois: 85/100. Teto honesto sem recurso novo: ~86. Meta 90+ depende dos itens AUTOR acima.

## Rodada 1b (follow-up autorizado pelo autor), 2026-05-30
- Autor autorizou: ampliar bases de busca e extrair texto completo.

### IMP-4 elevado a FEITO (texto completo)
- 2a passada sobre pdf-extracts/*.md dos 25 estudos (5 leitores Explore em paralelo). Achados reais por estudo + resultados empíricos concretos auto-reportados. Arquivos: extracted/key-findings.{md,csv}; novo parágrafo "Evidência empírica reportada pelos estudos" em 04_resultados_sintese (pt+en) com AutoDev 91,5% Pass@1, ASTRA 11-66%, SDD até 50%, SKaruppuchamy 20x deploy, Watfa SEM n=328, Reversa 517 claims (97,1%), SeyedmoeinMohsenimofidi 5% de 10k repos. Limitação de granularidade resolvida (vira ressalva de resultados auto-reportados e heterogêneos). Delta: Magnitude 11 -> 12.

### IMP-7 busca suplementar (auditoria de completude)
- run_supplementary_search.py: arXiv API direta + Crossref com descritores do protocolo; 350 brutos, dedupe vs 234 search-results + matriz + logs. Filtro de escopo + triagem manual: 12 estudos no escopo não capturados pela busca original (5 na janela <=2025; 7 de 2026 no/após o corte). Artefatos: snowballing/supplementary/{raw-*,new-candidates,screened-inscope}.{json,md}. Reportado com honestidade na Limitação "Saturação parcial e recall da busca" (pt+en). NÃO inflou o corpus: os 12 não foram extraídos sob o protocolo congelado, para preservar a integridade da síntese. Expansão real do corpus (re-extração dos 12) fica PENDENTE-AUTOR.

### Gates (follow-up)
- latex-validator: 0 fatais pt+en; 40/40 cite-keys; 0 citação nova; 0 órfãos; 0 travessão.
- Q depois: 86/100 (teto honesto desta rodada atingido). 90+ exige IRR humano real + re-extração dos 12 estudos da busca suplementar.

## Rodada 1c (expansão do corpus, autorizada pelo autor), 2026-05-31
- Autor autorizou expandir o corpus. Recomendação seguida: incorporar só os 5 estudos de 2025 (dentro da janela); 4 viáveis + 1 pendente.

### Estudos incorporados (corpus 37 -> 41)
- Tawosi2025 (ALMAS), Erten2025 (Scrum-AI), Zabardast2025 (3-Layer NFR), Chen2025 (AutoReview). Todos peer-reviewed (IEEE ASEW, IEEE UBMK, ACM FSE), 2025, dentro da janela. DOIs verificados no CrossRef (título/autores conferidos). Extração a nível de resumo (Semantic Scholar/OpenAlex), confiança média, pois nenhum tem PDF aberto.
- MengDocDriven2025: dentro do escopo e da janela, mas sem resumo recuperável -> pendência operacional (não extraído).

### Artefatos e propagação
- refs.bib +4 entradas (@inproceedings com DOI + \href). extraction-matrix.csv 37->41. screening/supplementary.log.csv (5 registros). run_supplementary_search.py + snowballing/supplementary/.
- Figuras regeneradas: methodology (funil com etapa suplementar e corpus 41), snowball_saturation (5a barra +4), data figures e quality (n=41).
- Contagens propagadas nas DUAS línguas em abstract, método, resultados (composição + qualidade + temas + empírica), discussão, conclusão, limitações: framework 37, empírica 28, peer-reviewed 29/71%, qualidade 11/20/10, caso 6, confiança média 6, 2025:15, segurança 26, T5 15%.
- Os 4 novos citados nos temas: T1 (Tawosi2025, Erten2025), T4 (Zabardast2025), T6 (Chen2025) + AutoReview na evidência empírica.

### Gates (expansão)
- latex-validator: 0 fatais pt+en. cross_validate: 44 cite-keys = 44 bib, 0 órfãs. validate_bib: 0 fatais (18 avisos cosméticos pré-existentes). 0 travessão. Consistência numérica e ausência de regressão confirmadas por paper-critic (ciclo 5, REVISÃO MENOR).
- Generalização 8 -> 9. Q depois: 87/100. 90+ exige itens AUTOR (IRR humano, 7 pós-corte + mais bases, texto completo dos abstract-level).
