
import matplotlib.pyplot as plt

# Data
values = [
    12, 20, 25, 30, 35, 40, 42, 45, 48, 50, 52, 55, 60, 62, 65, 70, 75, 80, 82, 85,
    87, 90, 92, 95, 97, 100, 102, 105, 107, 110, 115, 120, 125, 130, 132, 135, 137, 
    140, 145, 150, 152, 155, 157, 160, 165, 170, 175, 180, 182, 185, 187, 190, 195, 
    200, 203, 205, 207, 210, 215, 220, 225, 227, 230, 235, 240, 242, 245, 248, 250, 
    255, 260, 265, 270, 272, 275, 277, 280, 285, 290, 295, 300, 305, 310, 315, 320, 
    325, 330, 335, 340, 345, 350, 355, 360, 365, 370, 375, 380, 385, 390, 395, 400, 
    405, 410, 415, 420, 425, 430, 435, 440, 445, 450, 455, 460, 465, 470, 475, 480, 
    485, 490, 495, 500
]

# Create histogram
plt.figure(figsize=(10, 8))
plt.hist(values, bins=30, color='#1f77b4', orientation='horizontal', rwidth=0.85)

# Customize chart
plt.title('Distribution of Monthly Sales ($ in thousands)')
plt.xlabel('Frequency')
plt.ylabel('Monthly Sales')
plt.grid(axis='x', color='gray', linestyle='--', linewidth=0.5)

plt.show()