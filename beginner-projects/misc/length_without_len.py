def number_length(num):
    strlen = 0
    num = str(num)
    for c in num:
        strlen += 1

    print(strlen)


number_length(1)
number_length(10)
number_length(100)
number_length(5000)
number_length(50005000)
