import numpy as np

#random = np.random.rand(3, 2)
#print("random values matrix\n", random)

# ----------------------------------------------
print('')

# empty array (zero matrix)
empty_matrix = np.zeros([4, 4])
print('an empty matrix\n', empty_matrix)
# to change a value in a zero matrix
# access by index
print('')

empty_matrix[0, 0] = 10
empty_matrix[1, 1] = 10
empty_matrix[2, 2] = 10
empty_matrix[3, 3] = 10
print('matrix 10 diagonal:\n', empty_matrix)
print('-'*100)
# or

a = 0
b = 0

for i in empty_matrix:
    empty_matrix[a, b] += 20
    a += 1
    b += 1


print('')
print(empty_matrix)
