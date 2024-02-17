keuangan = {
'pengeluaran': [2, 2.5, 2.25, 2.5, 3.2, 2.5, 3.5, 4, 3],
'pemasukan': [7.8, 7.5, 9, 7.6, 7.2, 7.5, 7, 10, 7.5]
}

# Perhitungan rata-rata pemasukan dan rata-rata pengeluaran
total_pengeluaran = 0
total_pemasukan = 0
for biaya in keuangan['pengeluaran']: 
    total_pengeluaran += biaya
for masuk in keuangan['pemasukan']: 
    total_pemasukan += masuk

print(total_pengeluaran)
print(total_pemasukan)

print(type(keuangan['pengeluaran']))
print(type(keuangan['pemasukan']))

rata_rata_pengeluaran = total_pengeluaran / len(keuangan['pengeluaran'])
rata_rata_pemasukan = total_pemasukan / len(keuangan['pemasukan'])
print(rata_rata_pengeluaran) 
print(rata_rata_pemasukan)

print(len(keuangan['pengeluaran']))
print(len(keuangan['pemasukan']))


print(keuangan.keys)
print(keuangan.values)