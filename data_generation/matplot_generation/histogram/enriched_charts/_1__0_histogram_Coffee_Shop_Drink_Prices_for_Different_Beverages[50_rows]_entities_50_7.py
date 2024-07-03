import matplotlib.pyplot as plt

# Data Points
exercise_hours = [
    2.5, 3.1, 3.6, 4.0, 4.5, 5.0, 5.3, 5.7, 6.0, 6.5, 7.0, 7.3, 7.8, 8.0, 8.5, 9.0, 9.3, 9.7, 10.0, 10.5,
    11.0, 11.5, 12.0, 12.5, 13.0, 13.5, 14.0, 14.5, 15.0, 15.5, 16.0, 16.5, 17.0, 17.5, 18.0, 18.5, 19.0, 19.5, 
    20.0, 20.5, 21.0, 21.5, 22.0, 22.5, 23.0, 23.5, 24.0, 24.5, 25.0, 25.5, 26.0, 26.5, 27.0, 27.5, 28.0, 28.5, 
    29.0, 29.5, 30.0, 30.5, 31.0, 31.5, 32.0, 32.5, 33.0, 33.5, 34.0, 34.5, 35.0, 35.5, 36.0, 36.5, 37.0, 37.5, 
    38.0, 38.5, 39.0, 39.5, 40.0, 40.5, 41.0, 41.5, 42.0, 42.5, 43.0, 43.5, 44.0, 44.5, 45.0, 45.5, 46.0, 46.5, 
    47.0, 47.5, 48.0, 48.5, 49.0, 49.5, 50.0
]

# Histogram Configuration
plt.figure(figsize=(12, 6))
plt.hist(exercise_hours, bins=25, orientation='vertical', color='#e74c3c', rwidth=0.8)
plt.title('Weekly Exercise Hours Distribution')
plt.xlabel('Exercise Hours')
plt.ylabel('Frequency')
plt.grid(axis='y', color='gray', linestyle='--', linewidth=0.5)

# Show the plot
plt.show()