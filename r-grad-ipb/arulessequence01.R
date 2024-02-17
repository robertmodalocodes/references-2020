library(dplyr)
library(tidyverse)
library(arulesSequences)

#Import standard transaction data
setwd(choose.dir())
covid <- read.csv("covid19_2.csv", sep = ";")

# Start time of data to be considered
start_month <- "2019-12"

# Create list of Azure services by customer ID and CleanMonth (formatted dates)
trans_sequence <- covid %>%
  group_by(Collection_Date, Protein) %>%
  summarize(
    SIZE = n(),
    ServiceLevel = paste(as.character(Geo_Location), collapse = ';')
  )

# Make event and sequence IDs into factors
elapsed_months <- function(end_date, start_date) {
  ed <- as.POSIXlt(end_date)
  sd <- as.POSIXlt(start_date)
  12 * (ed$year - sd$year) + (ed$mon - sd$mon)
}

trans_sequence$eventID <- elapsed_months(trans_sequence$Collection_Date, start_month)
trans_sequence = trans_sequence[,c(1,5,3,4)]
names(trans_sequence) = c("sequenceID", "eventID", "SIZE", "Sequence")
trans_sequence <- data.frame(lapply(trans_sequence, as.factor))
trans_sequence <- trans_sequence[order(trans_sequence$sequenceID, trans_sequence$eventID),]

# Convert to transaction matrix data type
write.table(trans_sequence, "mytxtout.txt", sep=";", row.names = FALSE, col.names = FALSE, quote = FALSE)
trans_matrix <- read_baskets("mytxtout.txt", sep = ";", info = c("sequenceID","eventID","SIZE"))0
