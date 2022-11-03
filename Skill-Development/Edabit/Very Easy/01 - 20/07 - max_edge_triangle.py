"""
Maximum Edge of a Triangle

Create a function that finds the maximum range of a triangle's third edge, where the side lengths are all integers
"""

def next_edge(x, y):
    x = int(x)
    y = int(y)

    edge = (x + y) - 1
    print(f'Edge1:{x} & Edge2:{y} = Edge3:{edge}')


next_edge(8, 10)
next_edge(5, 7)
next_edge(9, 2)
