def percentage(percent, amount):
    print(f'Amount\t    : £{amount}')

    # Process
    start_amount = amount
    ans = (amount / 100) * percent
    amount = amount - ans
    start_amount = start_amount - amount

    # Output
    print(f'Percentage  : {int(percent)}%')
    print(f'Amount to go: £{int(start_amount)}')
    print(f'Amount left : £{int(amount)}\n')


if __name__ == '__main__':
    print('10% Club')
    percentage(10, 100)
    percentage(10, 21740)
    percentage(10, 1500)
    print('\n')

    print('20% Club')
    percentage(20, 100)
    percentage(20, 21740)
    percentage(20, 1500)
    print('\n')

    print('30% Club')
    percentage(30, 100)
    percentage(30, 21740)
    percentage(30, 1500)
    print('\n')

    print('40% Club')
    percentage(40, 100)
    percentage(40, 21740)
    percentage(40, 1500)
    print('\n')

    print('50% Club')
    percentage(50, 100)
    percentage(50, 21740)
    percentage(50, 1500)
    print('\n')

    print('60% Club')
    percentage(60, 100)
    percentage(60, 21740)
    percentage(60, 1500)
    print('\n')

    print('70% Club')
    percentage(70, 100)
    percentage(70, 21740)
    percentage(70, 1500)
    print('\n')

    print('80% Club')
    percentage(80, 100)
    percentage(80, 21740)
    percentage(80, 1500)
    print('\n')

    print('90% Club')
    percentage(90, 100)
    percentage(90, 21740)
    percentage(90, 1500)
    print('\n')

    print('100% Club')
    percentage(100, 100)
    percentage(100, 21740)
    percentage(100, 1500)
    print('\n')