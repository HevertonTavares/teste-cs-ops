# Parte 3: Análise de Risco e Expansão

## 1. Clientes em risco de churn  Top 10

Eu estimei risco combinando três sinais:

• Health Score baixo  peso maior  
• Queda recente de logins  novembro e dezembro vs setembro e outubro  
• Tickets acima do padrão da base  

A ideia aqui é capturar tanto falta de valor percebido quanto tendência de queda e fricção.

<table>
<thead><tr><th>Número</th><th>Cliente ID</th><th>Nome</th><th>Segmento</th><th>MRR</th><th>Principais sinais de risco</th></tr></thead>
<tbody><tr><td>1</td><td>230</td><td>Fazenda Bom Futuro Souza</td><td>Pequeno Produtor</td><td>391.96</td><td>health score 30.62, queda de 58 por cento nos logins (nov e dez vs set e out), média 2.0 tickets por mês (últimos 3 meses), uso de módulos 39 por cento do contratado, usuários ativos 100 por cento do contratado</td></tr><tr><td>2</td><td>198</td><td>Rancho Boa Vista Silva</td><td>Pequeno Produtor</td><td>663.41</td><td>health score 30.41, queda de 49 por cento nos logins (nov e dez vs set e out), média 1.3 tickets por mês (últimos 3 meses), uso de módulos 50 por cento do contratado, usuários ativos 33 por cento do contratado</td></tr><tr><td>3</td><td>250</td><td>Fazenda Recanto</td><td>Médio Produtor</td><td>1801.22</td><td>health score 27.70, queda de 50 por cento nos logins (nov e dez vs set e out), média 1.0 tickets por mês (últimos 3 meses), uso de módulos 33 por cento do contratado, usuários ativos 25 por cento do contratado</td></tr><tr><td>4</td><td>90</td><td>Granja Campo Belo</td><td>Médio Produtor</td><td>2328.75</td><td>health score 33.41, queda de 47 por cento nos logins (nov e dez vs set e out), média 1.3 tickets por mês (últimos 3 meses), uso de módulos 33 por cento do contratado, usuários ativos 33 por cento do contratado</td></tr><tr><td>5</td><td>419</td><td>Granja São José Ferreira</td><td>Pequeno Produtor</td><td>616.77</td><td>health score 23.49, queda de 27 por cento nos logins (nov e dez vs set e out), média 1.3 tickets por mês (últimos 3 meses), uso de módulos 33 por cento do contratado, usuários ativos 50 por cento do contratado</td></tr><tr><td>6</td><td>27</td><td>Rancho União Oliveira</td><td>Pequeno Produtor</td><td>742.36</td><td>health score 39.08, queda de 48 por cento nos logins (nov e dez vs set e out), média 1.3 tickets por mês (últimos 3 meses), uso de módulos 50 por cento do contratado, usuários ativos 56 por cento do contratado</td></tr><tr><td>7</td><td>376</td><td>Haras Terra Rica</td><td>Pequeno Produtor</td><td>620.8</td><td>health score 34.42, queda de 48 por cento nos logins (nov e dez vs set e out), média 1.0 tickets por mês (últimos 3 meses), uso de módulos 33 por cento do contratado, usuários ativos 100 por cento do contratado</td></tr><tr><td>8</td><td>150</td><td>Granja Bom Futuro</td><td>Médio Produtor</td><td>1631.31</td><td>health score 34.56, queda de 34 por cento nos logins (nov e dez vs set e out), média 1.7 tickets por mês (últimos 3 meses), uso de módulos 42 por cento do contratado, usuários ativos 33 por cento do contratado</td></tr><tr><td>9</td><td>368</td><td>Haras Santa Fé</td><td>Pequeno Produtor</td><td>685.29</td><td>health score 26.24, queda de 31 por cento nos logins (nov e dez vs set e out), média 1.0 tickets por mês (últimos 3 meses), uso de módulos 33 por cento do contratado, usuários ativos 50 por cento do contratado</td></tr><tr><td>10</td><td>76</td><td>Estância Recanto Oliveira</td><td>Pequeno Produtor</td><td>614.19</td><td>health score 30.33, queda de 37 por cento nos logins (nov e dez vs set e out), média 1.0 tickets por mês (últimos 3 meses), uso de módulos 33 por cento do contratado, usuários ativos 50 por cento do contratado</td></tr></tbody>
</table>

