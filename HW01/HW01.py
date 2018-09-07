#PHYS344 HW01
#Random Number Scatter Plot

import numpy as np
import matplotlib.pyplot as plt

# Fixing random state for reproducibility


N = 10
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
area = (20)  

plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.show()

# Functions
import matplotlib

matplotlib.axes.Axes.scatter
matplotlib.pyplot.scatter

################################################################################




