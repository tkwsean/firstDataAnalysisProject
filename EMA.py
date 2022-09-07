import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd


df = pd.read_csv('BTC-USD.csv')
print(df.head())

# create 20 days simple moving average column
df['EMA_20'] = df['Close'].ewm(span = 20, adjust = False).mean()

# create 50 days simple moving average column
df['EMA_50'] = df['Close'].ewm(span = 50, adjust = False).mean()

df.plot(x = "Date", y = ["Close", "EMA_20", "EMA_50"], kind = "line", figsize = (15, 8), title='Bitcoin Price in USD', xlabel= 'Date', ylabel= 'Price')
plt.show()