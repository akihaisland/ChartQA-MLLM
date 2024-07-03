import matplotlib.pyplot as plt

age_data = [
    25, 34, 42, 19, 27, 33, 45, 38, 29, 36, 41, 23, 21, 28, 39, 35, 47, 26, 32, 22,
    30, 40, 24, 31, 37, 44, 46, 20, 48, 43, 50, 49, 18, 51, 17, 52, 53, 16, 15, 54,
    14, 55, 13, 12, 56, 57, 11, 58, 10, 59, 60, 9, 8, 61, 62, 63, 7, 6, 64, 65, 5,
    4, 66, 67, 3, 2, 68, 69, 70, 1, 71
]

plt.figure(figsize=(10, 8))
plt.hist(age_data, bins=15, color="#3498DB", orientation='horizontal', rwidth=0.7)
plt.title('Age Distribution in a Community', pad=20)
plt.xlabel('Frequency')
plt.ylabel('Age')
plt.grid(axis='x', linestyle='--')
plt.show()