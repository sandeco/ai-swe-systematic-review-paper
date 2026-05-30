# Synthesis, ai-dev-frameworks-review

> Generated on: 2026-05-28 15:05
> Method: thematic (modo hibrido: temas indutivos validados contra a taxonomia de 6 dimensoes)
> Papers synthesized: 37
> Protocol: kitchenham
> Quality assessment: none (sem ponderacao por risco de vies)

## Nota de reconciliacao (RQs e numeracao)

O `protocol.md` congelado define CINCO research questions (RQ1 a RQ5). O `PAPER.md` lista apenas QUATRO perguntas, com texto parcialmente diferente. Esta sintese segue a numeracao do protocolo, que e a autoridade metodologica:

- **RQ1**: dimensoes arquiteturais que distinguem os frameworks.
- **RQ2**: como os frameworks organizam contexto, papeis, artefatos, execucao e validacao.
- **RQ3**: que tipos de evidencia sustentam as alegacoes (empirico, conceitual, documental, repositorio, literatura cinzenta).
- **RQ4**: riscos e limitacoes reportados ou inferiveis (drift, lock-in, seguranca, governanca, rastreabilidade, dependencia de plataforma).
- **RQ5**: lacunas de pesquisa que permanecem para comparar, avaliar e governar esses frameworks em projetos reais.

A RQ5 existe no protocolo mas NAO foi incluida em `PAPER.md`. Recomenda-se reconciliar `PAPER.md` para listar as cinco perguntas. Observe ainda que a matriz de extracao (`extraction-matrix.csv`) e todas as 37 fichas marcam apenas `RQ1, RQ2, RQ3, RQ4` no campo de RQs por estudo. Isso nao e uma lacuna de dados: RQ5 e uma pergunta de nivel de sintese, respondida transversalmente pela secao "Lacunas e implicacoes para pesquisa futura" sobre o corpus inteiro, e nao por tagging estudo a estudo. A cobertura de RQ5 esta concentrada nessa secao.

## Overview

Esta sintese consolida os achados dos 37 estudos incluidos finais da revisao sistematica sobre frameworks de desenvolvimento de software com IA que deslocam a unidade de trabalho do prompt isolado para processos estruturados com artefatos persistentes, papeis agenticos, execucao integrada e validacao. O metodo aplicado e tematico em modo hibrido: primeiro derivamos seis temas indutivamente a partir dos campos estruturados das fichas (artefatos, papeis, execucao, validacao, portabilidade, riscos, natureza e evidencia) e das justificativas de inclusao substantivas; depois mapeamos esses temas contra a taxonomia de seis dimensoes comprometida como contribuicao central do paper (especificacao, contexto, papeis, execucao, validacao, portabilidade), reportando sobreposicoes, dimensoes pouco cobertas e temas emergentes que nao cabem na taxonomia. O objetivo do modo hibrido e validar empiricamente a taxonomia em vez de assumi-la. A sintese responde RQ1 a RQ4 por tema e reserva RQ5 para a secao de lacunas. Nao ha ponderacao por qualidade porque o protocolo fixou `quality_assessment: none`.

## Quantitative summary

| Aspect | N | Notes |
|--------|---|-------|
| Total de estudos incluidos | 37 | Apos screening de duas passadas e 3 rodadas de snowballing |
| Natureza: Framework | 34 | Predominancia quase total da categoria framework |
| Natureza: Arquitetura | 1 | JulesWhite2023 (prompt patterns como arquitetura reutilizavel) |
| Natureza: Plataforma ou IDE | 1 | YuCheng2023 (Prompt Sapper) |
| Natureza: Metodo ou processo | 1 | JSauvola2024 |
| Com avaliacao empirica | 26 | RQ3: maioria reivindica algum grau de validacao empirica |
| Com repositorio publico | 22 | RQ3: rastreabilidade de codigo em mais da metade do corpus |
| Preprint arXiv | 10 | Forte presenca de literatura ainda nao revisada por pares |
| Survey ou revisao | 2 | AhmedEHassan2024, JundaHe2025 |
| Estudo de caso | 5 | Ulfsnes2024, ZeeshanRasheed2024, Baron2025, Khan2026, Macedo2026 |
| Intervalo temporal | 2022 a 2026 | Crescimento marcante a partir de 2024 |
| Distribuicao por ano | 2022:1, 2023:4, 2024:9, 2025:11, 2026:12 | Aceleracao consistente do campo |
| Origem: Academia ou academia tecnica | 31 | Dominio academico |
| Origem: Industria ou pratica profissional | 6 | Ulfsnes2024, YuntongZhang2024, Akbar2025, Watfa2026 e correlatos |
| Confianca de extracao alta | 35 | |
| Confianca de extracao media | 2 | Dam2025, JundaHe2025 |
| Pendencia operacional fora do corpus | 1 | AshaRajbhoj2024, sem PDF local, nao extraido nem sintetizado |

