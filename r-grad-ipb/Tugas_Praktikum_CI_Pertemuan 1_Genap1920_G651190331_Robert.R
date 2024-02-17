# Tugas praktikum Kecerdasan Komputasional pertemuan 1
# Nama  : Robert John Modalo
# NIM   : G651190331
# Bagian B.

# 1. Baris kode untuk Fungsi "cel_to_far" yang dapat mengkonversi nilai Celcius ke Farenhait Input: 24
cel_to_far <- function(celcius) {
  fahrenheit <- (9/5 * celcius) + 32
  return(fahrenheit)
}

cel_to_far(24)


# 2. Baris kode untuk Fungsi "des_to_bin" yang dapat mengkonversi decimal ke nilai biner Input: 231
des_to_bin <- function(desimal) {
  if (desimal > 1) {
    des_to_bin(as.integer(desimal/2))
  }
  cat(desimal %% 2)
}

des_to_bin(231)


# 3. Baris kode untuk Fungsi "nilai_abs" yang dapat mengembalikan nilai absolut dari suatu bilangan desimal
nilai_abs <- function(des) {
  return((des^2)^.5)
}

nilai_abs(-5)


# 4. Baris kode dari rumus abc, untuk menghitung akar- akar persamaan kuadrat f (x) = ax2+ bx + c = 0, 
# untuk berbagai nilai a, b, c.
akar <- function(a, b, c) {
  if(delta(a,b,c) > 0) {
    x_1 = (-b + sqrt(delta(a, b, c))) / (2 * a)
    x_2 = (-b - sqrt(delta(a, b, c))) / (2 * a)
    return(rbind(x_1, x_2))
  }
  else if(delta(a, b, c) == 0) {
    x = -b / (2 * a)
  }
  else {"Akar-akar tidak ditemukan"}
}

delta <- function(a, b, c) {
  b^2 - 4*a*c
}

i <- akar(1, -5, 6)
ii <- akar(1, 0, -4)
i
ii
