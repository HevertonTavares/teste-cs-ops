# Parte 1: SQL

**Candidato(a):** Heverton Vilas Boas Matiello

**Data:** 22/01/2025

## Pergunta 1

Liste os 10 clientes com maior MRR que tiveram zero logins no último mês (2024-12).

### Query

```sql
SELECT c.id, c.nome, c.mrr, COALESCE(u.logins,0) AS logins_dez
FROM clientes c
LEFT JOIN uso_mensal u
  ON u.cliente_id = c.id AND u.mes = '2024-12'
WHERE COALESCE(u.logins,0) = 0
ORDER BY c.mrr DESC
LIMIT 10;
```

### Resultado

<table>
<thead><tr><th>id</th><th>nome</th><th>mrr</th><th>logins_dez</th></tr></thead>
<tbody><tr><td>460</td><td>Rancho Nova Era</td><td>787.65</td><td>0</td></tr><tr><td>254</td><td>Estância Progresso</td><td>707.46</td><td>0</td></tr><tr><td>24</td><td>Fazenda União dos Santos</td><td>525.93</td><td>0</td></tr><tr><td>189</td><td>Fazenda Bela Vista</td><td>412.35</td><td>0</td></tr></tbody>
</table>

Observação: no dataset existem apenas 4 clientes com zero logins em 2024 12.

## Pergunta 2

Calcule a taxa de churn por segmento considerando os eventos de churn registrados. Ordene do maior para o menor.

### Query

```sql
WITH churns AS (
  SELECT DISTINCT cliente_id
  FROM eventos
  WHERE tipo = 'churn'
),
base AS (
  SELECT segmento, COUNT(*) AS total_clientes
  FROM clientes
  GROUP BY segmento
),
churn_por_segmento AS (
  SELECT c.segmento, COUNT(DISTINCT c.id) AS churns
  FROM clientes c
  JOIN churns ch ON ch.cliente_id = c.id
  GROUP BY c.segmento
)
SELECT b.segmento,
       b.total_clientes,
       COALESCE(cs.churns,0) AS churns,
       ROUND(1.0*COALESCE(cs.churns,0)/b.total_clientes, 4) AS taxa_churn
FROM base b
LEFT JOIN churn_por_segmento cs ON cs.segmento = b.segmento
ORDER BY taxa_churn DESC, churns DESC;
```

### Resultado

<table>
<thead><tr><th>segmento</th><th>total_clientes</th><th>churns</th><th>taxa_churn</th></tr></thead>
<tbody><tr><td>Grande Produtor</td><td>63</td><td>8</td><td>0.127</td></tr><tr><td>Pequeno Produtor</td><td>229</td><td>28</td><td>0.1223</td></tr><tr><td>Médio Produtor</td><td>171</td><td>17</td><td>0.0994</td></tr><tr><td>Cooperativa</td><td>24</td><td>2</td><td>0.0833</td></tr></tbody>
</table>

## Pergunta 3

Qual CSM tem a melhor taxa de retenção? (menor % de churn entre seus clientes). Mostre a query e interprete o resultado brevemente.

### Query

```sql
WITH churns AS (
  SELECT DISTINCT cliente_id
  FROM eventos
  WHERE tipo = 'churn'
),
base AS (
  SELECT csm_responsavel, COUNT(*) AS total_clientes
  FROM clientes
  GROUP BY csm_responsavel
),
churn_por_csm AS (
  SELECT c.csm_responsavel, COUNT(DISTINCT c.id) AS churns
  FROM clientes c
  JOIN churns ch ON ch.cliente_id = c.id
  GROUP BY c.csm_responsavel
)
SELECT b.csm_responsavel,
       b.total_clientes,
       COALESCE(cc.churns,0) AS churns,
       ROUND(1.0*(b.total_clientes-COALESCE(cc.churns,0))/b.total_clientes, 4) AS taxa_retencao
FROM base b
LEFT JOIN churn_por_csm cc ON cc.csm_responsavel = b.csm_responsavel
ORDER BY taxa_retencao DESC, total_clientes DESC;
```

