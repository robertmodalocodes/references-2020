import numpy as np
from matplotlib import pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

plt.close('all')


def zfunction(x, y):
    return (1-(x**2 + y**3)) * np.exp(-(x**2 + y**2) / 2)


N = 100
x = np.linspace(-3.0, 3.0, N)
y = np.linspace(-3.0, 3.0, N)

X, Y = np.meshgrid(x, y)

Z = zfunction(X, Y)

fig = plt.figure()
ax = fig.gca(projection='3d')

ax.plot_surface(X, Y, Z, rstride=8, cstride=8, alpha=0.3)
cset = ax.contourf(X, Y, Z, zdir='x', offset=X.min(), cmap=cm.coolwarm)
cset = ax.contourf(X, Y, Z, zdir='y', offset=Y.min(), cmap=cm.coolwarm)
cset = ax.contourf(X, Y, Z, zdir='z', offset=Z.min(), cmap=cm.coolwarm)

ax.set_xlabel('X')
ax.set_xlim(X.min(), X.max())
ax.set_ylabel('Y')
ax.set_ylim(Y.min(), Y.max())
ax.set_zlabel('Z')
ax.set_zlim(Z.min(), Z.max())
plt.title('contour - surface')
plt.grid('on')
plt.show()