Venues e canais de publicacao mais frequentes: ACM Transactions on Software Engineering and Methodology (5), preprints arXiv (10), seguidos de uma cauda longa de conferencias e periodicos de engenharia de software com 1 a 2 estudos cada (CAIN, AIxSE, ASEW, AutoCodeRover em ASE, IEEE, Elsevier, Springer, SSRN). A dispersao de venues indica um campo emergente sem foro consolidado.

## Synthesis by Theme

Seis temas indutivos emergiram da analise. Juntos cobrem os 37 estudos (cobertura de 100%, acima do alvo de 80%). Cada estudo pode pertencer a mais de um tema. A ordem reflete frequencia decrescente de tema primario.

### T1: Orquestracao multiagente e divisao de papeis

**Definicao**: frameworks que decompoem o ciclo de desenvolvimento entre multiplos agentes ou personas especializados (por exemplo gerente de produto, arquiteto, desenvolvedor, testador, revisor) que colaboram por protocolos de comunicacao, fluxos sequenciais ou enxames.

**Estudos**: ChenQian2023 (ChatDev), SiruiHong2023 (MetaGPT), ZeeshanRasheed2024 (CodePori), MicheleTufano2024 (AutoDev), YuntongZhang2024 (AutoCodeRover), Anon2026 (DevFlow), BESLEAGA2026 (GABBE), Dam2025, Alsegier2026, JundaHe2025, AhmedEHassan2024, Merchant2025, Paduraru2026, SKaruppuchamy2026, Paiva2026, Akbar2025, RanjanSapkota2025, LiyiCai2025.

**Achados consolidados**: este e o tema mais populoso e o eixo arquitetonico dominante do corpus, respondendo diretamente a RQ1. A convergencia central e que a estruturacao do trabalho por papeis distintos, e nao a escolha do modelo de linguagem, e o que diferencia os frameworks. ChatDev codifica uma "chat chain" com fases de design, codificacao, testing e revisao, alem de um mecanismo de "communicative dehallucination". MetaGPT internaliza SOPs (standard operating procedures) de engenharia de software, atribuindo a cada papel artefatos especificos: o product manager gera PRDs, o arquiteto gera design e interfaces, o desenvolvedor implementa. CodePori escala isso para agentes de gerencia, arquitetura, estrutura, desenvolvimento, verificacao e finalizacao. JundaHe2025 (survey) e AhmedEHassan2024 (visao SE 3.0) confirmam que a literatura ja organiza esses sistemas por etapas do SDLC. **Consenso parcial, nao total**: ha tensao clara sobre o grau de autonomia. RanjanSapkota2025 contrasta explicitamente "vibe coding" com "agentic coding", e enquanto CodePori e MetaGPT inclinam-se ao desenvolvimento autonomo de ponta a ponta, outros desenhos preservam pontos de decisao humana. Limitacao compartilhada: a maioria avalia em benchmarks de geracao de codigo ou tarefas controladas, e a confiabilidade e o overhead de coordenacao aparecem como riscos recorrentes neste tema.

### T2: Especificacao e contrato como artefato central

**Definicao**: frameworks que colocam um artefato de especificacao persistente (spec, PRD, contrato, criterio de aceitacao, requisito estruturado) como fonte de verdade que dirige e restringe a geracao de codigo.

