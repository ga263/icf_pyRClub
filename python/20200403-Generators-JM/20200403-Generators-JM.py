# -*- coding: utf-8 -*-

# Hey everyone!  George asked me to write a short Python tip for this week, so 
# here goes!  This one's about a core-language feature that maybe doesn't get 
# as much love as it should.

# If you've done much Python coding at all, you've probably seen list 
# comprehensions (and if you haven't, you should take a look!  
# https://www.python.org/dev/peps/pep-0202/).  
# List comprehensions are a fantastic way to write concise and 
# readable code, but that's not actually my tip! 

# My tip of the week is about generator expressions.  These look like list 
# comprehensions without the brackets, but they act very differently behind the 
# scenes and are very useful when working with lots of data!  Why?  A list 
# comprehension will create an entire new object in memory, which can take up 
# quite a bit of space and even slow your code.  A generator expression, however,
# only "generates" each item on the fly, saving you potentially quite a bit of 
# memory!  For example, say you have a very long list of numeric strings, and 
# you want to convert them to numbers and sum them.  You might be tempted to say:

long_list_of_string_numbers = list(range(100000000))
a = sum([float(x) for x in long_list_of_string_numbers])

# But this will create another huge list (of floats, rather than strings) in 
# your memory which is only used for that one sum.  What's a better way?  Just 
# remove those braces and you have a generator expression!

b = sum(float(x) for x in long_list_of_string_numbers)
assert a == b #a and b are equal

# This code only generates one number at a time in memory, so you don't have to
# clog your computer with all those intermediate numbers you'll never look at again!

# Now, this is a really simple example, but this concept can pay off in big 
# savings as you do more complicated operations on bigger sets of data.  
#Take a look at the official docs to learn more! https://www.python.org/dev/peps/pep-0289/

# Hope y'all have had a good week, and are going into a great weekend!