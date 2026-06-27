import csv
import matplotlib.pyplot as plt
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

def total_expense(self):
    total = sum(expense["amount"] for expense in self.expenses)
    print(f"\nTotal Expense: ₹{total}")

  def show_chart(self):
    if not self.expenses:
        print("No expenses to display.")
        return

    categories = []
    amounts = []

    for expense in self.expenses:
        categories.append(expense["category"])
        amounts.append(expense["amount"])

    plt.bar(categories, amounts)
    plt.xlabel("Category")
    plt.ylabel("Amount")
    plt.title("Expense Distribution")
    plt.show()
