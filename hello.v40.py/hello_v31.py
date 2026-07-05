secret = 7989
guess = int(input("What is your password?:"))
while guess!= secret:
    guess = int(input("Wrong password, try again:"))
print("Access granted")