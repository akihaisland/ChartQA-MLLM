
import matplotlib.pyplot as plt

# Data representing time spent on a particular activity
time_spent = [
    45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120,
    125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180, 185, 190,
    195, 200, 205, 210, 215, 220, 225, 230, 235, 240, 245, 250, 255, 260,
    265, 270, 275, 280, 285, 290, 295, 300, 305, 310, 315, 320, 325, 330,
    335, 340, 345, 350, 355, 360, 365, 370, 375, 380, 385, 390, 395, 400,
    405, 410, 415, 420, 425, 430, 435, 440, 445, 450, 455, 460, 465, 470,
    475, 480, 485, 490, 495, 500, 505, 510, 515, 520, 525, 530, 535, 540,
    545, 550, 555, 560, 565, 570, 575, 580, 585, 590, 595, 600
]

# Set figure size
plt.figure(figsize=(14, 10))

# Create a vertical histogram with modified color and bin width
plt.hist(time_spent, bins=20, color='#FF4500', edgecolor='#000000', linewidth=1.2)

# Set the chart title and labels
plt.title('Distribution of Time Spent on a Project')
plt.xlabel('Time Spent (hours)')
plt.ylabel('Frequency')

# Customize the tick marks
plt.xticks(range(0, 700, 50))
plt.yticks(range(0, 15, 1))

# Display the plot
plt.show()