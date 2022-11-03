"""
Area of a Triangle

Write a function that takes the base and height of a triangle and return its area
"""

def tri_area(b, h):
    b = int(b)
    h = int(h)

    # area of triangle - (b * h) / 2
    triangle_area = (b * h) / 2
    print(f'Base:{b}, Height:{h}')
    print(f'Area of triangle is: {int(triangle_area)}\n')
    pass


tri_area(3, 2)
tri_area(7, 4)
tri_area(10, 10)
