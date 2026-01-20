# Teste Técnico: Analista de CS Operations

Bem-vindo(a) ao teste técnico para a vaga de **Analista Pleno de CS Operations**.

Este teste avalia suas habilidades em análise de dados, SQL, e capacidade de transformar dados em insights acionáveis para Customer Success.

## Contexto

Você recebeu dados de uma empresa SaaS do agronegócio que oferece um software de gestão para produtores rurais. A empresa tem aproximadamente **500 clientes** e está preocupada com:

1. **Churn** - Clientes cancelando o serviço
2. **Engajamento** - Clientes que não estão usando o produto adequadamente
3. **Expansão** - Oportunidades de upsell/cross-sell

Sua missão é analisar os dados, identificar padrões e propor ações.

---

## Estrutura dos Dados

### Tabela: `clientes`

| Coluna | Tipo | Descrição |
|--------|------|-----------|
| id | INT | Identificador único |
| nome | TEXT | Nome da fazenda/empresa |
| segmento | TEXT | Pequeno Produtor, Médio Produtor, Grande Produtor, Cooperativa |
| plano | TEXT | Starter, Professional, Enterprise |
| mrr | FLOAT | Receita Mensal Recorrente (R$) |
| usuarios_contratados | INT | Número de licenças contratadas |
| modulos_contratados | TEXT | Lista de módulos (separados por vírgula) |
| data_inicio | DATE | Data de início do contrato |
| csm_responsavel | TEXT | Customer Success Manager responsável |
| estado | TEXT | Estado (UF) |

### Tabela: `uso_mensal`

| Coluna | Tipo | Descrição |
|--------|------|-----------|
| cliente_id | INT | FK para clientes.id |
| mes | TEXT | Mês de referência (YYYY-MM) |
| logins | INT | Total de logins no mês |
| usuarios_ativos | INT | Usuários únicos que logaram |
| modulos_usados | INT | Quantidade de módulos utilizados |
| tickets_suporte | INT | Tickets de suporte abertos |
| acoes_realizadas | INT | Ações/transações no sistema |

### Tabela: `eventos`

| Coluna | Tipo | Descrição |
|--------|------|-----------|
| cliente_id | INT | FK para clientes.id |
| data | DATE | Data do evento |
| tipo | TEXT | churn, upgrade, downgrade, nps_response |
| detalhes | TEXT | Informações adicionais |

---

## O Teste

O teste é dividido em **4 partes**. Responda nos arquivos da pasta `templates/`.

### Parte 1: SQL (30-40 min)

Responda às perguntas usando SQL. Você pode usar o arquivo `data/database.sqlite` com qualquer cliente SQLite (DB Browser, DBeaver, linha de comando, etc.).

**Arquivo de resposta:** `templates/parte1_sql.md`

**Perguntas:**

1. Liste os **10 clientes com maior MRR** que tiveram **zero logins no último mês** (2024-12).

2. Calcule a **taxa de churn por segmento** considerando os eventos de churn registrados. Ordene do maior para o menor.

3. Qual **CSM tem a melhor taxa de retenção**? (menor % de churn entre seus clientes). Mostre a query e interprete o resultado brevemente.

4. **(Bônus - opcional)** Encontre clientes que tiveram **queda de mais de 50% nos logins** comparando os últimos 2 meses com os 2 meses anteriores.
   > ℹ️ Esta questão é opcional. Não perde pontos se não fizer, mas pode ganhar pontos extras se fizer corretamente.

---

### Parte 2: Health Score (40-50 min)

Crie uma fórmula de **Health Score** (escala 0-100) para classificar a saúde dos clientes.

**Arquivo de resposta:** `templates/parte2_health_score.md`

**Requisitos:**

1. Use pelo menos 3 das métricas disponíveis:
   - Frequência de uso (logins)
   - Amplitude (módulos usados vs contratados)
   - Profundidade (usuários ativos vs contratados)
   - Engajamento (ações realizadas)
   - Suporte (tickets - pode ser positivo ou negativo)

