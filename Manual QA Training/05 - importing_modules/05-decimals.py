# imports all the functions from decimal module
from decimal import *

item = 0.70
rate = 1.05

tax = item * rate
total = item + tax

print('Section 1:')
print('Item:\t', '%.2f' % item)  # formats the data to be returned with 2 decimal places
print('Item:\t', item)
print('-----')
print('Tax:\t', '%.2f' % tax)
print('Tax:\t', tax)
print('-----')
print('Total:\t', '%.2f' % total)
print('Total:\t', total)

print('\nSection 2:')
print('Item:\t', '%.20f' % item)  # formats the data to be returned with 20 decimal places
print('Item:\t', item)
print('-----')
print('Tax:\t', '%.20f' % tax)
print('Tax:\t', tax)
print('-----')
print('Total:\t', '%.20f' % total)
print('Total:\t', total)

item = Decimal(0.70)
rate = Decimal(1.05)

print('\nSection 3:')
print('Item:\t', '%.2f' % item)  # formats the data to be returned with 2 decimal places
print('Item:\t', item)
print('-----')
print('Tax:\t', '%.2f' % tax)
print('Tax:\t', tax)
print('-----')
print('Total:\t', '%.2f' % total)
print('Total:\t', total)

