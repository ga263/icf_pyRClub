#GAB 2020/06/20

require(testit)

# some computations generate probabilities below ..
prob_A <- 0.11
prob_B <- 0.3
prob_C <- 0.4
prob_D <- 0.2

# sum of probabilities should = 1 so we insert an assert statement
assert("Sum of all probabilities should equal 1",
       {
       sum(prob_A, prob_B, prob_C, prob_D) == 1
       })

# rest of code...