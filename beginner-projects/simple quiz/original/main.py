"""Title: Simple Quiz
Author: J. Smith
Date: 23/11/2022
Description: A simple quiz cli created all manually
"""

import time

# lists for the options
true = ["T", "t", "True"]
false = ["F", "f", "False"]
# correct ans count
correct = 0

# user name
name = input("What's your name?")

# welcome message
print("\nOK, " + name + ", let's get started. Remember, the following answers are only True or False.")
time.sleep(2)

# question 1
print("\nParis is the capitial of France.")
choice = input(">>> ")
if choice in true:
    correct += 1  # If correct, the user gets one point
else:
    correct += 0

# question 2
print("\nEngland is an island.")
choice = input(">>> ")
if choice in false:
    correct += 1
else:
    correct += 0

# question 3
print("\nNorthern Ireland isn't part of Great Britain.")
choice = input(">>> ")
if choice in false:
    correct += 1
else:
    correct += 0

# question 4
print("\nAndorra is between France and Spain.")
choice = input(">>> ")
if choice in true:
    correct += 1
else:
    correct += 0

# question 5
print("\nIran use to be part of the Perisan Empire.")
choice = input(">>> ")
if choice in true:
    correct += 1
else:
    correct += 0

# question 6
print("\nTurkmenistan isn't a real country.")
choice = input(">>> ")
if choice in false:
    correct += 1
else:
    correct += 0

# print final result
print("\nYou're finished, " + name + ". You got", correct, "out of 6 correct.")
