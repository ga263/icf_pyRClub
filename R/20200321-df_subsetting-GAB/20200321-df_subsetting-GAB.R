# create a random data frame
df <- data.frame(column1 = 1:10,
                 column2 = 1:10,
                 column3 = 1:10,
                 column4 = 1:10)

# TASK1: subset the first 5 rows of column2 
# and column 4

# The typical way to do it by indexing
df_5rows = df[1:5, c(2,4)] 
# df_5rows is a data.frame, no problem

#==

# Task2: subset the first 5 rows of only column1

# OPTION #1:
df_column1a <- df[1:5, c(1)]
# df_column1a is a vector, NOT a data.frame

# ok maybe we can convert back to data.frame
convert_df <- as.data.frame(df_column1a)
# but convert_df loses original column name and
# we need one additional line of code to set it:
colnames(convert_df) <- c("column1")


# OPTION #2 (better):
df_column1b <- df[1:5, c(1), drop = FALSE]
# df_column1b is a data.frame, no problem

# NOTES
# I) The "matrix" function has this problem as well,
# so be sure to use drop = FALSE when subsetting a
# matrix

# II) data.table does not have this problem

# III) data.table is also faster than data.frame so 
# perhaps use data.table instead of data.frame when 
# working with data