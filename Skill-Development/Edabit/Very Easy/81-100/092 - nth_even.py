def nth_even(num):
    if num == 1:
        print(0)
    else:
        num = num - 1
        print(num * 2)


nth_even(1)  # 0
nth_even(2)  # 2
nth_even(3)  # 4
nth_even(100)  # 198
nth_even(1298734)  # 2597466
