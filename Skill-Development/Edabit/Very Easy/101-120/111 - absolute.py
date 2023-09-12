def absolute(num):
    # Converts a negative number to a positive number
    num = max(-num, num)
    print(num)

absolute(-5) # 5
absolute(-3.14) # 3.14
absolute(250) # 250
absolute(0) # 0
absolute(6.28) # 6.28
absolute(11037) # 11037