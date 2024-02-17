import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

data = pd.read_excel('D:/Datasets/Exercise/uji_pearson.xlsx', 'Sheet1')

plt.close('all')
plt.scatter(data['matematika'], data['tpa'])
plt.xlabel('matematika')
plt.ylabel('tpa')

x = data['matematika']
y = data['tpa']

#x = np.reshape(x, (np.size(x, 0), 1))
#y = np.reshape(y, (np.size(y, 0), 1))

x = np.ravel(x)
y = np.ravel(y)

# pearson correlation
r = stats.pearsonr(x, y)[0]

plt.title('Nilai Pearson ' + str(r))
plt.show()
