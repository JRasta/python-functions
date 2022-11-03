"""
Largest Palindrome product

A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


def largest_palindrome_product():
    start_range = 100
    end_range = 1000

    while start_range < end_range:
        total = start_range * end_range
        status = isPalindrome(str(total))
        if status:
            print(total)
        start_range += 1


def isPalindrome(number):
    if number[0] == number[-1] and number[1] == number[-2] and number[2] == number[-3]:
        return True
    else:
        return False


largest_palindrome_product()
