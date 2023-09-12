"""
Divides Evenly

Given two integers, a and b, return True if a can be divided evenly by b. Return False otherwise
"""

def divide_evenly(x, y):
    total = x / y

    if total.is_integer():
        print("True")
    else:
        print("False")


divide_evenly(98, 7)
divide_evenly(85, 4)
