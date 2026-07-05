numbers = []
for i in range (5):
    number = int(input("Enter numbers: "))
    numbers.append (number)
smallest = numbers[0]
for number in numbers:
    if number < smallest:
        smallest = numbers 
print(smallest)