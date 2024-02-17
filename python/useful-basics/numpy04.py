# kasus penjumlahan
import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[4, 5], [6, 7]])
c = a + b

print('a = \n', a)
print('b = \n', b)
print('c = \n', c)
print('')

# kasus pengurangan
d = a - b
print('d = \n', d)
print('')

# kasus pembagian
e = a / b
print('e = \n', e)
print('')

# operasi perkalian
# skalar
f = a * b
print('f = \n', f)
print('')

# dot
g = np.dot(a, b)
print('dot = ', g)
