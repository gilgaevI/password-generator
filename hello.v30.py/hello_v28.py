secret = 457
guess = int(input("Guess the number "))
while guess != secret:
    if guess > secret:
        guess = int(input("Too high "))
    else:
        guess = int(input("Too low "))
print("You win!")