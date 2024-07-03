
import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO

# CSV data
csv_data = """Day,Interactions
1,15000
2,16000
3,17000
4,18000
5,17500
6,19000
7,20000
8,21000
9,22000
10,23000
11,22500
12,24000
13,24500
14,25000
15,26000
16,27000
17,28000
18,27500
19,28500
20,29000
21,30000
22,31000
23,32000
24,33000
25,32500
26,33500
27,34000
28,35000
29,35500
30,36000
31,37000"""

# Read data into a pandas DataFrame
data = pd.read_csv(StringIO(csv_data))

# Create figure and plot
fig, ax = plt.subplots(figsize=(16, 8))

# Fill area under the line
ax.fill_between(data['Day'], data['Interactions'], color="#FF5733", alpha=0.6, label='AI Chatbot Interactions')

# Labels and Titles
ax.set_xlabel('Day of the Month', fontsize=14)
ax.set_ylabel('Number of Interactions', fontsize=14)
ax.set_title('Daily Number of AI Chatbot Interactions Over a Month', fontsize=20, pad=30)

# Annotations
for i in range(0, len(data), 5):
    ax.text(data['Day'][i], data['Interactions'][i], str(data['Interactions'][i]), fontsize=10, verticalalignment='bottom')

# Legend
ax.legend(loc='upper right')

# Display
plt.show()