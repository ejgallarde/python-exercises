#! /usr/bin/env python3
# Name:         lottery.py
# Author:       Earl John Gallarde
# Version:      1.0
# Description:  This program generates 6 unique lottery numbers from 1 to 50

"""
    DocString:
"""
import random

my_list = [1, 2, 3, 2]
print(type(my_list))
print(my_list)

tup = (1, 2, 3, 1)
print(type(tup))
print(tup)

my_set = {1, 2, 3, 1}
print(type(my_set))
print(my_set)

my_dict = {'one': 1, 'two': 2, 'three': 3}
print(type(my_dict))
print(my_dict)

lottery_numbers = set()
while len(lottery_numbers) < 6:
    lottery_numbers.add(random.randint(1,50))
else:
    print(lottery_numbers)
