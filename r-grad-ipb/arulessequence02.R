setwd(choose.dir())
covid <- read.csv('titanic.raw.csv', sep = ";")

#write.csv(titanic.raw, file="titanic.raw.csv", row.names = FALSE)

# Basic sequential pattern mining, taken from https://en.wikibooks.org/wiki/Data_Mining_Algorithms_In_R/Sequence_Mining/SPADE
# taken from Package arulesSequences https://cran.r-project.org/web/packages/arulesSequences/arulesSequences.pdf

covid_data <- data.frame(covid)

library(arules)
library(arulesSequences)
require(utils)
data(covid_data)                         # list all available data sets
try(data(package = "arulesSequences") )  # list the data sets in the arulesSequences package
data("Titanic")
summary(covid)
as(covid, "data.frame")

# execute the CSPADE algorithm
s1 <- cspade(covid_data, parameter = list(support = 0.4), control = list(verbose = TRUE, tidLists = TRUE))
summary(s1)
as(s1, "data.frame")

summary(tidLists(s1))
transactionInfo(tidLists(s1))

## use timing constraint
s2 <- cspade(zaki, parameter = list(support = 0.4, maxgap = 5))
as(s2, "data.frame")

## use classification
t <- zaki
transactionInfo(t)$classID <-as.integer(transactionInfo(t)$sequenceID) %% 2 + 1L
s3 <- cspade(t, parameter = list(support = 0.4, maxgap = 5))
as(s3, "data.frame")
