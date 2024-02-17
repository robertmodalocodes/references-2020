'''
    Linear regression
    original code by tech with Tim
'''

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle
import pickle

df = pd.read_csv('D:/Datasets/Exercise/student-mat.csv', sep=';')
print(df.head(4))

# select the preferred attributes
df = df[['G1', 'G2', 'G3', 'studytime', 'failures', 'absences']]
print(df.head(4))
# define the label
label = 'G3'

# define X and Y
# X is the dataset without the label (the prediction target)
X = np.array(df.drop([label], 1))
Y = np.array(df[label])

# split the dataset into training data and testing data
# split some chunks of the data into training x and some for training y
# and test data x and test data y
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(
    X, Y, test_size=0.4)
# 0.2 is the chunk size of the data in percentage to the original data
# to be assigned to the test data

# build the model
linear = linear_model.LinearRegression()

# fit the model with the training data / train the data
# to find the best fit line with the training data

linear.fit(x_train, y_train)
# check the accuracy of the model
acc = linear.score(x_test, y_test)
print('Accuracy:', acc)
print('')

print('Coefficient:\n', linear.coef_)
print('Intercept:\n', linear.intercept_)
print('')

# predict with test data / test the model with the test data
predictions = linear.predict(x_test)

# print the prediction results
for x in range(len(predictions)):
    print(predictions[x], x_test[x], y_test[x])
