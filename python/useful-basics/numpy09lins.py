import numpy as np

seq = np.linspace(1, 10, 10)
print('sequence:\n', seq)
print('')

seq2 = np.linspace(1, 10, 6)
print('sequence 2:\n', seq2)
print('')

seq3 = np.linspace(1, 10, num=6)
print('sequence 3:\n', seq3)
print('')

seq4 = np.linspace(1, 10, num=6, endpoint=False)
print('sequence 4:\n', seq4)
print('')
