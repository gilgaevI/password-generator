numbers = []
for i in range (5):
    number = int(input("Enter your number "))
    numbers.append (number)
biggest = numbers[0]
for number in numbers:
    if number % 2 != 0 and number > biggest:
        biggest = number   
print(biggest)