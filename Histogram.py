import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

df = pd.read_csv("BTC-USD.csv")
df = df.set_index('Date')
df['daily_changes'] = df['Adj Close'].pct_change(periods = 1)
sns.displot(df['daily_changes'].dropna(), bins=100, color='purple', kde=True, height = 6, aspect = 1.5)
plt.suptitle('Daily % return of BITCOIN (USD) price, 05-09-2021 to 04-09-2022', fontsize=12, color='black')
plt.grid(True)
plt.show()

print(df['daily_changes'].describe())