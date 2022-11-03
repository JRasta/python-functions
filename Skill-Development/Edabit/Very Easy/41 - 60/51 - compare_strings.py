"""
Compare Strings by Count of Characters

Create a function that takes two strings as arguments and return either True or False depending on whether
the total number of characters in the first string is equal to the total number of characters in the second string
"""

def comp(str_1, str_2):
    total_str_1 = len(str_1)
    total_str_2 = len(str_2)

    if total_str_1 == total_str_2:
        print("True")
    else:
        print("False")


comp("AB", "CD")
comp("ABC", "DE")
comp("hello", "edabit")
