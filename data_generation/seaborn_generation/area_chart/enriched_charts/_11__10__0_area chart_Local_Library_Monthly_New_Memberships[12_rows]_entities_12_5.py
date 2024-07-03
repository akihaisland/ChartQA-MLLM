
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Month': ['Jan-2021', 'Feb-2021', 'Mar-2021', 'Apr-2021', 'May-2021', 
              'Jun-2021', 'Jul-2021', 'Aug-2021', 'Sep-2021', 'Oct-2021',
              'Nov-2021', 'Dec-2021', 'Jan-2022', 'Feb-2022', 'Mar-2022',
              'Apr-2022', 'May-2022', 'Jun-2022', 'Jul-2022', 'Aug-2022',
              'Sep-2022', 'Oct-2022', 'Nov-2022', 'Dec-2022'],
    'Daily_Steps': [7000, 7500, 7200, 7800, 7600, 8100, 8300, 8500, 8700, 8900,
                    9100, 9300, 9500, 9700, 9900, 10100, 10300, 10500, 10700, 10900, 
                    11100, 11300, 11500, 11700]
}

df = pd.DataFrame(data)

# Set the aesthetic style of the plots
sns.set_theme(style="whitegrid")

# Define the area chart
plt.figure(figsize=(14, 7))  # Change width and height
ax = sns.lineplot(data=df, x='Month', y='Daily_Steps', color="#1f77b4")  # Specific color code
ax.fill_between(df['Month'], df['Daily_Steps'], color="#1f77b4", alpha=0.3)

# Rotate x-axis labels for better readability
for item in ax.get_xticklabels():
    item.set_rotation(45)

# Add a title and labels
ax.set_title('Monthly Average Daily Steps Over Two Years', fontsize=20, pad=20)
ax.set_xlabel('Month', fontsize=12)
ax.set_ylabel('Daily Steps', fontsize=12)

# Annotate the chart with a sample text label
ax.annotate('Start of 2022', xy=('Jan-2022', 9500), xytext=('Feb-2022', 9800), fontsize=12,
            arrowprops=dict(facecolor='black', shrink=0.05),
            )

# Show the plot
plt.tight_layout()
plt.show()