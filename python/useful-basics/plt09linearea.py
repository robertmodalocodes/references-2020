import numpy as np
from matplotlib import pyplot as plt

colors = ('r', 'g', 'b', 'c', 'm', 'y', 'k')

plt.close('all')

x = np.linspace(-np.pi, np.pi, 201)
plt.fill(x, np.sin(x), label='sin(x)', color=colors[5])
plt.fill(x, np.sin(x*0.8), label='sin(x*0.8)', color=colors[4])
plt.legend(loc=2, borderaxespad=0.1)
plt.grid()
plt.title('line area')
plt.show()
