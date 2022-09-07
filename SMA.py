import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd


df = pd.read_csv('BTC-USD.csv')
print(df.head())

# create 20 days simple moving average column
df['SMA_20'] = df['Close'].rolling(window = 20, min_periods = 1).mean()

# create 50 days simple moving average column
df['SMA_50'] = df['Close'].rolling(window = 50, min_periods = 1).mean()

df.plot(x = "Date", y = ["Close", "SMA_20", "SMA_50"], kind = "line", figsize = (15, 8), title='Bitcoin Price in USD', xlabel= 'Date', ylabel= 'Price')
plt.show()