**Estudos**: DeepakBabuPiskala2026 (Spec-Driven Development), Macedo2026 (Reversa), SaiZhang2025 (AgileGen), SiruiHong2023 (MetaGPT, via PRDs), Watfa2026 (Risk-Aware Requirements Engineering), Paduraru2026 (Trace-Based Assurance, via contratos), RanjanSapkota2025, BESLEAGA2026, Gadamsetty2025, Gupta2022, MitulModi2024, Khan2026.

**Achados consolidados**: este tema responde RQ1 e RQ2 e materializa a tese central do paper de que a especificacao se torna a unidade de coordenacao. DeepakBabuPiskala2026 formaliza o spec-driven development como passagem "do codigo ao contrato", tratando a spec como artefato versionavel. SaiZhang2025 (AgileGen) usa criterios de aceitacao em Gherkin como contrato executavel e mantem memoria e iteracao ate a validacao. **Contradicao produtiva**: ha duas direcoes opostas de fluxo da especificacao. A maioria assume spec-first (a spec precede e gera o codigo, como em SDD, MetaGPT e AgileGen), enquanto Macedo2026 (Reversa) inverte o fluxo, recuperando especificacoes operacionais a partir de codigo legado para alimentar agentes. Essa oposicao spec-first versus spec-recovered e um achado de diferenciacao relevante para a matriz comparativa. Watfa2026 adiciona engenharia de requisitos consciente de risco, ligando a especificacao a governanca. O drift entre especificacao e codigo, hipotese de risco central do paper, e nomeado explicitamente como risco em DeepakBabuPiskala2026, Paduraru2026, Watfa2026 e YuCheng2023.

### T3: Engenharia de contexto e recuperacao de conhecimento do repositorio

**Definicao**: frameworks cujo diferencial e como capturam, estruturam e injetam contexto (codigo existente, documentacao, memoria de execucao) para que os agentes operem sobre projetos reais e nao apenas em prompts isolados.

**Estudos**: SeyedmoeinMohsenimofidi2025 (Context Engineering), YuntongZhang2024 (AutoCodeRover, recuperacao estrutural de contexto), AhmedEHassan2024 (SE 3.0), LiyiCai2025 (self-evolving software), Macedo2026 (Reversa), SaiZhang2025 (memoria), Chechik2026, Paiva2026 (sincronizacao de artefatos multimodais).

**Achados consolidados**: responde RQ2 com foco na dimensao de contexto. SeyedmoeinMohsenimofidi2025 trata a engenharia de contexto como disciplina propria para agentes em software open source. AutoCodeRover demonstra que a recuperacao estrutural de contexto no codigo (busca por programa, nao apenas embedding textual) melhora a geracao de patches. Paiva2026 (Agentic RTE) aborda a sincronizacao de artefatos multimodais, isto e, manter coerencia entre artefatos heterogeneos ao longo do ciclo. LiyiCai2025 leva o tema ao extremo do software autoevolutivo. **Tensao a registrar**: a visao de software autoevolutivo de LiyiCai2025 esta em tensao com a enfase em rastreabilidade e contrato dos temas T2 e T4; quanto mais o software se modifica autonomamente, mais dificil e ancorar cada mudanca em uma especificacao auditavel. O risco "contexto" e o mais frequente do corpus inteiro, presente em quase todos os estudos, o que sugere que a janela e a fidelidade de contexto sao o gargalo pratico transversal.

### T4: Validacao, rastreabilidade, asseguramento e governanca

**Definicao**: frameworks centrados em mecanismos de garantia: gates, testes automatizados, traces e auditoria, contratos ou politicas, revisao humana obrigatoria, com enfase em rastreabilidade e governanca do trabalho agentico.

**Estudos**: Paduraru2026 (Trace-Based Assurance), Merchant2025 (colaboracao verificavel via blockchain), Alsegier2026 (variabilidade de agencia governada, product-line), SKaruppuchamy2026, Watfa2026, BESLEAGA2026, Chechik2026, Reversa (Macedo2026), MitulModi2024, Ulfsnes2024, Akbar2025, Baron2025, KRRaghi2024, Gupta2022, KumarAle2024.

