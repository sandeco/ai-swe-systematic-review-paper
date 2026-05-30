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
