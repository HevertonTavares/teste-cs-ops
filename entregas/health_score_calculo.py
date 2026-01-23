import pandas as pd
import numpy as np
from pathlib import Path

# Health Score 0 a 100 usando janela de 3 meses mais recentes do dataset outubro, novembro e dezembro de 2024
BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"
OUT_DIR = BASE_DIR / "entregas"

clientes = pd.read_csv(DATA_DIR / "clientes.csv")
uso = pd.read_csv(DATA_DIR / "uso_mensal.csv")
eventos = pd.read_csv(DATA_DIR / "eventos.csv")

meses_janela = ["2024-10", "2024-11", "2024-12"]

# Identificar churn
churned = set(eventos.loc[eventos["tipo"] == "churn", "cliente_id"].unique())

# Contagem de módulos contratados
clientes["modulos_contratados_n"] = clientes["modulos_contratados"].fillna("").apply(
    lambda s: len([x for x in str(s).split(",") if x.strip()])
)

uso_janela = uso[uso["mes"].isin(meses_janela)].copy()

agg = uso_janela.groupby("cliente_id").agg(
    avg_logins=("logins", "mean"),
    avg_users_active=("usuarios_ativos", "mean"),
    avg_modules_used=("modulos_usados", "mean"),
    avg_tickets=("tickets_suporte", "mean"),
    avg_actions=("acoes_realizadas", "mean"),
).reset_index()

df = clientes.merge(agg, left_on="id", right_on="cliente_id", how="left")

for col in ["avg_logins", "avg_users_active", "avg_modules_used", "avg_tickets", "avg_actions"]:
    df[col] = df[col].fillna(0)

def pct_rank(s):
    return s.rank(pct=True, method="average") * 100

df["freq_score"] = pct_rank(df["avg_logins"])
df["engagement_score"] = pct_rank(df["avg_actions"])

# Opcional, garante 0 quando não existe uso
df.loc[df["avg_logins"] == 0, "freq_score"] = 0
df.loc[df["avg_actions"] == 0, "engagement_score"] = 0

df["depth_ratio"] = (
    df["avg_users_active"] / df["usuarios_contratados"].replace(0, np.nan)
).fillna(0).clip(0, 1)
df["depth_score"] = df["depth_ratio"] * 100

df["breadth_ratio"] = (
    df["avg_modules_used"] / df["modulos_contratados_n"].replace(0, np.nan)
).fillna(0).clip(0, 1)
df["breadth_score"] = df["breadth_ratio"] * 100

p90 = df["avg_tickets"].quantile(0.9)
if not np.isfinite(p90) or p90 <= 0:
    p90 = 1.0
df["support_score"] = (100 - (df["avg_tickets"] / p90 * 100)).clip(0, 100)

weights = dict(
    freq_score=0.25,
    breadth_score=0.20,
    depth_score=0.20,
    engagement_score=0.20,
    support_score=0.15,
)

df["health_score"] = 0
for k, w in weights.items():
    df["health_score"] += df[k] * w

df["health_score"] = df["health_score"].clip(0, 100).round(2)

# Somente clientes ativos
df_active = df[~df["id"].isin(churned)].copy()

out_cols = [
    "id", "nome", "segmento", "plano", "mrr", "csm_responsavel", "estado",
    "health_score", "freq_score", "breadth_score", "depth_score", "engagement_score", "support_score",
]
df_active[out_cols].to_csv(OUT_DIR / "health_scores.csv", index=False)

print("Arquivo gerado em entregas/health_scores.csv")
