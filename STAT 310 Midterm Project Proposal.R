union = read.csv(file = '/home/bultok/Documents/School/Senior Year/Spring/Stat 310/jan23pub.csv')
union_1 = union
union_1[union_1 < 0] = 0 
install.packages("dplyr")

library(dplyr)
union_1 = union_1 %>%
            na.omit()
write.csv(union_1, '/home/bultok/Documents/School/Senior Year/Spring/Stat 310/cleanunion.csv')
