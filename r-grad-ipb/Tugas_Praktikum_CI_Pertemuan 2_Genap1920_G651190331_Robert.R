# Tugas Praktikum Kecerdasan Komputasional Pertemuan 2
# Nama  : Robert John Modalo
# NIM   : G651190331


# variabel predictor (untuk x1, x2, x3)
X <- matrix(c(
  0, 0, 1,
  0, 1, 1,
  1, 0, 1,
  1, 1, 1), ncol = 3, byrow = T)

# Tentukan variabel Respon Y
Y <- c(0, 1, 1, 0)

# Combine variabel predictor dan respon menjadi 1 tabular cbind(X, Y)
cbind(X, Y)

# Bangkitkan sebuah nilai random 0-1 untuk tiap elemen X
# dijadikan sebagai bobot inisialisasi untuk layer 1
rand_vector <- runif(ncol(X) * nrow(X))

# Konversi vector di atas ke dalam matrix
rand_matrix <- matrix(
  rand_vector, 
  nrow = ncol(X),
  ncol = nrow(X),
  byrow = TRUE
)

# Buat list yang menyimpan parameter NN yang akan di training
my_nn <- list(
  # Variabel Input
  input = X,
  # Bobot untuk layer 1
  weights1 = rand_matrix,
  # Bias untuk layer 1
  bias1 = 1.0,
  # Bobot untuk layer 2
  weights2 = matrix(runif(4), ncol = 1),
  # Bias untuk layer 2
  bias2 = 1.0,
  # Nilai Aktual
  y = Y,
  # Variabel untuk menyimpan nilai prediksi
  output = matrix(
    rep(0, times = 4),
    ncol = 1
  )
)

# Fungsi Aktivasi Sigmoid
sigmoid <- function(x) {
  1.0 / (1.0 + exp(-x))
}

# Penjabaran Formulasi Feedforward
feedforward <- function(nn) {
  nn$layer1 <- sigmoid((nn$input %*% nn$weights1) + nn$bias1)
  nn$output <- sigmoid((nn$layer1 %*% nn$weights2) + nn$bias2)
  nn
}

my_nn <- feedforward(my_nn)
data.frame(
  "Predicted" = round(my_nn$output, 3),
  "Actual" = Y
)



# kesimpulan
#   Predicted Actual
# 1     0.958      0
# 2     0.965      1
# 3     0.962      1
# 4     0.967      0

# Dapat dilihat bahwa hasil prediksi 1 dan 4 berbeda jauh dengan nilai aktualnya.
# Sementara hasil prediksi 2 dan 3 mendekati nilai aktualnya.
# Fungsi feedforward menjalankan fungsi aktivasi yaitu fungsi sigmoid yang meneruskan informasi dari satu layer ke layer berikutnya
# Namun, model di atas merupakan contoh model neural network dasar. Fungsi yang dijalankan hanya fungsi feedforward.
# sehingga input langsung diteruskan hingga menjadi output. neural network tidak dilatih.
# bias sebesar satu untuk setiap layer (perceptron) menyebabkan fungsi sigmoid memberikan output yang kurang lebih mirip
# padahal seharusnya hasil prediksi harus mendekati nilai aktual.












