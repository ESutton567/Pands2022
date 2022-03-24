# This program scatter plots the salaries (from lab8.1-salaries.py)
# and ages that have the same number random values as salaries (range 21-65)
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
plt.show()