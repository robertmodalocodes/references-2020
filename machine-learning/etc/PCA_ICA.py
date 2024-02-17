"""
Tugas 9 Pengenalan Pola
Independent Component Analysis

Nama    :   Robert John Modalo
NIM     :   G651190331
"""


from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from matplotlib.colors import ListedColormap
import sklearn
from sklearn.decomposition import PCA, FastICA
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
print(__doc__)

wine = datasets.load_wine()
print(wine.feature_names)
print(wine.target_names)
print('')

df_wine = pd.DataFrame(wine.data)
print(df_wine.head(4))
print('')

# df_wine.columns = ['label', 'alcohol', 'malic_acid', 'ash', 'alcalinity_of_ash', 'magnesium', 'total_phenols', 'flavanoids',
#                  'nonflavanoid_phenols', 'proanthocyanins', 'color_intensity', 'hue', 'od280/od315_of_diluted_wines', 'proline']

X, y = df_wine.iloc[:, 1:].values, df_wine.iloc[:, 0].values

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(
    X, y, test_size=0.3)

sc = StandardScaler()
x_train_std = sc.fit_transform(x_train)
x_test_std = sc.fit_transform(x_test)

matrix_kov = np.cov(x_train_std.T)
print(matrix_kov[0::5])
print('')

# mencari nilai eigen dan vektor eigen
eigen_val, eigen_vec = np.linalg.eig(matrix_kov)
print('nilai eigen, vektor eigen')
print(eigen_val, eigen_vec[::5])
print('')


tot = sum(eigen_val)
var_exp = [(i / tot) for i in sorted(eigen_val, reverse=True)]
cum_var_exp = np.cumsum(var_exp)
'''
plt.bar(range(1, 14), var_exp, alpha=0.5,
        align='center', label='varian individu')
plt.step(range(1, 14), cum_var_exp, where='mid', label='varian kumulatif')
plt.ylabel('rasio varian')
plt.xlabel('Principal components')
plt.legend(loc='best')
plt.show()
'''
# transformasi data ke ruang vektor baru
pasangan_eigen = \
    [(np.abs(eigen_val[i]), eigen_vec[:, i])
     for i in range(len(eigen_val))]
pasangan_eigen.sort(reverse=True)

print('Pasangan eigen')
print(pasangan_eigen[:5])

# ambil dua vektor eigen yang paling tinggi
w = np.hstack((pasangan_eigen[0][1][:, np.newaxis],
               pasangan_eigen[1][1][:, np.newaxis]))
print(w.shape)
print('vektor eigen tertinggi')
print(w)
print('')

print(x_train_std[0])
print('')
print(x_train_std[0].dot(w))

# transformasi dataset dengan perkalian dot
x_train_pca = x_train_std.dot(w)
# ukuran data setelah transofrmasi
print(x_train_std.shape, w.shape, x_train_pca.shape)
print('')

# visualisasi hasil transformasi data
colors = ['r', 'b', 'g']
markers = ['s', 'x', 'o']

for l, c, m in zip(np.unique(y_train), colors, markers):
    plt.scatter(x_train_pca[y_train == l, 0], x_train_pca[y_train == l, 1],
                c=c, label=l, marker=m)
plt.xlabel('Principal components 1')
plt.ylabel('Principal components 2')
plt.legend(loc='lower left')
plt.show()


# dengan library scikit-learn
# ICA
imp = SimpleImputer(missing_values=np.NaN, strategy='mean')

XX = datasets.load_wine().data
imp.fit(XX)

icax = FastICA(n_components=2)
X_trans = icax.fit_transform(XX)
print('Komponen hasil ICA')
print(icax.components_)
plt.scatter(X_trans[:, 0], X_trans[:, 1])
