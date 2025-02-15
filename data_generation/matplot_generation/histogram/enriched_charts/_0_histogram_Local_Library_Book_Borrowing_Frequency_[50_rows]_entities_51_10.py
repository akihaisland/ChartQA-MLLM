
import matplotlib.pyplot as plt

# Data points for the Ages of 300 individuals
ages = [
    23, 29, 31, 22, 24, 27, 33, 35, 22, 21, 30, 27, 38, 24, 26, 25, 32, 29, 28,
    34, 34, 36, 35, 31, 21, 23, 24, 25, 27, 30, 32, 33, 35, 37, 39, 22, 28, 26,
    23, 25, 35, 34, 33, 31, 29, 38, 36, 28, 32, 34, 35, 37, 24, 36, 25, 33, 22,
    28, 30, 31, 29, 37, 26, 21, 39, 40, 23, 24, 28, 32, 36, 35, 33, 29, 27, 25,
    31, 39, 23, 22, 26, 35, 34, 31, 28, 29, 30, 27, 22, 26, 39, 38, 37, 25, 24,
    23, 33, 31, 28, 29, 27, 26, 34, 32, 30, 35, 33, 31, 39, 37, 25, 22, 21, 28,
    29, 30, 27, 26, 34, 32, 31, 35, 36, 39, 38, 22, 24, 26, 28, 29, 31, 33, 35,
    37, 39, 25, 27, 30, 32, 34, 36, 38, 21, 23, 28, 30, 32, 34, 36, 22, 24, 26,
    27, 29, 31, 33, 35, 21, 23, 25, 28, 30, 32, 34, 36, 29, 31, 33, 35, 24, 26,
    28, 30, 21, 23, 25, 27, 29, 31, 33, 35, 38, 40, 24, 26, 28, 30, 32, 34, 36,
    38, 27, 29, 31, 33, 35, 37, 39, 22, 24, 26, 28, 30, 32, 34, 36, 29, 31, 33,
    35, 37, 39, 28, 30, 32, 34, 36, 38, 23, 25, 27, 29, 31, 33, 35, 37, 26, 28,
    30, 32, 34, 36, 38, 40, 22, 24, 26, 28, 30, 32, 34, 36, 38, 25, 27, 29, 31,
    33, 35, 37, 39
]

# Creating histogram
plt.figure(figsize=(10, 8)) # Changing width and height of the chart
plt.hist(ages, bins=range(20, 45, 1), orientation='horizontal', color='#607D8B', rwidth=0.8) # Modifying color, bins and orientation

plt.title('Age Distribution of a Group of Individuals') # Changing the topic/headline
plt.xlabel('Frequency') # Flipping the axis labels due to change in orientation
plt.ylabel('Age')

# Display the histogram
plt.show()