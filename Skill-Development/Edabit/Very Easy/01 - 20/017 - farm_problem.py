"""
The Farm Problem

In this challenge, a farmer is asking you to tell him how many legs can be counted among all his animals.
The farmer breeds three species:

* chickens = 2 legs
* cows = 4 legs
* pigs = 4 legs

The farmer has counted his animals, and he gives you a subtotal for each species.
You have to implement a function that returns the total number of legs of all the animals
"""

def animals(chick, cow, pig):
    chick_legs = chick * 2
    cow_legs = cow * 4
    pig_legs = pig * 4
    print(f'Total amount of legs: {chick_legs + cow_legs + pig_legs}')


animals(2, 3, 5)
animals(1, 2, 3)
animals(5, 2, 8)
