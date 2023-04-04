#! /usr/bin/env python3
# Name:         words.py
# Author:       Earl John Gallarde
# Version:      1.0
# Description:  This program searches for words in a text file using loops.

"""
    This lesson focuses on the usage of loops, lists, and dictionaries.
    It also explores the reading of text files using the open() method.
"""
import string
import sys


def brute_force() -> string:
    # TO-DO
    # Use a counting 'for' loop to search sequentially for the word "Zulu'. When found,
    # break out of the loop and return the word's position, plus 1 (which is the line
    # number in the file).
    # Open file handle for Reading Mode.
    file = open(r"C:\Users\ecgallar\PycharmProjects\python-exercises\src\5_collections\words.txt", mode="rt")

    # Iterate through each line of the file handle using an ITERATOR for loop.
    counter = 0
    for line in file:
        if 'Zulu' == line.strip():
            break
        else:
            counter += 1

    # Flush buffers and close file handle.
    file.close()
    return counter + 1


print(brute_force())


def get_using_index():
    # TO-DO
    # The next function to complete is rather less code. Recall the index() method
    # which may be called on a list. It returns the position of the first item found
    # with the given value. Call this in the index() function, returning the position
    # plus 1. Test the script, is index() faster than brute force?
    fh_in = open(r"C:\Users\ecgallar\PycharmProjects\python-exercises\src\5_collections\words.txt", mode="rt")

    # Prints the type of the file handler - TextIOWRapper
    # print(type(fh_in))

    # Use read() to read the contents into a string variable
    # text = fh_in.read()

    # Use readlines() to read the contents into a list of strings
    # Note that each string in the list includes the newline character \n at the end,
    # which represents the end of the line in the file.
    # If you want to remove the newline characters from the strings,
    # you can use the strip() method on each string.
    lines = [line.strip() for line in fh_in.readlines()]
    index = lines.index('Zulu')

    # Flush buffers and close file handle.
    fh_in.close()
    return index + 1


print(get_using_index())

# Create a dictionary called words_dict where the keys are the words
fh_in = open(r"C:\Users\ecgallar\PycharmProjects\python-exercises\src\5_collections\words.txt", mode="rt")

# Iterate through each line of the file handle using an ITERATOR for loop.
words_dict = {}
count = 0
for line in fh_in:
    words_dict.update({line: count + 1})
    count += 1

# Flush buffers and close file handle.
fh_in.close()

print(words_dict)

sys.exit(0)
