"""
Sum of Polygon Angles

Given an n-sided regular polygon n, return the total sum of internal angles (in degrees)
"""

def sum_polygon(x):
    if x <= 2:
        print(f'{x}-sided polygon is invalid. A polygon must have at least 3 sides')
    else:
        sum_of_polygon = (x - 2) * 180
        print(f'{x}-sided polygon returns the sum of internal angles: {sum_of_polygon}')


sum_polygon(3)
sum_polygon(4)
sum_polygon(6)
sum_polygon(1)
sum_polygon(2)
