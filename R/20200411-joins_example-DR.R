#load the dplyr library
library(dplyr)

#initialize some dummy data
num <- 1:8
id1 <- as.factor(c("a", "b", "b", "c", "c", "c", "y", "z"))

id2 <- as.factor(c("a", "b", "c", "d", "e"))
col <- as.factor(c("red", "green", "blue", "yellow", "white"))

df1 <- cbind.data.frame(num, id1)
df2 <- cbind.data.frame(id2, col)

#name the columns so the two data frames have an overlapping variable
names(df1) <- c("num", "id")
names(df2) <- c("id", "col")

#join the data frames in a few different examples
merged_left <- left_join(df1, df2, by = "id")
merged_right <- right_join(df1, df2, by = "id")
merged_inner <- inner_join(df1, df2, by = "id")
not_merged <- anti_join(merged_left, merged_right)
