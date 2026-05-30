# Estrategia de Busca - Frameworks de Desenvolvimento de Software com IA

> Gerado por SCIENTEX / search-descriptors em 2026-05-27.
> Este arquivo e a versao canonica das queries. Use-o como referencia para reproduzir a busca.

## 1. Contexto da busca

- **Tema geral**: frameworks de desenvolvimento de software com IA que organizam o trabalho por processos, artefatos persistentes, agentes, workflows e validacao.
- **Conceitos-chave escolhidos**: desenvolvimento de software com IA; frameworks e processos; agentes, workflows e artefatos persistentes; validacao, governanca e riscos.
- **Origem das tres decisoes de elicitacao**: protocolo Kitchenham congelado em `systematic-review/protocol.md`.
- **Recorte temporal**: 2018 a 2026.
- **Tipos de documento**: artigos de journal, artigos de conferencia, preprints arXiv, technical reports, documentacao oficial, repositorios publicos e literatura cinzenta tecnicamente verificavel.
- **Venues / bases**: arXiv, ACM, IEEE, Scopus via OpenAlex, Web of Science via metadados abertos, Crossref, OpenAlex, Semantic Scholar, Google Scholar, GitHub e documentacao oficial.
- **Idioma**: ingles e portugues.
- **Exclusoes declaradas**: modelos de linguagem sem camada de processo, APIs isoladas, benchmarks de codigo sem workflow, assistentes genericos sem artefatos persistentes, trabalhos de tarefa unica sem framework, conteudo puramente promocional, duplicatas, fontes inacessiveis ou abandonadas e opinioes sem detalhes tecnicos.

## 2. Blocos de descritores

### Bloco 1 - Desenvolvimento de software com IA

```text
("AI software development" OR "AI-assisted software development" OR "AI-powered software development" OR "AI-native software development" OR "artificial intelligence in software engineering" OR "LLM-based software engineering" OR "LLM-based software development" OR "agentic software engineering" OR "software engineering agent*" OR "coding agent*" OR "AI coding assistant*" OR "desenvolvimento de software com IA" OR "engenharia de software com IA")
```

Justificativa dos termos: este bloco ancora a busca no dominio de engenharia de software com IA. Inclui variantes centradas em AI, LLM, agentic software engineering, coding agents e termos equivalentes em portugues aceitos pelo protocolo.

### Bloco 2 - Frameworks, processos e ciclo de desenvolvimento

```text
("framework" OR "method" OR "methodology" OR "toolkit" OR "process" OR "workflow*" OR "software development lifecycle" OR "SDLC" OR "development lifecycle" OR "spec-driven development" OR "specification-driven development" OR "process-oriented" OR "framework de desenvolvimento" OR "metodologia" OR "fluxo de trabalho")
```

Justificativa dos termos: este bloco separa frameworks e processos de usos pontuais de IA. Inclui SDLC, workflow, metodologia, toolkit e spec-driven development porque o protocolo compara estruturas de trabalho, nao apenas ferramentas isoladas.

### Bloco 3 - Artefatos persistentes, especificacao e contexto

```text
("specification*" OR "software specification*" OR "requirements" OR "product requirements document" OR "PRD" OR "task*" OR "story" OR "stories" OR "plan*" OR "context" OR "context engineering" OR "traceability" OR "artifact*" OR "persistent artifact*" OR "living specification*" OR "documentacao" OR "especificacao" OR "artefato*")
```

Justificativa dos termos: este bloco captura a tese central do paper, isto e, a passagem do prompt isolado para artefatos persistentes de especificacao, contexto, planejamento, tarefas e rastreabilidade.

### Bloco 4 - Agentes, automacao e validacao

```text
("AI agent*" OR "LLM agent*" OR "multi-agent" OR "agentic workflow*" OR "autonomous agent*" OR "human-in-the-loop" OR "validation" OR "verification" OR "test*" OR "governance" OR "audit*" OR "review" OR "evidence" OR "guardrail*" OR "agente*" OR "validacao" OR "governanca")
```

Justificativa dos termos: este bloco cobre os mecanismos de execucao e controle esperados pela revisao, incluindo agentes, workflows, validacao, testes, revisao humana, auditoria e governanca.

### Bloco de exclusao

```text
NOT ("benchmark only" OR "code generation benchmark" OR "prompt engineering only" OR "API only" OR "language model only" OR "model evaluation" OR "single task" OR "opinion" OR "editorial" OR "tutorial" OR "slides")
```

