age = int(input("How old are you? "))
money = int(input("How much money do you have? "))
vip = input("Do you have a vip? ").lower()
if vip=="yes" or (age>=18 and money>=4500):
    print("You can buy a laptop")
else:
    print("You can't buy a laptop")