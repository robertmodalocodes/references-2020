# invers matrix

import numpy as np

A = np.array([[3, 5], [1, 2]])
invers_A = np.linalg.inv(A)
print("invers matrix a:\n", invers_A)
print("")

'''
to solve a linear equation
suppose we have a linear equation:
2x + 7y = 62
8x + 6y = 116
which is :
A * X = B
[2, 7] * x = 62
[8, 6] * y = 116
in order to find the solution of X, the equation is transformed into:
X = B/A
which means X = B * invers of matrix A
'''

print('-'*100)
print('')
a = np.array([[2.0, 7], [8, 6]])
b = np.array([[62.0], [116]])
xy = np.dot(np.linalg.inv(a), b)
print("x, y:\n", xy)
print("is A * xy equals to B?")
print('B is:')
print(np.dot(a, xy))
