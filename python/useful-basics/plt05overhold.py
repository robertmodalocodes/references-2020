import numpy as np
from matplotlib import pyplot as plt

plt.close('all')

x = np.linspace(-np.pi, np.pi, 201)
plt.close('all')

plt.plot(x, np.sin(x), label='sin(x)')
plt.hold('on')
plt.plot(x, np.cos(x), label='cos(x)')
plt.plot(x, np.sin(x * 0.5), label='sin(x * 0.5)')
plt.legend(loc=2, borderaxespad=0.1)
plt.hold('off')
plt.xlabel('radian')
plt.title('sudut')
plt.show()
