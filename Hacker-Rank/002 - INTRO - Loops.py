"""
The provided code stub reads and integer, n, from STDIN.
For all non-negative integers i < n, print i ** 2.
"""

if __name__ == '__main__':
    n = o = int(input())

    nums = list(range(n, -1, -1))
    nums.remove(o)
    nums.reverse()

    for i in nums:
        squared_val = i ** 2
        print(squared_val)
