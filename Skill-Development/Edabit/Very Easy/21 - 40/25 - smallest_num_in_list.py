"""
Find the Smallest Number in a List

Create a function that takes a list of numbers and returns the smallest number in the list
"""

def find_smallest_num(num_list):
    result = min(num_list)
    print(result)


find_smallest_num([34, 15, 88, 2])
find_smallest_num([34, -345, -1, 100])
find_smallest_num([-76, 1.345, 1, 0])
find_smallest_num([0.4356, 0.8795, 0.5435, -0.9999])
find_smallest_num([7, 7, 7])
