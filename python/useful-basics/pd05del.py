import pandas as pd

df = pd.DataFrame(columns=('Mouse', 'Keyboard', 'Usb-Hub'))
df.loc['Jumlah'] = [20, 30, 15]
df.loc['harga'] = [60000, 100000, 1500]
df.loc['supplier'] = ['Mitra utama', 'Computer trade', 'Indo trade']
print('data')
print(df)

df = df.drop('supplier', axis=0)
print('\ndata baris supplier dihapus')
print(df)

df = df.drop('Mouse', axis=1)
print('\ndata kolom mouse dihapus')
print(df)
