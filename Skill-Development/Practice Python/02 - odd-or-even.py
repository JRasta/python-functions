"""
Odd or Even

Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user

Extra(s):
1) If the number is a multiple of 4, print out a different message
2) Ask the user for two numbers: one number to check (call it num) and one number to divide by (check)
   If check divides evenly into num, tell that to the user. If not, print a different appropriate message
"""

number = input("Enter a number: ")
number = int(number)

if number % 2 == 0:
    if number % 4 == 0:
        print("Number is even & divisible by 4 also")
    else:
        print("Number entered is even")
else:
    print("Number entered is odd")