**Achados consolidados**: responde RQ2 (dimensao validacao) e RQ4 (riscos de governanca e rastreabilidade). Quase todo o corpus declara algum mecanismo de validacao, mas este tema agrupa os estudos para os quais a validacao e o ponto central, e nao um apendice. Paduraru2026 propoe asseguramento baseado em traces com contratos, testing e governanca. Merchant2025 usa blockchain para tornar verificavel a colaboracao entre assistentes agenticos, registrando atos no fluxo. Alsegier2026 importa engenharia de linha de produto para governar a variabilidade de agencia. **Consenso forte**: rastreabilidade e auditoria de trace aparecem como requisito recorrente para confiar em agentes em projetos reais (Paduraru2026, Merchant2025, Reversa, SKaruppuchamy2026, Watfa2026, Chechik2026, Anon2026). **Contradicao de custo**: ha um eixo de tensao entre cerimonia pesada de governanca (Merchant2025 com blockchain, Paduraru2026 com contratos formais) e agilidade leve (Khan2026 para startups, vibe coding em RanjanSapkota2025, prompt patterns em JulesWhite2023). O overhead e nomeado como risco em boa parte deste grupo, o que materializa a tensao governanca versus produtividade que a agenda de pesquisa do paper deve enderecar.

### T5: Colaboracao humano-IA, adocao e confianca (tema emergente)

**Definicao**: estudos cujo foco primario nao e a arquitetura tecnica do framework, mas a integracao da IA no trabalho humano: fluxos de colaboracao, fatores de adocao organizacional, construcao de confianca e impacto sociotecnico.

**Estudos**: DanielRusso2024 (Human-AI Collaboration and Adaptation Framework), Ulfsnes2024 (insights empiricos sobre colaboracao e workflow), Baron2025 (adocao e confianca), Khan2026 (toolchain para startups), JSauvola2024 (cenarios futuros de operacao com IA), Akbar2025 (perspectivas de praticantes ao longo do SDLC).

**Achados consolidados**: responde RQ2 parcialmente e RQ4 pelo angulo humano. DanielRusso2024 propoe e valida um framework de colaboracao e adaptacao humano-IA, modelando fatores de workflow e estrategias organizacionais. Ulfsnes2024 e Akbar2025 trazem evidencia empirica de campo (estudo de caso e perspectivas de praticantes) sobre como equipes reais reorganizam colaboracao e fluxo. Baron2025 centra-se em fomentar confianca como precondicao de adocao. **Achado emergente importante**: este tema NAO cabe limpo em nenhuma das seis dimensoes da taxonomia. As seis dimensoes (especificacao, contexto, papeis, execucao, validacao, portabilidade) sao todas tecnico-arquiteturais; a dimensao humana, organizacional e de confianca atravessa o corpus mas nao tem casa na taxonomia atual. Seis estudos (16% do corpus) tem este como foco primario, o que e material o bastante para recomendar uma extensao da taxonomia (ver Cross-cutting findings). Nao foram dobrados a forca em "papeis", que no corpus designa papeis de agentes de software, nao papeis humanos organizacionais.

### T6: Seguranca, robustez e red-teaming (tema emergente)

**Definicao**: estudos cujo foco e a seguranca do codigo e do comportamento agentico: red-teaming, deteccao de vulnerabilidades, robustez adversarial e mitigacao de alucinacao com impacto de seguranca.

**Estudos**: XiangzheXu2025 (ASTRA, red-teaming autonomo), Watfa2026 (engenharia de requisitos consciente de risco), RanjanSapkota2025 (implicacoes de seguranca do agentic coding), ChenQian2023 (communicative dehallucination), Merchant2025 (verificabilidade), BESLEAGA2026.

**Achados consolidados**: responde RQ4 diretamente. XiangzheXu2025 (ASTRA) propoe red-teaming espaco-temporal autonomo para assistentes de software com IA, tratando seguranca como atividade ativa e nao como propriedade assumida. O risco "seguranca" e o segundo mais frequente do corpus. **Achado emergente**: assim como T5, este tema so se conecta parcialmente as seis dimensoes. Seguranca aparece quase sempre como risco a mitigar (campo de riscos), raramente como dimensao de projeto positiva embutida na arquitetura do framework. ASTRA e a excecao que faz da seguranca o objeto central. Isso sugere que seguranca e mais um eixo de avaliacao transversal do que uma das dimensoes arquiteturais que classificam frameworks, mas sua frequencia justifica trata-la explicitamente, possivelmente como subdimensao de validacao ou como criterio independente da matriz comparativa.

