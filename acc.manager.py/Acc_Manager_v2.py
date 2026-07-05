import json
file = open("acc_manager.json", "r")
text = json.load(file)
file.close()
if not text:
    info = []
    file = open("acc_manager.json", "w")
    json.dump(info, file)
    file.close()
else:
    info = text
while True:
    print("--------------------")
    print("1 - Add account ")
    print("2 - Show accounts ")
    print("3 - Delete account ")
    print("4 - Exit ")
    print("--------------------")
    choice = int(input("Choose: "))
    if choice == 1:
        website = input("Website: ")
        login = input("Login: ")
        password = input("Password: ")
        data = {
                "website": website,
                "login": login,
                "password": password,
            }
        info.append(data)
        file = open("acc_manager.json", "w")
        json.dump(info, file)
        file.close()
    elif choice == 2:
        if not info:
            print("You don't have any acoounts")
        else:
            print("-------------------")
            for i in range(len(info)):
                print("Account", i + 1)
                print("Website:", info[i]["website"])
                print("Login:", info[i]["login"])
                print("Password:", info[i]["password"])
                print("-------------------")
    elif choice == 3:
        if not info:
            print("You don't have any accounts to delete")
        else:
            number = int(input("Delete account number: "))
            if 1 <= number <= len(info):
                info.pop(number - 1)
                file = open("acc_manager.json", "w")
                json.dump(info, file)
                file.close()
            else:
                print("invalid tusk number")
    elif choice == 4:
        break