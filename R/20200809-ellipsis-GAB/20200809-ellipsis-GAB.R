#GAB 2020/08/09

#define function which attaches "thank you." to an arbitrary number of string arguments 
fxn_without_named_arguments = function(...){
  return(paste(..., " thank you."))
}
print(fxn_without_named_arguments("my ", "name ", "is ", "R"))

#define a function without specifying argument names
fxn_with_many_named_arguments = function(...){
  argss <- list(...)
  print(names(argss))
  return(argss$a+argss$b)
}
print(fxn_with_many_named_arguments(a=4, b=9))


#Using ... can make your function very flexible, 
#but to understand how to use it, users need to read that function's documentation
#For instance how can a user know your function expects (or can use) an argument called "a"

#Which means the next time you see a function with ... 
#be sure to read that function's documentation closely if you
#want to find out about more arguments you could use.