"""
Length of Number

Create a function that takes a number num and returns its length
The use of the len() function is prohibited
"""

def length_of_number(num):
    count = 0

    num = str(num)
    for _ in num:
        count += 1
    print(count)


length_of_number(10)
length_of_number(5000)
length_of_number(1)
