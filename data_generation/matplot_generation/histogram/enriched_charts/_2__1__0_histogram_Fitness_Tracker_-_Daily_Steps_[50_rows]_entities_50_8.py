import matplotlib.pyplot as plt

# Data: page counts of books read
book_page_counts = [
    48, 52, 58, 60, 62, 65, 68, 70, 75, 78, 80, 82, 85, 88, 90, 92, 95, 98, 100, 102, 105, 108, 110, 112, 115, 118, 120, 122, 125, 128, 130, 132, 135, 138, 140, 142, 145, 148, 150, 152, 155, 158, 160, 162, 165, 168, 170, 172, 175, 178, 180, 182, 185, 188, 190, 192, 195, 198, 200, 202, 205, 208, 210, 212, 215, 218, 220, 222, 225, 228, 230, 232, 235, 238, 240, 242, 245, 248, 250, 252, 255, 258, 260, 262, 265, 268, 270, 272, 275, 278, 280, 282, 285, 288, 290, 292, 295, 298, 300, 302
]

plt.figure(figsize=(10, 6))

plt.hist(book_page_counts, bins=15, orientation='horizontal', color='#ff7f0e', rwidth=0.85)

plt.title('Distribution of Book Page Counts')
plt.ylabel('Page Counts')
plt.xlabel('Number of Books')

plt.show()