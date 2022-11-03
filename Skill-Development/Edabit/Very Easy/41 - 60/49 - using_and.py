"""
Using the "and" Operator

Python has a logical operator and.
The and operator takes two boolean values, and returns True if both values are True
"""


def and_op(x, y):
    if x is True and y is True:
        print("True")
    else:
        print("False")


and_op(True, False)
and_op(True, True)
and_op(False, True)
and_op(False, False)
