"""
Front 3 - Slice Check Repeat Concatenate

Create a function that takes a string; we'll say that the front is the first three characters of the string.
If the string length is less than three characters, the front is whatever is there.
Return a new string, which is three copies of the front
"""

def front3(string):
    new_string = string[0:3]
    print(new_string * 3)


front3("Python")
front3("Cucumber")
front3("bioshock")
