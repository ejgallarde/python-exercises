#! /usr/bin/env python3
# Name:         leap_year.py
# Author:       Earl John Gallarde
# Version:      1.0
# Description:  Program that identifies if the entered year is a leap year

"""
    If a year is exactly divisible by 4 but not by 100, the year is a leap year. There is
    an exception to this rule. Years exactly divisible by 400 are leap years. The year
    2000 is a good example.
"""

import sys

isResume = 'y'
while 'y' == isResume.lower():
    year = int(input('Please enter a year: '))

    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print(f"{year} is leap year")
        isResume = input('Continue? y/n : ')
    else:
        print(f"{year} is NOT a leap year")
        isResume = input('Continue? y/n : ')
else:
    print("Thank you.")

sys.exit(0)
