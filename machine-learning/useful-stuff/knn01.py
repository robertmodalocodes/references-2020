import sklearn
from sklearn.utils import shuffle
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
from sklearn import linear_model, preprocessing
import pickle

data = pd.read_csv('D:/Datasets/Exercise/car.data')
print(data.head(8))

# preprocessing data that contains many non-numerical attributes
# convert all the non-numerical data in each attribute to numeric/integer
le = preprocessing.LabelEncoder()
buying = le.fit_transform(list(data['buying']))
maint = le.fit_transform(list(data['maint']))
door = le.fit_transform(list(data['door']))
persons = le.fit_transform(list(data['persons']))
lug_boot = le.fit_transform(list(data['lug_boot']))
safety = le.fit_transform(list(data['safety']))
clss = le.fit_transform(list(data['class']))

label = 'class'

X = list(zip(buying, maint, door, persons, lug_boot, safety))
Y = list(clss)

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(
    X, Y, test_size=0.2)

# print('')
#print('X:\n', X)
#print('Y:\n', Y)
# print('')
#print(x_train, y_test)

# build the model
model = KNeighborsClassifier(n_neighbors=9)
# fit/train the model
model.fit(x_train, y_train)
# calculate the accuracy of the model
acc = model.score(x_test, y_test)
print('Accuracy:', acc)

'''
# save the model
with open('carknnmodel.pickle', 'wb') as f:
    pickle.dump(model, f)

pickle_in = open('carknnmodel.pickle', 'rb')
model = pickle.load(pickle_in)
'''

predicted = model.predict(x_test)
names = ['unacc', 'acc', 'good', 'vgood']

for x in range(len(predicted)):
    print("Predicted: ", names[predicted[x]], 'Data: ',
          x_test[x], 'Actual: ', names[y_test[x]])

print('')
acc = model.score(x_test, y_test)
print('Accuracy:', acc)
