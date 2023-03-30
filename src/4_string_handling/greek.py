#! /usr/bin/env python3
# Name:         greek.py
# Author:       Earl John Gallarde
# Version:      1.0
# Description:  Program that plays with unicode characters, particularly the Greek alphabet.

"""
    This exercise demonstrates the use of f strings and techniques in formatting
"""
import sys

greek = ['Alpha', 'Beta', 'Gamma', 'Delta', 'Epsilon', 'Zeta',
         'Eta', 'Theta', 'Iota', 'Kappa', 'Lambda', 'Mu', 'Nu',
         'Xi', 'Omicron', 'Pi', 'Rho', 'Sigma final', 'Sigma', 'Tau', 'Upsilon',
         'Phi', 'Chi', 'Psi', 'Omega']

try:
    pos = 0x03b1
    for name in greek:
        print(f"{pos:#x} {name:<12s} : {chr(pos)} {chr(pos).upper()}")
        pos += 1
except UnicodeError as err:
    print('unknown', err)

sys.exit(0)
