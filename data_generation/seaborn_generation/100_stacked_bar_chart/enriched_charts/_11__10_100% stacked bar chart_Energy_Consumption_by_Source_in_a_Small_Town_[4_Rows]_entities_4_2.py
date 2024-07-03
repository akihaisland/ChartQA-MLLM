
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Input data
data = [
    {'Year': 2019, 'Work (%)': 35, 'Exercise (%)': 12, 'Sleep (%)': 33, 'Leisure (%)': 15, 'Other (%)': 5},
    {'Year': 2020, 'Work (%)': 38, 'Exercise (%)': 14, 'Sleep (%)': 30, 'Leisure (%)': 13, 'Other (%)': 5},
    {'Year': 2021, 'Work (%)': 40, 'Exercise (%)': 18, 'Sleep (%)': 25, 'Leisure (%)': 12, 'Other (%)': 5},
    {'Year': 2022, 'Work (%)': 37, 'Exercise (%)': 20, 'Sleep (%)': 26, 'Leisure (%)': 11, 'Other (%)': 6},
    {'Year': 2023, 'Work (%)': 39, 'Exercise (%)': 22, 'Sleep (%)': 23, 'Leisure (%)': 12, 'Other (%)': 4}
]

# Create a DataFrame
df = pd.DataFrame(data)

# Set the index to 'Year'
df.set_index('Year', inplace=True)

# Normalize data to 100%
df_normalized = df.div(df.sum(axis=1), axis=0) * 100

# Define colors for each stack
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Setup seaborn style
sns.set_style('whitegrid')

# Plotting
plt.figure(figsize=(10, 6))

# Creating the bar stacks
bottom = None
bar_width = 0.5
for (columnName, columnData), color in zip(df_normalized.iteritems(), colors):
    plt.bar(df_normalized.index, columnData, bottom=bottom, color=color, label=columnName, edgecolor='white', width=bar_width)
    bottom = columnData if bottom is None else bottom + columnData

# Add legend
plt.legend(title="Daily Activity")

# Formatting the plot
plt.title('Daily Routine Distribution Over the Years')
plt.xlabel('Year')
plt.ylabel('Activity Contribution (%)')
plt.yticks(range(0, 101, 10))
plt.xticks(df_normalized.index)
sns.despine()  # Remove the top and right spines

# Show the plot
plt.show()