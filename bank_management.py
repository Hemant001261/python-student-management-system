accounts = {}

while True:
    print("\n===== BANK MANAGEMENT SYSTEM =====")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Account Holder Name: ")
        acc = input("Enter Account Number: ")
        balance = float(input("Enter Initial Deposit: "))
        accounts[acc] = {"name": name, "balance": balance}
        print("✅ Account Created Successfully!")

    elif choice == "2":
        acc = input("Enter Account Number: ")
        if acc in accounts:
            amount = float(input("Enter Deposit Amount: "))
            accounts[acc]["balance"] += amount
            print("✅ Deposit Successful!")
        else:
            print("❌ Account Not Found!")

    elif choice == "3":
        acc = input("Enter Account Number: ")
        if acc in accounts:
            amount = float(input("Enter Withdraw Amount: "))
            if accounts[acc]["balance"] >= amount:
                accounts[acc]["balance"] -= amount
                print("✅ Withdrawal Successful!")
            else:
                print("❌ Insufficient Balance!")
        else:
            print("❌ Account Not Found!")

    elif choice == "4":
        acc = input("Enter Account Number: ")
        if acc in accounts:
            print("Account Holder:", accounts[acc]["name"])
            print("Balance:", accounts[acc]["balance"])
        else:
            print("❌ Account Not Found!")

    elif choice == "5":
        print("Thank You for Using Bank Management System!")
        break

    else:
        print("❌ Invalid Choice!")
