import pandas as pd
import numpy as np

df = pd.DataFrame(columns=('mouse', 'ketboard'))

print(df)

print('\nTAMBAH BARIS')
df.loc['jumlah'] = [20, 30]
df.loc['harga'] = [60000, 100000]
df.loc['supplier'] = ['mitra utama', 'computer trade']
print(df)

print('\nTAMBAH KOLOM')
df['usb-hub'] = [15, 15000, 'indo trade']
print(df)

print('\nDAFTAR INDEX')
for i in range(0, df.index.size):
    print(str(i) + ' = ' + df.index[i])

print('\nDAFTAR KOLOM')
for j in range(0, df.columns.size):
    print(str(j) + ' = ' + df.columns[j])
