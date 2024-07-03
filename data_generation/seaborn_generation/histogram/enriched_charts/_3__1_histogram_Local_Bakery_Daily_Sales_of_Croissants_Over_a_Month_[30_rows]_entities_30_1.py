
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data
step_data = {'Daily_Steps': [3200, 4500, 5100, 5500, 6000, 6200, 6400, 6800, 7200, 7500, 
                             7800, 8000, 8500, 8700, 9000, 9200, 9400, 9600, 9800, 10000,
                             10200, 10500, 10700, 11000, 11200, 11500, 11700, 12000, 12200, 
                             12500, 12800, 13000, 13200, 13500, 13700, 14000, 14300, 14500, 
                             14800, 15000, 15300, 15500, 15800, 16000, 16300, 16500, 16800, 
                             17000, 17300, 17500, 17800, 18000, 18300, 18500, 18800, 19000, 
                             19300, 19500, 19800, 20000, 20300, 20500, 20800, 21000, 21300, 
                             21500, 21800, 22000, 22300, 22500, 22800, 23000, 23300, 23500, 
                             23800, 24000, 24300, 24500, 24800, 25000, 25300, 25500, 25800, 
                             26000, 26300, 26500, 26800, 27000, 27300, 27500, 27800, 28000, 
                             28300, 28500, 28800, 29000, 29300, 29500, 29800, 30000]}
df = pd.DataFrame(step_data)

# Set size of the figure
plt.figure(figsize=(12, 8))

# Plotting the histogram
sns.histplot(data=df, y='Daily_Steps', binwidth=2000, color='#FF5733', edgecolor='#2E2E2E')

# Additional customizations
plt.title('Daily Step Count Distribution')
plt.xlabel('Frequency')
plt.ylabel('Daily Steps')
plt.grid(True)

# Show the plot
plt.show()