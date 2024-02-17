# Clustering using DBSCAN algorithm 
# Reading dataset
library(fpc)
tabel <- read.table("D:/Courses/MKOM_Topik dalam Data Mining Terapan/Genap1617/Bahan Praktikum//hotspotsekuens.csv", header=TRUE, sep=",")
# GoogleMapsPlot(tabel,lat = "latitude", long = "longitude")

#Clustering using DBSCAN
x <- as.matrix(tabel) 
ds <- dbscan(x, eps=0.1, MinPts=3) 
plot(ds, x)
# ds
ds$cluster
plotcluster(x, ds$cluster)
