import numpy as np

# axis
print('*'*100)
a = np.array([[1, 3, 4], [5, 6, 7]])
# array operation by column, use axis=0
print('===COLUMN===')
print('sum  = \n', np.sum(a, axis=0))
print('mean = \n', np.mean(a, axis=0))
print('min  = \n', np.min(a, axis=0))
print('max  = \n', np.min(a, axis=0))
print('')

# array operation by row, use axis=1
print('===ROW===')
print('sum  = \n', np.sum(a, axis=1))
print('mean = \n', np.mean(a, axis=1))
print('min  = \n', np.min(a, axis=1))
print('max  = \n', np.min(a, axis=1))
print('')

# where operation
# to search location of an integer in an array
print('-'*100)
a = np.array([[1, 3, 4], [5, 4, 7]])
[row_location, column_location] = np.where(a == 4)
for i in range(0, len(row_location)):
    print('i = ' + str(row_location[i]) + ', j = ' + str(column_location[i]))

# replacing a value(s) in an array
print('')
b = np.array([[1, 3, 4], [5, 4, 7]])
print('before replacing 4 \n', b)
print('')
c = np.where(a == 4, 0, b)  # useful for cleaning data
print('after replacing 4 \n', c)
print('')
d = np.where(a == 4, 0, 1)
print('after replacing 4 \n', d)
print('')
e = np.where(a == 4, 2, 2)
print('after replacing 4 \n', e)
print('')
