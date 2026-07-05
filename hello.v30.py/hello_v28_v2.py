secret = 457
attempts = 3
guess = int(input("Guess the number "))
while attempts>0 and guess!= secret:
    if guess > secret:
        attempts -= 1
        guess = int(input("Too high "))
    else:
        guess = int(input("Too low "))
        attempts -= 1

if guess == secret:
    print("You win!")
else:
     print("Game over")