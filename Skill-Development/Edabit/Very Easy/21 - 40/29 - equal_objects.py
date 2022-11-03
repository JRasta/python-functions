"""
Check if objOne Is Equal to objTwo

Create a function that checks to see if two object arguments are equal to one another.
Return True if the objects are equal, otherwise, return False
"""

# The first object parameter
obj_one = {
  "name": "Benny",
  "phone": "3325558745",
  "email": "benny@edabit.com"
}

# The second object parameter.
obj_two = {
  "name": "Jason",
  "phone": "9853759720",
  "email": "jason@edabit.com"
}

# The third object parameter
obj_three = {
  "name": "Benny",
  "phone": "3325558745",
  "email": "benny@edabit.com"
}

def is_equal(x, y):
    if x == y:
        print("True")
    else:
        print("False")


is_equal(obj_one, obj_two)
is_equal(obj_one, obj_three)
