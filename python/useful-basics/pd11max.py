import numpy as np
import pandas as pd

path = 'D:/Datasets/Exercise/saham.xlsx'
saham = pd.read_excel(path, 'Sheet1')
kode_saham = saham['kode'].drop_duplicates()
kode_saham = kode_saham.reset_index()

# fx mencari harga tertinggi untuk masing-masing kode


def sahamtertinggi(daftar_saham, kode_saham):
    saham_seleksi = saham[saham['kode'] == kode_saham]
    saham_tertinggi = saham_seleksi[saham_seleksi['harga']
                                    == saham_seleksi['harga'].max()]
    return saham_tertinggi


for i in range(0, len(kode_saham)):
    print(sahamtertinggi(saham, kode_saham['kode'][i]))
