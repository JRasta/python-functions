import random
import string

from words import words

def get_valid_word(word):
    r_word = random.choice(word)
    while '-' in word or ' ' in word:
        r_word = random.choice(word)
    return r_word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 6
    print('\n')

    # get user input
    while len(word_letters) > 0 and lives > 0:
        # letters the user has already used
        print('\nYou have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))
        # tell the user what the word is with dashes
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))
        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                print('Letter is not in word')

        elif user_letter in used_letters:
            print('You have already used this character. Please try again!')
        else:
            print('Invalid character. Please try again')

    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print('\nYou died, sorry. The word was ', word)
    else:
        print('\nYou guessed the word', word, '!!')


hangman()
