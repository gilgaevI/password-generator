money = int(input("How much money do you have? "))
vip = input("Do you have a vip? ")
if money>=5000 or (money>=4000 and vip=="Yes"):
    print("You can buy a phone ")
else:
    print("You can't buy a phone ")