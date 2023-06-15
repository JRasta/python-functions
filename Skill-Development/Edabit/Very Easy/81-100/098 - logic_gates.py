def NOT(n):
    if n == 1:
        print(0)
    else:
        print(1)

def AND(x, y):
    if x == 1 and y == 1:
        print(1)
    else:
        print(0)

def OR(x, y):
    if x == 1 or y == 1:
        print(1)
    else:
        print(0)


AND(1, 1)  # 1
OR(1, 1)  # 1
AND(0, 1)  # 0
AND(0, 0)  # 0
OR(0, 1)  # 1
OR(1, 0)  # 1
OR(0, 0)  # 0
NOT(0)  # 1
AND(1, 0)  # 0
NOT(1)  # 0
