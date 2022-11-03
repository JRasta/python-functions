"""
exception example 1
"""

# initialise variable <string>
title = 'Python In Easy Steps'

# try block -> run the code
# if false -> hit the except block
try:
    print(titel)
# except block -> displays an error if NameError is triggered
except NameError as msg:
    # print the error message
    print(msg)


"""
exception example 2
"""

# initialise integer value
day = 32

print()
try:
    # tests the variable value
    if day > 31:
        # specify custom error message
        raise ValueError('Invalid Day Number')
# except block -> display error whe it occurs
except ValueError as msg:
    print('The program found an:', msg)
# finally block -> displays a message after the exception has been handled
finally:
    print('But Today is Beautiful Anyway')
