number = int(input("Enter your number "))
count = 0
while number!= 0:
    if number % 2== 0:
        count += 1
    number = int(input("Enter your number "))
print(count, "Even numbers ")