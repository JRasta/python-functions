"""Title: Rock, Paper, Scissors
Author: J. Smith
Date: 23/11/2022
Description: A simple version of rock, paper, scissors
"""

import random

def get_full_title(selected):
    """Function to get full word of selection
    :param: character
    :return: string
    """

    if selected == 'r':
        return 'rock'
    if selected == 'p':
        return 'paper'
    else:
        return 'scissors'


def play():
    """Main play function
    :param: none
    :return: none
    :print: string
    """

    # user's inputted choice
    user = input("\nWhat's your choice ? 'r' for Rock, 'p' for Paper, 's' for Scissors: ").lower()
    user_choice = get_full_title(user)

    # computer random choice
    computer = random.choice(['r', 'p', 's'])
    computer_choice = get_full_title(computer)

    # if tie, print this message
    if user == computer:
        print(f'\nIt\'s a tie, both players picked {user_choice}')
    else:
        # check who wins
        if is_win(user, computer):
            # winner message
            print(f'\nYou win!, user picked {user_choice} VS computer picked {computer_choice}')
        else:
            # loser message
            print(f'\nYou lose!, user picked {user_choice} VS computer picked {computer_choice}')


def is_win(user, computer):
    """Check to see who wins
    :info: r > s, s > p, p > r
    :param: user's choice, computer's choice
    :return: boolean
    """

    if (user == 'r' and computer == 's') or (user == 's' and computer == 'p') or (user == 'p' and computer == 'r'):
        return True


play()
