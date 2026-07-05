number = int(input("Enter number "))
total = 0
count = 0
average = 0
while number!=0:
    total += number
    count += 1
    number = int(input("Enter number" ))
average = total / count
print("average number is", average)