
import matplotlib.pyplot as plt

# Data points
data = [
    83, 29, 31, 32, 30, 21, 54, 67, 71, 26, 32, 29, 33, 56, 63, 41, 64, 23, 35, 27,
    31, 39, 53, 66, 48, 21, 24, 37, 29, 31, 52, 19, 22, 33, 47, 68, 21, 40, 35, 34,
    36, 27, 26, 38, 44, 49, 53, 63, 73, 72, 45, 34, 58, 39, 40, 44, 50, 53, 26, 38,
    57, 66, 28, 30, 42, 49, 55, 39, 43, 47, 51, 22, 28, 38, 25, 31, 57, 64, 43, 42,
    51, 63, 69, 32, 36, 40, 41, 53, 56, 67, 70, 71, 37, 44, 61, 68, 32, 55, 59, 41,
    46, 49, 55, 33, 38, 46, 50, 62, 72, 35, 42, 47, 53, 29, 37, 40, 44, 55, 60, 25,
    28, 32, 39, 43, 49, 50
]

# Define the number of bins and their edges
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Histogram chart settings
plt.figure(figsize=(10, 6))  # Width and height of the chart
plt.hist(data, bins=bins, orientation='vertical', color='#FF6347', rwidth=0.75)

# Titles and labels
plt.title('Popularity of Different Book Genres')
plt.xlabel('Ages')
plt.ylabel('Number of People')

# Set limit on vertical axis to enforce uniform bar height
plt.ylim(0, max([data.count(i) for i in range(0, 101)]) + 1)

# Display the histogram
plt.show()