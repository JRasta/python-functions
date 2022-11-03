"""
String to Integer and Vice Versa

Write two functions:
to_int() : A function to convert a string to an integer.
to_str() : A function to convert an integer to a string.
"""

def to_int(obj):
    obj = int(obj)
    print(f"Type of argument: {type(obj)}, argument: {obj}")

def to_str(obj):
    obj = str(obj)
    print(f"Type of argument: {type(obj)}, argument: {obj}")


to_int("77")
to_int("532")
to_str(152)
to_str(578)
