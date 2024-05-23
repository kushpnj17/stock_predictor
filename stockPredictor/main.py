import numpy as np
import pandas as pd
import math
import pandas_datareader as web
from sklearn.preprocessing import MinMaxScaler
from keras import layers
from keras import models
import matplotlib.pyplot as plt
import yfinance as yf

Apple = yf.Ticker("AAPL")
Apple = Apple.history(period="max")
print(Apple)

print(Apple.index)