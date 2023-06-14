"""
Concatenate First and Last Name into One String

Given two strings, first_name and last_name, return a single string in the format "last, first"
"""

def concat_name(first, last):
    name_str = last + ", " + first
    print(name_str)


concat_name("First", "Last")
concat_name("John", "Doe")
concat_name("Mary", "Jane")
