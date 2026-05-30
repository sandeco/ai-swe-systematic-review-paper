# Recomendação de Venue, From Prompt to Process: A Systematic Review of AI-Assisted Software Development Frameworks

> Gerado por SCIENTEX / venue-recommender em 2026-05-30.
> Paper: `_papers/ai-swe-systematic-review-paper/PAPER.md`
> Q (qualidade estimada e validada com o autor): 74/100
> Todas as metricas capturadas em 2026-05-30. Onde nao foi possivel confirmar via fonte autoritativa hoje, marcado [CONFIRMAR].

---

## 1. Briefing usado nesta recomendação

- **Título**: From Prompt to Process: A Systematic Review of AI-Assisted Software Development Frameworks (revisão sistemática Kitchenham, bilíngue pt-br + en).
- **Área principal**: Engenharia de Software (agentes de IA / LLMs no desenvolvimento de software; cs.SE, cross cs.AI).
- **Contribuição**: taxonomia de seis dimensões validada empiricamente contra um corpus de 37 estudos; três eixos de tensão; agenda de pesquisa orientada a processo.
- **Q decomposto**: Novidade 16/20, Rigor do protocolo 16/25, Reprodutibilidade 13/15, Clareza 13/15, Magnitude 10/15, Generalização 6/10 = 74/100.
- **Perfil de risco escolhido**: Balanceado (alvo principal tier 2, revisão em 3 a 6 meses).
- **Restrições duras**: internacional em inglês; sem APC (preferência por venues gratuitos ou de baixo custo). Observação do autor: deseja uma revista bem conceituada.

> Nota de rigor: as objeções mais prováveis de revisores de RSL (ausência de confiabilidade entre avaliadores e de avaliação de qualidade / risco de viés) permanecem. Com a restrição "sem APC", os melhores alvos gratuitos de alto conceito são poucos; o plano abaixo concilia isso.

## 2. Tier 1, Aspirational

### ACM Computing Surveys (CSUR), ACM
- **Tipo**: revista de surveys.
- **Métricas**: JIF 23.8 (JCR 2024), fonte: https://www.acm.org/media-center/2024/july/impact-factors-2024 ; SJR 5.797 Q1 (2024), fonte: https://www.scimagojr.com/journalsearch.php?q=23038&tip=sid ; h5 ~168 (proxy Scilit) [CONFIRMAR].
- **Aceitação**: ~12% [CONFIRMAR]. **APC / OA**: ACM migrando para OA total em 2026; APC [CONFIRMAR]. **Atenção: pode ter APC**, o que conflita com a restrição "sem APC".
- **Aceita RSL/survey**: sim, é o escopo. Fonte: https://dl.acm.org/journal/csur/author-guidelines
- **Scope match**: 70/100. Encaixe de formato perfeito, mas CSUR espera cobertura enciclopédica; 37 estudos podem soar estreitos.
- **AcceptOdds dado Q=74**: baixa (<25%). **Justificativa do tier**: máximo prestígio em surveys. **Riscos**: seletividade altíssima; exige expandir muito a cobertura; provável APC.

### IEEE Transactions on Software Engineering (TSE), IEEE
- **Métricas**: JIF ~6.5 (JCR) [CONFIRMAR 2024]; SJR Q1 (SE), fonte: https://www.scimagojr.com/journalsearch.php?q=18711&tip=sid . **APC/OA**: híbrido (assinatura sem APC).
- **Aceita RSL**: raramente; favorece contribuição empírica/técnica nova. **Scope match**: 62/100. **AcceptOdds**: baixa (<25%). Estudos secundários puros são difíceis no TSE e as lacunas de rigor seriam muito escrutinadas.

## 3. Tier 2, Realistic (alvo principal)

