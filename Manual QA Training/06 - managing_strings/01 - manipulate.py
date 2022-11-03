def display(s):
    """Display an argument value"""
    print(s)


# call the function to display the comment
display(display.__doc__)  # prints out the multi-line comment within the function


# display a raw string
display(r'C:\Program Files')
"""
A Python raw string is created by prefixing a string literal with 'r' or 'R'
Python raw string treats the backslash character (\) as a literal character'
This is useful when we want to have a string that contains a backslash character
and don't want it to be treated as an escape character 

In Python strings, the backslash (\) is a special character, also called the 'escape' character.
It is used in representing certain whitespace characters: 
'\t' is a tab, '\n' is a new line, and '\r' is a carriage return
"""

# display a concatenation of 2 strings
display('\nHello' + 'Python')

# display a splice of a specified string
display('Python In Easy Steps\n'[10:])  # selects the string starting at index 10

# display results of seeking characters within a specified string - returns a boolean value
# remember when searching for characters of a string Python is case-sensitive
display('P' in 'Python')
display('p' in 'Python')
