# showing a plot for a quadratic equation
import numpy as np
import matplotlib.pyplot as plt

plt.close('all')


def equation(x):
    y = x**2 + 4*x + 6
    return y


x = np.array(range(-80, 80, 10))
y = equation(x)

plt.close('all')

# showing the plot
plt.plot(x, y)
plt.xlabel('nilai x')
plt.ylabel('nilai y')
plt.grid('on')  # show the grid
plt.title('graph for X^2 + 4x + 6')
plt.show()
