import numpy as np
import pandas as pd

saham = pd.read_excel('D:/Datasets/Exercise/saham.xlsx', 'Sheet1', index_col=0)
print(saham)

print('')
saham.loc[saham['kode'] == 'TLKM', 'kode'] = 'PT. TELKOM INDONESIA'
print(saham)
