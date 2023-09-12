def absolute_negative(num):
    # Converts a negative number to a positive number
    num = min(-num, num)
    print(num)

absolute_negative(-5) # -5
absolute_negative(-3.14) # -3.14
absolute_negative(250) # -250
absolute_negative(0) # 0
absolute_negative(6.28) # -6.28
absolute_negative(11037) # -11037