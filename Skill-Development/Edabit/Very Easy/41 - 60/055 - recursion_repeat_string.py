"""
Recursion to Repeat a String n Number of Times

Create a recursive function that takes two parameters and repeats the string n number of times.
The first parameter txt is the string to be repeated and the second parameter is
the number of times the string is to be repeated
"""

def repetition(txt, n, c=0):
    if c < n:
        print(txt * n)
        repetition(txt, n, c=c + 1)


repetition("ab", 3)
repetition("kiwi", 1)
repetition("cherry", 2)
