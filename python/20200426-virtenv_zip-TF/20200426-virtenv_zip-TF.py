# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 21:25:21 2020

@author: 39492
"""
# TIP #1

# If you aren’t already using virtual environments, you should be! Rather than 
# having a single instance of Python on your system, you can have a separate 
# environment for each project / task / etc. You can then “pip install” needed 
# packages into this particular environment without cluttering up others that 
# don’t need it. This reduces the chance of running into compatibility issues 
# between packages and lowers the chance of “but it works on MY computer” issues.
# The exact way to do this depends a little on how you’ve installed Python - for 
# instance if you’ve installed a distribution like Anaconda, that has its own way 
# of managing virtual environments) - but https://docs.python-guide.org/dev/virtualenvs/ is a good place to start.

# TIP #2

# “zip” is a great function that can save some effort if you are navigating 
# multiple iterables at once – it “zips” them together and you get an iterator 
# of tuples. You use like:

cities = [ "Durham", "Northfield", "Fairfax" ]
states = [ "NC", "MN", "VA" ]
info = [ "really hot", "snowy", "trafficky" ]

for city, state, misc in zip(cities, states, info):
    print(f"{city} is in {state} and its {misc} there.")

# """
# Durham is in NC and its really hot there.
# Northfield is in MN and its snowy there.
# Fairfax is in VA and its trafficky there.
# """