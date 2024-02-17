import numpy as np

print('\n')
a = np.array([[2, 7], [8, 6], [9, 5]])

print('a =')
print(np.shape(a))
print("jumlah baris =", np.size(a, 0))
print("jumlah kolom =", np.size(a, 1))
print("")

print("baris ke 0, kolom ke 0 =", a[0, 0])
print("data baris ke 0 untuk semua kolom =", a[0, :])
print("jumlah a =", np.sum(a))
print("max a =", np.max(a))
print("min a =", np.min(a))
print("rata-rata a =", np.mean(a))
