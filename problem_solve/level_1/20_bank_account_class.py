"""Problem: Create a basic bank account class."""

# Problem:
# Make a class that can deposit and withdraw money.


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited {amount}. Balance: {self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient balance."
        self.balance -= amount
        return f"Withdrew {amount}. Balance: {self.balance}"

    def show_account(self):
        return f"{self.owner} has balance {self.balance}"


# Solution:
account = BankAccount("Moshiur", 1000)
print(account.deposit(500))
print(account.withdraw(300))
print(account.show_account())

# Logic:
# 1. Store account data inside a class.
# 2. Use methods for deposit and withdraw.
# 3. Keep the balance updated in the object.

# Explanation:
# This is a tiny real-world example of OOP in action.