### Cobertura dos temas

Todos os 37 estudos foram atribuidos a pelo menos um tema (cobertura 100%). T1 (orquestracao multiagente) e T4 (validacao e governanca) sao os mais densos; T5 e T6 sao menores mas decisivos por serem emergentes fora da taxonomia.

## Mapeamento hibrido: temas indutivos contra a taxonomia de 6 dimensoes

A tabela cruzada abaixo marca a forca da relacao entre cada tema indutivo e cada dimensao planejada da taxonomia. Legenda: forte (a dimensao e o eixo do tema), media (a dimensao aparece de forma relevante), fraca (toque marginal), ausente (sem relacao significativa).

| Tema indutivo | Especificacao | Contexto | Papeis | Execucao | Validacao | Portabilidade |
|---|---|---|---|---|---|---|
| T1 Orquestracao multiagente | media | media | forte | forte | media | fraca |
| T2 Especificacao e contrato | forte | media | fraca | media | forte | fraca |
| T3 Engenharia de contexto | fraca | forte | fraca | media | fraca | fraca |
| T4 Validacao, trace e governanca | media | fraca | fraca | media | forte | fraca |
| T5 Colaboracao humano-IA e adocao | fraca | fraca | fraca | fraca | fraca | ausente |
| T6 Seguranca e red-teaming | fraca | fraca | fraca | media | media | ausente |

Leitura do mapeamento:

- **Dimensoes bem cobertas pelos dados**: *papeis* e *execucao* (ancoradas em T1), *especificacao* e *validacao* (ancoradas em T2 e T4), *contexto* (ancorado em T3). Cinco das seis dimensoes recebem suporte empirico forte de pelo menos um tema. A taxonomia, nessa parte, e empiricamente validada.
- **Dimensao pouco coberta**: *portabilidade* nao recebe relacao "forte" de nenhum tema e e "ausente" em dois. Nos dados, portabilidade aparece quase sempre pelo lado negativo, como risco de lock-in e de dependencia de IDE, modelo comercial ou plataforma (campo de portabilidade das fichas registra dependencia de IDE ou ambiente em praticamente todos os 37 estudos, e dependencia possivel de LLM comercial em cerca de metade). Quase nenhum framework trata portabilidade como propriedade de projeto positiva e deliberada. Lock-in como risco explicito so aparece nomeado em SeyedmoeinMohsenimofidi2025. Conclusao: portabilidade e a dimensao mais fraca da taxonomia quando confrontada com a evidencia, e deve ser apresentada no paper como dimensao predominantemente diagnostica (risco) e nao como diferenciador positivo entre frameworks.
- **Temas fora da taxonomia (emergentes)**: T5 (colaboracao humano-IA, adocao, confianca) e T6 (seguranca e red-teaming) nao tem casa clara nas seis dimensoes. T5 cobre o eixo humano e organizacional; T6 cobre o eixo de seguranca, que no corpus e majoritariamente risco e nao dimensao de projeto. Ambos sao recomendacoes concretas de extensao da taxonomia, detalhadas em Cross-cutting findings. A regra do modo hibrido foi respeitada: esses temas nao foram forcados nas dimensoes existentes.

## Tabela cruzada: temas indutivos contra RQs

| Tema indutivo | RQ1 (dimensoes) | RQ2 (organizacao) | RQ3 (evidencia) | RQ4 (riscos) | RQ5 (lacunas) |
|---|---|---|---|---|---|
| T1 Orquestracao multiagente | sim | sim | sim | sim | via sintese |
| T2 Especificacao e contrato | sim | sim | parcial | sim | via sintese |
| T3 Engenharia de contexto | sim | sim | parcial | sim | via sintese |
| T4 Validacao, trace e governanca | parcial | sim | sim | sim | via sintese |
| T5 Colaboracao humano-IA e adocao | parcial | sim | sim | sim | via sintese |
| T6 Seguranca e red-teaming | nao | parcial | sim | sim | via sintese |

