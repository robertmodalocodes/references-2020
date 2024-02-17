# Basic matrix arithmetic

# Data
box_office <- c(460.998, 314.4, 290.475, 247.900, 309.306, 165.8)
star_wars_matrix <- matrix(box_office, nrow = 3, byrow = TRUE,
                           dimnames = list(c("A New Hope", "The Empire Strikes Back", "Return of the Jedi"), 
                                           c("US", "non-US")))

phantom_menace <- c(474.5,  552.5)
the_clones <- c(310.7, 338.7)
the_sith <- c(380.3, 468.5)

region2 <- c("US", "non-US")
titles2 <- c("The Phantom Menace", "Attack of the Clones", "Revenge of the Sith")

box_office2 <- c(phantom_menace, the_clones, the_sith)
star_wars_matrix2 <- matrix(box_office2, byrow = TRUE, nrow = 3)

colnames(star_wars_matrix2) <- region2
rownames(star_wars_matrix2) <- titles2

all_wars_matrix <- rbind(star_wars_matrix, star_wars_matrix2)

# all_wars_matrix is available in your workspace
all_wars_matrix

# Estimate the visitors
visitors <- all_wars_matrix / 5

# Print the estimate to the console
visitors

# ticket_prices_matrix
# US non-US
# A New Hope              5.0    5.0
# The Empire Strikes Back 6.0    6.0
# Return of the Jedi      7.0    7.0
# The Phantom Menace      4.0    4.0
# Attack of the Clones    4.5    4.5
# Revenge of the Sith     4.9    4.9

# all_wars_matrix and ticket_prices_matrix are available in your workspace
all_wars_matrix
ticket_prices_matrix

# Estimated number of visitors
visitors <- all_wars_matrix / ticket_prices_matrix

# US visitors
us_visitors <- visitors[,1]

# Average number of US visitors
mean(us_visitors)