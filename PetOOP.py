class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name}. I am {self.age} years old")

    def speak(self):
        print(f"I am {self.name} and I don't know what to say")


class Cat(Pet):  # Including and Inheriting from a parent or super class
    def __init__(self, name, age, color):
        # instead of re-assigning the name and age properties, since these have already been inherited from the Pet
        # class, you can just call the Super class (Pet) init to initialize and inherit the properties and assignments
        super().__init__(name, age)
        self.color = color  # color property doesn't exist on the super class, so you can initialize

    def speak(self):
        print("I meow")

    def show(self):
        print(f"I am {self.name}, I am {self.age} years old and I am {self.color}")


class Dog(Pet):
    def speak(self):
        print("I bark")
