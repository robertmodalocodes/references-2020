import numpy as np
from matplotlib import pyplot as plt

plt.close('all')


def equation1(x):
    return x**2 + 4*x + 6


def equation2(x):
    return -(x**2 + 4*x + 6)


sub_row = 1
sub_column = 2

x = np.array(range(-90, 100, 10))
y = equation1(x)
y2 = equation2(x)

plt.close('all')
plt.subplot(sub_row, sub_column, 1)  # column 1
a, = plt.plot(x, y, color='red', label='y = x^2 + 4x + 6')
plt.legend(handles=[a])  # notice this code
plt.xlabel('x')
plt.ylabel('y')
plt.grid('on')
plt.title('quadratic equation 1')

plt.subplot(sub_row, sub_column, 2)  # column 2
b, = plt.plot(x, y2, color='black',
              label='y = -(x^2 + 4x + 6)', linestyle='--')
plt.legend(handles=[b])
plt.xlabel('x')
plt.ylabel('y')
plt.grid('on')
plt.title('quadratic equation 2')
plt.show()  # always write this code at the end of the line to show the plot
