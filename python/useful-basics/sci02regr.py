import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

data = pd.read_excel('D:/Datasets/Exercise/uji_pearson.xlsx')

plt.close('all')
plt.scatter(data['matematika'], data['tpa'])
plt.xlabel('matematika')
plt.ylabel('tpa')

regr = linear_model.LinearRegression()
x = data['matematika']  # variabel bebas
y = data['tpa']  # variabel terikat

#x = np.reshape(x, (np.size(x, 0), 1))
#y = np.reshape(y, (np.size(y, 0), 1))

#x = np.ravel(x)
#y = np.ravel(y)

regr.fit(x[:, np.newaxis], y)

# prediksi
xfit = np.linspace(55, 85, 1000)
prediksi_cacat = regr.predict(xfit[:, np.newaxis])
yfit = prediksi_cacat

plt.scatter(x, y)
plt.plot(xfit, yfit)

# plt.hold('on')
# plt.plot(x, prediksi_cacat, color='red', linewidth=3)
# plt.hold('off')
plt.title('regresi linear')
plt.show()

print('nilai b:', regr.coef_[0])
print('\n')
print('nilai a:', regr.intercept_)
