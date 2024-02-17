p.parameter <- 0.7
# sequence <- rpois(1000, 20000)


# Maximum Likelihood Estimation for data from Poisson Distribution
# generate data from Poisson distribution
# with the parameter lambda=13
# untuk n = 100
data <- rpois(n=100, lambda=13)

# convert to data frame
df_Poisson <- data.frame(data=data)

df_Poisson %>% 
  ggplot(aes(x=sekuens))+ 
  geom_histogram(bins=100) +
  ylab("Count")+ xlab("data")+
  theme_bw(base_size = 16) +
  ggtitle("Poisson Distribution: rpois(100, 13)")



# Likelihood
# Computing Likelihood for Poisson Distribution
dpois(data[1], lambda=1)

likelihood <- dpois(data[1], lambda=seq(20))

# likelihood single data point
likelihood <- dpois(data[1], lambda=seq(20))

# likelihood single data point as data frame
lh_single <- data.frame(x=seq(20), likelihood=likelihood )

lh_single %>% 
  ggplot(aes(x=x,y=likelihood))+
  geom_point(size=4,color="dodgerblue")+
  xlab("Lambda") + ylab("Likelihood") +
  ggtitle("Likelihood of a single data point over multiple lambda") +
  theme_bw(base_size = 16) 

# compute log-likelihood of single data point
log_likelihood <- dpois(data[1], lambda=seq(20), log=TRUE)
# log likelihood in data frame
llh_single <- data.frame(x=seq(20), log_like=log_likelihood)

llh_single %>% 
  ggplot(aes(x=x,y=likelihood))+
  geom_point(size=4,color="dodgerblue")+
  xlab("Lambda") + ylab("Log Likelihood") +
  ggtitle("Log-Likelihood of a single data point ") +
  theme_bw(base_size = 16) 




# Computing Likelihood for Observed Data
llh_poisson <- function(lambda, y){
  # log(likelihood) by summing 
  llh <- sum(dpois(y, lambda, log=TRUE))
  return(llh)
}

lambdas <- seq(1,15, by=0.5)

# compute log-likelihood for all lambda values
ll <- sapply(lambdas,function(x){llh_poisson(x,data)})

# save the lambdas and log-likelihoods in a data frame
df <- data.frame(ll=ll, lambda=lambdas)





# Maximum Likelihood Estimate from Observed Data
df %>% 
  ggplot(aes(x=lambda,y=ll))+
  geom_point(size=4,color="dodgerblue")+
  xlab("Lambda") +
  ylab("Log Likelihood")+
  theme_bw(base_size = 16) +
  geom_vline(xintercept = lambdas[which.max(ll)], color="red",size=2)



