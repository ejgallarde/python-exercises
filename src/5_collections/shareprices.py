#! /usr/bin/env python3
# Name:         shareprices.py
# Author:       Earl John Gallarde
# Version:      1.0
# Description:  This program calculates random share prices for some fictional companies
#               and displays them all continually, with a two-second delay between each display.

"""
    DocString:
"""
import time
import random

share_prices = {'Global Motors': 50,
                'Big Blue Inc.': 50,
                'Gates Software': 50,
                'Banana Computers': 50
                }

while True:
    # We use the items() method to get a view object of the key-value pairs in the dictionary
    for share, price in share_prices.items():
        price = max(1.0, price * (1 + ((random.random() - 0.5) / 0.5) * 0.05))
        share_prices[share] = price
        print("{:<18s}${:05.2f}".format(share, share_prices[share]))
        print()
        time.sleep(2)
