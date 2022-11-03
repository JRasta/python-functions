"""
Concatenating First and Last Character of a String

Create a function that takes a string and returns the concatenated first and last character
"""

def first_last(string):
    first_letter = string[0]
    last_letter = string[-1]
    new_word = first_letter + last_letter
    print(new_word)


first_last("ganesh")
first_last("kali")
first_last("shiva")
first_last("vishnu")
first_last("durga")
