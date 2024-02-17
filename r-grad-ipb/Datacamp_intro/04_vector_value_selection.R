# vector value selection

# Poker and roulette winnings from Monday to Friday:
poker_vector <- c(140, -50, 20, -120, 240)
roulette_vector <- c(-24, -50, 100, -350, 10)
days_vector <- c("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
names(poker_vector) <- days_vector
names(roulette_vector) <- days_vector


# Define a new variable based on a selection
poker_wednesday <- poker_vector[3] # in R, the index of the first value in a vector starts from 1
# so the value of wednesday is the poker_vector[3] which is 20


# Define a new variable based on a selection
poker_midweek <- poker_vector[c(2, 3, 4)] # selects values of tuesday, wednesday, and thursday in a vector

# or select value by this rule
roulette_selection_vector <- roulette_vector[2:5] # it means select values from index two to five

# or select by labels
# Select poker results for Monday, Tuesday and Wednesday
poker_start <- poker_vector[c("Monday", "Tuesday", "Wednesday")]

# Calculate the average of the elements in poker_start
mean(poker_start) # function for calculating average


# selection by comparison
# Which days did you make money on poker?
selection_vector <- poker_vector > 0 # check which values in poker_vector that have value over 0

# Print out selection_vector
selection_vector

# Select from poker_vector these days
poker_winning_days <- poker_vector[selection_vector] # selects whichever value is true then assign it into a variable

# Which days did you make money on roulette?
selection_vector_2 <- roulette_vector > 0

# Select from roulette_vector these days
roulette_winning_days <- roulette_vector[selection_vector_2]







