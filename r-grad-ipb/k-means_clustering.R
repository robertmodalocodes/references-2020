# Tugas 4 Praktikum Topik Dalam Data Mining Terapan (KOM631)
# Nama  : Robert John Modalo
# NIM   : G651190331

# K-means clustering

setwd(choose.dir())
raindata <- read.csv("rainausie_norm.csv")

View(raindata)

# raindata2 <- raindata[,c(-1,-2,-8,-10,-11,-12,-14,-16,-18,-20,-22)] # menghapus beberapa variabel/atribut/kolom

# View(raindata2)

raincluster <- raindata


#K-means clustering dengan 3 cluster
raincluster$RainTomorrow <- NULL
(kmeans.result <- kmeans(raincluster, 3))

#hasil clustering di bandingkan dengan label asli
table(raindata$RainTomorrow, kmeans.result$cluster)

#Plot cluster
plot(raincluster[c("Temp3pm", "Humidity3pm")], col = kmeans.result$cluster)
#plot cluster centers
points(kmeans.result$centers[,c("Temp3pm", "Humidity3pm")], col = 1:3, pch = 8, cex=2)


#write.table(raindata2, file="D:/Docs/Datasets/rainausie.csv", sep = ",", row.names = FALSE, na = " ")
