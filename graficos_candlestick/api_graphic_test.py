import mplfinance as mpf
import yfinance as yf

df_dados = yf.download("PETR4.SA", start="2023-01-01", end="2023-12-31")
mpf.plot(df_dados.head(30), type='candle', figsize=(16,8), volume=True, mav=(7,14), style="brasil")
