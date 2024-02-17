import sklearn
from sklearn.impute import SimpleImputer
from sklearn import datasets
from sklearn.decomposition import FastICA
import matplotlib.pyplot as plt
import numpy as np

imp = SimpleImputer(missing_values=np.nan, strategy='mean')

XX = datasets.load_wine().data
imp.fit(XX)

icax = FastICA(n_components=2)
X_trans = icax.fit_transform(XX)
print(icax.components_)
plt.scatter(X_trans[:, 0], X_trans[:, 1])
