task = input("Enter your task: ")
file = open ("tasks.txt", "w")
file.write(task)
file.close()