# calculating matrices

# Construct star_wars_matrix
box_office <- c(460.998, 314.4, 290.475, 247.900, 309.306, 165.8)
star_wars_matrix <- matrix(box_office, nrow = 3, byrow = TRUE,
                           dimnames = list(c("A New Hope", "The Empire Strikes Back", "Return of the Jedi"), 
                                           c("US", "non-US")))

# Calculate worldwide box office figures
worldwide_vector <- rowSums(star_wars_matrix)
worldwide_vector

# Bind the new variable worldwide_vector as a column to star_wars_matrix
all_wars_matrix <- cbind(star_wars_matrix, worldwide_vector)
# add the new worldwide_vector as a column to the all_wars_matrix
# cbind means column bind whereas rbind means row bind

phantom_menace <- c(474.5,  552.5)
the_clones <- c(310.7, 338.7)
the_sith <- c(380.3, 468.5)

region2 <- c("US", "non-US")
titles2 <- c("The Phantom Menace", "Attack of the Clones", "Revenge of the Sith")

box_office2 <- c(phantom_menace, the_clones, the_sith)

star_wars_matrix2 <- matrix(box_office2, byrow = TRUE, nrow = 3)
colnames(star_wars_matrix2) <- region2
rownames(star_wars_matrix2) <- titles2

# Bind by rows
all_wars_matrix2 <- rbind(star_wars_matrix, star_wars_matrix2)

# Print
all_wars_matrix2

# Calculate by columns
# Total revenue for US and non-US
total_revenue_vector <- colSums(all_wars_matrix2)

# Print out total_revenue_vector
total_revenue_vector

