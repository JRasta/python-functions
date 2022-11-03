"""
Testing K^K == N?

Write a function that returns True if k^k == n for input (n, k) and return False otherwise
"""

def k_to_k(x, y):
    k = y ** y

    if x == k:
        print("True")
    else:
        print("False")


k_to_k(4, 2)
k_to_k(387420489, 9)
k_to_k(3124, 5)
k_to_k(17, 3)
