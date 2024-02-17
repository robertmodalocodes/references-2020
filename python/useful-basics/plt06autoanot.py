import numpy as np
from matplotlib import pyplot as plt
plt.close('all')


def equation1(x):
    return x**2 + 4*x + 6


x = np.array(range(-80, 80, 10))
y = equation1(x)

plt.close('all')
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.grid('on')
plt.plot(x[2], y[2], marker='o', markersize=10, color='r')
plt.text(x[2]+10, y[2]+10, 'point 1', fontsize=15)
plt.plot(x[12], y[12], marker='*', markersize=20, color='b')
plt.text(x[12]+10, y[12]+10, 'point 2', fontsize=15)
plt.title('graph for x^2 + 4x + 6')
plt.show()
