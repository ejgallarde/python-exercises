#! /usr/bin/env python3
# Name:         ex2.py
# Author:       Earl John Gallarde
# Version:      1.0
# Description:  This exercise carries out some basic operations on variables.

"""
    This exercise carries out some basic operations on variables.
    Introduces learner to lists and dictionaries
"""
import sys

firstName = "Earl John"
lastName = "Gallarde"
print(firstName, lastName)

nameList = [firstName, lastName]
# Access individual list values
print(nameList[0], nameList[1])

# Prints as a list
print(nameList)

nameDict = {'first': firstName, 'last': lastName}
# Access individual dictionary values
print(nameDict['first'], nameDict['last'])

# Prints the entire dictionary
print(nameDict)

sys.exit(0)