####### Tugas Pertemuan 7 Kelompok Pola #######
# Maximum Likelihood Estimation dengan distribusi poisson
# Nur Azizah Eka Budiarti (G651190211)
# Robert John Modalo      (G651190331)
# Rizqi Alifahasni Z      (G651190571)

library(dplyr)
# Maximum Likelihood Estimation for data from Poisson Distribution
# bangkitkan sejumlah data berdasarkan distribusi poisson
# dengan parameter lambda=13
# untuk n = 100, 1000, dan 2000
data0 <- rpois(n=100, lambda=13)
data1 <- rpois(n=1000, lambda=13)
data2 <- rpois(n=2000, lambda=13)

# convert to data frame
#df_poisson0 <- data.frame(data0)
#df_poisson1 <- data.frame(data1)
#df_poisson2 <- data.frame(data2)

# bangkitkan data berdasarkan distribusi poisson
# dengan jarak setiap data 0.2 dalam rentang lambda 1 - 13
lambdas <- seq(1,13, by=0.2)

# fungsi naive likelihood
# Computing Likelihood for Observed Data
llh_poisson <- function(lambda, y){
  # likelihood by summing 
  llh <- sum(dpois(y, lambda))
  return(llh)
}

# compute likelihood for all lambda values
# hitung naive likelihood n=100 untuk semua nilai lambda
llh_0 <- sapply(lambdas, function(x){llh_poisson(x, data0)})

mle0 <- which.max(llh_0)
maxllh_0 <- list(likelihood = llh_0[mle0], parameter = lambdas[mle0])
maxllh_0

# hitung naive likelihood n=1000 untuk semua nilai lambda
llh_1 <- sapply(lambdas, function(x){llh_poisson(x,data1)})

mle1 <- which.max(llh_1)
maxllh_1 <- list(likelihood = llh_1[mle1], parameter = lambdas[mle1])
maxllh_1

# hitung naive likelihood n=2000 untuk semua nilai lambda
llh_2 <- sapply(lambdas, function(x){llh_poisson(x,data2)})

mle2 <- which.max(llh_2)
maxllh_2 <- list(likelihood = llh_2[mle2], parameter = lambdas[mle2])
maxllh_2


# fungsi log-likelihood
# Computing Log-Likelihood for Observed Data
logllh_poisson <- function(lambda, y){
  # log(likelihood) by summing 
  llh <- sum(dpois(y, lambda, log=TRUE))
  return(llh)
}

# hitung log-likelihood n=100 untuk semua nilai lambda
logllh_0 <- sapply(lambdas, function(x){logllh_poisson(x, data0)})

logmle0 <- which.max(logllh_0)
maxlogllh_0 <- list(likelihood = logllh_0[logmle0], parameter = lambdas[logmle0])
maxlogllh_0

# hitung log-likelihood n=1000 untuk semua nilai lambda
logllh_1 <- sapply(lambdas, function(x){logllh_poisson(x, data1)})

logmle1 <- which.max(logllh_1)
maxlogllh_1 <- list(likelihood = logllh_1[logmle1], parameter = lambdas[logmle1])
maxlogllh_1

# hitung log-likelihood n=2000 untuk semua nilai lambda
logllh_2 <- sapply(lambdas, function(x){logllh_poisson(x, data2)})

logmle2 <- which.max(logllh_2)
maxlogllh_2 <- list(likelihood = logllh_2[logmle2], parameter = lambdas[logmle2])
maxlogllh_2


# rata-rata naive likelihood
mean(llh_0)
mean(llh_1)
mean(llh_2)

# rata-rata loglikelihood
mean(logllh_0)
mean(logllh_1)
mean(logllh_2)

# simpan semua nilai lambda dan likelihood dalam dataframe
dfllh_0 <- data.frame(llh100=llh_0, lambda=lambdas)
dfllh_1 <- data.frame(llh1000=llh_1, lambda=lambdas)
dfllh_2 <- data.frame(llh2000=llh_2, lambda=lambdas)

dflogllh_0 <- data.frame(logllh100=logllh_0, lambda=lambdas)
dflogllh_1 <- data.frame(logllh1000=logllh_1, lambda=lambdas)
dflogllh_2 <- data.frame(logllh2000=logllh_2, lambda=lambdas)

# plot nilai likelihood untuk setiap nilai lambda
library(ggplot2)
dfllh_0
ggplot(dfllh_0, aes(lambda, llh100)) + geom_line(aes(colour = llh100))

dfllh_1
ggplot(dfllh_1, aes(lambda, llh1000)) + geom_line(aes(colour = llh1000))

dfllh_2
ggplot(dfllh_2, aes(lambda, llh2000)) + geom_line(aes(colour = llh2000))


dflogllh_0
ggplot(dflogllh_0, aes(lambda, logllh100)) + geom_line(aes(colour = logllh100))

dflogllh_1
ggplot(dflogllh_1, aes(lambda, logllh1000)) + geom_line(aes(colour = logllh1000))

dflogllh_2
ggplot(dflogllh_2, aes(lambda, logllh2000)) + geom_line(aes(colour = logllh2000))





