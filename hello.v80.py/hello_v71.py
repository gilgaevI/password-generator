email = input("Email: ")
password = input ("Enter your password ")
if "@" in email and "." in email:
    if len(password) >= 8:
        print("Registration succesful")
    else:
        print("Registration failed")
else:
    print("Registration failed")