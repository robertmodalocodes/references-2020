import numpy as np
from matplotlib import pyplot as plt

N = 10
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
plt.figure()
area = np.pi * (15 * np.random.rand(N)) ** 2  # circle area
plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.title('Scatter')

plt.show()
