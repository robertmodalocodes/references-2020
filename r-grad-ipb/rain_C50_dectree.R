# Tugas 3 Praktikum Topik Dalam Data Mining Terapan (KOM631)
# Nama  : Robert John Modalo
# NIM   : G651190331

# Teknik dasar data mining - Klasifikasi berbasis pohon dan aturan

# set directory
setwd(choose.dir())
dataset <- read.csv('rain_ausie2.csv')
rain <- dataset

rain$RainToday[rain$RainToday == " "] <- "Yes"

# 1. Pembagian dengan skema 80 - 20
str(rain)
set.seed(1234)
clas <- sample(2, nrow(rain), replace=TRUE, prob=c(0.8, 0.2))
# membuat set training dan test
trainData <- rain[clas==1,]
testData <- rain[clas==2,]

library(party)
library(C50)
# membuat model berbasis tree untuk skema 80 - 20
myFormula <- RainTomorrow ~ Humidity3pm + Sunshine + Rainfall + Cloud3pm
# Decision tree dengan C5.0
rain_ctree <- C5.0(myFormula, data=trainData)
# check the prediction
# table(predict(rain_ctree), trainData$RainTomorrow)
summary(rain_ctree)

print(rain_ctree)
plot(rain_ctree)
plot(rain_ctree, type="simple")
# prediksi test data
testPred <- predict(rain_ctree, newdata = testData)
# cek prediksi
table(testPred, testData$RainTomorrow)
# akurasi
library(e1071)
library(caret)
postResample(testPred, testData$RainTomorrow)

# membuat model berbasis rule untuk skema 80 - 20
rain_rule <- C5.0(myFormula, data=trainData, rules = TRUE)
rain_rule
testPred_rule <- predict(rain_rule, testData)
# akurasi model berbasis rule untuk skema 80/20
summary(rain_rule)
table(testPred_rule, testData$RainTomorrow)
postResample(testPred_rule, testData$RainTomorrow)




dataset <- read.csv("rain_ausie2.csv")
rain2 <- dataset
set.seed(9850)

library(C50)
library(caret)

# 2. Pembagian dengan skema 10 cross fold validation
folds<-cut(seq(1,nrow(rain2)),breaks=10, labels=FALSE)
for(i in 1:10){
  testIndexes <- which(folds==i, arr.ind=TRUE)
  testData <- rain2[testIndexes, ]
  trainData <-  rain2[-testIndexes,]}

# membuat model berbasis tree
oneTree <- C5.0(RainTomorrow ~ Humidity3pm + Sunshine + Rainfall + Cloud3pm, data=trainData)
oneTree
summary(oneTree)
plot(oneTree)
plot(oneTree, type="simple")

library(e1071)
# menghitung akurasi model berbasis tree menggunakan fungsi predict
oneTreePred  <-  predict(oneTree, testData)
table(oneTreePred, testData$RainTomorrow)
postResample(oneTreePred,testData$RainTomorrow)

# membuat model berbasis rule (aturan)
rules <- C5.0(RainTomorrow ~ Humidity3pm + Sunshine + Rainfall + Cloud3pm, data=trainData, rules=TRUE)
rules
summary(rules)

# menghitung akurasi model berbasis rule menggunakan fungsi predict
rulesPred <-  predict(rules,testData)
table(rulesPred, testData$RainTomorrow)
postResample(rulesPred,testData$RainTomorrow)
plot(rulesPred, xlab = "Rain Tomorrow")




