from math import ceil, floor

def years_in_one_house(age, moves):
    moves = moves + 1
    ans = age / moves
    decimal_point = str(ans).split('.')
    decimal_point = decimal_point[1]
    if '5' in decimal_point[0] or '4' in decimal_point[0] or '3' in decimal_point[0]:
        print(int(floor(ans)))
    else:
        print(int(ceil(ans)))


years_in_one_house(30, 1)
years_in_one_house(15, 2)
years_in_one_house(80, 0)
years_in_one_house(23, 2)
years_in_one_house(31, 2)
years_in_one_house(1, 0)
