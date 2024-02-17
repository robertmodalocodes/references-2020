import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=float)
# saving the output/variable into a textfile/csv
np.savetxt('result.csv', a, delimiter=',')
print('a ', a)

# loading a file from a directory
b = np.genfromtxt('result.csv', delimiter=',')
print('b', b)