## 2. Clientes com potencial de expansão  Top 5

Eu priorizei clientes ativos que não estão no plano Enterprise e que apresentam:

• Health Score alto  
• Alta amplitude e profundidade de uso  
• Engajamento alto em ações realizadas  
• Suporte baixo ou controlado  

<table>
<thead><tr><th>Número</th><th>Cliente ID</th><th>Nome</th><th>Plano Atual</th><th>MRR</th><th>Sinais de potencial</th></tr></thead>
<tbody><tr><td>1</td><td>373</td><td>Estância São José</td><td>Starter</td><td>6505.3</td><td>health score 87.31, uso de módulos 83 por cento do contratado, usuários ativos 84 por cento do contratado, média 1906 ações por mês (últimos 3 meses), média 0.3 tickets por mês</td></tr><tr><td>2</td><td>180</td><td>Sítio Paraíso</td><td>Starter</td><td>21823.67</td><td>health score 90.20, uso de módulos 67 por cento do contratado, usuários ativos 87 por cento do contratado, média 8188 ações por mês (últimos 3 meses), média 0.0 tickets por mês, NPS 6</td></tr><tr><td>3</td><td>428</td><td>Estância Campo Belo dos Santos</td><td>Professional</td><td>2637.14</td><td>health score 86.50, uso de módulos 78 por cento do contratado, usuários ativos 87 por cento do contratado, média 1753 ações por mês (últimos 3 meses), média 0.3 tickets por mês</td></tr><tr><td>4</td><td>454</td><td>Estância Campo Belo dos Santos</td><td>Starter</td><td>2360.11</td><td>health score 82.81, uso de módulos 89 por cento do contratado, usuários ativos 88 por cento do contratado, média 1160 ações por mês (últimos 3 meses), média 0.7 tickets por mês, NPS 5</td></tr><tr><td>5</td><td>149</td><td>Estância Bela Vista Oliveira</td><td>Professional</td><td>17063.16</td><td>health score 82.58, uso de módulos 75 por cento do contratado, usuários ativos 96 por cento do contratado, média 8522 ações por mês (últimos 3 meses), média 1.0 tickets por mês, NPS 7</td></tr></tbody>
</table>

## 3. Ações recomendadas

### Para clientes em risco

Ação proposta: campanha de recuperação de adoção em duas etapas, focada em valor rápido e redução de fricção

Objetivo: recuperar uso e reduzir probabilidade de churn antes de virar cancelamento formal

Como executar
1. Eu crio uma lista dinâmica no CRM com clientes em Crítico ou Atenção com queda de uso e tickets altos, atualizada semanalmente  
2. Eu disparo um contato consultivo curto, com foco em um objetivo específico do cliente e um roteiro de reativação guiada no produto  
3. Eu agendo uma sessão de 30 minutos de revisão de módulos, removendo bloqueios e configurando alertas e relatórios que gerem valor em 7 dias  

Métricas de sucesso
• aumento de logins e ações em 14 dias  
• redução de tickets por cliente em 30 dias  
• queda de churn em 60 dias no grupo tratado vs grupo controle  

### Para clientes com potencial de expansão

Ação proposta: playbook de expansão por maturidade, usando gatilhos de saturação e adoção

Objetivo: aumentar receita via upgrade de plano e expansão de licenças e módulos

Como executar
1. Eu crio um gatilho de expansão quando usuários ativos ficam acima de 80 por cento do contratado por 2 meses ou quando módulos usados ficam acima de 75 por cento do contratado  
2. Eu preparo um pacote de proposta com dois caminhos, upgrade de plano e aumento de licenças, com benefício claro e ROI simples  
3. Eu faço abordagem com base em dados, mostrando o nível atual de uso e o que o cliente destrava com a expansão  

Métricas de sucesso
• taxa de conversão de propostas  
• receita expandida em MRR  
• retenção de 90 dias pós upgrade  
