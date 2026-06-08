"""Problem: Build a small banking system."""

# Problem:
# Create accounts and support deposit and transfer.


class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            return False
        self.balance -= amount
        return True


class Bank:
    def transfer(self, sender, receiver, amount):
        if sender.withdraw(amount):
            receiver.deposit(amount)
            return "Transfer complete"
        return "Transfer failed"


# Solution:
account_one = Account("Moshiur", 1000)
account_two = Account("Nadia", 500)
bank = Bank()
print(bank.transfer(account_one, account_two, 300))
print(account_one.balance, account_two.balance)

# Logic:
# 1. Keep each account balance in its own object.
# 2. Withdraw from one account and deposit into another.
# 3. Return a clear transfer result.

# Explanation:
# This is a small real-world example of class collaboration.
