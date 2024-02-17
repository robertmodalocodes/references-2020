
# set directory
setwd(choose.dir())
dataset <- read.csv('rain_ausie2.csv')
rain <- dataset

rain$RainToday[rain$RainToday == " "] <- "Yes"

# Decision Trees with Package rpart
str(rain)
set.seed(1234)
clas <- sample(2, nrow(rain), replace=TRUE, prob=c(0.7, 0.3))
# create training set and testing set
trainData <- rain[clas==1,]
testData <- rain[clas==2,]

library(party)
# creating the model
myFormula <- RainTomorrow ~ Humidity3pm + Sunshine + Rainfall + Cloud3pm
rain_ctree <- ctree(myFormula, data=trainData)
# check the prediction
table(predict(rain_ctree), trainData$RainTomorrow)

print(rain_ctree)
plot(rain_ctree)
plot(rain_ctree, type="simple")
# predict on test data
testPred <- predict(rain_ctree, newdata = testData)
table(testPred, testData$RainTomorrow)

