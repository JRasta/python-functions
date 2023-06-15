def operate(x, y, operator):
    if '+' in operator:
        print(x + y)
    elif '-' in operator:
        print(x - y)
    elif '*' in operator:
        print(x * y)
    elif '/' in operator:
        print(int(x / y))
    elif '%' in operator:
        print(x % y)


operate(1, 1, "+")  # 2
operate(1, 1, "-")  # 0
operate(1, 1, "*")  # 1
operate(1, 1, "/")  # 1
operate(1, 1, "%")  # 0
operate(2, 1, "+")  # 3
operate(2, 1, "-")  # 1
operate(2, 1, "*")  # 2
operate(2, 1, "/")  # 2
operate(2, 1, "%")  # 0
operate(1234, -1234, "-")  # 2468
