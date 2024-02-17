# calculating vectors
# examples
# c(1, 2, 3) + c(4, 5, 6)
# c(1 + 4, 2 + 5, 3 + 6)
# c(5, 7, 9)

# a <- c(1, 2, 3) 
# b <- c(4, 5, 6)
# c <- a + b

# adding two vectors
A_vector <- c(1, 2, 3)
B_vector <- c(4, 5, 6)

# Take the sum of A_vector and B_vector
total_vector <- A_vector + B_vector

# Print out total_vector
total_vector

# Poker and roulette winnings from Monday to Friday:
poker_vector <- c(140, -50, 20, -120, 240)
roulette_vector <- c(-24, -50, 100, -350, 10)
days_vector <- c("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
names(poker_vector) <- days_vector
names(roulette_vector) <- days_vector

# calculate
# Assign to total_daily how much you won/lost on each day
total_daily <- roulette_vector + poker_vector

# Total winnings with poker
total_poker <- sum(poker_vector)

# Total winnings with roulette
total_roulette <- sum(roulette_vector)

# Total winnings overall
total_week <- sum(total_poker + total_roulette)

# Print out total_week
total_week

# comparing the sum of two vectors
# Check if you realized higher total gains in poker than in roulette 
total_poker > total_roulette
