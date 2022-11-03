def specialReverse(statement, char):
    str_statement = ''

    word_list = statement.split(' ')

    for word in word_list:
        if word[0] == char:
            reversed_word = word[::-1]
            str_statement = str_statement + ' ' + reversed_word
        else:
            str_statement = str_statement + ' ' + word

    print(str_statement)


specialReverse('word searches are super fun', 's')
specialReverse('first man to walk on the moon', 'm')
specialReverse('peter piper picked pickled peppers', 'p')
