class Customer:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

cust = Customer('Myriam', 123456)
print(cust)


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    """
    Works with print(object) and str(object), is informal and for end user. String representation
    """
    def __str__(self):
        cust_str = f"""
        Employee:
            name: {self.name}
            salary: {self.salary}
        """
        return cust_str

    """
    Works with repr() built-in func, is for formal use, mainly developers, reproducible representation, alterntive for
    print. Also works callin the instance of a class
    """
    def __repr__(self):
        return f"Employee('{self.name}', {self.salary})"


empl1 = Employee('Myriam', 3000)
print(empl1)    # use __str__
print(repr(empl1)) # use __repr__
empl1   # use __repr__