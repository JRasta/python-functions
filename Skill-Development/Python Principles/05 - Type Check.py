""" Write a function named only_ints that takes two parameters. Your function should return True if
    both parameters are integers, and False otherwise """

def only_ints(x1, x2):
    if type(x1) == int and type(x2) == int:
        print("True")
    else:
        print("False")


only_ints(10, 20)
only_ints(23.5, 'a')
only_ints(10, "b")
only_ints(21.6, 10)
only_ints(12, 45)
