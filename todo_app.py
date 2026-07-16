tasks=[]

while True:
    print("1.Add Task")
    print("2.View Tasks")
    print("3.Exit")

    ch=input("Choice:")

    if ch=="1":
        task=input("Enter Task:")
        tasks.append(task)

    elif ch=="2":
        for t in tasks:
            print("-",t)

    elif ch=="3":
        break
