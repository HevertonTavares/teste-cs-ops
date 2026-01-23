# Parte 3: Análise de Risco e Expansão

## 1. Clientes em risco de churn  Top 10

Eu estimei risco combinando três sinais:

• Health Score baixo  peso maior.
• Queda recente de logins  novembro e dezembro vs setembro e outubro. 
• Tickets acima do padrão da base.

A ideia aqui é capturar tanto falta de valor percebido quanto tendência de queda e fricção.



## 2. Clientes com potencial de expansão  Top 5

Eu priorizei clientes ativos que não estão no plano Enterprise e que apresentam:

• Health Score alto.  
• Alta amplitude e profundidade de uso. 
• Engajamento alto em ações realizadas. 
• Suporte baixo ou controlado.

<table> 
<thead> <tr> <th>Número</th> <th>Cliente ID</th> <th>Nome</th> <th>Segmento</th> <th>MRR</th> <th>Principais sinais de risco</th> </tr> </thead> <tbody> <tr> <td>1</td> <td>230</td> <td>Fazenda Bom Futuro Souza</td> <td>Pequeno Produtor</td> <td>391.96</td> <td>health score 30.62, queda de 58% nos logins (nov e dez vs set e out), média de 2.0 tickets por mês nos últimos 3 meses, uso de módulos em 39% do contratado, usuários ativos em 100% do contratado</td> </tr> <tr> <td>2</td> <td>198</td> <td>Rancho Boa Vista Silva</td> <td>Pequeno Produtor</td> <td>663.41</td> <td>health score 30.41, queda de 49% nos logins (nov e dez vs set e out), média de 1.3 tickets por mês nos últimos 3 meses, uso de módulos em 50% do contratado, usuários ativos em 33% do contratado</td> </tr> <tr> <td>3</td> <td>250</td> <td>Fazenda Recanto</td> <td>Médio Produtor</td> <td>1801.22</td> <td>health score 27.70, queda de 50% nos logins (nov e dez vs set e out), média de 1.0 ticket por mês nos últimos 3 meses, uso de módulos em 33% do contratado, usuários ativos em 25% do contratado</td> </tr> <tr> <td>4</td> <td>90</td> <td>Granja Campo Belo</td> <td>Médio Produtor</td> <td>2328.75</td> <td>health score 33.41, queda de 47% nos logins (nov e dez vs set e out), média de 1.3 tickets por mês nos últimos 3 meses, uso de módulos em 33% do contratado, usuários ativos em 33% do contratado</td> </tr> <tr> <td>5</td> <td>419</td> <td>Granja São José Ferreira</td> <td>Pequeno Produtor</td> <td>616.77</td> <td>health score 23.49, queda de 27% nos logins (nov e dez vs set e out), média de 1.3 tickets por mês nos últimos 3 meses, uso de módulos em 33% do contratado, usuários ativos em 50% do contratado</td> </tr> <tr> <td>6</td> <td>27</td> <td>Rancho União Oliveira</td> <td>Pequeno Produtor</td> <td>742.36</td> <td>health score 39.08, queda de 48% nos logins (nov e dez vs set e out), média de 1.3 tickets por mês nos últimos 3 meses, uso de módulos em 50% do contratado, usuários ativos em 56% do contratado</td> </tr> <tr> <td>7</td> <td>376</td> <td>Haras Terra Rica</td> <td>Pequeno Produtor</td> <td>620.80</td> <td>health score 34.42, queda de 48% nos logins (nov e dez vs set e out), média de 1.0 ticket por mês nos últimos 3 meses, uso de módulos em 33% do contratado, usuários ativos em 100% do contratado</td> </tr> <tr> <td>8</td> <td>150</td> <td>Granja Bom Futuro</td> <td>Médio Produtor</td> <td>1631.31</td> <td>health score 34.56, queda de 34% nos logins (nov e dez vs set e out), média de 1.7 tickets por mês nos últimos 3 meses, uso de módulos em 42% do contratado, usuários ativos em 33% do contratado</td> </tr> <tr> <td>9</td> <td>368</td> <td>Haras Santa Fé</td> <td>Pequeno Produtor</td> <td>685.29</td> <td>health score 26.24, queda de 31% nos logins (nov e dez vs set e out), média de 1.0 ticket por mês nos últimos 3 meses, uso de módulos em 33% do contratado, usuários ativos em 50% do contratado</td> </tr> <tr> <td>10</td> <td>76</td> <td>Estância Recanto Oliveira</td> <td>Pequeno Produtor</td> <td>614.19</td> <td>health score 30.33, queda de 37% nos logins (nov e dez vs set e out), média de 1.0 ticket por mês nos últimos 3 meses, uso de módulos em 33% do contratado, usuários ativos em 50% do contratado</td> </tr> </tbody> 
</table>

## 3. Ações recomendadas

### Para clientes em risco

Ação proposta: Detecção e recuperação de adoção com segmentação por causa raiz e cadência operacional padronizada.

Objetivo: Detectar risco cedo, aplicar as ações certas por perfil de risco e medir impacto em churn, adoção e tickets
Como executar

