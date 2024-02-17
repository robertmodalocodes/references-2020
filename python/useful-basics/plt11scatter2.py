import numpy as np
import matplotlib.pyplot as plt

N = 10
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)

x2 = x * 1.5
y2 = y * 1.5
x3 = x * 1.5
y3 = y * 1.5

plt.figure()
area = np.pi * (15 * np.random.rand(N)) ** 2
# plt.hold('on')
plt.scatter(x2, y2, s=area, c=colors, alpha=0.5)
plt.scatter(x3, y3, s=area, marker='x', c='black')
plt.title('Scatter - Multi Marker')

plt.show()
