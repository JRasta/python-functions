"""
PROJECT: A game called Pig
DATE: 12/12/2023
VIDEO: Tech With Tim - YT
LINK: https://www.youtube.com/watch?v=21FnnGKSRZo&t=142s

DESCRIPTION: When you roll the dice, you're going to get some number from 1 to 6.
If you get anything other than one, you take that number, and you add that number to the score of your turn
You can roll as many times as you like. Now the catch is as soon as you hit a one,
whatever you got on your roll is going to be your turn finished. Whatever you got on your turn is now zero
MAX SCORE: Be anything -- This case it will be 50

IE: Roll 01 - 5 -- Score: 5
    Roll 02 - 3 -- Score: 5+3=8
    Roll 03 - 2 -- Score: 8+2=10
    Roll 04 - 1 -- Score: 10 -- End of turn
"""
import random


def roll():
    min_value = 1
    max_value = 6
    # create a random number between 1 and 6 (inclusive)
    roll_num = random.randint(min_value,max_value)
    return roll_num

# get the number of players
while True:
    players = input("Enter the number of players (2 - 4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break  # breaks while loop
        else:
            print("Must be between 2 - 4 players.")
    else:
        print("Invalid, please try again.")

max_score = 50

# list comprehension -- creates a 0 (placeholder) for each player's total score
# IE: Enter the number of players (2 - 4): 3 -- player_scores: [0, 0, 0]
player_scores = [0 for _ in range(players)]


# full game mode
while max(player_scores) < max_score:

    # player x
    for player_idx in range(players):
        print(f"\nPlayer {player_idx + 1} turn has just started!")
        print(f"Your total score is: {player_scores[player_idx]}\n")
        current_score = 0

        # turn
        while True:
            should_roll = input("Would you like to roll (y)? ")
            if should_roll.lower() != "y":
                break
            value = roll()

            if value == 1:
                print("You rolled a 1! Turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print(f"You rolled a {value}")
            print(f"Your score is: {current_score}")

        # turn score
        player_scores[player_idx] += current_score
        print(f"Your total score is: {player_scores[player_idx]}")

# final score
max_score = max(player_scores)
win_idx = player_scores.index(max_score)
print(f"\nPlayer {win_idx + 1} is the winner with a score of: {max_score}")