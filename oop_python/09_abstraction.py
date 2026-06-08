"""Abstraction example."""

from abc import ABC, abstractmethod


class Payment(ABC):
    # Abstract class gives a common structure.
    @abstractmethod
    def pay(self, amount):
        # Child classes must implement this method.
        pass


class BkashPayment(Payment):
    def pay(self, amount):
        return f"Paid {amount} using bKash."


class CardPayment(Payment):
    def pay(self, amount):
        return f"Paid {amount} using card."


payments = [BkashPayment(), CardPayment()]

for payment in payments:
    print(payment.pay(500))
