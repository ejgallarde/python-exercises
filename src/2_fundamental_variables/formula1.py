#! /usr/bin/env python3
# Name:         formula1.py
# Author:       Earl John Gallarde
# Version:      1.0
# Description:  Program that computes the minimum fuel requirement of an F1 Race Car

"""
    This program explores some of the mathematics involved in Formula 1 racing car.
    Consider the 3 questions below:

    *** Question 1: "During a race of 45 laps, what is the minimum fuel requirement?"
    You will need to know the fuel consumption found during the race qualifying, which is 2.25kg per lap.

    Typically, a car will carry an extra 50% fuel for contingency.
    *** Question 2: What fuel will be carried by our fictional F1 car at the start of the race?

    The qualifying lap time was 80.45 seconds, but that was with only 5kg of fuel:
    each 10 kg of fuel increases the lap time by 0.35 seconds.
    *** Question 3: What will be the lap time for the first lap with all the required fuel on board?
"""
import sys

# Number of laps
laps = 45

# Basic consumption
fuel_consumption_per_lap = 2.25

# Basic requirement
fuel_requirement = laps * fuel_consumption_per_lap
print("Answer to Question 1")
print("Basic fuel requirement = ", fuel_requirement)

# Contingency load is 50%
contingency_load = 0.5

# Advanced requirement
fuel_requirement = fuel_requirement * (1 + contingency_load)
print("Answer to Question 1")
print("Modified fuel requirement = ", fuel_requirement)

# Theoretical initial lap time
qualifying_lap_time = 80.45
theoretical_lap_time = qualifying_lap_time - (0.35/10) * 5
print("Theoretical initial lap time:", theoretical_lap_time)
print("Answer to Question 3")
lap_one_time = theoretical_lap_time + ((fuel_requirement/10) * 0.35)
print("Lap one time:", lap_one_time, "seconds")

sys.exit(0)
