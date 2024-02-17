import numpy as np
import pandas as pd

saham = pd.read_excel('D:/Datasets/Exercise/saham.xlsx', 'Sheet1')

# hapus record duplikat
kode_saham = saham['kode'].drop_duplicates()

# reset index
kode_saham = kode_saham.reset_index(drop=True)

print('Kode saham\n {}'.format(kode_saham))
print('')

# kode_saham = kode_saham.drop(columns=['index'])
# print('Kode saham\n {}'.format(kode_saham))
