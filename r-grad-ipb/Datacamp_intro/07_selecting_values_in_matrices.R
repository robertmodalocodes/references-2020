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

# Select the non-US revenue for all movies
non_us_all <- all_wars_matrix[,2] # selects all the second column

# Average non-US revenue
mean(non_us_all)

# Select the non-US revenue for first two movies
non_us_some <- all_wars_matrix[1:2,2] # selects first two rows of the second column

# Average non-US revenue for first two movies
mean(non_us_some)
