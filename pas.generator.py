import random
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
letters = ["A", "v", "P", "b", "T"]
symbols = ["!", "$", "@", "?", "#"]
all_symbols = numbers + letters + symbols
while True:
    print("----------------------")
    print("1 - Generate password")
    print("2 - Exit")
    print("----------------------")
    choice = int(input("Choose: "))
    if choice == 1:
        password = ""
        length = int(input("The password length: "))
        for i in range(length):
            elements = random.choice(all_symbols)
            password = password + elements
        print("Generated password is:", password)
    elif choice == 2:
        break