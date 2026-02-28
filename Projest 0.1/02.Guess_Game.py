import random
def manin ():
    print("Welcome the guess the Number Game")
    secret = random.randint(1,100)
    attempts = 0

    while True:
        guess_str = input("Enter your guess (1-100) or 'quit' to exit: ").strip().lower()
        if guess_str == "quit":
            print("Bye!")
            break
        if not guess_str.isdigit():
            print("Invalid input. Please enter a number between 1 and 100 or 'quit' to exit.")
            continue
        guess = int(guess_str)
        attempts += 1

        if guess < secret:
            print("Too low! Try again.")
        elif guess > secret:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {secret} in {attempts} attempts!")
            break
if __name__ == "__main__":    manin()
