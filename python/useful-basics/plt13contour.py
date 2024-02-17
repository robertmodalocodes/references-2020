import numpy as np
import matplotlib.pyplot as plt


def zfunction(x, y):
    return (1-(x**2+y**3)) * np.exp(-(x**2+y**2) / 2)


N = 100
x = np.linspace(-3.0, 3.0, N)
y = np.linspace(-3.0, 3.0, N)

X, Y = np.meshgrid(x, y)

Z = zfunction(X, Y)

plt.contourf(X, Y, Z, cmap=plt.cm.PuBu_r)
# plt.grid('on')
plt.title('Contour')

plt.show()
