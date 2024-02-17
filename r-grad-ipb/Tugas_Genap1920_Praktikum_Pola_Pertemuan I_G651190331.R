# PRAKTIKUM TOPIK DALAM PENGENALAN POLA
# PERTEMUAN 1 
# ANALISIS DATA DAN PENGENALAN POLA  

# Nama		:	Robert John Modalo
# NIM		  :	G651190331


# 1
setwd(choose.dir())
dataset <- read.csv("data sales-prak 1.csv")
#View(dataset)

# 2
dim(dataset)
str(dataset) 

# 3
table((is.na(dataset))) 

# 4
colSums(is.na(dataset))

# 5
dataset_clean <- dataset[complete.cases(dataset),]

# 6
summary(dataset_clean)
dataset_clean[dataset_clean == 0] <- NA # mengganti nilai 0 dengan NA

#View(dataset_clean)

# 7
library(ggplot2)
ggplot(dataset, aes(x= Item_Visibility, y = Item_Outlet_Sales)) +  
  geom_point(size = 2.5, color="navy") +  
  xlab("Item Visibility") +  
  ylab("Item Outlet Sales") +  
  ggtitle("Item Visibility vs Item Outlet Sales") 

# 8
ggplot(dataset, aes(Item_Type, Item_MRP)) + 
  geom_boxplot() + 
  ggtitle("Box Plot") +  
  theme(axis.text.x = element_text(angle = 70, vjust = 0.5, color = "r ed")) +  
  xlab("Item Type") +  
  ylab("Item MRP") +  
  ggtitle("Item Type vs Item MRP") 



