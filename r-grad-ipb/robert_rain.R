airausie1 <- read.csv("D:/Docs/Data Mining/weatherAUS.csv")
summary(airausie1)

airausie2 <- airausie1

summary(airausie2)

# Fungsi untuk mencari modus
getmode <- function(v, na.rm = TRUE) {
  uniqv <- unique(v)
  uniqv[which.max(tabulate(match(v, uniqv)))]
}

# karena atribut MinTemp berdistribusi normal,
# missing values pada atribut MinTemp diisikan dengan rata-rata record dari atribut tersebut
airausie2$MinTemp[which(is.na(airausie2$MinTemp))] <- mean(airausie2$MinTemp, na.rm = TRUE)

# atribut MaxTemp juga berdistribusi normal,
# missing values pada atribut MaxTemp digantikan dengan rata-rata record dari atribur tersebut
airausie2$MaxTemp[which(is.na(airausie2$MaxTemp))] <- mean(airausie2$MaxTemp, na.rm = TRUE)

# Rainfall
rain_vector <- c(airausie2$Rainfall)
rain_vector_nona <- c(na.omit(rain_vector))
rain_mode <- getmode(rain_vector_nona)
airausie2$Rainfall[which(is.na(airausie2$Rainfall))] <- rain_mode

# Evaporation
evap_vector <- c(airausie2$Evaporation)
evap_vector_nona <- c(na.omit(evap_vector))
evap_mode <- getmode(evap_vector_nona)
airausie2$Evaporation[which(is.na(airausie2$Evaporation))] <- evap_mode

# Sunshine
airausie2$Sunshine[which(is.na(airausie2$Sunshine))] <- mean(airausie2$Sunshine, na.rm = TRUE)

# WindGustSpeed
airausie2$WindGustSpeed[which(is.na(airausie2$WindGustSpeed))] <- mean(airausie2$WindGustSpeed, na.rm = TRUE)

# WindSpeed9am
airausie2$WindSpeed9am[which(is.na(airausie2$WindSpeed9am))] <- mean(airausie2$WindSpeed9am, na.rm = TRUE)

# WindSPeed3pm
airausie2$WindSpeed3pm[which(is.na(airausie2$WindSpeed3pm))] <- mean(airausie2$WindSpeed3pm, na.rm = TRUE)

# Humidity9am
airausie2$Humidity9am[which(is.na(airausie2$Humidity9am))] <- mean(airausie2$Humidity9am, na.rm = TRUE)

# Humidity3pm
airausie2$Humidity3pm[which(is.na(airausie2$Humidity3pm))] <- mean(airausie2$Humidity3pm, na.rm = TRUE)

# Pressure9am
airausie2$Pressure9am[which(is.na(airausie2$Pressure9am))] <- mean(airausie2$Pressure9am, na.rm = TRUE)

# Pressure3pm
airausie2$Pressure3pm[which(is.na(airausie2$Pressure3pm))] <- mean(airausie2$Pressure3pm, na.rm = TRUE)

# Cloud9am
cloud9am_vector <- c(airausie2$Cloud9am)
cloud9am_vector_nona <- c(na.omit(cloud9am_vector))
cloud9am_mode <- getmode(cloud9am_vector_nona)
airausie2$Cloud9am[which(is.na(airausie2$Cloud9am))] <- cloud9am_mode

# Cloud3pm
cloud3pm_vector <- c(airausie2$Cloud3pm)
cloud3pm_vector_nona <- c(na.omit(cloud3pm_vector))
cloud3pm_mode <- getmode(cloud3pm_vector_nona)
airausie2$Cloud3pm[which(is.na(airausie2$Cloud3pm))] <- cloud3pm_mode

# Temp9am
airausie2$Temp9am[which(is.na(airausie2$Temp9am))] <- mean(airausie2$Temp9am, na.rm = TRUE)

# Temp3pm
airausie2$Temp3pm[which(is.na(airausie2$Temp3pm))] <- mean(airausie2$Temp3pm, na.rm = TRUE)

# RainToday
airausie2$RainToday[which(is.na(airausie2$RainToday))] <- "No"

write.table(airausie2, file="D:/Docs/Data Mining/rain_ausie2.", sep = ",", row.names = FALSE, na = " ")

