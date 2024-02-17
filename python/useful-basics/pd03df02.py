import numpy as np
import pandas as pd

df = pd.DataFrame(columns=('mouse', 'keyboard'))

print(df)

print('')

print('TAMBAH BARIS')
df.loc['jumlah'] = [20, 30]
df.loc['harga'] = [60000, 100000]
df.loc['supplier'] = ['mitra utama', 'computer trade']
print(df)

print('TAMBAH KOLOM')
df['usb-hub'] = [15, 15000, 'indo trade']
print(df)
