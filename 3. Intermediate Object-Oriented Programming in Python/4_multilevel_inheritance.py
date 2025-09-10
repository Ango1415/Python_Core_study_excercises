class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Hello, my name is {self.name}")

class Employee(Person):
    def __init__(self, name, title):
        Person.__init__(self, name)
        self.title = title

    def change_position(self, new_title):
        print(f"Starting new role as {new_title}")
        self.title = new_title

class Manager(Employee):
    def __init__(self, name, title, number_reports):
        Employee.__init__(self, name, title)
        self.number_reports = number_reports


mike = Manager("Mike", "Engineering Manager", 14)
mike.introduce()
mike.change_position('Director of Engineering')
print(mike.number_reports)
print(Manager.mro())