Justificativa dos termos: o bloco reduz falsos positivos de trabalhos que avaliam apenas modelos, prompts, APIs ou tarefas isoladas, sem propor processo, framework ou workflow.

## 3. String canonica

```text
(("AI software development" OR "AI-assisted software development" OR "AI-powered software development" OR "AI-native software development" OR "artificial intelligence in software engineering" OR "LLM-based software engineering" OR "LLM-based software development" OR "agentic software engineering" OR "software engineering agent*" OR "coding agent*" OR "AI coding assistant*" OR "desenvolvimento de software com IA" OR "engenharia de software com IA")
AND
("framework" OR "method" OR "methodology" OR "toolkit" OR "process" OR "workflow*" OR "software development lifecycle" OR "SDLC" OR "development lifecycle" OR "spec-driven development" OR "specification-driven development" OR "process-oriented" OR "framework de desenvolvimento" OR "metodologia" OR "fluxo de trabalho")
AND
("specification*" OR "software specification*" OR "requirements" OR "product requirements document" OR "PRD" OR "task*" OR "story" OR "stories" OR "plan*" OR "context" OR "context engineering" OR "traceability" OR "artifact*" OR "persistent artifact*" OR "living specification*" OR "documentacao" OR "especificacao" OR "artefato*")
AND
("AI agent*" OR "LLM agent*" OR "multi-agent" OR "agentic workflow*" OR "autonomous agent*" OR "human-in-the-loop" OR "validation" OR "verification" OR "test*" OR "governance" OR "audit*" OR "review" OR "evidence" OR "guardrail*" OR "agente*" OR "validacao" OR "governanca"))
AND NOT
("benchmark only" OR "code generation benchmark" OR "prompt engineering only" OR "API only" OR "language model only" OR "model evaluation" OR "single task" OR "opinion" OR "editorial" OR "tutorial" OR "slides")
```

## 4. Strings prontas por base

### 4.1 IEEE Xplore

```text
(("All Metadata":"AI software development" OR "All Metadata":"AI-assisted software development" OR "All Metadata":"AI-native software development" OR "All Metadata":"artificial intelligence in software engineering" OR "All Metadata":"LLM-based software engineering" OR "All Metadata":"agentic software engineering" OR "All Metadata":"software engineering agent" OR "All Metadata":"coding agent" OR "All Metadata":"AI coding assistant")
AND
("All Metadata":"framework" OR "All Metadata":"methodology" OR "All Metadata":"toolkit" OR "All Metadata":"workflow" OR "All Metadata":"software development lifecycle" OR "All Metadata":"SDLC" OR "All Metadata":"spec-driven development" OR "All Metadata":"specification-driven development")
AND
("All Metadata":"specification" OR "All Metadata":"requirements" OR "All Metadata":"product requirements document" OR "All Metadata":"PRD" OR "All Metadata":"task" OR "All Metadata":"plan" OR "All Metadata":"context engineering" OR "All Metadata":"traceability" OR "All Metadata":"artifact")
AND
("All Metadata":"AI agent" OR "All Metadata":"LLM agent" OR "All Metadata":"multi-agent" OR "All Metadata":"agentic workflow" OR "All Metadata":"human-in-the-loop" OR "All Metadata":"validation" OR "All Metadata":"verification" OR "All Metadata":"governance" OR "All Metadata":"audit" OR "All Metadata":"guardrail"))
NOT ("All Metadata":"benchmark only" OR "All Metadata":"prompt engineering only" OR "All Metadata":"API only" OR "All Metadata":"single task" OR "All Metadata":"tutorial")
```

Filtros adicionais na UI: Years 2018 to 2026; Content Type = Journals and Conferences; Subjects = Software Engineering, Artificial Intelligence.

### 4.2 Scopus

```text
TITLE-ABS-KEY(("AI software development" OR "AI-assisted software development" OR "AI-powered software development" OR "AI-native software development" OR "artificial intelligence in software engineering" OR "LLM-based software engineering" OR "LLM-based software development" OR "agentic software engineering" OR "software engineering agent*" OR "coding agent*" OR "AI coding assistant*")
AND
("framework" OR "method" OR "methodology" OR "toolkit" OR "process" OR "workflow*" OR "software development lifecycle" OR "SDLC" OR "development lifecycle" OR "spec-driven development" OR "specification-driven development" OR "process-oriented")
AND
("specification*" OR "software specification*" OR "requirements" OR "product requirements document" OR "PRD" OR "task*" OR "story" OR "stories" OR "plan*" OR "context engineering" OR "traceability" OR "artifact*" OR "persistent artifact*" OR "living specification*")
AND
("AI agent*" OR "LLM agent*" OR "multi-agent" OR "agentic workflow*" OR "autonomous agent*" OR "human-in-the-loop" OR "validation" OR "verification" OR "test*" OR "governance" OR "audit*" OR "review" OR "evidence" OR "guardrail*"))
AND NOT TITLE-ABS-KEY("benchmark only" OR "code generation benchmark" OR "prompt engineering only" OR "API only" OR "language model only" OR "model evaluation" OR "single task" OR "opinion" OR "editorial" OR "tutorial" OR "slides")
AND PUBYEAR > 2017 AND PUBYEAR < 2027
```

