library(EBImage)
library(pbapply)


########################## Import dan Ekstraksi Citra #################################

#Ekstraksi Citra
extract_feature <- function(dir_path, width, height, label, add_label = TRUE) {
  require(pbapply)
  img_size <- width * height
  ## List images in path
  images_names <- list.files(dir_path)
  #if (add_label) {
  #  label <- label
  #}
  print(paste("Start processing", length(images_names), "images"))
  
  ## merubah ukuran dan warna citra menjadi grayscale
  feature_list <- pblapply(images_names, function(imgname) {
    img <- readImage(file.path(dir_path, imgname))
    ## merubah ukuran citra
    img_resized <- resize(img, w = width, h = height)
    ## merubah warna citra
    grayimg <- channel(img_resized, "gray")
    ## mengambil fitur-fitur satu citra greyscale sebagai matrix
    img_matrix <- grayimg@.Data
    ## merubah matrix menjadi vektor
    img_vector <- as.vector(t(img_matrix))
    return(img_vector)
  })
  
  ## menggabungkan vektor setiap citra menjadi satu matrix
  feature_matrix <- do.call(rbind, feature_list)
  feature_matrix <- as.data.frame(feature_matrix)
  
  ## mengubah nama
  names(feature_matrix) <- paste0("pixel", c(1:img_size))
  #if (add_label) {
    # menambahkan label untuk setiap vektor dalam matrix
  #  feature_matrix <- cbind(label = label, feature_matrix)
  #}
  return(feature_matrix)
}

##### Pilih Folder foto yang akan di resize#####
{
  dir_path <- (choose.dir())
  foto_wajah <- extract_feature(dir_path, 16, 32, 1, TRUE) ## 30 maksudnya meresize width gambar menjadi 30 pixel
  dir_path <- (choose.dir())
  foto_wajah2 <- extract_feature(dir_path, 16, 32, 1, TRUE)
}
#Resize foto dilakukan untuk mengurangi komputasi semakin besar ukuran foto semakin banyak pixel yang akan dihitung

#menggabungkan seluruh matrix objek kedalam satu dataframe
data_wajah <- rbind(foto_wajah, foto_wajah2)

#menyimpan dataset hasil ekstraksi fitur
write.csv(data_buah, "C:/Datasets/wajah.csv", row.names = FALSE)


data_wajah_df <-data.frame(data_wajah)
data_wajah_df[1:nrow(data_wajah_df),1]<-data_wajah_df[1:nrow(data_wajah_df),1]-3
data_wajah_df[1:nrow(data_wajah_df),3]<-data_wajah_df[1:nrow(data_wajah_df),3]+3

rerata = apply(data_wajah,2,mean)
matrixrata <- matrix(rep(rerata, 20), ncol=2, byrow=T)
datacov <- (data_wajah-matrixrata)

matkov <- (t(datacov)%*%as.matrix(datacov))/(nrow(datacov)-1)

eigennya<-eigen(matkov)
eigennya$vectors
eigennya$values

# dalam R eigennya sudah terurut decreasing 
konversi=eigennya$values/sum(eigennya$values) * 100
(persentase_ciri=cumsum(konversi/sum(konversi) * 100))

pc<-80
idx<-as.integer()
for(i in 1:length(persentase_ciri)){
  if(persentase_ciri[i] >= pc){
    idx<-i
    break
  }
}

pc_80=eigennya$vectors[, 1:idx]
dataPCA=as.matrix(data_wajah_df)%*%pc_80 

