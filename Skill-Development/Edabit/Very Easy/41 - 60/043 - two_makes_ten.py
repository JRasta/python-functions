"""
Two Makes Ten

Create a function that takes two arguments.
Both arguments are integers, a and b. Return True if one of them is 10 or if their sum is 10
"""

def makes10(x, y):
    total = x + y

    if total == 10 or x == 10 or y == 10:
        print("True")
    else:
        print("False")


makes10(9, 10)
makes10(9, 9)
makes10(1, 9)
