# messing with histograms

import numpy as np
import matplotlib.pyplot as plt

# seeding the data will ensure that the numbers that come out in the
# random generator will be the same each time
# they can differ
# handy when you are debugging
np.random.seed(1)   
normData = np.random.normal(size=1000000)  # need big number to look truely randomised

plt.hist(normData)
plt.show()