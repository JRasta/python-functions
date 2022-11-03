# imports the math and random Python modules (built-in to Python)
import math, random

print('Rounded up 9.5:   ', math.ceil(9.5))
print('Rounded down 9.5: ', math.floor(9.5))

num = 4
print()
print(num, 'squared:     ', math.pow(num, 2))
print(num, 'square root: ', math.sqrt(num))

# creates a random selection of 6 numbers between the range of 1-59
nums = random.sample(range(1, 59), 6)
nums.sort()
print('\nWinning Lotto numbers: ', nums)
