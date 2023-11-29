
uniondat = read.csv (file = '/home/bultok/Documents/School/Senior Year/Spring/Stat 310/cleanunion.csv')

uniondat$peernlab[uniondat$peernlab == 0] = NA
uniondat$peernlab
uniondat = na.omit(uniondat)
nrow(uniondat)
uniondat$peernlab[uniondat$peernlab == 2] = 0
uniondat$peernlab


library(MASS)
steplm = lm(peernlab ~., data = uniondat)
stepAIC(steplm, direction ="forward")



logit <- glm(PERNLAB ~ ., data = uniondat, family = "binomial")

install.packages("corrplot")
library(corrplot)
corrplot(res, type = "upper", order = "hclust", 
         tl.col = "black", tl.srt = 45)