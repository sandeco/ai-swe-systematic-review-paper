# Protocolo de Revisao Sistematica

> Paper: **Do Prompt ao Processo: uma Revisao de Frameworks de Desenvolvimento de Software com IA**
> Slug: `ai-dev-frameworks-review`
> Protocolo aplicado: `kitchenham`
> Data de fixacao: 2026-05-27
> Status: **CONGELADO**, alteracoes pos-fixacao exigem registro em "Emendas" abaixo.

## 1. PICO/PICOC

- **Population**: frameworks, metodos, toolkits, IDEs, CLIs, kits comunitarios e plataformas que organizam atividades de desenvolvimento de software com IA.
- **Intervention**: uso de processos estruturados com artefatos persistentes, especificacoes, planos, tarefas, contexto, agentes, personas, skills, workflows, validacoes, testes, revisao humana ou integracao com IDE, terminal, navegador e repositorios.
- **Comparison**: uso de prompts isolados, assistentes genericos de codigo sem workflow proprio e abordagens tradicionais de desenvolvimento sem camada agentica ou sem artefatos persistentes de coordenacao.
- **Outcome**: taxonomia de dimensoes arquiteturais, matriz comparativa, identificacao de riscos praticos, lacunas empiricas e agenda de pesquisa para avaliacao e governanca desses frameworks.
- **Context**: engenharia de software, desenvolvimento assistido por IA, agentic software engineering, spec-driven development, projetos open source, ambientes industriais quando documentados, documentacao oficial, literatura academica e literatura cinzenta tecnicamente verificavel.

## 2. Research Questions

- **RQ1**: Quais dimensoes arquiteturais distinguem frameworks de desenvolvimento de software com IA que organizam trabalho por processos, artefatos persistentes, agentes ou workflows?
- **RQ2**: Como os frameworks identificados organizam contexto, papeis, artefatos, execucao e validacao durante o ciclo de desenvolvimento de software?
- **RQ3**: Que tipos de evidencia sustentam as alegacoes desses frameworks, distinguindo estudos empiricos, papers conceituais, documentacao oficial, repositorios publicos e literatura cinzenta?
- **RQ4**: Quais riscos e limitacoes sao reportados ou inferiveis a partir das fontes, incluindo drift entre especificacao e codigo, lock-in, seguranca de extensoes, governanca, rastreabilidade e dependencia de plataforma?
- **RQ5**: Que lacunas de pesquisa permanecem para comparar, avaliar e governar frameworks de desenvolvimento com IA em projetos reais?

## 3. Criterios de inclusao

| # | Criterio | Tipo |
|---|----------|------|
| I1 | A fonte descreve um framework, metodo, toolkit, plataforma, IDE, CLI ou kit que organiza desenvolvimento de software com IA em mais de uma etapa. | individual |
| I2 | A fonte descreve producao ou consumo de artefatos persistentes, como especificacoes, planos, PRDs, tarefas, stories, contexto, logs, evidencias ou checklists. | agregado |
| I3 | A fonte define papeis, agentes, personas, skills, workflows, comandos ou mecanismos equivalentes de coordenacao. | agregado |
| I4 | A fonte descreve integracao com execucao de codigo, testes, terminal, IDE, navegador, repositorios ou pipelines de validacao. | agregado |
| I5 | A fonte e academica, oficial, comunitaria tecnicamente verificavel ou literatura cinzenta com autoria, data e criterios rastreaveis. | individual |
| I6 | A fonte esta disponivel em ingles ou portugues. | individual |
| I7 | A fonte foi publicada, disponibilizada ou atualizada entre 2018 e 2026. | individual |
| I8 | A fonte permite extrair pelo menos quatro campos do esquema de extracao definido para a revisao. | individual |

Regra agregada: fontes que nao satisfazem I1 devem ser excluidas. Para fontes que satisfazem I1, incluir quando pelo menos dois entre I2, I3 e I4 tambem forem satisfeitos.

## 4. Criterios de exclusao

