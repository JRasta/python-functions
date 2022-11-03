"""
Miserable Parody of a Calculator

Create a function that will handle simple math expressions. The input is an expression in the form of a string
"""

def calculator(expression):
    new_expression = eval(expression)
    print(int(new_expression))


calculator("23+4")
calculator("45-15")
calculator("13+2-5*2")
calculator("49/7*2-3")
