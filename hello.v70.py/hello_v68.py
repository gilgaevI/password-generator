password = input("Enter your password ")
if len(password) < 8:
    print("Weak password")
else:
    print("Strong password")