| # | Criterio | Tipo |
|---|----------|------|
| E1 | A fonte trata apenas de modelos de linguagem, APIs ou benchmarks de codigo sem camada de processo, workflow ou framework de desenvolvimento. | individual |
| E2 | A fonte descreve assistente de codigo generico sem artefatos persistentes, papeis, comandos, workflow ou validacao propria. | individual |
| E3 | A fonte discute LLMs para uma unica tarefa isolada de engenharia de software sem proposta de framework ou processo. | individual |
| E4 | A fonte e puramente promocional e nao apresenta criterios, arquitetura, exemplos verificaveis, repositorio, documentacao tecnica ou evidencia rastreavel. | individual |
| E5 | A fonte e duplicata de outra fonte mais completa, mais recente ou mais citavel. | individual |
| E6 | A fonte esta abandonada ou inacessivel de modo que nao seja possivel verificar autoria, data, escopo minimo ou conteudo tecnico. | individual |
| E7 | A fonte e apenas resumo, slide, anuncio breve, comentario social ou opiniao sem detalhes tecnicos suficientes para extracao. | individual |
| E8 | A fonte menciona frameworks de desenvolvimento com IA apenas tangencialmente, sem analise substantiva ou descricao operacional. | individual |

## 5. Quality assessment

- **Framework**: `none`
- **Threshold para inclusao final**: N/A. A revisao classificara a forca da evidencia por categoria de fonte, mas nao aplicara exclusao por checklist formal de qualidade nesta primeira rodada.

## 6. Snowballing

- **Direcao**: `both`
- **Profundidade**: 1 nivel
- **Rodadas maximas**: 3

## 7. Bases de dados-alvo

- arXiv
- ACM Digital Library
- IEEE Xplore
- Scopus via OpenAlex quando acesso direto nao estiver disponivel
- Web of Science via metadados abertos quando acesso direto nao estiver disponivel
- Crossref
- OpenAlex
- Semantic Scholar
- Google Scholar para busca complementar e verificacao de citacoes
- GitHub e documentacao oficial para fontes primarias de frameworks
- Blogs tecnicos oficiais e literatura cinzenta verificavel quando necessarios para frameworks recentes sem paper academico

## 8. Periodo de cobertura

- **Data inicial**: 2018
- **Data final**: 2026

## 9. Idiomas aceitos

- Ingles
- Portugues

## 10. Esquema de extracao planejado

| Campo | Descricao |
|---|---|
| Nome | Nome oficial ou comunitario do framework, metodo, toolkit, IDE, CLI ou plataforma |
| Natureza | Metodologia, toolkit, plataforma, framework academico ou pratico, extensao comunitaria |
| Origem | Academia, empresa, comunidade, autor independente ou combinacao |
| Artefatos | Specs, PRDs, planos, tasks, stories, docs, logs, evidencias ou outros artefatos persistentes |
| Papeis | Agentes, personas, roles ou unidades de responsabilidade definidas |
| Execucao | IDE, CLI, terminal, browser, testes, edicao de codigo, repositorio ou pipeline |
| Validacao | Checklists, testes, gates, hooks, revisao humana, evidencias, auditoria ou politicas |
| Portabilidade | Dependencia de fornecedor, IDE, modelo, formato, extensoes ou plataforma |
| Evidencia | Paper, documentacao, repositorio, estudo empirico, relato tecnico ou comparacao pratica |
| Riscos | Drift, lock-in, contexto, seguranca, supply chain, overhead, governanca ou rastreabilidade |

## 11. Emendas pos-fixacao

- **2026-05-28, autor**: o desenho foi reconhecido e renomeado como revisao de literatura multivocal (MLR), aplicando o protocolo Kitchenham a literatura formal e as diretrizes de Garousi et al. (2019) para a literatura cinzenta. A mudanca e de nomenclatura e formalizacao, nao de escopo: o protocolo ja listava GitHub, documentacao oficial e blogs tecnicos nas bases-alvo (secao 7) e ja aceitava literatura cinzenta tecnicamente verificavel no criterio I5. A literatura formal (37 estudos) seguiu busca automatizada por string; a literatura cinzenta (7 frameworks) seguiu busca dirigida as fontes primarias, sob os mesmos criterios de elegibilidade e o mesmo esquema de extracao. Motivo: alinhar o relato ao que foi de fato executado e sustentar a inclusao dos frameworks como objetos de analise.

## 12. Aprovacao do protocolo

- **Aprovado por**: autor
- **Data**: 2026-05-27 11:11
- **Registro**: o autor respondeu `APROVAR` ao checkpoint da Etapa 1.
