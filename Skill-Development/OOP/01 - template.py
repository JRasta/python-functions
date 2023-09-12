# Object Orientated Programming in Python

class Dog:
    # initialise class with reusable variables
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # method to get the variable from __init__
    def get_name(self):
        return self.name

    # method to get the variable from __init__
    def get_age(self):
        return self.age

    # method to update variable from __init__
    def set_name(self, name):
        self.name = name

    # method to update variable from __init__
    def set_age(self, age):
        self.age = age


# create an instance of Object Dog set as d
d = Dog('Timmy', 34)
print(d.get_name(), d.get_age())
d.set_age(20)
print(d.get_name(), d.get_age())
d.set_name('Dwight')
print(d.get_name(), d.get_age())
