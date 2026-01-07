class Category:
    def __init__(self, name) :
        self.name = name
        self.ledger = []

    def deposit(self, amount, description = '') :
        transaction = {'amount' : amount, 'description': description}
        self.ledger.append(transaction)

    def withdraw(self, amount, description = '') :
        if amount <= self.get_balance() :
            withdrawal = {'amount': -amount, 'description': description}
            self.ledger.append(withdrawal)
            return True
        return False

    def get_balance(self) :
        total = 0
        for item in self.ledger :
            total += item['amount']
        return total
    
    def transfer(self, amount, other) :
        if amount <= self.get_balance() :
            self.withdraw(amount, f"Transfer to {other.name}")
            other.deposit(amount, f"Transfer from {self.name}")
            return True
        return False
    
    def check_funds(self, amount) :
        if amount > self.get_balance() :
            return False
        return True

    def __str__(self) :
        output = self.name.center(30,"*") + '\n'

        for item in self.ledger :
            desc = item['description'][:23].ljust(23)
            amt = f"{item['amount']:.2f}".rjust(7)
            output += desc + amt + '\n'
        output += f"Total: {self.get_balance()}"
        return output


def create_spend_chart(categories):
    # Title
    chart = "Percentage spent by category\n"

    # Calculate withdrawals per category
    spending = []
    for category in categories:
        total = sum(-item["amount"] for item in category.ledger if item["amount"] < 0)
        spending.append(total)

    total_spent = sum(spending)

    # Calculate percentages, rounded down to nearest 10
    percentages = [(int((amount / total_spent) * 100) // 10) * 10 for amount in spending]

    # Build the bars from 100 down to 0
    for level in range(100, -1, -10):
        chart += str(level).rjust(3) + "| "
        for percent in percentages:
            chart += "o  " if percent >= level else "   "
        chart += "\n"

    # Horizontal line (3 dashes per category + 1 extra)
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # Vertical category names
    max_len = max(len(cat.name) for cat in categories)
    for i in range(max_len):
        chart += "     "
        for cat in categories:
            if i < len(cat.name):
                chart += cat.name[i] + "  "
            else:
                chart += "   "
        chart += "\n"

    # Remove final newline 
    return chart.rstrip("\n")

food = Category("Food")
clothing = Category("Clothing")
auto = Category("Auto")

food.deposit(1000, "Initial deposit")
clothing.deposit(500, "Paycheck")
auto.deposit(200, "Car savings")

food.withdraw(105.55, "Groceries")
food.withdraw(15.89, "Snacks")
clothing.withdraw(33.40, "Jeans")
auto.withdraw(10, "Fuel")

food.transfer(50, clothing)  # Transfer $50 from Food → Clothing

print("Food balance:", food.get_balance())
print("Clothing balance:", clothing.get_balance())
print("Auto balance:", auto.get_balance())

print("\nFood ledger:")
print(food)

print("\nClothing ledger:")
print(clothing)

print("\nAuto ledger:")
print(auto)

print(create_spend_chart([food, clothing, auto]))



        
        
