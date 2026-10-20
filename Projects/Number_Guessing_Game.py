import random

attempts = 5

def rule_list():
    print("*****Welcome to Number Guessing Game*****\n")
    print("Guess number between 1 to 100.")
    print("You have Only 5 attempts for guessing the correct number!\n")

def play(number, attempt = 1):
    if attempt > attempts:
        print("\nGAME OVER")
        print("The correct number was: ", number)
        return

    guess = input(f"Attempt {attempts}/7 - Enter your guess-")
    try:
        guess = int(guess)
    except ValueError:
        print("Enter a valid number")
        return play(number, attempt)

    if guess < 1 or guess > 100:
        print("Please enter a number between 1 to 100")
        return play(number, attempt)

    check_guess = lambda x, y : "correct" if x == y else(
        "low" if x < y else "high"

    )

    result = check_guess(guess, number)

    if result == guess:
        print("CONGRATULATIONS!!! You gussed the correct number!")
        print("Your gussed number{number} : Number of attempt{attempt}")
        return

    if result == "low":
        print("Too Low! try a higher number\n")
    else:
        print("Too High! try a lower number\n")

        play(number, attempt + 1)

    
