numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
import random
password = ""
for i in range(5):
    number = random.choice(numbers)
    password = password + number
print(password)