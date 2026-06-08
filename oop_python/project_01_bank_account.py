"""Simple project: bank account system."""


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # Keep balance private.

    @property
    def balance(self):
        # Read-only balance from outside the class.
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            return "Deposit amount must be positive."

        self.__balance += amount
        return f"Deposited {amount}. New balance: {self.__balance}"

    def withdraw(self, amount):
        if amount <= 0:
            return "Withdraw amount must be positive."

        if amount > self.__balance:
            return "Insufficient balance."

        self.__balance -= amount
        return f"Withdrew {amount}. New balance: {self.__balance}"

    def transfer(self, amount, receiver_account):
        if amount > self.__balance:
            return "Transfer failed. Insufficient balance."

        self.__balance -= amount
        receiver_account.deposit(amount)
        return f"Transferred {amount} to {receiver_account.owner}."

    def __str__(self):
        return f"{self.owner}'s account balance is {self.__balance}"


account_one = BankAccount("Moshiur", 1000)
account_two = BankAccount("Nadia", 500)

print(account_one.deposit(300))
print(account_one.withdraw(200))
print(account_one.transfer(400, account_two))
print(account_one)
print(account_two)
