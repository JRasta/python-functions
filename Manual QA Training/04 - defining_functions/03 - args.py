# a function with three arguments: user, lang, sys
def echo(user, lang, sys):
    print('User:', user, 'Language:', lang, 'System:', sys)


# function with 3 string values in order they appear
echo('Mike', 'Python', 'Windows')

# function with 3 strings values by specifying argument names
echo(lang='Python', sys='Mac OS', user='Anne')

# define another function, accept 2 arguments with default values
def mirror(user='Carole', lang='Python'):
    print('\nUser:', user, 'Language:', lang)


# call the second function
mirror()

# call the second function with specified overriding values
mirror(lang='Java')
mirror(user='Tony')

# call the second function with overriding values
mirror('Susan', 'C++')
