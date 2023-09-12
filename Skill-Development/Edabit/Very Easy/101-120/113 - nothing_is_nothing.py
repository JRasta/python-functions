def nothing_is_nothing(*args):
    my_list = []
    for i in args:
        if i:
            my_list.append(True)
        else:
            my_list.append(False)
    if False in my_list:
        result = False
    else:
        result = True
    print(result)

nothing_is_nothing(True, True, True) # True
nothing_is_nothing(False, True, 1, 2, 3) # False
nothing_is_nothing(0, 1, 2, 3, 4, 5) # False
nothing_is_nothing(1, 2, 7, 84, 357) # True
nothing_is_nothing("Hi", "Hello","This was translated from JS to python") # True
nothing_is_nothing([], {}, "") # False
