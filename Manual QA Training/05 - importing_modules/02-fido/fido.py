# import the functions from the external python file
from dog import bark, lick, nap

# Call the functions from dog.py without passing an argument
print()
bark()
lick()
nap()

# Call the functions from dog.py with arguments
print()
bark('Fido')
lick('Fido')
nap('Fido')

# User input
pet = input('\nEnter a pet name: ')

# Call the functions from dog.py with user input arguments
bark(pet)
lick(pet)
nap(pet)

