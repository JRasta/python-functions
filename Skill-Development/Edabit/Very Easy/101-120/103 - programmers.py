def programmers(one, two, three):
    lst = [one, two, three]
    max_pay, min_pay = max(lst), min(lst)
    res = max_pay - min_pay
    print(res)


programmers(1, 5, 9)  # 8
programmers(43, 33, 43)  # 10
programmers(88, 14, 23)  # 74
programmers(33, 72, 74)  # 41
programmers(147, 33, 526)  # 493
programmers(234, 345, 457)  # 223