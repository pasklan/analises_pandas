import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import mplfinance as mpf
import yfinance as yf
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Criando subplots

"""
Cria uma figura que conterá o gráfico usando make_subplots
Teremos multiplos gráficos em uma única visualização, um gráfico candlestick e outro para o volume de transações

"""

fig = make_subplots(
    rows=2, cols=1, 
    shared_xaxes=True, 
    vertical_spacing=0.1, 
    subplot_titles=('Candlesticks', 'Volume de Transações'),
    row_width=[0.2, 0.7])

"""
Cada cancle representa um dia de negociação, mostrando o preço de abertura, fechamento, máximo e mínimo. 
Vamos adicionar este gráfico à figura
"""

# Adicionando o gráfico
fig.add_trace(go.Candlestick(
    x=df.index,
    open=df['Abertura'],
    high=df['Maximo'],
    low=df['Minimo'],
    close=df['Fechamento'],
    name='Candlestick'),
    row=1, col=1)

# Adicionando as médias móveis
fig.add_trace(go.Scatter(
    x=df.index,
    y=df['MA7'],
    mode='lines',
    name='MA7 - Média Móvel 7 Dias'),
    row=1, col=1)

# Adicionando as médias móveis
fig.add_trace(go.Scatter(
    x=df.index,
    y=df['MA14'],
    mode='lines',
    name='MA17 - Média Móvel 14 Dias'),
    row=1, col=1)

# adicionando o gráfico de barras
fig.add_trace(go.Bar(
    x=df.index,
    y=df['Volume'],
    name='Volume'),
    row=2, col=1)


# Atualizando o layout, configurando titulo, formatando eixo
fig.update_layout(yaxis_title='Preço',
          xaxis_rangeslider_visible=False, # desativa o range slider
          width=1100, height=600)

# Exibe gráficos
fig.show()

