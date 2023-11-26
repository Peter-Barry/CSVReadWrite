# Event: LCCS Python Fundamental Skills Workshop
# Date: May 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: A program to calculate the average height of 5 people
#          The heights are stored in a file called 'heights.csv'
#          You should download 'heights.csv' before running this program

import pandas as pd
import numpy as np
with open("heights.csv", "r") as heightFile:
    totalHeight = 0
    print("line", heightFile.readline())
#     height = int(heightFile.readline())
#     totalHeight += height
"""
totalHeight = 0  # Initialise a running total to zero

print("line", heightFile.readline())  # Read and print the first line
height = int(heightFile.readline())  # Read the first height value
totalHeight = totalHeight + height  # Keep a running total



height = float(heightFile.readline())   # read the next value
totalHeight = totalHeight + height      # keep a running total

height = float(heightFile.readline())   # read the next value
totalHeight = totalHeight + height      # keep a running total

height = float(heightFile.readline())   # read the next value
totalHeight = totalHeight + height      # keep a running total

height = float(heightFile.readline())   # read the next value
totalHeight = totalHeight + height      # keep a running total

# Calculate the average
avgHeigth = totalHeight/5

# Display the result
print("The average height is "+str(round(avgHeigth,2))+"cm")
print("The average height is", round(avgHeigth*0.393701,2), "inches")
"""

heightFile.close()