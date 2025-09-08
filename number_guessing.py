import random
print("Welcome to the Number Guessing Game!")
print("I have chosen a number between 1 and 100. Can you guess it?")

low = 1
high = 100
secret_number = random.randint(low, high)
attempts = 0

while True:
    raw = input(f"Enter your guess ({low}-{high}): ")
    try:
        guess = int(raw)
    except ValueError:
        print("Please enter a whole number (e.g., 42).")
        continue

    if not low <= guess <= high:
        print(f"Please enter a number between {low} and {high}.")
        continue

    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"🎉 Congratulations! You guessed the number correctly in {attempts} attempts!")
        break