### Information and Software Technology (IST), Elsevier  [MELHOR ENCAIXE]
- **Tipo**: revista de Engenharia de Software, principal foro de RSL/RSL em SE.
- **Métricas**: SJR 1.045 Q1, fonte: https://www.scimagojr.com/journalsearch.php?q=18732&tip=sid ; JIF ~3.8 a 4.3 [CONFIRMAR Clarivate 2024], fonte: https://www.resurchify.com/impact/details/18732 ; h5 [CONFIRMAR].
- **APC / OA**: híbrido; rota de assinatura sem APC (OA opcional ~USD 3.890). Fonte: https://www.sciencedirect.com/journal/information-and-software-technology/publish/guide-for-authors
- **Aceita RSL/survey**: sim, explicitamente; limite de 20.000 palavras para estudos sistemáticos; descrita como o foro premier de estudos sistemáticos em SE. Fonte: guide for authors acima.
- **Scope match**: 92/100 (melhor). É a revista que publicou as diretrizes de Kitchenham; a metodologia é nativa do venue. **AcceptOdds dado Q=74**: moderada (25-50%). **Justificativa**: melhor relação risco/retorno + sem APC pela rota de assinatura. **Riscos**: revisores podem exigir IRR e avaliação de qualidade.

### Journal of Systems and Software (JSS), Elsevier
- **Métricas**: SJR 0.975 Q1, fonte: https://www.scimagojr.com/journalsearch.php?q=19309&tip=sid ; JIF ~3.5 a 4.1 [CONFIRMAR]. **APC/OA**: híbrido, assinatura sem APC (OA ~USD 3.670).
- **Aceita RSL**: sim. **Scope match**: 84/100. **AcceptOdds**: moderada (25-50%). Escopo SE amplo cobre IA-para-SE; irmão próximo do IST.

### Empirical Software Engineering (EMSE), Springer
- **Métricas**: JIF 3.6 (JCR 2024), fonte: https://emsejournal.github.io/metrics.html ; SJR 0.895 Q1, fonte: https://www.scimagojr.com/journalsearch.php?q=18650&tip=sid . **APC/OA**: híbrido, assinatura sem APC (OA ~USD 3.390).
- **Aceita RSL**: sim, tipo central. **Scope match**: 80/100. **AcceptOdds**: moderada SE as lacunas de método forem corrigidas; senão baixa. EMSE é o venue que mais provavelmente exige IRR + avaliação de qualidade. Bom alvo somente após remediar rigor.

### Automated Software Engineering (AUSE), Springer
- **Métricas**: JIF ~3.1 (2024) [CONFIRMAR]; SJR 0.625 Q2, fonte: https://www.scimagojr.com/journalsearch.php?q=24145&tip=sid . **APC/OA**: híbrido, assinatura sem APC.
- **Scope match**: 79/100 (IA/automação em SE é o núcleo). **AcceptOdds**: moderada (25-50%). Mais atingível (Q2) e topicamente alinhada se enfatizar o ângulo de agentes/LLM.

## 4. Tier 3, Safe

### e-Informatica Software Engineering Journal (EISEJ)  [SEM APC]
- **Tipo**: revista de SE, OA diamond (sem taxas), WoS + Scopus + DOAJ.
- **Métricas**: JIF 1.2 (2024) [CONFIRMAR]; SJR 0.376 Q3, fonte: https://www.scimagojr.com/journalsearch.php?q=21100259509&tip=sid ; CiteScore 3.5. **APC/OA**: gratuito, CC-BY. Fonte: https://www.e-informatyka.pl/ e DOAJ https://doaj.org/toc/2084-4840
- **Aceita RSL**: sim, foco empírico em SE. **Legitimidade**: não predatória (DOAJ + WoS + Scopus). **Scope match**: 81/100. **AcceptOdds**: alta (>50%). Excelente opção de custo zero, mas impacto menor (Q3).

### PeerJ Computer Science
- **Métricas**: SJR 0.719 Q1, fonte: https://www.scimagojr.com/journalsearch.php?q=21100830173&tip=sid ; JIF ~2.5 [CONFIRMAR]. **APC**: ~USD 2.155 (conflita com "sem APC"). **AcceptOdds**: alta (>50%); revisão por soundness. Usar só se aceitar pagar APC.

