"""Task
The provided code stub reads two integers, a and b, from STDIN.

Add logic to print two lines. The first line should contain the result of integer division,  a // b.
The second line should contain the result of float division, a / b.

No rounding or formatting is necessary.

Author: J. Smith
Date: September 2023
Lang: Pypy3
"""

if __name__ == '__main__':
    a = int(input("Enter 1st number: "))
    b = int(input("Enter 2nd number: "))

    print("Integer division: ", a // b)
    print("Float division", a / b)