# Autonomous Run, ai-swe-systematic-review-paper

> Comando: /scientex-autonomous quero agora que vc conclua o artigo de ai-swe-systematic-review-paper
> Iniciado em: 2026-05-30
> Coordenador: autonomous-maestro (executado no main loop pelo Maestro)
> Modo: AUTONOMO (zero checkpoints)
> Instrucao extra do autor: ao concluir, humanizar e traduzir para o ingles.

## Parametros resolvidos
- Tipo solicitado: systematic-review (paper ja existente, em fase de redacao final)
- Tipo efetivo: systematic-review (downgrade: nao)
- Tema: revisao sistematica de frameworks de desenvolvimento de software com IA (corpus de 37 estudos)
- Slug: ai-swe-systematic-review
- Venue: arXiv (preprint), cs.SE (cross-list cs.AI). Origem: PAPER.md (ja definido pelo autor).
- Fonte: literatura real (37 estudos, DOIs verificados; pipeline systematic-review concluido ate a sintese)
- Idioma de redacao: pt-br; entrega final traduzida para ingles + humanizada (pedido do autor)

## Decisoes automaticas (substituem checkpoints)
| Timestamp | Fase | Decisao | Justificativa |
|-----------|------|---------|---------------|
| 2026-05-30 | Setup | Reconstruir refs.bib a partir da extraction-matrix.csv (37 DOIs reais) + 3 refs metodologicas; descartar os @misc de docs dos frameworks-irmaos e entradas grey-lit sem DOI | As secoes herdadas citavam chaves do paper irmao (BMAD/Spec Kit/Antigravity) e a synthesis usa as chaves do corpus (ChenQian2023 etc.); alinhar tudo as chaves do corpus com DOI atende ao gate de citacao (tolerancia zero a citacao sem DOI). |
| 2026-05-30 | Framing | Manter 02_metodo_revisao.tex (PRONTO/herdado) e enquadrar o restante do paper em torno do corpus de 37 estudos como objeto primario; taxonomia validada empiricamente contra o corpus | PAPER.md define este recorte como a revisao formal dos 37 estudos; a figura da metodologia ja carrega as contagens reais do funil. |
| 2026-05-30 | RQs | Adotar as 5 RQs do protocol.md (autoridade), reconciliando o PAPER.md antigo que listava 4 | A synthesis.md e o protocol.md fixam 5 RQs; RQ5 e respondida transversalmente na Agenda. |
| 2026-05-30 | Gap (Fase 2) | Gap escolhido (maior confianca): ausencia de uma revisao com lente de Engenharia de Software focada em frameworks operacionais que deslocam a unidade de trabalho do prompt para o processo, com taxonomia validada empiricamente | Deriva direto da synthesis (Cross-cutting) e do recorte do PAPER.md; pipeline ja concluido sustenta o gap com evidencia real. |

## Gap escolhido
- Gap: lente de Engenharia de Software, ausente nas revisoes existentes (focadas em arquitetura de agentes abstrata ou em tarefas isoladas do SDLC), para caracterizar frameworks operacionais que estruturam o processo de desenvolvimento com IA; taxonomia de 6 dimensoes validada contra o corpus. | Confianca: HIGH | Score: pipeline concluido (37 estudos, cobertura 100% dos temas)
- Gaps descartados: comparacao de produtos dos 6 frameworks de apoio (foi para o paper irmao dev-agent-frameworks-review-paper).

