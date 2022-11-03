"""
Not finished yet!!!
"""

def to_scottish_screaming(phrase):
    # Variables
    convert_phrase = ''

    # Convert phrase to all lowercase
    phrase = phrase.lower()

    # Iterate through the string
    for char in phrase:
        if char == 'a':
            phrase = phrase.replace(char, 'e')
        elif char == 'i':
            phrase = phrase.replace(char, 'e')
        elif char == 'o':
            phrase = phrase.replace(char, 'e')
        elif char == 'u':
            phrase = phrase.replace(char, 'e')

    # Convert string to all uppercase
    phrase = phrase.upper()
    print(phrase)


to_scottish_screaming('hello world')
to_scottish_screaming('Mr Fox was very naughty')
to_scottish_screaming('Butterflies are beautiful!')
