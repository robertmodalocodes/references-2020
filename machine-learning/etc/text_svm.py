import numpy as np
from sklearn.svm import SVC
import matplotlib.pyplot as plt
import seaborn as sns

x1 = np.array([-1, 2, 1])
x2 = np.array([1, -2, 1])

dotx = np.dot(x1, x2)
print('x1 dot x2', dotx)

dot1 = np.dot(x1, x1)
dot2 = np.dot(x2, x2)

print('x1 dot x1', dot1)
print('x2 dot x2', dot2)

dotxa = np.dot(x2, x1.transpose())
print('x2 dot x1', dotxa)
