def value_at(lst, ind):
    ind = eval(str(ind))
    ind = int(ind)
    print(lst[ind])


value_at([1, 2, 3, 4, 5, 6], 10 // 2) # 6
value_at([1, 2, 3, 4], 6.535355314 // 2) # 4
value_at([1, 2], 1.0 // 2) # 1
value_at([1, 2, 3, 4, 5, 6], 8.0 // 2) # 5