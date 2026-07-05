number = int(input("Enter number "))
smallest = number
while number!= 0:
    smallest = number
    if number < smallest:
        smallest = number
    number = int(input("Enter number "))
print("The smallest number is: ", smallest)