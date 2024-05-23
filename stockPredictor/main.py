# import math
# import pandas_datareader as web
# import numpy as np
# import pandas as pd
# from sklearn.preprocessing import MinMaxScaler
# from keras import layers
# from keras import models
# import matplotlib.pyplot as plt
import yfinance as yf
# plt.style.use('fivethirtyeight')

sp500 = yf.Ticker("AAPL")
sp500 = sp500.history(period = "max")
# print(sp500)

# print(sp500.index)

print(sp500.plot.line(y = "Close", use_index = True))
