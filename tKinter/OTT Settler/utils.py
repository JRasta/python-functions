"""
Types of bets currently within the UK markets
"""

# Single
def single(o):
    if o == "lose":
        return 0
    else:
        x, y = o.split("/")
        odd = int(x) / int(y)
        odd += 1
        return odd
