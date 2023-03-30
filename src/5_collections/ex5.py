#! /usr/bin/env python3
# Name:         ex5.py
# Author:       Earl John Gallarde
# Version:      1.0
# Description:  Learn basics of collections in Python 3

"""
    DocString:
"""

# This is a list
cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
# cheese += 'Oke'
# Use append() function to add to a list
cheese.append('Oke')
print(cheese)

# This is a string that has a value 'Hello'
tup = 'Hello'
print(len(tup))
# Prints 5

# This is not a string. This is a Python tuple
# Notice the comma at the end. This is a legal way of writing a tuple
tup = 'Hello',
print(len(tup))
# Prints 1