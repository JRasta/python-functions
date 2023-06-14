"""
Let's Fuel Up!

A vehicle needs 10 times the amount of fuel than the distance it travels.
However, it must always carry a minimum of 100 fuel before setting off.

Create a function which calculates the amount of fuel it needs, given the distance
"""

def calculate_fuel(d):
    fuel_needed = 10 * d

    if fuel_needed < 100:
        fuel_needed = 100

    print(int(fuel_needed))


calculate_fuel(15)
calculate_fuel(23.5)
calculate_fuel(3)
