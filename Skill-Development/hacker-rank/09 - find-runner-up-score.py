"""Given the participants' score-sheet for your University Sports Day, you are required to find the runner-up score.
You are given N scores. Store them in a list and find the score of the runner-up.

Author: J. Smith
Date: May 2024
Lang: Pypy3
"""

if __name__ == '__main__':
    # Original code
    n = int(input("Enter number of scores: "))
    arr = map(int, input("Enter scores:").split())

    # Convert into a set -- remove duplicates
    new_list = set(arr)

    # Remove largest number
    new_list.remove(max(new_list))

    # Print next largest number
    print(max(new_list))
