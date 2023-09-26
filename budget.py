class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, budget_category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {budget_category.category}")
            budget_category.deposit(amount, f"Transfer from {self.category}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = f"{self.category:*^30}\n"
        items = ""
        total = 0
        for item in self.ledger:
            description = item["description"][:23]
            amount = "{:.2f}".format(item["amount"])
            items += f"{description}{' '*(30-len(description)-len(amount))}{amount}\n"
            total += item["amount"]
        output = title + items + "Total: {:.2f}".format(total)
        return output


def create_spend_chart(categories):
    chart = "Percentage spent by category\n"
    spent = [(c.get_balance() / sum(item["amount"] for item in c.ledger)) * 100 for c in categories]
    for i in range(100, -1, -10):
        chart += str(i).rjust(3) + "| "
        for s in spent:
            chart += "o" if s >= i else " "
            chart += "  "
        chart += "\n"
    chart += "    ----------\n     "
    max_len = max(len(c.category) for c in categories)
    for i in range(max_len):
        for c in categories:
            chart += c.category[i] if i < len(c.category) else " "
            chart += "  "
        if i < max_len - 1:
            chart += "\n     "
    return chart
