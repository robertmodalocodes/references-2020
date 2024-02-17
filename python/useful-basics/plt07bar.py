import numpy as np
from matplotlib import pyplot as plt

plt.close('all')

font_label = {
    'family': 'arial',
    'color': 'blue',
    'weight': 'normal',
    'size': 16,
}

font_title = {
    'family': 'arial',
    'color': 'black',
    'weight': 'bold',
    'size': 20,
}

x = np.array(['IT', 'FCGM', 'automotive', 'beverage'])
x_l = np.arange(len(x))
y = np.array([10, 5, 15, 7], float)

fig, ax = plt.subplots()
ax.bar(np.arange(0, len(x), 1), y, align='center', color='red')
ax.set_xticks(np.arange(0, len(x), 1))
ax.set_xticklabels(x)
ax.set_ylabel('amount', fontdict=font_label)
ax.set_xlabel('division', fontdict=font_label)
ax.set_title('sales data', fontdict=font_title)

# adding text
for i in range(0, len(x)):
    ax.text(x_l[i], y[i] + 0.1, y[i], ha='center', fontdict=font_label)

plt.show()
