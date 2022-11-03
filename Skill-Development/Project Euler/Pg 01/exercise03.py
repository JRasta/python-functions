"""
Largest Prime Factor

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""


def largest_prime_factor(num):
    num = int(num)
    i = 1

    while i <= num:
        c = 0
        if num % i == 0:
            j = 1
            while j <= i:
                if i % j == 0:
                    c = c + 1
                j = j + 1

            if c == 2:
                print(i)
        i = i + 1


largest_prime_factor(600851475143)
