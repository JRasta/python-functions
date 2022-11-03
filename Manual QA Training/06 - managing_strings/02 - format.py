# assign Burger to 1st {}
# assign Fries to 2nd {}
snack = '{} and {}'.format('Burger', 'Fries')
print('\nReplaced: ', snack)

# assign Fries to 1st {}
# assign Burger to 2nd {}
snack = '{1} and {0}'.format('Burger', 'Fries')
print('\nReplaced: ', snack)

# assign Milk to 1st %s
# assign Cookies to 2nd %s
snack = '%s and %s' % ('Milk', 'Cookies')
print('\nSubstituted: ', snack)
