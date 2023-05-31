def check(lst, number):
    if number in lst:
        print(f'List: {lst}')
        print(f'Required Number: {number}')
        return print(f'Is {number} in the list ==> {True}\n')
    else:
        print(f'List: {lst}')
        print(f'Required Number: {number}')
        return print(f'Is {number} in the list ==> {False}\n')


check([1, 2, 3, 4, 5], 3)  # TRUE
check([1, 1, 2, 1, 1], 3)  # FALSE
check([1, 1, 2, 1, 5, 4, 7], 7)  # TRUE
check([1, 1, 2, 1, 5, 4, 7], 8)  # FALSE
check([5, 5, 5, 6], 5)  # TRUE
check([], 5)  # FALSE
