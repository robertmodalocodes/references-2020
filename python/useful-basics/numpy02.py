# array multidimensi

import numpy as np

multi_array = np.array([
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[10, 11, 12], [13, 14, 15], [16, 17, 18]]
])

print(multi_array)
[baris, kolom, dimensi] = multi_array.shape
print('')
print('baris', baris)
print('kolom', kolom)
print('dimensi', dimensi)
print('nilai array', multi_array[0, 0, 0])
print('')
print('nilai array', multi_array[0, 1, 0])
print('')
print('nilai array', multi_array[1, 1, 0])
print('')
print('nilai array', multi_array[1, 2, 2])
