# Parte 4: Memo Executivo

**Para:** Liderança de Customer Success  
**De:** Heverton Vilas Boas Matiello  
**Data:** 22 de janeiro de 2026  
**Assunto:** Situação da base de clientes  janeiro de 2025

## Resumo executivo

Eu analisei 487 clientes. Existem 55 clientes com evento de churn no histórico, o que representa taxa de churn observada de 11.3 por cento. O MRR total da base é R$ 1,143,813.87 e o MRR de clientes ativos é R$ 1,013,606.38.

## Principais alertas

### 1. Queda forte de uso é sinal precoce de churn

Eu encontrei 20 clientes com queda acima de 50 por cento em logins ao comparar novembro e dezembro com setembro e outubro. Todos esses clientes apresentam evento de churn, indicando que este é um gatilho muito forte para detecção precoce.

Impacto potencial: se eu capturar esse sinal antes do churn, eu consigo atuar preventivamente em carteiras com risco alto.

### 2. Segmentos com maior taxa de churn

O segmento com maior churn é Grande Produtor, com 12.7 por cento, seguido por Pequeno Produtor com 12,2 por cento. Isso sugere necessidade de abordagem diferente por ICP, maturidade e nível de suporte.

Impacto potencial: priorização de iniciativas de adoção por segmento para reduzir churn estrutural.

### 3. Inatividade total em dezembro de 2024

Existem 4 clientes com zero logins em dezembro de 2024. Mesmo com MRR menor, a inatividade total tende a anteceder cancelamento, então eu trataria como alerta de recuperação imediata.

Impacto potencial: risco de churn de curto prazo e aumento de suporte reativo.

## Oportunidades identificadas

### 1. Grande volume em faixa Atenção no Health Score

Ao calcular Health Score em janela de 3 meses, eu observo 62,7 por cento dos clientes ativos em faixa Atenção. Existe espaço para um programa simples de adoção para mover parte dessa base para Saudável e reduzir churn futuro.

Potencial: redução de churn e aumento de expansão por maturidade.

### 2. Expansão em clientes fora do plano Enterprise com uso alto

Eu identifiquei clientes com Health Score acima de 80 e uso alto de módulos e usuários, ainda em Starter ou Professional. Isso sugere oportunidade de upgrade de plano e expansão de licenças.

Potencial: aumento direto de MRR com baixo risco, pois já existe valor percebido.

## Próximos passos recomendados

<table>
<thead><tr><th>Ação</th><th>Responsável</th><th>Prazo</th><th>Prioridade</th></tr></thead>
<tbody>
<tr><td>Implementar gatilho de alerta de queda de uso e fila semanal de clientes em risco</td><td>CS Ops</td><td>2 semanas</td><td>Alta</td></tr>
<tr><td>Criar playbook de recuperação de adoção com roteiro e materiais por segmento</td><td>CS</td><td>4 semanas</td><td>Alta</td></tr>
<tr><td>Criar playbook de expansão com gatilhos de saturação e oferta padronizada</td><td>CS com apoio CS Ops</td><td>4 semanas</td><td>Média</td></tr>
</tbody>
</table>

## Anexos

• Parte 1 SQL  
• Parte 2 Health Score e arquivo health_scores.csv  
• Parte 3 lista de risco e expansão  
