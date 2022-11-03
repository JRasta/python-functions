num_list = [2, 8, 7, 5]

def warOfNumbers(n_list):
    even_list = []
    odd_list = []
    even_total = 0
    odd_total = 0

    for num in n_list:
        if num % 2 == 0:
            even_list.append(num)
        else:
            odd_list.append(num)

    for even in even_list:
        even_total += even

    for odd in odd_list:
        odd_total += odd

    if odd_total > even_total:
        overall_total = odd_total - even_total
    else:
        overall_total = even_total - odd_total

    print('Diff:', overall_total)


warOfNumbers(num_list)
