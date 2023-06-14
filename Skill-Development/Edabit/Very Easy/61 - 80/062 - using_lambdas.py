"""
Using Lambda Functions

Create a function that returns its given argument, but by using a lambda function
"""

def lambda_func(arg):
    (lambda args: print(arg))(arg)


lambda_func(3)
lambda_func("3")
lambda_func(True)
