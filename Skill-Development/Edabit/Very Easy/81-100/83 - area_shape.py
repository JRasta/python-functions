def area_shape(dec_base, dec_hgt, str_shape):
    if 'triangle' in str_shape:
        calculation = 0.5 * dec_base * dec_hgt
        print(f'Triangle calculation is: {calculation}')
    else:
        calculation = dec_base * dec_hgt
        print(f'Triangle calculation is: {calculation}')


area_shape(2, 3, 'triangle')  # 3
area_shape(8, 6, 'parallelogram')  # 48
area_shape(0, 1, 'triangle')  # 0
area_shape(2.9, 1.3, 'parallelogram')  # 3.77
area_shape(0.01, 5, 'triangle')  # 0.025
