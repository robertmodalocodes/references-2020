import numpy as np
from matplotlib import pyplot as plt

plt.close('all')


def equation1(x):
    return x**2 + 4*x + 6


def equation2(x):
    return -(x**2 + 4*x + 6)


x = np.array(range(-90, 100, 10))
y = equation1(x)
y2 = equation2(x)

plt.close('all')

a, = plt.plot(x, y, color='r', label='y = x^2 + 4x + 6')
b, = plt.plot(x, y2, color='b', label=' -(x^2 + 4x + 6)', linestyle='--')
plt.xlabel('x'), plt.ylabel('y')
plt.legend(handles=[a, b])
plt.grid('on')
plt.title('Quadratic Equation')
plt.show()
