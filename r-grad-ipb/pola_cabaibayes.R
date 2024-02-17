library(EBImage)
library(pbapply)
library(caret)
library(Amelia)
library(e1071)

# Ekstrasi to import image 
extract_feature <- function(dir_path, width, height, label, add_label = TRUE) {
  require(pbapply)
  img_size <- width*height
  ## List images in path
  images_names <- list.files(dir_path)
  if (add_label) {
    label <- label
  }
  print(paste("Start processing", length(images_names), "images"))

## This function will resize an image, turn it into greyscale
  feature_list <- pblapply(images_names, function(imgname) {
    ## Read image
    img <- readImage(file.path(dir_path, imgname))
    ## Resize image
    img_resized <- resize(img, w = width, h = height)
    ## Set to grayscale
    grayimg <- channel(img_resized, "gray")
    ## Get the image as a matrix
    img_matrix <- grayimg@.Data
    ## Coerce to a vector
    img_vector <- as.vector(t(img_matrix))
    return(img_vector)
  })
  
## bind the list of vector into matrix
  feature_matrix <- do.call(rbind, feature_list)
  feature_matrix <- as.data.frame(feature_matrix)
  
## Set names
  names(feature_matrix) <- paste0("pixel", c(1:img_size))
  if (add_label) {
    ## Add label
    feature_matrix <- cbind(label = label, feature_matrix)
  }
  return(feature_matrix)
}

img <- readImage(choose.files())
display(img + 0.2)
w <- 60
h <- 45
{
  dir_path <- (choose.dir())
  buah_pir <- extract_feature(dir_path,w,h,1,TRUE)
  dir_path <- (choose.dir() )
  buah_naga <- extract_feature(dir_path,w,h,2,TRUE)
  dir_path <- (choose.dir() )
  buah_jambu <- extract_feature(dir_path,w,h,3,TRUE)
}

#menggabungkan seluruh observasi gambar kedalam satu frame
data_buah <- rbind(buah_pir, buah_naga, buah_jambu)

#menyimpan dataset hasil ekstraksi fitur
write.csv(data_buah, file = "D:/Dataimg/dataset_buah.csv", row.names = FALSE)


#klasifikasi dataset hasil ekstraksi fitur dengan naive bayes
#membuka dataset hasil ektraksi fitur
dataset_buah <- read.csv("D:/Dataimg/dataset_buah.csv")
dataset_buah <- as.data.frame(dataset_buah)
dataset_buah$label <- as.factor(dataset_buah$label)
levels(dataset_buah$label) <- list(buahpir="1", buahnaga="2", buahjambu="3")

#str(dataset_buah)
missmap(dataset_buah)

# membuat data training dan test dengan skema 70 - 30
str(dataset_buah)
set.seed(1234)
clas <- sample(2, nrow(dataset_buah), replace=TRUE, prob=c(0.7, 0.3))
# membuat set training dan test
train_data <- dataset_buah[clas==1,]
test_data <- dataset_buah[clas==2,]

# membuat model naive bayes berdasarkan dataset
model_nb <- naiveBayes(label~., data=dataset_buah)
prediksi <- predict(model_nb, dataset_buah)
table(dataset_buah$label)
table(prediksi, dataset_buah$label)


# Membuat model Naïve Bayes menggunakan datalatih
model.nB <- naiveBayes(label~., data=train_data)

# Prediksi datauji / data baru
predict(model.nB, test_data[2:2701])
predict(model.nB, test_data[2:2701], type="raw")
table(predict=predict(model.nB, test_data[,-1]), true=test_data[,1])

# Prediksi model menggunakan testData 
prediction <- predict(model.nB, newdata = test_data)
table(test_data$label)
table(prediction, test_data$label)

model_nb
summary(model_nb)
model.nB
summary(model.nB)

# Cek akurasi model menggunakan Confusion Matrix
confusionMatrix(prediction, test_data$label)

