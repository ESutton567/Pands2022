# This program demonstrates how to make a pie plot of the unique occurances of values in an array
# Author: Éilis Sutton

import numpy as np
import matplotlib.pyplot as plt

# make an array of occurences
possibleCounties = ['Dublin', 'Wexford', 'Antrim', 'Laois', 'Wicklow']
# pick 100 randomly from possible counties with the frequency set in p
counties = np.random.choice(
    possibleCounties , 
    p=[0.1, 0.3, 0.2, 0.12, 0.28],
    size=(100)
)

# now we need the number of occurences of each county
# this returns a tuple of the unique value and how many times they appear
unique, counts = np.unique(counties, return_counts=True)
# we can now put this into a pie plot
plt.pie(counts, labels=unique)

plt.show()
