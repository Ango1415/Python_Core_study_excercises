# Parent class
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        self.balance -= amount

# Child class
class SavingsAccount(BankAccount):
    pass


# Constructor inherited from BankAcount
saving_acct = SavingsAccount(10000)
print(type(saving_acct))

# Attribute inherited from BankAccount
print(saving_acct.balance)

# Method inherited from BankAccount
saving_acct.withdraw(5000)
print(saving_acct.balance)


# isinstance excercise
bank_acct = BankAccount(3000)
print(isinstance(saving_acct, SavingsAccount))
print(isinstance(saving_acct, BankAccount))
print(isinstance(bank_acct, BankAccount))
print(isinstance(bank_acct, SavingsAccount))