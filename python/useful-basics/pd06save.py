import numpy as np
import pandas as pd

anggota = {'nama': ['Dino', 'Dani', 'Yudi', 'Ibrahim'],
           'asal-kota': ['Pati', 'Kebumen', 'Klaten', 'Solo']}

df = pd.DataFrame(anggota)

df.to_csv('D:/Datasets/Exercise/data.csv', sep=';')  # simpan dalam format csv
# simpan dalam format xlsx
writer = pd.ExcelWriter('D:/Datasets/Exercise/data.xlsx')
df.to_excel(writer, 'kota')
writer.save()
