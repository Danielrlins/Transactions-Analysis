import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine

# 1. Conexão com o PostgreSQL
engine = create_engine("postgresql+psycopg2://postgres:123@localhost:5432/meu_banco")

# 2. Ler dados da tabela
df = pd.read_sql("SELECT * FROM transacoes_pagamentos", con=engine)
df['data'] = pd.to_datetime(df['data'])

# ======================
# 3. Estatísticas gerais
# ======================
print("Total de transações:", len(df))
print("Valor médio das transações: R$", round(df['valor'].mean(), 2))
print("Distribuição por meio de pagamento:\n", df['meio_pagamento'].value_counts())

# ======================
# 4. Total de transações por meio de pagamento
# ======================
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x='meio_pagamento',
              order=df['meio_pagamento'].value_counts().index, palette='viridis')
plt.title("Número de Transações por Meio de Pagamento")
plt.xlabel("Meio de Pagamento")
plt.ylabel("Quantidade")
plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig("total-trasacao.png")
plt.show()

# ======================
# 5. Evolução mensal dos meios de pagamento
# ======================
df['ano_mes'] = df['data'].dt.to_period('M')
pagamentos_mensal = df.groupby(['ano_mes', 'meio_pagamento']).size().unstack()

pagamentos_mensal.plot(kind='line', figsize=(8, 5))
plt.title("Evolução Mensal dos Meios de Pagamento")
plt.xlabel("Ano-Mês")
plt.ylabel("Quantidade de Transações")
plt.legend(title="Meio de Pagamento")
plt.tight_layout()
plt.savefig("evolucao-pagamento.png")
plt.show()


# ======================
# 6. Valor total por meio de pagamento
# ======================
plt.figure(figsize=(6, 4))
sns.barplot(
    data=df,
    x='meio_pagamento',
    y='valor',
    estimator=lambda x: sum(x) / 1_000_000,  # converte para milhões
    palette='magma',
    order=df['meio_pagamento'].value_counts().index
)
plt.title("Valor Total por Meio de Pagamento (em Milhões R$)")
plt.xlabel("Meio de Pagamento")
plt.ylabel("Valor Total (R$ Milhões)")
plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig("valor-total-meio-pagamento.png")
plt.show()
print("Dados importados PostGreeSQl com sucesso e gráficos gerados com sucesso!")