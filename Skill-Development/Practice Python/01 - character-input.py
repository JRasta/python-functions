"""
Character Input

Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they will turn 100 years old
"""
import datetime


def year_count(name, age):
    get_year = datetime.datetime.now()
    get_year = int(get_year.strftime("%Y"))
    get_count = 100 - age
    set_year = get_year + get_count
    if age > 100:
        print(f"{name} you are already 100")
    else:
        print(f"{name}, you will be 100 in {set_year}")


year_count("Matt", 19)
year_count("Bob", 25)
year_count("Gina", 32)
year_count("Emily", 43)
year_count("Amy", 57)
year_count("Linda", 63)
year_count("Gemma", 72)
year_count("Kasia", 89)
year_count("Skunk", 93)
year_count("Roach", 102)
