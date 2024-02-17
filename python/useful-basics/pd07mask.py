import numpy as np
import pandas as pd

sports = pd.read_excel('D:/Datasets/Exercise/sports.xlsx', 'Sheet1')
print('tabel sports\n', sports)
print('jumlah kolom', sports.columns.size)

print('')
print('nama-nama kolom')

for j in range(0, sports.columns.size):
    print(sports.columns[j])

print('')

print('jumlah menang\n', np.array(sports['menang']).sum())
print('jumlah kalah\n', np.array(sports['kalah']).sum())
