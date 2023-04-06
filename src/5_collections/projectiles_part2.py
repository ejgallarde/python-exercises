#! /usr/bin/env python3
# Name:         projectiles_part2.py
# Author:       Earl John Gallarde
# Version:      1.0
# Description:  Program that computes the height of a projectile

"""
    Extension of Exercise 2: projectiles
    This exercise focuses more on the use collections. It also introduces the use of the matplotlib module.
"""

# Imports the math and sys modules
import math
import sys
import matplotlib.pyplot as pyplot

# Acceleration due to gravity: 9.81 m/s squared
g = -9.81
# Initial velocity
Vo = 44
# elevation angle in degrees
theta_in_degrees = 80
# 0 (theta) elevation angle in radians
theta_in_radians = theta_in_degrees * (math.pi / 180)
# Height of the barrel (m)
Yo = 1

# Horizontal distance
x = 0.0
y = Yo
x_axis = []
y_axis = []

while y > 0 and x <= 0.5:
    x_axis.append(x)
    y_axis.append(y)
    print('x={:.1f}m, y={:1f}m'.format(x, y))
    y = Yo + x * math.tan(theta_in_radians) - (g * math.pow(x, 2) / 2 * (math.pow(Vo * math.cos(theta_in_radians), 2)))
    x += 0.1


# Graph
pyplot.ylabel('Height m')
pyplot.xlabel('Distance m')

# Optional realism
pyplot.ylim(-1, max(max(x_axis), max(y_axis)))

pyplot.plot(x_axis, y_axis)
pyplot.show()

sys.exit(0)
