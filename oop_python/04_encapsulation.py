"""Encapsulation example."""


class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner  # Public attribute.
        self._account_type = "Savings"  # Protected by convention.
        self.__balance = balance  # Private name-mangled attribute.

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        # Private data is accessed through methods.
        return self.__balance


account = BankAccount("Moshiur", 1000)
account.deposit(500)

print(account.owner)
print(account._account_type)
print(account.get_balance())
