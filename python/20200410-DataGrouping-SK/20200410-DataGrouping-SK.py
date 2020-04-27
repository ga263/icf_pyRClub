# -*- coding: utf-8 -*-
import pandas as pd

# Happy Friday  R/Python Club!  I have the Python Tip for this week, and I’m 
# going to use my moment to talk about favorite Python library and easy ways of 
# grouping/aggregating data.  This tip is aimed at those who want to get started 
# using Python for some basic data analysis and data wrangling!    

# If you are not familiar with Pandas, it’s a flexible and easy to use library 
# for data analysis and data manipulation.  What’s really nice about Pandas is 
# that it takes data (like a CSV) and creates an object called a “data frame”. 
# A data frame can be thought of as a table similar to Excel (R coders will see
# similarities to R as well), but with the power of Python behind it.  

# I’m going to skip over installing the library and reading in data.  I promise
# it’s straight forward; if you need some help getting started, here is a 
# helpful tutorial (https://towardsdatascience.com/a-quick-introduction-to-the-pandas-python-library-f1b678f34673). 
# What I really want to discuss is  “groupby” and “agg”.  These are probably my
# most used functions in Python, and are also useful tools beginners can use 
# for basic analysis.

# Within Pandas, “groupby” allows you to take data and split that data into 
# groups based on some criteria.  While grouping data is great, it becomes 
# really cool if we can perform some sort of aggregation or transformation 
# while we do it. Say we have a really important dataset as a Panda’s data 
# frame (named ‘df’), like below:

df = pd.DataFrame({"Week":["A","A","B","B","C","C"],
                   "Day":["Monday","Friday","Monday","Friday","Monday","Friday"],
                   "Coffees Consumed":[5,1,4,2,3,1],
                   "Hours of Sleep":[8,7,10,7,4,12]})

# We want to get the mean, min, and max number of coffees I consumed, grouped 
# by the day of the week.  Using groupby and aggregate we can easily get those 
# values.  First, we group the data using the groupby function, df.groupby(‘Day’)… . 
# With the data grouped, we can then aggregate (.agg) the data using a dictionary.  
# The dictionary takes the column that you are aggregating as a key, and a list 
# of aggregation functions as its value, .agg({‘Coffees Consumed’ : [‘mean’,’min’,’max’]}). 
# The resulting code would look like this:

grouped_data = df.groupby("Day").agg({"Coffees Consumed" : ["mean","min","max"]})
print(grouped_data)

# Once you get proficient with the basics, the aggregation function can even 
# take your own custom aggregation methods using Python’s lambda function, a 
# tip for another day!  Next time you are going to pull out Excel to do some 
# simple data analysis, give Pandas a try! It might be slightly slower initially,
# but its powerful once you have the basics down.