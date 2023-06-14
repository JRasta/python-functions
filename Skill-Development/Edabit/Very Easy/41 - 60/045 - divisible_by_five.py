"""
Check if an Integer is Divisible By Five

Create a function that returns True if an integer is evenly divisible by 5, and False otherwise
"""

def divisible_by_five(x):
    if x % 5 == 0:
        print("True")
    else:
        print("False")


divisible_by_five(5)
divisible_by_five(-55)
divisible_by_five(37)
