password = input("Enter your password ")
if "@" in password and len(password) >= 8:
    print("Valid")
else:
    print("Invalid")   