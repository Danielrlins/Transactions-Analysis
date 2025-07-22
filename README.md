# 📊 Análise de Transações com Python & PostgreSQL  

Este projeto tem como objetivo realizar uma **análise exploratória de dados (EDA)** de transações financeiras armazenadas em um banco **PostgreSQL**, utilizando **Python, Pandas, Matplotlib e Seaborn** para gerar gráficos e insights.

---

## 🚀 **Principais Funcionalidades**
- **Conexão com banco de dados PostgreSQL** via SQLAlchemy.  
- **Estatísticas gerais**:
  - Quantidade total de transações.
  - Valor médio das transações.
  - Distribuição por meio de pagamento.
- **Visualizações gráficas**:
  - Número de transações por meio de pagamento.
  - Evolução mensal dos meios de pagamento.
  - Valor total por meio de pagamento (em milhões de R$).

---

## 🛠 **Tecnologias Utilizadas**
- **Linguagem:** Python 3  
- **Bibliotecas:**
  - `pandas`
  - `matplotlib`
  - `seaborn`
  - `sqlalchemy`
  - `psycopg2`
- **Banco de Dados:** PostgreSQL

---

## ⚡ **Como Executar o Projeto**
 **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/analise-transacoes-postgres.git
   cd analise-transacoes-postgres

## **Crie um ambiente virtual e instale as dependências:**

```bash
  python -m venv venv
  source venv/bin/activate    # Linux/Mac
  venv\Scripts\activate       # Windows
  pip install -r requirements.txt 
```

## **Configure a conexão com o banco PostgreSQL**:

```No arquivo analise_transacoes.py, altere a linha:

  engine = create_engine("postgresql+psycopg2://usuario:senha@localhost:5432/nome_do_banco")

```
##  **Execute o script**:

python analise_transacoes.py

## **🖼 Exemplo de Gráfico**:
Você pode gerar gráficos como estes:
    ![Gráfico de Evolução de Pagamento](assets/evolucao-pagamento.png)

--
    ![Gráfico de Transações Totais](assets/total-trasacao.png)
--
    ![Gráfico de Valor Total por meio de pagamento](assets/valor-total-meio-pagamento.png)
---