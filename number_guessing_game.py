import random


def number_guessing_game():
    random_number = random.randint(1, 100)
    max_attempts = 7

    print("Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between 1 and 100. You have {max_attempts} attempts.")

    for attempt in range(1, max_attempts + 1):
        guess = int(input(f"\nAttempt {attempt}/{max_attempts} - Enter your guess: "))

        if guess < random_number:
            print("Too low!")
        elif guess > random_number:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed it in {attempt} attempt(s)!")
            break
    else:
        print(f"\nSorry, you've used all {max_attempts} attempts. The correct number was {random_number}.")


number_guessing_game()
