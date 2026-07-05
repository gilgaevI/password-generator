biggest = 0
numbers = [2, 5, 8, 1, 4]
for number in numbers:
    if number % 2 == 0 and number > biggest:
        biggest = number
print(biggest)