Filtros adicionais: Document type = Article, Conference Paper, Review only for competitor mapping; Subject area = Computer Science.

### 4.3 Web of Science

```text
TS=(("AI software development" OR "AI-assisted software development" OR "AI-powered software development" OR "AI-native software development" OR "artificial intelligence in software engineering" OR "LLM-based software engineering" OR "LLM-based software development" OR "agentic software engineering" OR "software engineering agent*" OR "coding agent*" OR "AI coding assistant*")
AND
("framework" OR "method" OR "methodology" OR "toolkit" OR "process" OR "workflow*" OR "software development lifecycle" OR "SDLC" OR "development lifecycle" OR "spec-driven development" OR "specification-driven development" OR "process-oriented")
AND
("specification*" OR "software specification*" OR "requirements" OR "product requirements document" OR "PRD" OR "task*" OR "story" OR "stories" OR "plan*" OR "context engineering" OR "traceability" OR "artifact*" OR "persistent artifact*" OR "living specification*")
AND
("AI agent*" OR "LLM agent*" OR "multi-agent" OR "agentic workflow*" OR "autonomous agent*" OR "human-in-the-loop" OR "validation" OR "verification" OR "test*" OR "governance" OR "audit*" OR "review" OR "evidence" OR "guardrail*"))
NOT TS=("benchmark only" OR "code generation benchmark" OR "prompt engineering only" OR "API only" OR "language model only" OR "model evaluation" OR "single task" OR "opinion" OR "editorial" OR "tutorial" OR "slides")
```

Filtros adicionais: Timespan 2018 to 2026; Document Types = Article, Proceedings Paper, Early Access, Review for competitor mapping.

### 4.4 ACM Digital Library

```text
[All: "AI software development"] OR [All: "AI-assisted software development"] OR [All: "AI-native software development"] OR [All: "artificial intelligence in software engineering"] OR [All: "LLM-based software engineering"] OR [All: "agentic software engineering"] OR [All: "software engineering agent"] OR [All: "AI coding assistant"]
AND
([All: "framework"] OR [All: "methodology"] OR [All: "toolkit"] OR [All: "workflow"] OR [All: "software development lifecycle"] OR [All: "SDLC"] OR [All: "spec-driven development"] OR [All: "specification-driven development"])
AND
([All: "specification"] OR [All: "requirements"] OR [All: "product requirements document"] OR [All: "PRD"] OR [All: "task"] OR [All: "plan"] OR [All: "context engineering"] OR [All: "traceability"] OR [All: "artifact"])
AND
([All: "AI agent"] OR [All: "LLM agent"] OR [All: "multi-agent"] OR [All: "agentic workflow"] OR [All: "human-in-the-loop"] OR [All: "validation"] OR [All: "verification"] OR [All: "governance"] OR [All: "audit"] OR [All: "guardrail"])
NOT
([All: "benchmark only"] OR [All: "prompt engineering only"] OR [All: "API only"] OR [All: "single task"] OR [All: "tutorial"])
```

Filtros adicionais: Publication Date 2018 to 2026; Content type = Research Article, Proceedings.

### 4.5 Google Scholar

```text
("AI software development" OR "AI-assisted software development" OR "AI-native software development" OR "agentic software engineering" OR "LLM-based software engineering") ("framework" OR "methodology" OR "workflow" OR "software development lifecycle" OR "spec-driven development") ("specification" OR "requirements" OR "context engineering" OR "artifact" OR "traceability") ("AI agent" OR "LLM agent" OR "multi-agent" OR "validation" OR "governance") -"benchmark only" -"prompt engineering only" -"API only" -"tutorial"
```

Filtros adicionais: Since 2018; sort by relevance first, then repeat with sort by date for recent frameworks.

### 4.6 ArXiv

