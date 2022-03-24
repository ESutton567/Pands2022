# This program adds a legend to agesSalariesColour(ASC)
# and saves it to prettier-plot.png
# Author: Éilis Sutton

import numpy as np
import matplotlib.pyplot as plt

minSalary = 20000
maxSalary = 80000
numberOfEntries = 100

np.random.seed(1) 
salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)
ages = np.random.randint(low=21, high=65, size=numberOfEntries) # better to have absolute values set first

plt.scatter(ages, salaries, label = 'salaries') 
# plt.show() # if you do this here the program will stop here until the plot is closed

# add x squared
xpoints = np.array(range(1,101))
ypoints = xpoints * xpoints

plt.plot(xpoints, ypoints, color='g', label = 'x-squared')

plt.title('random plot')
plt.xlabel('Salaries')
plt.ylabel('Age')
plt.legend()
# plt.show() # can run either show or save, not both

plt.savefig('prettier-plot.png')