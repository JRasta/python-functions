"""
Is the String Odd or Even?

Given a string, return True if its length is even or False if the length is odd
"""

def odd_or_even(string):
    length_of_string = len(string)

    if length_of_string % 2 == 0:
        print("True")
    else:
        print("False")


odd_or_even("apples")
odd_or_even("pears")
odd_or_even("cherry")
