#! /usr/bin/env python3
# Name:         pickacard.py
# Author:       Earl John Gallarde
# Version:      1.0
# Description:  Program that uses the Showcard module to display a single card.

"""
    Program that uses the Showcard module to display a single card.
"""

import sys
import showcard #assume showcard module is available

number = input("Enter a number from 1-52: ")
filename = "BMP" + number + ".GIF"

showcard.display_file(filename)


sys.exit(0)