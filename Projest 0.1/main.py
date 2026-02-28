import random

# Simple Rock Paper Scissors game
# The user plays against the computer until they choose to quit.

OPTIONS = ["rock", "paper", "scissors"]


def get_computer_choice():
    return random.choice(OPTIONS)


def get_user_choice():
    choice = input("Choose rock, paper, or scissors (or 'quit' to exit): ").strip().lower()
    while choice not in OPTIONS and choice != "quit":
        choice = input("Invalid choice. Please enter rock, paper, scissors, or quit: ").strip().lower()
    return choice


def determine_winner(user, computer):
    if user == computer:
        return "tie"
    # rock beats scissors, scissors beats paper, paper beats rock
    wins = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock",
    }
    if wins[user] == computer:
        return "user"
    else:
        return "computer"


def main():
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        user_choice = get_user_choice()
        if user_choice == "quit":
            print("Thanks for playing!")
            break

        computer_choice = get_computer_choice()
        print(f"Computer chose {computer_choice}.")

        result = determine_winner(user_choice, computer_choice)
        if result == "tie":
            print("It's a tie!")
        elif result == "user":
            print("You win!")
        else:
            print("Computer wins!")
        print()


if __name__ == "__main__":
    main()