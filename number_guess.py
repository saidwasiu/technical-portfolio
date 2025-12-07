import random

print("\n🎯 Number Guessing Game")
print("I'm thinking of a number between 1 and 100.")

number = random.randint(1, 100)
guess = None

while guess != number:
    try:
        guess = int(input("Enter your guess: "))

        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print(f"✅ Congratulations! You guessed the number: {number}")

    except ValueError:
        print("⚠️ Please enter a valid number.")
