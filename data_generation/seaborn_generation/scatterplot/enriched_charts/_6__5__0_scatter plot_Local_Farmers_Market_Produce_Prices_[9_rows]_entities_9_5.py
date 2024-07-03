
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO

data = '''
Date,StockPrice,TradingVolume
2024-01-01,150,80000
2024-01-02,155,85000
2024-01-03,152,82000
2024-01-04,160,87000
2024-01-05,158,86000
2024-01-06,162,89000
2024-01-07,165,91000
2024-01-08,160,88000
2024-01-09,168,92000
2024-01-10,170,93000
2024-01-11,172,95000
2024-01-12,160,88000
2024-01-13,175,97000
2024-01-14,158,86000
2024-01-15,180,100000
2024-01-16,182,101000
2024-01-17,178,99000
2024-01-18,185,104000
2024-01-19,180,100000
2024-01-20,188,106000
2024-01-21,190,108000
2024-01-22,195,110000
2024-01-23,192,109000
2024-01-24,198,112000
2024-01-25,200,114000
2024-01-26,202,115000
2024-01-27,198,112000
2024-01-28,205,118000
2024-01-29,210,120000
2024-01-30,215,122000
2024-01-31,220,125000
'''

df = pd.read_csv(StringIO(data), parse_dates=['Date'])

plt.figure(figsize=(14, 8))

sns.scatterplot(data=df, x='Date', y='StockPrice', size='TradingVolume',
                sizes=(50, 500), hue='TradingVolume', 
                palette=["#FF5733", "#33FF57", "#3357FF", "#F333FF", "#FF33A1", "#33FFD7", "#FFA833"])

plt.title('Daily Stock Prices and Trading Volume', fontsize=20, y=1.02)
plt.xlabel('Date', fontsize=16)
plt.ylabel('Stock Price', fontsize=16)

plt.show()