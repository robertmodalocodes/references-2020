import pandas as pd

anggota = {'nama': ['Dino', 'Dani', 'Yudi', 'Ibrahim'],
           'asal-kota': ['Pati', 'Kebumen', 'Klaten', 'Solo']}

df = pd.DataFrame(anggota)

print(df)
print('')
print('    Asal kota')

print(df['asal-kota'])
