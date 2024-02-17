import numpy as np
import pandas as pd
from sklearn import neighbors

df = pd.read_excel('D:/Datasets/Exercise/uji_clustered.xlsx')

x = np.array(df[['x', 'y']])
y = np.array([df['label']])
y = np.array(y.ravel())

knn = neighbors.KNeighborsClassifier()
knn.fit(x, y)
x2 = np.array([[3, 14]])  # data testing

hasil = knn.predict(x2)
print(x2)
print('termasuk kelas = ' + str(hasil))