## Paper-critic (3 ciclos critica->correcao)
| Ciclo | Veredito | Issues FATAL/MAJOR/MINOR | Correcoes aplicadas neste ciclo |
|-------|----------|--------------------------|---------------------------------|
| 1 | REVISAO MENOR | 0 FATAL / 2 GRAVE / 2 MENOR | G1: ano 2024:9->10, 2026:12->11 (tabela seguia synthesis.md mas a autoridade e a extraction-matrix.csv) + prosa "doze"->"onze". G2: origem "31/6"->"33/4" (19+8+6 academico/tecnico, 4 industria). M1: roadmap da Introducao incluiu Trabalhos Relacionados. M2: Metodo "(RQ1 a RQ4)"->"(RQ1 a RQ5)". |
| 2 | REVISAO MENOR | 0 FATAL / 0 GRAVE / 1 MODERADO | D1: Related Work fino; adicionada Hou et al. 2024 (TOSEM, DOI 10.1145/3695988, verificada via CrossRef) como anchor de revisao LLM4SE e citada. |
| 3 | REVISAO MENOR | 0 FATAL / 1 MODERADO-GRAVE-para-SLR | L1: criada secao dedicada "Limitacoes da Revisao" (5 pontos da synthesis); paragrafo de limitacoes do Metodo aparado para apontar a nova secao. |

Apos os 3 ciclos: ZERO issues FATAL/MAJOR residuais. Veredito final: REVISAO MENOR (solido). Sem aviso "REVISAO HUMANA RECOMENDADA".

## Validacao de citacoes (loop ate 100% limpo)
| Iteracao | VERIFICADAS | INCERTAS | NAO ENCONTRADAS | Acao (trocada/removida + chave) |
|----------|-------------|----------|-----------------|---------------------------------|
| 1 (automatica, CrossRef/DataCite/S2) | 39 | 0 | 1 (Macedo2026, falso-negativo) | Macedo2026 reverificada manualmente: arXiv 2605.18684 resolve com titulo/autores exatos (submetida 2026-05-18, 12 dias atras). Falso-negativo do lookup automatico porque DataCite/S2 ainda nao indexaram preprint tao recente. Mantida como preprint arXiv legitimo (DOI arXiv canonico). |
| 2 (final) | 40 | 0 | 0 | Gate PASSA. Todas as \cite apontam para entradas com DOI confirmado; 10 preprints arXiv marcados como `Preprint, arXiv`. |

Detalhe: 39/40 confirmadas via CrossRef ou Semantic Scholar (titulo casa). A 40a (Macedo2026, Reversa, paper do proprio autor) confirmada via pagina arXiv (abs/2605.18684) com titulo e autores exatos. Cobertura de fontes: CrossRef (29), Semantic Scholar (8), arXiv (1) + 3 refs metodologicas classicas (Kitchenham, Garousi, Wohlin) via CrossRef.

## Gate de validacao (resultado final)
- Consistencia: PASS (40 cite-keys == 40 bib-keys, zero orfaos) | BibTeX: PASS (0 FATAL; 17 avisos soft de `volume` ausente, aceitaveis para preprint; todos com DOI) | Citacoes: PASS (40/40 VERIFICADAS, 0 alucinadas) | Figuras: herdada (methodology.{pdf,png,svg}, ja em 96 DPI)
- Stats: n/a (revisao, sem experimento proprio) | Compliance: arXiv preprint OK | GenAI policy: declaracao canonica no main.tex (ingles, single-author) | Travessoes (U+2014/U+2013): 0 ocorrencias

## Traducao e humanizacao (pedido do autor)
- Traducao pt-br -> ingles: todas as 10 secoes + titulo + abstract + keywords; babel brazil->english. Sem residuo de portugues na prosa; secao titles em ingles.
- Figura da metodologia regenerada em ingles (make_methodology_figure_en.py) a 96 DPI (regra 13) e fontes >=12pt (regra 12); contagens batem com o Metodo (100->85->28->25->+12->37; exclusoes 57, 3).
- Humanizacao (skill humanizer): alvo voz Ng/Rajpurkar de reference_authors/. Burstiness media 24,6->23,8; longas 30%->27%; +7 frases. Zero palavra-fetiche / conectivo-clichê. \cite (41), numeros e fatos preservados; veredito do contrato de preservacao: OK.
- Re-gate pos-traducao/humanizacao: 0 travessao; cross_validate 41 citadas / 0 faltando / 0 orfa; validate_bib 0 FATAL; merged doc sem fatais reais.

## Publicacao
- Repositorio: (pendente) | Commit: (pendente) | Push: (pendente)

## Revisao humana recomendada
- (a preencher ao final)
