import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import mplfinance as mpf
import yfinance as yf
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Coletar dados financeiros do ano passado da Petrobas
df_dados = yf.download("PETR4.SA", start="2023-01-01", end="2023-12-31")
df = df_dados.head(60).copy()
# converte o indice em uma coluna
df['Data'] = df.index
# converte as datas para formato numerico para plotagem correta pleo matplotlib
df['Data'] = df['Data'].apply(mdates.date2num)

# definição do gráfico, inicialmente em branco
fig, ax = plt.subplots(figsize=(15, 8))

# largura dos candles
width = 0.7

for i in range(len(df)):
    # Determinando a cor do candle
    # Se preço de fechamento for maior que o de abertura, candle é verde (ação valorizou)
    # senão o candle será vermelho (ação desvalorizou)
    if df['Fechamento'].iloc[i] > df['Abertura'].iloc[i]:
        color = 'green'
    else:
        color = 'red'
        
    # Desenhando linha vertical do candle
    # mostra os preços máximo e mínimo do dia
    # ax desenha a linha vertical
    ax.plot(
        [
            df['Data'].iloc[i], 
             df['Data'].iloc[i]
        ],
        [
            df['Minimo'].iloc[i], 
             df['Maximo'].iloc[i]
        ],
         color=color,
         linewidth=1)
    
    ax.add_patch(plt.Rectangle(
        (
            df['Data'].iloc[i] - width / 2, 
             min(df['Abertura'].iloc[i], 
             df['Fechamento'].iloc[i])
        ),
             width,
             abs(df['Fechamento'].iloc[i] - df['Abertura'].iloc[i]),
             facecolor=color))
    
df['MA7'] = df['Fechamento'].rolling(window=7).mean()
df['MA14'] = df['Fechamento'].rolling(window=14).mean()

# Plotando médias móveis
ax.plot(df['Data'], df['MA7'], color='orange', label='Média móvel 7 Dias') # Média de 7 dias
ax.plot(df['Data'], df['MA14'], color='yellow', label='Média móvel 14 Dias') # Média de 14 dias
# Adicionando legendas para as médias móveis
ax.legend()

# Formatando o eixo X para mostrar datas corretas
ax.xaxis_date() # informa que as datas estão no eixo X
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.xticks(rotation=45)

# adicionando título e rótulos para os eixos X e Y
plt.title("Gráfico de Candlestick - PETR4.SA com matplotlib")
plt.xlabel('Data')
plt.ylabel('Preço')

# Adicionando uma grade para facilitar a visialização dos valores
plt.grid(True)

# Exibindo o gráfico
plt.show()
