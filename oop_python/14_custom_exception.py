"""Custom exception example."""


class InsufficientBalanceError(Exception):
    # Custom exception makes the error meaning clear.
    pass


class Wallet:
    def __init__(self, balance):
        self.balance = balance

    def spend(self, amount):
        if amount > self.balance:
            raise InsufficientBalanceError("Not enough money in wallet.")
        self.balance -= amount
        return self.balance


wallet = Wallet(300)

try:
    print(wallet.spend(500))
except InsufficientBalanceError as error:
    print(error)
