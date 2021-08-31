class Category:
    def __init__(self, name): 
        self.name = name
        self.ledger = []
        self.balance = 0

    def deposit(self, amount, description=''):
        self.balance += amount
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.balance -= amount
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return self.balance

    def transfer(self, amount, budget):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {budget.name}")
            budget.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return self.balance >= amount

    def __repr__(self):
        header = f'{self.name:*^30}'
        operations = (
            f'{item["description"][:23]: <23}{float(item["amount"]): >7.2f}'
            for item in self.ledger
        )
        footer = f'Total: {float(self.balance):.2f}'
        return "\n".join([header, *operations, footer])
    
import math

def normalize_names(categories):
    max = 0
    for category in categories:
        if max < len(category.name):
            max = len(category.name)
    return (f'{category.name: <{max}}' for category in categories)

def o_bar_generator(amount, total):
    ratio = amount / total
    return ('o' * ((math.floor(ratio * 10)) + 1)).rjust(11)

def create_spend_chart(categories):
    total = 0
    amount_withdraw = []
    
    for category in categories:
        withdraw = 0
        for operation in category.ledger:
            if operation["amount"] < 0:
                withdraw += operation["amount"]
                
        amount_withdraw.append(withdraw)
        total += withdraw
        
    category_o_bar = (o_bar_generator(amount, total) for amount in amount_withdraw)
    
    y_axis = ["100|", " 90|", " 80|", " 70|", " 60|", " 50|", " 40|", " 30|", " 20|", " 10|", "  0|"]
    
    header = "Percentage spent by category"
    table = (
        f"{line[0]} {'  '.join(line[1:])}  "
        for line in zip(y_axis, *category_o_bar)
    )
    
    separator = f"    {('-' * ( 3 * len(categories) + 1))}"
    names = (
        f"     {'  '.join(line)}  "
        for line in zip(*normalize_names(categories))
    )

    return "\n".join((header, *table, separator, *names))
