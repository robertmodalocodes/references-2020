import cv2
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
from sklearn import preprocessing

img = cv2.imread('D:/Dataimg/Pola-Buah/Jambu/Crop/IMG_20200224_142041.jpg', 0)

ret, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
ret, thresh4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
ret, thresh5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

titles = ['Original Image', 'BINARY',
          'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()

df1 = pd.DataFrame(data=thresh1).T
df2 = pd.DataFrame(data=thresh2).T
df3 = pd.DataFrame(data=thresh3).T
df4 = pd.DataFrame(data=thresh4).T
df5 = pd.DataFrame(data=thresh5).T

prep_df1 = preprocessing.normalize(df1)

df1_flat = np.ravel(df1)
df2_flat = np.ravel(df2)
df3_flat = np.ravel(df3)
df4_flat = np.ravel(df4)
df5_flat = np.ravel(df5)


print(df1)
print('')
print(prep_df1)

df1prep = pd.DataFrame(data=prep_df1)

# df1prep.to_csv('normalized.csv')

df1_flat_data = pd.DataFrame(df1_flat)
df1_flat_data.to_csv('df1_flat_data.csv')
df2_flat_data = pd.DataFrame(df2_flat)
