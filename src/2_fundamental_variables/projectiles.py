#! /usr/bin/env python3
# Name:         projectiles.py
# Author:       Earl John Gallarde
# Version:      1.0
# Description:  Program that computes the height of a projectile

"""
    Introduces learner to basic Python operations using the math module

    Write a Python program to answer the following question:

    At a barrel height of 1 meter, after a horizontal distance of 0.5m, an elevation of 80
    degrees, and an initial velocity of 44 m/s, what is the height of the projectile?

    To convert degrees (deg) to radians use:
    theta = deg * (pi/180)
"""

# Imports the math and sys modules
import math
import sys

# Acceleration due to gravity: 9.81 m/s squared
g = -9.81

# Initial velocity
Vo = 44

# elevation angle in degrees
theta_in_degrees = 80

# math.pi is a constant value = 3.14159..
print(math.pi)
print("Theta in degrees = ", theta_in_degrees)

# 0 (theta) elevation angle in radians
theta_in_radians = theta_in_degrees * (math.pi / 180)
print("Theta in radians = ", theta_in_radians)

# Horizontal distance travelled
X = 0.5

# Height of the barrel (m)
Yo = 1

# Formula to compute Y, the height of the projectile
# Y = Yo + x tan@ - [gx^2 / 2(Vo cos@)^2 ]

Y = Yo + X * math.tan(theta_in_radians) - (g * math.pow(X, 2) / 2 * (math.pow(Vo * math.cos(theta_in_radians), 2)))
# Quick intro on the use of printf
# Notice the f in front of the string and how the variable Y was used with {} braces
print(f"The height of the projectile is {Y}m")

sys.exit(0)