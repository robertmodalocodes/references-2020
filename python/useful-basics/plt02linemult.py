import numpy as np
from matplotlib import pyplot as plt

plt.close('all')


def equation1(x):
    return x**2 + 4*x + 6


def equation2(x):
    return -(x**2 + 4*x + 6)


x = np.array(range(-90, 100, 10))
y = equation1(x)  # call the function equation1
y2 = equation2(x)  # call the function equation2
plt.figure()  # figure1
plt.plot(x, y, color='red'), plt.xlabel('x'), plt.ylabel('y')
plt.title('quadratic equation 1: \ny = x^2 + 4x + 6')

plt.figure()  # figure2
plt.plot(x, y2, color='black', linestyle='-.'), plt.xlabel('x'), plt.ylabel('y')
plt.title('quadratic equation 2: \ny = x^2 + 4x + 6')
plt.show()
