# utiliza aprendizado de máquina para criar um gráfico mostrando linhas de dados reais, para prever valores futuros durante um período de
# 12 meses.

import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from prophet import Prophet

# Baixar dados dos últimos quatro anos para uma ação específica
dados = yf.download("JNJ", start="2020-01-01", end="2023-12-31", progress=False)
dados = dados.reset_index()

# Divisão entre dados de treino (até o final do primeiro semestre de 2023) e teste (segundo semestre de 2023)
dados_treino = dados[dados['Date'] < '2023-07-01']
dados_teste = dados[dados['Date'] >= '2023-07-31']

# separando 2 colunas para o modelo, renomeando para 'ds' e 'y'
dados_propetht_treino = dados_treino[['Date', 'Close']].rename(columns={'Date':'ds', 'Close':'y'})

# instanciando Propeth, semanalmente e anuamente como True, diariamente como False
modelo = Prophet(weekly_seasonality=True, yearly_seasonality=True, daily_seasonality=False)

# incluindo feriados nacionais americanos
modelo.add_country_holidays(country_name='US')
modelo.fit(dados_propetht_treino)

# criar datas futuras parea previsão até o final de 2023
futuro = modelo.make_future_dataframe(periods=150)
previsao = modelo.predict(futuro)

# plotar gráfico
plt.figure(figsize=(14,8))
# Eixo X
plt.plot(dados_treino['Date'], dados_treino['Close'], label='Dados de Treino', color='blue')
# Eixo Y
plt.plot(dados_teste['Date'], dados_teste['Close'], label='Dados Reais (Teste)', color='green')
# Linha de previsão
plt.plot(previsao['ds'], previsao['yhat'], label='Previsão', color='orange', linestyle='--')

plt.axvline(dados_treino['Date'].max(), color='red', linestyle='--', label='Início da Previsão')
plt.xlabel('Data')
plt.ylabel('Preço de Fechamento')
plt.title('Previsão de Preço de Fechamento vs Dados Reais')
plt.legend()
plt.show()
