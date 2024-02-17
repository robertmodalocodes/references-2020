import numpy as np
import pandas as pd

sports = pd.read_excel('D:/Datasets/Exercise/sports.xlsx', 'Sheet1')
nama_tim = 'Satria Muda'
tim = sports[sports['tim'] == nama_tim]

print('nama tim = ' + nama_tim)
print('info \n', tim)
print('jumlah menang', np.array(tim['menang']).sum())
print('jumlah kalah', np.array(tim['kalah']).sum())
