import pandas as pd
import yfinance as yf
from datetime import date, timedelta
from matplotlib import pyplot as plt

stock = input("View which stock?: ") 
print("this one? " + stock)

Start = date.today() - timedelta(365)
Start.strftime('%Y-%m-%d')

End = date.today() + timedelta(2)
End.strftime('%Y-%m-%d')

def closing_price(ticker):
    Asset = pd.DataFrame(yf.download(ticker, start=Start,
      end=End)['Adj Close'])     
    return Asset

stockInfo = closing_price(stock)
plt.plot(stockInfo)
plt.title(stock)
plt.show()
