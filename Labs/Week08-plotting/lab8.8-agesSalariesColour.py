# This program takes lab.8.7-agesSalaries.py and shows y=xE2 in a different colour
# Author: Éilis Sutton

import numpy as np
import matplotlib.pyplot as plt

minSalary = 20000
maxSalary = 80000
numberOfEntries = 100

np.random.seed(1) 
salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)
ages = np.random.randint(low=21, high=65, size=numberOfEntries) # better to have absolute values set first

plt.scatter(ages, salaries) # this will be random
# plt.show() # if you do this here the program will stop here until the plot is closed

# add x squared
xpoints = np.array(range(1,101))
ypoints = xpoints * xpoints

plt.plot(xpoints, ypoints, color='g')
plt.show()
