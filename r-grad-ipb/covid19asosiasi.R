# Tugas 5 Praktikum Topik Dalam Data Mining Terapan (KOM631)
# Nama  : Robert John Modalo
# NIM   : G651190331

# asic association rule mining, taken from R and Data Mining

library(arules)
library(arulesSequences)
require(utils)

setwd(choose.dir())
covir <- read.csv("covid19_3.csv", sep = ";")
rules.all <- apriori(covir)
print(rules.all)
rules.all_sorted <- sort(rules, by=)
inspect(rules.all)

rules <- apriori(covir, control = list(verbose=F), parameter = list(minlen=2, supp=0.010, conf=0.8), appearance = list(rhs=c("Isolation_Source=oronasopharynx", "Isolation_Source=lung", "Isolation_Source=feces"), default="lhs"))
quality(rules) <- round(quality(rules), digits = 3)
rules_sorted <- sort(rules, by="lift")
inspect(rules_sorted)

# Visualizing association rules
library(arulesViz)
plot(rules.all)
plot(rules.all, method="grouped")
plot(rules.all, method="graph")
plot(rules.all, method="graph", control=list(type="Items"))
plot(rules.all, method="paracoord", control=list(reorder=TRUE))

