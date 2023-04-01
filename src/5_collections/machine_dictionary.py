#! /usr/bin/env python3
# Name:         machine_dictionary.py
# Author:       Earl John Gallarde
# Version:      1.0
# Description:  Program that maintains a Python dictionary

"""
    This exercise focuses on dictionary manipulation
"""

machines = {'user100': 'yogi',
            'user1': 'booboo',
            'user2': 'rupert',
            'user3': 'teddy',
            'user4': 'care',
            'user5': 'winnie',
            'user6': 'sooty',
            'user7': 'padders',
            'user8': 'polar',
            'user9': 'grizzly',
            'user10': 'baloo',
            'user11': 'bungle',
            'user12': 'fozzie',
            'user13': 'hugagy',
            'user14': 'barnaby',
            'user15': 'hair',
            'user16': 'greppy'}

# Implement the following changes:
# user14 no longer has a machine assigned.
machines['user14'] = '-'
print('User14 has', machines['user14'])

# The name of user15's machine is changed to ‘cinnamon’.
machines['user15'] = 'cinnamon'
print('User15 has', machines['user15'])

# user16 is leaving the company and a new user, user17 will be assigned his
# machine.
machines['user17'] = machines['user16']
del machines['user16']
print('User17 has', machines['user17'])
# Access to a deleted item will result in an errors
# print('User17 has', machines['user17'])

# user4, user5, and user6 are all leaving at the same time, but their machine
# names are to be stored in a list called unallocated. Hint: pop in a loop.

unallocated2 = []
for user in ('user4', 'user5', 'user6'):
    unallocated2 += [machines.pop(user)]
print('Unallocated list 2:', unallocated2)

# unallocated = []
# num = 4
# while num < 7:
#     unallocated.append(machines['user' + str(num)])
#     machines['user' + str(num)] = '-'
#     num += 1
# else:
#     print('Unallocated list:', unallocated)

# user8 gets another machine called 'kodiak' in addition to the one they
# already have.
machines['user8'] = [machines['user8'], 'kodiak']
print('User8 has', machines['user8'])

# Print a list of users with their machine in any order. Print each user/machine
# pair on a separate line.
print('\nPrinting all of the users:')
# values() returns only the values
for machine in machines.values():
    print(machine)

print('\nPrinting all of the machines and users:')
# items() returns the key-value pair as tuples
for machine_and_user in machines.items():
    print(machine_and_user)

# Print a list of unallocated machines, sorted alphabetically.
unallocated2.sort()
print('Unallocated list sorted alphabetically:')
for i in unallocated2:
    print(i)
