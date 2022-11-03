import random

"""
Computer picks a random number for the User to guess
"""
def guess(x):
    random_number = random.randint(1, x)
    guess_number = 0  # declare a number to guess
    while guess_number != random_number:
        guess_number = int(input(f'\nGuess a number between 1 and {x}: '))
        if guess_number > random_number:
            print('Your guess is too high')
        elif guess_number < random_number:
            print('Your guess is too low')

    print(f'Well done!! {random_number} was the random number!!')


guess(100)
