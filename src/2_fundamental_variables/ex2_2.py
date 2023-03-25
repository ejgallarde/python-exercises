#! /usr/bin/env python3
# Name:         ex2_2.py
# Author:       Earl John Gallarde
# Version:      1.0
# Description:  To experiment with some of the basic variable types within Python and some of their operations.

"""
    Introduces learner to input(), which takes in a user input
    Introduces learner to basic string manipulations and the len()
    and isdecimal() methods
    Introduces learner to importing python modules (math module)
"""

# Imports the math library to be able to use isdecimal()
import sys

# This is an easy way of outputting a prompt to the console and getting a reply.
# The variable var is a reference to that reply, which is a string.
var = input("Please enter a value: ")

# Using the upper method to print in upper case
print(var.upper())

# Using len() to print the size of the entered value
print(len(var))

# Using isdecimal() to identify if the entered value is a number
# Returns True if yes, False if no
print(var.isdecimal())

sys.exit(0)
