""" Task
The provided code stub reads and integer, n, from STDIN.
For all non-negative integers i < n, print 1 squared.

Author: J. Smith
Date: September 2023
Lang: Pypy3
"""

if __name__ == '__main__':
    n_list= []
    n = int(input("Enter a number less than 20: "))

    if n <= 20:
        while n > 0:
            n -= 1
            n_list.append(n)

        n_list.reverse()
        for i in n_list:
            print(i * i)
