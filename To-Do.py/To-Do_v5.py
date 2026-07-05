tasks = []
while True:
    print("---------------------")
    print("1 - Add task ")
    print("2 - Show tasks ")
    print("3 - Delete task ")
    print("4 - Exit ")
    print("---------------------")
    choice = int(input("Choose "))
    if choice == 1:
        task = input("Enter task ")
        tasks.append(task)
    elif choice == 2:
        if not tasks:
            print("You don't have any tasks")
        else:
            for i in range(len(tasks)):
                print("---------------------")
                print(i + 1,"-",tasks[i])
    elif choice == 3:
        if not tasks:
            print("You don't have any tasks to delete")
        else:
            number = int(input("Delete task: "))
            if 1 <= number <= len(tasks):
                tasks.pop(number - 1)
            else:
                print("Invalid task number")
    elif choice == 4:
        break