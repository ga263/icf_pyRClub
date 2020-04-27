#from Graham Glen - 03/26/2020


x <- c(5,2,7)
for (i in 1:length(x)) {
  cat(i, x[i],"\n")
}

# This produces the expected result:
  
# 1 5 
# 2 2 
# 3 7 

#But this does not work if the upper bound is zero:
  
y <- x[x>10]
for (i in 1:length(y)) {
  cat(i, y[i], "\n")
}

# which produces

# 1 NA 
# 0  

# The problem is that the loop is done twice (with i=1 and i=0) when you don’t want 
# it done at all.  R has a rule that sequences automatically decrease 
# if the second value is less than the first, so z <- 1:0 is a list of length two.


# To get the correct behavior I usually just put the loop inside a test:
  
y <- x[x>10]
if (length(y)>0) {
  for (i in 1:length(y)) {
    cat(i, y[i], "\n")
  }
}

#Then it does nothing.