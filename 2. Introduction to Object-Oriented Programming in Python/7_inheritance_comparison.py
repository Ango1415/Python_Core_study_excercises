
class BankAccount:
    def __init__(self, number, balance=0):
        self.balance = balance
        self.number = number

    def withdraw(self, amount):
        self.balance -= amount

    def __eq__(self, other):
        print("BankAccount __eq__() called")
        return self.number == other.number

# W define excactly the same both eq methods to see how of them is called first
class SavingsAccount(BankAccount):
    def __init__(self, number, balance, interest_rate):
        BankAccount.__init__(self, number, balance)
        self.interest_rate = interest_rate

    # Define __eq__ that returns True if the number attributes are equal
    def __eq__(self, other):
        print("SavingsAccount __eq__() called")
        return self.number == other.number


ba = BankAccount(123, 10000)
sa = SavingsAccount(123, 2000, 0.05)
# Compare the two objects
print(ba == sa)
print(sa == ba)