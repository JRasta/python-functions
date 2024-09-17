"""
In the Gregorian calendar, three conditions are used to identify leap years:
    The year can be evenly divided by 4, is a leap year, unless:
    The year can be evenly divided by 100, it is NOT a leap year, unless:
    The year is also evenly divisible by 400. Then it is a leap year.

Given a year, determine whether it is a leap year.
If it is a leap year, return the Boolean True, otherwise return False.
"""

# Function
def is_leap(y):
    leap = y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)
    return leap


# Main method
if __name__ == '__main__':
    year = int(input())
    print(is_leap(year))
