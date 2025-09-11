
class Student:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name


student = Student('John', 22)
print(student.name)
student.name = 'John Doe'
print(student.name)