1. Eu construo uma visão única de risco combinando uso e atrito
   
• Queda de uso como variação percentual e queda de recorrência no período.
• Atrito como volume de tickets, recorrência e reabertura quando disponível.
• Profundidade de adoção como módulos usados e consistência de uso ao longo do mês.

2. Eu classifico os clientes em risco em três perfis operacionais para acionar estratégias diferentes
   
• Baixa adoção: Baixo volume de uso, baixa profundidade de módulos e pouca recorrência.
• Queda recente: Redução relevante de uso versus histórico do cliente, com risco de churn crescente.
• Atrito: Queda de uso combinada com tickets altos, solicitações repetidas ou problemas recorrentes.

3. Eu crio listas dinâmicas no CRM atualizadas semanalmente com regras estáveis e rastreáveis
   
• Lista Crítico: Score crítico ou atenção + queda de uso relevante + atrito alto.
• Lista Atenção: Queda de uso moderada ou tendência negativa por duas janelas consecutivas.
• Lista Baixa adoção: Baixa recorrência e baixa profundidade de módulos independentemente de churn formal.

Eu registro data de entrada e saída de cada lista para medir tempo de recuperação.

4. Eu aplico as ações certas em pacotes padronizados, não em abordagens manuais caso a caso
   
• Pacote A ativação rápida: foco em elevar recorrência e ações chave em 7 dias.
• Pacote B redução de atrito: foco em diminuir tickets repetidos e corrigir causas raiz.
• Pacote C reativação de rotina: foco em retomar uso consistente após queda dastrica.

Cada pacote tem checklist, material padrão, SLA e critérios claros de sucesso.

5. Eu automatizo a abertura de tarefas e alertas com base em regras do score e do perfil
   
• Crítico: Recebe tarefa com SLA curto e prioridade alta.
• Atenção: Entra em cadência automatizada e só escala para humano se não reagir em 14 dias.
• Baixa: Adoção entra em cadência de ativação e segue até atingir metas mínimas de uso.

6. Eu valido o impacto com um experimento simples para evitar achismo
   
• Coortes tratadas versus controle por segmento e score semelhante.
• Janelas de acompanhamento em 14, 30 e 60 dias.
• Métricas primárias: aumento de usuários ativos, aumento de ações chave, churn em 60 dias.
• Métricas secundárias: tickets por cliente, reaberturas, tempo de resolução e estabilidade do uso.

Métricas de sucesso

• Aumento de recorrência de uso em 14 dias e manutenção em 30 dias
• Redução de tickets repetidos e fricção em 30 dias
• Queda de churn em 60 dias no grupo tratado versus grupo controle
• Tempo médio para sair do segmento crítico reduzido

### Para clientes com potencial de expansão

Ação proposta: Identificação de expansão por maturidade de adoção, saturação e criação automática de oportunidades

Objetivo: Aumentar receita via expansão saudável, transformando sinais de uso em pipeline previsível, com controle de qualidade pós upsell.

Como executar

1. Eu defino gatilhos de expansão combinando saturação e maturidade, para reduzir falso positivo

• Saturação de usuários: usuários ativos acima de 80% do contratado por dois meses.
• Saturação de módulos: módulos usados acima de 75% do contratado por dois meses.
• Maturidade: uso recorrente em múltiplos módulos e crescimento consistente de atividade por 6 a 8 semanas.

2. Criar um gatilho no CRM que abre automaticamente uma oportunidade de expansão quando as condições são atendidas

• Cria negócio em pipeline de expansão com estágio inicial padronizado.
• Registra motivo do gatilho e os dados que justificam a expansão.
• Evita duplicidade com uma regra de janela, por exemplo não criar nova oportunidade para o mesmo cliente em 60 dias.

3. Eu padronizo pacotes de expansão por perfil para dar previsibilidade e reduzir atrito

• Expansão por licenças: quando há saturação de usuários e dependência operacional do produto.
• Expansão por módulos: quando há profundidade em um módulo e espaço claro para ativar outro módulo com ganho direto.
• Upgrade de plano: quando o cliente atinge limites e precisa de estrutura maior para continuar escalando.

4. Eu preparo um pacote de proposta orientado a dados para facilitar execução e aumentar conversão

• Resumo do uso atual e da tendência.
• O que está saturado e qual o risco de continuar sem expandir.
• O que o cliente destrava com a expansão em linguagem simples e ROI direto.
• Dois caminhos possíveis, upgrade de plano ou aumento de licenças e módulos, com recomendação clara.

5. Eu fecho o ciclo com medição de adoção pós expansão, garantindo qualidade da receita

• Check de adoção do item expandido em 30 dias.
• Alerta se expansão ocorreu e o uso não acompanhou, para evitar churn pós upsell.
• Retenção em 90 dias pós atualização como métrica de expansão saudável.

Métricas de sucesso

• Taxa de conversão das oportunidades geradas automaticamente.
• MRR expandido e receita incremental por coorte.
• Adoção do que foi expandido em 30 dias e manutenção em 60 dias.
• Retenção em 90 dias pós expansão.
• Taxa de reversão, downgrade ou churn pós upsell reduzida.
