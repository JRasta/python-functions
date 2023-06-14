def pos_com(s):
    if '1' in s and '0' not in s:
        print(f'No of switches : {s}')
        s = int(s)
        print(f'Total Combos   : {s * 2}\n')
    else:
        print(f'No of switches : {s}')
        s = int(s)
        print(f'Total Combos   : {2 ** s}\n')


pos_com('5')  # 32
pos_com('4')  # 16
pos_com('3')  # 8
pos_com('2')  # 4
pos_com('1')  # 2
pos_com('6')  # 64
pos_com('7')  # 128
pos_com('8')  # 256
pos_com('9')  # 512
pos_com('10')  # 1024
pos_com('25')  # 33554432
