tasks = ["Learn python", "read book", "go to sleep"]
for i in range(len(tasks)):
    print(i + 1, tasks[i])
number = int(input("Delete task: "))
tasks.pop(number - 1)
for i in range(len(tasks)):
    print(i + 1, tasks[i])