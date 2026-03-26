# Q12. Create a number guessing game.
import random
print("Welcome to Number Guessing Game!")
print("I have picked a number between 1 to 100: ")
num = random.randint(1,100) #81
guessed = False
count = 0
while not guessed:
    guess = int(input("Enter your guess: "))
    if guess < num:
        print(f"More than {guess}")
        count = count + 1
    elif guess > num:
        print(f"Less than {guess}")
        count = count + 1
    else:
        count = count + 1
        print(f"🎉 Correct! You guessed it in {count} attempts!")
        guessed = True
