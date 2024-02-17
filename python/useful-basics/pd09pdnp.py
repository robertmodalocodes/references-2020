import numpy as np
import pandas as pd

sports = pd.read_excel('D:/Datasets/Exercise/sports.xlsx', 'Sheet1')
tim = sports[sports['tim'] == 'Satria Muda']
data = np.array(tim[['menang', 'kalah']])

print('jumlah menang dan kalah', data.sum(axis=0))
