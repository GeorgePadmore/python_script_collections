# Introducing class methods
class Person:
    person_count = 0

    def __init__(self, name):
        self.name = name
        Person.add_person()

    def show(self):
        print(f"Person: {self.name}\n")

    @classmethod
    def number_of_people(cls):
        return cls.person_count

    @classmethod
    def add_person(cls):
        cls.person_count += 1
