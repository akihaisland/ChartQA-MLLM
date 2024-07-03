
import seaborn as sns
import matplotlib.pyplot as plt

# Data: Number of books read by students in a year
books_read_data = [7.5, 8.3, 9.1, 10.2, 7.8, 8.4, 9.3, 10.5, 7.9, 8.6, 9.0, 10.1, 7.2, 8.1, 9.4, 10.3, 7.6, 8.5, 9.5, 10.0, 7.3, 8.7, 9.6, 10.8, 7.4, 8.2, 9.7, 10.6, 7.1, 8.0, 9.2, 10.4, 7.7, 8.9, 9.8, 10.9, 7.0, 8.8, 9.9, 11.0, 7.6, 8.1, 9.5, 10.3, 7.2, 8.4, 9.1, 10.2, 7.3, 8.3, 9.6, 10.8, 7.9, 8.7, 9.9, 11.0, 7.8, 8.6, 9.4, 10.7]

# Set the size of the chart
plt.figure(figsize=(12, 6))

# Create a histogram with horizontal orientation
sns.histplot(data=books_read_data, kde=False, color="#3498db", binwidth=0.4, orientation='horizontal')

# Set chart title and labels
plt.title('Number of Books Read by Students in a Year')
plt.xlabel('Frequency')
plt.ylabel('Number of Books')

# Show the plot
plt.show()