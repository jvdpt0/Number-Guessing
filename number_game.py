import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == 'easy':
    attempts = 10
else:
    attempts = 5
correct = False
number = random.randint(1, 100)

while correct == False and attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Makes a guess: "))
    if guess == number:
        print(f"You got it! The answer was {number}")
        correct = True
    elif guess > number:
        print("Too high.")
        attempts -= 1
    elif guess < number:
        print("Too low.")
        attempts -= 1
if attempts == 0:
    print("You've run out of guesses, you lose.")