RQ5 nao tem coluna de tagging por estudo porque e meta-pergunta respondida pela secao "Lacunas e implicacoes" sobre o corpus inteiro, conforme a nota de reconciliacao.

## Cross-cutting findings

Achados que atravessam multiplos temas e RQs:

- **A unidade de trabalho deslocou-se do prompt para o processo, e a tese central do paper se sustenta empiricamente.** Em 34 dos 37 estudos a contribuicao e descrita como framework, e os campos de artefatos persistentes (specs, PRDs, tarefas, logs), papeis e validacao estao presentes na esmagadora maioria. O modelo de linguagem raramente e o diferenciador declarado; a estrutura de processo e.

- **A taxonomia de seis dimensoes e parcialmente validada e parcialmente desafiada.** Cinco dimensoes (especificacao, contexto, papeis, execucao, validacao) tem ancoragem empirica forte. A sexta, portabilidade, e fraca e quase sempre diagnostica (risco), nao diferencial positivo. Alem disso, dois eixos relevantes emergem fora das seis dimensoes: o humano-organizacional (T5) e o de seguranca (T6). Recomendacao concreta: considerar estender a taxonomia com uma dimensao de "colaboracao e governanca humano-IA" e tratar "seguranca" como criterio de avaliacao transversal ou subdimensao de validacao. Esta e a contribuicao analitica central do modo hibrido.

- **Tres eixos de tensao recorrentes (consenso parcial, nao consenso):**
  1. Autonomia versus controle humano. CodePori, MetaGPT e ChatDev inclinam-se ao fluxo autonomo de ponta a ponta; AgileGen, DanielRusso2024 e Baron2025 inserem decisao e confianca humanas como elementos de projeto; RanjanSapkota2025 teoriza o contraste vibe versus agentic.
  2. Governanca pesada versus agilidade leve. Merchant2025 (blockchain) e Paduraru2026 (contratos formais) versus Khan2026 (startups), JulesWhite2023 (prompt patterns) e vibe coding. O overhead e o preco recorrente da governanca.
  3. Fluxo da especificacao: spec-first (SDD, MetaGPT, AgileGen) versus spec-recovered de legado (Reversa). Os dois ancoram-se na mesma dimensao de especificacao mas com direcoes opostas, o que e material para a matriz comparativa.

- **Rastreabilidade e contexto sao os dois requisitos transversais mais citados.** O risco "contexto" aparece em quase todos os estudos e a rastreabilidade e demanda recorrente nos temas T2 e T4. Juntos, indicam que os gargalos praticos do campo nao sao a geracao de codigo em si, mas manter o agente ancorado no projeto real e auditavel ao longo do tempo.

- **A evidencia e desigual (RQ3).** Embora 26 dos 37 estudos declarem avaliacao empirica e 22 tenham repositorio publico, 10 sao preprints arXiv ainda nao revisados por pares e a maioria das avaliacoes ocorre em benchmarks ou estudos de caso pontuais, nao em projetos industriais longitudinais. A forca da evidencia varia muito por categoria de fonte, exatamente como o protocolo antecipou ao classificar evidencia por categoria em vez de aplicar exclusao por qualidade.

## Lacunas e implicacoes para pesquisa futura (resposta a RQ5)

- **Ausencia de benchmarks orientados a processo.** A avaliacao do corpus concentra-se no resultado final (codigo gerado, taxa de resolucao de issues), nao na qualidade do processo: aderencia da implementacao a especificacao, taxa de drift, custo de coordenacao entre agentes, qualidade dos artefatos intermediarios. Nenhum estudo propoe um benchmark padronizado de processo. Estudo futuro indicado: definir metricas e datasets que avaliem o pipeline, nao so a solucao.

- **Falta de comparacao empirica direta entre frameworks.** Cada estudo avalia seu proprio framework isoladamente. Nao ha estudo comparativo controlado que confronte, por exemplo, ChatDev, MetaGPT e AgileGen na mesma tarefa com as mesmas metricas. Isso bloqueia conclusoes sobre qual estrutura de processo funciona melhor sob quais condicoes. Estudo futuro: experimentos comparativos head-to-head com protocolos comuns.

