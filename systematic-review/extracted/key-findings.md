# Achados narrativos por estudo (segunda passada, texto completo)

> Segunda passada de extração sobre o texto completo (pdf-extracts/*.md) dos estudos cuja
> justificativa de inclusão de primeira passada era genérica. Cada achado é fundamentado no
> texto do próprio estudo; resultados numéricos são os reportados pelos autores (auto-reportados,
> em setups heterogêneos e não comparáveis entre si). Sem fabricação.

## Estudos com resultado empírico concreto reportado

- **KumarAle2024**: framework de IA generativa para geração, execução e validação de casos de teste em e-commerce; relata 95% de cobertura de testes, detecção de defeitos 20% superior e 30% de redução no tempo de execução vs métodos tradicionais.
- **MicheleTufano2024 (AutoDev)**: agentes com acesso a compilação, teste e git; relata 91,5% de Pass@1 em geração de código e 87,8% em geração de testes no HumanEval, sem treino adicional.
- **Gadamsetty2025**: relata redução de cerca de 42% no tempo de geração de documentos de software (SRS, SDD) com ligeira queda de qualidade.
- **XiangzheXu2025 (ASTRA)**: red-teaming autônomo espaço-temporal para assistentes de código; relata encontrar de 11% a 66% mais vulnerabilidades que técnicas existentes.
- **DeepakBabuPiskala2026 (SDD)**: trata a especificação como artefato primário e o código como derivado; relata redução de até 50% em erros de código gerado por LLM quando alimentado com especificações humanas refinadas.
- **SKaruppuchamy2026**: blueprint de integração de assistentes LLM com governança multi-camadas no caso "RetailCo"; relata 20x na frequência de deployment, 40% de redução no ciclo, 20% de melhora em defect density e 40% de redução no esforço manual de triagem.
- **Watfa2026 (RARE)**: requisitos cientes de risco com rastreabilidade arquitetural; validação SEM com 328 participantes, cadeia causal significativa (coeficientes β de 0,64 a 0,72).
- **Macedo2026 (Reversa)**: engenharia de documentação reversa multiagente de legado para especificação; estudo exploratório COBOL para Go com 517 claims (97,1% de confiança interna), 53 cenários Gherkin de paridade e 9 de 11 tarefas de reconstrução estruturadas.
- **Paiva2026**: Round-Trip Engineering agêntico (NL para UML) com quatro agentes; relata 5% a 10% de melhora em similaridade semântica com pruning e iteração humana, com modelos menores chegando perto dos maiores após 2 a 3 iterações.
- **SeyedmoeinMohsenimofidi2025**: estudo de adoção de arquivos de contexto de IA (estilo AGENTS.md) em 10.000 repositórios do GitHub; relata adoção em torno de 5%, com forte variação de estrutura.
- **Ulfsnes2024**: estudo empírico com 13 profissionais; relata que assistentes reduzem tempo em tarefas repetitivas mas podem reduzir o compartilhamento de conhecimento na equipe (sem métrica numérica única).
- **Akbar2025**: estudo qualitativo com 21 especialistas sobre IA agêntica no SDLC; 18 de 21 percebem benefício significativo, com desafios de confiança, governança e integração de ferramentas.

## Estudos de proposta/visão sem resultado numérico (contribuição conceitual)

- **Gupta2022 (AIUEF)**: IA e ontologias para avaliar usabilidade de requisitos de interação humano-computador via personas sintéticas.
- **AhmedEHassan2024 (SE 3.0)**: visão de engenharia de software nativa de IA, conversacional e orientada por intenções (Teammate.next, IDE.next, Compiler.next, FM.next).
- **Baron2025**: framework de adoção centrado em confiança, em fase de design, com estudo de caso profissional planejado.
- **Dam2025 (DM-Agents)**: multiagente para design de software que gera UML a partir de linguagem natural e negocia conflitos entre versões de design.
- **LiyiCai2025**: software autoevolutivo multiagente que interpreta requisitos, gera e valida código por cross-validation; viável em quatro cenários.
- **Merchant2025**: integra agentes de código com blockchain para registro imutável e auditoria de ações de agentes.
- **RanjanSapkota2025**: distingue vibe coding de agentic coding e propõe uma taxonomia de autonomia com casos de uso.
- **Alsegier2026**: engenharia de linha de produto centrada em agência, com nove dimensões de variabilidade para sistemas agênticos governados.
- **Anon2026 (DevFlow)**: usa raciocínio de modelo para planejar arquitetura e roteiro de implementação antes de gerar código.
- **BESLEAGA2026 (GABBE)**: arquitetura dual-layer com mais de 30 agentes e inferência ativa para tratar descompasso de velocidade, não determinismo e assimetria de custo.
- **Chechik2026 (AHASE)**: agentes que executam metodologias model-based explícitas para gerar artefatos rastreáveis em vez de soluções black-box.
- **Khan2026**: estudo qualitativo com seis startups sobre toolchain de IA (Copilot, ChatGPT, Fireflies) em fluxo Ágil.
- **Paduraru2026**: asseguramento baseado em traços (Message-Action Traces) com contratos, stress testing e governança em tempo de execução.
