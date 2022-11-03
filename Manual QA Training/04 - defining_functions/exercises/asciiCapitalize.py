def asciiCapitalize(statement):
    str_statement = statement
    new_str_statement = ''

    for char in str_statement:
        ascii_value = ord(char)
        if ascii_value % 2 == 0:
            char = char.upper()
        else:
            char = char.lower()
        new_str_statement += char

    print(new_str_statement)


asciiCapitalize("to be or not to be!")
asciiCapitalize("THE LITTLE MERMAID")
asciiCapitalize("Oh what a beautiful morning")
