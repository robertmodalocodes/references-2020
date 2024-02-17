# variabel predictor (untuk x1, x2, x3)
X <- matrix(c(
  0, 0, 1,
  0, 1, 1,
  1, 0, 1,
  1, 1, 1,
  0, 0, 0), ncol = 3, byrow = T)

# Tentukan variabel Respon Y
Y <- c(0, 1, 1, 0, 0)

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
  weights2 = matrix(runif(5), ncol = 1),
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

# Turunan fungsi aktifasi sigmoid (derivative of sigmoid)
sigmoid_derivative <- function(x) { 
  x * (1.0 - x)
}

# Loss Function
loss_function <- function(nn) {
  sum((nn$Y - nn$output) ^ 2)
} 

loss_function(my_nn)

# Penjabaran Formulasi Feedforward
feedforward <- function(nn) {
  nn$layer1 <- sigmoid((nn$input %*% nn$weights1) + nn$bias1)
  nn$output <- sigmoid((nn$layer1 %*% nn$weights2) + nn$bias2)
  nn
}

my_nn <- feedforward(my_nn)
data.frame(
  "Predicted" = round(my_nn$output, 5),
  "Actual" = Y
)

### Backpropagasi Balik berdasarkan aturan rantai (derivasi)
backprop <- function(nn) { 
  
  # d_weights2 adalah aturan rantai (derivasi) bobot 2
  d_weights2 <- (
    t(nn$layer1) %*%
      ((nn$y - nn$output) * sigmoid_derivative(nn$output))) 
  
  
  # d_weights1 adalah aturan rantai (derivasi) bobot 1 dan bobot 2
  d_weights1 <- (
    t(nn$input) %*%
      (((nn$y - nn$output) * sigmoid_derivative(nn$output))%*%
         t(nn$weights2)* sigmoid_derivative(nn$layer1))) 
  
  # update bobot menggunakan derivatif(slope) loss function
  nn$weights1 <- nn$weights1 + d_weights1
  nn$weights2 <- nn$weights2 + d_weights2
  nn 
}

# Train Model dengan iterasi n = 1500
n <- 1500

# Buat data frame untuk menyimpan hasil loss function tiap iterasi
loss_df <- data.frame(
  iteration = 1:n,
  loss = vector("numeric", length = n))

# Lakukan pelatihan sebanya n iterasi kemudian simpan nilai loss
for (i in 1:n) {
  my_nn <- feedforward(my_nn)
  my_nn <- backprop(my_nn)
  # Simpan hasil loss function, untuk lihat plot perubahan erorr
  loss_df$loss[i] <- loss_function(my_nn)
}

# lihat hasil prediksi dengan backprop
data.frame(
  "Predicted" = round(my_nn$output, 3),
  "Actual" = Y
)

# Sebelum propagasi balik
# Predicted Actual
# 1   0.92361      0
# 2   0.93086      1
# 3   0.93452      1
# 4   0.93835      0
# 5   0.91296      0

# Predicted Actual
# 1     0.019      0
# 2     0.954      1
# 3     0.955      1
# 4     0.055      0
# 5     0.002      0

# Dapat dilihat bahwa sebelum propagasi balik nilai 
# prediksi mendekati nilai aktual pada input 2 dan 3,
# mendekati nilai aktualnya, tetapi nilai inpu 1, 4, 5 
# menjauhi nilai aktualnya.
# Tetapi setelah di propagasi balik, 
# semua nilai prediksi makin mendekati nilai aktual.
# Hal ini dikarenakan semua nilai output telah diketahui errornya, 
# dan dari nilai error tersebut, proses propagasi balik-
# akan mengupdate seluruh nilai bobot.
# Setelah itu feed forward akan dijalankan lagi 
# dengan nilai-nilai bobot yang sudah diupdate pada iterasi berikutnya
# sampai ke iterasi yang ditentukan (n),
# hingga nilai loss function menjadi minimum.
# Yang pada akhirnya mengakibatkan nilai prediksi
# mendekati nilai aktual.












