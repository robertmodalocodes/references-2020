import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

df = pd.read_excel('D:/Datasets/Exercise/uji_clustering.xlsx')
data_masuk = np.array(df[['x', 'y']])
kmeans = KMeans(n_clusters=3, random_state=0)
kmeans.fit(data_masuk)
center = kmeans.cluster_centers_
print('centroid')
print(center)
print('')

# plot
plt.figure('plotting data')
plt.scatter(data_masuk[:, 0], data_masuk[:, 1], s=40, c='b', marker='o')
# plt.hold('on')
plt.scatter(center[:, 0], center[:, 1], s=600, c='r', marker='+')
# plt.hold('off')

# labelling
labels = kmeans.labels_
labels = labels.reshape(np.size(labels), 1)
data_masuk = np.hstack((data_masuk, labels))  # susun horizontal
print('hasil')
print(data_masuk)
print('')

df2 = pd.DataFrame(data_masuk, columns=('x', 'y', 'label'))
keterangan = ['satu', 'dua', 'tiga']

for i in range(0, 3):
    df2.loc[df2['label'] == i, 'label'] = keterangan[i]

print('diubah keterangan')
print(df2)

plt.show()

writer = pd.ExcelWriter('D:/Datasets/Exercise/uji_clustered.xlsx')

# save file
df2.to_excel(writer, 'Sheet1')

writer.save()
