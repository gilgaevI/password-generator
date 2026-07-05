age = int(input("How old are you? "))
ticket = input("Do you have a ticket? ")
vip = input("Do you have a vip? ")
if vip=="Yes" or (age>=18 and ticket=="Yes"):
    print("Access granted")
else:
    print("Access denied")