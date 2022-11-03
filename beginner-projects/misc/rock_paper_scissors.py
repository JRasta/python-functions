import random

selection = []

def get_full_title(selected):
    if selected == 'r':
        return 'rock'
    if selected == 'p':
        return 'paper'
    else:
        return 'scissors'


def play():
    user = input("\nWhat's your choice ? 'r' for Rock, 'p' for Paper, 's' for Scissors: ").lower()
    user_choice = get_full_title(user)

    computer = random.choice(['r', 'p', 's'])
    computer_choice = get_full_title(computer)

    if user == computer:
        return f'\nIt\'s a tie, both players picked {user_choice}'

    if is_win(user, computer):
        return f'\nYou win!, user picked {user_choice} VS computer picked {computer_choice}'

    return f'\nYou lose!, user picked {user_choice} VS computer picked {computer_choice}'

# return true if user wins
def is_win(user, computer):
    # r > s, s > p, p > r
    if (user == 'r' and computer == 's') or (user == 's' and computer == 'p') or (user == 'p' and computer == 'r'):
        return True


print(play())
