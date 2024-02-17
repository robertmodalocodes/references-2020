"""
==========================
FastICA on 2D point clouds
==========================

This example illustrates visually in the feature space a comparison by
results using two different component analysis techniques.

:ref:`ICA` vs :ref:`PCA`.


"""
from sklearn.decomposition import PCA, FastICA
import matplotlib.pyplot as plt
import numpy as np
print(__doc__)

# Authors: Alexandre Gramfort, Gael Varoquaux
# License: BSD 3 clause

# import library-library yang diperlukan (plot, matematika)
# serta library berisi fungsi PCA dan ICA

# Generate sample dat
# Membangkitkan data sampel secara acak
# dengan jumlah seed 42
rng = np.random.RandomState(42)

# membangkitkan data sampel berdasarkan distribusi t-Student standar
# dengan derajat bebas (1.5), ukuran data 20000 baris 2 kolom
# berdasarkan matrix
S = rng.standard_t(1.5, size=(20000, 2))
# kolom pertama matrix dikalikan 2
S[:, 0] *= 2.

# Gabung data
# Bangkitkan suatu matrix baru (A)
A = np.array([[1, 1], [0, 2]])

# perkalian dot matrix (dot product)
# matrix X yaitu matrix dot product S dengan A transpose
X = np.dot(S, A.T)  # membangkitkan data observasi

A.T

# mengakses kelas PCA dan menyimpannya ke dalam
# suatu variabel (pca)
pca = PCA()
# melatih model dengan data X/data latih (jumlah sampel, jumlah fitur)
# (mendapatkan eigen value dan eigen vector dengan fungsi fit)
S_pca_ = pca.fit(X).transform(X)
# menerapkan reduksi dimensi ke data X
# data X kemudian diproyeksikan pada 'pricipal component'
# yang sebelumnya diekstraksi dari data training
# lalu tetapkan sebagai variabel

# mengakses kelas FastICA yaitu algoritma ICA
# dengan data random yang sudah dibangkitkan
ica = FastICA(random_state=rng)
# melatih model dengan data X/data latih (jumlah sampel, jumlah fitur)
S_ica_ = ica.fit(X).transform(X)  # transformasi data X
# lalu tetapkan sebagai variabel

# Returns the standard deviation of the array elements along given axis.
# Hasilkan simpangan baku dari array hasil training model tersebut
S_ica_ /= S_ica_.std(axis=0)


# #############################################################################
# Plot hasil analisis
# fungsi plot
def plot_samples(S, axis_list=None):
    plt.scatter(S[:, 0], S[:, 1], s=2, marker='o', zorder=10,
                color='steelblue', alpha=0.5)
    if axis_list is not None:
        colors = ['orange', 'red']
        for color, axis in zip(colors, axis_list):
            axis /= axis.std()
            x_axis, y_axis = axis
            # Trick to get legend to work
            plt.plot(0.1 * x_axis, 0.1 * y_axis, linewidth=2, color=color)
            plt.quiver(0, 0, x_axis, y_axis, zorder=11, width=0.01, scale=6,
                       color=color)

    plt.hlines(0, -3, 3)
    plt.vlines(0, -3, 3)
    plt.xlim(-3, 3)
    plt.ylim(-3, 3)
    plt.xlabel('x')
    plt.ylabel('y')


plt.figure()
plt.subplot(2, 2, 1)
plot_samples(S / S.std())
plt.title('True Independent Sources')

axis_list = [pca.components_.T, ica.mixing_]
plt.subplot(2, 2, 2)
plot_samples(X / np.std(X), axis_list=axis_list)
legend = plt.legend(['PCA', 'ICA'], loc='upper right')
legend.set_zorder(100)

plt.title('Observations')

plt.subplot(2, 2, 3)
plot_samples(S_pca_ / np.std(S_pca_, axis=0))
plt.title('PCA recovered signals')

plt.subplot(2, 2, 4)
plot_samples(S_ica_ / np.std(S_ica_))
plt.title('ICA recovered signals')

plt.subplots_adjust(0.09, 0.04, 0.94, 0.94, 0.26, 0.36)
plt.show()

"""
Representing ICA in the feature space gives the view of 'geometric ICA':
ICA is an algorithm that finds directions in the feature space
corresponding to projections with high non-Gaussianity. These directions
need not be orthogonal in the original feature space, but they are
orthogonal in the whitened feature space, in which all directions
correspond to the same variance.

PCA, on the other hand, finds orthogonal directions in the raw feature
space that correspond to directions accounting for maximum variance.

Here we simulate independent sources using a highly non-Gaussian
process, 2 student T with a low number of degrees of freedom (top left
figure). We mix them to create observations (top right figure).
In this raw observation space, directions identified by PCA are
represented by orange vectors. We represent the signal in the PCA space,
after whitening by the variance corresponding to the PCA vectors (lower
left). Running ICA corresponds to finding a rotation in this space to
identify the directions of largest non-Gaussianity (lower right).
"""
