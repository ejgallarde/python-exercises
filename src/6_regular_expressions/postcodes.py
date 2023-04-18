#! /usr/bin/env python3
# Name:         postcodes.py
# Author:       Earl John Gallarde
# Version:      1.0
# Description:  Python script that will perform basic validation and formatting of UK
#               postcodes

"""
    DocString:
"""
import sys
import re

# Open File Handle for READING in TEXT mode.
fh_in = open(r"postcodes.txt", mode="rt")

# Iterate through file handle and read one line at a time
# using an ITERATOR for loop.
print("BEGIN: Using basic string manipulation")
for line in fh_in:
    if line.isspace():
        continue
    else:
        formatted_line = line.replace(' ', '').upper().strip()
        print(formatted_line[:4], formatted_line[4:])
print("END: basic sting manipulation \n")
fh_in.close()  # Flush buffers and close file handles.

fh_in = open(r"postcodes.txt", mode="rt")
# Using regular expressions
print("BEGIN: RegEx")

for line in fh_in:
    if line.isspace():
        continue
    else:
        postcode = re.sub('[\t\n ]', '', line)
        postcode = postcode.upper().rstrip()
        # Notice the grouping enclosed in ()
        # r indicates raw strings - In a raw string, however,
        # the backslash "" character is treated as a literal character,
        # rather than as an escape character.
        postcode = re.sub(r"([0-9][A-Z]{2}$)", r" \1", postcode)
        print(postcode)

print("END: RegEx")

fh_in.close()  # Flush buffers and close file handles.

sys.exit(0)
