import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from matplotlib.ticker import LinearLocator
from mpl_toolkits.mplot3d import Axes3D

plt.close('all')

fig = plt.figure()
ax = fig.gca(projection='3d')

N = 100
X = np.linspace(-10, 10, N)
Y = np.linspace(-10, 10, N)
X, Y = np.meshgrid(X, Y)

r = np.sqrt(X**2 + Y**2)
Z = np.sin(r) / r

surf = ax.plot_surface(X, Y, Z, linewidth=0, antialiased=True, cmap=cm.bone_r)
ax.zaxis.set_major_locator(LinearLocator(10))
fig.colorbar(surf, aspect=5)
plt.grid('on')
plt.title('Surface - Color Bar')
plt.show()