### IEEE Access
- **Métricas**: SJR 0.849 Q1, fonte: https://www.scimagojr.com/journalsearch.php?q=21100374601&tip=sid ; aceitação ~27% oficial, decisão em ~3-6 semanas, fonte: https://ieeeaccess.ieee.org/about/rapid-peer-review/ . **APC**: ~USD 2.160 (conflita com "sem APC"). Rápido e por soundness; usar só se aceitar APC.

## 5. Plano de submissão sequencial (nunca paralelo)

| Ordem | Venue | Por que | Se rejeitado |
|---|---|---|---|
| 1 | **IST** (realistic, melhor encaixe, sem APC pela assinatura) | foro nativo de RSL em SE; scope 92 | revisar com o feedback e ir para 2 |
| 2 | **JSS** ou **EMSE** (realistic, sem APC pela assinatura) | EMSE se já tiver corrigido IRR/qualidade; JSS para alcance amplo | ir para 3 |
| 3 | **Automated Software Engineering** (realistic, Q2, sem APC) | reenquadrar no ângulo de agentes/LLM | ir para 4 |
| 4 | **e-Informatica (EISEJ)** (safe, custo zero) | aceite mais provável, sem taxa | considerar reescrita maior |

Tiros aspiracionais (CSUR, TSE) são desvios opcionais de alto risco; só com expansão substancial do paper e ciente da baixa probabilidade e do provável APC.

## 6. Preprint paralelo

O paper já está no escopo de arXiv (cs.SE). Manter o preprint no arXiv antes da submissão ao tier 1 é permitido pela maioria dos venues (Elsevier e Springer aceitam preprint anterior) e aumenta visibilidade. Verificar a política específica do venue do tier 1 antes de submeter: https://www.elsevier.com/about/policies/sharing (IST/JSS) [CONFIRMAR].

## 7. Excluídos por suspeita de predação

Nenhum. Todos os candidatos são indexados em WoS e/ou Scopus, de editoras estabelecidas (ACM, IEEE, Elsevier, Springer) ou OA verificado (EISEJ via DOAJ, PeerJ). Sem red flags.

## 8. Pendências para o autor (antes de submeter ao tier 1/2)

- [ ] Adicionar confiabilidade entre avaliadores (Cohen's kappa) na triagem e na extração, ou justificar transparentemente a revisão por avaliador único. Item nº 1 de objeção em revisores de RSL.
- [ ] Incluir uma avaliação de qualidade / risco de viés (mesmo que leve, ex.: checklist DARE/CASP adaptado), ou declarar explicitamente a decisão e o impacto.
- [ ] Suavizar o termo "validação empírica" da taxonomia para "confronto com a evidência", já que o mapeamento forte/média/fraca é julgado pelo autor sem segundo codificador.
- [ ] Confirmar JIF Clarivate 2024 e h5-index dos venues do tier 1/2 antes de decidir.

## 9. Histórico de captura

| Item | URL | Data |
|---|---|---|
| Scimago (IST/JSS/EMSE/AUSE/CSUR/EISEJ/Access) | https://www.scimagojr.com/ | 2026-05-30 |
| ACM Impact Factors 2024 | https://www.acm.org/media-center/2024/july/impact-factors-2024 | 2026-05-30 |
| EMSE metrics | https://emsejournal.github.io/metrics.html | 2026-05-30 |
| IST guide for authors | https://www.sciencedirect.com/journal/information-and-software-technology/publish/guide-for-authors | 2026-05-30 |
| EISEJ / DOAJ | https://doaj.org/toc/2084-4840 | 2026-05-30 |

## 10. Notas metodológicas

- Probabilidades de aceite são estimativas heurísticas (bandas), não predições.
- Vários JIF estão como [CONFIRMAR] porque agregadores divergem do Clarivate JCR; confirme o valor oficial antes da decisão final.
- Reexecute esta skill se o intervalo até a submissão passar de 6 meses.
