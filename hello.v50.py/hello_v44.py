numbers = []
count = 0
for i in range (5):
    number = int(input("Enter your number "))
    numbers.append (number)
    if number % 2 == 0:
        count += 1
print(count)