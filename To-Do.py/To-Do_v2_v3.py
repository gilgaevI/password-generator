tasks = []
for i in range(3):
    task = input("Enter task: ")
    tasks.append(task)
for i in range(len(tasks)):
    print(i + 1, tasks[i])