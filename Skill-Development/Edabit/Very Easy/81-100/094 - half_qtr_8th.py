def half_quarter_eighth(n):
    half_qtr_8th_list = [(n / 2), (n / 4), (n / 8)]
    print(half_qtr_8th_list)


half_quarter_eighth(6)  # [3, 1.5, 0.75]
half_quarter_eighth(22)  # [11, 5.5, 2.75]
half_quarter_eighth(25)  # [12.5, 6.25, 3.125]
half_quarter_eighth(18)  # [9, 4.5, 2.25]
half_quarter_eighth(98)  # [49, 24.5, 12.25]
half_quarter_eighth(14)  # [7, 3.5, 1.75]
