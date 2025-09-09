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

emp1 = Employee('John', 40000)
print(emp1.MIN_SALARY)

emp2 = Employee('Jane', 60000)
print(emp2.MIN_SALARY)

# Update MIN_SALARY of emp1
emp1.MIN_SALARY = 50000
print(emp1.MIN_SALARY)
print(emp2.MIN_SALARY)
"""
Updating MIN_SALARY of an object will not affect the value in the class definition
"""