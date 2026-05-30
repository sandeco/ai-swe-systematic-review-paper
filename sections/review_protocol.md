# Protocolo de Revisao

Data inicial: 2026-05-26.

## Tipo de revisao

Revisao narrativa estruturada, com possibilidade de evoluir para scoping review.

O objetivo nao e medir efeito causal, mas mapear e comparar frameworks de desenvolvimento com IA como artefatos de processo.

## Unidade de analise

Framework de desenvolvimento com IA, definido como um conjunto estruturado de um ou mais elementos:

- artefatos de especificacao;
- comandos ou CLI;
- agentes/personas;
- skills/templates/workflows;
- superficies de execucao em IDE, terminal ou navegador;
- mecanismos de validacao, revisao ou governanca.

## Criterios de inclusao

Incluir artefatos que atendam a pelo menos dois criterios:

1. Organizam o desenvolvimento com IA em mais de uma etapa.
2. Produzem ou consomem artefatos persistentes de especificacao, plano, tarefa, contexto ou validacao.
3. Definem papeis, agentes, skills ou workflows especializados.
4. Integram execucao de codigo, terminal, IDE, testes ou navegador.
5. Sao citados em literatura academica, documentacao oficial, repositorios publicos ou comparacoes praticas relevantes.

## Criterios de exclusao

Excluir:

- assistentes de codigo genericos sem workflow proprio;
- apenas modelos de linguagem ou APIs sem camada de processo;
- artigos que discutem LLMs para uma unica tarefa sem framework;
- repositorios abandonados sem documentacao minima;
- comparacoes puramente promocionais que nao descrevem criterios verificaveis.

## Categorias de fonte

| Categoria | Exemplos | Uso no artigo |
|---|---|---|
| Academica | arXiv, ACM, IEEE, ScienceDirect | Fundamentacao, lacunas, evidencia empirica |
| Oficial | docs, blogs de produto, repositorios oficiais | Descricao de features e arquitetura declarada |
| Comunitaria | repositorios, plugins, kits | Ecossistema, extensibilidade, riscos de supply chain |
| Literatura cinzenta | blogs, comparacoes de mercado, guias | Sinais de adocao e linguagem praticante |

## Strings iniciais de busca

As strings devem ser aplicadas em Google Scholar, arXiv, ACM Digital Library, IEEE Xplore e busca web geral.

```text
"agentic software engineering" survey
"AI agents" "software engineering" survey
"LLM-based agents" "software engineering" survey
"spec-driven development" "AI coding assistants"
"Spec Kit" "BMAD" "OpenSpec" "Kiro"
"AI-native software development" framework review
"agentic SDLC" software development
"context-grounded" "software engineering agents"
"software development lifecycle" "AI agents" framework
"supply chain" "AI agents" skills workflows
```

## Esquema de extracao

Para cada framework, extrair:

| Campo | Descricao |
|---|---|
| Nome | Nome oficial ou comunitario |
| Natureza | Metodologia, toolkit, plataforma, framework academico/pratico, extensao comunitaria |
| Origem | Academia, empresa, comunidade, autor independente |
| Artefatos | Specs, PRDs, planos, tasks, stories, docs, evidencias |
| Papeis | Agentes/personas definidos |
| Execucao | IDE, CLI, terminal, browser, testes, edicao de codigo |
| Validacao | Checklists, testes, gates, hooks, revisao humana, evidencias |
| Portabilidade | Dependencia de fornecedor, IDE, modelo ou formato |
| Evidencia | Paper, docs, repositorio, estudo empirico, comparacao pratica |
| Riscos | Drift, lock-in, contexto, seguranca, supply chain, overhead |

## Dimensoes comparativas

Dimensoes principais:

1. Especificacao.
2. Contexto.
3. Papeis.
4. Execucao.
5. Validacao.
6. Portabilidade.

Subdimensoes candidatas:

- specs vivas vs specs estaticas;
- greenfield vs brownfield;
- autonomia sincrona vs assincrona;
- extensao oficial vs comunitaria;
- validacao por teste final vs validacao por fase;
- contexto declarado vs contexto verificado.

## Ameacas ao metodo

- Campo em rapida mudanca.
- Documentacao de produto pode exagerar capacidades.
- Comparacoes comerciais podem ter conflito de interesse.
- Repositorios publicos podem mudar sem versao citavel.
- Ferramentas recentes ainda carecem de estudos empiricos independentes.

## Proxima iteracao recomendada

1. Aplicar as strings em bases academicas.
2. Registrar resultados brutos em `related-work/search-results.json`.
3. Marcar cada fonte como direta, adjacente ou excluida.
4. Criar matriz CSV/XLSX com o esquema de extracao.
5. Atualizar `concorrentes.md` com somente fontes verificadas e classificadas.
