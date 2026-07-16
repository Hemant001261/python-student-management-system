expenses=[]

while True:
    amount=float(input("Enter Expense: "))
    expenses.append(amount)

    ch=input("Add more? (y/n): ")

    if ch.lower()=="n":
        break

print("Total Expense =",sum(expenses))
