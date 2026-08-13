
expenses = {}

while True:
    print("===== EXPENSE TRACKER =====")
    print("1. Add expense\n2. View expenses\n3. Show total\n4. Exit\n")
    option = int(input("Choose an option: "))
    if option == 1:
        category = input("\nEnter category: ")
        amount = float(input("Enter amount:"))
        expenses[category] = amount
        print("\nExpense added!\n")
    elif option == 2:
        print("\nYour expenses: \n",expenses)
    elif option == 3:
        expenses = sum(expenses.values())
        print("\nTotal spent: ",expenses)
    elif option == 4:
        print("\nGoodbye")
        break
    else:
        print("\nInvalid choice!")
