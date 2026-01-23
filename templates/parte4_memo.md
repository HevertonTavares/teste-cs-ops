# Parte 4: Memo Executivo

**Candidato(a):** Heverton Vilas Boas Matiello

**Data:** 22/01/2026

# Memo: Situação da Base de Clientes

**Para:** Liderança de Customer Success  
**De:** Heverton Vilas Boas Matiello  
**Data:** 22 de janeiro de 2026  
**Assunto:** Situação da base de clientes  janeiro de 2025

## Resumo executivo

Eu analisei 487 clientes. Existem 55 clientes com evento de churn no histórico, o que representa taxa de churn observada de 11.3%. O MRR total da base é R$ 1,143,813.87 e o MRR de clientes ativos é R$ 1,013,606.38.

## Principais alertas

### 1. Queda forte de uso é sinal precoce de churn

Eu encontrei 20 clientes com queda acima de 50% em logins ao comparar novembro e dezembro com setembro e outubro. Todos esses clientes apresentam evento de churn, indicando que este é um gatilho muito forte para detecção precoce.

Impacto potencial: se eu capturar esse sinal antes do churn, eu consigo atuar preventivamente em carteiras com risco alto.

Melhoria proposta: criar um gatilho automatizado no CRM para queda acima de 50% e uma fila semanal de revisão por CS Ops, com segmentação por provável causa, baixa adoção, fricção via suporte ou sazonalidade.

### 2. Segmentos com maior taxa de churn

O segmento com maior churn é Grande Produtor, com 12.7%, seguido por Pequeno Produtor com 12,2%. Isso sugere necessidade de abordagem diferente por ICP, maturidade e nível de suporte.

Impacto potencial: priorização de iniciativas de adoção por segmento para reduzir churn estrutural.

Melhoria proposta: criar cohorts por segmento e medir recuperação de uso em 14 dias após intervenção, comparando grupo tratado vs grupo controle, para validar quais ações reduzem churn de forma consistente.

### 3. Inatividade total em dezembro de 2024

Existem 4 clientes com zero logins em dezembro de 2024. Mesmo com MRR menor, a inatividade total tende a anteceder cancelamento, então eu trataria como alerta de recuperação imediata.

Impacto potencial: risco de churn de curto prazo e aumento de suporte reativo.

Melhoria proposta: regra de prioridade máxima para contas com 0 logins no mês, com SLA de primeira ação em até 48 horas e monitoramento de reativação em 7 dias.

## Oportunidades identificadas

### 1. Grande volume em faixa Atenção no Health Score

Ao calcular Health Score em janela de 3 meses, eu observo 62,7% dos clientes ativos em faixa Atenção. Existe espaço para um programa simples de adoção para mover parte dessa base para Saudável e reduzir churn futuro.

Potencial: redução de churn e aumento de expansão por maturidade.

Melhoria proposta: criar uma cadência automatizada para a faixa Atenção, com objetivo de aumentar recorrência e profundidade de módulos em 30 dias, antes de escalar para atuação humana.

### 2. Expansão em clientes fora do plano Enterprise com uso alto

Eu identifiquei clientes com Health Score acima de 80 e uso alto de módulos e usuários, ainda em Starter ou Professional. Isso sugere oportunidade de upgrade de plano e expansão de licenças.

Potencial: aumento direto de MRR com baixo risco, pois já existe valor percebido.

Melhoria proposta: criar gatilhos de expansão baseados em saturação, usuários ativos acima de 80% do contratado por 2 meses e módulos usados acima de 75% do contratado por 2 meses, com abertura automática de oportunidade no CRM para evitar perda de timing.

## Próximos passos recomendados

<table>
<thead><tr><th>Ação</th><th>Responsável</th><th>Prazo</th><th>Prioridade</th></tr></thead>
<tbody>
<tr><td>Implementar gatilho de alerta de queda de uso e fila semanal de clientes em risco</td><td>CS Ops</td><td>2 semanas</td><td>Alta</td></tr>
<tr><td>Criar playbook de recuperação de adoção com roteiro e materiais por segmento</td><td>CS</td><td>4 semanas</td><td>Alta</td></tr>
<tr><td>Criar playbook de expansão com gatilhos de saturação e oferta padronizada</td><td>CS com apoio CS Ops</td><td>4 semanas</td><td>Média</td></tr>
<tr><td>Definir governança quinzenal com painel de risco e expansão por segmento, incluindo métricas tratado vs controle</td><td>CS Ops</td><td>4 semanas</td><td>Média</td></tr>
</tbody>
</table>

## Anexos

• Parte 1 SQL  
• Parte 2 Health Score e arquivo health_scores.csv  
• Parte 3 lista de risco e expansão  
