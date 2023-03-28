#! /usr/bin/env python3
# Name:         globbing_template.py
# Author:       Earl John Gallarde
# Version:      1.0
# Description:  Use this as a template for globbing.py

"""
    Template for globbing exercise
"""
import sys
import glob
import os

# Get the directory name
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']

# Construct a portable wildcard pattern
pattern = os.path.join(hdir, '*')

sys.exit(0)