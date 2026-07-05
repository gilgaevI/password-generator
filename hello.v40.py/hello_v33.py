biggest = 0
number = int(input("Enter number "))
while number!= 0:
    if number > biggest:
        biggest = number
    number = int(input("Enter number "))
print("The biggest number is: ", biggest)