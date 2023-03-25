#! /usr/bin/env python3
# Name:         
# Author:       Earl John Gallarde
# Version:      1.0
# Description:  Program that emulates the high-street bank mechanism for checking a PIN.
#               Keep taking input from the keyboard (see below) until itis
#               identical to a password number which is hard-coded by you in the program.

"""
    Note: Hard-coded pin = '12345'

    Passwords, and PINs, would not normally be displayed (echoed) to the screen for
    security reasons. We will add the functionality to hide the characters typed.

    You'll need to import a module called getpass, which is part of the standard library.

"""
import sys
import getpass

hardcoded_pin = '12345'
isMismatch = True
tries = 0
while isMismatch and tries < 3:
    # Basic way for accepting input
    # supplied_pin = input("Enter PIN: ")

    # Using getpass module
    supplied_pin = getpass.getpass("Enter PIN:")
    if supplied_pin != hardcoded_pin:
        print("Incorrect PIN!")
        tries += 1
    else:
        print("Correct! Exiting program.")
        isMismatch = False
        break
else:
    print("Max tries reached. Card confiscated. Thank you.")

sys.exit(0)
