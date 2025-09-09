# Parent class
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        self.balance -= amount

# Child class
class SavingsAccount(BankAccount):
    # Constructor of SavingAccount with additional argument
    def __init__(self, balance, interest_rate):
        # Call the parent constructor using ClassName.__init__()
        # self is a SavingAccount but also a BankAccount
        BankAccount.__init__(self, balance)
        # Add more functionality
        self.interest_rate = interest_rate

    # Add new functionality
    def compute_interest(self, n_periods=1):
        return self.balance * ((1 - self.interest_rate) ** n_periods - 1)


acct = SavingsAccount(10000, 0.03)
print(acct.interest_rate)
print('--------')


# Adding a second child class
class CheckingAccount(BankAccount):
    def __init__(self, balance, limit):
        BankAccount.__init__(self, balance)
        self.limit = limit

    # Overriding the Parents method
    def withdraw(self, amount, fee=0):
        if amount <= self.limit:
            BankAccount.withdraw(self, amount + fee)
        else:
            pass

    # Adding new functionality
    def deposit(self, amount):
        self.balance += amount

check_acct = CheckingAccount(10000, 25)
"""
Here comes the idea of LEGB rule in Python
"""
# Will call withdraw from ChekingAccount
check_acct.withdraw(200)
print(check_acct.balance)

# Will call withdraw from ChekingAccount
check_acct.withdraw(5000,15)
print(check_acct.balance)


bank_acct = BankAccount(50000)

bank_acct.withdraw(3000)
print(bank_acct.balance)
# bank_acct.withdraw(200, 50) # This throws an error
print(bank_acct.balance)