```text
(all:"AI software development" OR all:"AI-assisted software development" OR all:"AI-native software development" OR all:"artificial intelligence in software engineering" OR all:"LLM-based software engineering" OR all:"agentic software engineering" OR all:"software engineering agent" OR all:"AI coding assistant")
AND
(all:"framework" OR all:"methodology" OR all:"toolkit" OR all:"workflow" OR all:"software development lifecycle" OR all:"SDLC" OR all:"spec-driven development" OR all:"specification-driven development")
AND
(all:"specification" OR all:"requirements" OR all:"product requirements document" OR all:"PRD" OR all:"task" OR all:"plan" OR all:"context engineering" OR all:"traceability" OR all:"artifact")
AND
(all:"AI agent" OR all:"LLM agent" OR all:"multi-agent" OR all:"agentic workflow" OR all:"human-in-the-loop" OR all:"validation" OR all:"verification" OR all:"governance" OR all:"audit" OR all:"guardrail")
ANDNOT
(all:"benchmark only" OR all:"prompt engineering only" OR all:"API only" OR all:"single task" OR all:"tutorial")
```

Filtros adicionais: Category = cs.SE, cs.AI, cs.CL, cs.HC; Submitted from 2018 to 2026.

### 4.7 PubMed

```text
("AI software development"[Title/Abstract] OR "AI-assisted software development"[Title/Abstract] OR "artificial intelligence in software engineering"[Title/Abstract] OR "LLM-based software engineering"[Title/Abstract] OR "agentic software engineering"[Title/Abstract])
AND
("framework"[Title/Abstract] OR "methodology"[Title/Abstract] OR "workflow"[Title/Abstract] OR "software development lifecycle"[Title/Abstract] OR "specification-driven development"[Title/Abstract])
AND
("specification"[Title/Abstract] OR "requirements"[Title/Abstract] OR "context engineering"[Title/Abstract] OR "traceability"[Title/Abstract] OR "artifact"[Title/Abstract])
AND
("AI agent"[Title/Abstract] OR "LLM agent"[Title/Abstract] OR "multi-agent"[Title/Abstract] OR "validation"[Title/Abstract] OR "verification"[Title/Abstract] OR "governance"[Title/Abstract])
NOT
("benchmark only"[Title/Abstract] OR "prompt engineering only"[Title/Abstract] OR "API only"[Title/Abstract] OR "single task"[Title/Abstract] OR "tutorial"[Title/Abstract])
```

Nota: PubMed e periferico para este paper. Usar apenas para trabalhos de engenharia de software aplicada a saude ou governanca de IA em software clinico.

### 4.8 ScienceDirect

```text
TITLE-ABSTR-KEY("AI software development" OR "AI-assisted software development" OR "AI-native software development" OR "artificial intelligence in software engineering" OR "LLM-based software engineering" OR "agentic software engineering" OR "software engineering agent" OR "AI coding assistant")
AND
TITLE-ABSTR-KEY("framework" OR "methodology" OR "toolkit" OR "workflow" OR "software development lifecycle" OR "SDLC" OR "spec-driven development" OR "specification-driven development")
AND
TITLE-ABSTR-KEY("specification" OR "requirements" OR "product requirements document" OR "PRD" OR "task" OR "plan" OR "context engineering" OR "traceability" OR "artifact")
AND
TITLE-ABSTR-KEY("AI agent" OR "LLM agent" OR "multi-agent" OR "agentic workflow" OR "human-in-the-loop" OR "validation" OR "verification" OR "governance" OR "audit" OR "guardrail")
AND NOT
TITLE-ABSTR-KEY("benchmark only" OR "prompt engineering only" OR "API only" OR "single task" OR "tutorial")
```

Filtros adicionais: Years 2018 to 2026; Article type = Research articles, Review articles only for competitor mapping.

### 4.9 OpenAlex

```text
search=("AI software development" OR "AI-assisted software development" OR "AI-native software development" OR "artificial intelligence in software engineering" OR "LLM-based software engineering" OR "agentic software engineering" OR "software engineering agent" OR "AI coding assistant") AND ("framework" OR "methodology" OR "workflow" OR "software development lifecycle" OR "spec-driven development" OR "specification-driven development") AND ("specification" OR "requirements" OR "context engineering" OR "traceability" OR "artifact") AND ("AI agent" OR "LLM agent" OR "multi-agent" OR "validation" OR "governance")
filter=from_publication_date:2018-01-01,to_publication_date:2026-12-31,concepts.id:C41008148
```

Nota: `C41008148` e o conceito OpenAlex para Computer science. Confirmar o ID no momento da execucao se a API retornar baixa cobertura.

