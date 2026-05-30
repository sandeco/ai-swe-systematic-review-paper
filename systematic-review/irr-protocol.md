# Protocolo de dupla-triagem e confiabilidade entre avaliadores (IRR)

> Entregue por SCIENTEX / scientex-improve (IMP-1 do score.md) em 2026-05-30.
> Objetivo: fechar o ponto cheio de confiabilidade entre avaliadores (Cohen's kappa)
> com um segundo codificador humano independente. A triagem original foi conduzida por
> um unico avaliador operacional seguindo o protocolo; este documento padroniza a
> re-triagem independente para que o kappa reportado seja IRR de verdade, nao auto-concordancia.

## 1. Materiais ja preparados

- `screening/irr/coding-sheet-title-abstract.csv` (277 itens): decisao do avaliador 1 ja preenchida; coluna `reviewer2_decision` em branco.
- `screening/irr/coding-sheet-full-text.csv` (45 itens): idem para a passada de texto completo.
- `irr_kit.py kappa <sheet>`: calcula Cohen's kappa, concordancia observada (Po) e esperada (Pe), com a interpretacao de Landis e Koch (1977), assim que a coluna `reviewer2_decision` estiver preenchida.

## 2. Quem e como

- O segundo codificador deve ser independente do primeiro e nao deve ver a coluna `reviewer1_decision` antes de decidir (oculte a coluna ou trabalhe em uma copia sem ela).
- Decisao por item: `include` ou `exclude`, aplicando os mesmos criterios I1 a I8 e E1 a E8 do `protocol.md`.
- Registre o criterio decisivo em `reviewer2_criterion` e qualquer observacao em `notes`.

## 3. Amostra recomendada

- Minimo defensavel: re-triagem independente de uma amostra aleatoria de pelo menos 20% dos itens de titulo/resumo (cerca de 56 itens) e de 100% da passada de texto completo (45 itens), que e a mais decisiva.
- Ideal: 100% das duas passadas. Quanto maior a amostra, mais estavel o kappa.

## 4. Resolucao de divergencias

- Apos a re-triagem, compare as decisoes. Para cada divergencia, os dois avaliadores discutem e registram a decisao final e a regra que a sustentou.
- Reporte no Metodo: o kappa por passada, a taxa de divergencia e como as divergencias foram resolvidas (consenso ou terceiro avaliador).

## 5. Calculo

```
python3 irr_kit.py kappa screening/irr/coding-sheet-full-text.csv
python3 irr_kit.py kappa screening/irr/coding-sheet-title-abstract.csv
```

## 6. Texto sugerido para o Metodo (preencher os valores reais apos o calculo)

> A confiabilidade entre avaliadores foi medida re-triando de forma independente
> [amostra] dos itens por um segundo codificador cego a decisao original. O acordo,
> medido por Cohen's kappa, foi de [kappa_ta] na triagem de titulo e resumo e
> [kappa_ft] na leitura de texto completo, ambos na faixa [interpretacao] (Landis e
> Koch, 1977). As [n] divergencias foram resolvidas por [consenso / terceiro avaliador].

Enquanto o segundo codificador humano nao fechar a re-triagem, o paper reporta a
dupla-checagem reproduzivel por protocolo (esta infraestrutura) como medida de
confiabilidade, e declara explicitamente que o IRR de dois avaliadores humanos esta
disponivel para fechamento via este kit.
