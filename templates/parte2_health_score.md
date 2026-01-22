# Parte 2: Health Score

## 1. Fórmula proposta

Eu construí um Health Score em escala de 0 a 100 usando uma visão dos últimos 3 meses (outubro, novembro e dezembro de 2024) para reduzir efeito de sazonalidade.

### Componentes escolhidos

<table>
<thead>
<tr><th>Componente</th><th>Métrica base</th><th>Peso</th><th>Justificativa</th></tr>
</thead>
<tbody>
<tr><td>Frequência de uso</td><td>Média de logins nos últimos 3 meses, normalizada por percentil na base</td><td>25 por cento</td><td>Uso recorrente é o melhor proxy inicial de valor percebido</td></tr>
<tr><td>Amplitude de uso</td><td>Média de módulos usados dividido por módulos contratados</td><td>20 por cento</td><td>Quando o cliente usa mais módulos, a solução vira parte do processo dele e reduz risco</td></tr>
<tr><td>Profundidade de uso</td><td>Média de usuários ativos dividido por usuários contratados</td><td>20 por cento</td><td>Adoção do time do cliente aumenta stickiness e facilita expansão</td></tr>
<tr><td>Engajamento</td><td>Média de ações realizadas, normalizada por percentil na base</td><td>20 por cento</td><td>Ações são sinal de valor prático, não só login</td></tr>
<tr><td>Suporte</td><td>Média de tickets, invertida e normalizada</td><td>15 por cento</td><td>Tickets em excesso tendem a indicar fricção, mas não devem dominar o score</td></tr>
</tbody>
</table>

### Fórmula final

```text
Health Score =
  Frequência × 0.25
+ Amplitude × 0.20
+ Profundidade × 0.20
+ Engajamento × 0.20
+ Suporte × 0.15
```

### Escala

• 0 a 30  Crítico  
• 31 a 60  Atenção  
• 61 a 100  Saudável  

## 2. Justificativa dos pesos

Eu coloco maior peso em frequência porque é o sinal mais consistente de retenção em produto B2B SaaS. Em seguida eu equilibro amplitude, profundidade e engajamento para capturar adoção real, evitando olhar só login. Eu reduzo o peso de suporte porque ticket pode representar uso avançado, mas quando cresce sem adoção geralmente vira alerta.

## 3. Implementação

Ferramenta utilizada: Python

Eu implementei o cálculo em um script que lê os CSVs e exporta um arquivo com o score por cliente.

Arquivo anexo: entregas health_score_calculo.py e entregas health_scores.csv

## 4. Distribuição dos resultados

### Estatísticas

<table>
<thead><tr><th>Métrica</th><th>Valor</th></tr></thead>
<tbody><tr><td>Média</td><td>54.36</td></tr><tr><td>Mediana</td><td>52.82</td></tr><tr><td>Mínimo</td><td>23.49</td></tr><tr><td>Máximo</td><td>92.2</td></tr><tr><td>Desvio Padrão</td><td>14.84</td></tr></tbody>
</table>

### Distribuição por faixa

<table>
<thead><tr><th>Faixa</th><th>Quantidade</th><th>Percentual</th></tr></thead>
<tbody><tr><td>Crítico (0-30)</td><td>11</td><td>2.5</td></tr><tr><td>Atenção (31-60)</td><td>271</td><td>62.7</td></tr><tr><td>Saudável (61-100)</td><td>150</td><td>34.7</td></tr></tbody>
</table>

## 5. Limitações e melhorias

1. Eu não tenho informações sobre limites de plano, por exemplo limite de usuários ou de módulos, o que ajudaria a detectar expansão por saturação.

2. Eu não tenho métricas de valor entregue, por exemplo resultados no campo, economia e produtividade, então uso é proxy e pode não refletir sucesso real.

3. Eu não tenho dados de uso por recurso específico dentro de cada módulo, então o módulo usado pode mascarar adoção parcial.

4. Eu não tenho o detalhamento semanal ou diária de uso, então quedas rápidas podem ser percebidas apenas no fechamento do mês, reduzindo tempo de reação.

5. Eu não tenho baseline individual por cliente, então a mesma queda percentual pode ter impacto diferente dependendo do padrão histórico de cada conta.

6. Eu não tenho variáveis de suporte e relacionamento, por exemplo volume de tickets, tempo de resolução e sentimento, o que ajudaria a explicar risco além do uso.

7. Eu não tenho informações comerciais e financeiras, por exemplo atraso de pagamento, downgrade e renegociação, que são sinais fortes para churn e também para expansão.

## 5.1 Melhorias

1. Score por semana e não só por mês, eu colocaria um uso semanal ou diário para capturar queda antes e ganhar tempo de ação.

2. Health Score com baseline individual por cliente, em vez de comparar todo mundo igual, eu comparo o cliente contra ele mesmo. Exemplo queda de 50 por cento vs média dos últimos 3 meses.

3. Automação de playbooks por faixa de risco. Exemplo High risco cria tarefa e alerta para CSM.

4. Adicionar indicadores de adoção real: Percentual de usuários ativos sobre contratados, módulos usados sobre módulos contratados, ações chave realizadas. Isso melhoria muito a precisão.
