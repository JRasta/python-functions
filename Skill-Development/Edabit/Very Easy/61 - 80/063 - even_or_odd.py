"""
Even or Odd?

Given a list of integers, determine whether the sum of its elements is even or odd
"""

def even_or_odd(lst):
    total_num = 0

    for num in lst:
        total_num = num + total_num

    if total_num % 2 == 0:
        print("True")
    else:
        print("False")


even_or_odd([0])
even_or_odd([1])
even_or_odd([])
even_or_odd([0, 1, 5])
even_or_odd([0, 1, 4])
even_or_odd([0, 1, 6])
even_or_odd([0, 1, 8])
