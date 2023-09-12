"""
Return the Next Number from the Integer Passed

Create a function that takes a number as an argument, increments the number by +1 and returns the result
"""

def increment(number):
    number = int(number)
    number += 1
    print(f'{number - 1} incremented by 1 equals {number}')


increment(0)
increment(9)
increment(-3)
