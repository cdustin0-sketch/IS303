from decimal import Decimal
import secrets


class BankAccount:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.account_number = secrets.randbelow(90000) + 10000
        self.balance = Decimal("0.00")

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("The deposit amount must be greater than zero.")

        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("The withdrawal amount must be greater than zero.")

        if amount > self.balance:
            return False

        self.balance -= amount
        return True

    def display_information(self):
        print(f"\nName: {self.customer_name}")
        print(f"Account #: {self.account_number}")
        print(f"Balance: ${self.balance:.2f}")