- **Portabilidade e lock-in pouco estudados como objeto, muito presentes como risco.** Dependencia de IDE, plataforma e modelo comercial e quase universal nas fichas, mas apenas SeyedmoeinMohsenimofidi2025 nomeia lock-in explicitamente e nenhum estudo mede portabilidade de forma sistematica. Estudo futuro: instrumentos para medir acoplamento a fornecedor e custo de migracao entre plataformas agenticas.

- **Governanca e rastreabilidade carecem de validacao em escala real.** Propostas de trace, contrato e auditoria (Paduraru2026, Merchant2025, Watfa2026, Reversa) sao promissoras mas validadas em estudos de caso ou prototipos, nao em organizacoes ao longo do tempo. Falta tambem analise de custo-beneficio do overhead de governanca. Estudo futuro: avaliacao longitudinal de regimes de governanca em equipes reais.

- **A dimensao humana e de adocao esta sub-representada na taxonomia tecnica.** O tema emergente T5 mostra que colaboracao, confianca e adocao organizacional sao decisivos, mas a taxonomia de seis dimensoes nao os contempla. Estudo futuro: integrar uma camada sociotecnica a classificacao de frameworks e estudar fatores de adocao em campo.

- **Seguranca tratada reativamente.** Exceto ASTRA (XiangzheXu2025), seguranca aparece como risco a mitigar e nao como propriedade de projeto avaliada. Falta avaliacao sistematica de superficie de ataque de frameworks agenticos, em especial de extensoes, skills e plugins comunitarios. Estudo futuro: framework de avaliacao de seguranca especifico para pipelines de desenvolvimento agentico.

## Limitacoes da revisao

- **Granularidade da extracao de primeira passada.** A sintese tematica foi derivada predominantemente dos campos estruturados das fichas (artefatos, papeis, execucao, validacao, portabilidade, riscos, natureza, evidencia) somados a cerca de 16 justificativas de inclusao substantivas; as 21 fichas restantes trazem justificativa de inclusao generica ("texto completo confirma fonte dentro do escopo"), pois a primeira passada de extracao nao capturou um campo narrativo de key_findings por estudo. Os temas e os achados foram, portanto, complementados pela identidade publica conhecida de frameworks bem documentados (por exemplo ChatDev, MetaGPT, AutoCodeRover, Reversa, SDD, AgileGen, ASTRA). Uma segunda passada de extracao com campo de achados narrativos por estudo aumentaria a profundidade da sintese e e recomendada antes da redacao final da secao de Discussao.

- **Sem ponderacao por qualidade.** O protocolo fixou `quality_assessment: none`. Assim, achados de preprints arXiv nao revisados por pares (10 estudos) e de estudos com confianca de extracao media (2) entram com o mesmo peso nominal dos revisados por pares. A forca da evidencia e qualificada qualitativamente por categoria de fonte na sintese, mas nao ha exclusao nem ponderacao formal por risco de vies.

- **Recorte de idioma e de bases.** O protocolo restringe a ingles e portugues, no periodo 2018 a 2026. A busca direta no arXiv falhou em parte por timeout ou HTTP 429, com cobertura de preprints recuperada via Semantic Scholar e DOI arXiv, o que pode ter deixado de fora preprints muito recentes nao indexados nessas rotas. Vies de publicacao a favor de frameworks com resultados positivos e provavel, dado que estudos negativos ou de falha de adocao sao raros no corpus.

- **Pendencia operacional fora do corpus.** O estudo `AshaRajbhoj2024` foi incluido por titulo e abstract mas nao teve o PDF obtido localmente, ficando fora da extracao e desta sintese. O corpus efetivamente sintetizado e de 37 estudos; a inclusao tardia de `AshaRajbhoj2024` poderia ajustar contagens marginais, sem alterar a estrutura tematica.

- **Limite de snowballing.** O snowballing foi encerrado no limite protocolar de 3 rodadas. As ultimas rodadas ainda adicionavam incluidos finais (3 na rodada 2 e 3 na rodada 3), o que sugere que o corpus pode nao ter atingido saturacao completa; rodadas adicionais poderiam revelar estudos relevantes, em especial fora das comunidades de origem dos seeds.
