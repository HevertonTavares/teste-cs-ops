# Estrutura dos Dados

Eu descrevo aqui o esquema das tabelas usadas no teste. As mesmas informações existem nos arquivos CSV dentro da pasta data e também no arquivo database.sqlite.

## Tabela clientes

<table>
<thead><tr><th>Coluna</th><th>Tipo</th><th>Descrição</th></tr></thead>
<tbody>
<tr><td><code>id</code></td><td>INT</td><td>Identificador único</td></tr>
<tr><td><code>nome</code></td><td>TEXT</td><td>Nome da fazenda ou empresa</td></tr>
<tr><td><code>segmento</code></td><td>TEXT</td><td>Pequeno Produtor, Médio Produtor, Grande Produtor, Cooperativa</td></tr>
<tr><td><code>plano</code></td><td>TEXT</td><td>Starter, Professional, Enterprise</td></tr>
<tr><td><code>mrr</code></td><td>FLOAT</td><td>Receita Mensal Recorrente, em reais</td></tr>
<tr><td><code>usuarios_contratados</code></td><td>INT</td><td>Número de licenças contratadas</td></tr>
<tr><td><code>modulos_contratados</code></td><td>TEXT</td><td>Lista de módulos, separados por vírgula</td></tr>
<tr><td><code>data_inicio</code></td><td>DATE</td><td>Data de início do contrato</td></tr>
<tr><td><code>csm_responsavel</code></td><td>TEXT</td><td>Customer Success Manager responsável</td></tr>
<tr><td><code>estado</code></td><td>TEXT</td><td>Estado, UF</td></tr>
</tbody></table>

## Tabela uso_mensal

<table>
<thead><tr><th>Coluna</th><th>Tipo</th><th>Descrição</th></tr></thead>
<tbody>
<tr><td><code>cliente_id</code></td><td>INT</td><td>Chave estrangeira para clientes.id</td></tr>
<tr><td><code>mes</code></td><td>TEXT</td><td>Mês de referência, formato AAAA barra MM</td></tr>
<tr><td><code>logins</code></td><td>INT</td><td>Total de logins no mês</td></tr>
<tr><td><code>usuarios_ativos</code></td><td>INT</td><td>Usuários únicos que fizeram login no mês</td></tr>
<tr><td><code>modulos_usados</code></td><td>INT</td><td>Quantidade de módulos utilizados no mês</td></tr>
<tr><td><code>tickets_suporte</code></td><td>INT</td><td>Tickets de suporte abertos no mês</td></tr>
<tr><td><code>acoes_realizadas</code></td><td>INT</td><td>Ações ou transações realizadas no sistema no mês</td></tr>
</tbody></table>

## Tabela eventos

<table>
<thead><tr><th>Coluna</th><th>Tipo</th><th>Descrição</th></tr></thead>
<tbody>
<tr><td><code>cliente_id</code></td><td>INT</td><td>Chave estrangeira para clientes.id</td></tr>
<tr><td><code>data</code></td><td>DATE</td><td>Data do evento, formato AAAA barra MM barra DD</td></tr>
<tr><td><code>tipo</code></td><td>TEXT</td><td>Tipo do evento, exemplo churn</td></tr>
<tr><td><code>detalhes</code></td><td>TEXT</td><td>Informações adicionais do evento</td></tr>
</tbody></table>
