"""
Less Than 100?

Given two numbers, return True if the sum of both numbers is less than 100. Otherwise, return False
"""

def less_than_100(x, y):
    total = x + y
    if total < 100:
        print("True")
    else:
        print("False")


less_than_100(22, 15)
less_than_100(83, 34)
less_than_100(3, 77)
