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
y = np.array([10, 5, 15, 7], float)
x_1 = np.arange(len(x))

rows = 1
columns = 3

ax1 = plt.subplot2grid((rows, columns), (0, 0))
ax1.bar(np.arange(0, len(x), 1), y, align='center')
ax1.set_xticks(np.arange(0, len(x), 1))
ax1.set_xticklabels(x)
ax1.set_ylabel('amount', fontdict=font_label)
ax1.set_xlabel('division', fontdict=font_label)
ax1.set_title('sales data', fontdict=font_title)

# adding text for each bar
for i in range(0, len(x)):
    ax1.text(x_1[i], y[i] + 0.1, y[i], ha='center', fontdict=font_label)

index = np.argsort(y)
x_order = x[index]
y_order = np.sort(y)
ax2 = plt.subplot2grid((rows, columns), (0, 1))
ax2.bar(np.arange(0, len(x_order), 1), y_order, align='center', color='green')
ax2.set_xticks(np.arange(0, len(x_order), 1))
ax2.set_xticklabels(x_order)
ax2.set_ylabel('amount', fontdict=font_label)
ax2.set_xlabel('division', fontdict=font_label)
ax2.set_title('sales ranking', fontdict=font_title)

# adding text for each bar
for i in range(0, len(x)):
    ax2.text(x_1[i], y_order[i] + 0.1, y_order[i],
             ha='center', fontdict=font_label)

ax3 = plt.subplot2grid((rows, columns), (0, 2))
# autopercentage is for precerntage labels for each slice
ax3.pie(y_order, labels=x_order, shadow=True, autopct='%1.1f%%', startangle=90)
ax3.set_title('sales percentage', fontdict=font_title)

plt.show()

ax1.get_figure().savefig('D:/Plots/barplot_latihan01.png')
print('plots have been saved')
