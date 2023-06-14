"""
Sum of List Less Than 100 List Remix

Given a list of numbers, return True if the sum of the values in the list is less than 100; otherwise return False
"""

def list_less_than_100(lst):
    new_num = 0

    for num in lst:
        new_num = num + new_num

    if new_num < 100:
        print("True")
    else:
        print("False")


list_less_than_100([5, 57])
list_less_than_100([77, 30])
list_less_than_100([0])
