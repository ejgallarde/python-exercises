#! /usr/bin/env python3
# Name:         zellers_congruence.py
# Author:       Earl John Gallarde
# Version:      1.0
# Description:  Program that asks for a date in DD/MM/YYYY format
#               and print sout the day of the week for the date.

"""
    There is a formula, called Zeller's Congruence, which calculates the day of the
    week from a given day, month and year. Zeller's congruence is defined as
    follows:

    z=(1+d+(m*2)
    +(3* (m+1)/5)
    +y + y/4 - y/100 + y/400) % 7
    where d, m and y are day, month, year and z are an integer (0 = Sun, 6 = Sat).
"""

import sys
import string

dateEntered = input("Enter a date in this format (DD/MM/YYYY): ")

# Extract day, month, year from entered value
date_split = dateEntered.split("/")
print(date_split)
d = int(date_split[0])
m = int(date_split[1])
y = int(date_split[2])
print("day:", d, "month:", m, "year:", y)

# Compute if y is a leap year
isLeapYear = y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)
print(y, "isLeapYear: ", isLeapYear)

# Perform adjustments
if m == 1 or m == 2:
    m += 12
    if isLeapYear:
        d -= 2
    else:
        d -= 1

# Division
print("single / divide: ", 2 / 4)  # evaluates to 0.5
print("double // divide: ", 2 // 4)  # returns 0

# Use Zeller's Congruence
z = (1 + d + (m * 2) + (3 * (m + 1) // 5) + y + y // 4 - y // 100 + y // 400) % 7

# Print the day
days = ['Sun', 'Mon', 'Tues', 'Wednes', 'Thurs', 'Fri']
print(days[z] + 'day')

# Alternative way to print the day
# if z == 0:
#     print("Sunday")
# elif z == 1:
#     print("Monday")
# elif z == 2:
#     print("Tuesday")
# elif z == 3:
#     print("Wednesday")
# elif z == 4:
#     print("Thursday")
# elif z == 5:
#     print("Friday")
# else:
#     print("Saturday")

sys.exit(0)