### 4.10 Semantic Scholar

```text
("AI software development" OR "AI-assisted software development" OR "AI-native software development" OR "artificial intelligence in software engineering" OR "LLM-based software engineering" OR "agentic software engineering" OR "software engineering agent" OR "AI coding assistant") AND ("framework" OR "methodology" OR "workflow" OR "software development lifecycle" OR "spec-driven development" OR "specification-driven development") AND ("specification" OR "requirements" OR "context engineering" OR "traceability" OR "artifact") AND ("AI agent" OR "LLM agent" OR "multi-agent" OR "validation" OR "governance")
```

Filtros adicionais: Year 2018 to 2026; Fields of Study = Computer Science.

### 4.11 GitHub e documentacao oficial

```text
("AI software development" OR "agentic software engineering" OR "AI coding assistant" OR "spec-driven development" OR "agentic workflow") ("framework" OR "methodology" OR "toolkit" OR "template" OR "workflow") ("specification" OR "PRD" OR "tasks" OR "agents" OR "skills" OR "validation")
```

Aplicacao: usar para localizar fontes primarias de frameworks recentes, documentacao oficial e repositorios. Registrar data de acesso, commit ou release quando disponivel.

## 5. Palavras-chave sugeridas para o paper

Keywords em ingles:

- AI-assisted software development
- Agentic software engineering
- Spec-driven development
- Software engineering agents
- AI development frameworks
- Human-in-the-loop validation

Alternativas em portugues:

- desenvolvimento de software com IA
- engenharia de software agentica
- desenvolvimento orientado por especificacao
- frameworks de desenvolvimento com IA
- validacao com humano no ciclo

## 6. Tabela de sinonimos e variantes

| Conceito | EN principal | EN variantes | PT principal | PT variantes | Siglas |
|---|---|---|---|---|---|
| desenvolvimento com IA | AI software development | AI-assisted software development; AI-powered software development; AI-native software development; LLM-based software engineering | desenvolvimento de software com IA | engenharia de software com IA | AI; LLM |
| agentes em software | software engineering agents | coding agents; AI agents; LLM agents; autonomous agents; agentic workflows | agentes de software | agentes de IA; workflows agenticos | AI agents; LLM agents |
| processo de desenvolvimento | software development lifecycle | SDLC; workflow; method; methodology; toolkit; process-oriented framework | ciclo de desenvolvimento de software | metodologia; fluxo de trabalho | SDLC |
| especificacao e artefatos | specification | requirements; PRD; task; story; plan; artifact; living specification | especificacao | artefatos; tarefas; planos; documentacao | PRD |
| contexto e rastreabilidade | context engineering | traceability; persistent context; evidence; audit | engenharia de contexto | rastreabilidade; evidencias; auditoria | N/A |
| validacao e governanca | validation | verification; testing; review; human-in-the-loop; governance; guardrails | validacao | governanca; revisao humana; testes | N/A |

## 7. Historico de execucao

| Base | Data | N de resultados | Observacoes |
|---|---|---|---|
| IEEE Xplore | | | |
| Scopus | | | |
| Web of Science | | | |
| ACM Digital Library | | | |
| Google Scholar | | | |
| ArXiv | | | |
| PubMed | | | |
| ScienceDirect | | | |
| OpenAlex | | | |
| Semantic Scholar | | | |
| GitHub/docs oficiais | | | |

## 8. Refinamento sugerido

Se a string retornar mais de 500 resultados:

- Restringir o Bloco 2 para `framework`, `methodology`, `workflow` e `spec-driven development`.
- Exigir Bloco 3 no titulo ou abstract.
- Separar busca academica de busca por documentacao oficial.
- Adicionar termos de validacao, governanca ou traceability como obrigatorios.

Se a string retornar menos de 30 resultados:

- Remover o Bloco 4 temporariamente.
- Trocar `agentic software engineering` por termos mais amplos como `AI coding assistant`.
- Rodar buscas separadas para `spec-driven development`, `AI coding assistants` e `software engineering agents`.
- Remover exclusoes, aplicar criterios E1 a E8 apenas no screening.

## 9. Seeds conhecidos para busca dirigida

Estes termos nao substituem a busca sistematica, mas devem ser usados como busca complementar para fontes primarias e snowballing:

- BMAD Method
- Reversa
- GitHub Spec Kit
- Spec Kit Agents
- Spec-Driven Development
- Google Antigravity
- Antigravity Kit
- OpenSpec
- Kiro