2. Defina pesos para cada componente e **justifique suas escolhas**.

3. Implemente a fórmula usando **Python, Excel ou Google Sheets** (o que preferir).

4. Calcule o Health Score para todos os clientes ativos e mostre a distribuição.

**Dica:** Não existe resposta "certa". Queremos entender seu raciocínio.

---

### Parte 3: Análise de Risco e Expansão (30-40 min)

Com base nos dados (e no Health Score se você criou), identifique oportunidades e riscos.

**Arquivo de resposta:** `templates/parte3_analise.md`

**Tarefas:**

1. **Risco de Churn:** Identifique **10 clientes** com maior risco de churn (que ainda não cancelaram). Justifique cada escolha com dados.

2. **Potencial de Expansão:** Identifique **5 clientes** com potencial de upsell/upgrade. Justifique com base no comportamento de uso.

3. **Ações Recomendadas:** Para cada grupo, proponha **1 ação específica** que o time de CS poderia executar.

---

### Parte 4: Comunicação Executiva (20-30 min)

Escreva um **memo de 1 página** para a liderança de CS.

**Arquivo de resposta:** `templates/parte4_memo.md`

**Conteúdo esperado:**

- Situação atual da base (resumo executivo)
- 3 principais alertas/riscos identificados
- 2 oportunidades de melhoria
- Próximos passos recomendados

**Dica:** Seja objetivo(a). Lideranças têm pouco tempo. Use bullets e destaque os números importantes.

---

## Instruções de Entrega

### Passo 1: Fork do Repositório

1. Faça um **fork** deste repositório para sua conta pessoal do GitHub
2. Clone o fork para sua máquina local:
   ```bash
   git clone https://github.com/SEU_USUARIO/teste-cs-ops.git
   cd teste-cs-ops
   ```

### Passo 2: Realize o Teste

1. Preencha os arquivos na pasta `templates/`
2. Se criar scripts ou planilhas adicionais, coloque na pasta `entregas/`
3. Faça commits conforme avança (não precisa ser um commit por parte, mas queremos ver seu histórico)

### Passo 3: Envie sua Entrega

1. Faça push das suas alterações para o seu fork:
   ```bash
   git add .
   git commit -m "Entrega do teste técnico - [Seu Nome]"
   git push origin main
   ```
2. Envie o **link do seu repositório** por email para pedro@aegro.com.br
3. Certifique-se de que o repositório está **público** ou adicione o usuário `pmdusso` como colaborador

**Prazo:** 5 dias corridos a partir do recebimento

> 💡 **Dica:** Commits intermediários demonstram seu processo de pensamento e são bem vistos na avaliação!

---

## Critérios de Avaliação

| Parte | Peso | O que observamos |
|-------|------|------------------|
| Parte 1: SQL | 25% | Queries funcionam, JOINs corretos, lógica consistente |
| Parte 2: Health Score | 28% | Fórmula coerente, justificativas sólidas, implementação funcional |
| Parte 3: Análise | 23% | Identificação correta de riscos/oportunidades, ações viáveis |
| Parte 4: Memo | 18% | Clareza, objetividade, linguagem executiva |
| Git & Organização | 6% | Fork correto, histórico de commits, arquivos organizados |

---

## Pré-requisitos

- **Conta no GitHub** (gratuita) - para fazer o fork e entrega
- **Git instalado** na sua máquina ([instruções](https://git-scm.com/book/pt-br/v2/Come%C3%A7ando-Instalando-o-Git))
- **Cliente SQL** para consultar o banco SQLite

## Ferramentas Sugeridas

- **SQL:** DB Browser for SQLite, DBeaver, ou qualquer cliente SQL
- **Python:** Pandas, Jupyter Notebook (opcional)
- **Planilhas:** Excel, Google Sheets
- **Visualização:** O que preferir (não é obrigatório)

---

**Boa sorte! Estamos ansiosos para ver sua análise.** 🚀