### Resultado

<table>
<thead><tr><th>csm_responsavel</th><th>total_clientes</th><th>churns</th><th>taxa_retencao</th></tr></thead>
<tbody><tr><td>Carla Mendes</td><td>102</td><td>9</td><td>0.9118</td></tr><tr><td>Diego Oliveira</td><td>80</td><td>8</td><td>0.9</td></tr><tr><td>Bruno Costa</td><td>123</td><td>14</td><td>0.8862</td></tr><tr><td>Elena Santos</td><td>59</td><td>7</td><td>0.8814</td></tr><tr><td>Ana Silva</td><td>123</td><td>17</td><td>0.8618</td></tr></tbody>
</table>

### Interpretação

Pelo critério de maior taxa de retenção, eu encontro Carla Mendes como melhor resultado, com 0,9118 de retenção no período observado. Eu usaria esse dado como ponto de partida e validaria se há viés de carteira, por exemplo distribuição de segmentos e planos por CSM.

## Pergunta 4 Bônus

Encontre clientes com queda de mais de 50 por cento nos logins comparando os últimos 2 meses com os 2 meses anteriores.

### Query

```sql
WITH sums AS (
  SELECT cliente_id,
         SUM(CASE WHEN mes IN ('2024-11','2024-12') THEN logins ELSE 0 END) AS logins_recentes,
         SUM(CASE WHEN mes IN ('2024-09','2024-10') THEN logins ELSE 0 END) AS logins_anteriores
  FROM uso_mensal
  GROUP BY cliente_id
)
SELECT c.id AS cliente_id,
       c.nome,
       s.logins_recentes,
       s.logins_anteriores,
       ROUND( (1.0*s.logins_recentes - s.logins_anteriores) / NULLIF(s.logins_anteriores,0), 4) AS variacao_pct
FROM sums s
JOIN clientes c ON c.id = s.cliente_id
WHERE s.logins_anteriores > 0
  AND s.logins_recentes < 0.5 * s.logins_anteriores
ORDER BY variacao_pct ASC
LIMIT 10;
```

### Resultado

<table>
<thead><tr><th>cliente_id</th><th>nome</th><th>logins_recentes</th><th>logins_anteriores</th><th>variacao_pct</th></tr></thead>
<tbody><tr><td>153</td><td>Rancho Horizonte</td><td>3</td><td>24</td><td>-0.875</td></tr><tr><td>189</td><td>Fazenda Bela Vista</td><td>1</td><td>8</td><td>-0.875</td></tr><tr><td>29</td><td>Haras Esperança</td><td>45</td><td>305</td><td>-0.8525</td></tr><tr><td>254</td><td>Estância Progresso</td><td>1</td><td>6</td><td>-0.8333</td></tr><tr><td>356</td><td>Sítio Horizonte</td><td>4</td><td>23</td><td>-0.8261</td></tr><tr><td>130</td><td>Rancho Nova Era dos Santos</td><td>82</td><td>450</td><td>-0.8178</td></tr><tr><td>1</td><td>Granja Boa Vista</td><td>11</td><td>58</td><td>-0.8103</td></tr><tr><td>24</td><td>Fazenda União dos Santos</td><td>1</td><td>5</td><td>-0.8</td></tr><tr><td>392</td><td>Sítio União</td><td>7</td><td>34</td><td>-0.7941</td></tr><tr><td>293</td><td>Granja Recanto Oliveira</td><td>37</td><td>168</td><td>-0.7798</td></tr></tbody>
</table>

Observação: neste conjunto de dados, todos os clientes que apresentaram queda superior a 50% acabaram entrando em churn. Isso reforça que quedas muito acentuadas no uso são um forte indicativo de risco.
