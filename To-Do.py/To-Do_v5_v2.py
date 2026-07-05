file = open("tasks.txt", "r")
text = file.read()
file.close()
if not text:
    tasks = []
else:
    tasks = text.split("\n")
while True:
    print("---------------------")
    print("1 - Add task ")
    print("2 - Show tasks ")
    print("3 - Delete tasks ")
    print("4 - Exit ")
    print("---------------------")
    choice = int(input("Choose "))
    if choice == 1:
        task = input("Enter task:\n ")
        file = open("tasks.txt", "a")
        file.write(task + "\n")
        file.close()
        tasks.append(task)
    elif choice == 2:
        if not tasks:
            print("You don't have any tasks")
        else:
            for i in range(len(tasks)):
                print(i + 1, tasks[i])
    elif choice == 3:
        if not tasks:
            print("You don't have any tasks to delete ")
        else:
            number = int(input("Delete task: "))
            if 1 <= number <= len(tasks):
                tasks.pop(number - 1)
                file = open("tasks.txt", "w")
                file.write("\n".join(tasks))
                file.close()
            else:
                print("Wrong number ")
    elif choice == 4:
        break