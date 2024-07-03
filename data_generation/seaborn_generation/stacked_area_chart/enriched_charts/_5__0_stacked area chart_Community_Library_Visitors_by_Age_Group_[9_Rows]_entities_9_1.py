
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Data
data = {
    'Year': [i for i in range(2000, 2022)],
    'Manufacturing': [5000 + 100 * i for i in range(22)],
    'Research': [1500 + 100 * i for i in range(22)],
    'Development': [1200 + 100 * i for i in range(22)],
    'Marketing': [800 + 100 * i for i in range(22)],
    'Sales': [600 + 100 * i for i in range(22)],
}
df = pd.DataFrame(data)

# Melting the data to long format
df_melted = df.melt('Year', var_name='Sector', value_name='Expenses')

# Pivot for cumulative sum to stack the sectors on top of each other
df_melted['Cumulative'] = df_melted.groupby('Year')['Expenses'].cumsum()

# Plot
plt.figure(figsize=(14, 7))
colors = ["#FF5733", "#33FF57", "#3357FF", "#FF33A1", "#57FF33"]

# Loop to create the stacked area plot
for i, sector in enumerate(df_melted['Sector'].unique()):
    if i == 0:
        plt.fill_between(df['Year'], 0, df_melted[df_melted['Sector'] == sector]['Cumulative'], color=colors[i], label=sector)
    else:
        plt.fill_between(df['Year'], 
                         df_melted[df_melted['Sector'] == df_melted['Sector'].unique()[i-1]]['Cumulative'], 
                         df_melted[df_melted['Sector'] == sector]['Cumulative'], 
                         color=colors[i], label=sector)

# Annotating the last value of Manufacturing for example
last_year_data = df_melted[df_melted['Year'] == df['Year'].max()]
manufacturing_last_value = last_year_data[last_year_data['Sector'] == 'Manufacturing']['Cumulative'].values[0]
plt.text(df['Year'].max(), manufacturing_last_value - 250, "Manufacturing", verticalalignment='center', horizontalalignment='center', color="white", fontsize=10)

# Customizing the plot
plt.title("Corporate Expenses Over Time by Department", fontsize=16)
plt.xlabel("Year")
plt.ylabel("Expenses (Million USD)")
plt.legend(loc='upper left')
sns.despine()
plt.show()