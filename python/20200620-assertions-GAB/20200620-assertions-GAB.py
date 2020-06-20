# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 10:37:03 2020

@author: 39492
"""

# some computations generate probabilities below ..
prob_A = 0.11
prob_B = 0.3
prob_C = 0.4
prob_D = 0.2

# sum of probabilities should = 1 so we insert an assert statement
assert sum([prob_A, prob_B, prob_C, prob_D]) == 1

# rest of code...