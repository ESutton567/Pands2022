# This program makes a list of salaries with 10 random numbers between 20000-80000
# Author: Éilis Sutton

import numpy as np
# set absolute values into variables at the begining of the program
minSalary = 20000
maxSalary = 80000
numberOfEntries = 10

np.random.seed(1) # modifes program so random numbers are the same each time (easier to debug)
salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)
print (salaries)

salariesPlus = salaries + 5000 # matrix operation
print (salariesPlus)

salariesMult = salaries * 1.05
print(salariesMult) # this is a float array.
# Convert to an int arrat  (it does a floor)
newSalaries = salariesMult.astype(int)
print(newSalaries)