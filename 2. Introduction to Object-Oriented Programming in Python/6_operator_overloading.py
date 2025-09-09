"""
Overloading methods - Object equality
"""
class Customer:
    def __init__(self, name, balance):
        self.name, self.balance = name, balance

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __eq__(self, other):
        is_name = self.name == other.name
        is_salary = self.salary == other.salary
        is_type = type(self) == type(other)
        return is_name and is_salary and is_type

customer1 = Customer('Myriam Azar', 3000)
customer2 = Customer('Myriam Azar', 3000)

# Check equality
print(customer1 == customer2)
print(customer1)
print(customer2)

list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(list1 == list2)

# Check equality
employee1 = Employee('Myriam Azar', 3000)
employee2 = Employee('Myriam Azar', 3000)
print(employee1 == employee2)
