class Transaction:
    def __init__(self, amount, tag, merchant, id=None):
        self.amount = amount
        self.tag = tag
        self.merchant = merchant
        self.id = id


def total_spent(transactions):
    total_spent = 0
    for transaction in transactions:
        total_spent += transaction.amount
    return total_spent
