class ExpenseManager:
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount, category):
        expense = {
            "amount": amount,
            "category": category
        }
        self.expenses.append(expense)
        print("Expense added successfully!")
