"""
Difference of Max and Min Numbers in List

Create a function that takes a list and returns the difference between the biggest and smallest numbers
"""

def difference_max_min(lst):
    max_num = max(lst)
    min_num = min(lst)
    difference = max_num - min_num
    print(difference)


difference_max_min([10, 4, 1, 4, -10, -50, 32, 21])
difference_max_min([44, 32, 86, 19])
