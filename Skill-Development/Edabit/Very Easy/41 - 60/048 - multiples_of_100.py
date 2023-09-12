"""
Multiples of 100

Create a function that takes an integer and returns True if it's divisible by 100, otherwise return False
"""

def divide_by_100(x):
    if x % 100 == 0:
        print("True")
    else:
        print("False")


divide_by_100(1)
divide_by_100(1000)
divide_by_100(100)
