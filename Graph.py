import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

df = pd.read_csv('BTC-USD.csv')

def plot_df(df, x, y, title="", xlabel='', ylabel=''):
    plt.figure(figsize=(16,5))
    plt.plot(x, y, color='tab:red')
    plt.gca().set(title=title, xlabel=xlabel, ylabel=ylabel)
    plt.show()


df.plot(x = "Date", y = ["Close"], kind = "line", figsize = (15, 8), title='Bitcoin Price in USD', xlabel= 'Date', ylabel= 'Price')
plt.show()