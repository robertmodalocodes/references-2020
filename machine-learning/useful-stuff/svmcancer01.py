# -*- coding: utf-8 -*-
"""
Created on Tue May 26 08:02:58 2020

@author: HP Envy
"""

import sklearn
from sklearn import datasets
from sklearn import svm
from sklearn import metrics
import pickle
from sklearn.neighbors import KNeighborsClassifier

bcancer = datasets.load_breast_cancer()
print(bcancer.feature_names)
print(bcancer.target_names)
print('')

# define the data
x = bcancer.data
y = bcancer.target

# split the data into train data and test data
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(
    x, y, test_size=0.2)
print(x_train, y_train)
print('')

classes = ['malignant', 'benign']

# define the algorithm/model
clf = svm.SVC(kernel='linear', C=1.0)
#clf2 = KNeighborsClassifier(n_neighbors=8)
# train the model
clf.fit(x_train, y_train)

'''
with open('bcancersvm.pickle', 'wb') as f:
    pickle.dump(clf, f)

pickle_in = open('bcancersvm.pickle', 'rb')
clf = pickle.load(pickle_in)
'''

# predict some data (test data) using the model
y_pred = clf.predict(x_test)

acc = metrics.accuracy_score(y_test, y_pred)
print('accuracy:', acc)
