# Criando manualmente o gráfico

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import mplfinance as mpf
import yfinance as yf
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Coletar dados financeiros do ano passado da Petrobas
df_dados = yf.download("PETR4.SA", start="2023-01-01", end="2023-12-31")

# Traduzir colunas
df_dados.columns = ['Abertura', 'Maximo', 'Minimo', 'Fechamento', 'Fech_Ajustado', 'Volume']

# Traduzir o índice
df_dados = df_dados.rename_axis("Data")
# Variação do preço por data
df_dados['Fechamento'].plot(figsize=(10,6))
plt.title('Variação do preço por data', fontsize=16)
plt.legend(['Fechamento'])
