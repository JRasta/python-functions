# define 3 functions to return a passed argument raised to various powers
def power_2(x): return x ** 2
def power_3(x): return x ** 3
def power_4(x): return x ** 4


# create a list of the 3 functions
# NB: minus the parenthesis
callbacks = [power_2, power_3, power_4]

# display heading and result of each named functions
print('\nNamed Functions:')
for power_to in callbacks:
    # essentially saying: print('Result', power_2(3) | power_3(3) | power_4(3))
    print('Result:', power_to(3))

# create a list of anon functions
callbacks = [lambda x: x ** 2, lambda x: x ** 3, lambda x: x ** 4]

# display heading and result of each named functions
print('\nAnon Functions:')
for anon_func in callbacks:
    # essentially saying: print('Result', lambda(3))
    print('Result:', anon_func(3))
