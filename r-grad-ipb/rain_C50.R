# Classification using c5.0, source: Package C50 documetation 
# Package required: C50, caret 
# Read dataset
setwd(choose.dir())
dataset <- read.csv("rain_ausie2.csv")
rain2 <- dataset
set.seed(9850)

library(C50)
library(caret)

# Apply cross fold validation
folds<-cut(seq(1,nrow(rain2)),breaks=10, labels=FALSE)
for(i in 1:10){
  testIndexes <- which(folds==i, arr.ind=TRUE)
  testData <- rain2[testIndexes, ]
  trainData <-  rain2[-testIndexes,]}

# Create decision tree
oneTree <- C5.0(RainTomorrow ~ Humidity3pm + Sunshine + Rainfall + Cloud3pm, data=trainData)
oneTree
summary(oneTree)
plot(oneTree)
plot(oneTree, type="simple")

library(e1071)
# Calculate accuracy of tree-based model using function  predict 
oneTreePred  <-  predict(oneTree, testData)
postResample(oneTreePred,testData$RainTomorrow)

# Create rule-based model
rules <- C5.0(RainTomorrow ~ Humidity3pm + Sunshine + Rainfall + Cloud3pm, data=trainData, rules=TRUE)
rules
summary(rules)

# Calculate accuracy of rule-based model Using predict 
rulesPred <-  predict(rules,testData)
postResample(predict(rules,testData),testData$RainTomorrow)
plot(rulesPred, xlab = "Rain Tomorrow")




