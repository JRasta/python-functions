# initialise a string
title = '\nPython In Easy Steps'

# loop -> print every character of the string
for char in title: print(char, end='')

# loop -> prints each char of the string
# replaces -> y with an *
for char in title:
    if char == 'y':
        print(char, '*', end='')
        continue
    print(char, end='')

# loop -> prints each char of the string
# adds * in front of char y
for char in title:
    if char == 'y':
        pass

