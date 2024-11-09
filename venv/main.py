import yfinance as yf
AAPL_stock = yf.Ticker('AAPL').history(period='3mo',interval='1d')
print(AAPL_stock)

import seaborn as sns
sns.lineplot(data=AAPL_stock, x='Date', y="Close")

import matplotlib.ticker as ticker
ax = sns.lineplot(data=AAPL_stock, x='Date', y="Close")
ax.xaxis.set_major_locator(ticker.MultipleLocator(25))