import csv
class ExpenseManager:
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount, category):
    expense = {
        "amount": amount,
        "category": category
    }
    self.expenses.append(expense)

    with open("expenses.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([amount, category])

    print("Expense added successfully and saved!")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded.")
            return

        print("\nExpenses:")
        for expense in self.expenses:
            print(f"Amount: ₹{expense['amount']} | Category: {expense['category']}")
