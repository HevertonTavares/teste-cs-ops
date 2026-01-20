"""
Exemplo de Estrutura para Health Score
======================================

Este arquivo é um EXEMPLO OPCIONAL de como estruturar o cálculo do Health Score.
Você NÃO precisa usar Python - pode usar Excel, Google Sheets ou outra ferramenta.

Se usar Python, sinta-se livre para modificar completamente esta estrutura.
"""

import pandas as pd

# Carregar dados
clientes = pd.read_csv("../data/clientes.csv")
uso_mensal = pd.read_csv("../data/uso_mensal.csv")

# Filtrar apenas o último mês de uso (ou últimos N meses)
ultimo_mes = uso_mensal["mes"].max()
uso_recente = uso_mensal[uso_mensal["mes"] == ultimo_mes]

# Juntar dados de clientes com uso
df = clientes.merge(uso_recente, left_on="id", right_on="cliente_id", how="left")


# =============================================================================
# DEFINA SUAS FUNÇÕES DE CÁLCULO AQUI
# =============================================================================

def calcular_componente_frequencia(row):
    """
    Exemplo: Frequência de uso baseada em logins.

    TODO: Implemente sua lógica aqui.
    - Considere normalizar pela quantidade de usuários contratados
    - Defina o que é "bom" e "ruim" para logins
    """
    # Seu código aqui
    pass


def calcular_componente_amplitude(row):
    """
    Exemplo: Amplitude de uso (módulos usados vs contratados).

    TODO: Implemente sua lógica aqui.
    """
    # Seu código aqui
    pass


def calcular_componente_profundidade(row):
    """
    Exemplo: Profundidade (usuários ativos vs contratados).

    TODO: Implemente sua lógica aqui.
    """
    # Seu código aqui
    pass


def calcular_health_score(row):
    """
    Função principal que calcula o Health Score.

    TODO: Combine os componentes com seus pesos.
    """
    # Exemplo de estrutura:
    # freq = calcular_componente_frequencia(row)
    # ampl = calcular_componente_amplitude(row)
    # prof = calcular_componente_profundidade(row)
    #
    # PESO_FREQ = 0.XX
    # PESO_AMPL = 0.XX
    # PESO_PROF = 0.XX
    #
    # health_score = (freq * PESO_FREQ) + (ampl * PESO_AMPL) + (prof * PESO_PROF)
    #
    # return min(100, max(0, health_score))  # Garantir escala 0-100

    pass


# =============================================================================
# APLICAR CÁLCULO
# =============================================================================

# df["health_score"] = df.apply(calcular_health_score, axis=1)


# =============================================================================
# ANÁLISE DA DISTRIBUIÇÃO
# =============================================================================

# print("Estatísticas do Health Score:")
# print(df["health_score"].describe())

# print("\nDistribuição por faixa:")
# bins = [0, 30, 60, 100]
# labels = ["Crítico", "Atenção", "Saudável"]
# df["faixa"] = pd.cut(df["health_score"], bins=bins, labels=labels)
# print(df["faixa"].value_counts())


# =============================================================================
# EXPORTAR RESULTADOS
# =============================================================================

# df.to_csv("../entregas/health_scores.csv", index=False)
# print("\nResultados salvos em entregas/health_scores.csv")
