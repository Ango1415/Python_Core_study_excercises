class BalanceError(Exception):
    pass

class Customer:
    def __init__(self, name, balance):
        if balance < 0:
            raise BalanceError('Balance has to be non-negative!')
        else:
            self.name = name
            self.balance = balance

    def __repr__(self):
        return f"Customer({self.name}, {self.balance})"

try:
    cust = Customer('Myriam', -100)
except BalanceError as be:
    print(be)
    cust = Customer('Myriam', 0)
finally:
    print(cust)
