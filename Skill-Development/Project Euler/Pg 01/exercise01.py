"""
Multiples of 3 or 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

def find_multiples_of_3_or_5(end_point):
    # setup variables
    total = 0
    i = 1

    # convert to an integer
    end_point = int(end_point)

    while i < end_point:
        # find multiples of 3 & 5
        if i % 3 == 0 or i % 5 == 0:
            total += i
        i += 1

    print(f'The natural number of {end_point} has the sum of:', total, '(multiples of 3 or 5)')


find_multiples_of_3_or_5(10)
find_multiples_of_3_or_5(50)
find_multiples_of_3_or_5(100)
find_multiples_of_3_or_5(500)
find_multiples_of_3_or_5(1000)
