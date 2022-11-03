# import the external python file
import cat

# Call the functions from cat.py without passing an argument
print()
cat.purr()
cat.lick()
cat.nap()

# Call the functions from cat.py with arguments
print()
cat.purr('Kitty')
cat.lick('Kitty')
cat.nap('Kitty')

# User input
pet = input('\nEnter a pet name: ')

# Call the functions from cat.py with user input arguments
cat.purr(pet)
cat.lick(pet)
cat.nap(pet)
