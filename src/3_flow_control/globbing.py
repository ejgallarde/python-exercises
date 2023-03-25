#! /usr/bin/env python3
# Name:         globbing.py
# Author:       Earl John Gallarde
# Version:      1.0
# Description:  This program displays the files in your home directory, with their size.

"""
     Objective:
    To use the flow control structures of Python and to gain familiarity in coding based on indentation!

    Introduce learners to a couple of modules from the Python standard library.
"""
import sys
import glob
import os

# Get the directory name
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
    print('HOMEPATH:', hdir)
else:
    hdir = os.environ['HOME']
    print('HOME:', hdir)

# Construct a portable wildcard pattern
pattern = os.path.join(hdir, '*')
print("Pattern = ", pattern)

# Use glob() to obtain the list of filenames
filenames = glob.glob(pattern)

# Perform a loop on filenames and print
# Use os.path.getsize() to get the file size
# Use os.path.basename() to remove the leading directory name(s)
for file in filenames:
    print(os.path.basename(file), "size:", os.path.getsize(file), "KB")

sys.exit(0)
