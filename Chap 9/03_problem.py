import random

def game():
    print("Welcome to the guessing game!")
    score = random.randint(1, 10)

    # Read old high score safely
    try:
        with open("high_score.txt", "r") as f:
            content = f.read().strip()
            high_score = int(content) if content else 0
    except FileNotFoundError:
        high_score = 0

    # Check & update
    if score > high_score:
        print("Congratulations! You have a new high score!")
        with open("high_score.txt", "w") as f:
            f.write(str(score))
    else:
        print(f"High score stays: {high_score}")

    print(f"Your score is: {score}")
    return score

if __name__ == "__main__":
    game()
