"""
Maximum Difference

Given a list of integers, return the difference between the largest and smallest integers in the list
"""

def max_difference(lst):
    max_num = max(lst)
    min_num = min(lst)
    total = max_num - min_num
    print(total)


max_difference([10, 15, 20, 2, 10, 6])
max_difference([-3, 4, -9, -1, -2, 15])
max_difference([4, 17, 12, 2, 10, 2])
