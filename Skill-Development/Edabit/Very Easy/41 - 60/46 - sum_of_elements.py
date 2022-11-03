"""
Get the Sum of All List Elements

Create a function that takes a list and returns the sum of all numbers in the list
"""

def get_sum_of_elements(lst):
    total_num = 0

    for num in lst:
        total_num = num + total_num
    print(total_num)


get_sum_of_elements([2, 7, 4])
get_sum_of_elements([45, 3, 0])
get_sum_of_elements([-2, 84, 23])
