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


"""
Users picks a random number for the computer to guess
"""
def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    guess_number = 0
    print('\n')
    while feedback != 'c':
        if low != high:
            guess_number = random.randint(low, high)
        else:
            guess_number = low
        feedback = input(f'Is {guess_number} too high (H), too low (L) or correct (C)?? ').lower()
        if feedback == 'h':
            high = guess_number - 1
        elif feedback == 'l':
            low = guess_number + 1

    print(f'\nYay! The computer guessed your number, {guess_number}, correctly!')


computer_guess(10)
