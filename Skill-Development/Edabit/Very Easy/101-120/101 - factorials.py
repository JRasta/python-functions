def factorial(n):
    maxi = n
    total = 0
    res = 0

    while maxi > 0:
        if maxi == 1:
            next_no = 1
        else:
            next_no = maxi - 1
        if n == maxi:
            total = maxi * next_no
        else:
            total = res * next_no
        res = total
        maxi = maxi - 1
    print(res)


factorial(1)  # 1! = 1
factorial(2)  # 2! = 2
factorial(3)  # 3! = 6
factorial(4)  # 4! = 24
factorial(5)  # 5! = 120
factorial(6)  # 6! = 720
factorial(7)  # 7! = 5040
factorial(8)  # 8! = 40320
factorial(9)  # 9! = 362880
factorial(10)  # 10! = 3628800
