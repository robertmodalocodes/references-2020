import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm


colors = cm.rainbow(np.linspace(0, 1, 3))

N = 10
x = np.random.rand(N)
y = np.random.rand(N)
z = x**2 + y*10

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z, color=colors[0])

N = 100
x = np.random.rand(N)
y = np.random.rand(N)
z = x**2 + y*2
ax.scatter(x, y, z, color=colors[1])

N = 100
x = np.random.rand(N)
y = np.random.rand(N)
z = x**2 + y
ax.scatter(x, y, z, color=colors[2])

plt.show()
