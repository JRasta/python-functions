def destruct_code(lst):
    first, second, third, *other = lst
    print(first)
    print(second)
    print(third)
    print(other)


destruct_code([1, 2, 3, 4, 5, 6, 7, 8])
