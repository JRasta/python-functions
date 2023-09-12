def all_truthy(*args):
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

all_truthy(True, True, True) # True
all_truthy(False, True, 1, 2, 3) # False
all_truthy(0, 1, 2, 3, 4, 5) # False
all_truthy(1, 2, 7, 84, 357) # True
all_truthy("Hi", "Hello","This was translated from JS to python") # True
all_truthy([], {}, "") # False
