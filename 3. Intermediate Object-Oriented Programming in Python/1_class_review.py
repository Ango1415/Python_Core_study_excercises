class Person:
    residence = "Planet Earth"  # Class attributes, accessed without an instance

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hello, my name is {self.name}")

    @classmethod
    def wake_up(cls):
        print("Time to start you day!")

    # Overloading
    def __eq__(self, other):
        return self.name == other.name

class Employee(Person):

    def __init__(self, name, age, title):
        Person.__init__(self, name, age)
        self.title = title

    def change_position(self, new_title):
        self.title = new_title

    # Overriding
    def introduce(self):
        print(f"My name is {self.name}, and I am a {self.title}")

class Customer(Person):

    def __init__(self, name, age, balance):
        super().__init__(name, age)     # We can use super() without self
        self.balance = balance
