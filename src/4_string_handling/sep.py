#! /usr/bin/env python3
# Name:         sep.py
# Author:       Earl John Gallarde
# Version:      1.0
# Description:  To understand the basics of string handling

"""
    This exercise shows the basics of string handling and string manipulation
"""

import sys

# Print the default encoding for strings, which is UTF-8
print(sys.getdefaultencoding())

# The print() function has several named arguments
# end= characters to be appended, default is newline
# file= fileobject to be written to, default is sys.stdout
# sep= separator used between list items, default is a space
# flush= to flush or not to flush, default is False

belgium = "Belgium,11183000,818"
items = belgium.split(",")

# a
count = 0
while count < len(belgium):
    print("-", end="")
    count += 1
else:
    print("")

# b
print(belgium.replace(",", ":"))

# c
print(items)
print(items[0])
print(items[1])
print(items[2])
# index 1 and 2 contain string values so convert them to int first
print(int(items[1]) + int(items[2]))

# d
# You can perform multiplication on string values
print('-' * len(belgium))

sys.exit(0)