def less_than_100(num1, num2):
    total = num1 + num2
    if total < 100:
        return True
    else:
        return False


print(less_than_100(22, 15))  # TRUE
print(less_than_100(5, 57))  # TRUE
print(less_than_100(77, 30))  # FALSE
print(less_than_100(0, 59))  # TRUE
print(less_than_100(78, 35))  # FALSE
print(less_than_100(63, 11))  # TRUE

