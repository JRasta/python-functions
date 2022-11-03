"""
Inches to Feet

Create a function that accepts a measurement value in inches and
returns the equivalent of the measurement value in feet
"""

def inches_to_feet(num):
    ft = 0
    if num < 12:
        print(ft)
    else:
        ft = num / 12
        ft = int(ft)
        print(ft)


inches_to_feet(324)
inches_to_feet(12)
inches_to_feet(36)
inches_to_feet(10)
