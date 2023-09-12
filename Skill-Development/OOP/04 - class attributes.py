class Person:

    # class attribute
    number_of_people = 0

    def __init__(self, name):
        self.name = name

        # call class method
        Person.add_person()

    # class specific method
    @classmethod
    def num_of_ppl(cls):
        return cls.number_of_people

    # class specific method
    @classmethod
    def add_person(cls):
        cls.number_of_people += 1


# create person
p1 = Person('Tim')
print(Person.num_of_ppl())
p2 = Person('Jill')
print(Person.num_of_ppl())
