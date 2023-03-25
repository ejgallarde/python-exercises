#! /usr/bin/env python3
# Name:         countdown.py
# Author:       Earl John Gallarde
# Version:      1.0
# Description:  Program to display a range of numbers by steps of -2

"""
    *** range method ***
 |  range(stop) -> range object
 |  range(start, stop[, step]) -> range object
 |
 |  Return an object that produces a sequence of integers from start (inclusive)
 |  to stop (exclusive) by step.

        range(i, j) produces i, i+1, i+2, ..., j-1.
 |
 |  start defaults to 0, and stop is omitted!
        range(4) produces 0, 1, 2, 3.
 |  These are exactly the valid indices for a list of 4 elements.
 |  When step is given, it specifies the increment (or decrement).

        range(0,7,2) produces 0,2,4,6
"""

import sys

# Prompt user for input
var = input("Enter an integer: ")

if var.isdecimal():
    int_var = int(var)
    while int_var >= 0:
        print(int_var)
        int_var -= 2
else:
    print("Invalid input.")

print("Examples of using range():")

# Sample range with 1 parameter - start
# Print range as a list
list_range = list(range(8))
print(list_range)

# Sample range with 2 parameters - start, and stop
# Print range using a for loop
list_range = range(0, 8)
for num in list_range:
    print(num, end="")

print("\n")
# Sample range with 3 parameters - start, stop, and step
list_range = list(range(0, 9, 3))
print(f"{list_range}")

sys.exit(0)
