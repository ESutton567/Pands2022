# this program plots the function y = xE
# Author: Éilis Sutton

# pyplot is a state-based interface to matplotlib
# It provides a MATLAB-like way of plotting

import numpy as np
import matplotlib.pyplot as plt

xpoints = np.array(range(1,101))
ypoints = xpoints * xpoints  # x squared

plt.plot(xpoints, ypoints)
plt.show()