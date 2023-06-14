"""
Return the Remainder from Two Numbers

There is a single operator in Python, capable of providing the remainder of a division operation.
Two numbers are passed as parameters.
The first parameter divided by the second parameter will have a remainder, possibly zero.
Return that value
"""

def remainder(x, y):
    x = int(x)
    y = int(y)

    r = x % y
    print(f'Remainder of {x} / {y} = {r}')


remainder(1, 3)
remainder(3, 4)
remainder(5, 5)
remainder(7, 2)
