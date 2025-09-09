"""
This an example of a basic class named Employee
"""

class Employee:
    MIN_SALARY = 30000  # This is a class attribute

    def __init__(self, name, salary):
        self.name = name

        if salary < Employee.MIN_SALARY:    # Use class name to access the class attribute.
            self.salary = Employee.MIN_SALARY
        else:
            self.salary = salary

    def give_rise(self, amount):
        self.salary += amount

    """
    This is an class method, doesn't require a instance-level 
    """
    @classmethod
    def from_file(cls, filename):
        with open(filename) as file:
            name = file.readline().strip()
            salary = int(file.readline().strip())
        return  cls(name, salary)

emp1 = Employee('Adam', 40000)
emp2 = Employee.from_file('employee.txt')
print(emp1.name)
print(emp2.name)