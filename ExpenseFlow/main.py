from expense_manager import ExpenseManager

def main():
    manager = ExpenseManager()

    while True:
        print("\n===== ExpenseFlow Menu =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Total Expense")
        print("4. Show Chart")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            manager.add_expense(amount, category)

        elif choice == "2":
            print(manager.expenses)

        elif choice == "3":
    manager.total_expense()

     elif choice == "4":
    manager.show_chart()

elif choice == "5":
    print("Exiting ExpenseFlow...")
    break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
