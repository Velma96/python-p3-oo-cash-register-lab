#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0.0
        self.items = []
        self.last_transaction_amount = 0.0

    def add_item(self, title, price, quantity=1):
        """Adds an item and updates total price."""
        self.total += price * quantity
        self.items.extend([title] * quantity)
        self.last_transaction_amount = price * quantity

    def apply_discount(self):
        """Applies discount if available, otherwise prints an error message."""
        if self.discount > 0:
           self.total -= self.total * (self.discount / 100)
           self.total = round(self.total, 2)  # Round for accuracy
           formatted_total = int(self.total) if self.total.is_integer() else self.total
           print(f"After the discount, the total comes to ${formatted_total}.")
        else:
           print("There is no discount to apply.")

    def void_last_transaction(self):
        """Removes the last added transaction from the total."""
        self.total -= self.last_transaction_amount
        self.total = max(self.total, 0)  

