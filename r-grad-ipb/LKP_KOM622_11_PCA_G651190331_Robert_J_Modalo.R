# Tugas pengenalan pola pertemuan 11
# LKP_KOM622_Pertemuan 11 PCA
# Nama    :   Robert John Modalo
# NIM     :   G651190331

library(EBImage)
library(pbapply)

# FUngsi ekstraksi Citra
extract_feature <- function(dir_path, width, height, label, add_label = TRUE) {
  require(pbapply)
  img_size <- width * height
  ## List images in path
  images_names <- list.files(dir_path)
  if (add_label) {
    label <- label
  }
  print(paste("Start processing", length(images_names), "images"))
  
  # merubah ukuran dan warna citra menjadi grayscale
  feature_list <- pblapply(images_names, function(imgname) {
    img <- readImage(file.path(dir_path, imgname))
    # merubah ukuran citra
    img_resized <- resize(img, w = width, h = height)
    # merubah warna citra
    grayimg <- channel(img_resized, "gray")
    # mengambil fitur-fitur satu citra greyscale sebagai matrix
    img_matrix <- grayimg@.Data
    # merubah matrix menjadi vektor
    img_vector <- as.vector(t(img_matrix))
    return(img_vector)
  })
  
  # menggabungkan vektor setiap citra menjadi matrix
  feature_matrix <- do.call(rbind, feature_list)
  feature_matrix <- as.data.frame(feature_matrix)
  
  names(feature_matrix) <- paste0("pixel", c(1:img_size))
  if (add_label) {
  # menambahkan label untuk setiap vektor dalam matrix
    feature_matrix <- cbind(label = label, feature_matrix)
  }
  return(feature_matrix)
}

# Pilih folder citra yang akan digunakan
{
  dir_path <- (choose.dir())
  foto_wajah <- extract_feature(dir_path, 16, 32, 1, TRUE) ## 30 maksudnya meresize width gambar menjadi 30 pixel
  dir_path <- (choose.dir())
  foto_wajah2 <- extract_feature(dir_path, 16, 32, 2, TRUE)
}

# Resize foto dilakukan untuk mengurangi komputasi semakin besar ukuran foto semakin banyak pixel yang akan dihitung

# menggabungkan seluruh matrix objek kedalam satu dataframe
data_wajah <- rbind(foto_wajah, foto_wajah2)

# menyimpan dataset hasil ekstraksi fitur
write.csv(data_wajah, "D:/Datasets/wajah.csv", row.names = FALSE)

# buka file hasil ekstraksi
wajah <- read.csv("D:/Datasets/wajah.csv")

wajah <- as.data.frame(wajah)
wajah$label <- as.factor(wajah$label)
# menambahkan label untuk masing-masing citra
levels(wajah$label) <- list(foto_wajah="1", foto_wajah2="2")

# membagi dataset menjadi data latih dan data uji
library(caTools)
set.seed(123)
split = sample.split(wajah$label, SplitRatio = 0.8)
training_set = subset(wajah, split == TRUE)
test_set = subset(wajah, split == FALSE)


# implementasi PCA
# install.packages('caret')
library(caret)

library(e1071)
# hapus kolom label
pca = preProcess(x = training_set[-1], method = 'pca', pcaComp = 2)
# menggunakan predict untuk menerapkan objek pca di data latih
training_set = predict(pca, training_set)
# atur kolom sesuai urutan
training_set = training_set[c(2, 3, 1)]
test_set = predict(pca, test_set)
test_set = test_set[c(2, 3, 1)]

# Principal component (PC) 1 dan 2 adalah variabel baru

head(training_set)

# ujicoba svm dengan data latih
#library(e1071)
classifier = svm(formula = label ~ .,
                 data = training_set,
                 type = 'C-classification',
                 kernel = 'linear')

# prediksi hasil uji
y_pred = predict(classifier, newdata = test_set[-3])
y_pred

# membuat confusion matrix
cm = table(test_set[, 3], y_pred)
cm

# prediksi hasil latih
y_predTR = predict(classifier, newdata = training_set[-3])
y_predTR

# confusion matrix untuk data latih
cmTR = table(training_set[, 3], y_predTR)
cmTR


# visualisasi hasil data latih
library(ElemStatLearn)
set = training_set
X1 = seq(min(set[, 1]) - 1, max(set[, 1]) + 1, by = 0.01)
X2 = seq(min(set[, 2]) - 1, max(set[, 2]) + 1, by = 0.01)
grid_set = expand.grid(X1, X2)
colnames(grid_set) = c('PC1', 'PC2')
y_grid = predict(classifier, newdata = grid_set)
plot(set[, -3],
     main = 'Principal Component Analysis (PCA) (Training set)',
     xlab = 'PC1', ylab = 'PC2',
     xlim = range(X1), ylim = range(X2))
contour(X1, X2, matrix(as.numeric(y_grid), length(X1), length(X2)), add = TRUE)
points(grid_set, pch = '.', col = ifelse(y_grid == 2, 'deepskyblue', ifelse(y_grid == 1, 'springgreen3', 'tomato')))
points(set, pch = 21, bg = ifelse(set[, 3] == 2, 'blue3', ifelse(set[, 3] == 1, 'green4', 'red3')))

# visualisasi hasil data uji
set = test_set
X1 = seq(min(set[, 1]) - 1, max(set[, 1]) + 1, by = 0.01)
X2 = seq(min(set[, 2]) - 1, max(set[, 2]) + 1, by = 0.01)
grid_set = expand.grid(X1, X2)
colnames(grid_set) = c('PC1', 'PC2')
y_grid = predict(classifier, newdata = grid_set)
plot(set[, -3], main = 'Principal Component Analysis (PCA) (Test set)',
     xlab = 'PC1', ylab = 'PC2',
     xlim = range(X1), ylim = range(X2))
contour(X1, X2, matrix(as.numeric(y_grid), length(X1), length(X2)), add = TRUE)
points(grid_set, pch = '.', col = ifelse(y_grid == 2, 'deepskyblue', ifelse(y_grid == 1, 'springgreen3', 'tomato')))
points(set, pch = 21, bg = ifelse(set[, 3] == 2, 'blue3', ifelse(set[, 3] == 1, 'green4', 'red3')))
