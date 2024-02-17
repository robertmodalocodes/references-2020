library(readr)

openaq <- read.csv("D:/Docs/Kuliah/Tugas/Semester 2/Data Mining/openaq.csv")
View(openaq)

# head
head(openaq)

openaq$attribution <- NULL
openaq$location <- NULL

write.table(openaq, file="D:/Docs/Kuliah/Tugas/Semester 2/Data Mining/openaqExp.csv", sep = ",", row.names = FALSE)

write.table(openaq, file="D:/Docs/Kuliah/Tugas/Semester 2/Data Mining/openaqExp.txt", sep = "\t", row.names = FALSE)

summary(openaq)

summary(openaq$city)

city <- table(openaq$city)
parameter <- table(openaq$parameter == "pm10")

View(city)
View(parameter)


summary(city)

barplot(openaq$city)

hist(openaq$value [openaq$parameter == "pm25"], 
     #xlim = c(0, 25),
     #breaks = 9,
     main = "pm25 concentration in India",
     xlab = "pm25 (µg/m³)",
     col = "red")

hist(openaq$value [openaq$parameter == "pm10"],
     #xlim = c(0, 25),
     #breaks = 9,
     main = "pm10 concentration in India",
     xlab = "pm10 (µg/m³)",
     col = "red")

hist(openaq$value [openaq$city == "Chennai"], 
     #xlim = c(0, 25),
     #breaks = 9,
     main = "pm concentration in Chennai",
     xlab = "pm2.5 & pm10 (µg/m³)",
     col = "red")

hist(openaq$value [openaq$parameter == "pm25"] [openaq$city == "Chennai"],
     #xlim = c(0, 25),
     breaks = 9,
     main = "pm2.5 concentration in Chennai",
     xlab = "pm2.5 (µg/m³)",
     col = "purple")

hist(openaq$value [openaq$parameter == "pm10"] [openaq$city == "Chennai"],
     #xlim = c(0, 25),
     breaks = 9,
     main = "pm10 concentration in Chennai",
     xlab = "pm10 (µg/m³)",
     col = "yellow")

summary(openaq$value [openaq$parameter == "pm25"])

summary(openaq$value [openaq$parameter == "pm10"])

summary(openaq$value [openaq$parameter == "pm25"] [openaq$city == "Chennai"])

summary(openaq$value [openaq$parameter == "pm10"] [openaq$city == "Chennai"])

hist(openaq$value [openaq$city == "Mumbai"])

hist(openaq$value [openaq$city == "Solapur"])

hist(openaq$value [openaq$city == "Delhi"])

hist(openaq$value [openaq$city == "Kolkata"])

hist(openaq$value [openaq$city == "Hyderabad"])


plot(openaq$value [openaq$city == "Chennai"],
     #xlim = c(0, 3),
     #breaks = 9,
     main = "Air quality in Chennai",
     xlab = "Air Quality (µg/m³)",
     col = "red")

