"""
Are the Numbers Equal?

Create a function that returns True when num1 is equal to num2; otherwise return False
"""

def is_same_num(x, y):
    if x == y:
        result = True
    else:
        result = False
    print(result)


is_same_num(4, 8)
is_same_num(2, 2)
is_same_num(2, "2")
