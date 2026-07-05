numbers = []
biggest = 0
for i in range (5):
    number = int(input("Enter numbers: "))
    numbers.append (number)
    if number > biggest:
        biggest = number
print(biggest)