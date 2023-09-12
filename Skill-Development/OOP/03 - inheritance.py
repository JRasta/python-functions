# general OOP class
# super class
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # shows the Pet
    def show(self):
        print(f'I am {self.name} and I am {self.age} years old')

    # this is only used if same method is not available
    # within the inheriting classes
    def speak(self):
        print('I do not know what I say')

# inherits the class Pet
class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    # this over rides the upper class method
    def speak(self):
        print('Meow\n')

    # shows the Pet
    def show(self):
        print(f'I am {self.name} and I am {self.age} years old and I am {self.color}')

# inherits the class Pet
class Dog(Pet):
    # this over rides the upper class method
    def speak(self):
        print('Bark\n')

# inherits the class Pet
class Fish(Pet):
    pass


# create a generic pet
p = Pet('Tim', 19)
p.show()

# create a specific pets
c = Cat('Bill', 34, 'Brown')
d = Dog('Denver', 24)
f = Fish('Bubbles', 13)

# call specific pet methods
c.show()
c.speak()
d.show()
d.speak()
f.speak()
