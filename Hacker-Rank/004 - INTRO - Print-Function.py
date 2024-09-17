"""
The included code stub will read an integer, n, from STDIN.

Without using any string methods, try to print the following:
123...n
Note that "..." represents the consecutive values in between.
"""

if __name__ == '__main__':
    n = int(input())
    lst = []

    nums = range(n)
    for i in nums:
        lst.append(str(i+1))
    print("".join(lst))
